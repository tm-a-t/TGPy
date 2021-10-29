from telethon.tl import TLObject
from telethon.tl.custom import Message


class Context:
    msg: Message = None
    orig: Message = None

    def __str__(self):
        return f'<Context(msg, orig)>'


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
