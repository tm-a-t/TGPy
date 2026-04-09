---
description: 'Examples of using Context object and TGPy modules: saving shortcuts for message operations, getting chat stats, sharing modules, and more.'
---

# Module examples

These are examples of using [`ctx`](context) and [modules](modules).
It may be handy to save the functions here as modules to reuse in the future.

::: tip
Join the Russian-speaking chat [@tgpy_flood](https://t.me/tgpy_flood) to see the modules that users share.
:::

## Shortcut for deleting messages

Send `d()` in reply to any message to delete it.

```python
async def d():
    original = await ctx.msg.get_reply_message()
    await ctx.msg.delete()
    await original.delete()
```

## Shortcut for saving messages

Send `save()` in reply to any message to forward to Saved Messages.

```python
async def save():
    original = await ctx.msg.get_reply_message()
    await ctx.msg.delete()
    await original.forward_to('me')
```

## Stats for chat member IDs

Sort chat members by their IDs. In average, the lower the ID of a user is, the earlier they registered in Telegram.

```python
def fullname(user):
    return ((user.first_name or '') + ' ' + (user.last_name or '')).strip() or 'Deleted account'

def idstat(users):
    users.sort(key=lambda x: x.id)
    return '\n'.join([f'{x.id:>10} {fullname(x)}' for x in users])

async def idstatgrp():
    return idstat(await client.get_participants(ctx.msg.chat))
```

## Send the source of all your modules

```python
from html import escape

for name in modules:
    code = escape(modules[name].code)
    await ctx.msg.respond(f'<pre>Module "{name}":\n\n{code}</pre>')
```

## Process a message with sed

Use in reply to a message.

```python
import subprocess

async def sed(s):
    orig = await ctx.msg.get_reply_message()
    text = subprocess.run(["sed", s], input=orig.text, capture_output=True, check=True, encoding="utf-8").stdout
    if text == orig.text:
        return "(no changes)"
    if orig.from_id == ctx.msg.from_id:
        await orig.edit(text)
        await ctx.msg.delete()
    else:
        return text
```
