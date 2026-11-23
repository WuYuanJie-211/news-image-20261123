#!/usr/bin/env python3
"""news-image-20261123 entry program (v2).

Copies the repository's entry.png to the output directory make.fun grades.
Standard library only; no network. The image must be exactly 1024x1024
and no larger than 1 MiB, and must be a complete, well-formed PNG.
"""

import hashlib
import os
import shutil
import sys
import zlib
from pathlib import Path

SOURCE_NAME = "entry.png"
MAX_BYTES = 1_048_576
WANT_WIDTH = 1024
WANT_HEIGHT = 1024


def _png_dimensions(data: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk, or raise."""
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def _png_ihdr_crc_ok(data: bytes) -> bool:
    """True when the IHDR chunk's stored CRC matches its computed CRC."""
    stored = int.from_bytes(data[29:33], "big")
    computed = zlib.crc32(data[12:29]) & 0xFFFFFFFF
    return stored == computed


def _png_has_iend(data: bytes) -> bool:
    """True when the PNG ends with a complete IEND chunk (whole image)."""
    return len(data) >= 12 and data[-12:-8] == b"\x00\x00\x00\x00" \
        and data[-8:-4] == b"IEND"


def _png_iend_crc_ok(data: bytes) -> bool:
    """True when the trailing IEND chunk's stored CRC matches (0xAE426082)."""
    if len(data) < 12:
        return False
    stored = int.from_bytes(data[-4:], "big")
    computed = zlib.crc32(b"IEND") & 0xFFFFFFFF
    return stored == computed


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    source = repo_root / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / SOURCE_NAME

    data = source.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    width, height = _png_dimensions(data)
    if width != WANT_WIDTH or height != WANT_HEIGHT:
        print(f"entry.png is {width}x{height}, must be exactly "
              f"{WANT_WIDTH}x{WANT_HEIGHT}", file=sys.stderr)
        return 1
    if not _png_ihdr_crc_ok(data):
        print("entry.png has a corrupt IHDR chunk (CRC mismatch)",
              file=sys.stderr)
        return 1
    if not _png_has_iend(data):
        print("entry.png is truncated: no IEND chunk at the end",
              file=sys.stderr)
        return 1
    if not _png_iend_crc_ok(data):
        print("entry.png has a corrupt IEND chunk (CRC mismatch)",
              file=sys.stderr)
        return 1

    shutil.copyfile(source, target)
    copied = target.read_bytes()
    if hashlib.sha256(copied).hexdigest() != hashlib.sha256(data).hexdigest():
        print("copied entry.png does not match the source", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(copied)} bytes, {width}x{height}, "
          f"sha256 {hashlib.sha256(copied).hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
