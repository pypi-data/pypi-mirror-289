import logging
from typing import Type

import openai
from openai.types.chat.chat_completion import ChatCompletion
from pydantic import BaseModel, ValidationError

from .tools import BaseTool, ToolUsageError
from .types.chat_messages import ToolCall
from .utils import get_tool_schema, track_recursion_depth


class Agent:
    class AgentError(Exception):
        pass

    def __init__(
        self,
        api_key,
        system_message: str,
        logger=None,
        llm_params=None,
    ) -> None:
        self._init_logger()

        self.system_message = system_message

        self._recursion_depth = 0
        self._max_recursion_depth = 10

        default_llm_params = dict(
            model="gpt-4o",
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # merge the default params with the initialized params
        self.llm_params = default_llm_params | (llm_params or {})

        self.messages = [
            {"role": "system", "content": self.system_message},
        ]

        self.llm_client = self._init_llm_client(api_key)
        self.logger = self._init_logger(logger)

        self.tools = []
        self._responses = []

    def _init_llm_client(
        self,
        api_key,
    ):
        """
        Initialize the LLM client.

        Parameters
        ----------
        api_key : str
            The API key for the LLM

        Returns
        -------
        openai.Client
        """
        llm_client = openai.Client(api_key=api_key)
        return llm_client

    def _init_logger(
        self,
        logger=None,
    ) -> logging.Logger:
        if logger is not None:
            return logger
        else:
            return logging.getLogger(__name__)

    def _get_tool_call_secret_kwargs(self, tool_call: ToolCall) -> dict:
        """
        Get the secret kwargs for the tool call.
        Made to be overridden by the child class.

        Parameters
        ----------
        tool_call : ToolCall
            The openai tool call object
        """
        secret_kwargs = {"self": self, "tool_call": tool_call}
        return secret_kwargs

    def _get_tool_class(
        self,
        tool_name: str,
    ) -> BaseTool:
        """
        Get the tool class by name. Does some checks to make sure the tool is unique.

        Parameters
        ----------
        tool_name : str
            The name of the tool to get

        Returns
        -------
        BaseTool
            The tool class that matches the name
        """
        # Find the tool we want to call
        tool_classes = [
            tool_cls for tool_cls in self.tools if tool_cls.get_name() == tool_name
        ]

        if len(tool_classes) == 0:
            raise ValueError(f"Requested tool {tool_name} not found.")

        assert (
            len(tool_classes) == 1
        ), f"Multiple tools with the same name {tool_name} found."

        tool_class = tool_classes[0]

        return tool_class

    def _handle_tool_calls(
        self,
        response: ChatCompletion,
    ) -> None | ChatCompletion:
        """
        Handle tool calls by running the tool and adding the result to the messages

        Parameters
        ----------
        response : openai.resources.completions.Completion
            Response from the chat completion

        Returns
        -------
        None | openai.resources.completions.Completion
            If the last tool call specifies stop_chain_after=True, return None.
            Otherwise, return the next chat completion response.
        """

        self.logger.info("Handling tool calls...")

        content = response.choices[0].message.content
        tool_calls = response.choices[0].message.tool_calls

        # add the tools request to the messages
        self.add_assistant_message(content=content, tool_calls=tool_calls)

        # if we get at least one ToolUsageError, we will have to trigger
        # another complete_chat to get the final tool output message
        # here we keep track of the tool calls ids that require a retry
        errors_reqing_retry = []

        # keep track of which tools want to stop the chain
        # hopefully they all agree on this
        # if not, we default to True - and stop the chain
        stop_chain_after = {}

        for tool_call in tool_calls:
            func_name = tool_call.function.name

            self.logger.info(f"Calling tool function: {func_name}")

            secret_kwargs = self._get_tool_call_secret_kwargs(tool_call)

            tool_class = self._get_tool_class(func_name)

            # Keep track of which tools want to stop the chain
            stop_chain_after[tool_call.id] = tool_class.stop_chain_after()

            try:
                # strict=False => control characters (\t, \n, \r) will be allowed inside strings
                tool_instance = tool_class.model_validate_json(
                    tool_call.function.arguments, strict=False
                )

                try:
                    tool_output = tool_instance.function(secret_kwargs)
                    add_output = tool_instance.add_output_to_messages_after()
                except ToolUsageError as tool_usage_error:
                    tool_output = str(tool_usage_error)
                    self.logger.warning(f"Tool Usage Error: {tool_output}")
                    errors_reqing_retry.append(tool_call.id)
                    add_output = True

            except ValidationError as validation_error:
                tool_output = str(validation_error)
                self.logger.error(f"Validation Error: {tool_output}")
                errors_reqing_retry.append(tool_call.id)
                add_output = True

            if add_output:
                # Check early if the message would get 400'd
                # Can't pass null tool content to the API
                if not (tool_output == "" or tool_output is not None):
                    raise ValueError(
                        f"Tool output is empty but requires content for message: {tool_output=}"
                    )

                self.add_tool_message(
                    content=tool_output,
                    tool_call_id=tool_call.id,
                )

        stopping_chain = self._determine_if_stopping_chain(
            stop_chain_after, errors_reqing_retry
        )

        self.logger.info("Tool calls handled.")

        if not stopping_chain:
            return self.complete_chat()

    def _determine_if_stopping_chain(
        self, stop_chain_after: dict, errors_reqing_retry: list
    ) -> bool:
        # By default, we don't stop the next chat completion
        stopping_chain = False

        # If any tool wants to stop the chain, we stop the chain
        if any(stop_chain_after.values()):
            stopping_chain = True

            if len(errors_reqing_retry) > 0:
                # don't stop the chain if we have errors that require a tool call retry
                stopping_chain = False
                self.logger.warning(
                    f"{len(errors_reqing_retry)} tool calls require a retry due to errors, "
                    "even though some tools want to stop the chain. Defualting to retrying (stopping_chain = False)"
                )

            elif len(errors_reqing_retry) == 0:
                # if no errors, we can stop the chain

                # check if there is a disagreement between tool calls
                if not all(stop_chain_after.values()):
                    n_calls_that_want_stop = sum(
                        1 for _, stop in stop_chain_after.items() if stop
                    )

                    n_calls_that_want_continue = (
                        len(stop_chain_after) - n_calls_that_want_stop
                    )

                    self.logger.warning(
                        f"Disagreement on stopping the chain. {n_calls_that_want_stop} tool calls"
                        f" want to stop, {n_calls_that_want_continue} tools want to continue. "
                        "Defaulting to stopping the chain (stopping_chain = True)"
                    )

        return stopping_chain

    def _get_tools_dict(
        self,
    ) -> dict:
        """
        Dynamically generate tool options based on the tool classes
        """

        if len(self.tools) == 0:
            # Tools must have len >= 1 or be null
            return {}

        tool_schema = get_tool_schema(self.tools)

        tools_dict = {"tools": tool_schema}

        return tools_dict

    def _get_llm_response(
        self,
        messages: list,
        llm_params: dict,
        response_format: Type[BaseModel] | None = None,
    ) -> ChatCompletion:
        """
        Get the LLM response from the provider.
        Currently this only supports OpenAI's API, but later on
        this is where we would add support for other providers.
        """

        self.logger.info("Sending LLM request...")

        if response_format:
            response = self.llm_client.beta.chat.completions.parse(
                messages=self.messages,
                **self.llm_params,
                response_format=response_format,
            )

        else:
            response: ChatCompletion = self.llm_client.chat.completions.create(
                messages=messages, **llm_params
            )

        self.logger.info(
            "Received LLM response. Token Usage: "
            f"{response.usage.prompt_tokens:,} In + "
            f"{response.usage.completion_tokens:,} Out = "
            f"{response.usage.total_tokens:,} Total"
        )

        return response

    def _request_tool_message(
        self,
        tool: BaseTool,
    ):
        tool_name = tool.get_name()
        self.force_tool_usage(tool_name)
        response = self.complete_chat()

        if response:
            # if we are allow the chain to continue
            self.add_assistant_message_from_response(response)

    def _request_structured_message(
        self,
        response_format: Type[BaseModel],
    ):
        if self.llm_params["model"] not in ["gpt-4o-mini", "gpt-4o-2024-08-06,"]:
            raise ValueError(
                f"Structured messages are only supported for the following models: "
                f"'gpt-4o-mini', 'gpt-4o-2024-08-06', not {self.llm_params['model']}"
            )
        response = self._get_llm_response(
            messages=self.messages,
            llm_params=self.llm_params,
            response_format=response_format,
        )
        self.add_assistant_message_from_response(response)

    def get_total_usage(
        self,
    ) -> dict:
        """
        Get the usage of the agent

        Returns
        -------
        dict
            The usage of the agent in the form of a dictionary
            with the keys: prompt_tokens, completion_tokens, total_tokens
        """

        usage_dicts = [resp.usage for resp in self._responses]

        total_prompt_tokens = sum(usage.prompt_tokens for usage in usage_dicts)
        total_compl_tokens = sum(usage.completion_tokens for usage in usage_dicts)
        total_total_tokens = sum(usage.total_tokens for usage in usage_dicts)

        total_usage = {
            "prompt_tokens": total_prompt_tokens,
            "completion_tokens": total_compl_tokens,
            "total_tokens": total_total_tokens,
        }

        return total_usage

    def add_user_message(
        self,
        content: str,
    ) -> None:
        """
        Add a user message to the messages list

        Parameters
        ----------
        content : str
            The content of the user message

        Returns
        -------
        None
            Updates the `messages` attribute
        """
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str, tool_calls: list[ToolCall]) -> None:
        """
        Add an assistant message to the messages list

        Parameters
        ----------
        content : str
            The content of the assistant message

        tools_calls : list[BaseModel | dict] | None
            A list of tool calls to make.
            These are when the LLM wants to call a tool.
            By default, we don't inlcude any tool calls.

        Returns
        -------
        None
            Updates the `messages` attribute
        """
        msg = {"role": "assistant", "content": content}

        if tool_calls:
            # convert the tool calls to a model dump (dict)
            _tool_calls = []
            for tool_call in tool_calls:
                if isinstance(tool_call, BaseModel):
                    tool_call = tool_call.model_dump()
                    _tool_calls.append(tool_call)
                elif isinstance(tool_call, dict):
                    _tool_calls.append(tool_call)
                else:
                    raise ValueError(
                        f"Tool call must be of type BaseModel or dict, not {type(tool_call)}"
                    )

            msg["tool_calls"] = _tool_calls

        self.messages.append(msg)

    def add_tool_message(
        self,
        content: str,
        tool_call_id: str,
    ) -> None:
        """
        Add a tool message to the messages list.
        This is when a tool returns an output or raises an error.

        Parameters
        ----------
        content : str
            The content of the tool message

        tool_call_id : str
            The id of the tool call

        Returns
        -------
        None
        """
        self.messages.append(
            {"role": "tool", "content": content, "tool_call_id": tool_call_id}
        )

    def force_tool_usage(self, tool_name: str | None):
        """
        Forces the LLM to use a specific tool for all completions until reset.
        Reset by calling with tool_name=None.

        Parameters
        ----------
        tool_name : str | None
            The name of the tool to force usage of.
            If None, resets the forced tool usage.
        """

        if tool_name is None:
            self.llm_params["tool_choice"] = None
            return

        tool_names = [tool.get_name() for tool in self.tools]

        if tool_name not in tool_names:
            raise ValueError(
                f"Tool {tool_name} not found in the list of available tools: {tool_names}"
            )

        self.llm_params["tool_choice"] = {
            "type": "function",
            "function": {"name": tool_name},
        }

    def add_assistant_message_from_response(self, response: ChatCompletion):
        self.add_assistant_message(
            content=response.choices[0].message.content,
            tool_calls=response.choices[0].message.tool_calls,
        )

    @track_recursion_depth
    def complete_chat(
        self,
    ) -> None | ChatCompletion:
        """
        Runs chat completions until the next chat message is generated
        (i.e. all tools calls are completed) or until we use a tool with
        stop_chain_after=True.

        The flow of the function is as follows:

                        response
        `complete_chat`--<                     None
            ↑           `handle_tool_calls`---<
            |                                 |
            |_________________________________|

        1. `complete_chat` either returns a response, or dispatches to `handle_tool_calls`.
        2. `handle_tool_calls` either returns None (depending on the tools' preference),
            or dispatches back to `complete_chat`

        Returns
        -------
        None | openai.resources.completions.Completion
            If the last tool call specifies stop_chain_after=True, return None.
            Otherwise, return the next chat completion response.
        """

        # dynamically generate the tools dict
        # incase we updated this on the fly
        llm_params = self.llm_params | self._get_tools_dict()

        response = self._get_llm_response(
            messages=self.messages,
            llm_params=llm_params,
        )

        if response.choices[0].finish_reason == "length":
            raise self.AgentError("Max tokens reached.")

        # Cache responses for debugging, usage tracking, etc.
        self._responses.append(response)

        if response.choices[0].message.tool_calls:
            return self._handle_tool_calls(response)

        return response

    def request_message(
        self,
        conform_to: BaseTool | Type[BaseModel] | None,
    ):
        """
        Request a message from the agent that conforms to the specified type,
        and add it to the messages list.

        Parameters
        ----------
        conform_to : BaseTool | BaseModel | None
            The type of message to request.
            If BaseTool: forces tool usage.
                Forces the agent to use the specified tool during the next message.
                Further behavior is dependant on the tool's configuration
                (e.g. stop_chain_after, add_output_to_messages_after).
                If a chat message is generated, it will be added to the messages list.
            If Pydantic Model: forces structured output.
                Forces the agent to return a structured message that conforms to the
                specified model. This is useful when you want to get a specific
                type of output from the agent, e.g. a structured response that can be
                used in a downstream system. The message will be added to the messages
                list, and the chain will end.
                If a chat message is generated, it will be added to the messages list.
            If None: the chat is completed.
                Use this when you want the agent to decide what to do next.
                The agent will either
                    1. respond directly by an assistant message with content, or
                    2. call a tool (if available), with further behavior dependant
                       on said tool's configuration (see `If BaseTool`).
        """
        if isinstance(conform_to, BaseTool):
            self._request_tool_message(conform_to)

        elif issubclass(conform_to, BaseModel):
            self._request_structured_message(conform_to)

        elif conform_to is None:
            self.complete_chat()

        else:
            raise ValueError(
                f"conform_to must be of type BaseTool or a subclass of pydantic.BaseModel, not {type(conform_to)}"
            )
