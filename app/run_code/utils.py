from telethon.tl import TLObject


class Context:
    msg = None
    orig = None

    def __repr__(self):
        return f'<Context>'


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
