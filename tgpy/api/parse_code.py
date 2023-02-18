import ast
import logging
from dataclasses import dataclass

import tgpy.api
from tgpy.api.transformers import ast_transformers, code_transformers

logger = logging.getLogger(__name__)


@dataclass
class ParseResult:
    is_code: bool = False
    uses_orig: bool = False
    original: str = ''
    transformed: str = ''
    tree: ast.AST | None = None
    exc: Exception | None = None


def _is_node_unknown_variable(node: ast.AST, locs: dict) -> bool:
    """Check if AST node is a Name or Attribute not present in locals"""
    if isinstance(node, ast.Attribute):
        return _is_node_unknown_variable(node.value, locs)
    return isinstance(node, ast.Name) and node.id not in locs


def _is_node_suspicious_binop(node: ast.AST, locs: dict) -> bool:
    """Check if AST node can be an operand of binary operation (ast.BinOp, ast.Compare, ast.BoolOp)
    with operands which do not pass _is_node_unknown_variable check, or is such operation"""
    if _is_node_unknown_variable(node, locs):
        return True
    if not isinstance(node, (ast.BoolOp, ast.BinOp, ast.Compare)):
        return False
    if isinstance(node, ast.Compare):
        return _is_node_unknown_variable(node.left, locs) or any(
            _is_node_unknown_variable(x, locs) for x in node.comparators
        )
    return any(
        _is_node_suspicious_binop(operand, locs)
        for operand in (
            (node.left, node.right) if isinstance(node, ast.BinOp) else node.values
        )
    )


def _ignore_node_simple(node: ast.AST, locs: dict) -> bool:
    """Check if message is constant or unknown variable"""
    return (
        # Messages like "python", "123" or "example.com"
        isinstance(node, ast.Constant)
        or _is_node_unknown_variable(node, locs)
    )


def _ignore_node(node: ast.AST, locs: dict) -> bool:
    """Check if AST node didn't seem to be meant to be code"""
    if isinstance(node, ast.Expr):
        return _ignore_node(node.value, locs)
    return (
        _ignore_node_simple(node, locs)
        # Messages like "-1", "+spam" and "not foo.bar"
        # `getattr(..., None) or node.value` is used here to avoid AttributeError and because in UnaryOp and Starred
        # operands are stored in different attributes ("operand" and "value" respectively)
        or isinstance(node, (ast.Starred, ast.UnaryOp))
        and isinstance(
            getattr(node, 'operand', None) or node.value,
            (ast.Constant, ast.Name, ast.Attribute),
        )
        # Messages like one-two, one is two, one >= two, one.b in two.c
        or _is_node_suspicious_binop(node, locs)
        # Messages like "yes, understood"
        or isinstance(node, ast.Tuple)
        and any(_ignore_node(elt, locs) for elt in node.elts)
        # Messages like "cat (no)"
        or isinstance(node, ast.Call)
        and _ignore_node(node.func, locs)
        and any(_ignore_node(arg, locs) for arg in node.args)
        # Messages like "fix: fix"
        or isinstance(node, ast.AnnAssign)
        and node.value is None
        and _ignore_node(node.target, locs)
        and _ignore_node(node.annotation, locs)
    )


async def parse_code(text: str, ignore_simple: bool = True) -> ParseResult:
    """Parse given text and decide should it be evaluated as Python code"""
    result = ParseResult(original=text)

    text = await code_transformers.apply(text)
    result.transformed = text

    try:
        tree = ast.parse(text, '', 'exec')
    except (SyntaxError, ValueError) as e:
        result.exc = e
        return result

    tree = await ast_transformers.apply(tree)
    result.tree = tree

    if ignore_simple:
        locs = (
            list(tgpy.api.variables.keys())
            + list(tgpy.api.constants.keys())
            + ['msg', 'print', 'orig']
        )
        if all(_ignore_node(body_item, locs) for body_item in tree.body):
            return result

    result.is_code = True

    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == 'orig':
            result.uses_orig = True
            return result

    return result


__all__ = ['ParseResult', 'parse_code']
