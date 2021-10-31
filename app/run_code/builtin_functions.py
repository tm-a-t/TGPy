import getpass
import os
import socket
import sys
from textwrap import dedent

from app import client
from app.data.hooks import Hook, HookType
from app.run_code import variables
from app.run_code.utils import Context, filename_prefix
from app.utils import run_cmd, get_base_dir, get_commit

ctx = Context()


def ping():
    return f'Pong!\n' \
           f'Running on {getpass.getuser()}@{socket.gethostname()}\n' \
           f'Commit: {get_commit()}'


def restart():
    os.chdir(get_base_dir())
    os.execl(sys.executable, sys.executable, '-m', 'app', *sys.argv[1:])


def update():
    run_cmd(['git', 'pull'])
    hook_code = dedent(f'''
        from app.message_design import edit_message, get_code
        msg = await client.get_messages({ctx.msg.chat_id}, ids={ctx.msg.id})
        await edit_message(msg, get_code(msg), 'Updated successfuly! Current commit: {get_commit()}')
    ''')
    hook = Hook(
        name='__post_update',
        type=HookType.onstart,
        once=True,
        save_locals=False,
        code=hook_code,
        origin=f'{filename_prefix}post_update'
    )
    hook.save()
    restart()


variables['ctx'] = ctx
variables['ping'] = ping
variables['restart'] = restart
variables['update'] = update

# other default variables might be here
