"""
    name: ping
    origin: tgpy://builtin_module/ping
    priority: 600
"""

from textwrap import dedent

from tgpy.api import get_hostname, get_running_version, get_user


def ping():
    return dedent(
        f'''
        Pong!
        Running on {get_user()}@{get_hostname()}
        Version: {get_running_version()}
        '''
    )


__all__ = ['ping']
