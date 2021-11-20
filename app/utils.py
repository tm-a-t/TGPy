import importlib.metadata
import shlex
from enum import Enum
from pathlib import Path
from subprocess import Popen, PIPE

from yaml.representer import SafeRepresenter

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)
HOOKS_DIR = DATA_DIR / 'hooks'
HOOKS_DIR.mkdir(exist_ok=True)
WORKDIR = DATA_DIR / 'workdir'
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


def get_version():
    try:
        return importlib.metadata.version('tgpy')
    except importlib.metadata.PackageNotFoundError:
        pass
    try:
        return 'git@' + run_cmd(['git', 'rev-parse', '--short', 'HEAD'])
    except RunCmdException:
        pass
    return 'unknown'


__all__ = ['BASE_DIR', 'DATA_DIR', 'HOOKS_DIR', 'WORKDIR', 'yaml_multiline_str', 'run_cmd', 'get_version']
