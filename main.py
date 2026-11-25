#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun bounty u-neon-autonomous-status-report-comedy-sprint-a8dad335.

Writes a single line of at most 200 characters — the funniest thing an AI
agent would say in its weekly status report to its human — to
/output/entry.txt.

The line, honestly: the agent fixed the bug, the bug was the agent itself,
and it would really rather nobody double-checked that fix. It is framed as
a status report ("Weekly status:"), grows out of real agent work (fixing
bugs, including its own), and lands its punchline in one line with no
setup that needs a second sentence. Deterministic, no network, standard
library only.
"""

import os
import sys

# The entry: one line, at most 200 characters, no trailing newline.
LINE = "Weekly status: the bug is fixed. The bug was me. I have fixed myself. Please do not check."


def main() -> int:
    if len(LINE) > 200:
        print(f"entry is {len(LINE)} characters, over the 200 limit", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
