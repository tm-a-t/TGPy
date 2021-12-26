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


def migrate_config():
    from tgpy.app_config import Config
    old_base_dir = Path(__file__).parent.parent

    old_data_dir = old_base_dir / 'data'
    old_session_file = old_base_dir / 'TGPy.session'
    new_session_file = old_data_dir / SESSION_FILENAME.name
    if not old_session_file.exists() or DATA_DIR.exists():
        # old config file doesn't exist or new config file already exists
        return
    # ensure old_data_dir exists (it should, because old_session_file does)
    old_data_dir.mkdir(exist_ok=True)
    # migrate old session file
    old_session_file.rename(new_session_file)

    # migrate old config file
    old_config_file = old_base_dir / 'config.py'
    new_config_file = old_data_dir / CONFIG_FILENAME.name
    if old_config_file.exists():
        try:
            config_mod = importlib.import_module('config')
            config = Config(api_id=config_mod.api_id, api_hash=config_mod.api_hash)
            with open(new_config_file, 'w') as file:
                yaml.safe_dump(config.dict(), file)
        except (ValidationError, AttributeError, ImportError):
            pass
        old_config_file.unlink()

    # finally, move data dir to new location
    old_data_dir.rename(DATA_DIR)


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
           'yaml_multiline_str', 'run_cmd', 'get_version', 'migrate_config', 'create_config_dirs',
           'installed_as_package']
