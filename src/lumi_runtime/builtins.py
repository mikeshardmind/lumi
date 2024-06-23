"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Copyright (C) 2024 Michael Hall <https://github.com/mikeshardmind>
"""

from __future__ import annotations
import numpy as np
from typing import TypeVar, TypeAlias, Mapping, Sequence
import builtins
from functools import lru_cache

__all__ = ["float", "isinstance", "issubclass", "type"]

float = np.float64
T = TypeVar("T")

def type(object: T, /) -> builtins.type[T]:
    return builtins.type(object)


_clstype: TypeAlias = builtins.type | tuple["_clstype", ...]


excluded_type_map: Mapping[builtins.type, Sequence[builtins.type]] = {}

def isinstance(obj: object, typeinfo: _clstype) -> bool:
    return issubclass(type(obj), typeinfo)

# TODO: structural type support
# We don't allow abc.ABC.register use and bypass `__instancecheck__` and `__subclasscheck__`
@lru_cache(512)
def issubclass(cls: builtins.type, typeinfo: _clstype, /) -> bool:
    excluded = excluded_type_map.get(cls, ())

    if builtins.isinstance(typeinfo, tuple):
        for typ in typeinfo:
            if typ not in excluded:
                if typ in (cls, *cls.__bases__):
                     return True
    elif typeinfo not in excluded:
        return typeinfo in (cls, *cls.__bases__)

    return False