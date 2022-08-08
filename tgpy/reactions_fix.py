"""
This module tries to fix Telegram bug/undocumented feature where
setting/removing reaction sometimes triggers message edit event.
This bug/feature introduces a security vulnerability in TGPy,
because message reevaluation can be triggered by other users.
"""
import json
from enum import Enum
from hashlib import sha256

from telethon.tl.custom import Message

content_hashes: dict[tuple[int, int], bytes] = {}


def get_content_hash(message: Message) -> bytes:
    entities = [json.dumps(e.to_dict()) for e in message.entities or []]
    data = str(len(entities)) + '\n' + '\n'.join(entities) + message.raw_text
    return sha256(data.encode('utf-8')).digest()


class ReactionsFixResult(Enum):
    ignore = 1
    evaluate = 2
    show_warning = 3


def check_hash(message: Message) -> ReactionsFixResult:
    message_uid = (message.chat_id, message.id)
    content_hash = get_content_hash(message)
    if message_uid not in content_hashes:
        return ReactionsFixResult.show_warning
    if content_hashes[message_uid] == content_hash:
        return ReactionsFixResult.ignore
    return ReactionsFixResult.evaluate


def update_hash(message: Message) -> None:
    message_uid = (message.chat_id, message.id)
    content_hashes[message_uid] = get_content_hash(message)


__all__ = ['ReactionsFixResult', 'check_hash', 'update_hash']
