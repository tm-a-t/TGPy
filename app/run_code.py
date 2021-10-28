import sys
import traceback
from collections import Iterable

from telethon.tl import TLObject
from telethon.tl.custom import Message

from app import client
from app import message_design
from app.meval import meval
from app.variables import variables


class _Output:
    text = ''

    def print(self, *values, sep=' ', end='\n', file=None, flush=True):
        if file:
            print(*values, sep=sep, end=end, file=file, flush=flush)
        else:
            self.text += sep.join(str(val) for val in values) + end


async def eval_message(code: str, message: Message, uses_orig=False) -> None:
    await message_design.edit_message(message, code, 'Running...')

    output = _Output()
    kwargs = {'orig': await message.get_reply_message()} if uses_orig else {}
    # noinspection PyBroadException
    try:
        new_variables, result = await meval(
            code,
            globals(),
            variables,
            client=client,
            msg=message,
            print=output.print,
            **kwargs,
        )
    except Exception:
        result = 'Error occurred'
        exc = ''.join(traceback.format_exception(*sys.exc_info()))
    else:
        variables.update(new_variables)
        result = convert_result(result)
        exc = ''

    await message_design.edit_message(message, code, result, traceback=exc, output=output.text)


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result
