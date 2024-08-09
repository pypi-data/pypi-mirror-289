#!/usr/bin/env python3

"""Provides functionality to unload modules"""

import sys


def unload_module(path_or_name: str, prefix: str = "/ramdisk") -> None:
    """Searches and unloads module with provided name or file path.
    Not exactly sophisticated, but works for now..
    Implementation found here:
        https://forum.micropython.org/viewtopic.php?t=413&start=20
    """

    def without_prefix(string: str, prefix: str) -> str:
        return string[len(prefix) :] if string.startswith(prefix) else string

    for name, mod in sys.modules.items():
        if not (
            name == path_or_name
            or without_prefix(mod.__file__ or "", prefix).lstrip("/")
            == without_prefix(path_or_name, prefix).lstrip("/")
        ):
            continue
        try:
            loaded_module = __import__(name)
            del loaded_module
        except ImportError:
            pass
        try:
            del sys.modules[name]
        except KeyError:
            pass
        return
