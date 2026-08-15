"""Document-wide link-reference collection and lookup."""

from dataclasses import dataclass, field
import re


def normalize_label(label: str) -> str:
    # Only spaces, tabs, and line endings are collapsible in labels.
    return " ".join(re.split(r"[ \t\r\n]+", label.strip(" \t\r\n"))).casefold()


@dataclass
class ReferenceCollector:
    """Mutable during block parsing, immutable in practice for later phases."""

    definitions: dict[str, tuple[str, str | None]] = field(default_factory=dict)

    def add(self, label: str, destination: str, title: str | None = None) -> None:
        self.definitions.setdefault(normalize_label(label), (destination, title))

    def get(self, label: str) -> tuple[str, str | None] | None:
        return self.definitions.get(normalize_label(label))


def _unescape(value: str) -> str:
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)


def _balanced_title(text: str, start: int) -> tuple[str, int] | None:
    opener = text[start]
    closer = ")" if opener == "(" else opener
    i = start + 1
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    title_parts = normalized[start + 1:].split("\n")
    if any(not line.strip(" \t") for line in title_parts[1:-1]):
        return None
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == closer:
            return _unescape(text[start + 1:i]), i + 1
        i += 1
    return None


def parse_definition(lines: list[str], start: int) -> tuple[int, str, str, str | None] | None:
    """Parse one definition at the beginning of a paragraph's source lines."""
    first = lines[start]
    match = re.match(r"^[ \t]{0,3}\[", first)
    if not match:
        return None
    # Remove only the permitted indentation, retaining the label's source.
    text = first[first.index("["):]
    i = start
    close = None
    while i < len(lines) and len(text) <= 1000:
        if i > start:
            text += "\n" + lines[i]
        for pos, char in enumerate(text):
            if char == "]" and (pos == 0 or text[pos - 1] != "\\"):
                close = pos
                break
        if close is not None:
            break
        i += 1
    if close is None:
        return None
    label = text[1:close]
    if not label.strip(" \t\r\n") or "[" in re.sub(r"\\\[", "", label):
        return None
    rest = text[close + 1:]
    if not rest.startswith(":"):
        return None
    rest = rest[1:]
    consumed = i + 1
    rest = rest.lstrip(" \t")
    if not rest and consumed < len(lines):
        rest = lines[consumed].lstrip(" \t")
        consumed += 1
    if rest.startswith("<"):
        end = rest.find(">", 1)
        if end < 0 or "\n" in rest[1:end] or "<" in rest[1:end]:
            return None
        destination, rest = rest[1:end], rest[end + 1:]
        if rest and rest[0] not in " \t\r\n":
            return None
    else:
        destination_match = re.match(r"([^ \t\r\n]+)(.*)$", rest)
        if not destination_match:
            return None
        destination, rest = destination_match.groups()
        depth = 0
        escaped = False
        for char in destination:
            if escaped:
                escaped = False
                continue
            if char == "\\":
                escaped = True
                continue
            if char == "(": depth += 1
            elif char == ")": depth -= 1
            if depth < 0: return None
    rest = rest.lstrip(" \t")
    title = None
    if rest:
        if rest[0] not in "\"'(":
            return None
        title_result = _balanced_title(rest, 0)
        while title_result is None and consumed < len(lines):
            rest += "\n" + lines[consumed]
            consumed += 1
            title_result = _balanced_title(rest, 0)
        if title_result is None:
            return None
        title, end = title_result
        if rest[end:].strip(" \t"):
            return None
    elif consumed < len(lines) and lines[consumed].lstrip(" \t").startswith(("\"", "'", "(")):
        candidate = lines[consumed].lstrip(" \t")
        title_result = _balanced_title(candidate, 0)
        if title_result is not None and not candidate[title_result[1]:].strip(" \t"):
            title, _ = title_result
            consumed += 1
    if rest and any(not line.strip(" \t") for line in rest.replace("\r\n", "\n").replace("\r", "\n").split("\n")[:-1]):
        return None
    return consumed, label, _unescape(destination), title
