import sys
import tokenize
import traceback
from io import BytesIO

from telethon.tl import TLObject


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result


def format_traceback():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    return traceback.format_exception(exc_type, exc_value, exc_traceback)


def tokenize_string(s: str) -> list[tokenize.TokenInfo] | None:
    try:
        return list(tokenize.tokenize(BytesIO(s.encode('utf-8')).readline))
    except (IndentationError, tokenize.TokenError):
        return None


def untokenize_to_string(tokens: list[tokenize.TokenInfo]) -> str:
    return tokenize.untokenize(tokens).decode('utf-8')
