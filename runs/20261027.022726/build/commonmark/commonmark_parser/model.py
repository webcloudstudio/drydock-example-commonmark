from dataclasses import dataclass, field


@dataclass
class Node:
    """A block or inline node; raw content is retained for later stages."""

    type: str
    children: list["Node"] = field(default_factory=list)
    raw: str = ""
    level: int | None = None
    literal: str = ""
    info: str = ""

    @property
    def raw_content(self) -> str:
        return self.raw


@dataclass
class Document:
    children: list[Node] = field(default_factory=list)
    references: dict[str, tuple[str, str | None]] = field(default_factory=dict)
