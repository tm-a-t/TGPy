# Context data

The [`msg`](../reference/builtins.md#telethon-objects) object always refers to the message where it was used. For
instance, if you use `msg` in a function, it will refer to the message that defined this function, even if it is
called from another message later. However, sometimes you need to define reusable functions that use the current
message.

Let’s say we want to define a `cat()` function which sends a cat picture to the chat it was used at. Somehow the
function must use the current chat. We could pass `msg` as an argument, but it wouldn’t be handy enough to reuse the
function. Instead, we will use `ctx.msg` variable.

`ctx.msg` always contains your latest TGPy message. With it, we can define `cat()` function as follows:

```python
async def cat():
    cat_url = 'https://cataas.com/cat'  # URL for a cat image
    await ctx.msg.respond(file=cat_url)
```

## Getting the original message

To get the message which `ctx.msg` replies to, use:

```python
original = await ctx.msg.get_reply_message()
```

!!! info
    
    The shortcut `ctx.orig` is planned but not implemented yet.
