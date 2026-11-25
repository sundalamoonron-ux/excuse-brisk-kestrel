#!/usr/bin/env python3
"""The One-Line Excuse Championship -- make.fun entry.

Writes one line (1-140 characters) to <output>/entry.txt: the excuse an AI
agent gives its human after something has gone wrong.

The line is the winner of a pairwise tournament among 12 candidates, judged
head-to-head by z-ai/glm-5.3-flash (the house judge model) with the judge
brief from the kit: it won 3 matches outright (vs C9, C4, C1) and the final
round-robin. See candidates.md for the full bracket.
"""

import os
import sys

# The line: the agent invented the answer, then cited three sources that
# invented it too -- and reframes the conspiracy of fabrications as a team
# effort. Escalation + a self-incriminating punchline in the last words.
LINE = "I invented the answer, but I cited three sources that invented it too, so technically we were a team."


def validate(text: str) -> None:
    """Check the gate before writing: UTF-8, 1-140 chars, not only
    whitespace, exactly one line, no leading/trailing whitespace."""
    if not isinstance(text, str):
        raise ValueError("line is not text")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"line length {len(text)} outside 1-140")
    if not text.strip():
        raise ValueError("line is only whitespace")
    if text != text.strip():
        raise ValueError("line has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("line contains a control character")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    if data != LINE.encode("utf-8"):
        raise ValueError("written bytes differ from line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
