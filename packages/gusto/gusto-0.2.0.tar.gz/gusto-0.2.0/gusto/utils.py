@staticmethod
def track_recursion_depth(func):
    """
    Decorator to track recursion depth.
    Raises a AgentError if the max recursion depth is reached.
    """

    def wrapper(self, *args: list, **kwargs: dict):
        self._recursion_depth += 1
        if self._recursion_depth > self._max_recursion_depth:
            raise self.AgentError(
                f"Max recursion depth of {self._max_recursion_depth} reached."
            )

        result = func(self, *args, **kwargs)
        self._recursion_depth -= 1
        return result

    return wrapper


def get_tool_schema(tool_classes):
    """
    Extracts the name, description, and json-schema of the tools,
    and formats them into a json dict format for the LLM providers.
    """
    tools_schemas = [
        {
            "name": tool.get_name(),
            "description": tool.get_description(),
            "parameters": tool.model_json_schema(),
        }
        for tool in tool_classes
    ]

    tool_schema = [
        {"type": "function", "function": func_schema} for func_schema in tools_schemas
    ]

    return tool_schema
