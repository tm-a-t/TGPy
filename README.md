# TGPy

### Run Python code right in your Telegram messages

TGPy is a tool for evaluating expressions and Telegram API scripts, built on top of [Telethon](https://github.com/LonamiWebs/Telethon).

- Do Python calculations in dialogs
- Interact with your messages and chats
- Automate sending messages and more

## Getting started

Python 3.9+ required. Install TGPy and connect it to your Telegram account:

```shell
> pip install tgpy
> tgpy
```

You’re ready now. Send Python code to any chat, and it will run. Change your message to change the result.

Details on installation: http://tgpy.tmat.me/installation/

<img alt="" src="https://raw.githubusercontent.com/tm-a-t/TGPy/master/readme_assets/example.gif" width="540">

## New TGPy docs

**[Basics Guide:](http://tgpy.tmat.me/basics/code/)** All you need to know to start using TGPy.

**[Extensibility Guide:](http://tgpy.tmat.me/extensibility/context/)** Special features for advanced usage.

**[Reference:](http://tgpy.tmat.me/reference/builtins/)** List of TGPy objects and settings.

## Inspiration

TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. This leads both to convenience of single-use scripts and reusage flexibility.

## Credits

TGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), which allows to integrate Telegram features in Python code.

Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

## License

This project is licensed under the terms of the MIT license.
