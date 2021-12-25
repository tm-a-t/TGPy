import importlib.metadata
import shlex
from enum import Enum
from pathlib import Path
from subprocess import Popen, PIPE

import yaml
from pydantic import ValidationError
from yaml.representer import SafeRepresenter

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)
HOOKS_DIR = DATA_DIR / 'hooks'
HOOKS_DIR.mkdir(exist_ok=True)
WORKDIR = DATA_DIR / 'workdir'
WORKDIR.mkdir(exist_ok=True)
CONFIG_FILENAME = DATA_DIR / 'config.yml'
SESSION_FILENAME = DATA_DIR / 'TGPy.session'


def migrate_from_old_versions():
    from tgpy.app_config import Config

    old_session_file = BASE_DIR / 'TGPy.session'
    if old_session_file.exists() and not SESSION_FILENAME.exists():
        old_session_file.rename(SESSION_FILENAME)
    old_config_file = BASE_DIR / 'config.py'
    if old_config_file.exists() and not CONFIG_FILENAME.exists():
        try:
            config_mod = importlib.import_module('config')
            config = Config(api_id=config_mod.api_id, api_hash=config_mod.api_hash)
            with open(CONFIG_FILENAME, 'w') as file:
                yaml.safe_dump(config.dict(), file)
        except (ValidationError, AttributeError, ImportError):
            pass
        old_config_file.unlink()


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


__all__ = ['BASE_DIR', 'DATA_DIR', 'HOOKS_DIR', 'WORKDIR', 'CONFIG_FILENAME', 'SESSION_FILENAME',
           'yaml_multiline_str', 'run_cmd', 'get_version', 'migrate_from_old_versions']
