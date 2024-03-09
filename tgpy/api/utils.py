import getpass
import importlib.metadata
import inspect
import os
import re
import socket
import tokenize
from io import BytesIO

from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import MessageService

import tgpy
from tgpy.utils import REPO_ROOT, RunCmdException, execute_in_repo_root, run_cmd


def get_installed_version():
    if version := _get_git_version():
        return version

    if installed_as_package():
        return importlib.metadata.version('tgpy')

    return None


def _get_git_version() -> str | None:
    if not REPO_ROOT:
        return None
    with execute_in_repo_root():
        try:
            return 'git@' + run_cmd(['git', 'rev-parse', '--short', 'HEAD'])
        except (RunCmdException, FileNotFoundError):
            pass

    return None


_COMMIT_HASH = _get_git_version()


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


async def try_await(func, *args, **kwargs):
    res = func(*args, **kwargs)
    if inspect.isawaitable(res):
        res = await res
    return res


def outgoing_messages_filter(e: events.NewMessage.Event | events.MessageEdited.Event):
    m: Message = e.message
    return (
        m.out and not m.forward and not m.via_bot and not isinstance(m, MessageService)
    )


def tokenize_string(s: str) -> list[tokenize.TokenInfo] | None:
    try:
        return list(tokenize.tokenize(BytesIO(s.encode('utf-8')).readline))
    except (IndentationError, tokenize.TokenError):
        return None


def untokenize_to_string(tokens: list[tokenize.TokenInfo]) -> str:
    return tokenize.untokenize(tokens).decode('utf-8')


__all__ = [
    'get_installed_version',
    'get_running_version',
    'installed_as_package',
    'get_user',
    'get_hostname',
    'running_in_docker',
    'try_await',
    'outgoing_messages_filter',
    'tokenize_string',
    'untokenize_to_string',
]
