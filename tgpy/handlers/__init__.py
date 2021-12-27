from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import Channel

from tgpy import app, message_design
from tgpy.handlers.utils import _handle_errors, outgoing_messages_filter
from tgpy.run_code import eval_message, get_variable_names, parse_code


async def handle_message(message: Message) -> None:
    raw_text = message.raw_text

    if not raw_text:
        return

    if message.text.startswith('//') and message.text[2:].strip():
        await message.edit(message.text[2:])
        return

    locals_ = get_variable_names()

    res = parse_code(raw_text, locals_)
    if not res.is_code:
        return

    await eval_message(raw_text, message, uses_orig=res.uses_orig)


@events.register(events.NewMessage(func=outgoing_messages_filter))
@_handle_errors
async def on_new_message(event: events.NewMessage.Event) -> None:
    await handle_message(event.message)


@events.register(events.MessageEdited(func=outgoing_messages_filter))
@_handle_errors
async def on_message_edited(event: events.NewMessage.Event) -> None:
    if isinstance(event.message.chat, Channel) and event.message.chat.broadcast:
        return
    code = message_design.get_code(event.message)
    if not code:
        await handle_message(event.message)
        return
    await eval_message(
        code, event.message, uses_orig=parse_code(code, get_variable_names()).uses_orig
    )


@events.register(
    events.NewMessage(pattern='(?i)^(cancel|сфтсуд)$', func=outgoing_messages_filter)
)
async def cancel(message: Message):
    prev = await message.get_reply_message()
    if not prev:
        async for msg in app.client.iter_messages(
            message.chat_id, max_id=message.id, limit=10
        ):
            if msg.out and message_design.get_code(msg):
                prev = msg
                break
        else:
            return
    # noinspection PyBroadException
    try:
        await prev.edit(message_design.get_code(prev))
    except Exception:
        pass
    else:
        await message.delete()


def add_handlers():
    app.client.add_event_handler(on_new_message)
    app.client.add_event_handler(on_message_edited)
    app.client.add_event_handler(cancel)
