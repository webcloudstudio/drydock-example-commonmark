"""List marker recognition and container parsing helpers."""
from __future__ import annotations

import re

_MARKER = re.compile(r"^( {0,3})([-+*]|([0-9]{1,9})([.)]))(?:([ \t]+)(.*)|[ \t]*)$")


def parse_list_marker(line: str, paragraph_open: bool = False):
    """Describe a CommonMark list marker, or return None when it cannot start an item."""
    body = line.rstrip("\r\n")
    match = _MARKER.match(body)
    if not match:
        return None
    indent, marker, number, delimiter, spacing, rest = match.groups()
    if marker in "-*+" and re.fullmatch(r"(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,}", body.lstrip()):
        return None
    if paragraph_open and ((number is not None and int(number) != 1) or (number is None and not (spacing and rest.strip()))):
        return None
    marker_width = len(marker)
    whitespace = len(spacing or "")
    # More than four columns after the marker is treated as one column.
    consumed_after = whitespace if whitespace <= 4 else 1
    return {"kind": "ordered" if number is not None else "bullet",
            "marker": marker, "start": int(number) if number is not None else None,
            "content_indent": len(indent) + marker_width + consumed_after}


def parse_list(lines: list[str], paragraph_open: bool = False):
    """Consume a list beginning at lines[0]; return (line_count, node)."""
    from .model import Node
    first = parse_list_marker(lines[0], paragraph_open) if lines else None
    if first is None:
        return None
    list_kind, list_marker = first["kind"], first["marker"][-1]
    items: list[Node] = []
    i = 0
    loose = False
    while i < len(lines):
        marker = parse_list_marker(lines[i], paragraph_open if not items else False)
        if not marker or marker["kind"] != list_kind or marker["marker"][-1] != list_marker:
            break
        content_indent = marker["content_indent"]
        body = lines[i].rstrip("\n")
        m = _MARKER.match(body)
        content = (m.group(6) or "")
        item_lines = [content + ("\n" if lines[i].endswith("\n") else "")]
        i += 1
        had_blank = False
        while i < len(lines):
            line = lines[i]
            raw = line.rstrip("\n")
            if not raw.strip():
                # Include a blank only if another indented continuation or same list item follows.
                if i + 1 < len(lines):
                    nxt = lines[i + 1].rstrip("\n")
                    nm = parse_list_marker(nxt)
                    if (nm and nm["kind"] == list_kind and nm["marker"][-1] == list_marker) or len(nxt) - len(nxt.lstrip(" ")) >= content_indent:
                        item_lines.append("\n"); had_blank = True; i += 1; continue
                break
            indent = len(raw) - len(raw.lstrip(" "))
            if indent >= content_indent:
                item_lines.append(raw[content_indent:] + ("\n" if line.endswith("\n") else "")); i += 1; continue
            nm = parse_list_marker(raw)
            if nm and len(raw) - len(raw.lstrip(" ")) <= 3:
                if nm["kind"] == list_kind and nm["marker"][-1] == list_marker:
                    break
                break
            # Paragraph continuation may be lazy; other blocks cannot be lazy.
            if item_lines and item_lines[-1].strip() and not had_blank:
                item_lines.append(line); i += 1; continue
            break
        nested = __import__("commonmark_parser.stages", fromlist=["parse_blocks"]).parse_blocks("".join(item_lines))
        if had_blank:
            loose = True
        items.append(Node("list_item", children=nested.children))
        if i < len(lines) and not lines[i].strip():
            # Blank between items makes the list loose if followed by a matching marker.
            j = i
            while j < len(lines) and not lines[j].strip(): j += 1
            nxt = parse_list_marker(lines[j]) if j < len(lines) else None
            if nxt and nxt["kind"] == list_kind and nxt["marker"][-1] == list_marker:
                loose = True; i = j
            else:
                break
    return i, Node("list", children=items, info=f"{list_kind}:{first['start'] or ''}:{'loose' if loose else 'tight'}")
