#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Copies the pre-rendered front page (entry.png, 1024x1024, Sunday
22 November 2026) into the grader's output directory. Deterministic:
both runs write the same bytes. Standard library only, no network.
"""
import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    # The output directory is provided by the grader; only write into it,
    # never delete or replace it.
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
