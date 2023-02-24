# Modules

You may want to define functions, classes, or constants to reuse later. If you want to keep them when TGPy restarts,
save their definitions to modules.

Modules are code snippets that run at every startup.

## Add a module

Say TGPy ran your message. Then you can reply to your message with this method:

```python
modules.add(name)
```

Alternatively, you can add a module from a string with `#!python modules.add(name, source)`.

!!! example

    1. Define a square function:

        <div class="tgpy-code-block">
        ```python
        def square(x):
           return x * x
        ```
        <hr>
        ```
        TGPy> None
        ```
        </div>
    
    2. Save the definition to modules:

        <div class="tgpy-code-block">
        ```python
        # in reply to the previous message
        modules.add('square')
        ```
        <hr>
        ```
        TGPy> Added module 'square'.
        The module will be executed every time TGPy starts.
        ```
        </div>


!!! Info

    If a module with this name already exists, its code will be replaced.


## Remove a module

Remove a module by name:

```python
modules.remove(name)
```

## Storage

Modules are stored as separate Python files in <code>[tgpy/](/installation/#data-storage)modules</code> directory. You can safely edit them manually.

Modules run each time TGPy starts. By default, they run in the order they were added.

Each module file contains [module metadata](/reference/module_metadata).

## Features

By default, all variables from a module are saved for future use. You can specify ones the with the `__all__` variable.

## Manage modules

Use the string value of `modules` to list all of your modules:

```python
modules
```

The `modules` object provides handy ways to manage your modules. You can iterate over it to get names of your 
modules or use `modules[name]` to get info about the module.

## Disable standard modules

TGPy has a number of features implemented via stanard modules.
You may want to disable them, for example to reimplement these features yourself.

Disabled modules are controlled by the `core.disabled_modules` config key. 
For example, to disable the `prevent_eval` module (provides // and cancel features) use the following code:

```python
tgpy.api.config.set('core.disabled_modules', ['prevent_eval'])
```

Full list of standard modules can be seen [here](https://github.com/tm-a-t/TGPy/tree/master/tgpy/std).
