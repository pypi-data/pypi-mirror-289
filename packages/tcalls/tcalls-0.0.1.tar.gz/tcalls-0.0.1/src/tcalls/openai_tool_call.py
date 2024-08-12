import inspect
from typing import Any, Callable

from docstring_parser import Docstring, parser
from openai.types.shared import FunctionDefinition


def type_to_name(type_annotation: Any) -> str:
    supported_types = {
        str: "string",
        int: "integer",
        float: "number",
        complex: "number",
        bool: "boolean",
        dict: "object",
        list: "array",
    }
    return supported_types.get(type_annotation, "null")


def get_openai_tool_schema(
    func: Callable,
) -> FunctionDefinition:
    function_schema = {
        "name": "",
        "description": "",
    }
    parameters_schema = {"type": "object", "required": [], "properties": {}}
    required = []

    signature = inspect.signature(func)
    docstring: Docstring = parser.parse(func.__doc__)
    function_schema["name"] = func.__name__
    function_schema["description"] = docstring.short_description or ""

    if len(signature.parameters) > 0:
        properties = {}
        for pname, parameter in signature.parameters.items():
            if parameter.default == inspect._empty:
                required.append(pname)
            type_name = type_to_name(parameter.annotation)
            properties[pname] = {
                "type": type_name,
            }

        parameters_schema["required"] = required

        # update parameter description by docstring.
        for d_param in docstring.params:
            if d_param.arg_name in properties and len(d_param.description.strip()) != 0:
                properties[d_param.arg_name]["description"] = d_param.description.strip()

        parameters_schema["properties"] = properties

        function_schema["parameters"] = parameters_schema

    return {"type": "function", "function": function_schema}
