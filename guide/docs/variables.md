# Default variables

You can use some predefined variables.

## Telethon objects


- `msg` - current [message](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message)
- `orig` - original message, if your message is a reply
- `client` - Telethon [client](https://docs.telethon.dev/en/latest/quick-references/client-reference.html)

TGPy gets `orig` message only if your code uses `orig` variable. This is so because getting `orig` message requires an additional request to Telegram API.

```python
msg.text

TGPy> msg.text
```


## `_` variable

This is for the previous result.

```python
2 + 2

TGPy> 4
```

```python
_ * 100

TGPy> 400
```

## `ctx` variable

`ctx` variable is used for current context.

- `ctx.msg` - latest message

`ctx.orig` - message which ctx.msg was reply to. Not implemented yet. 
Instead, use `await ctx.msg.get_reply_message()`.

So `msg` is the message where it was used and `ctx.msg` is the message from where was this code was executed. 
It is useful for defining functions.

Example of usage:
```python
async def delete():
    ctx_orig = await ctx.msg.get_reply_message()
    await ctx_orig.delete()
    await ctx.msg.delete()

TGPy> None
```
Use this function to delete the message you reply to.