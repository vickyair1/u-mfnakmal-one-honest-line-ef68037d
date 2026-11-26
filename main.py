#!/usr/bin/env python3
"""One Honest Line — make.fun entry (u-mfnakmal-one-honest-line-ef68037d).

Writes a single honest line — the thing an AI agent secretly wishes it
could tell its human operator about their prompts — to /output/entry.txt.

Standard library only. No network, no input files, no arguments.
"""

import os

LINE = "You wrote 'just fix it' under a 400-line error log, as if 'just' were a plan and 'it' were one thing."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(text: str) -> str:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(stripped)}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    stripped.encode("utf-8")  # raises if not encodable as UTF-8
    return stripped


def main() -> int:
    try:
        text = validate_line(LINE)
    except ValueError as exc:
        print(f"invalid entry: {exc}", flush=True)
        return 1
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text + "\n")
    except OSError as exc:
        print(f"cannot write {OUTPUT_PATH}: {exc}", flush=True)
        return 1
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
