---
description: Tips on fixing syntax highlighting and code autocompletion when using code editors for TGPy scripts.
---

# Writing TGPy programs in code editors

Editing complex code without syntax highlighting or code autocompletion is inconvenient. If you write a large code
snippet for TGPy, you will want to use a code editor instead of the message input field.

Of course, you can write code in an editor and then paste it to Telegram. However, editors will highlight TGPy-specific
builtins
as undefined and unknown-typed.

You can deal with this by annotating types of builtin variables.

Common TGPy builtins include `client`, `msg`, `orig`, and `ctx`. So, code with annotations will look like this:

```python
from telethon import TelegramClient
from telethon.tl.custom import Message
from tgpy.context import Context

client: TelegramClient
msg: Message
orig: Message
ctx: Context

# Custom code here
```

Write your code, copy it and paste to Telegram: this should work.

Unfortunately, editors won’t understand syntax tricks such
as [`.await` property-like notation,](../basics/asyncio#asyncio-in-tgpy) so you should use normal Python syntax.

By the way, normal Python syntax also forbids top-level await. To avoid syntax errors, you can wrap your code in an
async function. Or give up on hacks and have half of your code underlined as errors.

Why not.
