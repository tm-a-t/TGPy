import sys
import traceback

from telethon.tl import TLObject


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result


def format_traceback():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    return traceback.format_exception(exc_type, exc_value, exc_traceback)
