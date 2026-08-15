"""Inline parsing boundary, supplied with references after block parsing."""

from dataclasses import dataclass

from references import ReferenceCollector


@dataclass(frozen=True)
class Inline:
    kind: str
    content: str


def parse_inlines(text: str, references: ReferenceCollector) -> tuple[Inline, ...]:
    """Return inline source nodes; detailed CommonMark rules grow in this phase."""
    del references
    return (Inline("text", text),) if text else ()
