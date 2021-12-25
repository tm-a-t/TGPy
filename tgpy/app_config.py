from typing import Optional

import yaml
from pydantic import BaseModel, ValidationError

from tgpy.utils import CONFIG_FILENAME


class Config(BaseModel):
    api_id: Optional[int]
    api_hash: Optional[str]

    @classmethod
    def load(cls):
        try:
            with open(CONFIG_FILENAME) as file:
                config_dict = yaml.safe_load(file)
        except FileNotFoundError:
            config_dict = {}
        try:
            config = cls(**config_dict)
        except ValidationError:
            config = cls()
        return config

    def save(self):
        with open(CONFIG_FILENAME, 'w') as file:
            yaml.safe_dump(self.dict(), file)
