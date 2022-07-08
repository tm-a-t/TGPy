# Using modules

Modules are executed when TGPy starts. For example, with modules you can define shortcut functions for future using.

## Add modules

Add one of previous TGPy messages to modules by replying with the `modules.add` function.

```python
modules.add(module_name)
```

You can also use `#!python modules.add(module_name, code)` to add any other code.

!!! Info 
    If a module with this name already exists, its code will be replaced.

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

## Remove modules

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

Modules run each time TGPy starts. By default, they run in order of addition. [Read about module settings](/extensibility/module_settings)
