from typing import Optional

import yaml
from pydantic import BaseModel, ValidationError

from app.console import console
from app.utils import CONFIG_FILENAME


class Config(BaseModel):
    api_id: Optional[int]
    api_hash: Optional[str]
    phone: Optional[str]


def load_config():
    try:
        with open(CONFIG_FILENAME) as file:
            config_dict = yaml.safe_load(file)
    except FileNotFoundError:
        config_dict = {}

    try:
        config = Config(**config_dict)
    except ValidationError:
        config = Config()

    if not (config.api_id and config.api_hash and config.phone):
        console.print('[bold on bright_cyan] Welcome to TGPy ')
        console.print('Starting setup...')
        console.print()
        console.print('[bold on white] Step 1 of 2 ')
        console.print(
            '│ TGPy uses Telegram API, so you\'ll need to register your Telegram app.\n'
            '│  [cyan]1.[/] Go to https://my.telegram.org\n'
            '│  [cyan]2.[/] Login with your Telegram account\n'
            '│  [cyan]3.[/] Go to "API development tools"\n'
            '│  [cyan]4.[/] Create your app. Choose any app title and short_title. You can leave other fields empty.\n'
            '│ You will get api_id and api_hash.'
        )
        config.api_id = console.input('│ Please enter api_id: ')
        config.api_hash = console.input('│ ...and api_hash: ')
        console.print()
        console.print('[bold on white] Step 2 of 2 ')
        console.print('│ Now login to Telegram.')
        config.phone = console.input('│ Please enter your phone: ')
        console.print()

        with open(CONFIG_FILENAME, 'w') as file:
            yaml.safe_dump(config.dict(), file)

    return config
