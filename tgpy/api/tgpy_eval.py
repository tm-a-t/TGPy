import asyncio
from contextvars import Context, copy_context
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
    output: str | None


class Flusher:
    _code: str
    _message: Message | None
    _flushed_output: str
    _flush_timer: asyncio.Task[None] | None
    _finished: bool
    _flush_requested: bool

    def __init__(self, code: str, message: Message | None):
        self._code = code
        self._message = message
        self._flushed_output = ''
        self._flush_timer = None
        self._finished = False
        self._flush_requested = False

    async def _flush_and_wait(self):
        if self._message is None:
            return

        from tgpy._core.eval_message import initial_edit_tasks

        msg_key = (self._message.chat_id, self._message.id)
        if initial_edit_task := initial_edit_tasks.pop(msg_key, None):
            initial_edit_task.cancel()

        await message_design.edit_message(
            self._message,
            self._code,
            output=self._flushed_output,
            is_running=True,
        )
        await asyncio.sleep(3)

        self._flush_timer = None
        if self._flush_requested:
            self._flush_requested = False
            self.flush_handler()

    def flush_handler(self):
        if not self._message or self._finished or app.ctx.is_manual_output:
            return

        if app.ctx._output is None or self._flushed_output == app.ctx._output:
            # Nothing has changed, flush is no-op
            return

        if self._flush_timer is None:
            # noinspection PyProtectedMember
            self._flushed_output = app.ctx._output

            self._flush_timer = asyncio.create_task(self._flush_and_wait())
        else:
            self._flush_requested = True

    def set_finished(self):
        if self._flush_timer:
            self._flush_timer.cancel()
        self._finished = True


async def _tgpy_eval(
    code: str,
    message: Message | None = None,
    *,
    filename: str | None = None,
    wrap_stdio: bool = True,
) -> EvalResult:
    parsed = await parse_code(code, ignore_simple=False)
    if not parsed.is_code:
        if parsed.exc:
            raise parsed.exc
        else:
            raise ValueError('Invalid code provided')

    flusher = Flusher(code, message)

    if wrap_stdio:
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

    if parsed.quiet:
        result = None

    # noinspection PyProtectedMember
    return EvalResult(
        result=result,
        output=app.ctx._output,
    )


async def tgpy_eval(
    code: str,
    message: Message | None = None,
    *,
    filename: str | None = None,
    wrap_stdio: bool = True,
    ctx: Context | None = None,
) -> EvalResult:
    eval_ctx = ctx or copy_context()
    return await asyncio.create_task(
        _tgpy_eval(code, message, filename=filename, wrap_stdio=wrap_stdio),
        context=eval_ctx,
    )


__all__ = ['variables', 'constants', 'EvalResult', 'tgpy_eval']
