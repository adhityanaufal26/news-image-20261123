#!/usr/bin/env python3
"""Copy entry.png to the output directory.

Destination: $MAKEFUN_OUTPUT_DIR/entry.png if the env var is set,
otherwise /output/entry.png. The output directory is created if needed.
Stdlib only; byte-identical on every run.
"""
import os
import shutil
from pathlib import Path


def main():
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
