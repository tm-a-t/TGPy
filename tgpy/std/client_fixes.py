"""
name: client_fixes
origin: tgpy://builtin_module/client_fixes
priority: 800
"""

import re

import tgpy.api

DOUBLE_QUOTE_RE = re.compile(r'[“”]')
SINGLE_QUOTE_RE = re.compile(r'[‘’]')

tgpy.api.code_transformers.add(
    'apple_fix', lambda x: DOUBLE_QUOTE_RE.sub('"', SINGLE_QUOTE_RE.sub("'", x))
)
tgpy.api.code_transformers.add('android_fix', lambda x: x.replace('\u00a0', ' '))
