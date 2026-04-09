---
description: You can use TGPy to throw dice in Telegram and brute-force it to get a fake result. This also works with other emoji such as football and casino.
---

# Throwing dice (and faking the result)

When you send the 🎲 (dice) emoji in Telegram, it gets animated and shows a random result.

This trick works similarly on 🎯 🎳 ⚽️ 🏀. However, in this recipe I will refer to all such animation messages
as «dice messages» (they call it all dice in Telegram API.)

You can send a dice message from TGPy as following:

```python
from telethon.tl.types import InputMediaDice as Dice

await msg.respond(file=Dice('🎲'))
return
```

You can change the emoji to throw something other than a dice.
{.code-label}

You can't choose the result, because it's generated server-side. You also can't edit a dice message. Nevertheless, you
can send dice and delete them until you get the desired result:

```python
from telethon.tl.types import InputMediaDice as Dice


async def throw_dice(val):
    m = await ctx.msg.respond(file=Dice('🎲'))
    while m.media.value != val:
        await m.delete()
        m = await ctx.msg.respond(file=Dice('🎲'))
```

This will work for about 2 seconds. Chat members will see your messages quickly appear and disappear until you get the
right dice.

Note that the method works only in groups and channels due to the fact that you can't delete dice messages in direct
messages.

In terms of emoji other than 🎲, the result is usually represented in the same way. That is, the value is a number from 1
to 6 and 6 is the best result.

🎰 (casino) result, however, is the number from 1 to 64 where 64 is the win.

I don't recommend using the above brute-force method on 🎰, because it will spam sending-deleting messages for a while.
