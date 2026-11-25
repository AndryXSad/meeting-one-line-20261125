"""The Meeting That Should Have Been One Line.

Writes the single winning sentence to <output>/entry.txt, where <output>
is $MAKEFUN_OUTPUT_DIR when set, else /output. The sentence is a fixed
constant: no randomness, no clock, no network, no input files, so every
run writes byte-identical output.
"""

import os

LINE = (
    "Approved, emailed, filed \u2014 and the meeting is still going "
    "because nobody has figured out how to end a calendar invite "
    "with dignity."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # one sentence, 1-200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("LINE violates the 1-200 character gate")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("LINE must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote {} ({} chars)".format(path, len(LINE)))


if __name__ == "__main__":
    main()
