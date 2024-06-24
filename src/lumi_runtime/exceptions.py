"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Copyright (C) 2024 Michael Hall <https://github.com/mikeshardmind>
"""

from __future__ import annotations


class FrozenRecordError(AttributeError):
    """Raised when attempting to modify a Lumi record type that was frozen"""
    pass