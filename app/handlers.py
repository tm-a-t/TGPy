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


@client.on(events.NewMessage(outgoing=True, forwards=False, func=lambda m: not m.via_bot))
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


@client.on(events.MessageEdited(outgoing=True, func=lambda m: not m.via_bot))
@_handle_errors
async def on_message_edited(message: Message) -> None:
    code = message_design.get_code(message)
    if not code:
        return
    await eval_message(code, message)


@client.on(events.NewMessage(pattern='^(cancel|сфтсуд)$'))
async def cancel(message: Message):
    prev = await message.get_reply_message()
    if not prev:
        return
    try:
        await prev.edit(message_design.get_code(prev))
    except Exception:
        pass
    else:
        await message.delete()
