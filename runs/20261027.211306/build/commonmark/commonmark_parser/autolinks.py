"""Recognition of CommonMark URI and email autolinks."""

from dataclasses import dataclass
import re


@dataclass
class InlineNode:
    type: str
    literal: str = ""
    destination: str = ""
    label: str = ""


_URI = re.compile(r"[A-Za-z][A-Za-z0-9+.-]{1,31}:[^ <>\x00-\x20<>]*\Z")
_EMAIL = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\Z")


def parse_autolinks(source: str) -> list[InlineNode]:
    """Split valid angle-delimited autolinks from ordinary text."""
    nodes: list[InlineNode] = []
    pos = 0
    code_spans: list[tuple[int, int]] = []
    i = 0
    while i < len(source):
        if source[i] != "`":
            i += 1
            continue
        end = i + 1
        while end < len(source) and source[end] == "`":
            end += 1
        run = source[i:end]
        search = end
        matched = False
        while search < len(source):
            candidate = source.find("`", search)
            if candidate < 0:
                break
            close_end = candidate + 1
            while close_end < len(source) and source[close_end] == "`":
                close_end += 1
            if close_end - candidate == len(run):
                code_spans.append((i, close_end))
                i = close_end
                matched = True
                break
            search = close_end
        if not matched:
            i = end
    for match in re.finditer(r"<([^<>\n]*)>", source):
        # A code span opened before the angle token has precedence. Backticks
        # that begin inside a candidate autolink belong to its URI text.
        if any(start < match.start() < end for start, end in code_spans):
            continue
        body = match.group(1)
        destination = body if _URI.fullmatch(body) else "mailto:" + body if _EMAIL.fullmatch(body) else ""
        if not destination:
            continue
        if match.start() > pos:
            nodes.append(InlineNode("text", source[pos:match.start()]))
        nodes.append(InlineNode("link", destination=destination, label=body))
        pos = match.end()
    if pos < len(source):
        nodes.append(InlineNode("text", source[pos:]))
    return nodes
