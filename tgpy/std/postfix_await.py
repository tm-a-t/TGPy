"""
    name: postfix_await
    origin: tgpy://builtin_module/postfix_await
    priority: 300
"""

import ast
import tokenize

import tgpy.api
from tgpy.api import tokenize_string, untokenize_to_string

AWAIT_REPLACEMENT_ATTRIBUTE = '__tgpy_await__'


def code_trans(code: str) -> str:
    tokens = tokenize_string(code)
    if not tokens:
        return code
    for i, tok in enumerate(tokens):
        if i == 0:
            continue
        prev_tok = tokens[i - 1]
        if (
            tok.type == tokenize.NAME
            and tok.string == 'await'
            and prev_tok.type == tokenize.OP
            and prev_tok.string == '.'
        ):
            tokens[i] = tok._replace(string=AWAIT_REPLACEMENT_ATTRIBUTE)
    return untokenize_to_string(tokens)


class AwaitTransformer(ast.NodeTransformer):
    def visit_Attribute(self, node: ast.Attribute):
        node = self.generic_visit(node)
        if node.attr == AWAIT_REPLACEMENT_ATTRIBUTE:
            return ast.Await(value=node.value)
        else:
            return node


def ast_trans(tree: ast.AST) -> ast.AST:
    return AwaitTransformer().visit(tree)


tgpy.api.code_transformers.add('postfix_await', code_trans)
tgpy.api.ast_transformers.add('postfix_await', ast_trans)

__all__ = []
