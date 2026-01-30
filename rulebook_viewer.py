#!/usr/bin/env python3
"""
Render-friendly entrypoint.

The actual app script lives in `VSCODE MD Files/rulebook_viewer.py`, but that path contains spaces
which can be awkward for some deploy UIs. This wrapper simply delegates execution to that script.
"""

from __future__ import annotations

import runpy
from pathlib import Path


def main() -> None:
    target = Path(__file__).parent / "VSCODE MD Files" / "rulebook_viewer.py"
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()

