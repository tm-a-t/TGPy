"""
    name: restart
    origin: tgpy://builtin_module/restart
    priority: 500
"""

import os
import sys
from textwrap import dedent

from tgpy import app
from tgpy.modules import Module
from tgpy.utils import FILENAME_PREFIX


def restart(msg: str | None = 'Restarted successfully'):
    mod_code = dedent(
        f'''
        from tgpy.api.parse_tgpy_message import parse_tgpy_message
        from tgpy._core.message_design import edit_message
        msg = await client.get_messages({app.ctx.msg.chat_id}, ids={app.ctx.msg.id})
        await edit_message(msg, parse_tgpy_message(msg).code, '{msg}')
        '''
    )
    module = Module(
        name='__restart_message',
        once=True,
        code=mod_code,
        origin=f'{FILENAME_PREFIX}restart_message',
        priority=0,
    )
    module.save()
    os.execl(sys.executable, sys.executable, '-m', 'tgpy', *sys.argv[1:])


__all__ = ['restart']
