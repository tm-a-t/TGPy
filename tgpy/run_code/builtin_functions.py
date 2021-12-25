import getpass
import os
import socket
import sys
from textwrap import dedent
from typing import Optional

import datetime as dt

from tgpy.hooks import Hook, HookType, delete_hook_file, get_sorted_hooks
from tgpy.message_design import get_code
from tgpy.run_code import variables
from tgpy.run_code.utils import Context, filename_prefix, save_function_to_variables
from tgpy.utils import run_cmd, get_version, BASE_DIR

variables['ctx'] = ctx = Context()


@save_function_to_variables
def ping():
    return f'Pong!\n' \
           f'Running on {getpass.getuser()}@{socket.gethostname()}\n' \
           f'Version: {get_version()}'


@save_function_to_variables
def restart(msg: Optional[str] = 'Restarted successfully'):
    hook_code = dedent(f'''
        from tgpy.message_design import edit_message, get_code
        msg = await client.get_messages({ctx.msg.chat_id}, ids={ctx.msg.id})
        await edit_message(msg, get_code(msg), '{msg}')
    ''')
    hook = Hook(
        name='__restart_message',
        type=HookType.onstart,
        once=True,
        save_locals=False,
        code=hook_code,
        origin=f'{filename_prefix}restart_message',
        datetime=dt.datetime.fromtimestamp(0),
    )
    hook.save()
    os.chdir(BASE_DIR)
    os.execl(sys.executable, sys.executable, '-m', 'tgpy', *sys.argv[1:])


@save_function_to_variables
def update():
    run_cmd(['git', 'pull'])
    restart(f'Updated successfuly! Current version: {get_version()}')


class HooksObject:
    async def add(self, name: str, code: Optional[str] = None) -> str:
        if code is None:
            original = await ctx.msg.get_reply_message()
            if original is None:
                return 'Use this function in reply to a message'
            code = get_code(original)
            origin = f'{filename_prefix}message/{original.chat_id}/{original.id}'
        else:
            origin = f'{filename_prefix}message/{ctx.msg.chat_id}/{ctx.msg.id}'

        hook = Hook(
            name=name,
            type=HookType.onstart,
            once=False,
            save_locals=True,
            code=code,
            origin=origin,
            datetime=dt.datetime.now(),
        )
        hook.save()
        return dedent(f'''
            Added hook {name!r}.
            The hook will be executed every time TGPy starts.
        ''')

    def remove(self, name) -> str:
        try:
            delete_hook_file(name)
        except FileNotFoundError:
            return f'No hook named {name!r}.'
        return f'Removed hook {name!r}.'

    def __str__(self):
        lst = '\n'.join(f'{idx + 1}. {hook.name}' for idx, hook in enumerate(get_sorted_hooks()))
        if not lst:
            return dedent('''
                You have no hooks.
                Learn about hooks at https://tgpy.tmat.me/hooks.
            ''')
        return dedent('''
            Your hooks:
            {}
            
            Change hooks with `hooks.add(name)` and `hooks.remove(name)`.
            Learn more at https://tgpy.tmat.me/hooks.
        ''').format(lst)

    def __iter__(self):
        return (hook.name for hook in get_sorted_hooks())


variables['hooks'] = hooks = HooksObject()
