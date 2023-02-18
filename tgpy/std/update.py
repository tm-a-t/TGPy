"""
    name: update
    origin: tgpy://builtin_module/update
    priority: 700
"""

import sys

from tgpy.api.utils import (
    get_installed_version,
    get_running_version,
    installed_as_package,
    running_in_docker,
)
from tgpy.utils import REPO_ROOT, RunCmdException, execute_in_repo_root, run_cmd


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


__all__ = ['update']
