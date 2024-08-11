# =============================================================================
#  PROJECT:      pgtestkit
#  FILE:         __init__.py
#  AUTHOR:       Daniel Marín
#  EMAIL:        dani4marin@gmail.com
#  CREATED:      2024-08-10
#  DESCRIPTION:  The pgtestkit package initialization.
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


__all__ = ["__version__", "version_tuple"]

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown"
    version_tuple = (0, 0, "unknown")