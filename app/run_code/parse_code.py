import ast


class _Result:
    is_code = False
    uses_orig = False


def _is_node_fp_word(node: ast.AST, locs: dict) -> bool:
    """Check if AST node is a Name or Attribute not present in locals"""
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
        return node.value.id not in locs
    return isinstance(node, ast.Name) and node.id not in locs


def _check_node_on_false_binop(node: ast.AST, locs: dict) -> bool:
    """Check if AST node can be an operand or binary operation (ast.BinOp, ast.Compare, ast.BoolOp)
    with operands which do not pass _is_node_fp_word check"""
    if _is_node_fp_word(node, locs):
        return True
    if not isinstance(node, (ast.BoolOp, ast.BinOp, ast.Compare)):
        return False
    if isinstance(node, ast.Compare):
        return _is_node_fp_word(node.left, locs) and all(_is_node_fp_word(x, locs) for x in node.comparators)
    return all(_check_node_on_false_binop(operand, locs) for operand in ((node.left, node.right) if isinstance(node, ast.BinOp) else node.values))


def _is_node_false(node: ast.AST, locs: dict) -> bool:
    """Check if AST node didn't seem to be meant to be code"""
    return (
        isinstance(node, ast.Constant) or _is_node_fp_word(node, locs)
        or isinstance(node, ast.UnaryOp) and isinstance(node.operand, (ast.Constant, ast.Name, ast.Attribute))  # Messages like "-1", "+spam" and "not foo.bar"
        or _check_node_on_false_binop(node, locs)  # Messages like one-two, one is two, one >= two, one.b in two.c
        or isinstance(node, ast.Tuple) and all(_is_node_false(elt, locs) for elt in node.elts)  # "(yes, understood)"
    )


def parse_code(text: str, locs: dict) -> _Result:
    """Parse given text and decide should it be evaluated as Python code"""
    result = _Result()

    try:
        root = ast.parse(text, '', 'exec')
    except (SyntaxError, ValueError):
        return result

    if all(isinstance(body_item, ast.Expr) and _is_node_false(body_item.value, locs) for body_item in root.body):
        return result

    result.is_code = True

    for node in ast.walk(root):
        if isinstance(node, ast.Name) and node.id == 'orig':
            result.uses_orig = True
            return result

    return result

