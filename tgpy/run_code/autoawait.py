import ast
import tokenize
from io import BytesIO

AWAIT_REPLACEMENT_ATTRIBUTE = '__tgpy_await__'


def tokenize_string(s: str) -> list[tokenize.TokenInfo] | None:
    try:
        return list(tokenize.tokenize(BytesIO(s.encode('utf-8')).readline))
    except IndentationError:
        return None


def untokenize_to_string(tokens: list[tokenize.TokenInfo]) -> str:
    return tokenize.untokenize(tokens).decode('utf-8')


def pre_transform(code: str) -> str:
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


transformer = AwaitTransformer()

__all__ = ['pre_transform', 'transformer']
