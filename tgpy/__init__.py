import logging

from telethon import TelegramClient

from tgpy.context import Context
from tgpy.version import __version__

logging.basicConfig(
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)
logging.getLogger('telethon').setLevel(logging.WARNING)


class App:
    client: TelegramClient
    ctx: Context

    def __init__(self):
        self.ctx = Context()


app = App()

__all__ = ['App', 'app']
