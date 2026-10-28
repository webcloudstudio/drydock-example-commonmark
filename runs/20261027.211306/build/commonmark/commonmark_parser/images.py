"""Inline and reference image parsing."""

from __future__ import annotations

from dataclasses import dataclass
import html
import re

from .inlines import Inline, parse_inlines
from .links import _bracket_end, _decode, _destination_and_title, _normalize_label, parse_links


@dataclass
class ImageNode:
    type: str
    destination: str
    title: str | None
    alt: str


_ESCAPED = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])")


def _plain_description(source: str, references: dict) -> str:
    """Return text content of a description, dropping inline formatting."""
    # First identify nested images so their alternative text contributes as text.
    nested = parse_images(source, references)
    # A compact source transform retains descriptions while removing image
    # syntax; inline providers then decode escapes/entities and emphasis.
    out: list[str] = []
    i = 0
    while i < len(source):
        if source.startswith("![", i):
            close = _bracket_end(source, i + 1)
            if close is not None:
                label = source[i + 2:close]
                after = close + 1
                parsed = _destination_and_title(source, after + 1) if after < len(source) and source[after] == "(" else None
                dest = parsed is not None
                if parsed:
                    out.append(_plain_description(label, references)); i = parsed[2]; continue
                ref_label, end = label, after
                if after < len(source) and source[after] == "[":
                    ref_close = _bracket_end(source, after)
                    if ref_close is not None:
                        ref_label = source[after + 1:ref_close] or label
                        end = ref_close + 1
                if _normalize_label(_decode(ref_label)) in references:
                    out.append(_plain_description(label, references)); i = end; continue
        out.append(source[i]); i += 1
    plain = "".join(out)
    links = parse_links(plain, references)
    pieces: list[str] = []
    for node in links:
        if node.type == "link":
            pieces.extend(_plain_nodes(node.children or []))
        else:
            pieces.extend(_plain_nodes(parse_inlines(node.literal, references)))
    return "".join(pieces)


def _plain_nodes(nodes: list) -> list[str]:
    result: list[str] = []
    for node in nodes:
        if node.type in {"text", "code", "escaped"}:
            result.append(node.literal)
        elif node.children:
            result.extend(_plain_nodes(node.children))
        elif node.type == "softbreak":
            result.append("\n")
    return result


def parse_images(source: str, references: dict) -> list[ImageNode]:
    """Parse image constructs in source, resolving definitions by normalized label."""
    nodes: list[ImageNode] = []
    i = 0
    while i < len(source):
        if source[i] != "!" or (i and source[i - 1] == "\\") or i + 1 >= len(source) or source[i + 1] != "[":
            i += 1; continue
        close = _bracket_end(source, i + 1)
        if close is None:
            i += 1; continue
        label = source[i + 2:close]
        after = close + 1
        parsed = _destination_and_title(source, after + 1) if after < len(source) and source[after] == "(" else None
        if parsed is not None:
            destination, title, end = parsed
        else:
            ref_label, end = label, after
            if after < len(source) and source[after] == "[":
                ref_close = _bracket_end(source, after)
                if ref_close is not None:
                    ref_label = source[after + 1:ref_close] or label
                    end = ref_close + 1
            entry = references.get(_normalize_label(_decode(ref_label)))
            if entry is None:
                i += 1; continue
            if isinstance(entry, dict):
                destination, title = entry.get("destination", ""), entry.get("title")
            else:
                destination, title = entry[0], entry[1] if len(entry) > 1 else None
        nodes.append(ImageNode("image", destination, title, _plain_description(label, references)))
        i = end
    return nodes
