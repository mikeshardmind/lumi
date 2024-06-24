"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Copyright (C) 2024 Michael Hall <https://github.com/mikeshardmind>
"""

from __future__ import annotations
from typing import Any
# piggybacking on mumpy's implementation, for now. These are compatible with Lumi's numeric principles
from numpy import uint8, uint16, uint32, uint64, uint128, int8, int16, int32, int64, int128


#: This should never be manually used. It's used by Lumi for generating latebound function defaults.
MISSING: Any = object()
