import sys
import traceback
from typing import Any

from telethon.tl import TLObject


def convert_result(result: Any) -> str:
    if isinstance(result, TLObject):
        return result.stringify()
    else:
        return str(result)


def format_traceback() -> tuple[str, str]:
    _, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    te = traceback.TracebackException(
        type(exc_value), exc_value, exc_traceback, compact=True
    )
    return ''.join(te.format_exception_only()), ''.join(te.format())
