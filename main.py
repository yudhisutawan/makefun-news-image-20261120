"""The World Today - front page summing up Friday 20 November 2026.

Writes the pre-rendered 1024x1024 newspaper front page to the output
directory as entry.png (``$MAKEFUN_OUTPUT_DIR`` when set, else ``/output``).

Standard library only: the image lives in this repository as entry.png and
is copied byte for byte, so the program runs in a bare Python 3.13
container with no image libraries and no fonts. No network, no clock, no
randomness: every run writes identical bytes.

The image's SHA256 is
ec4f2f956d72f368355c895d672b48b88ce35e9796cb47696be28b299ffebd3d.

Run:  python3 main.py
"""

import os
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out = out_dir / "entry.png"
    # Plain byte copy: no re-encoding, no timestamps in the output, so two
    # runs produce the same file. The source lives in this repository.
    out.write_bytes(src.read_bytes())
    assert out.stat().st_size == src.stat().st_size, "copy size mismatch"
    print("wrote", out, "1024x1024")


if __name__ == "__main__":
    main()
