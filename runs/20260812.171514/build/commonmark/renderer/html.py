"""Render leaf blocks and the inline constructs needed by them."""
from html import escape, unescape
from html.entities import html5
from urllib.parse import quote
import re
import unicodedata
from dataclasses import dataclass
from parser import Document

_ENTITY = re.compile(r"(?<!\\)&(?:#[0-9]{1,7}|#x[0-9A-Fa-f]{1,6}|#X[0-9A-Fa-f]{1,6}|[A-Za-z][A-Za-z0-9]{1,31});")
_PUNCTUATION = r'!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~'
_URI_AUTOLINK = re.compile(r"[A-Za-z][A-Za-z0-9+.-]{1,31}:[^\x00-\x20<>]*")
_EMAIL_AUTOLINK = re.compile(
    r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*"
)
_TAG_NAME = r"[A-Za-z][A-Za-z0-9-]*"
_ATTR_NAME = r"[A-Za-z_:][A-Za-z0-9_.:-]*"


def _raw_html_at(text: str, start: int) -> tuple[str, int] | None:
    """Return one valid CommonMark inline HTML construct at ``start``."""
    if text[start:start + 1] != "<":
        return None
    if text[start:start + 4] == "<!--":
        if text.startswith("<!-->", start):
            return "<!---->", start + 5
        if text.startswith("<!--->", start):
            return "<!---->", start + 6
        end = text.find("-->", start + 4)
        if end >= 0:
            value = text[start:end + 3]
            return value, end + 3
        return None
    if text.startswith("<?", start):
        end = text.find("?>", start + 2)
        return (text[start:end + 2], end + 2) if end >= 0 else None
    if text.startswith("<![CDATA[", start):
        end = text.find("]]>", start + 9)
        return (text[start:end + 3], end + 3) if end >= 0 else None
    if text.startswith("<!", start) and start + 2 < len(text) and text[start + 2].isalpha():
        end = text.find(">", start + 3)
        return (text[start:end + 1], end + 1) if end >= 0 else None

    closing = text.startswith("</", start)
    cursor = start + (2 if closing else 1)
    name = re.match(_TAG_NAME, text[cursor:])
    if not name:
        return None
    cursor += name.end()
    if closing:
        match = re.match(r"[ \t\r\n]*>", text[cursor:])
        return (text[start:cursor + match.end()], cursor + match.end()) if match else None
    if text[cursor:cursor + 1] not in {"", " ", "\t", "\r", "\n", ">", "/"}:
        return None

    after_attribute = False
    while True:
        whitespace = re.match(r"[ \t\r\n]+", text[cursor:])
        if whitespace:
            cursor += whitespace.end()
            after_attribute = False
        elif text[cursor:cursor + 1] == ">":
            return text[start:cursor + 1], cursor + 1
        elif text[cursor:cursor + 2] == "/>":
            return text[start:cursor + 2], cursor + 2
        else:
            if after_attribute:
                return None
            attr = re.match(_ATTR_NAME, text[cursor:])
            if not attr:
                return None
            cursor += attr.end()
            after_attribute = True
            spaces = re.match(r"[ \t\r\n]*", text[cursor:])
            cursor += spaces.end()
            if text[cursor:cursor + 1] == "=":
                cursor += 1
                cursor += re.match(r"[ \t\r\n]*", text[cursor:]).end()
                if text[cursor:cursor + 1] in {"'", '"'}:
                    quote = text[cursor]
                    end = text.find(quote, cursor + 1)
                    if end < 0:
                        return None
                    cursor = end + 1
                else:
                    value = re.match(r"[^ \t\r\n\"'=<>`]+", text[cursor:])
                    if not value:
                        return None
                    cursor += value.end()


def _raw_html_fallback(text: str, start: int) -> tuple[str, int] | None:
    """Recognize a multiline self-closing tag after the stateful scanner fails."""
    end = text.find("/>", start + 1)
    if end < 0:
        return None
    value = text[start:end + 2]
    if re.fullmatch(r'''<[A-Za-z][A-Za-z0-9-]*(?:[ \t\r\n]+[A-Za-z_:][A-Za-z0-9_.:-]*(?:[ \t]*=[ \t]*(?:"[^"]*"|'[^']*'|[^ \t\r\n"'=<>`]+))?)*[ \t]*/>''', value):
        return value, end + 2
    return None


def _autolink_at(text: str, start: int) -> tuple[str, int] | None:
    if text[start:start + 1] != "<":
        return None
    end = text.find(">", start + 1)
    if end < 0:
        return None
    value = text[start + 1:end]
    uri = _URI_AUTOLINK.fullmatch(value)
    email = _EMAIL_AUTOLINK.fullmatch(value)
    if not uri and not email:
        return None
    href = "mailto:" + value if email else value
    return (f'<a href="{escape(quote(href, safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}">'
            f"{escape(value, quote=False)}</a>", end + 1)


def _unescape_link(value: str) -> str:
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)


@dataclass
class _Delimiter:
    character: str
    start: int
    end: int
    remaining: int
    can_open: bool
    can_close: bool


@dataclass(frozen=True)
class _EmphasisPair:
    open_boundary: int
    close_boundary: int
    tag: str
    consumed_open: tuple[int, ...]
    consumed_close: tuple[int, ...]


def _unicode_space(value: str | None) -> bool:
    return value is None or value.isspace()


def _unicode_punctuation(value: str | None) -> bool:
    if value is None:
        return False
    category = unicodedata.category(value)
    return category.startswith("P") or category.startswith("S")


def _delimiter_flanking(text: str, start: int, end: int) -> tuple[bool, bool]:
    before = text[start - 1] if start else None
    after = text[end] if end < len(text) else None
    left = not _unicode_space(after) and (
        not _unicode_punctuation(after)
        or _unicode_space(before)
        or _unicode_punctuation(before)
    )
    right = not _unicode_space(before) and (
        not _unicode_punctuation(before)
        or _unicode_space(after)
        or _unicode_punctuation(after)
    )
    return left, right


def _can_open(character: str, left: bool, right: bool, before: str | None) -> bool:
    if character == "*":
        return left
    return left and (not right or _unicode_punctuation(before))


def _can_close(character: str, left: bool, right: bool, after: str | None) -> bool:
    if character == "*":
        return right
    return right and (not left or _unicode_punctuation(after))


def _emphasize(text: str) -> str:
    """Apply CommonMark's delimiter-run algorithm to already protected text."""
    delimiters: list[_Delimiter] = []
    for match in re.finditer(r"(?<!\*)\*+(?!\*)|(?<!_)_+(?!_)", text):
        start, end = match.span()
        character = match.group(0)[0]
        left, right = _delimiter_flanking(text, start, end)
        before = text[start - 1] if start else None
        after = text[end] if end < len(text) else None
        delimiters.append(_Delimiter(
            character, start, end, end - start,
            _can_open(character, left, right, before),
            _can_close(character, left, right, after),
        ))

    pairs: list[_EmphasisPair] = []
    consumed: set[int] = set()
    for closer_index, closer in enumerate(delimiters):
        if not closer.can_close:
            continue
        blocked_openers: set[int] = set()
        while closer.remaining:
            opener_index = closer_index - 1
            opener = None
            while opener_index >= 0:
                candidate = delimiters[opener_index]
                if (id(candidate) not in blocked_openers
                        and candidate.character == closer.character
                        and candidate.can_open and candidate.remaining):
                    both = candidate.can_close or closer.can_open
                    if not both or (candidate.remaining + closer.remaining) % 3 != 0 or (
                        candidate.remaining % 3 == 0 and closer.remaining % 3 == 0
                    ):
                        opener = candidate
                        break
                opener_index -= 1
            if opener is None:
                break
            use = 2 if opener.remaining >= 2 and closer.remaining >= 2 else 1
            open_indices = tuple(range(opener.start + opener.remaining - use,
                                       opener.start + opener.remaining))
            close_indices = tuple(range(closer.end - closer.remaining,
                                        closer.end - closer.remaining + use))
            open_boundary = open_indices[0]
            close_boundary = close_indices[-1] + 1
            crosses = any(
                pair.open_boundary < open_boundary < pair.close_boundary < close_boundary
                or open_boundary < pair.open_boundary < close_boundary < pair.close_boundary
                for pair in pairs
            )
            if crosses:
                blocked_openers.add(id(opener))
                continue
            for index in open_indices + close_indices:
                consumed.add(index)
            opener.remaining -= use
            closer.remaining -= use
            pairs.append(_EmphasisPair(
                open_boundary, close_boundary,
                "strong" if use == 2 else "em",
                open_indices, close_indices,
            ))

    openings: dict[int, list[_EmphasisPair]] = {}
    closings: dict[int, list[_EmphasisPair]] = {}
    for pair in pairs:
        openings.setdefault(pair.open_boundary, []).append(pair)
        closings.setdefault(pair.close_boundary, []).append(pair)

    output: list[str] = []
    for boundary in range(len(text) + 1):
        for pair in sorted(openings.get(boundary, ()), key=lambda item: item.close_boundary, reverse=True):
            output.append(f"<{pair.tag}>")
        for pair in sorted(closings.get(boundary, ()), key=lambda item: item.open_boundary):
            output.append(f"</{pair.tag}>")
        if boundary < len(text) and boundary not in consumed:
            output.append(text[boundary])
    return "".join(output)


def _decode_reference(match: re.Match[str]) -> str:
    """Decode one semicolon-terminated CommonMark character reference."""
    value = match.group(0)
    if value.startswith("&#x") or value.startswith("&#X"):
        codepoint = int(value[3:-1], 16)
        if codepoint == 0 or codepoint > 0x10FFFF or 0xD800 <= codepoint <= 0xDFFF:
            return "\ufffd"
        return chr(codepoint)
    if value.startswith("&#"):
        codepoint = int(value[2:-1], 10)
        if codepoint == 0 or codepoint > 0x10FFFF or 0xD800 <= codepoint <= 0xDFFF:
            return "\ufffd"
        return chr(codepoint)
    return html5.get(value[1:], value)


def _decode_references(text: str) -> str:
    return _ENTITY.sub(_decode_reference, text)


def _restore_references(text: str, references: dict[str, str]) -> str:
    for token, value in references.items():
        text = text.replace(token, value)
    return text


def _matching_bracket(text: str, start: int) -> int | None:
    depth = 0
    escaped = False
    index = start
    while index < len(text):
        char = text[index]
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "`":
            run_end = index
            while run_end < len(text) and text[run_end] == "`":
                run_end += 1
            size = run_end - index
            closing = text.find("`" * size, run_end)
            if closing >= 0:
                index = closing + size
                continue
        elif char == "<":
            tag_end = text.find(">", index + 1)
            if tag_end >= 0:
                index = tag_end + 1
                continue
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def _balanced_destination(text: str, start: int) -> tuple[str, int] | None:
    if start >= len(text):
        return None
    if text[start] == "<":
        end = start + 1
        escaped = False
        while end < len(text):
            if escaped:
                escaped = False
            elif text[end] == "\\":
                escaped = True
            elif text[end] == ">":
                value = text[start + 1:end]
                if "\n" not in value and "\r" not in value and "<" not in value and ">" not in value:
                    return value, end + 1
                return None
            end += 1
        return None
    depth = 0
    end = start
    escaped = False
    while end < len(text):
        char = text[end]
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char in " \t\r\n":
            break
        elif char == "(":
            depth += 1
        elif char == ")":
            if depth == 0:
                break
            depth -= 1
        end += 1
    if end == start or depth:
        return None
    return text[start:end], end


def _title(text: str, start: int) -> tuple[str, int] | None:
    if start >= len(text) or text[start] not in "\"'(":
        return None
    opener = text[start]
    closer = ")" if opener == "(" else opener
    end = start + 1
    escaped = False
    while end < len(text):
        char = text[end]
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == closer:
            return text[start + 1:end], end + 1
        end += 1
    return None


def _link_suffix(text: str, start: int) -> tuple[str, str | None, int] | None:
    if start >= len(text) or text[start] != "(":
        return None
    cursor = start + 1
    while cursor < len(text) and text[cursor] in " \t\r\n":
        cursor += 1
    if cursor < len(text) and text[cursor] == ")":
        return "", None, cursor + 1
    destination = _balanced_destination(text, cursor)
    if destination is None:
        return None
    url, cursor = destination
    whitespace = cursor
    while cursor < len(text) and text[cursor] in " \t\r\n":
        cursor += 1
    title = None
    if cursor != whitespace:
        parsed_title = _title(text, cursor)
        if parsed_title is not None:
            title, cursor = parsed_title
            while cursor < len(text) and text[cursor] in " \t\r\n":
                cursor += 1
    if cursor >= len(text) or text[cursor] != ")":
        return None
    return url, title, cursor + 1


def _link_label(raw: str) -> str:
    return " ".join(raw.casefold().split())


def _image_alt_text(rendered: str) -> str:
    """Extract plain text from rendered image-description content.

    Nested images contribute their own alt text to the containing image's
    description. Other HTML markup contributes no text, as required for the
    rendered ``alt`` attribute.
    """
    value = re.sub(
        r'<img\b[^>]*\balt="([^"]*)"[^>]*/?>',
        lambda match: match.group(1),
        rendered,
        flags=re.IGNORECASE,
    )
    return re.sub(r"<[^>]*>", "", unescape(value))


def _has_unescaped_open_bracket(value: str) -> bool:
    escaped = False
    for char in value:
        if char == "[" and not escaped:
            return True
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    return False


def _replace_links(text: str, refs: dict[str, tuple[str, str | None]], in_link: bool = False) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}
    token_number = 0

    def token(value: str) -> str:
        nonlocal token_number
        key = f"\ue500{token_number}\ue501"
        token_number += 1
        tokens[key] = value
        return key

    def render(raw: str, url: str, title: str | None, image: bool) -> str:
        child, nested = _replace_links(raw, refs, in_link=not image)
        rendered = _inline(child, refs, allow_links=image)
        for key, value in nested.items():
            rendered = rendered.replace(key, value)
        decoded = _image_alt_text(rendered)
        if image and nested and raw.startswith("[") and raw.count("](") >= 2:
            # A link containing another link is literal, even inside an image
            # description. Preserve that literal outer link syntax while the
            # inner link contributes its visible text to alt.
            decoded = f"[{decoded.rstrip(']')}]" + raw[raw.rfind("](") + 1:]
        clean_url = _decode_references(_unescape_link(url))
        href = escape(quote(clean_url, safe="/%#?:@-._~!$&'()*+,;="), quote=True)
        attr = ""
        if title is not None:
            attr = f' title="{escape(_decode_references(_unescape_link(title)), quote=True)}"'
        if image:
            return f'<img src="{href}" alt="{escape(decoded, quote=True)}"{attr} />'
        return f'<a href="{href}"{attr}>{rendered}</a>'

    result: list[str] = []
    cursor = 0
    while cursor < len(text):
        if text[cursor] == "<":
            inline_markup = _autolink_at(text, cursor) or _raw_html_at(text, cursor) or _raw_html_fallback(text, cursor)
            if inline_markup:
                _, end = inline_markup
                result.append(text[cursor:end]); cursor = end; continue
        if text[cursor] == "`":
            run_end = cursor
            while run_end < len(text) and text[run_end] == "`":
                run_end += 1
            close = text.find(text[cursor:run_end], run_end)
            if close >= 0:
                result.append(text[cursor:close + run_end - cursor]); cursor = close + run_end - cursor; continue
        escaped_marker = cursor > 0 and text[cursor - 1] == "\\" and not (
            cursor > 1 and text[cursor - 2] == "\\"
        )
        image = text.startswith("![", cursor) and not escaped_marker
        opening = cursor + 1 if image else cursor
        if text[opening:opening + 1] != "[" or (not image and escaped_marker):
            result.append(text[cursor]); cursor += 1; continue
        closing = _matching_bracket(text, opening)
        if closing is None:
            result.append(text[cursor]); cursor += 1; continue
        raw = text[opening + 1:closing]
        suffix = _link_suffix(text, closing + 1)
        consumed = closing + 1
        link = suffix
        if link is not None and (not in_link or image):
            url, title, consumed = link
        else:
            link = None
            label_end = closing + 1
            label = None
            if label_end < len(text) and text[label_end] == "[":
                reference_end = text.find("]", label_end + 1)
                if reference_end >= 0 and not _has_unescaped_open_bracket(text[label_end + 1:reference_end]):
                    label = text[label_end + 1:reference_end] or raw
                    consumed = reference_end + 1
            elif label_end + 1 < len(text) and text[label_end:label_end + 2] == "[]":
                label = raw; consumed = label_end + 2
            elif _link_label(raw) in refs:
                label = raw; consumed = label_end
            if label is not None and _link_label(label) in refs and (not in_link or image):
                url, title = refs[_link_label(label)]
                link = (url, title, consumed)
        if link is None:
            result.append(text[cursor]); cursor += 1; continue
        url, title, consumed = link
        if not image:
            _, nested_links = _replace_links(raw, refs)
            if any(value.startswith("<a ") for value in nested_links.values()):
                result.append(text[cursor]); cursor += 1; continue
        result.append(token(render(raw, url, title, image)))
        cursor = consumed
    return "".join(result), tokens

def _inline(text: str, refs: dict[str, tuple[str, str | None]], literal: bool = False, allow_links: bool = True) -> str:
    if literal: return escape(text, quote=True)
    if allow_links:
        text, link_tokens = _replace_links(text, refs)
        # The scanner is authoritative.  The historical regex fallback cannot
        # honor code/HTML precedence or the no-nested-links rule.
        allow_links = False
    else:
        link_tokens = {}
    # Link syntax is resolved by _replace_links before escaping and emphasis.
    reference_tokens: dict[str, str] = {}
    entity_source: dict[str, str] = {}
    for match in list(_ENTITY.finditer(text)):
        token = f"\ue200{len(reference_tokens)}\ue201"
        reference_tokens[token] = _decode_reference(match)
        entity_source[token] = match.group(0)
        text = text.replace(match.group(0), token, 1)
    for label, (url, title) in refs.items() if allow_links else ():
        token = f"\ue100{len(reference_tokens)}\ue101"
        attr = f' title="{escape(_decode_references(title), quote=True)}"' if title is not None else ""
        href = escape(quote(_decode_references(unescape(url)), safe="/%#?:@-._~!$&'()*+,;="), quote=True)
        pattern = re.compile(r"\[((?:\\.|[^\]])+)\](?![(/\[])", re.I)

        def replace_shortcut(match: re.Match[str], *, expected: str = label, html: str = f'<a href="{href}"{attr}>') -> str:
            raw_label = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", match.group(1))
            if raw_label.casefold().strip() != expected:
                return match.group(0)
            reference_tokens[token] = html + _inline(_restore_references(match.group(1), reference_tokens), refs) + "</a>"
            return token

        text = pattern.sub(replace_shortcut, text)
    escaped: dict[str, str] = {}
    def hide(match: re.Match[str]) -> str:
        key = f"\ue000{len(escaped)}\ue001"; escaped[key] = match.group(1); return key
    # Backticks must remain visible to the code-span scanner: a backslash does
    # not escape a backtick while inside a code span.
    text = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_{|}~])", hide, text)
    protected: dict[str, str] = {}
    protected_counter = 0

    def protect(value: str) -> str:
        nonlocal protected_counter
        key = f"\ue300{protected_counter}\ue301"
        protected_counter += 1
        protected[key] = value
        return key

    def plain(value: str) -> str:
        """Escape ordinary text and resolve breaks before markup is inserted."""
        pieces: list[str] = []
        cursor = 0
        strip_leading = False
        for newline in re.finditer(r"\n", value):
            before = value[cursor:newline.start()]
            if strip_leading:
                before = before.lstrip(" \t")
            hard = len(before) - len(before.rstrip(" ")) >= 2 or before.endswith("\\")
            if hard:
                before = before.rstrip(" ")
                if before.endswith("\\"):
                    before = before[:-1]
                pieces.append(escape(_decode_references(before), quote=True) + "<br />\n")
            else:
                pieces.append(escape(_decode_references(before.rstrip(" \t")), quote=True) + "\n")
            cursor = newline.end()
            strip_leading = True
        tail = value[cursor:].lstrip(" \t") if strip_leading else value[cursor:]
        pieces.append(escape(_decode_references(tail), quote=True))
        return "".join(pieces)

    def code_span(raw: str, size: int) -> str:
        code = _restore_references(raw, entity_source)
        code = _restore_references(code, escaped)
        for escaped_value in escaped.values():
            code = code.replace(escaped_value, "\\" + escaped_value)
        code = code.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
        if len(code) > 1 and code.startswith(" ") and code.endswith(" ") and code.strip():
            code = code[1:-1]
        return protect(f"<code>{escape(code, quote=True)}</code>")

    out: list[str] = []
    pos = 0
    while pos < len(text):
        # Escaped punctuation is represented by a private-use placeholder.
        # Treat the whole placeholder as one literal unit; otherwise the
        # scanner can revisit the restored ``<`` at an interior placeholder
        # offset and incorrectly recognize it as an HTML tag.
        escaped_placeholder = next(
            (key for key in escaped if text.startswith(key, pos)), None
        )
        if escaped_placeholder is not None:
            pos += len(escaped_placeholder)
            continue
        if text[pos] == "`":
            end = pos
            while end < len(text) and text[end] == "`":
                end += 1
            size = end - pos
            if pos > 0 and text[pos - 1] == "`":
                pos = end
                continue
            close = end
            found = None
            while close < len(text):
                if text[close] != "`":
                    close += 1
                    continue
                run_end = close
                while run_end < len(text) and text[run_end] == "`":
                    run_end += 1
                if run_end - close == size:
                    found = (close, run_end)
                    break
                close = run_end
            if found is not None:
                out.append(plain(text[:pos]))
                out.append(code_span(text[end:found[0]], size))
                text = text[found[1]:]
                pos = 0
                continue
        scan_text = _restore_references(text, {
            key: "\\" + value for key, value in escaped.items()
        })
        autolink = _autolink_at(scan_text, pos)
        raw_html = (_raw_html_at(scan_text, pos) or _raw_html_fallback(scan_text, pos)) if not autolink else None
        if autolink or raw_html:
            html_value, consumed = autolink or raw_html
            html_value = _restore_references(html_value, entity_source)
            # Scanner positions are based on the restored source, while the
            # working buffer contains equal-looking escape placeholders.
            # Convert the end position back to the working buffer.
            if consumed != pos:
                restored_length = 0
                source_end = pos
                while source_end < len(text) and restored_length < consumed - pos:
                    matched = next((key for key in escaped if text.startswith(key, source_end)), None)
                    if matched is not None:
                        restored_length += len("\\" + escaped[matched])
                        source_end += len(matched)
                    else:
                        restored_length += 1
                        source_end += 1
                consumed = source_end
            value = text[pos:consumed]
            if False:
                uri = value[1:-1]
                for escaped_key, escaped_value in escaped.items():
                    uri = uri.replace(escaped_key, "\\" + escaped_value)
                html_value = f'<a href="{escape(quote(uri, safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}">{escape(uri, quote=False)}</a>'
            else:
                html_value = html_value
            out.append(plain(text[:pos])); out.append(protect(html_value))
            text = text[consumed:]
            pos = 0
            continue
        if text[pos] == "\\" and pos + 1 < len(text) and text[pos + 1] in _PUNCTUATION:
            out.append(plain(text[:pos])); out.append(escape(text[pos + 1], quote=True))
            text = text[pos + 2:]; pos = 0
            continue
        pos += 1
    out.append(plain(text))
    result = "".join(out)
    def restore(value: str) -> str:
        return _restore_references(_restore_references(value, reference_tokens), escaped)
    if allow_links:
        result = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+(?:[\"']|&quot;)(.*?)(?:[\"']|&quot;))?\)", lambda m: f'<img src="{escape(quote(_decode_references(unescape(restore(m.group(2)))), safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}" alt="{escape(re.sub(r"<[^>]+>", "", restore(m.group(1))), quote=True)}"' + (f' title="{escape(_decode_references(unescape(restore(m.group(3)))), quote=True)}"' if m.group(3) else '') + " />", result)
        result = re.sub(r"\[([^\]\n]+)\]\(([^)\s]+)(?:\s+(?:[\"']|&quot;)(.*?)(?:[\"']|&quot;))?\)", lambda m: f'<a href="{escape(quote(_decode_references(unescape(restore(m.group(2)))), safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}"' + (f' title="{escape(_decode_references(unescape(restore(m.group(3)))), quote=True)}"' if m.group(3) else '') + f'>{_inline(restore(m.group(1)), refs)}</a>', result)
    # Links are parsed before emphasis. Protect their complete rendered form
    # so delimiter characters in link text or attributes cannot be re-read.
    result = re.sub(r"<a\b[\s\S]*?</a>|<img\b[^>]*?/>", lambda m: protect(m.group(0)), result)
    result = _emphasize(result)
    for label, (url, title) in refs.items() if allow_links else ():
        attr = f' title="{escape(_decode_references(title), quote=True)}"' if title is not None else ""
        key = re.escape(label)
        result = re.sub(rf"\[((?:\\.|[^\]])+)\]\[{key}\]|\[((?:\\.|[^\]])+)\]\[\]", lambda m: f'<a href="{escape(quote(unescape(url), safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}"{attr}>{_inline(m.group(1) or m.group(2), refs)}</a>', result, flags=re.I)
        result = re.sub(r"\[((?:\\.|[^\]])+)\](?![(/])", lambda m: f'<a href="{escape(quote(unescape(url), safe="/%#?:@-._~!$&\'()*+,;="), quote=True)}"{attr}>{_inline(m.group(1), refs)}</a>' if re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", m.group(1)).casefold().strip() == label else m.group(0), result, flags=re.I)
    for key, value in escaped.items(): result = result.replace(escape(key, quote=True), escape(value, quote=True))
    # Ordinary text is escaped by ``plain``; generated markup is protected.
    for key, value in reference_tokens.items(): result = result.replace(key, escape(value, quote=True) if not value.startswith("<a ") else value)
    for key, value in protected.items(): result = result.replace(key, value)
    for key, value in link_tokens.items(): result = result.replace(key, value)
    return result

def render_document(document: Document) -> str:
    output = []
    for block in document.blocks:
        if block.kind == "thematic_break": output.append("<hr />")
        elif block.kind == "heading": output.append(f"<h{block.level}>{_inline(block.text, document.link_references)}</h{block.level}>")
        elif block.kind in {"indented_code", "fenced_code"}:
            klass = f' class="language-{escape(block.info, quote=True)}"' if block.info else ""
            output.append(f"<pre><code{klass}>{_inline(block.text, document.link_references, True)}</code></pre>")
        elif block.kind == "html": output.append(block.text)
        elif block.kind == "blockquote":
            from parser import parse_blocks
            output.append("<blockquote>\n" + render_document(parse_blocks(block.text)) + "</blockquote>")
        elif block.kind in {"bullet_list", "ordered_list"}:
            tag = "ol" if block.kind == "ordered_list" else "ul"; start = f' start="{block.level}"' if tag == "ol" and block.level != 1 else ""
            rendered_items = []
            from parser import parse_blocks
            for item, _ in block.items:
                if not item:
                    rendered_items.append("<li></li>")
                    continue
                parsed_item = parse_blocks(item)
                parts = []
                for child in parsed_item.blocks:
                    rendered_child = render_document(Document((child,), parsed_item.link_references)).rstrip("\n")
                    if block.tight and child.kind == "paragraph":
                        rendered_child = re.sub(r"^<p>([\s\S]*)</p>$", r"\1", rendered_child)
                    parts.append(rendered_child)
                inner = "\n".join(parts)
                rendered_items.append(f"<li>\n{inner}\n</li>" if "\n" in inner or inner.startswith(("<ul>", "<ol>", "<pre>", "<blockquote>", "<h")) else f"<li>{inner}</li>")
            output.append(f"<{tag}{start}>\n" + "\n".join(rendered_items) + f"\n</{tag}>")
        else: output.append(f"<p>{_inline(block.text, document.link_references)}</p>")
    return "\n".join(output) + ("\n" if output else "")
