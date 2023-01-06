import os
import sys
from datetime import datetime
from textwrap import dedent
from typing import Optional

from telethon.tl.custom import Message

from tgpy import app
from tgpy.message_design import parse_message
from tgpy.modules import (
    Module,
    delete_module_file,
    get_module_names,
    get_sorted_modules,
)
from tgpy.utils import (
    REPO_ROOT,
    RunCmdException,
    execute_in_repo_root,
    filename_prefix,
    get_hostname,
    get_installed_version,
    get_running_version,
    get_user,
    installed_as_package,
    run_cmd,
    running_in_docker,
)


def ping():
    return dedent(
        f'''
        Pong!
        Running on {get_user()}@{get_hostname()}
        Version: {get_running_version()}
        '''
    )


def restart(msg: Optional[str] = 'Restarted successfully'):
    mod_code = dedent(
        f'''
        from tgpy.message_design import edit_message, parse_message
        msg = await client.get_messages({app.ctx.msg.chat_id}, ids={app.ctx.msg.id})
        await edit_message(msg, parse_message(msg).code, '{msg}')
        '''
    )
    module = Module(
        name='__restart_message',
        once=True,
        save_locals=False,
        code=mod_code,
        origin=f'{filename_prefix}restart_message',
        priority=0,
    )
    module.save()
    os.execl(sys.executable, sys.executable, '-m', 'tgpy', *sys.argv[1:])


def update():
    old_version = get_running_version()

    if running_in_docker():
        return 'Can\'t update a docker container'

    if installed_as_package():
        update_args = [sys.executable, '-m', 'pip', 'install', '-U', 'tgpy']
        try:
            run_cmd(update_args)
        except RunCmdException:
            run_cmd(update_args + ['--user'])
    elif REPO_ROOT:
        with execute_in_repo_root():
            try:
                run_cmd(['git', 'pull'])
            except FileNotFoundError:
                return 'Git is not installed'
    else:
        return 'Could not find suitable update method'

    new_version = get_installed_version()
    if not new_version:
        return 'Could not determine upgraded version. This is probably a bug in TGPy.'
    if old_version == new_version:
        return 'Already up to date'
    else:
        restart(f'Updated successfully! Current version: {new_version}')


class ModulesObject:
    async def add(self, name: str, code: Optional[str] = None) -> str:
        name = str(name)

        if code is None:
            original: Message = await app.ctx.msg.get_reply_message()
            if original is None:
                return 'Use this function in reply to a message'
            message_data = parse_message(original)
            if not message_data.is_tgpy_message:
                return 'No code found in reply message'
            code = message_data.code

        origin = f'{filename_prefix}module/{name}'

        if name in self:
            module = self[name]
            module.code = code
        else:
            module = Module(
                name=name,
                once=False,
                save_locals=True,
                code=code,
                origin=origin,
                priority=datetime.now().timestamp(),
            )
        module.save()

        return dedent(
            f'''
            Added module {name!r}.
            Module's code will be executed every time TGPy starts.
            '''
        )

    def remove(self, name) -> str:
        try:
            delete_module_file(name)
        except FileNotFoundError:
            return f'No module named {name!r}.'
        return f'Removed module {name!r}.'

    def __str__(self):
        lst = '\n'.join(
            f'{idx + 1}. {mod.name}' for idx, mod in enumerate(get_sorted_modules())
        )
        if not lst:
            return dedent(
                '''
                You have no modules.
                Learn about modules at https://tgpy.tmat.me/modules.
                '''
            )
        return dedent(
            '''
            Your modules:
            {}
            
            Change modules with `modules.add(name)` and `modules.remove(name)`.
            Learn more at https://tgpy.tmat.me/modules.
            '''
        ).format(lst)

    def __iter__(self):
        return (mod.name for mod in get_sorted_modules())

    def __getitem__(self, mod_name):
        return Module.load(mod_name)

    def __contains__(self, mod_name):
        return mod_name in get_module_names()


def add_builtin_functions():
    variables = app.api.variables
    variables['ping'] = ping
    variables['restart'] = restart
    variables['update'] = update
    variables['modules'] = ModulesObject()
    constants = app.api.constants
    constants['tgpy'] = app.api
    constants['ctx'] = app.ctx
    constants['client'] = app.client
