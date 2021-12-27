import sys
import traceback

from telethon.tl import TLObject


class Output:
    text = ''

    def print(self, *values, sep=' ', end='\n', file=None, flush=True):
        if file:
            print(*values, sep=sep, end=end, file=file, flush=flush)
        else:
            self.text += sep.join(str(val) for val in values) + end


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result


def format_traceback():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    return traceback.format_exception(exc_type, exc_value, exc_traceback)
