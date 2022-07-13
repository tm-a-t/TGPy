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

## Send the source of all your modules

```python
for name in modules:
    code = modules[name].code
    await ctx.msg.respond(f'<pre># Module "{name}":\n\n{code}</pre>')
```
