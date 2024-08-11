# =============================================================================
#  PROJECT:      pgtestkit
#  FILE:         __main__.py
#  AUTHOR:       Daniel Marín
#  EMAIL:        dani4marin@gmail.com
#  CREATED:      2024-08-10
#  DESCRIPTION:  pgtestkit: unit and functional PostgreSQL testing with Python.
#  LICENSE:      MIT License
#  TYPING:       Python 3.8+ | Strongly Typed
# =============================================================================
#
#  Copyright (c) 2024 Daniel Marín
#
#  This file is part of the pgtestkit project. It is licensed under the terms
#  of the MIT License, as found in the LICENSE file in the root directory of
#  this source tree.
#
# =============================================================================
from __future__ import annotations

from _pgtestkit import __version__
from _pgtestkit import version_tuple


__all__ = [
    "__version__",
    "version_tuple",
]