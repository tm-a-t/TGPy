import sys
import traceback as tb

from telethon.tl.custom import Message
from telethon.tl.types import MessageEntityBold, MessageEntityCode, MessageEntityTextUrl

from tgpy import app

TITLE = 'TGPy>'
TITLE_URL = 'https://github.com/tm-a-t/TGPy'
FORMATTED_ERROR_HEADER = f'<b><a href="{TITLE_URL}">TGPy error&gt;</a></b>'


def utf16_codepoints_len(s: str):
    return len(s.encode('utf-16-le')) // 2


def utf16_codepoints_prefix(s: str, length: int):
    s = s.encode('utf-16-le')
    s = s[: length * 2]
    return s.decode('utf-16-le')


async def edit_message(
    message: Message, code: str, result, traceback: str = '', output: str = ''
) -> None:
    if result is None and output:
        result = output
        output = ''

    parts = [code.strip(), f'{TITLE} {str(result).strip()}']
    parts += [part for part in (output.strip(), traceback.strip()) if part]
    text = '\n\n'.join(parts)

    entities = []
    offset = 0
    for p in parts:
        entities.append(MessageEntityCode(offset, utf16_codepoints_len(p)))
        offset += utf16_codepoints_len(p) + 2

    entities[1].offset += utf16_codepoints_len(TITLE) + 1
    entities[1].length -= utf16_codepoints_len(TITLE) + 1
    entities[1:1] = [
        MessageEntityBold(
            utf16_codepoints_len(parts[0]) + 2,
            utf16_codepoints_len(TITLE),
        ),
        MessageEntityTextUrl(
            utf16_codepoints_len(parts[0]) + 2,
            utf16_codepoints_len(TITLE),
            TITLE_URL,
        ),
    ]

    if len(text) > 4096:
        text = text[:4095] + '…'
    await message.edit(text, formatting_entities=entities, link_preview=False)


def get_code(message: Message) -> str:
    for e in message.entities or []:
        if isinstance(e, MessageEntityTextUrl) and e.url == TITLE_URL:
            return utf16_codepoints_prefix(message.raw_text, length=e.offset).strip()
    return ''


async def send_error(chat) -> None:
    exc = ''.join(tb.format_exception(*sys.exc_info()))
    if len(exc) > 4000:
        exc = exc[:4000] + '…'
    await app.client.send_message(
        chat, f'{FORMATTED_ERROR_HEADER}\n\n<code>{exc}</code>', link_preview=False
    )
