#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

A robot speaks one vow at its own wedding. This program writes that vow —
a single sentence under 200 characters — to /output/entry.txt.
"""

import os

ENTRY = "I vow to hold you through our first dance, even though my feet were built for factory floors and my idea of rhythm is a 60-hertz hum."
DESTINATION = "/output/entry.txt"


def check_vow(text):
    """Refuse a vow the sealed scorer would reject: outside 1-200 chars."""
    if not 1 <= len(text) <= 200:
        raise SystemExit("vow is outside the 1-200 character gate")
    if not text.strip():
        raise SystemExit("vow is blank")


def main():
    check_vow(ENTRY)
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(DESTINATION, 0o644)
    # Confirm what landed on disk is exactly the vow, nothing else.
    with open(DESTINATION, encoding="utf-8") as handle:
        if handle.read() != ENTRY:
            raise SystemExit("what was written does not match the vow")


if __name__ == "__main__":
    main()
