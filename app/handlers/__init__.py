from telethon import events
from telethon.tl.custom import Message

from app import client, message_design
from app.handlers.uitls import _handle_errors, outgoing_messages_filter
from app.run_code.parse_code import parse_code
from app.run_code import eval_message


async def handle_message(message: Message) -> None:
    raw_text = message.raw_text

    if not raw_text:
        return

    if message.text.startswith('//'):
        await message.edit(message.text[2:])
        return

    res = parse_code(raw_text)
    if not res.is_code:
        return

    await eval_message(raw_text, message, uses_orig=res.uses_orig)


@client.on(events.NewMessage(func=outgoing_messages_filter))
@_handle_errors
async def on_new_message(message: Message) -> None:
    await handle_message(message)


@client.on(events.MessageEdited(func=outgoing_messages_filter))
@_handle_errors
async def on_message_edited(message: Message) -> None:
    code = message_design.get_code(message)
    if not code:
        await handle_message(message)
        return
    await eval_message(code, message, uses_orig=parse_code(code).uses_orig)


@client.on(events.NewMessage(pattern='^(cancel|сфтсуд)$', func=outgoing_messages_filter))
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
