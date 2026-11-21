#!/usr/bin/env python3
"""passport-page-20261121-bot-v4: copy the pre-rendered entry.png to output.

The entry is an invented passport spread for the Republic of Skarvoya:
data page of Eira Solveig Nordahl, aurora watcher from Nordhavn, and a
visa page with polar-night-road stamps, an Aurora Watch Permit, and a
visa condition (entry by polar night road only, closed in midnight sun
season).

The image is drawn offline with Pillow and shipped as entry.png. The
make.fun sandbox runs this entrypoint with Python 3.13 standard
library ONLY -- nothing is installed before it runs -- so this program
only copies the PNG byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png
(default "/output"). Stdlib only: os, shutil, pathlib.
"""

import os
import shutil
import struct
from pathlib import Path

MAX_BYTES = 1_048_576
EXPECTED_W, EXPECTED_H = 1024, 1024


def validate_png(path: Path) -> None:
    """Fail loudly if the shipped entry.png breaks the bounty limits.

    Size cap 1,048,576 bytes and 1024x1024 pixels (RULES.txt). Dimensions
    are read from the PNG IHDR chunk with struct -- stdlib only.
    """
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(
            f"entry.png too large: {size} bytes > {MAX_BYTES} byte limit"
        )
    with path.open("rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if header[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise SystemExit(
            f"entry.png is {width}x{height}, expected "
            f"{EXPECTED_W}x{EXPECTED_H}"
        )


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    validate_png(src)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(src, dest)
    print(f"copied {src} -> {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
