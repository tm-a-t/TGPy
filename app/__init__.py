import logging

from rich.logging import RichHandler
from telethon import TelegramClient

from app.app_config import Config
from app.console import console

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt="[%X]", handlers=[RichHandler()])


class App:
    config: Config = None
    client: TelegramClient = None


app = App()
