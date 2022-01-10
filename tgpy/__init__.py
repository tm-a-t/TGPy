import logging

from rich.logging import RichHandler
from telethon import TelegramClient

from tgpy.api import API
from tgpy.app_config import Config
from tgpy.console import console
from tgpy.context import Context

__version__ = "0.4.1"

logging.basicConfig(
    level=logging.INFO, format='%(message)s', datefmt="[%X]", handlers=[RichHandler()]
)


class App:
    config: Config = None
    client: TelegramClient = None
    api: API = None
    ctx: Context

    def __init__(self):
        self.ctx = Context()
        self.api = API()


app = App()
