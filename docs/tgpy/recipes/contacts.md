---
description: I wrote a TGPy script that adds to contacts all members from a selected group. Now I can see their stories and identify them in other contexts.
---

# Auto-adding group members to contacts to see their stories

I barely ever add people from Telegram to contacts. I chat in groups and private messages, so I have them in
my Telegram dialog history.

However, recently Telegram introduced stories. Their visibility is based on saved contacts: you need to have a person 
added to contacts if you want to see their stories.

I felt FOMO...

So I wanted to massively add all users from my favorite groups to contacts.

I also didn’t want to turn my contact list to a mess, so contacts should have been categorized. I would mark
their names with hashtags. For example, if I add to contacts _John Doe_ who I know from _Example Chat_, their contact title
will be _John Doe #ExampleChat._

Saving contacts with the sources would also help me remember from where I know these people.

I decided that every contact will have only one hashtag, as I usually know a person from one chat or a set of similar
chats (thus, one hashtag will be enough to identify the person.)

I only wanted to add people from a few chats I care about and didn’t want to implement regular contact updating.
I just wrote a code that would instantly add to contacts all members of a specified group.

So here is the code. When I want to use it, I paste it and change `chat` and `mark` variables.

`chat` can be the chat title, username, or id, whatever;

`mark` is the hashtag to add to contact names (without '#').

```python
from telethon.tl.functions.contacts import AddContactRequest

chat = ''
mark = ''

logs_chat = msg.chat
suffix = ' #' + mark
print('conflicts:')
async for user in client.iter_participants(chat):
    if user.contact and not (user.last_name and user.last_name.endswith(suffix)):
        print(user.first_name, user.last_name or '')
        continue
    elif user.contact or user.bot or user.id == msg.sender_id:
        continue

    first_name = user.first_name
    last_name = (user.last_name or '') + suffix
    username = '@' + user.username if user.username else ''
    phone = user.phone or ''

    await client(
        AddContactRequest(
            user,
            first_name,
            last_name,
            phone,
            add_phone_privacy_exception=False,
        )
    )
```

The code outputs «conflicts»: list of people who are already in my contacts but are marked with other hashtags or no
hashtag at all. These I handle manually.

Also, I want to keep my contact list clean, so I manually remove special symbols or emoji from contacts’ names.
