from telethon import events
from telethon.tl.custom import Message

from app import client, message_design
from app.handlers.uitls import _handle_errors, outgoing_messages_filter
from app.run_code.parse_code import parse_code
from app.run_code import eval_message, get_kwargs


async def handle_message(message: Message) -> None:
    raw_text = message.raw_text

    if not raw_text:
        return

    if message.text.startswith('//') and message.text[2:].strip():
        await message.edit(message.text[2:])
        return

    locals_ = get_kwargs()

    res = parse_code(raw_text, locals_)
    if not res.is_code:
        return

    await eval_message(raw_text, message, uses_orig=res.uses_orig)


@client.on(events.NewMessage(func=outgoing_messages_filter))
@_handle_errors
async def on_new_message(event: events.NewMessage.Event) -> None:
    await handle_message(event.message)


@client.on(events.MessageEdited(func=outgoing_messages_filter))
@_handle_errors
async def on_message_edited(event: events.NewMessage.Event) -> None:
    code = message_design.get_code(event.message)
    if not code:
        await handle_message(event.message)
        return
    await eval_message(code, event.message, uses_orig=parse_code(code, get_kwargs()).uses_orig)


@client.on(events.NewMessage(pattern='(?i)^(cancel|сфтсуд)$', func=outgoing_messages_filter))
async def cancel(message: Message):
    prev = await message.get_reply_message()
    if not prev:
        async for msg in client.iter_messages(message.chat_id, max_id=message.id, limit=10):
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
