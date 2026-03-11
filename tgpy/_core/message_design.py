import sys
import traceback as tb

from telethon.tl.custom import Message
from telethon.tl.types import (
    MessageEntityBold,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextUrl,
    TypeMessageEntity,
)

from tgpy import app, reactions_fix
from tgpy.api.utils import Utf16CodepointsWrapper

TITLE = 'TGPy>'
RUNNING_TITLE = 'TGPy running>'
OLD_TITLE_URLS = ['https://github.com/tm-a-t/TGPy', 'https://tgpy.tmat.me/']
TITLE_URL = 'https://tgpy.dev/'
FORMATTED_ERROR_HEADER = f'<b><a href="{TITLE_URL}">TGPy error&gt;</a></b>'


async def edit_message(
    message: Message,
    code: str,
    result: str | None = '',
    traceback: str = '',
    output: str = '',
    is_running: bool = False,
) -> Message:
    output_parts = [result, output, traceback]
    if not result and any(output_parts):
        # if result is None, but there is output/traceback, don't show None
        output_parts.pop(0)
    output_parts = [str(x) for x in output_parts]
    output_parts = [x for x in output_parts if x.strip()]
    # make sure there are no trailing spaces
    for i in range(len(output_parts) - 1, -1, -1):
        if not output_parts[i].rstrip():
            output_parts.pop(i)
        else:
            output_parts[i] = output_parts[i].rstrip()
            break

    parts: list[tuple[str, list[type[TypeMessageEntity]]]] = [
        (code.strip(), [MessageEntityPre]),
        ('\n\n', []),
        (
            RUNNING_TITLE if is_running else TITLE,
            [MessageEntityBold, MessageEntityTextUrl],
        ),
    ]
    if output_parts:
        parts.append((' ', []))
        parts.extend([
            (part + ('\n' if i != len(output_parts) - 1 else ''), [MessageEntityCode])
            for i, part in enumerate(output_parts)
        ])

    entities = []
    offset = 0
    for i, (part, ent_classes) in enumerate(parts):
        part = Utf16CodepointsWrapper(part)
        for ent_cls in ent_classes:
            if ent_cls is MessageEntityPre:
                entities.append(MessageEntityPre(offset, len(part), 'python'))
            elif ent_cls is MessageEntityBold or ent_cls is MessageEntityCode:
                entities.append(ent_cls(offset, len(part)))
            elif ent_cls is MessageEntityTextUrl:
                entities.append(MessageEntityTextUrl(offset, len(part), TITLE_URL))
            else:
                raise ValueError(f'Unknown entity class {ent_cls}')
        offset += len(part)

    text = str(''.join(part for part, _ in parts))
    if len(text) > 4096:
        text = text[:4095] + '…'
    for ent in entities:
        if ent.offset >= 4096:
            ent.offset = 0
            ent.length = 0
        elif ent.offset + ent.length > 4096:
            ent.length = 4096 - ent.offset

    res = await message.edit(text, formatting_entities=entities, link_preview=False)
    reactions_fix.update_hash(res, in_memory=False)
    return res


def get_title_entity(message: Message) -> MessageEntityTextUrl | None:
    for e in message.entities or []:
        if isinstance(e, MessageEntityTextUrl) and (
            e.url in OLD_TITLE_URLS or e.url == TITLE_URL
        ):
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
