import importlib.metadata
import shlex
from enum import Enum
from pathlib import Path
from subprocess import Popen, PIPE

import appdirs
import yaml
from pydantic import ValidationError
from yaml.representer import SafeRepresenter

DATA_DIR = Path(appdirs.user_config_dir('tgpy'))
HOOKS_DIR = DATA_DIR / 'hooks'
WORKDIR = DATA_DIR / 'workdir'
CONFIG_FILENAME = DATA_DIR / 'config.yml'
SESSION_FILENAME = DATA_DIR / 'TGPy.session'


def create_config_dirs():
    DATA_DIR.mkdir(exist_ok=True)
    HOOKS_DIR.mkdir(exist_ok=True)
    WORKDIR.mkdir(exist_ok=True)


def _multiline_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')


def _enum_presenter(dumper, data):
    value = data.value
    if isinstance(value, str):
        return dumper.represent_str(value)
    if isinstance(value, int):
        return dumper.represent_int(value)
    if isinstance(value, bool):
        return dumper.represent_bool(value)
    raise ValueError


class yaml_multiline_str(str):
    pass


SafeRepresenter.add_representer(yaml_multiline_str, _multiline_presenter)
SafeRepresenter.add_multi_representer(Enum, _enum_presenter)


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


__all__ = ['DATA_DIR', 'HOOKS_DIR', 'WORKDIR', 'CONFIG_FILENAME', 'SESSION_FILENAME',
           'yaml_multiline_str', 'run_cmd', 'get_version', 'create_config_dirs',
           'installed_as_package']
