import logging

from rich.logging import RichHandler
from telethon import TelegramClient

from tgpy.app_config import Config
from tgpy.console import console


__version__ = "0.2.0"

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt="[%X]", handlers=[RichHandler()])


class App:
    config: Config = None
    client: TelegramClient = None


app = App()
