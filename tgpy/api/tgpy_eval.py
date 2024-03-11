import asyncio
import time
from dataclasses import dataclass
from typing import Any

from telethon.tl.custom import Message

import tgpy.api
from tgpy import app
from tgpy._core import message_design
from tgpy._core.meval import _meval
from tgpy.api.parse_code import parse_code
from tgpy.utils import FILENAME_PREFIX, numid

variables: dict[str, Any] = {}
constants: dict[str, Any] = {}


@dataclass
class EvalResult:
    result: Any
    output: str


class Flusher:
    _code: str
    _message: Message | None
    _flushed_output: str
    _flush_timer: asyncio.Task | None
    _finished: bool

    def __init__(self, code: str, message: Message | None):
        self._code = code
        self._message = message
        self._flushed_output = ''
        self._flush_timer = None
        self._finished = False

    async def _wait_and_flush(self):
        await asyncio.sleep(3)
        await message_design.edit_message(
            self._message,
            self._code,
            output=self._flushed_output,
            is_running=True,
        )
        self._flush_timer = None

    def flush_handler(self):
        if not self._message or self._finished:
            return
        # noinspection PyProtectedMember
        self._flushed_output = app.ctx._output
        if self._flush_timer:
            # flush already scheduled, will print the latest output
            return
        self._flush_timer = asyncio.create_task(self._wait_and_flush())

    def set_finished(self):
        if self._flush_timer:
            self._flush_timer.cancel()
        self._finished = True


async def tgpy_eval(
    code: str,
    message: Message | None = None,
    *,
    filename: str | None = None,
) -> EvalResult:
    parsed = await parse_code(code, ignore_simple=False)
    if not parsed.is_code:
        if parsed.exc:
            raise parsed.exc
        else:
            raise ValueError('Invalid code provided')

    if message:
        await message_design.edit_message(message, code, is_running=True)

    flusher = Flusher(code, message)

    # noinspection PyProtectedMember
    app.ctx._init_stdio(flusher.flush_handler)
    kwargs = {'msg': message}
    if message:
        # noinspection PyProtectedMember
        app.ctx._set_msg(message)
    if not filename:
        if message:
            filename = f'{FILENAME_PREFIX}message/{message.chat_id}/{message.id}'
        else:
            filename = f'{FILENAME_PREFIX}eval/{numid()}'
    if parsed.uses_orig:
        if message:
            orig = await message.get_reply_message()
            kwargs['orig'] = orig
        else:
            kwargs['orig'] = None

    try:
        new_variables, result = await _meval(
            parsed,
            filename,
            tgpy.api.variables,
            **tgpy.api.constants,
            **kwargs,
        )
    finally:
        flusher.set_finished()
    if '__all__' in new_variables:
        new_variables = {
            k: v for k, v in new_variables.items() if k in new_variables['__all__']
        }
    tgpy.api.variables.update(new_variables)

    # noinspection PyProtectedMember
    return EvalResult(
        result=result,
        output=app.ctx._output,
    )


__all__ = ['variables', 'constants', 'EvalResult', 'tgpy_eval']
