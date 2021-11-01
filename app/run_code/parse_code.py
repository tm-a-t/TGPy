import ast


class _Result:
    is_code = False
    uses_orig = False


def parse_code(text: str):
    result = _Result()

    try:
        root = ast.parse(text, '', 'exec')
    except (SyntaxError, ValueError):
        return result

    if len(root.body) == 1 and isinstance(root.body[0], ast.Expr):
        if isinstance(root.body[0].value, (ast.Constant, ast.Name)):
            return result
        if isinstance(root.body[0].value, ast.UnaryOp) and isinstance(root.body[0].value.operand, ast.Constant):
            return result

    result.is_code = True

    for node in ast.walk(root):
        if isinstance(node, ast.Name) and node.id == 'orig':
            result.uses_orig = True
            return result

    return result

