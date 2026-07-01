from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    """

    try:

        result = eval(expression)

        return str(result)

    except Exception:

        return "Invalid mathematical expression."