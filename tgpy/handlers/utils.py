from typing import Callable

from telethon.tl.custom import Message

from tgpy import message_design


def _handle_errors(func: Callable):
    async def result(message: Message):
        # noinspection PyBroadException
        try:
            await func(message)
        except Exception:
            await message_design.send_error(message.chat_id)

    return result


def outgoing_messages_filter(m: Message):
    return m.out and not m.forward and not m.via_bot
