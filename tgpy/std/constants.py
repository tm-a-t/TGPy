"""
    name: constants
    origin: tgpy://builtin_module/constants
    priority: 100
"""

import tgpy.api
from tgpy import app

tgpy.api.constants['ctx'] = app.ctx
tgpy.api.constants['client'] = app.client

__all__ = []
