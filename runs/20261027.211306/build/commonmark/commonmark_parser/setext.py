"""Setext heading recognition for paragraph source lines."""

import re
from collections.abc import Sequence

_UNDERLINE = re.compile(r"^ {0,3}(=+|-+)[ \t]*$")


def parse_setext(lines: Sequence[str]) -> tuple[int, str] | None:
    """Return a heading level and raw content for paragraph lines plus underline."""
    if len(lines) < 2:
        return None
    match = _UNDERLINE.fullmatch(lines[-1])
    if match is None:
        return None
    content = "\n".join(lines[:-1]).strip(" \t")
    if not content:
        return None
    return (1 if match.group(1)[0] == "=" else 2), content
