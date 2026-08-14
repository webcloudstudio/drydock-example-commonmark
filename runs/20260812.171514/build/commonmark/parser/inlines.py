"""Inline-structure parsing boundary."""

from dataclasses import dataclass


@dataclass(frozen=True)
class InlineText:
    """Inline content ready for the renderer."""

    text: str


def parse_inlines(block: object, link_references: dict[str, str]) -> InlineText:
    """Parse inline structure after block parsing has completed."""

    del link_references
    text = block.text if hasattr(block, "text") else str(block)
    return InlineText(text=text)
