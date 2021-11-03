# Home

### Run Python code right in your Telegram messages

Made with Telethon library, TGPy is a tool for evaluating expressions and Telegram API scripts.

- Do Python calculations in dialogs
- Interact with your messages and chats
- Automate sending messages and more

![Example](assets/example.gif)

Just send Python code to any chat, and it will be executed. Change your message to change the result.

## Examples

Send any of these examples to any chat to evaluate:

🐍 Do Python calculations

```python
for i in range(5):
    print(i)
```

⏳ Delete the current message in 5 seconds

```python
import asyncio

await asyncio.sleep(5)
await msg.delete()
```

↪️ Forward the message you replied to to another chat

```python
orig.forward_to('Chat title')
```

🖼 Send all chat profile photos to the same chat

```python
photos = await client.get_profile_photos(msg.chat)
msg.reply(file=photos)
```

🔖 Define a function which forwards messages to Saved Messages with reply

```python
def save():
    message = ctx.msg
    original = await message.get_reply_message()
    await original.forward_to('me')
    return 'Saved!'
``` 

🗑 Define a function which deletes messages with reply

```python
async def delete():
    message = ctx.msg
    original = await message.get_reply_message()
    await original.delete()
    await message.delete()
```

## Guide

- [Basics](basics)
- [TGPy builtins](builtins)
- [Code detection](code_detection)

## Installation

[Go to Installation](installation){ .md-button }

## Credits

- Thanks to [penn5](https://github.com/penn5) for [meval](https://github.com/penn5/meval)
- Thanks to [Lonami](https://github.com/LonamiWebs) for [Telethon](https://github.com/LonamiWebs/Telethon)

## License

This project is licensed under the terms of the MIT license.
