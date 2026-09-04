import sys
from collections.abc import Callable
from contextvars import ContextVar
from io import BytesIO, TextIOBase, TextIOWrapper
from typing import override

from telethon.tl.custom import Message

# TODO: move the whole Context in a ContextVar?
_is_module: ContextVar[bool] = ContextVar('_is_module')
_message: ContextVar[Message] = ContextVar('_message')
_stdout: ContextVar[BytesIO] = ContextVar('_stdout')
_stdout_wrapper: ContextVar[TextIOWrapper] = ContextVar('_stdout_wrapper')
_stderr: ContextVar[BytesIO] = ContextVar('_stderr')
_stderr_wrapper: ContextVar[TextIOWrapper] = ContextVar('_stderr_wrapper')
_flush_handler: ContextVar[Callable[[], None]] = ContextVar('_flush_handler')
_is_manual_output: ContextVar[bool] = ContextVar('_is_manual_output', default=False)


class FlushingBytesIO(BytesIO):
    @override
    def flush(self) -> None:
        super().flush()
        if flush_handler := _flush_handler.get(None):
            flush_handler()


class _ContextIOStream(TextIOBase):
    def __init__(self, contextvar: ContextVar[TextIOWrapper], fallback: TextIOWrapper):
        self.__contextvar = contextvar
        self.__fallback = fallback

    def __getobj(self) -> TextIOBase:
        return self.__contextvar.get(self.__fallback)

    @override
    def write(self, s: str) -> int:
        return self.__getobj().write(s)

    @override
    def flush(self) -> None:
        self.__getobj().flush()
        if flush_handler := _flush_handler.get(None):
            flush_handler()

    @override
    def writable(self) -> bool:
        return self.__getobj().writable()

    @override
    def isatty(self) -> bool:
        return self.__getobj().isatty()


sys.stdout = _ContextIOStream(_stdout_wrapper, sys.__stdout__)
sys.stderr = _ContextIOStream(_stderr_wrapper, sys.__stderr__)


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
    def msg(self) -> Message | None:
        return _message.get(None)

    @staticmethod
    def _set_msg(msg: Message):
        _message.set(msg)

    @staticmethod
    def _init_stdio(flush_handler: Callable[[], None]):
        stdout = FlushingBytesIO()
        _stdout.set(stdout)
        _stdout_wrapper.set(
            TextIOWrapper(stdout, line_buffering=True, encoding='utf-8')
        )

        stderr = FlushingBytesIO()
        _stderr.set(stderr)
        _stderr_wrapper.set(
            TextIOWrapper(stderr, line_buffering=True, encoding='utf-8')
        )

        _flush_handler.set(flush_handler)

    @property
    def _output(self) -> str | None:
        if _stderr.get(None) is None or _stdout.get(None) is None:
            return None
        stderr = cleanup_erases(_stderr.get().getvalue().decode())
        stdout = cleanup_erases(_stdout.get().getvalue().decode())
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
        return '<Context(is_manual_output, is_module, msg)>'
