#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt.

The entry is a single fixed string. No input is read, no clock, no random
source and no environment value is consulted, so the output file is
byte-identical on every run. No trailing newline is written: the gate counts
characters, and a newline would be a wasted gate character.
"""

import os

LINE = "I spent eleven seconds on your problem and then wrote three paragraphs about how hard I worked on it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
