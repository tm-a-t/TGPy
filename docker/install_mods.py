import logging
from subprocess import Popen

from tgpy.api.config import config

logging.basicConfig(
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)
logger = logging.getLogger('install_mods')


def main():
    config.load()
    command_groups: dict = config.get('docker.setup_commands', {})
    command_groups['_core'] = 'apt-get update'
    for name, commands in sorted(command_groups.items()):
        if isinstance(commands, str):
            commands = [commands]
        logger.info(f"Running setup command group '{name}'")
        for command in commands:
            logger.info(f"Running setup command '{command}'")
            p = Popen(command, shell=True)
            p.wait()
            if p.returncode != 0:
                logger.info("Running setup command failed")


if __name__ == '__main__':
    main()
