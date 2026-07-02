import ast
import operator

from langchain_core.tools import tool


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        operand = _safe_eval(node.operand)
        return _ALLOWED_OPERATORS[type(node.op)](operand)

    raise ValueError("Invalid mathematical expression.")


@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    Use this tool for arithmetic calculations.
    """
    try:
        parsed_expression = ast.parse(expression, mode="eval")
        result = _safe_eval(parsed_expression.body)
        return str(result)
    except Exception:
        return "Invalid mathematical expression."
