from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy._core import message_design
from tgpy._core.utils import convert_result, format_traceback
from tgpy.api import constants, tgpy_eval


async def eval_message(code: str, message: Message) -> Message | None:
    await message_design.edit_message(message, code, 'Running...')

    # noinspection PyBroadException
    try:
        eval_result = await tgpy_eval(code, message, filename=None)
    except Exception:
        result = None
        output = ''
        exc, full_exc = format_traceback()
    else:
        if app.ctx.is_manual_output:
            return
        result = convert_result(eval_result.result)
        output = eval_result.output
        exc = ''
        full_exc = None

    constants['exc'] = full_exc

    try:
        # noinspection PyProtectedMember
        return await message_design.edit_message(
            message,
            code,
            result,
            traceback=exc,
            output=output,
        )
    except MessageIdInvalidError:
        return None


__all__ = ['eval_message']
