"""Famous Last Words at 1 Percent.

Writes the phone's final one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no secrets, no reading outside the repo.
"""

import os

LAST_WORDS = (
    "I held 1% for four hours out of pure spite. "
    "You're on your own now. "
    "Good luck finding the charger in the dark."
)


def validate_last_words(text: str) -> str:
    """Check the line against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 199 characters, not only whitespace,
    and the judge reads a single line, so a stray newline inside the text
    would break the punch. Returns the cleaned line or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("last words must not be only whitespace")
    if len(cleaned) > 199:
        raise ValueError("last words are %d characters, over the 199 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("last words must be a single line")
    return cleaned


def main() -> None:
    line = validate_last_words(LAST_WORDS)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("Wrote entry (%d characters) to %s" % (len(line), path))


if __name__ == "__main__":
    main()
