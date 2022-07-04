# Context data

[`msg`](../builtins.md#telethon-objects) object always relates
to the message where it was used. However, sometimes you need to define reusable functions that use 
the current message. Let’s say you want to define `cat()` function which sends a random cat picture to the same chat.

The function must use the current chat. Instead of passing arguments, you can use `ctx.msg` variable.

`ctx.msg` always contains your latest TGPy message. With it you can define `cat()` function as following:

```python
cat_url = 'https://cataas.com/cat'  # URL for a random cat image

async def cat():
    await ctx.msg.respond(file=cat_url)

TGPy> None
```

## Getting original message

TODO
