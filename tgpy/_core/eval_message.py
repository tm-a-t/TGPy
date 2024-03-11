import asyncio
from asyncio import Task

from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy._core import message_design
from tgpy._core.utils import convert_result, format_traceback
from tgpy.api import constants, tgpy_eval

running_messages: dict[tuple[int, int], Task] = {}


async def eval_message(code: str, message: Message) -> Message | None:
    task = asyncio.create_task(tgpy_eval(code, message, filename=None))
    running_messages[(message.chat_id, message.id)] = task
    # noinspection PyBroadException
    try:
        eval_result = await task
    except asyncio.CancelledError:
        # message cancelled, do nothing
        # return no message as it wasn't edited
        return None
    except Exception:
        result = None
        output = ''
        exc, constants['exc'] = format_traceback()
    else:
        if app.ctx.is_manual_output:
            return
        result = convert_result(eval_result.result)
        output = eval_result.output
        exc = ''
        constants['exc'] = None
    finally:
        running_messages.pop((message.chat_id, message.id))

    try:
        return await message_design.edit_message(
            message,
            code,
            result,
            traceback=exc,
            output=output,
        )
    except MessageIdInvalidError:
        return None


__all__ = ['eval_message', 'running_messages']
