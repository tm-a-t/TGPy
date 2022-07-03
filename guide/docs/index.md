# TGPy

### Run Python code right in your Telegram messages

TGPy is a tool for evaluating expressions and Telegram API scripts, built on top of [Telethon](https://github.com/LonamiWebs/Telethon).

- Do Python calculations in dialogs
- Interact with your messages and chats
- Automate sending messages and more

## Getting started

Python 3.9+ required. Host TGPy and connect it to your Telegram account:

```shell
> pip install tgpy
> tgpy
```

You’re ready now. Send Python code to any chat, and it will run. Change your message to change the result.

[Learn basics](/basics/code){ .md-button .md-button--primary }

<img alt="" src="https://raw.githubusercontent.com/tm-a-t/TGPy/master/readme_assets/example.gif" width="540">

## Userbot convenience

Since TGPy is a program to interact with your user account, it is called a _userbot_.

Unlike other userbots for evaluating code in messages, TGPy is designed for sequent and frequent using. That’s why it provides special features such as:

- Run every Python code without a command.
- Re-run a code message after editing.
- Auto-save variables for using in following messages. 
- Automatically return values and await functions.
- Save code as modules to run it every time TGPy starts.

TODO: links

## Credits

- Basic TGPy code transformation (such as values auto-return) is based on [meval](https://github.com/penn5/meval).
- TGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), which allows to integrate Telegram features in Python code. 

## License

This project is licensed under the terms of the MIT license.