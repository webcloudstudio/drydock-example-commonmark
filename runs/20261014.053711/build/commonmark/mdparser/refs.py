"""Link reference definitions: extraction, the document-wide reference map, and `normalize_label`.

Responsibility: extract link reference definitions when a paragraph closes, store them in one
reference map, and normalize labels with `str.casefold` plus whitespace collapse.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from mdparser.entities import ASCII_PUNCTUATION, unescape_and_decode

# A link label may hold at most this many characters between its brackets.
MAX_LABEL_LENGTH = 999
# Whitespace inside a label collapses to one space: spaces, tabs and line endings.
LABEL_WHITESPACE_PATTERN = re.compile(r"[ \t\r\n]+")
# Title delimiters: each opener maps to the closer that ends the title.
TITLE_CLOSERS = {'"': '"', "'": "'", "(": ")"}


@dataclass(frozen=True)
class LinkReference:
    """A stored definition: the decoded destination and the decoded title, or None when untitled."""

    destination: str
    title: str | None


def normalize_label(label: str) -> str:
    """Return the matching key for a link label.

    The brackets are stripped when the label has them, the text is case folded, and runs of
    spaces, tabs and line endings collapse to one space. Matching compares these keys only.
    """
    if label.startswith("[") and label.endswith("]"):
        label = label[1:-1]
    return LABEL_WHITESPACE_PATTERN.sub(" ", label.casefold()).strip(" ")


class ReferenceMap:
    """The document-wide map from normalized label to definition. The first definition wins."""

    def __init__(self) -> None:
        self._entries: dict[str, LinkReference] = {}

    def add(self, label: str, destination: str, title: str | None = None) -> None:
        """Store a definition under its normalized label unless that label is already present."""
        key = normalize_label(label)
        if key not in self._entries:
            self._entries[key] = LinkReference(destination, title)

    def get(self, label: str) -> LinkReference | None:
        """The definition for `label`, matched on its normalized form, or None when absent."""
        return self._entries.get(normalize_label(label))

    def __contains__(self, label: object) -> bool:
        return isinstance(label, str) and normalize_label(label) in self._entries

    def __len__(self) -> int:
        return len(self._entries)


def extract_definitions(text: str, references: ReferenceMap) -> str:
    """Remove the link reference definitions at the start of a closed paragraph's text.

    Each definition found is added to `references`. Scanning stops at the first line that is not a
    definition, and the rest of the text is returned. Text that is not at the start of the
    paragraph is never examined, so a definition cannot interrupt a paragraph.
    """
    pos = 0
    while pos < len(text):
        parsed = _parse_definition(text, pos)
        if parsed is None:
            break
        label, destination, title, pos = parsed
        references.add(label, destination, title)
    return text[pos:]


def _parse_definition(text: str, pos: int) -> tuple[str, str, str | None, int] | None:
    """Parse one definition at `pos`. Return (raw label, destination, title, index after it), or None."""
    label_end = scan_label(text, pos)
    if label_end is None:
        return None
    label = text[pos:label_end]
    if text[label_end : label_end + 1] != ":":
        return None
    index = skip_whitespace_with_line_ending(text, label_end + 1)
    destination = parse_destination(text, index)
    if destination is None:
        return None
    destination_text, after_destination = destination

    destination_line_end = _line_end(text, after_destination)
    if not _is_blank(text[after_destination:destination_line_end]):
        # Anything after the destination on its line must be a title on that same line.
        title_start = _skip_spaces(text, after_destination)
        if title_start == after_destination or not _is_title_opener(text, title_start):
            return None
        title = parse_title(text, title_start)
        if title is None or not _rest_of_line_is_blank(text, title[1]):
            return None
        return label, destination_text, title[0], _after_line(text, title[1])

    # The destination ends its line. A title may follow on a later line; if it does not parse
    # cleanly, the definition keeps its destination and the title text stays in the paragraph.
    title_start = skip_whitespace_with_line_ending(text, after_destination)
    if title_start > after_destination and _is_title_opener(text, title_start):
        title = parse_title(text, title_start)
        if title is not None and _rest_of_line_is_blank(text, title[1]):
            return label, destination_text, title[0], _after_line(text, title[1])
    return label, destination_text, None, _after_line(text, destination_line_end)


def scan_label(text: str, pos: int) -> int | None:
    """Return the index just past the closing `]` of a link label at `pos`, or None.

    The label is 1 to 999 characters between its brackets, holds no unescaped bracket, and has at
    least one non-whitespace character.
    """
    if text[pos : pos + 1] != "[":
        return None
    index = pos + 1
    while index < len(text):
        char = text[index]
        if char == "\\" and _is_escapable(text, index):
            index += 2
            continue
        if char == "[":
            return None
        if char == "]":
            inner = text[pos + 1 : index]
            if not 1 <= len(inner) <= MAX_LABEL_LENGTH or not inner.strip():
                return None
            return index + 1
        index += 1
    return None


def parse_destination(text: str, pos: int) -> tuple[str, int] | None:
    """Return the decoded destination and the index just past it, or None."""
    if text[pos : pos + 1] == "<":
        return _parse_angle_destination(text, pos)
    return _parse_plain_destination(text, pos)


def _parse_angle_destination(text: str, pos: int) -> tuple[str, int] | None:
    """A destination in angle brackets: no line ending, and no unescaped `<` or `>` inside."""
    index = pos + 1
    while index < len(text):
        char = text[index]
        if char == "\\" and _is_escapable(text, index):
            index += 2
            continue
        if char in "<\n":
            return None
        if char == ">":
            return unescape_and_decode(text[pos + 1 : index]), index + 1
        index += 1
    return None


def _parse_plain_destination(text: str, pos: int) -> tuple[str, int] | None:
    """A nonempty destination with no space or control character and balanced parentheses."""
    index = pos
    depth = 0
    while index < len(text):
        char = text[index]
        if char == "\\" and _is_escapable(text, index):
            index += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        elif char == " " or _is_ascii_control(char):
            break
        index += 1
    if index == pos or depth != 0:
        return None
    return unescape_and_decode(text[pos:index]), index


def parse_title(text: str, pos: int) -> tuple[str, int] | None:
    """A title in double quotes, single quotes or parentheses. Return (decoded title, index past it)."""
    opener = text[pos]
    closer = TITLE_CLOSERS[opener]
    index = pos + 1
    while index < len(text):
        char = text[index]
        if char == "\\" and _is_escapable(text, index):
            index += 2
            continue
        if char == closer:
            return unescape_and_decode(text[pos + 1 : index]), index + 1
        if opener == "(" and char == "(":
            return None
        index += 1
    return None


def _is_escapable(text: str, index: int) -> bool:
    """True when the backslash at `index` escapes the character after it."""
    return index + 1 < len(text) and text[index + 1] in ASCII_PUNCTUATION


def _is_title_opener(text: str, pos: int) -> bool:
    return text[pos : pos + 1] in TITLE_CLOSERS


def _is_ascii_control(char: str) -> bool:
    return char < " " or char == "\x7f"


def _is_blank(segment: str) -> bool:
    return segment.strip(" \t") == ""


def _skip_spaces(text: str, pos: int) -> int:
    """Index of the first character at or after `pos` that is not a space or tab."""
    while pos < len(text) and text[pos] in " \t":
        pos += 1
    return pos


def skip_whitespace_with_line_ending(text: str, pos: int) -> int:
    """Skip spaces and tabs, then at most one line ending, then spaces and tabs."""
    pos = _skip_spaces(text, pos)
    if text[pos : pos + 1] == "\n":
        pos = _skip_spaces(text, pos + 1)
    return pos


def _line_end(text: str, pos: int) -> int:
    """Index of the line ending at or after `pos`, or the end of the text."""
    end = text.find("\n", pos)
    return len(text) if end == -1 else end


def _after_line(text: str, pos: int) -> int:
    """Index just past the line ending at or after `pos`, or the end of the text."""
    end = _line_end(text, pos)
    return min(end + 1, len(text))


def _rest_of_line_is_blank(text: str, pos: int) -> bool:
    return _is_blank(text[pos : _line_end(text, pos)])
