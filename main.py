"""Write one funny excuse for skipping a pointless meeting to entry.txt.

Pure standard library. Deterministic: the same single line every run.
The line stays well inside the 1-200 character gate.
"""

import os

LINE = (
    "Sorry — I'm double-booked with the meeting about why we have too many "
    "meetings, and unlike this one, that one actually has an agenda."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
