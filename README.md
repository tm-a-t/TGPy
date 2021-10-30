![TGPy](readme_assets/TGPy.png)

## Run Python code right in your Telegram messages

Made with Telethon library, TGPy is a tool for evaluating expressions and Telegram API scripts.

- Do Python calculations in dialogs
- Interact with your messages and chats
- Automate sending messages and more

![Example](readme_assets/example.gif)

# Examples

Do Python calculations:

```python
a = [1, 2, 3]
a.append(4)
a

TGPy> [1, 2, 3, 4]
```

Delete the message in 5 seconds:
```python
import asyncio

await asyncio.sleep(5)
await msg.delete()
```

Forward the message you replied to to another chat:

```python
orig.forward_to('Chat title')

TGPy> Message(...)
```

Send all chat profile photos to the same chat:

```python
photos = await client.get_profile_photos(msg.chat)
msg.reply(file=photos)

TGPy> [...]
```

Define a function to forward messages to Saved Messages with reply:

```python
def save():
    message = await ctx.msg.get_reply_message()
    await message.forward_to('me')
    return 'Saved!'

TGPy> None
``` 

Define a function to delete messages you reply to with this function:
```python
async def delete():
    message = await ctx.msg.get_reply_message()
    await message.delete()
    await ctx.msg.delete()

TGPy> None
```

# [TGPy Guide](https://tgpy.tmat.me)

# Installation

1. You'll need Telegram API key. Register your "app" at [my.telegram.org](https://my.telegram.org) to get `api_id` and 
`api_hash`. App title and other data don't matter.

2. Clone the repo:
   ```shell
   > git clone https://github.com/tm-a-t/TGPy
   > cd TGPy
   ```

3. Create `config.py`. Enter your API data and your phone to log in:
   ```python
   api_id = ...
   api_hash = ...
   phone = ...
   ```

4. Install the requirements and run TGPy:
   ```shell
   > pip install -r requirements.txt
   > python -m app
   ```

# Credits

- Thanks to [penn5](https://github.com/penn5) for [meval](https://github.com/penn5/meval)
- Thanks to [Lonami](https://github.com/LonamiWebs) for [Telethon](https://github.com/LonamiWebs/Telethon)

# License

MIT
