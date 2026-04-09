[//]: # (# TGPy. <span style="color: var&#40;--vp-c-text-2&#41;">Your Pythonic Swiss Knife for Telegram</span>)

# TGPy

<p style="display: flex; align-items: start; column-gap: 2px">
    <a href="https://github.com/tm-a-t/tgpy" target="_blank">
        <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/tm-a-t/tgpy?style=flat-square&logo=github" style="border-radius: 10px">
    </a>
    <a href="https://pypi.org/project/tgpy" target="_blank">
        <img alt="GitHub Repo stars" src="https://img.shields.io/pypi/v/tgpy?style=flat-square" style="border-radius: 10px">
    </a>
</p>

---

TGPy is a Pythonic swiss knife for Telegram. 
It runs Python code in your messages and integrates with your Telegram workspace. 
See the video:

<video controls loop muted src="https://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4" style="border: solid var(--vp-c-text-3) 1px"></video>

## Quick Start

Python 3.10+ required. Install using pipx:

```shell
pipx install tgpy
tgpy
```

or Docker:

```shell
docker pull tgpy/tgpy
docker run -it --rm -v /tgpy_data:/data tgpy/tgpy
```

Then follow instructions to connect your Telegram account.

## Next steps

- [More on installation](installation.md)
- [Learn TGPy basics](basics/code)

TGPy uses Telegram API through the [Telethon](https://github.com/LonamiWebs/Telethon) library.

## Use Cases

Here are a few examples of how people use TGPy:

🧮 Run Python as an in-chat calculator

🔍 Search for song lyrics within a chat

🧹 Delete multiple messages with a command

📊 Find out the most active members in a chat

## About

TGPy allows you to easily write and execute code snippets directly within your Telegram messages. Combine Telegram
features with the full power of Python: Integrate with libraries and APIs. Create functions and TGPy modules to reuse
code in the future. Set up code transformers and hooks to create custom commands and tweak Python syntax.


TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. 
However, the key concept is different: 
TGPy is totally based on usage of code in Telegram rather than plugging extra modules. 
It was designed for running single-use scripts and reusing code flexibly. 
You can think of TGPy as a userbot for programmers.

We built TGPy with [Telethon](https://github.com/LonamiWebs/Telethon), a Python library to interact with Telegram API.
Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

MIT license.
