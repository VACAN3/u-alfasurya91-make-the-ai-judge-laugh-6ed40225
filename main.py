"""One office-life joke, one line, for the make.fun bounty
u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing) and prints it to stdout.
"""

import os
import sys

# Final: two concrete numbers ($12,000, 90 slides) escalating to a banal
# payoff; deadpan understatement, exactly one twist, fresh consultant angle.
LINE = "We spent $12,000 on a consultant whose 90-slide deck concluded that we should talk to each other more."

MIN_LEN = 1
MAX_LEN = 159  # sealed scorer accepts 1-200; past rounds only scored 1-159


def main() -> int:
    line = LINE.strip()
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        print(
            f"ERROR: entry is {len(line)} chars, must be {MIN_LEN}-{MAX_LEN}",
            file=sys.stderr,
        )
        return 1
    if "\n" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
