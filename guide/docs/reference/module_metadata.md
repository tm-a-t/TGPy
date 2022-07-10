# Module metadata

Modules are stored as separate Python files in `data/modules` directory. Module metadata is a YAML comment in the module file.

You can safely edit it manually. The changes will apply after a restart.

## Metadata example

```python
"""
    name: MyModule
    once: false
    origin: tgpy://module/MyModule
    priority: 1655584820
    save_locals: true
"""
```

## Fields

### `name`

The module name.

### `once`

If `true`, the module will be deleted after running.

Default value: `false`

### `origin`

The string for the module origin (used for logs).

Default value: `tgpy://module/<module_name>`

### `priority`

Number defining the order of running the modules.

(The module with the lowest priority will run first)

Default value: timestamp for the time the module was created.

### `save_locals`

If `true`, the module variables can be later used in TGPy code snippets.

Default value: `true`
