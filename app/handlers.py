from typing import Callable

from telethon import events
from telethon.tl.custom import Message

from app import client, message_design
from app.parse_code import parse_code
from app.run_code import eval_message


def _handle_errors(func: Callable):
    async def result(message: Message):
        # noinspection PyBroadException
        try:
            await func(message)
        except Exception:
            await message_design.send_error(message.chat_id)

    return result


def filter(m: Message):
    return not (m.forward or m.via_bot) and m.out


@client.on(events.NewMessage(func=filter))
@_handle_errors
async def on_new_message(message: Message) -> None:
    text = message.raw_text

    if not text:
        return

    if text.startswith('//'):
        await message.edit(text[2:])
        return

    res = parse_code(text)
    if not res.is_code:
        return

    await eval_message(text, message, uses_orig=res.uses_orig)


@client.on(events.MessageEdited(func=filter))
@_handle_errors
async def on_message_edited(message: Message) -> None:
    code = message_design.get_code(message)
    if not code:
        return
    await eval_message(code, message, uses_orig=parse_code(code).uses_orig)


@client.on(events.NewMessage(pattern='^(cancel|сфтсуд)$', func=filter))
async def cancel(message: Message):
    prev = await message.get_reply_message()
    if not prev:
        me = await client.get_me()
        async for prev in client.iter_messages(message.chat_id, max_id=message.id, limit=10):
            if prev.sender_id != me.id:
                continue
            if message_design.get_code(prev):
                break
        else:
            return
    try:
        await prev.edit(message_design.get_code(prev))
    except Exception:
        pass
    else:
        await message.delete()
