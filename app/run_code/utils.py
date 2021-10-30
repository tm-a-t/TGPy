import sys
import traceback
from typing import Optional

from telethon.tl import TLObject
from telethon.tl.custom import Message


class Context:
    msg: Optional[Message] = None

    def __str__(self):
        return f'<Context(msg)>'


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


filename_prefix = 'tgpy://'


def format_traceback():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    while not exc_traceback.tb_frame.f_code.co_filename.startswith(filename_prefix):
        exc_traceback = exc_traceback.tb_next
    return traceback.format_exception(exc_type, exc_value, exc_traceback)
