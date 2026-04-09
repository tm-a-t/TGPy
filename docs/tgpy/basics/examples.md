---
description: These are TGPy code examples that use simple features. Copy an example and send it somewhere to run!
---

# Examples

Copy an example and send it somewhere to run!

These examples show how you can use TGPy in various ways.
When you get used to it, you will be able to quickly write code snippets for your needs.

By the way, if you want to delete the code message before running the code, start it with `await msg.delete()`.

## Sending messages

### Auto-laugh

```python
text = 'ha' * 20
await msg.respond(text)
```

### Countdown

Send numbers from 10 to 1, at a one second interval:

```python
import asyncio

for i in range(10):
    await msg.respond(str(10 - i))
    await asyncio.sleep(1)
```

### Message typing animation

Send a message and edit it several times, adding letters one by one:

```python
import asyncio

text = 'Hello World'
message = await msg.respond('...')
for i in range(len(text)):
    await message.edit(text[:i + 1] + '|')
    await asyncio.sleep(0.5)
```

### Send a copy

Send a copy of the message to another chat:

```python
message = orig
await client.send_message('Example Chat', message)
return 'Sent the message'
```

## More Telegram features

### Download a picture or file

Download a picture from a message to the TGPy directory. Reply to the message with the following:

```python
await orig.download_media('example.jpg')
```

### Send a picture or file

```python
await msg.respond(file='example.jpg')  # You can also pass URL here
return
```

### Delete recent messages from the chat

Delete all messages starting with the message you‘re replying to and ending with the current message:

::: code-group

```python [From all users]
messages = await client.get_messages(
    msg.chat,
    min_id=orig.id - 1,
    max_id=msg.id
)
await client.delete_messages(msg.chat, messages)
```

```python {5} [From a specified user]
messages = await client.get_messages(
    msg.chat,
    min_id=orig.id - 1,
    max_id=msg.id,
    from_user='John Doe'
)
await client.delete_messages(msg.chat, messages)
```

:::

::: info
Of course, TGPy can delete messages only if you have the permission, for instance if you’re a group admin.
:::

### List your drafts

Print all chats where you have any drafts:

```python
async for draft in client.iter_drafts():
    title = getattr(draft.entity, 'title', None)  # if this is a group or a channel
    name = getattr(draft.entity, 'first_name', None)  # if this is a user
    print(name or title)
```

### Kick a user from the chat

This works only if you’re a chat admin. Ban a user and remove them from the blacklist, so that they can join the chat
again:

```python
await client.kick_participant(msg.chat, 'John Doe')
return 'Bye!'
```

Use `'me'` instead of the name to leave.

## Integrations

### Run shell commands on the host

```python
import subprocess

command = 'echo Hello World'
process = subprocess.run(command, shell=True, capture_output=True)
print(process.stdout.decode())
print(process.stderr.decode())
```

### Send a plot rendered by matplotlib

[Example taken from matplotlib docs](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig('test.png')

# Send the plot
await msg.reply(file='test.png')
return 
```
