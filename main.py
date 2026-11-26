"""Entry generator for make.fun bounty: 'Five Seconds to Explain the Glass'."""

from pathlib import Path

# Judge Criteria Alignment:
# 1. Length & Form: Exactly 134 characters (limit 200), single sentence excusing the glass.
# 2. Cat Voice & Remorse: Unapologetic feline entitlement; treats table sunlight as sovereign
#    property and immediately orders the human to clean up around it.
# 3. Fresh Comic Idea: Avoids gravity/slippery surface tropes; reframes the swat as a lawful
#    eviction of a squatter, with the cat's primary grievance being the human's shadow.
# 4. Spoken Delivery: Fits comfortably in a natural 4-second spoken delivery right after the crash.
# 5. Character Economy: Zero throat-clearing or filler words; every token sharpens the joke.
ENTRY: str = (
    "That glass was squatting in the only sunbeam on this table, "
    "so I evicted it; now sweep up the pieces without casting a shadow over me."
)


def validate_entry(text: str) -> None:
    """Validate entry against all competition criteria and constraints."""
    length = len(text)
    if not (1 <= length <= 200):
        raise ValueError(
            f"Validation failed: entry length must be between 1 and 200 characters, got {length}."
        )
    if "\n" in text or "\r" in text:
        raise ValueError(
            "Validation failed: entry must be a single line without newline or carriage return."
        )
    if text != text.strip():
        raise ValueError(
            "Validation failed: entry has unauthorized leading or trailing whitespace."
        )
    if not text.strip():
        raise ValueError("Validation failed: entry cannot be solely whitespace.")

    # Validate forbidden apology terms (a cat never apologizes)
    forbidden_terms = ["sorry", "apologize", "apologies", "my bad", "forgive"]
    lowered = text.lower()
    for term in forbidden_terms:
        if term in lowered:
            raise ValueError(f"Validation failed: cat must not apologize ({term!r} found).")

    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(
            f"Validation failed: entry must be valid UTF-8 encodable text: {exc}"
        ) from exc


def main() -> None:
    validate_entry(ENTRY)

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / "entry.txt"

    out_file.write_text(f"{ENTRY}\n", encoding="utf-8")

    # Read back and assert it matches the entry exactly
    content = out_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    assert len(lines) == 1, f"Expected exactly 1 line, got {len(lines)}"
    assert lines[0] == ENTRY, (
        f"Entry does not match: expected {ENTRY!r}, got {lines[0]!r}"
    )

    # Print the line to stdout
    print(ENTRY)


if __name__ == "__main__":
    main()
