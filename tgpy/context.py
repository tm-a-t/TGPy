from contextvars import ContextVar
from typing import Optional

from telethon.tl.custom import Message


class Context:
    __print_output: ContextVar[str]
    __msg: ContextVar[Optional[Message]]

    def __init__(self):
        self.__msg = ContextVar('msg')
        self.__print_output = ContextVar('print_output', default='')

    @property
    def msg(self):
        return self.__msg.get(None)

    @msg.setter
    def msg(self, msg: Message):
        self.__msg.set(msg)

    @property
    def _print_output(self):
        return self.__print_output.get()

    def _print(self, *values, sep=' ', end='\n', file=None, flush=True):
        if file:
            print(*values, sep=sep, end=end, file=file, flush=flush)
        else:
            output = sep.join(str(val) for val in values) + end
            self.__print_output.set(self.__print_output.get() + output)

    def __str__(self):
        return f'<Context(msg)>'
