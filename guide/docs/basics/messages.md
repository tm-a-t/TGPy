# Messages

## Telegram objects

TGPy is based on **Telethon**, Telegram API client library. You can
use [Telethon objects and methods](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html)
for messages, users and chats. This page explains basic actions with messages, such as sending and editing.

??? tldr "Already familiar with Telethon?"

    Already familiar with Telethon?

    All you need to know is that in TGPy you can use the following objects:

    - `client` for the Telethon client
    - `msg` for the current message
    - `orig` for the message you’re replying to

    See the [Builtin reference](/reference/builtins/#telethon-objects) for details.

    Now you can skip the rest of the page and go to the [examples](/basics/examples) :)

TGPy provides some builtin Telegram objects. The `client` object is useful for general functions such as sending
messages, listing chats and so on. The `msg` object always refers to the current message.

## Sending a message

The simplest Telegram action is sending a message. There is a method for that:

```python
await client.send_message(chat, text)
```

As the `chat` you can use either a chat name, a username or an ID.

Therefore, to send a «Hello World» to the current chat you may use:

```python
await client.send_message(msg.chat_id, "Hello World")
```

Or there is a shortcut for that:

```python
await msg.respond("Hello World")
```

You can also use `msg.reply` instead of `msg.respond` to send the message as a reply.

!!! Note
    Remember you can omit the `await` keyword in simple scripts.

The new message object can be used later:

```python
hello = await msg.respond("Hello")
# `hello` is now the new message object.
# Let's edit that message!
await hello.edit("Hiiiiiiiiii")
```

## Message attributes

You can use message properties such as `message.text`, `message.chat`, `message.user` and others.

There are also message methods for common actions, such as `message.edit()`, `message.delete()`, `message.forward_to()`, `message.pin()`.

Have fun :)

[Telethon reference for Message attributes](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html#message)

[Telethon reference for client attributes](https://docs.telethon.dev/en/stable/quick-references/client-reference.html)

??? example "Example: show full message data"

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
