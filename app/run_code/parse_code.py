import ast


class _Result:
    is_code = False
    uses_orig = False


FALSE_BINOP_TYPES = (ast.Constant, ast.Name, ast.Attribute)


def _check_node_on_false_binop(node) -> bool:
    if isinstance(node, FALSE_BINOP_TYPES):
        return True
    if not isinstance(node, (ast.BoolOp, ast.BinOp, ast.Compare)):
        return False
    if isinstance(node, ast.Compare):
        return isinstance(node.left, FALSE_BINOP_TYPES) and all(isinstance(x, FALSE_BINOP_TYPES) for x in node.comparators)
    return all(_check_node_on_false_binop(operand) for operand in ((node.left, node.right) if isinstance(node, ast.BinOp) else node.values))


def _is_node_false(node: ast.AST) -> bool:
    return (
        isinstance(node, (ast.Constant, ast.Name))
        or isinstance(node, ast.UnaryOp) and isinstance(node.operand, (ast.Constant, ast.Name, ast.Attribute))  # Messages like "-1", "+spam" and "not foo.bar"
        or _check_node_on_false_binop(node)  # Messages like one-two, one is two, one >= two, one.b in two.c
        or isinstance(node, ast.Tuple) and all(_check_node_on_false_binop(elt) for elt in node.elts)  # "(yes, understood)"
    )


def parse_code(text: str):
    result = _Result()

    try:
        root = ast.parse(text, '', 'exec')
    except (SyntaxError, ValueError):
        return result

    if all(isinstance(body_item, ast.Expr) and _is_node_false(body_item.value) for body_item in root.body):
        return result

    result.is_code = True

    for node in ast.walk(root):
        if isinstance(node, ast.Name) and node.id == 'orig':
            result.uses_orig = True
            return result

    return result

