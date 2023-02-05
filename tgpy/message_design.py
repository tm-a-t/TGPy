import sys
import traceback as tb
from dataclasses import dataclass
from typing import Optional

from telethon.tl.custom import Message
from telethon.tl.types import (
    MessageEntityBold,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextUrl,
)

from tgpy import app

TITLE = 'TGPy>'
TITLE_URL = 'https://github.com/tm-a-t/TGPy'
FORMATTED_ERROR_HEADER = f'<b><a href="{TITLE_URL}">TGPy error&gt;</a></b>'


class Utf16CodepointsWrapper(str):
    def __len__(self):
        return len(self.encode('utf-16-le')) // 2

    def __getitem__(self, item):
        s = self.encode('utf-16-le')
        if isinstance(item, slice):
            item = slice(
                item.start * 2 if item.start else None,
                item.stop * 2 if item.stop else None,
                item.step * 2 if item.step else None,
            )
            s = s[item]
        elif isinstance(item, int):
            s = s[item * 2 : item * 2 + 2]
        else:
            raise TypeError(f'{type(item)} is not supported')
        return s.decode('utf-16-le')


async def edit_message(
    message: Message,
    code: str,
    result: str,
    traceback: str = '',
    output: str = '',
) -> Message:
    if result is None and output:
        result = output
        output = ''

    title = Utf16CodepointsWrapper(TITLE)
    parts = [
        Utf16CodepointsWrapper(code.strip()),
        Utf16CodepointsWrapper(f'{title} {str(result).strip()}'),
    ]
    parts += [
        Utf16CodepointsWrapper(part)
        for part in (output.strip(), traceback.strip())
        if part
    ]

    entities = []
    offset = 0
    for p in parts:
        entities.append(MessageEntityCode(offset, len(p)))
        offset += len(p) + 2

    entities[0] = MessageEntityPre(entities[0].offset, entities[0].length, 'python')
    entities[1].offset += len(title) + 1
    entities[1].length -= len(title) + 1
    entities[1:1] = [
        MessageEntityBold(
            len(parts[0]) + 2,
            len(title),
        ),
        MessageEntityTextUrl(
            len(parts[0]) + 2,
            len(title),
            TITLE_URL,
        ),
    ]

    text = str('\n\n'.join(parts))
    if len(text) > 4096:
        text = text[:4095] + '…'
    return await message.edit(text, formatting_entities=entities, link_preview=False)


@dataclass
class MessageParseResult:
    is_tgpy_message: bool
    code: Optional[str]
    result: Optional[str]


def get_title_entity(message: Message) -> Optional[MessageEntityTextUrl]:
    for e in message.entities or []:
        if isinstance(e, MessageEntityTextUrl) and e.url == TITLE_URL:
            return e
    return None


def parse_message(message: Message) -> MessageParseResult:
    e = get_title_entity(message)
    if not e:
        return MessageParseResult(False, None, None)
    msg_text = Utf16CodepointsWrapper(message.raw_text)
    code = msg_text[: e.offset].strip()
    result = msg_text[e.offset + e.length :].strip()
    return MessageParseResult(True, code, result)


async def send_error(chat) -> None:
    exc = ''.join(tb.format_exception(*sys.exc_info()))
    if len(exc) > 4000:
        exc = exc[:4000] + '…'
    await app.client.send_message(
        chat,
        f'{FORMATTED_ERROR_HEADER}\n\n<code>{exc}</code>',
        link_preview=False,
        parse_mode='html',
    )


__all__ = [
    'edit_message',
    'MessageParseResult',
    'parse_message',
    'send_error',
]
