import os
from pathlib import Path

import appdirs

if env_tgpy_data := os.getenv('TGPY_DATA'):
    DATA_DIR = Path(env_tgpy_data).absolute()
else:
    # noinspection PyTypeChecker
    DATA_DIR = Path(appdirs.user_config_dir('tgpy', appauthor=False))
STD_MODULES_DIR = Path(__file__).parent.parent / 'std'
MODULES_DIR = DATA_DIR / 'modules'
WORKDIR = DATA_DIR / 'workdir'

__all__ = [
    'DATA_DIR',
    'STD_MODULES_DIR',
    'MODULES_DIR',
    'WORKDIR',
]
