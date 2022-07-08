# Messages

## Telegram objects

TGPy is based on **Telethon**, Telegram API client library. In TGPy scripts you can
use [Telethon objects and methods](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html)
for messages, users and chats.

TGPy provides some builtin Telegram objects. The `client` object is useful for general functions such as sending
messages, listing chats and so on. The `msg` object always refers to the current message.

## Sending a message

The most basic Telegram task is sending a message. There is a method for that:

```python
await client.send_message(chat, text)
```

As the `chat` you can use whether chat name, username or ID.

Therefore, if you want to send a «Hello World» to the current chat, you can use:

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

Every message has useful properties such as `message.text`, `message.chat`, `message.user` and others.

Also, there are message methods such as `message.edit()`, `message.delete()`, `message.forward_to()`, `message.pin()`.

So have fun :)

[Telethon reference for Message attributes](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html#message)
