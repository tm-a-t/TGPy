# Default variables

In TGPy you can use some predefined variables.

## Telethon objects


- `msg` - current [message](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message)
- `orig` - original message, if your message is a reply
- `client` - Telethon [client](https://docs.telethon.dev/en/latest/quick-references/client-reference.html)

??? example "Example: show current message data"

    ```python
    return msg
    
    TGPy> Message(
     id=77305,
     peer_id=PeerChannel(
      channel_id=1544471292
     ),
     date=datetime.datetime(2021, 10, 31, 11, 20, 28, tzinfo=datetime.timezone.utc),
     message='return msg',
     out=True,
     mentioned=False,
     media_unread=False,
     silent=False,
     post=False,
     from_scheduled=False,
     legacy=False,
     edit_hide=False,
     pinned=False,
     from_id=PeerUser(
      user_id=254210206
     ),
     fwd_from=None,
     via_bot_id=None,
     reply_to=None,
     media=None,
     reply_markup=None,
     entities=[
     ],
     views=None,
     forwards=None,
     replies=MessageReplies(
      replies=0,
      replies_pts=87625,
      comments=False,
      recent_repliers=[
      ],
      channel_id=None,
      max_id=None,
      read_max_id=None
     ),
     edit_date=None,
     post_author=None,
     grouped_id=None,
     restriction_reason=[
     ],
     ttl_period=None
    )
    ```

TGPy gets `orig` message only if your code uses `orig` variable (because it requires an additional request to Telegram API).

## Previous result

The `_` variable stands for the previous result.

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