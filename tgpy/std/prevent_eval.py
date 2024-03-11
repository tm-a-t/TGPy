"""
    name: prevent_eval
    origin: tgpy://builtin_module/prevent_eval
    priority: 400
"""

import re

from telethon import TelegramClient
from telethon.tl.custom import Message

import tgpy.api
from tgpy import Context, reactions_fix
from tgpy._core.eval_message import running_messages

client: TelegramClient
ctx: Context

MODULE_NAME = 'prevent_eval'
IGNORED_MESSAGES_KEY = f'{MODULE_NAME}.ignored_messages'
CANCEL_RGX = re.compile(r'(?i)^(cancel|сфтсуд)$')
INTERRUPT_RGX = re.compile(r'(?i)^(stop|ыещз)$')


async def cancel_message(message: Message, permanent: bool = True) -> None:
    parsed = tgpy.api.parse_tgpy_message(message)

    if task := running_messages.get((message.chat_id, message.id)):
        task.cancel()
    message = await message.edit(parsed.code)

    if permanent:
        ignored_messages = tgpy.api.config.get(IGNORED_MESSAGES_KEY, [])
        ignored_messages.append([message.chat_id, message.id])
        tgpy.api.config.save()
    else:
        reactions_fix.update_hash(message)


async def handle_cancel(message: Message, permanent: bool = True):
    target: Message = await message.get_reply_message()
    if not target:
        async for msg in client.iter_messages(
            message.chat_id, max_id=message.id, limit=10
        ):
            if not msg.out:
                continue
            parsed = tgpy.api.parse_tgpy_message(msg)
            if parsed.is_tgpy_message:
                target = msg
                break

    if not target:
        return

    await cancel_message(target, permanent)
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
    is_interrupt = INTERRUPT_RGX.fullmatch(message.raw_text) is not None
    if not is_comment and not is_cancel and not is_interrupt:
        return True

    if is_cancel or is_interrupt:
        await handle_cancel(message, permanent=is_cancel)
    elif is_comment:
        await handle_comment(message)

    return False


tgpy.api.exec_hooks.add(MODULE_NAME, exec_hook)

__all__ = []
