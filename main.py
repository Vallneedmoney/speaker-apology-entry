"""Entry for make.fun bounty u-kiencx-sorry-i-heard-that-wrong-1858c729.

Writes one funny one-line apology a smart speaker gives its owner after
mishearing them, to entry.txt in the output directory. Standard library
only, fully deterministic: no network, no randomness, no timestamps.
"""

import os

LINE = "Sorry, I heard 'turn off the lights' as 'turn off the flights,' so I cancelled nothing. I did feel very powerful for a second, though."


def build() -> str:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build())


if __name__ == "__main__":
    main()
