"""Block-structure boundary; inline syntax is intentionally not handled here."""

from dataclasses import dataclass, field
import re

from normalization import expand_indentation, indentation_columns
from references import ReferenceCollector, parse_definition


@dataclass(frozen=True)
class Block:
    kind: str
    content: str = ""
    level: int | None = None
    children: tuple["Block", ...] = ()


@dataclass(frozen=True)
class SourceLine:
    raw: str
    structural: str


LIST_RE = re.compile(r"^( {0,3})([*+-]|[0-9]{1,9}[.)])([ \t]*)(.*)$")
HEADING_RE = re.compile(r"^( {0,3})(#{1,6})(?:[ \t]+(.*)|[ \t]*)$")
FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})([^\n]*)$")
SETEXT_RE = re.compile(r"^ {0,3}(=+|-+)[ \t]*$")
BLOCK_TAGS = ("address|article|aside|base|basefont|blockquote|body|caption|center|col|"
              "colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|"
              "footer|form|frame|frameset|h1|h2|h3|h4|h5|h6|head|header|hr|html|"
              "iframe|legend|li|link|main|menu|menuitem|nav|noframes|ol|optgroup|"
              "option|p|param|search|section|summary|table|tbody|td|tfoot|th|thead|"
              "title|tr|track|ul")
HTML_BLOCK_RE = re.compile(r"^ {0,3}</?(?:" + BLOCK_TAGS + r")(?:[ \t]|/?>|$)", re.I)
HTML_TAG_RE = re.compile(r"^ {0,3}</?[A-Za-z][^<>]*>[ \t]*$")


@dataclass(frozen=True)
class Document:
    blocks: tuple[Block, ...]
    references: ReferenceCollector = field(compare=False)


def parse_blocks(text: str) -> Document:
    """Build the initial block tree; inline parsing happens after this phase."""
    lines = [SourceLine(line, expand_indentation(line)) for line in text.split("\n")]
    blocks: list[Block] = []
    references = ReferenceCollector()
    paragraph: list[str] = []

    def emit_code(raw_lines: list[SourceLine]) -> None:
        content = [remove_indent(line.raw, 4) for line in raw_lines]
        blocks.append(Block("code", "\n".join(content) + "\n"))

    def parse_simple(lines_to_parse: list[SourceLine]) -> list[Block]:
        result: list[Block] = []
        index = 0
        while index < len(lines_to_parse):
            line = lines_to_parse[index]
            if not line.structural.strip():
                index += 1
                continue
            definition = parse_definition([x.raw for x in lines_to_parse], index)
            if definition is not None:
                end, label, destination, title = definition
                references.add(label, destination, title)
                index = end
                continue
            fence = FENCE_RE.match(line.structural)
            if fence and (fence.group(2)[0] == "~" or "`" not in fence.group(3)):
                marker, info = fence.group(2), fence.group(3).strip(" \t")
                body: list[str] = []
                index += 1
                while index < len(lines_to_parse):
                    candidate = lines_to_parse[index]
                    close = re.match(r"^ {0,3}" + re.escape(marker[0]) + r"{" + str(len(marker)) + r",}[ \t]*$", candidate.structural)
                    if close:
                        index += 1
                        break
                    if index == len(lines_to_parse) - 1 and candidate.raw == "":
                        index += 1
                        break
                    body.append(remove_indent(candidate.raw, len(fence.group(1))))
                    index += 1
                language = info.split()[0] if info else ""
                result.append(Block("fence", "\n".join(body) + ("\n" if body else ""), children=(Block("info", language),)))
                continue
            html_kind = html_block_kind(line.structural)
            if html_kind:
                raw = [line.raw]
                index += 1
                end_re = html_kind[1]
                if end_re and end_re.search(line.raw):
                    result.append(Block("html", "\n".join(raw)))
                    continue
                while index < len(lines_to_parse):
                    candidate = lines_to_parse[index]
                    if (html_kind[0] in {"blank", "tag7"} and not candidate.structural.strip()) or (end_re and end_re.search(candidate.raw)):
                        if end_re:
                            raw.append(candidate.raw)
                            index += 1
                        break
                    raw.append(candidate.raw)
                    index += 1
                result.append(Block("html", "\n".join(raw)))
                continue
            heading = HEADING_RE.match(line.structural)
            if heading:
                content = (heading.group(3) or "").strip(" \t")
                content = re.sub(r"(?<!\\)[ \t]+#+[ \t]*$", "", content)
                if re.fullmatch(r"(?<!\\)#+", content):
                    content = ""
                result.append(Block("heading", content, len(heading.group(2))))
                index += 1
                continue
            if is_thematic_break(line.structural):
                result.append(Block("hr"))
                index += 1
                continue
            if line.structural.startswith(">") and len(line.structural) <= 3 + len(line.structural.lstrip(">")):
                quote_lines: list[SourceLine] = []
                while index < len(lines_to_parse):
                    candidate = lines_to_parse[index]
                    if not candidate.structural.lstrip(" ").startswith(">"):
                        if SETEXT_RE.match(candidate.structural) and not re.match(r"^ {0,3}-+[ \t]*$", candidate.structural):
                            quote_lines.append(SourceLine(candidate.raw, candidate.structural + "x"))
                            index += 1
                            continue
                        if (candidate.structural.strip() and not is_thematic_break(candidate.structural)
                                and not LIST_RE.match(candidate.structural)
                                and not HEADING_RE.match(candidate.structural)):
                            quote_lines.append(SourceLine(candidate.raw, candidate.structural))
                            index += 1
                            continue
                        break
                    trimmed = candidate.structural.lstrip(" ")
                    rest = trimmed[1:]
                    original_rest = candidate.raw[candidate.raw.index(">") + 1:]
                    if original_rest.startswith("\t"):
                        # The first column after `>` is the optional marker
                        # space; the second tab contributes two remaining
                        # structural spaces inside the quote.
                        rest = "      " + rest.lstrip(" \t")
                    elif rest.startswith(" "):
                        rest = rest[1:]
                    quote_lines.append(SourceLine(rest, rest))
                    index += 1
                result.append(Block("blockquote", children=tuple(parse_simple(quote_lines))))
                continue
            marker = LIST_RE.match(line.structural) if not is_thematic_break(line.structural) else None
            if marker and not valid_list_match(marker):
                marker = None
            if marker and len(marker.group(1)) <= 3:
                items: list[Block] = []
                list_loose = False
                kind = "ordered" if marker.group(2)[0].isdigit() else "bullet"
                delimiter = marker.group(2)[-1] if kind == "ordered" else marker.group(2)
                start = int(marker.group(2)[:-1]) if kind == "ordered" else None
                while index < len(lines_to_parse):
                    if is_thematic_break(lines_to_parse[index].structural):
                        break
                    current = LIST_RE.match(lines_to_parse[index].structural)
                    if current and not valid_list_match(current):
                        current = None
                    if not current or len(current.group(1)) > 3:
                        break
                    current_kind = "ordered" if current.group(2)[0].isdigit() else "bullet"
                    current_delim = current.group(2)[-1] if current_kind == "ordered" else current.group(2)
                    if current_kind != kind or current_delim != delimiter:
                        break
                    body = [SourceLine(current.group(4), current.group(4))]
                    current_indent = len(current.group(1))
                    gap = len(expand_indentation(current.group(3)))
                    index += 1
                    while index < len(lines_to_parse):
                        nxt = lines_to_parse[index]
                        nxt_match = LIST_RE.match(nxt.structural)
                        if nxt_match and valid_list_match(nxt_match) and len(nxt_match.group(1)) <= current_indent:
                            break
                        if is_thematic_break(nxt.structural):
                            break
                        if not nxt.structural.strip():
                            if any(future.structural.strip() for future in lines_to_parse[index + 1:]):
                                list_loose = True
                            body.append(SourceLine("", ""))
                            index += 1
                            continue
                        body.append(SourceLine(nxt.raw, nxt.structural))
                        index += 1
                    # Remove the list item's content indentation.  A tab in
                    # the source is interpreted structurally, then preserved
                    # when it is part of code/text content.
                    indent = len(current.group(1)) + len(current.group(2)) + (1 if gap > 1 else max(1, gap))
                    normalized_body = [
                        (SourceLine(current.group(4), current.group(4)) if offset == 0 else
                         SourceLine(remove_indent(x.raw, indent), remove_indent(x.structural, indent)))
                        for offset, x in enumerate(body)
                    ]
                    items.append(Block("list_item", children=tuple(parse_simple(normalized_body))))
                attrs = str(start) if start is not None else ""
                result.append(Block(kind, attrs, level=1 if list_loose else 0, children=tuple(items)))
                continue
            if line.structural.startswith("    "):
                code_lines = [line]
                index += 1
                while index < len(lines_to_parse) and (not lines_to_parse[index].structural.strip() or lines_to_parse[index].structural.startswith("    ")):
                    code_lines.append(lines_to_parse[index])
                    index += 1
                while code_lines and not code_lines[-1].structural.strip():
                    code_lines.pop()
                result.append(Block("code", "\n".join(remove_indent(x.raw, 4) for x in code_lines) + "\n"))
                continue
            # A setext underline converts the immediately preceding paragraph
            # lines into one heading; detect it before starting a paragraph.
            setext_end = index + 1
            made_setext = False
            while setext_end < len(lines_to_parse) and lines_to_parse[setext_end].structural.strip():
                if SETEXT_RE.match(lines_to_parse[setext_end].structural):
                    content = "\n".join(x.raw.strip(" \t") for x in lines_to_parse[index:setext_end]).strip(" \t")
                    level = 1 if lines_to_parse[setext_end].structural.lstrip().startswith("=") else 2
                    result.append(Block("heading", content, level))
                    index = setext_end + 1
                    made_setext = True
                    break
                if (HEADING_RE.match(lines_to_parse[setext_end].structural) or
                    is_thematic_break(lines_to_parse[setext_end].structural) or
                    FENCE_RE.match(lines_to_parse[setext_end].structural)):
                    break
                setext_end += 1
            if made_setext:
                continue
            paragraph_lines = [line.raw.lstrip(" \t")]
            index += 1
            while index < len(lines_to_parse) and lines_to_parse[index].structural.strip():
                nxt = lines_to_parse[index]
                html_candidate = html_block_kind(nxt.structural)
                if (HEADING_RE.match(nxt.structural) or is_thematic_break(nxt.structural) or
                    (LIST_RE.match(nxt.structural) and valid_list_match(LIST_RE.match(nxt.structural))) or FENCE_RE.match(nxt.structural) or
                    (html_candidate and html_candidate[0] != "tag7") or nxt.structural.startswith(">")):
                    break
                paragraph_lines.append(nxt.raw.strip(" \t"))
                index += 1
            result.append(Block("paragraph", "\n".join(paragraph_lines)))
        return result

    parsed = _collect_references(parse_simple(lines), references)
    return Document(tuple(parsed), references)


def _collect_references(blocks: list[Block], references: ReferenceCollector) -> list[Block]:
    result: list[Block] = []
    for block in blocks:
        if block.children:
            block = Block(block.kind, block.content, block.level,
                          tuple(_collect_references(list(block.children), references)))
        if block.kind != "paragraph":
            result.append(block)
            continue
        lines = block.content.split("\n")
        index = 0
        while index < len(lines):
            parsed = parse_definition(lines, index)
            if parsed is None:
                break
            end, label, destination, title = parsed
            references.add(label, destination, title)
            index = end
        remaining = lines[index:]
        if remaining and any(line.strip() for line in remaining):
            result.append(Block("paragraph", "\n".join(remaining)))
    return result


def remove_indent(line: str, columns: int) -> str:
    prefix_end = 0
    while prefix_end < len(line) and line[prefix_end] in " \t":
        prefix_end += 1
    if prefix_end == 0:
        return line
    prefix = expand_indentation(line[:prefix_end])
    if len(prefix) <= columns:
        return line[prefix_end:]
    return prefix[columns:] + line[prefix_end:]


def is_thematic_break(line: str) -> bool:
    if len(line) - len(line.lstrip(" ")) > 3:
        return False
    stripped = line.strip(" \t")
    chars = stripped.replace(" ", "").replace("\t", "")
    return len(chars) >= 3 and len(set(chars)) == 1 and chars[0] in "*-_"


def valid_list_match(match: re.Match[str]) -> bool:
    """A marker needs whitespace before content, unless it is empty."""
    return not (match.group(3) == "" and match.group(4) != "")


def html_block_kind(line: str) -> tuple[str, re.Pattern[str] | None] | None:
    if len(line) - len(line.lstrip(" ")) > 3:
        return None
    text = line.lstrip(" ")
    for tag in ("pre", "script", "style", "textarea"):
        if re.match(r"<" + tag + r"(?:[ \t]|>|$)", text, re.I):
            return ("tag", re.compile(r"</" + tag + r"\s*>", re.I))
    if text.startswith("<!--"):
        return ("tag", re.compile(r"-->") )
    if text.startswith("<?"):
        return ("tag", re.compile(r"\?>"))
    if re.match(r"<![A-Za-z]", text):
        return ("tag", re.compile(r">"))
    if text.startswith("<![CDATA["):
        return ("tag", re.compile(r"\]\]>"))
    if HTML_BLOCK_RE.match(line):
        return ("blank", None)
    if HTML_TAG_RE.match(line):
        return ("tag7", None)
    return None
