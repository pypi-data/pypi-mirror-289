from pydantic import BaseModel


class ToolUsageError(Exception):
    """
    A special exception that when raised in a tool's function,
    it will pass the error as a tool message to the LLM and reprompt it.

    This is useful for when we want the LLM to retry the tool call.
    """

    pass


class BaseTool(BaseModel):
    @classmethod
    def get_name(cls):
        raise NotImplementedError

    @classmethod
    def get_description(cls):
        return cls.__doc__

    def function(self, secret_kwargs):
        raise NotImplementedError

    @staticmethod
    def add_output_to_messages_after():
        """Whether to add the tool's output to the messages list after running"""
        return True

    @staticmethod
    def stop_chain_after():
        """Whether to stop the chain after running the tool"""
        return False
