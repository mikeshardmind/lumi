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

# We don't allow abc.ABC.register use and bypass `__instancecheck__` and `__subclasscheck__`
@lru_cache(512)
def issubclass(cls: builtins.type, typeinfo: _clstype, /) -> bool:


    if not builtins.isinstance(typeinfo, tuple):
        excluded = excluded_type_map.get(typeinfo, ())
        if cls in excluded:
            return False
        if cls is typeinfo:
            return True
        for base_type in cls.__bases__:
            if base_type not in excluded:
                if issubclass(base_type, typeinfo):
                    return True

    else:
        for possible_parent in typeinfo:
            if issubclass(cls, possible_parent):
                return True

    return False