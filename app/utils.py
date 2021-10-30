import os
import shlex
from enum import Enum
from subprocess import Popen

from yaml.representer import SafeRepresenter


def get_base_dir():
    return os.path.dirname(os.path.dirname(__file__))


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


def run_cmd(args: list[str]):
    p = Popen(args)
    p.wait()
    if p.returncode:
        raise Exception(f'Command {shlex.join(args)} exited with code {p.returncode}')


__all__ = ['get_base_dir', 'yaml_multiline_str', 'run_cmd']
