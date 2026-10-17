import asyncio
from asyncio import Event, Task
from contextvars import Context
from typing import Any

from telethon.errors import MessageIdInvalidError
from telethon.tl.custom import Message

from tgpy import app
from tgpy._core import message_design
from tgpy._core.utils import convert_result, format_traceback
from tgpy.api.config import config
from tgpy.api.tgpy_eval import constants, tgpy_eval

running_messages: dict[tuple[int, int], Task[Any]] = {}
# (chat_id, msg_id) -> (cancel_evt, ensure_edit_evt, task)
initial_edit_tasks: dict[tuple[int, int], tuple[Event, Event, Task[None]]] = {}


async def eval_message(code: str, message: Message) -> Message | None:
    eval_ctx = Context()

    msg_key = (message.chat_id, message.id)

    delay = float(config.get('core.initial_edit_delay') or 0.0)
    if delay:
        _ie_cancel_evt = Event()
        _ie_ensure_evt = Event()
        _ie_task = asyncio.create_task(
            _delayed_initial_edit(
                message, code, delay, eval_ctx, _ie_cancel_evt, _ie_ensure_evt
            )
        )
        initial_edit_tasks[msg_key] = (_ie_cancel_evt, _ie_ensure_evt, _ie_task)
    else:
        await _initial_edit(message, code, eval_ctx)

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
        await cancel_initial_edit(message)
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


async def _delayed_initial_edit(
    message: Message,
    code: str,
    delay: float,
    ctx: Context,
    cancellation_event: Event,
    ensure_edit_event: Event,
):
    assert delay > 0
    try:
        await asyncio.wait_for(cancellation_event.wait(), timeout=delay)
        if ensure_edit_event.is_set():
            await _initial_edit(message, code, ctx)
        return
    except TimeoutError:
        pass

    # TODO: are these checks this really needed?
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

    await _initial_edit(updated_message, code, ctx)


async def _initial_edit(message: Message, code: str, ctx: Context):
    await message_design.edit_message(
        message,
        code,
        output=ctx.run(lambda: app.ctx._output) or '',
        is_running=True,
    )


async def cancel_initial_edit(message: Message, ensure_edit: bool = False):
    msg_key = (message.chat_id, message.id)
    if ie := initial_edit_tasks.pop(msg_key, None):
        cancel_evt, ensure_edit_evt, task = ie
        if ensure_edit:
            ensure_edit_evt.set()
        cancel_evt.set()
        await task


__all__ = ['eval_message', 'running_messages', 'cancel_initial_edit']
