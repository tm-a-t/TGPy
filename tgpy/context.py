import sys
from contextvars import ContextVar
from io import StringIO, TextIOBase

from telethon.tl.custom import Message

_is_module: ContextVar[bool] = ContextVar('_is_module')
_message: ContextVar[Message] = ContextVar('_message')
_stdout: ContextVar[StringIO] = ContextVar('_stdout')
_is_manual_output: ContextVar[bool] = ContextVar('_is_manual_output', default=False)


class _StdoutWrapper(TextIOBase):
    def __getobj(self):
        return _stdout.get(sys.__stdout__)

    def write(self, s: str) -> int:
        return self.__getobj().write(s)

    def flush(self) -> None:
        return self.__getobj().flush()

    @property
    def isatty(self):
        return getattr(self.__getobj(), 'isatty', None)


sys.stdout = _StdoutWrapper()


class Context:
    @property
    def is_module(self) -> bool:
        return _is_module.get(False)

    @staticmethod
    def _set_is_module(is_module: bool):
        _is_module.set(is_module)

    @property
    def msg(self) -> Message:
        return _message.get(None)

    @staticmethod
    def _set_msg(msg: Message):
        _message.set(msg)

    @staticmethod
    def _init_stdout():
        _stdout.set(StringIO())

    @property
    def _stdout(self) -> str:
        return _stdout.get().getvalue()

    @property
    def is_manual_output(self):
        return _is_manual_output.get()

    @is_manual_output.setter
    def is_manual_output(self, value: bool):
        _is_manual_output.set(value)

    def __str__(self):
        return f'<Context(is_manual_output, is_module, msg)>'
