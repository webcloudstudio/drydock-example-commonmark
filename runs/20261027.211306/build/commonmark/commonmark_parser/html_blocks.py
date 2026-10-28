"""CommonMark raw HTML block recognition."""

import re

_BLOCK = set("address article aside base basefont blockquote body caption center col colgroup dd details dialog dir div dl dt fieldset figcaption figure footer form frame frameset h1 h2 h3 h4 h5 h6 head header hr html iframe legend li link main menu menuitem nav noframes ol optgroup option p param search section summary table tbody td tfoot th thead title tr track ul".split())


def _start(line: str):
    indent = len(line) - len(line.lstrip(" "))
    if indent > 3:
        return None
    text = line[indent:]
    patterns = [
        (1, re.compile(r"<(?:pre|script|style|textarea)(?:[ \t/>]|$)", re.I), re.compile(r"</(?:pre|script|style|textarea)\s*>", re.I)),
        (2, re.compile(r"<!--"), re.compile(r"-->")),
        (3, re.compile(r"<\?"), re.compile(r"\?>")),
        (4, re.compile(r"<![A-Z]"), re.compile(r">")),
        (5, re.compile(r"<!\[CDATA\["), re.compile(r"\]\]>")),
    ]
    for kind, begin, end in patterns:
        if begin.match(text):
            return kind, end
    # Type 6 blocks begin at a block tag even when its attributes or closing
    # angle bracket continue on a later line. They end at a blank line.
    tag = re.match(r"</?([A-Za-z][A-Za-z0-9-]*)(?=[\s/>]|$)", text)
    if tag and tag.group(1).lower() in _BLOCK:
        return 6, None
    if re.fullmatch(r"</?[A-Za-z][A-Za-z0-9-]*(?:[ \t]+[^<>]*)?/?>[ \t]*", text):
        return 7, None
    return None


def parse_html_block(lines: list[str], paragraph_open: bool = False):
    if not lines:
        return None
    start = _start(lines[0])
    if not start:
        return None
    kind, end = start
    if kind == 7 and paragraph_open:
        return None
    consumed = 0
    for line in lines:
        if kind >= 6 and not line.strip(" \t"):
            break
        consumed += 1
        if end and end.search(line):
            break
    return "".join(line + "\n" for line in lines[:consumed]), consumed
