"""Input normalization owned by the parser boundary."""

from dataclasses import dataclass


def expand_indentation(line: str, tab_width: int = 4) -> str:
    """Expand only leading indentation for structural column decisions.

    Tabs after the first non-whitespace character remain literal.  A tab in
    indentation advances to the next tab stop, as required by CommonMark.
    """
    column = 0
    index = 0
    expanded: list[str] = []
    while index < len(line):
        char = line[index]
        if char == " ":
            expanded.append(char)
            column += 1
        elif char == "\t":
            spaces = tab_width - (column % tab_width)
            expanded.append(" " * spaces)
            column += spaces
        else:
            expanded.append(line[index:])
            break
        index += 1
    return "".join(expanded)


def indentation_columns(line: str, tab_width: int = 4) -> int:
    """Return the visual indentation of a line without changing its text."""
    prefix = expand_indentation(line, tab_width)
    return len(prefix) - len(prefix.lstrip(" "))


@dataclass(frozen=True)
class NormalizedInput:
    """The normalized source passed to block parsing."""

    text: str


def normalize_input(text: str) -> NormalizedInput:
    """Normalize Unicode input without discarding indentation information."""
    if not isinstance(text, str):
        raise TypeError("Markdown input must be text")
    normalized = text.replace("\x00", "\ufffd").replace("\r\n", "\n").replace("\r", "\n")
    return NormalizedInput(normalized)
