"""
    name: prevent_eval
    origin: tgpy://builtin_module/prevent_eval
    priority: 400
"""

import re

from telethon import TelegramClient
from telethon.tl.custom import Message

import tgpy.api
from tgpy import Context

client: TelegramClient
ctx: Context

MODULE_NAME = 'prevent_eval'
IGNORED_MESSAGES_KEY = f'{MODULE_NAME}.ignored_messages'
CANCEL_RGX = re.compile(r'(?i)^(cancel|сфтсуд)$')


async def handle_cancel(message: Message):
    prev: Message = await message.get_reply_message()
    if prev:
        parsed = tgpy.api.parse_tgpy_message(prev)
    else:
        async for msg in client.iter_messages(
            message.chat_id, max_id=message.id, limit=10
        ):
            if not msg.out:
                continue
            parsed = tgpy.api.parse_tgpy_message(msg)
            if parsed.is_tgpy_message:
                prev = msg
                break
        else:
            return

    ignored_messages = tgpy.api.config.get(IGNORED_MESSAGES_KEY, [])
    ignored_messages.append([prev.chat_id, prev.id])
    tgpy.api.config.save()

    # noinspection PyBroadException
    try:
        edit_result = await prev.edit(parsed.code)
    except Exception:
        return

    if edit_result is not None:
        await message.delete()


async def handle_comment(message: Message):
    ignored_messages = tgpy.api.config.get(IGNORED_MESSAGES_KEY, [])
    ignored_messages.append([message.chat_id, message.id])
    tgpy.api.config.save()

    entities = message.entities or []
    for ent in entities:
        if ent.offset < 2:
            ent.length -= 2 - ent.offset
            ent.offset = 0
        else:
            ent.offset -= 2
    await message.edit(message.raw_text[2:], formatting_entities=entities)


async def exec_hook(message: Message, is_edit: bool):
    ignored_messages = tgpy.api.config.get(IGNORED_MESSAGES_KEY, [])
    if [message.chat_id, message.id] in ignored_messages:
        return False

    is_comment = message.raw_text.startswith('//') and message.raw_text[2:].strip()
    is_cancel = CANCEL_RGX.fullmatch(message.raw_text) is not None
    if not is_comment and not is_cancel:
        return True

    if is_cancel:
        await handle_cancel(message)
    elif is_comment:
        await handle_comment(message)

    return False


tgpy.api.exec_hooks.add(MODULE_NAME, exec_hook)

__all__ = []
