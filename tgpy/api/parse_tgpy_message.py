from dataclasses import dataclass

from telethon.tl.custom import Message

from tgpy._core.message_design import Utf16CodepointsWrapper, get_title_entity


@dataclass
class MessageParseResult:
    is_tgpy_message: bool
    code: str | None
    result: str | None


def parse_tgpy_message(message: Message) -> MessageParseResult:
    e = get_title_entity(message)
    if not e:
        return MessageParseResult(False, None, None)
    msg_text = Utf16CodepointsWrapper(message.raw_text)
    code = msg_text[: e.offset].strip()
    result = msg_text[e.offset + e.length :].strip()
    return MessageParseResult(True, code, result)


__all__ = ['MessageParseResult', 'parse_tgpy_message']
