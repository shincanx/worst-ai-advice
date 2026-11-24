#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt (the file the sealed scorer reads) and prints it.
The line is deterministic: the same bytes on every run, no network.
"""

import os

LINE = (
    "Pro tip: tattoo your passwords on your arm \u2014 "
    "skin is the only cloud hackers can't breach."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
