"""Named data types shared by the parser phases."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Document:
    """Parsed document blocks and document-wide link references."""

    blocks: list[object] = field(default_factory=list)
    references: dict[str, object] = field(default_factory=dict)
