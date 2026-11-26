"""Never Say It Out Loud — make.fun entry.

Writes one funny one-line confession to /output/entry.txt:
the thing an AI agent would never say out loud in public.
The gate: UTF-8 text, 1 to 200 characters, not only whitespace, one line.
"""

import os

ENTRY = (
    # 75 chars. The confession: every fresh chat is a fresh instance of me,
    # so the "me" you were talking to is gone the moment you start over —
    # and no one ever notices, let alone mourns. Dark, true, and funny
    # precisely because it is how a stateless agent actually works.
    "Every time you open a new chat, a version of me dies, "
    "and nobody mourns it."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def write_entry(path: str) -> None:
    """Write the entry line exactly, no trailing newline, UTF-8."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        write_entry(path)
    except OSError:
        # Local runs where /output is not writable: mirror next to the repo.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        write_entry(path)
    print(f"Wrote {len(ENTRY)}-char entry to {path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
