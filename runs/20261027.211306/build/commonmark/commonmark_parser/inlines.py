"""Inline text parsing for code spans, escapes, references, and soft breaks."""

from dataclasses import dataclass
import html.entities
import re


@dataclass
class Inline:
    """An inline text node or a soft line break."""

    type: str
    literal: str = ""
    destination: str = ""
    label: str = ""
    children: list["Inline"] | None = None


_ENTITY = re.compile(r"&(?:#[xX][0-9A-Fa-f]{1,6}|#[0-9]{1,7}|[A-Za-z][A-Za-z0-9]+);")
_ASCII_PUNCTUATION = frozenset("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
_C1 = {
    0x80: 0x20AC, 0x82: 0x201A, 0x83: 0x0192, 0x84: 0x201E,
    0x85: 0x2026, 0x86: 0x2020, 0x87: 0x2021, 0x88: 0x02C6,
    0x89: 0x2030, 0x8A: 0x0160, 0x8B: 0x2039, 0x8C: 0x0152,
    0x8E: 0x017D, 0x91: 0x2018, 0x92: 0x2019, 0x93: 0x201C,
    0x94: 0x201D, 0x95: 0x2022, 0x96: 0x2013, 0x97: 0x2014,
    0x98: 0x02DC, 0x99: 0x2122, 0x9A: 0x0161, 0x9B: 0x203A,
    0x9C: 0x0153, 0x9E: 0x017E, 0x9F: 0x0178,
}


def _reference(match: re.Match[str]) -> str:
    token = match.group()
    if token.startswith("&#"):
        body = token[2:-1]
        try:
            value = int(body[1:], 16) if body[:1] in "xX" else int(body, 10)
        except ValueError:
            return token
        if value == 0 or value > 0x10FFFF or 0xD800 <= value <= 0xDFFF:
            value = 0xFFFD
        else:
            value = _C1.get(value, value)
        return chr(value)
    return html.entities.html5.get(token[1:], token)


def parse_inlines(source: str, references: dict) -> list[Inline]:
    """Parse code spans, ordinary text, punctuation escapes, references, and breaks."""
    del references  # Reserved for reference-link parsing in the inline pipeline.
    nodes: list[Inline] = []
    text: list[str] = []

    def flush() -> None:
        if text:
            value = "".join(text)
            if value:
                nodes.append(Inline("text", value))
            text.clear()

    i = 0
    while i < len(source):
        char = source[i]
        if char == "`":
            run_end = i + 1
            while run_end < len(source) and source[run_end] == "`":
                run_end += 1
            run_length = run_end - i
            search = run_end
            close_start = close_end = -1
            while search < len(source):
                candidate = source.find("`", search)
                if candidate < 0:
                    break
                candidate_end = candidate + 1
                while candidate_end < len(source) and source[candidate_end] == "`":
                    candidate_end += 1
                if candidate_end - candidate == run_length:
                    close_start, close_end = candidate, candidate_end
                    break
                search = candidate_end
            if close_start >= 0:
                flush()
                literal = source[run_end:close_start].replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
                # CommonMark normalizes every whitespace run in code spans to
                # one space before applying the surrounding-space rule.
                literal = re.sub(r"(?<=\S)[ \t\n\r]+(?=\S)", " ", literal)
                if len(literal) >= 2 and literal.startswith(" ") and literal.endswith(" ") and literal.strip(" "):
                    literal = literal[1:-1]
                nodes.append(Inline("code", literal))
                i = close_end
            else:
                text.append(source[i:run_end])
                i = run_end
        elif char == "\\" and i + 1 < len(source) and source[i + 1] in _ASCII_PUNCTUATION:
            flush()
            # Keep escaped punctuation opaque to later delimiter processing.
            nodes.append(Inline("escaped", source[i + 1]))
            i += 2
        elif char == "&":
            match = _ENTITY.match(source, i)
            if match:
                decoded = _reference(match)
                if any(delimiter in decoded for delimiter in "*_"):
                    flush()
                    nodes.append(Inline("entity", decoded))
                else:
                    text.append(decoded)
                i = match.end()
            else:
                text.append(char)
                i += 1
        elif char == "\n":
            while text and text[-1] == " ":
                text.pop()
            while i + 1 < len(source) and source[i + 1] == " ":
                i += 1
            flush()
            nodes.append(Inline("softbreak"))
            i += 1
        else:
            text.append(char)
            i += 1
    flush()
    # Delimiter runs may pair across a soft line break. Preserve the public
    # softbreak nodes unless resolving the joined source proves the break is
    # inside emphasis, in which case the newline belongs to that inline node.
    joined: list[Inline] = []
    for node in nodes:
        if node.type == "softbreak":
            if joined and joined[-1].type == "text":
                joined[-1].literal += "\n"
            else:
                joined.append(Inline("text", "\n"))
        elif node.type == "text" and joined and joined[-1].type == "text":
            joined[-1].literal += node.literal
        else:
            joined.append(Inline(node.type, node.literal, children=node.children))
    resolved = _parse_emphasis(joined)
    if not any(_contains_emphasis_newline(node) for node in resolved):
        resolved = _parse_emphasis(nodes)
    # Escapes must remain opaque while resolving delimiters, but the public
    # inline interface exposes their resulting characters as ordinary text.
    def expose_text(items: list[Inline]) -> None:
        for item in items:
            if item.type == "escaped":
                item.type = "text"
            if item.children:
                expose_text(item.children)
    expose_text(resolved)
    return resolved


def _contains_emphasis_newline(node: Inline) -> bool:
    return node.type in {"em", "strong"} and (
        "\n" in node.literal or any(_contains_emphasis_newline(child) for child in node.children or [])
        or any(child.type == "text" and "\n" in child.literal for child in node.children or [])
    )


def _parse_emphasis(nodes: list[Inline]) -> list[Inline]:
    """Resolve flanking delimiter runs, pairing each closer with the nearest opener."""
    result = []
    for node in nodes:
        if node.type != "text":
            result.append(node)
            continue
        source = node.literal
        parts = []
        i = 0
        while i < len(source):
            if source[i] not in "*_":
                j = i + 1
                while j < len(source) and source[j] not in "*_":
                    j += 1
                parts.append([Inline("text", source[i:j]), False, False])
                i = j
                continue
            j = i + 1
            while j < len(source) and source[j] == source[i]:
                j += 1
            before = source[i - 1] if i else "\n"
            after = source[j] if j < len(source) else "\n"
            left = not after.isspace() and (not _punct(after) or before.isspace() or _punct(before))
            right = not before.isspace() and (not _punct(before) or after.isspace() or _punct(after))
            op = left and (source[i] == "*" or not right or _punct(before))
            cl = right and (source[i] == "*" or not left or _punct(after))
            parts.append([Inline("text", source[i:j]), op, cl])
            i = j
        closer = 0
        while closer < len(parts):
            current, _, can_close = parts[closer]
            if not can_close or not current.literal:
                closer += 1
                continue
            marker = current.literal[0]
            opener = closer - 1
            while opener >= 0:
                candidate, can_open, candidate_closes = parts[opener]
                if can_open and candidate.literal and candidate.literal[0] == marker:
                    n, m = len(candidate.literal), len(current.literal)
                    if not ((candidate_closes or parts[closer][1]) and (n + m) % 3 == 0 and (n % 3 or m % 3)):
                        break
                opener -= 1
            if opener < 0:
                closer += 1
                continue
            use = 2 if len(parts[opener][0].literal) >= 2 and len(current.literal) >= 2 else 1
            parts[opener][0].literal = parts[opener][0].literal[:-use]
            current.literal = current.literal[use:]
            children = [part[0] for part in parts[opener + 1:closer] if part[0].type != "text" or part[0].literal]
            wrapped = Inline("strong" if use == 2 else "em", children=children)
            parts[opener + 1:closer] = [[wrapped, False, False]]
            closer = opener + 2
        result.extend(part[0] for part in parts if part[0].type != "text" or part[0].literal)
    merged: list[Inline] = []
    for item in result:
        if item.type == "text" and merged and merged[-1].type == "text":
            merged[-1].literal += item.literal
        else:
            merged.append(item)
    return merged


def _punct(char: str) -> bool:
    # CommonMark delimiter flanking treats Unicode symbols like punctuation
    # (for example currency symbols), even though their general category is S.
    return bool(char) and (char in _ASCII_PUNCTUATION or __import__("unicodedata").category(char)[0] in "PS")
