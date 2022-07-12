# Context data

[`msg`](../reference/builtins.md#telethon-objects) object always relates to the message where it was used. However,
sometimes you need to define reusable functions that use the current message.

Let’s say we want to define `cat()` function which sends a random cat picture to the chat it was used at. Somehow the
function must use the current chat. We could pass `msg` as an argument, but it wouldn’t be handy enough to reuse the
function. Instead, we will use `ctx.msg` variable.

`ctx.msg` always contains your latest TGPy message. With it, we can define `cat()` function as following:

```python
async def cat():
    cat_url = 'https://cataas.com/cat'  # URL for a random cat image
    await ctx.msg.respond(file=cat_url)


TGPy> None
```

## Getting original message

TODO
