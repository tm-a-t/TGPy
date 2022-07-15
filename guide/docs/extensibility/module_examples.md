# Module examples

## Shortcut for deleting messages

Send `d()` in reply to any message to delete it.

```python
async def d():
    original = await ctx.msg.get_reply_message()
    await msg.delete()
    await original.delete()
```

## Shortcut for saving messages

Send `save()` in reply to any message to forward to Saved Messages.

```python
async def save():
    original = await ctx.msg.get_reply_message()
    await msg.delete()
    await original.forward_to('me')
```

## Stats for chat member IDs

Sort chat members by their IDs. In average, the lower ID user has, the earlier they registered in Telegram.

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
