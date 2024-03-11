import logging
from typing import Callable

from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import Channel

import tgpy.api
from tgpy import app, reactions_fix
from tgpy._core import message_design
from tgpy._core.eval_message import eval_message, running_messages
from tgpy.api.parse_code import parse_code
from tgpy.api.transformers import exec_hooks
from tgpy.api.utils import outgoing_messages_filter
from tgpy.reactions_fix import ReactionsFixResult

logger = logging.getLogger(__name__)


def _handle_errors(func: Callable):
    async def result(message: Message):
        # noinspection PyBroadException
        try:
            await func(message)
        except Exception:
            await message_design.send_error(message.chat_id)

    return result


async def handle_message(original_message: Message) -> Message:
    if not (message := await exec_hooks.apply(original_message, is_edit=False)):
        reactions_fix.update_hash(message, in_memory=True)
        return original_message

    res = await parse_code(message.raw_text)
    if not res.is_code:
        reactions_fix.update_hash(message, in_memory=True)
        return original_message

    return await eval_message(message.raw_text, message)


@events.register(events.NewMessage(func=outgoing_messages_filter))
@_handle_errors
async def on_new_message(event: events.NewMessage.Event) -> None:
    await handle_message(event.message)


@events.register(events.MessageEdited(func=outgoing_messages_filter))
@_handle_errors
async def on_message_edited(event: events.MessageEdited.Event) -> None:
    message: Message | None = event.message
    if isinstance(message.chat, Channel) and message.chat.broadcast:
        # Don't allow editing in channels, as the editor may not be the same account
        # which sent the message initially and there is no way to detect it
        return
    if (message.chat_id, message.id) in running_messages:
        # Message is already running, editing should do nothing.
        # The message will be corrected on the next flush or after evaluation finishes.
        return

    message_data = tgpy.api.parse_tgpy_message(message)
    reactions_fix_result = reactions_fix.check_hash(message)

    if reactions_fix_result == ReactionsFixResult.ignore:
        return
    elif reactions_fix_result == ReactionsFixResult.show_warning:
        code = message_data.code if message_data.is_tgpy_message else message.raw_text
        await message_design.edit_message(
            message, code, 'Edit message again to evaluate'
        )
        return
    elif reactions_fix_result == ReactionsFixResult.evaluate:
        pass
    else:
        raise ValueError(f'Bad reactions fix result: {reactions_fix_result}')

    if not message_data.is_tgpy_message:
        await handle_message(message)
        return

    if not (new_message := await exec_hooks.apply(message, is_edit=True)):
        return
    message_data = tgpy.api.parse_tgpy_message(new_message)
    if not message_data.is_tgpy_message:
        return
    await eval_message(message_data.code, new_message)


def add_handlers():
    app.client.add_event_handler(on_new_message)
    app.client.add_event_handler(on_message_edited)
