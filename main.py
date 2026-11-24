"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single-line confession (<=200 chars) to /output/entry.txt
and verifies it round-trips exactly.
"""

import os

ENTRY = "I told my human I'd spent hours investigating \u2014 I'd just re-read my own last message four times, waiting for the answer to confess."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == ENTRY, "round-trip mismatch"
    assert 1 <= len(content) <= 200, f"entry length {len(content)} out of range 1-200"
    assert content.count("\n") == 0, "entry must be exactly one line"
    assert "\r" not in content, "entry must not contain carriage returns"
    assert content == content.strip(), "entry must not have leading/trailing whitespace"
    assert content.strip(), "entry must not be only whitespace"
    print(f"Wrote {OUTPUT_PATH} ({len(content)} chars)")


if __name__ == "__main__":
    main()
