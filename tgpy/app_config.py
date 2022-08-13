import dataclasses
from dataclasses import dataclass
from typing import Optional

import yaml

from tgpy.utils import CONFIG_FILENAME


@dataclass
class Config:
    api_id: Optional[int] = None
    api_hash: Optional[str] = None

    @classmethod
    def load(cls):
        try:
            with open(CONFIG_FILENAME) as file:
                config_dict = yaml.safe_load(file)
        except FileNotFoundError:
            config_dict = {}
        return cls(**config_dict)

    def save(self):
        with open(CONFIG_FILENAME, 'w') as file:
            yaml.safe_dump(dataclasses.asdict(self), file)
