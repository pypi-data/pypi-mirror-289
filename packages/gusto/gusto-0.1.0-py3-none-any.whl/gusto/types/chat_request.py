from typing import Literal, Optional, Union

from pydantic import BaseModel, Field

from .chat_messages import Messages


class ToolFunction(BaseModel):
    description: Optional[str] = Field(
        ...,
        description="A description of what the function does, used by the model to choose when and how to call the function.",
    )
    name: str = Field(
        ...,
        description="The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.",
    )
    parameters: Optional[dict] = Field(
        ...,
        description=(
            "The parameters the functions accepts, described as a JSON Schema object. "
            "See the guide for examples, and the JSON Schema reference for documentation about the format. "
            "Omitting parameters defines a function with an empty parameter list."
        ),
    )


class Tool(BaseModel):
    type: str = Field(
        Literal["function"],
        description="The type of the tool. Currently, only `function` is supported.",
    )
    function: ToolFunction = Field(
        ..., description="The function that the model may call."
    )


class ResponseFormat(BaseModel):
    type: str = Field(
        Literal["text", "json_object"],
        description="Must be one of `text` or `json_object`.",
    )


class ChatCompletionRequest(BaseModel):
    model: str = Field(
        ...,
        description="ID of the model to use. See the model endpoint compatibility table for details on which models work with the Chat API.",
    )
    messages: Messages = Field(
        ..., description="A list of messages comprising the conversation so far."
    )
    temperature: Optional[float] = Field(
        1.0,
        description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.",
    )
    top_p: Optional[float] = Field(
        1.0,
        description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.",
    )
    n: Optional[int] = Field(
        1,
        description="How many chat completion choices to generate for each input message.",
    )
    stream: Optional[bool] = Field(
        False,
        description="If set, partial message deltas will be sent, like in ChatGPT.",
    )
    logprobs: Optional[bool] = Field(
        False,
        description="Whether to return log probabilities of the output tokens or not.",
    )
    max_tokens: Optional[int] = Field(
        None,
        description="The maximum number of tokens that can be generated in the chat completion.",
    )
    top_k: Optional[int] = Field(
        None,
        description="The number of most likely tokens to return at each token position.",
    )
    frequency_penalty: Optional[float] = Field(
        0.0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far.",
    )
    presence_penalty: Optional[float] = Field(
        0.0,
        description="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far.",
    )
    stop: Optional[Union[str, list[str]]] = Field(
        None,
        description="Up to 4 sequences where the API will stop generating further tokens.",
    )
    logit_bias: Optional[dict] = Field(
        None,
        description="Modify the likelihood of specified tokens appearing in the completion.",
    )
    user: Optional[str] = Field(
        None,
        description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.",
    )
    response_format: Optional[ResponseFormat] = Field(
        None, description="An object specifying the format that the model must output."
    )
    tools: Optional[list[Tool]] = Field(
        None, description="A list of tools the model may call."
    )
    function_call: Optional[Union[str, dict]] = Field(
        None,
        description="Deprecated in favor of `tool_choice`. Controls which (if any) function is called by the model.",
    )
    functions: Optional[list[Tool]] = Field(
        None,
        description="Deprecated in favor of `tools`. A list of functions the model may generate JSON inputs for.",
    )
    tool_choice: Optional[Union[str, dict]] = Field(
        None, description="Controls which (if any) tool is called by the model."
    )
    seed: Optional[int] = Field(
        None,
        description="If specified, our system will make a best effort to sample deterministically.",
    )
    parallel_tool_calls: Optional[bool] = Field(
        True, description="Whether to enable parallel function calling during tool use."
    )
    stream_options: Optional[dict] = Field(
        None,
        description="Options for streaming response. Only set this when you set `stream: true`.",
    )
