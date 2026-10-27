import re

_TAGS = set('address article aside base basefont blockquote body caption center col colgroup dd details dialog dir div dl dt fieldset figcaption figure footer form frame frameset h1 h2 h3 h4 h5 h6 head header hr html iframe legend li link main menu menuitem nav noframes ol optgroup option p param search section summary table tbody td tfoot th thead title tr track ul'.split())
_SPECIAL = re.compile(r'^<(pre|script|style|textarea)(?:[ \t>]|$)', re.I)
_TAG = re.compile(r'^</?([A-Za-z][A-Za-z0-9-]*)(?:[ \t/>]|$)')


def _start(line):
    s = line.rstrip('\n')
    s = re.sub(r'^ {0,3}', '', s)
    if _SPECIAL.match(s): return 1
    if s.startswith('<!--'): return 2
    if s.startswith('<?'): return 3
    if re.match(r'<![A-Za-z]', s): return 4
    if s.startswith('<![CDATA['): return 5
    m = _TAG.match(s)
    if m and m.group(1).lower() in _TAGS: return 6
    if re.fullmatch(r'</?[A-Za-z][A-Za-z0-9-]*(?:\s+[^<>]*?)?\s*/?>[ \t]*', s) and not re.match(r'^<(?:pre|script|style|textarea)(?:\s|>|/)', s, re.I): return 7
    return 0


def parse_html_block(lines, paragraph_open=False):
    if not lines: return None
    kind = _start(lines[0])
    if not kind or (kind == 7 and paragraph_open): return None
    consumed = 0
    for line in lines:
        consumed += 1
        if kind == 1 and re.search(r'</(?:pre|script|style|textarea)\s*>', line, re.I): break
        if kind == 2 and '-->' in line: break
        if kind == 3 and '?>' in line: break
        if kind == 4 and '>' in line: break
        if kind == 5 and ']]>' in line: break
        if kind in (6, 7) and (consumed == len(lines) or not lines[consumed].strip(' \t\r\n')): break
    return consumed, ''.join(lines[:consumed])
