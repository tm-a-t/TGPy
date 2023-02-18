import getpass
import importlib.metadata
import inspect
import os
import re
import socket

from telethon.tl.custom import Message

import tgpy
from tgpy.utils import REPO_ROOT, RunCmdException, execute_in_repo_root, run_cmd


def get_installed_version():
    if version := _get_git_version():
        return version

    if installed_as_package():
        return importlib.metadata.version('tgpy')

    return None


def get_running_version():
    if not tgpy.version.IS_DEV_BUILD:
        return tgpy.version.__version__

    if _COMMIT_HASH:
        return _COMMIT_HASH

    if tgpy.version.COMMIT_HASH:
        return 'git@' + tgpy.version.COMMIT_HASH[:7]

    return 'unknown'


def installed_as_package():
    try:
        importlib.metadata.version('tgpy')
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def get_user():
    try:
        return getpass.getuser()
    except KeyError:
        return str(os.getuid())


DOCKER_DEFAULT_HOSTNAME_RGX = re.compile(r'[0-9a-f]{12}')


def get_hostname():
    real_hostname = socket.gethostname()
    if running_in_docker() and DOCKER_DEFAULT_HOSTNAME_RGX.fullmatch(real_hostname):
        return 'docker'
    return real_hostname


def running_in_docker():
    return os.path.exists('/.dockerenv') or os.path.exists('/run/.containerenv')


def _get_git_version() -> str | None:
    if not REPO_ROOT:
        return None
    with execute_in_repo_root():
        try:
            return 'git@' + run_cmd(['git', 'rev-parse', '--short', 'HEAD'])
        except (RunCmdException, FileNotFoundError):
            pass

    return None


async def try_await(func, *args, **kwargs):
    res = func(*args, **kwargs)
    if inspect.isawaitable(res):
        res = await res
    return res


def outgoing_messages_filter(m: Message):
    return m.out and not m.forward and not m.via_bot


_COMMIT_HASH = _get_git_version()

__all__ = [
    'get_installed_version',
    'get_running_version',
    'installed_as_package',
    'get_user',
    'get_hostname',
    'running_in_docker',
    'try_await',
    'outgoing_messages_filter',
]
