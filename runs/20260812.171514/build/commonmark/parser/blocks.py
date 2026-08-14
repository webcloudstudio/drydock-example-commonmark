"""Deterministic CommonMark leaf-block parsing."""
from dataclasses import dataclass
import re
from html.entities import html5

@dataclass(frozen=True)
class Block:
    kind: str
    text: str = ""
    level: int = 0
    info: str = ""
    items: tuple[tuple[str, bool], ...] = ()
    tight: bool = True

@dataclass(frozen=True)
class Document:
    blocks: tuple[Block, ...]
    link_references: dict[str, tuple[str, str | None]]

_FENCE = re.compile(r"^( {0,3})(`{3,}|~{3,})([^\r\n]*)$")
_ATX = re.compile(r"^( {0,3})(#{1,6})(?:[ \t]+(.*?)\s*|[ \t]*)$")
_REF = re.compile(r"^ {0,3}\[((?:\\.|[^\]])+)\]:[ \t]*(?:<([^>\r\n]*)>|([^<\s][^\s]*))(?:[ \t]+(?:\"((?:\\.|[^\"\\])*)\"|'((?:\\.|[^'\\])*)'|\(((?:\\.|[^)\\])*)\)))?[ \t]*$")


def _expand_structural_indent(line: str) -> str:
    """Expand tabs used before block content, retaining tabs in text."""
    column = 0
    index = 0
    while index < len(line) and line[index] in " \t":
        if line[index] == "\t":
            width = 4 - (column % 4)
            column += width
        else:
            column += 1
        index += 1
    return " " * column + line[index:]


def _indent_width(text: str, start: int = 0) -> int:
    column = start
    for character in text:
        if character == "\t":
            column += 4 - (column % 4)
        else:
            column += 1
    return column - start


def _quote_content(line: str) -> str:
    match = re.match(r"^( {0,3})>(.*)$", line)
    if not match:
        return line
    indent, remainder = match.groups()
    if remainder.startswith(" "):
        return remainder[1:]
    if remainder.startswith("\t"):
        width = _indent_width(remainder[: len(remainder) - len(remainder.lstrip(" \t"))], len(indent) + 1)
        leading = remainder[: len(remainder) - len(remainder.lstrip(" \t"))]
        return " " * (width - 1) + remainder[len(leading):]
    return remainder

def _thematic(line: str) -> bool:
    s = line.lstrip(" ")
    if len(line) - len(s) > 3 or not s: return False
    s = s.rstrip(" \t")
    chars = s.replace(" ", "").replace("\t", "")
    return bool(chars) and chars[0] in "-_ *" and chars[0] != " " and len(chars) >= 3 and all(c == chars[0] for c in chars)

def _label(label: str) -> str:
    return " ".join(label.casefold().split())

def _unescape(value: str) -> str:
    return re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", value)

def _decode_info(value: str) -> str:
    def replace(match: re.Match[str]) -> str:
        token = match.group(0)
        if token.startswith("&#x") or token.startswith("&#X"):
            return chr(int(token[3:-1], 16))
        if token.startswith("&#"):
            return chr(int(token[2:-1], 10))
        return html5.get(token[1:], token)
    return re.sub(r"&(?:#[0-9]{1,7}|#x[0-9A-Fa-f]{1,6}|#X[0-9A-Fa-f]{1,6}|[A-Za-z][A-Za-z0-9]{1,31});", replace, value)


def _quote_lazy_continuation(line: str, inner: list[str]) -> bool:
    """Return whether an unmarked line can lazily continue a quote paragraph."""
    if not inner or not inner[-1].strip():
        return False
    if re.match(r"^ {0,3}(?:`{3,}|~{3,})", inner[-1]):
        return False
    if re.match(r"^ {0,3}>", line):
        return False
    if _thematic(line):
        return False
    if re.match(r"^ {0,3}(?:`{3,}|~{3,})[^`\n]*$", line):
        return False
    if re.match(r"^ {0,3}#{1,6}(?:[ \t]|$)", line):
        return False
    if re.match(r"^ {0,3}(?:[-+*](?:[ \t]|$)|\d{1,9}[.)](?:[ \t]|$))", line):
        return False
    if re.match(r"^ {0,3}</?(?:address|article|aside|base|blockquote|body|div|h[1-6]|head|header|hr|html|li|main|nav|ol|p|section|table|td|th|title|tr|ul)(?:[ \t]|>|/>)", line, re.I):
        return False
    # Four spaces can only be lazy text when they could not begin an
    # indented code block in the quote's current paragraph.  A list marker
    # at that indentation is the CommonMark example of this case.
    if len(line) - len(line.lstrip(" ")) >= 4:
        return bool(re.match(r"^ {4}(?:[-+*](?:[ \t]|$)|\d{1,9}[.)](?:[ \t]|$))", line))
    return True

def parse_blocks(markdown: str) -> Document:
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if lines and lines[-1] == "": lines.pop()
    source_lines = lines[:]
    lines = [_expand_structural_indent(line) for line in lines]
    blocks: list[Block] = []; refs: dict[str, tuple[str, str | None]] = {}; paragraph: list[str] = []; i = 0
    def flush() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(Block("paragraph", "\n".join(x.lstrip(" \t") if n == 0 else x for n, x in enumerate(paragraph)).rstrip(" \t"))); paragraph = []
    while i < len(lines):
        line = lines[i]
        if not line.strip(): flush(); i += 1; continue
        if re.match(r"^ {0,3}>", line):
            flush(); inner = []
            raw_quote = []
            while i < len(lines):
                if re.match(r"^ {0,3}>", lines[i]):
                    raw_quote.append(lines[i]); inner.append(_expand_structural_indent(_quote_content(lines[i]))); i += 1
                    continue
                if not lines[i].strip() or not _quote_lazy_continuation(lines[i], inner):
                    break
                raw_quote.append(lines[i]); inner.append(re.sub(r"^ {0,3}>[ \t]?", "", lines[i])); i += 1
            for n, raw in enumerate(raw_quote):
                if not re.match(r"^ {0,3}>", raw) and re.match(r"^ {0,3}(=+|-+)[ \t]*$", inner[n]):
                    inner[n] = "\\" + inner[n].lstrip()
            nested = parse_blocks("\n".join(inner)); refs.update(nested.link_references); blocks.append(Block("blockquote", "\n".join(inner))); continue
        # A setext underline has precedence over a thematic break when it
        # follows paragraph text.
        if paragraph and re.match(r"^ {0,3}(=+|-+)[ \t]*$", line):
            blocks.append(Block("heading", "\n".join(paragraph).strip(" \t"), 1 if line.lstrip().startswith("=") else 2)); paragraph = []; i += 1; continue
        if _thematic(line): flush(); blocks.append(Block("thematic_break")); i += 1; continue
        list_match = re.match(r"^( {0,3})([-+*])([ \t]+|$)(.*)$", line) or re.match(r"^( {0,3})(\d{1,9})([.)])([ \t]+|$)(.*)$", line)
        list_content = (list_match.group(5) if list_match.group(2).isdigit() else list_match.group(4)) if list_match else ""
        if list_match and (not paragraph or (list_content.strip() and (list_match.group(2).isdigit() and list_match.group(2) == "1" or not list_match.group(2).isdigit()))):
            if paragraph:
                flush()
            ordered = list_match.group(2).isdigit()
            delimiter = list_match.group(3) if ordered else list_match.group(2)
            first_number = int(list_match.group(2)) if ordered else 1
            items: list[tuple[str, bool]] = []
            while i < len(lines):
                current = (re.match(r"^( {0,3})([-+*])([ \t]+|$)(.*)$", lines[i]) if not ordered
                           else re.match(r"^( {0,3})(\d{1,9})" + re.escape(delimiter) + r"([ \t]+|$)(.*)$", lines[i]))
                if not current or (not ordered and current.group(2) != delimiter) or (not ordered and _thematic(lines[i]) and current.group(2) != "-"):
                    break
                indent = len(current.group(1)); marker_width = len(current.group(2)) + (1 if ordered else 0)
                gap = current.group(3)
                gap_width = min(_indent_width(gap, indent + marker_width), 4) if gap else 1
                body_indent = indent + marker_width + gap_width
                body = [" " * max(0, _indent_width(gap, indent + marker_width) - 1) + current.group(4)]; i += 1; had_blank = False; separated = False; blank_outer = False
                while i < len(lines):
                    next_item = re.match(r"^( {0,3})([-+*]|\d{1,9}[.)])([ \t]+|$)(.*)$", lines[i])
                    if next_item and len(next_item.group(1)) < body_indent:
                        separated = had_blank
                        break
                    raw = lines[i]
                    if not raw.strip():
                        if not body[0].strip():
                            had_blank = True; i += 1; continue
                        had_blank = True; body.append("")
                    elif not raw.startswith((" ", "\t")) and _thematic(raw):
                        break
                    elif not body[0].strip() and had_blank:
                        break
                    elif body[0].startswith("    ") and had_blank:
                        body.append(raw[3:])
                    elif raw.expandtabs(4).startswith(" " * body_indent):
                        body.append(raw[body_indent:])
                    elif len(raw) - len(raw.lstrip(" ")) >= 4 and re.match(r"^ *(?:[-+*]|\d{1,9}[.)])(?:[ \t]|$)", raw):
                        if re.match(r"^ *\d{1,9}[.)](?:[ \t]|$)", raw):
                            break
                        body.append("\\" + raw.lstrip(" "))
                    elif had_blank and len(raw) - len(raw.lstrip(" \t")) < body_indent:
                        if body[0].startswith("    "):
                            body.append(raw[3:])
                        else:
                            break
                    elif raw.startswith((" ", "\t")):
                        body.append(raw.lstrip(" \t"))
                    else:
                        body.append(raw)
                    i += 1
                while body and not body[-1].strip(): body.pop()
                text = "\n".join(body)
                direct = parse_blocks(text).blocks if text else ()
                nested_lists = [b for b in direct if b.kind in {"bullet_list", "ordered_list"}]
                body_lines = text.splitlines()
                first_blank = next((n for n, value in enumerate(body_lines) if not value.strip()), len(body_lines))
                first_nested = next((n for n, value in enumerate(body_lines) if re.match(r"^[-+*] |^\d{1,9}[.)] ", value)), len(body_lines))
                direct_loose = had_blank and len(direct) > 1 and (
                    not nested_lists
                    or direct[-1].kind == "paragraph"
                    or (any(nested.tight for nested in nested_lists) and first_blank < first_nested)
                )
                code_only = len(direct) == 1 and direct[0].kind in {"fenced_code", "indented_code"}
                has_list = any(b.kind in {"bullet_list", "ordered_list"} for b in direct)
                separated = separated and (not has_list or bool(re.match(r"^(?:[-+*]|\d{1,9}[.)])(?:[ \t]|$)", text.splitlines()[-1] if text else "")))
                items.append((text, direct_loose or (separated and not code_only)))
            blocks.append(Block("ordered_list" if ordered else "bullet_list", level=first_number, items=tuple(items), tight=not any(x[1] for x in items))); continue
        fence = _FENCE.match(line)
        if fence:
            flush(); indent, marker, rest = fence.groups(); info = rest.strip()
            if marker[0] == "`" and "`" in info: paragraph.append(line); i += 1; continue
            content: list[str] = []; i += 1
            while i < len(lines):
                if re.match(r"^ {0,3}" + re.escape(marker[0]) + r"{" + str(len(marker)) + r",}[ \t]*$", lines[i]): i += 1; break
                raw = source_lines[i]
                if indent:
                    raw = raw[min(len(indent), len(raw) - len(raw.lstrip(" "))):]
                content.append(raw); i += 1
            blocks.append(Block("fenced_code", "\n".join(content) + ("\n" if content else ""), info=_unescape(_decode_info(info.split()[0])) if info else "")); continue
        if paragraph and (re.match(r"^ {4}", line) or line.startswith("\t")):
            paragraph.append(line[4:] if line.startswith("    ") else line[1:] if line.startswith("\t") else line); i += 1; continue
        if re.match(r"^ {4}", line) or line.startswith("\t"):
            flush(); content = []
            while i < len(lines) and (not lines[i].strip() or re.match(r"^ {4}", lines[i]) or lines[i].startswith("\t")):
                content.append(lines[i][4:] if lines[i].startswith("    ") else lines[i][1:] if lines[i].startswith("\t") else ""); i += 1
            while content and not content[-1]: content.pop()
            blocks.append(Block("indented_code", "\n".join(content) + "\n")); continue
        atx = _ATX.match(line)
        if atx:
            flush(); text = (atx.group(3) or "").strip(" \t"); text = re.sub(r"(?:^|[ \t])+#+[ \t]*$", "", text).strip(" \t")
            blocks.append(Block("heading", text, len(atx.group(2)))); i += 1; continue
        if paragraph and re.match(r"^ {0,3}(=+|-+)[ \t]*$", line):
            marker = line.strip(); blocks.append(Block("heading", "\n".join(paragraph).strip(" \t"), 1 if marker[0] == "=" else 2)); paragraph = []; i += 1; continue
        ref = _REF.match(line)
        loose_ref = re.match(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*$", line)
        if not paragraph and line.startswith("[") and "]:" not in line and "]" not in line:
            j = i
            label_lines = []
            while j < len(lines) and "]:" not in lines[j] and j < i + 10:
                label_lines.append(lines[j].strip()); j += 1
            if j < len(lines) and "]:" in lines[j]:
                prefix, rest = lines[j].split("]:", 1)
                label = " ".join(label_lines + [prefix]).strip()
                candidate = "[" + label.lstrip("[").strip() + "]:" + rest
                candidate_match = _REF.match(candidate)
                if candidate_match and not re.search(r"(?<!\\)\[", candidate_match.group(1)):
                    destination = candidate_match.group(2) if candidate_match.group(2) is not None else candidate_match.group(3) or ""
                    title = next((candidate_match.group(x) for x in (4, 5, 6) if candidate_match.group(x) is not None), None)
                    refs.setdefault(_label(candidate_match.group(1)), (_unescape(destination), _unescape(title) if title is not None else None)); i = j + 1; continue
        multiline_title = re.match(r"^ {0,3}\[((?:\\.|[^\]])+)\]:[ \t]*(<[^>]*>|[^<\s][^\s]*)[ \t]+([\"'])((?:.*))$", line)
        if not paragraph and multiline_title and multiline_title.group(3) not in multiline_title.group(4):
            quote_char = multiline_title.group(3)
            title_parts = [multiline_title.group(4)]
            cursor = i + 1
            closed = False
            while cursor < len(lines):
                # A blank line terminates a reference definition; the
                # title cannot span it. Leave the lines for normal parsing.
                if not lines[cursor].strip():
                    break
                title_parts.append(lines[cursor])
                if quote_char in lines[cursor]:
                    closed = True
                    cursor += 1
                    break
                cursor += 1
            if closed:
                destination = multiline_title.group(2).strip("<>")
                refs.setdefault(_label(multiline_title.group(1)), (_unescape(destination), _unescape("\n".join(title_parts).rsplit(quote_char, 1)[0])))
                i = cursor
                continue
        nested_title = re.match(r"^ {0,3}\[((?:\\.|[^\]])+)\]:[ \t]*(<[^>]*>|[^<\s][^\s]*)[ \t]+(['\"])(.*)\3[ \t]*$", line)
        if not paragraph and nested_title:
            destination = nested_title.group(2).strip("<>")
            refs.setdefault(_label(nested_title.group(1)), (_unescape(destination), _unescape(nested_title.group(4)))); i += 1; continue
        continued_title = re.match(r"^ {0,3}\[((?:\\.|[^\]])+)\]:[ \t]*(<[^>]*>|[^<\s][^\s]*)[ \t]*$", line)
        if not paragraph and continued_title and i + 1 < len(lines):
            tm = re.match(r"^[ \t]*(['\"])(.*)\1[ \t]*$", lines[i + 1])
            if tm:
                refs.setdefault(_label(continued_title.group(1)), (_unescape(continued_title.group(2).strip("<>")), _unescape(tm.group(2)))); i += 2; continue
        if loose_ref and not paragraph and i + 1 < len(lines):
            destination_line = lines[i + 1].strip()
            destination_match = re.match(r"(?:<([^>]+)>|([^\s]+))(?:[ \t]+(?:\"([^\"]*)\"|'([^']*)'|\(([^)]*)\)))?$", destination_line)
            if destination_match:
                destination = destination_match.group(1) if destination_match.group(1) is not None else destination_match.group(2) or ""
                title = next((destination_match.group(x) for x in (3, 4, 5) if destination_match.group(x) is not None), None)
                consumed = 2
                if title is None and i + 2 < len(lines):
                    title_match = re.match(r"^[ \t]*(?:\"([^\"]*)\"|'([^']*)'|\(([^)]*)\))[ \t]*$", lines[i + 2])
                    if title_match: title = next((title_match.group(x) for x in (1, 2, 3) if title_match.group(x) is not None), None); consumed = 3
                refs.setdefault(_label(loose_ref.group(1)), (destination, title)); i += consumed; continue
        if ref and not paragraph and not re.search(r"(?<!\\)\[", ref.group(1)):
            destination = ref.group(2) if ref.group(2) is not None else ref.group(3) or ""
            title = next((ref.group(x) for x in (4, 5, 6) if ref.group(x) is not None), None)
            refs.setdefault(_label(ref.group(1)), (_unescape(destination), _unescape(title) if title is not None else None)); i += 1; continue
        if i + 1 < len(lines) and re.match(r"^ {0,3}(=+|-+)[ \t]*$", lines[i + 1]) and line.strip() and not paragraph and not line.lstrip().startswith((">", "- ", "* ", "+ ")):
            blocks.append(Block("heading", line.strip(" \t"), 1 if "=" in lines[i + 1] else 2)); i += 2; continue
        stripped = line.lstrip()
        html_start = re.match(r"<(?:pre|script|style|textarea)(?:\s|>|$)|<!--|<\?|<!\[CDATA\[|<![A-Za-z]|</?(?:address|article|aside|base|blockquote|body|div|h[1-6]|head|header|hr|html|li|main|nav|ol|p|section|table|td|th|title|tr|ul)(?:\s|>|/>)", stripped, re.I)
        complete_tag = re.match(
            r'''</?[A-Za-z][A-Za-z0-9-]*(?:[ \t]+[A-Za-z_:][A-Za-z0-9_.:-]*(?:[ \t]*=[ \t]*(?:"[^"]*"|'[^']*'|[^ \t\r\n"'=<>`]+))?)*[ \t]*/?>\s*$''',
            stripped,
        ) if "://" not in stripped else None
        if stripped.startswith("</") and not re.match(r"</[A-Za-z][A-Za-z0-9-]*[ \t]*>", stripped):
            complete_tag = None
        partial_tag = bool(
            complete_tag is None
            and ">" not in stripped
            and re.match(
                r"</?(?:address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem|nav|noframes|ol|optgroup|option|p|param|search|section|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul)\b",
                stripped,
                re.I,
            )
        )
        if len(line) - len(stripped) <= 3 and (html_start or (complete_tag and not paragraph) or partial_tag):
            flush(); content = [line]; i += 1
            if partial_tag:
                while i < len(lines) and lines[i].strip():
                    content.append(lines[i]); i += 1
                blocks.append(Block("html", "\n".join(content))); continue
            if html_start and re.match(r"<(?:pre|script|style|textarea)", stripped, re.I):
                tag = re.match(r"<\s*(pre|script|style|textarea)", stripped, re.I).group(1)
                while i < len(lines) and not re.search(r"</" + tag + r"\s*>", "\n".join(content), re.I): content.append(lines[i]); i += 1
                if i < len(lines) and not re.search(r"</" + tag + r"\s*>", "\n".join(content), re.I): content.append(lines[i]); i += 1
            elif stripped.startswith("<!--") and "-->" in stripped:
                pass
            elif (stripped.startswith("<!--") and "-->" not in stripped) or stripped.startswith("<?") or stripped.startswith("<![CDATA[") or re.match(r"<![A-Za-z]", stripped):
                end = "-->" if stripped.startswith("<!--") else "?>" if stripped.startswith("<?") else "]] >".replace(" ", "") if stripped.startswith("<![CDATA[") else ">"
                while i < len(lines) and end not in "\n".join(content): content.append(lines[i]); i += 1
            else:
                while i < len(lines) and lines[i].strip(): content.append(lines[i]); i += 1
            blocks.append(Block("html", "\n".join(content))); continue
        paragraph.append(line); i += 1
    flush(); return Document(tuple(blocks), refs)
