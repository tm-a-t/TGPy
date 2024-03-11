import asyncio
from asyncio import Task

from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy._core import message_design
from tgpy._core.utils import convert_result, format_traceback
from tgpy.api.tgpy_eval import tgpy_eval

running_messages: dict[tuple[int, int], Task] = {}


async def eval_message(code: str, message: Message) -> Message | None:
    await message_design.edit_message(message, code, 'Running...')

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
        result = 'Error occurred'
        output = ''
        exc = ''.join(format_traceback())
    else:
        if app.ctx.is_manual_output:
            return
        result = convert_result(eval_result.result)
        output = eval_result.output
        exc = ''
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
