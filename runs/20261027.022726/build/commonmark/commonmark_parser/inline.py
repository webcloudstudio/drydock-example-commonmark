"""Inline escape and character-reference decoding helpers."""

from html.entities import html5
import re


_ASCII_PUNCTUATION = frozenset(
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)
_NAMED = re.compile(r"&([A-Za-z][A-Za-z0-9]+);")
_NUMERIC = re.compile(r"&#(?:([0-9]{1,7})|[xX]([0-9A-Fa-f]{1,6}));")
_BACKTICK_RUN = re.compile(r"`+")
_AUTOLINK = re.compile(r"<(https?://[^ <>]*|mailto:[^ <>]*|[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+)>")
_HTML_TAG = re.compile(r"</?[A-Za-z][^<>]*>|<!--.*?-->|<\?.*?\?>|<![A-Z][^<>]*>", re.S)
_DELIMS = re.compile(r"(\*+|_+)")


def _punct(ch: str) -> bool:
    return bool(ch) and (ch in _ASCII_PUNCTUATION or __import__('unicodedata').category(ch)[0] in 'PS')


def _resolve_emphasis(text: str) -> str:
    """Resolve delimiter runs with CommonMark flanking and multiple-of-three rules."""
    import html
    runs = []
    for match in _DELIMS.finditer(text):
        marker = match.group()[0]
        before = text[match.start()-1:match.start()]
        after = text[match.end():match.end()+1]
        before_ws = not before or before.isspace()
        after_ws = not after or after.isspace()
        before_p = _punct(before)
        after_p = _punct(after)
        left = not after_ws and (not after_p or before_ws or before_p)
        right = not before_ws and (not before_p or after_ws or after_p)
        if marker == '_':
            can_open, can_close = left and (not right or before_p), right and (not left or after_p)
        else:
            can_open, can_close = left, right
        runs.append({'start': match.start(), 'end': match.end(), 'char': marker,
                     'length': len(match.group()), 'open': can_open, 'close': can_close,
                     'used_open': 0, 'used_close': 0})
    before_tags = {}
    after_tags = {}
    consumed = set()
    for ci, closer in enumerate(runs):
        if not closer['close']:
            continue
        while closer['length'] - closer['used_close']:
            opener = None
            for oi in range(ci - 1, -1, -1):
                candidate = runs[oi]
                if candidate['char'] != closer['char'] or not candidate['open']:
                    continue
                if candidate['length'] == candidate['used_open'] + candidate['used_close']:
                    continue
                # Rule of three applies when either run can both open and close.
                if ((candidate['close'] or closer['open']) and
                    (candidate['length'] + closer['length']) % 3 == 0 and
                    (candidate['length'] % 3 != 0 or closer['length'] % 3 != 0)):
                    continue
                opener = candidate
                break
            if opener is None:
                break
            available_open = opener['length'] - opener['used_open'] - opener['used_close']
            available_close = closer['length'] - closer['used_open'] - closer['used_close']
            use = 2 if available_open >= 2 and available_close >= 2 else 1
            opener['used_open'] += use
            closer['used_close'] += use
            # Delimiters left unmatched inside a resolved pair are literal;
            # they cannot later escape the span and create crossing emphasis.
            for between in runs[ runs.index(opener) + 1:ci ]:
                if between['used_open'] + between['used_close'] < between['length']:
                    between['open'] = False
                    between['close'] = False
            opening_tag = '<strong>' if use == 2 else '<em>'
            closing_tag = '</strong>' if use == 2 else '</em>'
            op_start = opener['end'] - opener['used_open']
            cl_start = closer['start'] + closer['used_close'] - use
            before_tags.setdefault(op_start, []).append(opening_tag)
            after_tags.setdefault(cl_start + use - 1, []).append(closing_tag)
            consumed.update(range(op_start, opener['end']))
            consumed.update(range(cl_start, cl_start + use))
    out = []
    i = 0
    while i < len(text):
        out.extend(before_tags.get(i, ()))
        if i not in consumed:
            out.append(html.escape(decode_escapes_and_entities(text[i])))
        out.extend(after_tags.get(i, ()))
        i += 1
    return ''.join(out)


def _numeric_character(decimal: str | None, hexadecimal: str | None) -> str:
    codepoint = int(decimal, 10) if decimal is not None else int(hexadecimal, 16)
    if codepoint == 0 or codepoint > 0x10FFFF or 0xD800 <= codepoint <= 0xDFFF:
        codepoint = 0xFFFD
    return chr(codepoint)


def decode_escapes_and_entities(text: str) -> str:
    """Decode eligible CommonMark backslash escapes and semicolon references."""
    output: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text) and text[i + 1] in _ASCII_PUNCTUATION:
            output.append(text[i + 1])
            i += 2
            continue
        if text[i] == "&":
            numeric = _NUMERIC.match(text, i)
            if numeric:
                output.append(_numeric_character(numeric.group(1), numeric.group(2)))
                i = numeric.end()
                continue
            named = _NAMED.match(text, i)
            if named:
                value = html5.get(named.group(1) + ";")
                if value is not None:
                    output.append(value)
                    i = named.end()
                    continue
        output.append(text[i])
        i += 1
    return "".join(output)


def _link_at(text: str, start: int, references: dict | None):
    """Return (end, label, destination, title) for a link beginning at ``[``."""
    n = len(text); depth = 1; i = start + 1
    while i < n:
        if text[i] == "\\" and i + 1 < n:
            i += 2; continue
        if text[i] == '`':
            run = _BACKTICK_RUN.match(text, i)
            close_run = next((m for m in _BACKTICK_RUN.finditer(text, run.end())
                              if len(m.group()) == len(run.group())), None)
            if close_run:
                i = close_run.end(); continue
        if text[i] == '<':
            opaque = _AUTOLINK.match(text, i) or _HTML_TAG.match(text, i)
            if opaque:
                i = opaque.end(); continue
        if text[i] == "[": depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0: break
        i += 1
    if depth: return None
    label = text[start+1:i]; close = i
    # Inline destination: optional whitespace, balanced parentheses, optional title.
    j = close + 1
    if j < n and text[j] == "(":
        j += 1
        while j < n and text[j] in " \t\n": j += 1
        dest = ""
        if j < n and text[j] == "<":
            j += 1; buf=[]
            while j < n and text[j] != ">":
                if text[j] == "\\" and j+1<n:
                    if text[j+1] not in _ASCII_PUNCTUATION: buf.append('\\')
                    buf.append(text[j+1]); j+=2
                else:
                    if text[j] in "<>\n": return None
                    buf.append(text[j]); j+=1
            if j == n: return None
            j += 1; dest="".join(buf)
        else:
            buf=[]; parens=0
            while j < n:
                c=text[j]
                if c == "\\" and j+1<n:
                    if text[j+1] in _ASCII_PUNCTUATION: buf.append(text[j+1])
                    else: buf.extend(("\\", text[j+1]))
                    j+=2; continue
                if c == "(" :
                    parens += 1
                    if parens > 32: return None
                elif c == ")":
                    if parens == 0: break
                    parens -= 1
                if c in " \t\r\n" and parens == 0: break
                buf.append(c); j+=1
            dest="".join(buf)
        while j < n and text[j] in " \t\n": j+=1
        title=None
        if j<n and text[j] in '\"\'(':
            opener=text[j]; closer=')' if opener=='(' else opener; j+=1; buf=[]
            while j<n and text[j]!=closer:
                if text[j]=='\\' and j+1<n: buf.append(text[j+1]); j+=2
                else: buf.append(text[j]); j+=1
            if j==n: return None
            title="".join(buf); j+=1
            while j<n and text[j] in " \t\n": j+=1
        if j<n and text[j]==")": return j+1,label,dest,title
        # Invalid inline syntax falls through to reference resolution.
    # Full, collapsed, and shortcut reference forms.
    ref_label=None; end=close+1
    if end<n and text[end]=='[':
        k=end+1
        while k<n and text[k]!=']':
            if text[k]=='\\' and k+1<n: k+=2
            else: k+=1
        if k<n:
            ref_label=text[end+1:k] or label; end=k+1
    else: ref_label=label
    if references is not None:
        from .references import normalize_label
        definition=references.get(normalize_label(ref_label))
        if definition is not None: return end,label,definition[0],definition[1]
    return None


def render_inline(text: str, references: dict | None = None, links_allowed: bool = True) -> str:
    """Render inline content while allowing delimiters around opaque inline nodes."""
    import html
    atoms: list[str] = []
    chars: list[str] = []
    i = 0
    def atom(markup: str):
        key = chr(0xE000 + len(atoms))
        atoms.append(markup); chars.append(key)
    while i < len(text):
        if text.startswith('![', i):
            image = _link_at(text, i + 1, references)
            if image:
                end, label, dest, title = image
                from urllib.parse import quote
                src = quote(decode_escapes_and_entities(dest), safe="/:@-._~!$&'()*+,;=%#?")
                alt = re.sub(r'<[^>]*>', '', render_inline(label, references, False))
                attrs = f' src="{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}"'
                if title is not None:
                    attrs += f' title="{html.escape(decode_escapes_and_entities(title), quote=True)}"'
                atom(f'<img{attrs} />'); i = end; continue
        # Escaped punctuation is opaque to delimiter parsing.
        if text[i] == "\\" and i + 1 < len(text) and text[i+1] in _ASCII_PUNCTUATION:
            atom(html.escape(text[i+1])); i += 2; continue
        if text[i] == "`":
            m = _BACKTICK_RUN.match(text, i); n = len(m.group()); close = None
            for c in _BACKTICK_RUN.finditer(text, m.end()):
                if len(c.group()) == n: close = c; break
            if close:
                literal = text[m.end():close.start()].replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
                if literal.startswith(" ") and literal.endswith(" ") and any(x != " " for x in literal): literal = literal[1:-1]
                atom("<code>" + html.escape(decode_escapes_and_entities(literal)) + "</code>")
                i = close.end(); continue
            # An unmatched run is literal as a whole. Do not retry a suffix of
            # the run as a shorter code span opener (e.g. ```foo``).
            chars.append(m.group()); i = m.end(); continue
        auto = _AUTOLINK.match(text, i) if text[i] == "<" else None
        tag = _HTML_TAG.match(text, i) if text[i] == "<" else None
        if auto:
            target = auto.group(1); label = target[7:] if target.startswith("mailto:") else target
            atom(f'<a href="{html.escape(target.replace("`", "%60"), quote=True)}">{html.escape(label)}</a>')
            i = auto.end(); continue
        if tag:
            atom(tag.group()); i = tag.end(); continue
        # Inline links are represented as opaque atoms; their label has its own delimiter stack.
        link = _link_at(text, i, references) if text[i] == "[" else None
        # A code span can begin inside a bracketed sequence and continue
        # through its apparent link syntax. Such backticks bind before links.
        if link and links_allowed:
            end, label, dest, title = link
            # A link already formed inside these brackets disables the outer opener.
            if _has_link(label, references):
                link = None
        if link and links_allowed:
            end, label, dest, title = link
            title_attr = f' title="{html.escape(decode_escapes_and_entities(title), quote=True)}"' if title is not None else ''
            from urllib.parse import quote
            href = quote(decode_escapes_and_entities(dest), safe="/:@-._~!$&'()*+,;=%#?")
            atom(f'<a href="{html.escape(href, quote=True)}"{title_attr}>{render_inline(label, references, False)}</a>')
            i = end; continue
        chars.append(text[i]); i += 1
    rendered = _resolve_emphasis(''.join(chars))
    for n, markup in enumerate(atoms): rendered = rendered.replace(chr(0xE000+n), markup)
    return rendered

def _has_link(text: str, references) -> bool:
    i=0
    while i<len(text):
        if text[i]=='[' and not (i and text[i-1]=='!') and _link_at(text,i,references): return True
        i+=1
    return False
