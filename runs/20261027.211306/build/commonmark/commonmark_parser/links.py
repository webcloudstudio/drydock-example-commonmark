"""Inline and reference link parsing."""

from __future__ import annotations

from dataclasses import dataclass
import html
import re

from .inlines import Inline, parse_inlines


@dataclass
class LinkNode:
    type: str
    literal: str = ""
    destination: str = ""
    title: str | None = None
    children: list[Inline | "LinkNode"] | None = None


_ESCAPE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])")
_ENTITY = re.compile(r"&(?:#[xX][0-9A-Fa-f]{1,6}|#[0-9]{1,7}|[A-Za-z][A-Za-z0-9]+);")


def _decode(value: str) -> str:
    value = _ESCAPE.sub(r"\1", value)
    return _ENTITY.sub(lambda m: html.unescape(m.group()), value)


def _normalize_label(label: str) -> str:
    return " ".join(label.casefold().split())


def _destination_and_title(source: str, start: int) -> tuple[str, str | None, int] | None:
    """Parse the contents after an opening parenthesis; return end after ')' ."""
    i, n = start, len(source)
    while i < n and source[i] in " \t\n\r":
        i += 1
    destination = ""
    if i < n and source[i] == "<":
        i += 1
        part: list[str] = []
        while i < n:
            if source[i] == "\\" and i + 1 < n:
                part.extend((source[i], source[i + 1])); i += 2; continue
            if source[i] == "<" or source[i] in "\r\n":
                return None
            if source[i] == ">":
                i += 1; destination = _decode("".join(part)); break
            part.append(source[i]); i += 1
        else:
            return None
    else:
        depth, part = 0, []
        while i < n:
            c = source[i]
            if c == "\\" and i + 1 < n:
                part.extend((c, source[i + 1])); i += 2; continue
            if c in " \t\n\r":
                break
            if c == "(":
                depth += 1
                if depth > 32: return None
            elif c == ")":
                if depth == 0: break
                depth -= 1
            part.append(c); i += 1
        if depth:
            return None
        destination = _decode("".join(part))
    whitespace = i
    while i < n and source[i] in " \t\n\r":
        i += 1
    separated = i > whitespace
    title = None
    if i < n and source[i] in "\"'(":
        opener = source[i]; closer = ")" if opener == "(" else opener
        i += 1; part = []
        while i < n:
            c = source[i]
            if c == "\\" and i + 1 < n:
                part.extend((c, source[i + 1])); i += 2; continue
            if c == closer:
                title = _decode("".join(part)); i += 1; break
            if c in "\r\n" and opener != "(":
                return None
            part.append(c); i += 1
        else:
            return None
        if not separated:  # title must be separated from destination
            return None
        while i < n and source[i] in " \t\n\r": i += 1
    if i >= n or source[i] != ")":
        return None
    return destination, title, i + 1


def _bracket_end(source: str, opening: int) -> int | None:
    depth, i = 1, opening + 1
    while i < len(source):
        if source[i] == "`":
            run_end = i + 1
            while run_end < len(source) and source[run_end] == "`":
                run_end += 1
            run = source[i:run_end]
            close = source.find(run, run_end)
            if close >= 0:
                i = close + len(run)
                continue
        if source[i] == "\\":
            i += 2; continue
        if source[i] == "[": depth += 1
        elif source[i] == "]":
            depth -= 1
            if depth == 0: return i
        i += 1
    return None


def parse_links(source: str, references: dict) -> list[Inline | LinkNode]:
    """Parse links from inline source using an already collected reference map."""
    result: list[Inline | LinkNode] = []
    text: list[str] = []

    def flush() -> None:
        if text:
            result.append(Inline("text", "".join(text)))
            text.clear()

    i = 0
    while i < len(source):
        # Code spans have precedence over brackets, so their contents cannot
        # start a link (nor can a bracket inside a link label close a span).
        if source[i] == "`":
            run_end = i + 1
            while run_end < len(source) and source[run_end] == "`":
                run_end += 1
            run = source[i:run_end]
            close = source.find(run, run_end)
            if close >= 0:
                end = close + len(run)
                text.append(source[i:end])
                i = end
                continue
        if source[i] == "\\" and i + 1 < len(source):
            text.extend(source[i:i + 2]); i += 2; continue
        if source[i] != "[" or (i and source[i - 1] == "!"):
            text.append(source[i]); i += 1; continue
        close = _bracket_end(source, i)
        if close is None:
            text.append(source[i]); i += 1; continue
        label_source = source[i + 1:close]
        parsed: tuple[str, str | None, int] | None = None
        after = close + 1
        if after < len(source) and source[after] == "(":
            parsed = _destination_and_title(source, after + 1)
        if parsed is not None:
            dest, title, end = parsed
        else:
            reference_label = label_source
            end = after
            if after < len(source) and source[after] == "[":
                ref_close = _bracket_end(source, after)
                if ref_close is not None:
                    reference_label = source[after + 1:ref_close] or label_source
                    end = ref_close + 1
            entry = references.get(_normalize_label(_decode(reference_label)))
            if entry is None:
                text.append(source[i]); i += 1; continue
            if isinstance(entry, dict):
                dest, title = entry.get("destination", ""), entry.get("title")
            else:
                dest, title = entry[0], entry[1] if len(entry) > 1 else None
        flush()
        result.append(LinkNode("link", destination=dest, title=title,
                               children=parse_inlines(label_source, {})))
        i = end
    flush()
    return result
