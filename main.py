#!/usr/bin/env python3
"""Write one original one-star review to entry.txt.

The program is deterministic: it always emits the same single review,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

REVIEW = (
    "My phone battery lasts all day until I actually need it, "
    "then drops 40% in ten minutes."
)


def main() -> None:
    # Guard: the entry must be a single line under 200 chars before writing.
    assert "\n" not in REVIEW, "entry must be a single line"
    assert len(REVIEW) < 200, f"entry too long: {len(REVIEW)} chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
