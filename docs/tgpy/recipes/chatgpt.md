---
description: How to implement ChatGPT module for TGPy.
---

# Asking ChatGPT from TGPy

So, I implemented ChatGPT module for TGPy.

ChatGPT replies when I start my message with `ai,`:

![ChatGPT writes a joke about Python in a Telegram message](/assets/tgpy/chatgpt1.jpg)

It also remembers dialog history:

![ChatGPT explains its joke in another Telegram message](/assets/tgpy/chatgpt2.jpg)

To re-implement this feature, you will need to obtain an API key from [platform.openai.com.](https://platform.openai.com)

## 1. Functions

I wrote a couple of functions:

- `#!Python ai(text)` — sends a request to ChatGPT.
- `#!Python reset_ai()` — resets dialog history. You will want to reset the history often: API pricing [depends on the length of the dialog.](https://openai.com/pricing)

The official OpenAI Python library isn‘t async, so I made raw queries with aiohttp (`pip install aiohttp`).

```python
import aiohttp

openai_key = "YOUR_API_KEY_HERE"

http = aiohttp.ClientSession()
chatgpt_messages = []


async def ai(text: str) -> str:
  user_message = {"role": "user", "content": text}
  chatgpt_messages.append(user_message)
  result = await http.post(
    'https://api.openai.com/v1/chat/completions',
    headers={
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + openai_key,
    },
    json={ 
      "model": "gpt-3.5-turbo",
      "messages": chatgpt_messages,
    },
  )
  try:
    answer = result.json().await['choices'][0]['message']['content']
  except Exception as e:
    return 'Error: ' + str(e)
  assistant_message = {'role': 'assistant', 'content': answer}
  chatgpt_messages.append(assistant_message)
  return 'ChatGPT:\n' + answer


def reset_ai(prompt='You are a helpful assistant'):
  chatgpt_messages[:] = [{"role": "system", "content": prompt}]
  return 'Cleared ChatGPT dialog'
```

If you want to call GPT-4 instead of ChatGPT, replace `"gpt-3.5-turbo"` with `"gpt-4"`. See
[OpenAI API reference](https://platform.openai.com/docs/api-reference) for details.

Try it out: run the code above and call, `#!python ai('Hello ChatGPT!')`

## 2. Transformer

To address to ChatGPT by starting your message with `ai,` you will need a simple code transformer:

```python
def ai_transformer(text):
    prefix = 'ai, '
    if text.startswith(prefix):
        text = text.removeprefix(prefix)
        return f'ai("{text}")'
    return text

tgpy.api.code_transformers.add('chatgpt', ai_transformer)
```

This function transforms a string like `#!python 'ai, hello'` to code like `#!python ai("hello")`. 
By adding it as a transformer, you are applying it to all messages you send.
{.code-label}

Done!

Save all the code to a module and it will always work.

If you occasionally share sources of your modules with other people or publish modules in a git repo, you will want 
to store `openai_key` in an environment variable or [`tgpy.api.config`.](../extensibility/api#config)
