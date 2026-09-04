import asyncio
from asyncio import Task
from contextvars import Context, copy_context
from typing import Any

from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy._core import message_design
from tgpy._core.utils import convert_result, format_traceback
from tgpy.api import config, constants, tgpy_eval

running_messages: dict[tuple[int, int], Task[Any]] = {}
initial_edit_tasks: dict[tuple[int, int], Task[None]] = {}


async def eval_message(code: str, message: Message) -> Message | None:
    eval_ctx = copy_context()

    msg_key = (message.chat_id, message.id)

    delay = float(config.get('core.initial_edit_delay'))
    initial_edit_tasks[msg_key] = asyncio.create_task(
        initial_edit(message, code, delay, eval_ctx)
    )

    task = asyncio.create_task(tgpy_eval(code, message, filename=None, ctx=eval_ctx))
    running_messages[msg_key] = task
    try:
        eval_result = await task
    except asyncio.CancelledError:
        return
    except Exception:  # noqa: BLE001
        result = None
        output = ''
        exc, constants['exc'] = format_traceback()
    else:
        if eval_ctx.run(lambda: app.ctx.is_manual_output):
            return
        result = convert_result(eval_result.result)
        output = eval_result.output or ''
        exc = ''
        constants['exc'] = None
    finally:
        if initial_edit_task := initial_edit_tasks.pop(msg_key):
            initial_edit_task.cancel()
        running_messages.pop(msg_key)

    try:
        return await message_design.edit_message(
            message,
            code,
            result,
            traceback=exc,
            output=output,
        )
    except MessageIdInvalidError:
        return


async def initial_edit(message: Message, code: str, delay: float, ctx: Context):
    if delay:
        await asyncio.sleep(delay)

        chat = await message.get_input_chat() if message.is_channel else None
        try:
            updated_message = await message.client.get_messages(chat, ids=message.id)
        except ValueError:
            return

        if updated_message is None:
            return

        if updated_message.edit_date != message.edit_date:
            return

        if ctx.run(lambda: app.ctx.is_manual_output):
            return

    await message_design.edit_message(
        updated_message,
        code,
        output=ctx.run(lambda: app.ctx._output) or '',
        is_running=True,
    )


__all__ = ['eval_message', 'running_messages']
