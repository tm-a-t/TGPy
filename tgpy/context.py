import sys
from contextvars import ContextVar
from io import StringIO, TextIOBase

from telethon.tl.custom import Message

_message: ContextVar[Message] = ContextVar('_message')
_stdout: ContextVar[StringIO] = ContextVar('_stdout')


class _StdoutWrapper(TextIOBase):
    def __getobj(self):
        return _stdout.get(sys.__stdout__)

    def write(self, s: str) -> int:
        return self.__getobj().write(s)


sys.stdout = _StdoutWrapper()


class Context:
    @property
    def msg(self):
        return _message.get(None)

    @msg.setter
    def msg(self, msg: Message):
        _message.set(msg)

    def _init_stdout(self):
        _stdout.set(StringIO())

    @property
    def _stdout(self):
        return _stdout.get().getvalue()

    def __str__(self):
        return f'<Context(msg)>'
