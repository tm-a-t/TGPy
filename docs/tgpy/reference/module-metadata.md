---
description: Reference on module metadata. The metadata stores settings such as module name and execution order.
---

# Module metadata

[Modules are stored as separate Python files.](../extensibility/modules#storage) Module metadata is
a YAML comment in the beginning of the module file. You can safely edit it manually; the changes will apply 
after a restart.

## Metadata example

```python
"""
    name: MyModule
    once: false
    origin: tgpy://module/MyModule
    priority: 1655584820
"""

# module code goes here
```

## Fields

| Key        | Description                                                                                                              | Default value                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `name`     | The name of the module                                                                                                   |                                               |
| `once`     | If `true`, the module will be deleted after running.                                                                     | `false`                                       |
| `origin`   | The string that specifies the origin of the module (used for logs)                                                       | `tgpy://module/<module_name>`                 |
| `priority` | A number that defines the order in which modules are run at startup. The module with the lowest priority will run first. | timestamp for the time the module was created |

You can also define custom fields.


## Change as attributes

You can change the fields by editing the Module object. To set custom fields, use `.extra` dict. For example:

```python
m = modules['shell']
m.once = False
m.priority = 0
m.extra['description'] = 'This module defines shell() function'
m.save()
```

