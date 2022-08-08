# Module metadata

Modules are stored as separate Python files in `data/modules` directory. Module metadata is a YAML comment at the start of the module.

You can safely edit it manually. The changes will apply after a restart.

[Read on using modules](/extensibility/modules/)

## Metadata example

```python
"""
    name: MyModule
    once: false
    origin: tgpy://module/MyModule
    priority: 1655584820
    save_locals: true
"""

# module code goes here
```

## Fields

| Key | Description | Default value |
| --- | ----------- | ------------- |
| `name` | The name of the module | |
| `once` | If `true`, the module will be deleted after running | `false` |
| `origin` | The string specifying the origin of the module (used for logs) | `tgpy://module/<module_name>` |
| `priority` | A number that defines the order in which modules are run at startup. The module with the lowest priority will run first | timestamp for the time the module was created |
| `save_locals` | If `true`, the module variables can be later used in TGPy code snippets | `true` |
