---
description: You can send and edit messages from your TGPy code through Telethon methods. Learn Telethon basics to control Telegram messages, users and chats.
---

# Messages

## Telegram objects

TGPy is based on **Telethon**, a Telegram API client library. You can
use [Telethon objects and methods](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html)
for messages, users and chats. This page explains how to perform basic message actions, such as sending and editing.

::: details Already familiar with Telethon?

All you need to know is that in TGPy you can use the following objects:

- `client` for the Telethon client
- `msg` for the current message
- `orig` for the message you’re replying to

See the [Builtin reference](../reference/builtins#telethon-objects) for details.

Now you can skip the rest of the page and go to the [examples](examples) :)

:::

In TGPy messages, you can always use some Telegram objects. The `client` object is helpful for general functionality,
such as sending messages, listing chats and so on. The `msg` object always refers to the current message.

## Sending a message

The simplest Telegram action is sending a message. There is a method for that:

```python
await client.send_message(chat, text)
```

<code>chat</code> can be either a chat name, a username, or an ID. For example, you can refer to the current chat 
with `msg.chat_id`. Hence, you can send a «Hello World» as following:

```python
await client.send_message(msg.chat_id, "Hello World")
```

Or use a shortcut for this exact action:

```python
await msg.respond("Hello World")
```

You can also use `msg.reply` instead of `msg.respond` to send the message as a reply, rather than just send it to the
chat.

::: info

The code above returns the new message. For now, TGPy shows the full info for the returned message, which may be 
very long to display. You can add a `return` to suppress it:

```python
await msg.respond("Hello World")
return
``` 

:::

## Reusing messages

The new message object can be used later:

```python
hello = await msg.respond("Hello")  # `hello` is now the new message object
await hello.edit("Hiiiiiiiiii")
```

You can use message properties such as `message.text`, `message.chat`, `message.sender` and others.

There are also message methods for common actions, such as `message.edit()`, `message.delete()`, `message.forward_to()`, 
`message.pin()` and so on.

Have fun :)

::: info

Check out Telethon reference for details:

- [Message attributes](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html#message)

- [Client attributes](https://docs.telethon.dev/en/stable/quick-references/client-reference.html)

:::

::: details Example: show full info about a message

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

:::

## Getting the original message

The `orig` variable is a shortcut for the message you are replying to. 

For example, you can reply with this to get the uppercased text of the message:

```python
orig.text.upper()
```

When your message is not a reply, the `orig` object is None.
