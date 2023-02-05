from typing import Optional

from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import Channel

from tgpy import app, message_design, reactions_fix
from tgpy.handlers.utils import _handle_errors, outgoing_messages_filter
from tgpy.reactions_fix import ReactionsFixResult
from tgpy.run_code import eval_message, get_variable_names, parse_code


async def handle_message(
    message: Message, *, only_show_warning: bool = False
) -> Optional[Message]:
    if not message.raw_text:
        return message

    if message.raw_text.startswith('//') and message.raw_text[2:].strip():
        entities = message.entities or []
        for ent in entities:
            if ent.offset < 2:
                ent.length -= 2 - ent.offset
                ent.offset = 0
            else:
                ent.offset -= 2
        return await message.edit(message.raw_text[2:], formatting_entities=entities)

    locals_ = get_variable_names()

    res = parse_code(message.raw_text, locals_)
    if not res.is_code:
        return message

    if only_show_warning:
        return await message_design.edit_message(
            message,
            message.raw_text,
            'Edit message again to evaluate',
        )
    else:
        return await eval_message(message.raw_text, message, res.uses_orig)


@events.register(events.NewMessage(func=outgoing_messages_filter))
@_handle_errors
async def on_new_message(event: events.NewMessage.Event) -> None:
    message = await handle_message(event.message)
    if message is not None:
        reactions_fix.update_hash(message)


@events.register(events.MessageEdited(func=outgoing_messages_filter))
@_handle_errors
async def on_message_edited(event: events.MessageEdited.Event) -> None:
    message: Message = event.message
    if isinstance(message.chat, Channel) and message.chat.broadcast:
        return
    message_data = message_design.parse_message(message)
    reactions_fix_result = reactions_fix.check_hash(message)
    try:
        if reactions_fix_result == ReactionsFixResult.ignore:
            return
        elif reactions_fix_result == ReactionsFixResult.show_warning:
            if message_data.is_tgpy_message:
                message = await message_design.edit_message(
                    message, message_data.code, 'Edit message again to evaluate'
                )
            else:
                message = await handle_message(message, only_show_warning=True)
            return
        elif reactions_fix_result == ReactionsFixResult.evaluate:
            pass
        else:
            raise ValueError(f'Bad reactions fix result: {reactions_fix_result}')

        if not message_data.is_tgpy_message:
            message = await handle_message(message)
            return
        message = await eval_message(
            message_data.code,
            message,
            parse_code(message_data.code, get_variable_names()).uses_orig,
        )
    finally:
        if message is not None:
            reactions_fix.update_hash(message)


@events.register(
    events.NewMessage(pattern='(?i)^(cancel|сфтсуд)$', func=outgoing_messages_filter)
)
async def cancel(message: Message):
    prev: Message = await message.get_reply_message()
    if not prev:
        async for msg in app.client.iter_messages(
            message.chat_id, max_id=message.id, limit=10
        ):
            if msg.out and message_design.parse_message(msg).is_tgpy_message:
                prev = msg
                break
        else:
            return
    # noinspection PyBroadException
    try:
        edit_result = await prev.edit(message_design.parse_message(prev).code)
    except Exception:
        return

    if edit_result is not None:
        await message.delete()


def add_handlers():
    app.client.add_event_handler(on_new_message)
    app.client.add_event_handler(on_message_edited)
    app.client.add_event_handler(cancel)
