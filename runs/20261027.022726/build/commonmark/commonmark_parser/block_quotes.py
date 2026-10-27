"""Block quote marker extraction."""

import re

_MARKER = re.compile(r'^ {0,3}> ?')


def parse_block_quote(lines: list[str]):
    """Return consumed lines and quote content, including paragraph laziness."""
    if not lines or not _MARKER.match(lines[0].rstrip('\n')):
        return None
    content: list[str] = []
    consumed = 0
    paragraph_open = False
    for line in lines:
        body = line.rstrip('\n')
        marker = _MARKER.match(body)
        if marker:
            text = body[marker.end():]
            content.append(text + ('\n' if line.endswith('\n') else ''))
            consumed += 1
            if not text.strip():
                paragraph_open = False
            elif not paragraph_open:
                paragraph_open = True
            continue
        if (not body.strip() or not paragraph_open or
                re.match(r'^ {0,3}(?:#{1,6}(?:[ \t]|$)|(?:\*\s*){3,}$|(?:-\s*){3,}$|(?:_\s*){3,}$|`{3,}|~{3,})', body)):
            break
        content.append(line)
        consumed += 1
    return consumed, content
