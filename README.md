XiVO CLI
========

XiVO CLI offers shortcuts for common XiVO CLI commands. For example, instead of typing:
```
less /var/log/xivo-ctid.log
```

you could type:

```
xivo l cti  # short for xivo-log cti
```

The XiVO CLI is inspired by the `ip` command interface, in particular the command abbreviation logic.

Currently supported commands:

* xivo-log

Custom commands
---------------

You may add custom commands to the XiVO CLI by putting any executable named `xivo-*` in your PATH, much like `git` also accepts custom commands. For example, calling:
```
xivo custom
```

will find the executable `xivo-custom` in your path, and execute it, forwarding any remaining argument.
