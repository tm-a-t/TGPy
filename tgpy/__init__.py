import logging

from rich.logging import RichHandler
from telethon import TelegramClient

from tgpy.api import API
from tgpy.app_config import Config
from tgpy.console import console
from tgpy.context import Context
from tgpy.version import __version__

logging.basicConfig(
    level=logging.INFO, format='%(message)s', datefmt="[%X]", handlers=[RichHandler()]
)
logging.getLogger('telethon').setLevel(logging.WARNING)


class App:
    config: Config = None
    client: TelegramClient = None
    api: API = None
    ctx: Context

    def __init__(self):
        self.ctx = Context()
        self.api = API()


app = App()
