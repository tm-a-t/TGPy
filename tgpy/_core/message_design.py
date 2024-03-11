import sys
import traceback as tb

from telethon.tl.custom import Message
from telethon.tl.types import (
    MessageEntityBold,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextUrl,
)

from tgpy import app, reactions_fix

TITLE = 'TGPy>'
RUNNING_TITLE = 'TGPy running>'
OLD_TITLE_URL = 'https://github.com/tm-a-t/TGPy'
TITLE_URL = 'https://tgpy.tmat.me/'
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
    result: str = '',
    traceback: str = '',
    output: str = '',
    is_running: bool = False,
) -> Message:
    if not result and output:
        result = output
        output = ''
    if not result and traceback:
        result = traceback
        traceback = ''

    if is_running:
        title = Utf16CodepointsWrapper(RUNNING_TITLE)
    else:
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
    for i, p in enumerate(parts):
        entities.append(MessageEntityCode(offset, len(p)))
        newline_cnt = 1 if i == 1 else 2
        offset += len(p) + newline_cnt

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

    text = str(''.join(x + ('\n' if i == 1 else '\n\n') for i, x in enumerate(parts)))
    if len(text) > 4096:
        text = text[:4095] + '…'
    res = await message.edit(text, formatting_entities=entities, link_preview=False)
    reactions_fix.update_hash(res, in_memory=False)
    return res


def get_title_entity(message: Message) -> MessageEntityTextUrl | None:
    for e in message.entities or []:
        if isinstance(e, MessageEntityTextUrl) and e.url in (OLD_TITLE_URL, TITLE_URL):
            return e
    return None


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
    'send_error',
]
