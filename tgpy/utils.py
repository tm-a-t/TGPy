import importlib.metadata
import shlex
from pathlib import Path
from subprocess import PIPE, Popen

import appdirs

# noinspection PyTypeChecker
DATA_DIR = Path(appdirs.user_config_dir('tgpy', appauthor=False))
MODULES_DIR = DATA_DIR / 'modules'
WORKDIR = DATA_DIR / 'workdir'
CONFIG_FILENAME = DATA_DIR / 'config.yml'
SESSION_FILENAME = DATA_DIR / 'TGPy.session'

filename_prefix = 'tgpy://'


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


def installed_as_package():
    try:
        importlib.metadata.version('tgpy')
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def get_version():
    if installed_as_package():
        return importlib.metadata.version('tgpy')

    try:
        return 'git@' + run_cmd(['git', 'rev-parse', '--short', 'HEAD'])
    except RunCmdException:
        pass

    return 'unknown'


__all__ = [
    'DATA_DIR',
    'MODULES_DIR',
    'WORKDIR',
    'CONFIG_FILENAME',
    'SESSION_FILENAME',
    'run_cmd',
    'get_version',
    'create_config_dirs',
    'installed_as_package',
    'RunCmdException',
    'filename_prefix',
]
