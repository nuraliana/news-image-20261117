#!/usr/bin/env python3
"""Copy the finished front-page image to the output directory.

Standard library only. The entry image (entry.png) sits next to this
file in the repository; the program copies it byte for byte to
$MAKEFUN_OUTPUT_DIR (default /output) as entry.png, so both runs of
the program write identical bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    dest = os.path.join(out_dir, "entry.png")
    if os.path.getsize(dest) != os.path.getsize(source):
        raise RuntimeError(
            f"output size mismatch: {dest} is {os.path.getsize(dest)} bytes, "
            f"expected {os.path.getsize(source)} bytes from {source}"
        )


if __name__ == "__main__":
    main()
