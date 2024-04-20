import sys
import tokenize
import traceback
from io import BytesIO

from telethon.tl import TLObject


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result


def format_traceback() -> tuple[str, str]:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    te = traceback.TracebackException(
        type(exc_value), exc_value, exc_traceback, compact=True
    )
    return ''.join(te.format_exception_only()), ''.join(te.format())
