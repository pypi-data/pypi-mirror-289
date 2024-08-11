# =============================================================================
#  PROJECT:      pgtestkit
#  FILE:         __main__.py
#  AUTHOR:       Daniel Marín
#  EMAIL:        dani4marin@gmail.com
#  CREATED:      2024-08-10
#  DESCRIPTION:  The pgtestkit entry point.
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

import pgtestkit


if __name__ == "__main__":
    raise SystemExit(pgtestkit.console_main())