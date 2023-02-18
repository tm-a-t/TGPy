import os
import random
import shlex
import string
from contextlib import contextmanager
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any, NewType, Union

from tgpy.api.directories import DATA_DIR, MODULES_DIR, WORKDIR

JSON = NewType('JSON', Union[None, str, int, bool, list['JSON'], dict[str, 'JSON']])
UNDEFINED = object()

CONFIG_FILENAME = DATA_DIR / 'config.yml'
SESSION_FILENAME = DATA_DIR / 'TGPy.session'
REPO_ROOT = Path(__file__).parent.parent
if not os.path.exists(REPO_ROOT / '.git'):
    REPO_ROOT = None

FILENAME_PREFIX = 'tgpy://'


@contextmanager
def execute_in_repo_root():
    if not REPO_ROOT:
        raise ValueError('No repository found')
    old_cwd = os.getcwd()
    os.chdir(REPO_ROOT)
    try:
        yield
    finally:
        os.chdir(old_cwd)


def create_config_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    MODULES_DIR.mkdir(exist_ok=True)
    WORKDIR.mkdir(exist_ok=True)


class RunCmdException(Exception):
    def __init__(self, process: Popen):
        self.process = process

    def __str__(self):
        return f'Command {shlex.join(self.process.args)} exited with code {self.process.returncode}'


def run_cmd(args: list[str]):
    proc = Popen(args, stdout=PIPE)
    output, _ = proc.communicate()
    if proc.returncode:
        raise RunCmdException(proc)
    return output.decode('utf-8').strip()


def dot_get(
    obj: dict, key: str, default: Any | None = UNDEFINED, *, create: bool = False
) -> Any:
    if not key:
        return obj
    curr_obj = obj
    parts = key.split('.')
    for i, part in enumerate(parts):
        new_obj = curr_obj.get(part, UNDEFINED)
        if new_obj is UNDEFINED:
            if create and (default is UNDEFINED or i != len(parts) - 1):
                new_obj = curr_obj[part] = {}
            elif default is UNDEFINED:
                raise KeyError(key)
            else:
                if create:
                    curr_obj[part] = default
                return default
        if not isinstance(new_obj, dict) and i != len(parts) - 1:
            raise ValueError('.'.join(parts[: i + 1]) + ' is not a dict')
        curr_obj = new_obj
    return curr_obj


def numid():
    return ''.join(random.choices(string.digits, k=8))


__all__ = [
    'JSON',
    'UNDEFINED',
    'CONFIG_FILENAME',
    'SESSION_FILENAME',
    'REPO_ROOT',
    'FILENAME_PREFIX',
    'run_cmd',
    'create_config_dirs',
    'RunCmdException',
    'execute_in_repo_root',
    'dot_get',
    'numid',
]
