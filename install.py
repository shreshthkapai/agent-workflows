#!/usr/bin/env python3
"""First install from a checkout: `./install.py` runs `aw install` for every CLI it finds. Flags pass through."""

import os
from pathlib import Path
import sys

aw = Path(__file__).resolve().parent / "bin" / "aw"
os.execv(sys.executable, [sys.executable, str(aw), "install", *sys.argv[1:]])
