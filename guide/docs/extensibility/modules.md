# Using modules

All variables from your messages will be lost when TGPy stops. Yet, you can use modules to define some variables every
time TGPy starts.

Modules are code snippets executed every time TGPy starts. For example, with modules you can define some shortcut
functions, classes or constants for future using.

## Add a module

After running a code snippet with TGPy, you can add it to modules by replying with the `modules.add` function:

```python
modules.add(module_name)
```

You can add a module from a code string instead using `#!python modules.add(module_name, code)`.

!!! Info If a module with this name already exists, its code will be replaced.

!!! example

    1. Define a square function:

        ```python
        def square(x):
         return x * x
        
        TGPy> None
        ```
    
    2. Save the definition to modules:

        ```python
        # in reply to the previous message
        modules.add('square')
        
        TGPy> Added module 'square'.
        The module will be executed every time TGPy starts.
        ```

## Remove a module

Remove a module by name:

```python
modules.remove(module_name)
```

## Manage your modules

List all your modules with the string value of `modules`:

```python
modules
```

Modules are stored as separate Python files in `data/modules` directory. You can safely edit them manually.

Modules run each time TGPy starts. By default, they run in order of addition.

## Module settings

Module metadata is stored as a comment in the module file. You can edit it
manually. [Module metadata reference](/reference/module_metadata)
