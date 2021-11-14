import os
from typing import Optional

import yaml

from app.console import console
from app.utils import get_base_dir

from pydantic import BaseModel


class Config(BaseModel):
    api_id: Optional[int]
    api_hash: Optional[str]
    phone: Optional[str]


def load_config():
    config_filename = os.path.join(get_base_dir(), 'config.yaml')
    try:
        with open(config_filename) as file:
            config_dict = yaml.safe_load(file)
    except FileNotFoundError:
        config_dict = {}

    config = Config(**config_dict)

    if not (config.api_id and config.api_hash and config.phone):
        config.api_id = console.input('api_id: ')
        config.api_hash = console.input('api_hash: ')
        config.phone = console.input('phone: ')

        with open(config_filename, 'w') as file:
            yaml.safe_dump(config.dict(), file)

    return config
