from typing import Optional

from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app, message_design
from tgpy.run_code.meval import meval
from tgpy.run_code.parse_code import parse_code
from tgpy.run_code.utils import convert_result, format_traceback
from tgpy.utils import filename_prefix


def get_variable_names(include_orig=True):
    # fmt: off
    return (
        list(app.api.variables.keys()) + list(app.api.constants.keys()) + ['msg', 'print']
        + ['orig'] if include_orig else []
    )
    # fmt: on


async def eval_message(
    code: str, message: Message, uses_orig: bool
) -> Optional[Message]:
    await message_design.edit_message(message, code, 'Running...')

    app.ctx.msg = message

    orig_kwarg = {}
    if uses_orig:
        orig = await message.get_reply_message()
        orig_kwarg['orig'] = orig

    # noinspection PyBroadException
    try:
        # noinspection PyProtectedMember
        new_variables, result = await meval(
            code,
            f'{filename_prefix}message/{message.chat_id}/{message.id}',
            globals(),
            app.api.variables,
            msg=message,
            print=app.ctx._print,
            **app.api.constants,
            **orig_kwarg,
        )
    except Exception:
        result = 'Error occurred'
        exc = ''.join(format_traceback())
    else:
        app.api.variables.update(new_variables)
        result = convert_result(result)
        exc = ''

    try:
        # noinspection PyProtectedMember
        return await message_design.edit_message(
            message,
            code,
            result,
            traceback=exc,
            output=app.ctx._print_output,
        )
    except MessageIdInvalidError:
        return None
