"""Write the one-line honest appliance error entry to /output/entry.txt.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
characters, not only white space, and exactly one line. The line is
assembled from three parts so each clause can be tightened on its own:
the fault, the machine's alibi, and the accusation.
"""

import os

PARTS = (
    "Error: brush roll jammed with hair. ",
    "Not mine. I am bald. ",
    "We both know whose hair this is.",
)


def entry_line():
    return "".join(PARTS)


def main():
    line = entry_line()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    # Round-trip check: what the grader reads must be exactly the line
    # above, with no trailing newline added by the write.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch in /output/entry.txt"


if __name__ == "__main__":
    main()
