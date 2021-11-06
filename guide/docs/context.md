# Context

[`msg`](builtins.md#telethon-objects) and [`orig`](builtins.md#telethon-objects) objects are always related 
to the message where they were used. Although, sometimes you need to define functions that use current message and reuse
them later. For example, you might want to delete the messages you reply to with `delete()` function.

Instead of passing `msg` and `orig` as arguments, you can use `ctx` variable.

`ctx` contains current context objects:

- `ctx.msg` - the latest TGPy message

- `ctx.orig` - the message which the latest TGPy message was reply to

    !!! caution "Not implemented yet"
   
        `ctx.orig` is not implemented yet. Instead, use: 
        ```python
        await ctx.msg.get_reply_message()
        ```


Thus, you can define `delete()` function as following:

```python
async def delete():
    original_message = await ctx.msg.get_reply_message()
    await original_message.delete()
    await ctx.msg.delete()

TGPy> None
```

Now you can send `delete()` in reply to some message. The original message and your '`delete()`' message will be deleted.
