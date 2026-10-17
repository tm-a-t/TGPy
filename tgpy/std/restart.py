"""
name: restart
origin: tgpy://builtin_module/restart
priority: 500
"""

import os
import sys
from textwrap import dedent

from tgpy import app
from tgpy.api import cancel_initial_edit
from tgpy.context import Context
from tgpy.modules import Module
from tgpy.utils import FILENAME_PREFIX

ctx: Context


async def restart(msg: str | None = 'Restarted successfully'):
    mod_code = dedent(
        f"""
        from tgpy.api.parse_tgpy_message import parse_tgpy_message
        from tgpy._core.message_design import edit_message
        msg = await client.get_messages({app.ctx.msg.chat_id}, ids={app.ctx.msg.id})
        if not msg or not (parsed := parse_tgpy_message(msg)).is_tgpy_message:
            return
        await edit_message(msg, parsed.code, '{msg}')
        """
    )
    module = Module(
        name='__restart_message',
        once=True,
        code=mod_code,
        origin=f'{FILENAME_PREFIX}restart_message',
        priority=0,
    )
    module.save()
    await cancel_initial_edit(ctx.msg, ensure_edit=True)
    os.execl(sys.executable, sys.executable, *sys.argv)


__all__ = ['restart']
