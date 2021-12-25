from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy import message_design
from tgpy.run_code.meval import meval
from tgpy.run_code.utils import Output, convert_result, filename_prefix, format_traceback
from tgpy.run_code.variables import variables


def get_kwargs(include_orig=True):
    return list(variables.keys()) + ['ctx', 'msg', 'print', 'client'] + ['orig'] if include_orig else []


async def eval_message(code: str, message: Message, uses_orig=False) -> None:
    await message_design.edit_message(message, code, 'Running...')

    output = Output()

    variables['ctx'].msg = message

    kwargs = {}
    if uses_orig:
        orig = await message.get_reply_message()
        kwargs['orig'] = orig

    # noinspection PyBroadException
    try:
        new_variables, result = await meval(
            code,
            f'{filename_prefix}message/{message.chat_id}/{message.id}',
            globals(),
            variables,
            client=app.client,
            msg=message,
            ctx=variables['ctx'],
            print=output.print,
            **kwargs,
        )
    except Exception:
        result = 'Error occurred'
        exc = ''.join(format_traceback())
    else:
        variables.update(new_variables)
        result = convert_result(result)
        exc = ''

    try:
        await message_design.edit_message(message, code, result, traceback=exc, output=output.text)
    except MessageIdInvalidError:
        pass


from tgpy.run_code import builtin_functions
