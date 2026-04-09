---
description: 'Sometimes you will want to send notifications to yourself, such as reminders or logs. There are multiple approaches: scheduling messages, using a bot, or marking chats as unread.'
---

# Setting up reminders   

Sometimes you will want to send notifications to yourself, such as reminders or logs.   

You basically don't get a notification when your TGPy code sends a message to any chat, pretty like you don't get a notification when you send a message from another device.   

There are a few workarounds.   

## Method 1. Scheduling messages   

Telegram has a built-in feature for scheduling messages. You can try it by opening the app and long-tapping (or right clicking) the «Send» button.   

Luckily, Telegram notifies you whenever any of your scheduled messages was sent.   

That means your TGPy script can postpone a message by a minute rather then send it, and you will get a notification on your devices.   

Saved Messages suit well for scheduling reminders. You can also create a private group or channel to have such notifications there.   

The realization is as easy as adding the `schedule` argument to `client.send_message()` or `msg.respond()`. For example, this is how to schedule a message to Saved Messages:   

```python
import datetime as dt

next_minute = dt.datetime.utcnow() + dt.timedelta(minutes=1)
await client.send_message('me', 'Hey there!', schedule=next_minute)
```

## Method 2. Using a bot   

Direct messages from a bot are the natural way to have notifications.   

It's super-easy to control a bot from TGPy, as Telethon methods can be used for bots as well as user accounts.   

Firstly, you should create a bot with BotFather. Then log in using the bot token and API key that you are already using:   

```python
from telethon import TelegramClient
bot = TelegramClient('bot', client.API_ID, client.API_KEY)
await bot.start('your_token')
```

As a user, you should start the dialog so that the bot will be able to send you messages.   

The bot can talk now.   

```python
await bot.send_message(msg.sender_id, 'Hello world')
return
```

Just like this, you can use `bot` with familiar client methods to edit and pin messages, for example.   

## Bonus method. Marking chats as unread   

Putting «Unread» mark on a chat without notification may also be helpful.   

I used to have TGPy auto-reposting memes from other social media to my channel. My TGPy module sent a message and then marked the chat as unread so I would notice the new messages later.   

To mark a chat as uread, you should use the special API method:   

```python
from telethon import functions

await client(functions.messages.MarkDialogUnreadRequest(peer='Example Chat', unread=True))
```

As usual, `peer` here can be anything tha Telethon can convert to a peer: the title, the username, the id, a chat object and so on.   
