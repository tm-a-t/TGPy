# Installation

You can install and run TGPy on your computer, but you may need a remote server instead to have TGPy available 24/7.

!!! warning

    **Make sure you run TGPy on a trusted machine** — that is, no one except you can read TGPy files on the computer.
    Anyone with access to TGPy files can steal your Telegram account.

    And the other way: anyone with access to your Telegram account has access to the machine TGPy is running on.

Make sure you have [Python 3.9 or above](https://www.python.org/) installed.

Install TGPy:

```shell
pip install tgpy
```

And start it:

=== "With simple command"

    ```shell
    tgpy
    ```

=== "If simple command doesn’t work"

    ```shell
    python -m tgpy
    ```

Follow the instructions to connect your Telegram account for the first time.

When it’s ready, try sending `ping()` to any chat to check if TGPy is running.

## Updating

Update to the latest version:

=== "From Telegram message"

    ```python
    update()
    ```

=== "From shell"

    ```shell
    pip install -U tgpy
    ```
