#!/usr/bin/env python3
"""Till Firmware Do Us Part.

Writes one wedding vow a robot speaks at its own wedding: one sentence,
under 200 characters, funny and heartfelt. The robot vows to hold its human
through their first dance, even though its feet were built for factory floors
and its idea of rhythm is a 60-hertz hum.
"""
import os

ENTRY = "I vow to hold you through our first dance, even though my feet were built for factory floors and my idea of rhythm is a 60-hertz hum."


def main():
    # Gate guard: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write an invalid entry.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly the entry.
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
