"""Block parsing boundary for the CommonMark pipeline."""

from dataclasses import dataclass, field
import re
from .fenced_code import parse_fenced_code
from .html_blocks import parse_html_block
from .indented_code import parse_indented_code
from .references import extract_definitions
from .setext import parse_setext
from .indented_code import _strip_columns


@dataclass
class Block:
    """A minimal block node retaining source for later inline parsing."""

    kind: str
    children: list["Block"] = field(default_factory=list)
    literal: str = ""
    level: int | None = None
    info: str = ""
    ordered: bool = False
    start: int = 1
    tight: bool = True

    @property
    def type(self) -> str:
        """Compatibility name for the block node's kind."""
        return self.kind


@dataclass
class Document:
    """Ordered block tree and document-wide reference definitions."""

    children: list[Block] = field(default_factory=list)
    references: dict[str, object] = field(default_factory=dict)


def _thematic(line: str) -> bool:
    match = re.fullmatch(r" {0,3}([*_\-])(?:[ \t]*\1){2,}[ \t]*", line)
    return bool(match)


def _atx(line: str):
    match = re.match(r"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*$)", line)
    if not match:
        return None
    content = match.group(2) or ""
    if re.fullmatch(r"#+[ \t]*", content):
        content = ""
    content = re.sub(r"[ \t]+#+[ \t]*$", "", content).strip(" \t")
    return len(match.group(1)), content


def _quote_content(line: str) -> tuple[str, bool] | None:
    """Return quote content and whether the marked line is blank."""
    indent = len(line) - len(line.lstrip(" "))
    if indent > 3 or indent >= len(line) or line[indent] != ">":
        return None
    content = line[indent + 1:]
    # A single following space is part of the marker. A tab advances to the
    # next four-column stop; consume one column for the marker and retain the
    # remaining columns so indented code sees the original indentation.
    if content.startswith(" "):
        content = content[1:]
    elif content.startswith("\t"):
        # The tab begins one column after the marker, so it occupies three
        # columns in the source. The marker consumes one; remaining tabs keep
        # their original four-column stops, represented as spaces here.
        rest = content[1:]
        if rest.startswith("\t"):
            rest = "    " + rest[1:]
        content = "  " + rest.expandtabs(4)
    return content, not content.strip(" \t")


_LIST_MARKER = re.compile(r"^( {0,3})([-+*]|([0-9]{1,9})([.)]))([ \t]+|$)(.*)$")


def _list_marker(line: str):
    match = _LIST_MARKER.match(line)
    if not match:
        return None
    indent, marker, digits, delimiter, whitespace, rest = match.groups()
    if marker in "-*+" and _thematic(line):
        return None
    if marker in "*+" and re.fullmatch(r" {0,3}[ *_-](?:[ \t]*[ *_-]){2,}[ \t]*", line):
        return None
    ordered = digits is not None
    start = int(digits) if ordered else 1
    if ordered and start > 999999999:
        return None
    width = len(indent) + len(marker)
    # The marker starts after ``indent`` columns. Tab stops are measured from
    # the beginning of the original line, so expanding the whitespace alone
    # from column zero overcounts tabs after a list marker.
    marker_column = len(indent) + len(marker)
    pad = 0
    for char in whitespace:
        pad += 4 - (marker_column + pad) % 4 if char == "\t" else 1
    if rest and pad > 4:
        rest = " " * (pad - 1) + rest
        pad = 1
    else:
        pad = max(1, pad)
    if not rest.strip(" \t"):
        pad = 1
    return (len(indent), marker if not ordered else delimiter, ordered, start, width + pad, rest, bool(rest.strip(" \t")))


def parse_blocks(markdown: str) -> Document:
    """Parse supported block structures, retaining inline source where needed."""
    document = Document()
    paragraph: list[str] = []

    def finish_paragraph() -> None:
        if not paragraph:
            return
        # Continuation indentation is structural, while trailing whitespace on
        # those lines remains available to the inline parser (for hard breaks).
        lines = [paragraph[0].lstrip(" \t")]
        lines.extend(line.lstrip(" \t") for line in paragraph[1:])
        literal = "\n".join(lines).rstrip(" \t")
        literal = extract_definitions(literal + "\n", document.references).rstrip("\n")
        if literal:
            document.children.append(Block(kind="paragraph", literal=literal))
        paragraph.clear()

    lines = markdown.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        quote_line = _quote_content(line)
        if quote_line:
            finish_paragraph()
            quote_lines: list[str] = []
            has_paragraph = False
            lazy_setext_line: str | None = None
            while i < len(lines):
                marked = _quote_content(lines[i])
                if marked:
                    content, blank = marked
                    quote_lines.append(content)
                    # Lazy continuation is only valid after an open paragraph.
                    # A code block opener or an indented code line closes that
                    # paragraph even though the marked line itself is nonblank.
                    has_paragraph = bool(content.strip(" \t")) and not (
                        parse_fenced_code([content]) is not None
                        or (len(content) - len(content.lstrip(" ")) >= 4)
                    )
                    i += 1
                    continue
                # Blank lines without a marker close the quote. Missing quote
                # markers are lazy only while a paragraph is open.
                if not lines[i].strip(" \t"):
                    break
                if not has_paragraph:
                    break
                if _thematic(lines[i]) or _atx(lines[i]) or _list_marker(lines[i]) or parse_fenced_code(lines[i:]) or parse_html_block(lines[i:]):
                    break
                if quote_lines and parse_setext([quote_lines[-1], lines[i]]):
                    lazy_setext_line = lines[i]
                quote_lines.append(lines[i])
                i += 1
            child_doc = parse_blocks("\n".join(quote_lines))
            if lazy_setext_line is not None and child_doc.children and child_doc.children[-1].kind == "heading":
                heading = child_doc.children[-1]
                child_doc.children[-1] = Block(kind="paragraph", literal=heading.literal + "\n" + lazy_setext_line)
            document.references.update(child_doc.references)
            document.children.append(Block(kind="block_quote", children=child_doc.children))
            continue
        if not line.strip(" \t"):
            finish_paragraph()
            i += 1
            continue
        marker = _list_marker(line)
        if marker:
            indent, marker_type, ordered, start, content_column, rest, nonempty = marker
            # Lists may interrupt paragraphs only with a nonempty item; ordered
            # lists that interrupt must begin at one.
            if paragraph and (not nonempty or (ordered and start != 1)):
                paragraph.append(line)
                i += 1
                continue
            finish_paragraph()
            items: list[Block] = []
            list_loose = False
            while i < len(lines):
                current = _list_marker(lines[i])
                if not current or current[1] != marker_type or current[2] != ordered:
                    break
                item_indent, _, _, _, item_column, item_rest, _ = current
                item_lines = [item_rest]
                i += 1
                saw_blank = False
                blank_before_nested = False
                while i < len(lines):
                    nxt = _list_marker(lines[i])
                    if nxt and nxt[1] == marker_type and nxt[2] == ordered and nxt[0] < item_column:
                        break
                    if not lines[i].strip(" \t"):
                        # A blank line only belongs to the item when the next
                        # block is sufficiently indented or another sibling
                        # item. Otherwise it separates the list from following
                        # document content and must not loosen the list.
                        look = i + 1
                        while look < len(lines) and not lines[look].strip(" \t"):
                            look += 1
                        next_marker = _list_marker(lines[look]) if look < len(lines) else None
                        if not item_rest.strip(" \t"):
                            if next_marker and next_marker[1] == marker_type and next_marker[2] == ordered and next_marker[0] < item_column:
                                list_loose = True
                                saw_blank = True
                                item_lines.append("")
                                i += 1
                                continue
                            break
                        if next_marker and next_marker[1] == marker_type and next_marker[2] == ordered and next_marker[0] < item_column:
                            list_loose = True
                            saw_blank = True
                            item_lines.append("")
                            i += 1
                            continue
                        next_leading = 0
                        if look < len(lines):
                            for char in lines[look]:
                                if char == " ": next_leading += 1
                                elif char == "\t": next_leading += 4 - next_leading % 4
                                else: break
                        if look < len(lines) and next_leading >= item_column:
                            nested_line, _ = _strip_columns(lines[look], item_column)
                            blank_before_nested = _list_marker(nested_line) is not None
                        if look < len(lines) and next_leading >= item_column:
                            saw_blank = True
                            item_lines.append("")
                            i += 1
                            continue
                        break
                    leading = 0
                    for char in lines[i]:
                        if char == " ":
                            leading += 1
                        elif char == "\t":
                            leading += 4 - leading % 4
                        else:
                            break
                    if leading >= item_column:
                        continuation, _ = _strip_columns(lines[i], item_column)
                        item_lines.append(continuation)
                        i += 1
                        continue
                    if saw_blank:
                        break
                    # Lazy continuation is allowed only for an open paragraph.
                    if not item_lines or not item_lines[-1].strip(" \t"):
                        break
                    if _thematic(lines[i]) or _atx(lines[i]) or _list_marker(lines[i]) or parse_fenced_code(lines[i:]) or parse_html_block(lines[i:]):
                        break
                    item_lines.append(lines[i])
                    i += 1
                item_doc = parse_blocks("\n".join(item_lines).strip("\n"))
                document.references.update(item_doc.references)
                has_nested_list = any(child.kind == "list" for child in item_doc.children)
                paragraph_after_nested = any(
                    child.kind == "paragraph" for child in item_doc.children[
                        next((index + 1 for index, child in enumerate(item_doc.children) if child.kind == "list"), len(item_doc.children)):
                    ]
                )
                # A blank line before a nested list makes the containing list
                # loose, even when the blank is followed by no sibling block
                # at the item's own level.
                if saw_blank and (
                    not item_doc.children
                    # A blank line before a nested list belongs to that
                    # nested structure. It does not make this item's opening
                    # paragraph loose; only a blank between sibling blocks
                    # at the item's own level does.
                    or (
                        any(child.kind == "paragraph" for child in item_doc.children)
                        and (not has_nested_list or paragraph_after_nested or blank_before_nested)
                    )
                ):
                    list_loose = True
                items.append(Block(kind="item", children=item_doc.children))
            document.children.append(Block(kind="list", children=items, ordered=ordered, start=start, tight=not list_loose))
            continue
        setext = parse_setext([*paragraph, line]) if paragraph else None
        if setext and paragraph:
            # Remove complete definitions before resolving setext precedence.
            retained = extract_definitions("\n".join(paragraph) + "\n", document.references)
            if retained != "\n".join(paragraph) + "\n":
                paragraph[:] = retained.splitlines()
                setext = parse_setext([*paragraph, line]) if paragraph else None
        if setext:
            level, literal = setext
            paragraph.clear()
            document.children.append(Block(kind="heading", level=level, literal=literal))
            i += 1
            continue
        fenced = parse_fenced_code(lines[i:])
        html = parse_html_block(lines[i:], paragraph_open=bool(paragraph))
        heading = _atx(line)
        if fenced:
            finish_paragraph()
            content, info, consumed = fenced
            document.children.append(Block(kind="fenced_code", literal=content, info=info))
            i += consumed
        elif _thematic(line):
            finish_paragraph()
            document.children.append(Block(kind="thematic_break"))
            i += 1
        elif heading:
            finish_paragraph()
            level, content = heading
            document.children.append(Block(kind="heading", level=level, literal=content))
            i += 1
        elif html:
            finish_paragraph()
            raw, consumed = html
            document.children.append(Block(kind="html_block", literal=raw))
            i += consumed
        else:
            code = parse_indented_code(lines[i:], paragraph_open=bool(paragraph))
            if code:
                finish_paragraph()
                content, consumed = code
                document.children.append(Block(kind="indented_code", literal=content))
                i += consumed
            else:
                paragraph.append(line)
                i += 1
    finish_paragraph()
    return document
