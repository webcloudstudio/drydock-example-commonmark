"""Document-wide link reference definition extraction."""

import html
import re

_LABEL = re.compile(r"^ {0,3}\[((?:\\.|[^\[\]\\])+)\]:[ \t]*(.*)$", re.S)


def _unescape(value: str) -> str:
    value = html.unescape(value)
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)


def _label(value: str) -> str:
    return " ".join(value.casefold().strip(" \t\r\n").split())


def extract_definitions(text: str, references: dict) -> str:
    lines = text.splitlines(keepends=True)
    offset = 0
    while offset < len(lines):
        current = lines[offset].rstrip("\r\n")
        label_end = offset
        while current.lstrip().startswith("[") and not _LABEL.match(current) and label_end + 1 < len(lines):
            label_end += 1
            current += "\n" + lines[label_end].rstrip("\r\n")
        match = _LABEL.match(current)
        if not match or not match.group(1).strip():
            break
        offset = label_end
        key = _label(match.group(1))
        first_definition = key not in references
        rest = match.group(2).strip(" \t")
        # Destinations and titles may continue on following lines. Keep the
        # original indentation available while applying the CommonMark limits.
        if not rest and offset + 1 < len(lines):
            candidate = lines[offset + 1].strip(" \t\r\n")
            if candidate:
                rest = candidate
                offset += 1
        if rest and rest[0] in "\"'(" and rest[-1] != ({'"': '"', "'": "'", "(": ")"}[rest[0]]) and offset + 1 < len(lines):
            candidate = lines[offset + 1].strip(" \t\r\n")
            if candidate:
                rest += " " + candidate
                offset += 1
        # A title can span multiple nonblank lines; consume it only when closed.
        title_start = re.search(r"(?:^|[ \t])([\"'(])", rest)
        if title_start:
            opener = title_start.group(1)
            closer = ")" if opener == "(" else opener
            start = title_start.end()
            if closer not in rest[start:]:
                end_offset = offset
                extra = ""
                while end_offset + 1 < len(lines) and lines[end_offset + 1].strip():
                    end_offset += 1
                    extra += "\n" + lines[end_offset].rstrip("\r\n").strip(" \t")
                    if closer in extra:
                        rest += extra
                        offset = end_offset
                        break
        destination = None
        title = None
        if rest.startswith("<"):
            end = rest.find(">")
            if end > 0 and "\n" not in rest[1:end]:
                destination, tail = rest[1:end], rest[end + 1:].strip(" \t")
                separated = end + 1 == len(rest) or rest[end + 1].isspace()
            else:
                break
        else:
            dest_match = re.match(r"((?:\\.|[^\s])*)", rest)
            destination = dest_match.group(1) if dest_match else ""
            tail = rest[len(destination):].strip(" \t")
            separated = len(destination) == len(rest) or rest[len(destination)].isspace()
            if destination.count("(") - destination.count(")") > 0:
                break
        if not destination and not (rest.startswith("<") and rest.startswith("<>")):
            break
        if tail:
            if not separated or tail[0] not in "\"'(" or tail[-1] != ({'"': '"', "'": "'", "(": ")"}[tail[0]]):
                break
            title = _unescape(tail[1:-1])
        if first_definition:
            references[key] = (_unescape(destination), title)
        offset += 1
        if offset < len(lines) and lines[offset].lstrip(" \t").startswith(("\"", "'", "(")) and title is None:
            candidate = lines[offset].strip(" \t\r\n")
            if len(candidate) >= 2 and candidate[0] in "\"'(" and candidate[-1] == {'"': '"', "'": "'", "(": ")"}[candidate[0]]:
                if first_definition:
                    references[key] = (_unescape(destination), _unescape(candidate[1:-1]))
                offset += 1
    return "".join(lines[offset:])
