# Hooks

Hooks are executed every time TGPy starts. For example, with hooks you can define shortcut functions for future using.

## Add hooks

Add one of previous TGPy messages to hooks by replying with `hooks.add` function.

```python
hooks.add(hook_name)
```

You can also use `#!python hooks.add(hook_name, code)` to add any other code.

!!! example

    1. Define a square function:

        ```python
        def square(x):
         return x * x
        
        TGPy> None
        ```
    
    2. Save the definition to hooks:

        ```python
        # in reply to the previous message
        hooks.add('square')
        
        TGPy> Added hook 'square'.
        The hook will be executed every time TGPy starts.
        ```

## Remove hooks

Remove a hook by name:
```python
hooks.remove(hook_name)
```

!!! example

    ```python
    hooks.remove('square')

    TGPy> Removed hook 'square'.
    ```

## List hooks

To get all your hook names, use the string value of `hooks`:

```python
hooks
```

## Storage

Hooks are stored as .yaml files in `data/hooks` directory. You can edit them manually.

If TGPy fails to start because of hook errors, edit or delete the hook file.
