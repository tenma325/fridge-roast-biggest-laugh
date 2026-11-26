#!/usr/bin/env python3
"""Entry for make.fun: Fridge Roast, One Line, Biggest Laugh.

The entry is one line of at most 200 characters roasting a
smart fridge, and it roasts the fridge's proudest feature:
the inventory camera. The fridge photographs its contents,
catalogues them in the cloud and sends a weekly report, and
somehow still cannot answer the only question ever asked of
it, which is whether there is milk. A appliance that knows
the yoghurt's biography but not the milk's whereabouts has
not become smart; it has become a documentary crew,
complete with narration it sends to my phone at midnight.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My smart fridge catalogues every yoghurt in the cloud "
    "but still can't tell me if we have milk; it's not smart, "
    "it's a documentary crew."
)

# The yoghurt has 400 photos, a timeline and a fan wiki.
# The milk's status remains, officially, 'unconfirmed'.
PHOTOS_OF_YOGHURT = 400


def render_entry() -> str:
    """Return the roast exactly as it will be served, chilled."""
    return ENTRY_TEXT


def one_line_fridge_roast(text: str) -> bool:
    """Confirm the roast is one line of at most 200 characters."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_line_fridge_roast(text), "one line, at most 200 chars"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
