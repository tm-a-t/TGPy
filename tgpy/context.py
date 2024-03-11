import sys
from contextvars import ContextVar
from io import StringIO, TextIOBase
from typing import Callable

from telethon.tl.custom import Message

_is_module: ContextVar[bool] = ContextVar('_is_module')
_message: ContextVar[Message] = ContextVar('_message')
_stdout: ContextVar[StringIO] = ContextVar('_stdout')
_stderr: ContextVar[StringIO] = ContextVar('_stderr')
_flush_handler: ContextVar[Callable[[], None]] = ContextVar('_flush_handler')
_is_manual_output: ContextVar[bool] = ContextVar('_is_manual_output', default=False)


class _StdoutWrapper(TextIOBase):
    def __init__(self, contextvar, fallback):
        self.__contextvar = contextvar
        self.__fallback = fallback

    def __getobj(self):
        return self.__contextvar.get(self.__fallback)

    def write(self, s: str) -> int:
        return self.__getobj().write(s)

    def flush(self) -> None:
        self.__getobj().flush()
        if flush_handler := _flush_handler.get(None):
            flush_handler()

    @property
    def isatty(self):
        return getattr(self.__getobj(), 'isatty', None)


sys.stdout = _StdoutWrapper(_stdout, sys.__stdout__)
sys.stderr = _StdoutWrapper(_stderr, sys.__stderr__)


def cleanup_erases(data: str):
    lines = data.replace('\r\n', '\n').split('\n')
    return '\n'.join(x.rsplit('\r', 1)[-1] for x in lines)


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
    def _init_stdio(flush_handler: Callable[[], None]):
        _stdout.set(StringIO())
        _stderr.set(StringIO())
        _flush_handler.set(flush_handler)

    @property
    def _output(self) -> str:
        stderr = cleanup_erases(_stderr.get().getvalue())
        stdout = cleanup_erases(_stdout.get().getvalue())
        if stderr and stderr[-1] != '\n':
            stderr += '\n'
        return stderr + stdout

    @property
    def is_manual_output(self):
        return _is_manual_output.get()

    @is_manual_output.setter
    def is_manual_output(self, value: bool):
        _is_manual_output.set(value)

    def __str__(self):
        return f'<Context(is_manual_output, is_module, msg)>'
