"""Phase 1: block tree, block-type registry, per-line procedure, and lazy continuation.

Responsibility: consume lines one at a time, match them against open blocks, look for new block
starts, and add remaining text to the deepest open block. Link reference definitions are handed to
`mdparser.refs` when a paragraph closes.

Each block type is a `BlockType` record registered in a `BlockRegistry`. A type supplies a start
rule, a continue rule and a close (finalize) rule; the per-line loop in `DocumentParser` never
names a concrete type.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass

from mdparser.entities import unescape_and_decode
from mdparser.refs import ReferenceMap, extract_definitions

TAB_STOP = 4
SPACE_CHARS = " \t"

# A start rule inspects the rest of the line below `container`. It returns a new block, after
# advancing the cursor past its marker, or None, leaving the cursor untouched.
StartRule = Callable[["Cursor", "Block"], "Block | None"]
# A continue rule decides whether the line continues an open block. It advances the cursor only
# when it returns True.
ContinueRule = Callable[["Block", "Cursor"], bool]
# An add-line rule appends the remaining line text to a leaf block that accepts lines.
AddLineRule = Callable[["Block", "Cursor"], None]
# A finalize rule runs once when a block closes, for example to set its content.
FinalizeRule = Callable[["Block"], None]


def next_column(char: str, col: int) -> int:
    """Return the column after `char`, which sits at column `col`. Tabs advance to the next tab stop."""
    if char == "\t":
        return col + TAB_STOP - col % TAB_STOP
    return col + 1


def indent_columns(line: str, pos: int, col: int) -> int:
    """Return the width in columns of the spaces and tabs starting at `pos`, which sits at `col`."""
    end = pos
    end_col = col
    while end < len(line) and line[end] in SPACE_CHARS:
        end_col = next_column(line[end], end_col)
        end += 1
    return end_col - col


class Cursor:
    """A position in one source line, tracked both as a character index and as a column."""

    def __init__(self, line: str) -> None:
        self.line = line
        self.pos = 0
        self.col = 0
        # True when a container has consumed only part of the tab at `pos`. The columns left in the tab
        # are content indentation, so `rest` gives them as spaces.
        self.in_tab = False
        # True when the line can only join the open paragraph as a lazy continuation. A start rule that
        # cannot interrupt a paragraph then leaves the line alone.
        self.lazy_paragraph = False

    @property
    def rest(self) -> str:
        """The text from the current position to the end of the line.

        When a tab is partly consumed, its remaining columns come first, as spaces.
        """
        if self.in_tab:
            remaining = next_column(self.line[self.pos], self.col) - self.col
            return " " * remaining + self.line[self.pos + 1 :]
        return self.line[self.pos :]

    @property
    def indent(self) -> int:
        """Columns of indentation from the current position to the next non-space character."""
        return indent_columns(self.line, self.pos, self.col)

    def next_nonspace(self) -> int:
        """Index of the first character at or after the current position that is not a space or tab."""
        end = self.pos
        while end < len(self.line) and self.line[end] in SPACE_CHARS:
            end += 1
        return end

    def is_blank(self) -> bool:
        """True when only spaces and tabs remain on the line."""
        return self.next_nonspace() == len(self.line)

    def advance_to(self, index: int) -> None:
        """Move the cursor forward to character `index`, tracking the column."""
        while self.pos < index:
            self.col = next_column(self.line[self.pos], self.col)
            self.pos += 1
            self.in_tab = False

    def advance_nonspace(self) -> None:
        """Skip spaces and tabs up to the next non-space character."""
        self.advance_to(self.next_nonspace())

    def advance_columns(self, columns: int) -> None:
        """Consume spaces and tabs until `columns` columns are passed.

        A tab that straddles the target column is consumed whole, so the column may overshoot.
        """
        target = self.col + columns
        while self.pos < len(self.line) and self.col < target and self.line[self.pos] in SPACE_CHARS:
            self.col = next_column(self.line[self.pos], self.col)
            self.pos += 1
            self.in_tab = False

    def consume_columns(self, columns: int) -> None:
        """Consume spaces and tabs until `columns` columns are passed, without overshooting.

        A tab that straddles the target column is split: the cursor stops inside it, and the columns it
        has left are read back through `rest` as spaces.
        """
        target = self.col + columns
        while self.pos < len(self.line) and self.col < target and self.line[self.pos] in SPACE_CHARS:
            end_col = next_column(self.line[self.pos], self.col)
            if end_col > target:
                self.col = target
                self.in_tab = True
                return
            self.col = end_col
            self.pos += 1
            self.in_tab = False


class Block:
    """A node in the block tree. Leaf blocks keep their raw lines; `content` is set when they close."""

    def __init__(self, kind: BlockType) -> None:
        self.kind = kind
        self.parent: Block | None = None
        self.children: list[Block] = []
        self.is_open = True
        self.lines: list[str] = []
        self.content = ""
        # Heading level, 1 to 6, for an ATX heading. Zero for every other block.
        self.level = 0
        # The document-wide reference map. Only the document root holds one.
        self.references: ReferenceMap | None = None
        # The opening fence and its state, for a fenced code block. None for every other block.
        self.fence: Fence | None = None
        # The start condition and end state of an HTML block. None for every other block.
        self.html: HtmlState | None = None
        # The marker and content column of a list item. None for every other block.
        self.item: ListItem | None = None
        # True when the last line that reached this block was blank. List looseness reads it.
        self.last_line_blank = False

    def open_last_child(self) -> Block | None:
        """The last child if it is still open, otherwise None."""
        if self.children and self.children[-1].is_open:
            return self.children[-1]
        return None


@dataclass(frozen=True)
class BlockType:
    """The rules that define one kind of block.

    `accepts_lines` marks a leaf that takes line text. `interruptible` lets a start rule close such
    a leaf (a paragraph); a non-interruptible leaf blocks new starts. `lazy` lets a non-matching
    line join this block as a lazy continuation. `is_container` lets the block hold child blocks.
    """

    name: str
    continues: ContinueRule
    is_container: bool = False
    accepts_lines: bool = False
    interruptible: bool = False
    lazy: bool = False
    start: StartRule | None = None
    add_line: AddLineRule | None = None
    finalize: FinalizeRule | None = None

    def __post_init__(self) -> None:
        if self.accepts_lines and self.add_line is None:
            raise ValueError(f"block type {self.name!r} accepts lines but has no add_line rule")
        if self.lazy and not self.accepts_lines:
            raise ValueError(f"block type {self.name!r} is lazy but does not accept lines")


def _always_continues(block: Block, cursor: Cursor) -> bool:
    return True


def _paragraph_continues(block: Block, cursor: Cursor) -> bool:
    return not cursor.is_blank()


def _paragraph_add_line(block: Block, cursor: Cursor) -> None:
    cursor.advance_nonspace()
    block.lines.append(cursor.rest)


def _paragraph_finalize(block: Block) -> None:
    """Move leading link reference definitions into the document map and keep the remaining text.

    A paragraph that holds only definitions leaves the tree.
    """
    text = "\n".join(block.lines).strip(" \t")
    block.content = extract_definitions(text, _document_references(block))
    if not block.content and block.parent is not None:
        block.parent.children.remove(block)


def _document_references(block: Block) -> ReferenceMap:
    """The reference map of the document root that `block` belongs to."""
    root = block
    while root.parent is not None:
        root = root.parent
    assert root.references is not None
    return root.references


def _never_continues(block: Block, cursor: Cursor) -> bool:
    return False


THEMATIC_BREAK_MARKERS = "*-_"
THEMATIC_BREAK_MIN_MARKERS = 3


def _thematic_break_start(cursor: Cursor, container: Block) -> Block | None:
    """Start a thematic break when the rest of the line is three or more matching marker characters.

    Spaces and tabs may appear between and after the markers. Any other character, or four or more
    columns of indentation, means the line is not a thematic break.
    """
    if cursor.indent >= 4:
        return None
    start = cursor.next_nonspace()
    line = cursor.line
    if start == len(line) or line[start] not in THEMATIC_BREAK_MARKERS:
        return None
    marker = line[start]
    count = 0
    for char in line[start:]:
        if char == marker:
            count += 1
        elif char not in SPACE_CHARS:
            return None
    if count < THEMATIC_BREAK_MIN_MARKERS:
        return None
    cursor.advance_to(len(line))
    return Block(THEMATIC_BREAK)


ATX_MARKER = "#"
ATX_MAX_LEVEL = 6


def _atx_heading_start(cursor: Cursor, container: Block) -> Block | None:
    """Start an ATX heading when the line opens with one to six `#` characters.

    The opening run must be followed by a space, a tab or the end of the line. The content is the
    rest of the line, stripped of surrounding spaces and tabs, without a closing sequence.
    """
    if cursor.indent >= 4:
        return None
    line = cursor.line
    start = cursor.next_nonspace()
    end = start
    while end < len(line) and line[end] == ATX_MARKER:
        end += 1
    level = end - start
    if not 1 <= level <= ATX_MAX_LEVEL:
        return None
    if end < len(line) and line[end] not in SPACE_CHARS:
        return None
    cursor.advance_to(len(line))
    heading = Block(ATX_HEADING)
    heading.level = level
    heading.content = _strip_closing_sequence(line[end:].strip(SPACE_CHARS))
    return heading


def _strip_closing_sequence(content: str) -> str:
    """Remove a closing run of `#` characters from the end of heading content.

    The run must be the whole content or follow a space or tab. So `foo#` keeps its hash, and so
    does `foo \\#`, where the backslash is not whitespace.
    """
    stripped = content.rstrip(ATX_MARKER)
    if stripped == content:
        return content
    if stripped == "" or stripped[-1] in SPACE_CHARS:
        return stripped.rstrip(SPACE_CHARS)
    return content


SETEXT_MAX_INDENT = 3
SETEXT_LEVELS = {"=": 1, "-": 2}


def _setext_heading_start(cursor: Cursor, container: Block) -> Block | None:
    """Turn the open paragraph into a setext heading when the line is an underline of `=` or `-`.

    The underline has up to three spaces of indentation, one run of a single marker character and
    only trailing spaces or tabs after it. It applies to the whole paragraph, so every paragraph line
    becomes heading content. Definitions at the start of the paragraph are extracted first; if nothing
    is left, the line is not an underline and the paragraph keeps it as text.
    """
    if container.kind is not PARAGRAPH or cursor.indent > SETEXT_MAX_INDENT:
        return None
    line = cursor.line
    start = cursor.next_nonspace()
    marker = line[start : start + 1]
    if marker not in SETEXT_LEVELS:
        return None
    underline = line[start:].rstrip(SPACE_CHARS)
    if underline.count(marker) != len(underline):
        return None
    text = "\n".join(container.lines).strip(SPACE_CHARS)
    content = extract_definitions(text, _document_references(container))
    if not content:
        return None
    cursor.advance_to(len(line))
    # The paragraph's text now lives in the heading. Clearing its lines lets the paragraph close
    # empty, so it leaves the tree and the heading takes its place.
    container.lines = []
    heading = Block(SETEXT_HEADING)
    heading.level = SETEXT_LEVELS[marker]
    heading.content = content
    return heading


DOCUMENT = BlockType("document", continues=_always_continues, is_container=True)
PARAGRAPH = BlockType(
    "paragraph",
    continues=_paragraph_continues,
    accepts_lines=True,
    interruptible=True,
    lazy=True,
    add_line=_paragraph_add_line,
    finalize=_paragraph_finalize,
)
# A setext heading is a complete block made from the open paragraph. Its content is parsed as inlines
# when the document is rendered, like an ATX heading.
SETEXT_HEADING = BlockType(
    "setext_heading",
    continues=_never_continues,
    start=_setext_heading_start,
)
# A thematic break is a complete single-line block. It never takes continuation lines, so it closes
# as soon as the next line arrives.
THEMATIC_BREAK = BlockType(
    "thematic_break",
    continues=_never_continues,
    start=_thematic_break_start,
)
# An ATX heading is a complete single-line block, like a thematic break. Its content is parsed as
# inlines when the document is rendered.
ATX_HEADING = BlockType(
    "atx_heading",
    continues=_never_continues,
    start=_atx_heading_start,
)


CODE_INDENT = 4


def _indented_code_start(cursor: Cursor, container: Block) -> Block | None:
    """Start an indented code block when a non-blank line is indented four columns or more.

    A leaf that takes lines as the container means the line would continue an open paragraph, and
    an indented code block cannot interrupt one, so the line is left to that paragraph. The same holds
    for a lazy continuation of a paragraph that an unmatched container holds.
    """
    if container.kind.accepts_lines or cursor.lazy_paragraph or cursor.is_blank():
        return None
    if cursor.indent < CODE_INDENT:
        return None
    cursor.consume_columns(CODE_INDENT)
    return Block(INDENTED_CODE)


def _indented_code_continues(block: Block, cursor: Cursor) -> bool:
    """A blank line or a line indented four columns or more continues the code block.

    The four columns of indentation are consumed here, so the add-line rule receives the content.
    """
    if cursor.is_blank() or cursor.indent >= CODE_INDENT:
        cursor.consume_columns(CODE_INDENT)
        return True
    return False


def _indented_code_add_line(block: Block, cursor: Cursor) -> None:
    """Keep the literal rest of the line, including any indentation beyond the four columns."""
    block.lines.append(cursor.rest)


def _indented_code_finalize(block: Block) -> None:
    """Drop trailing blank lines and join the rest, each with a line ending, as the content."""
    lines = list(block.lines)
    while lines and not lines[-1].strip(SPACE_CHARS):
        lines.pop()
    block.content = "".join(line + "\n" for line in lines)


# An indented code block is a leaf that takes lines. It is not interruptible, so no start rule runs
# while it is open: a non-blank line that is not indented closes it through the continue rule.
INDENTED_CODE = BlockType(
    "indented_code",
    continues=_indented_code_continues,
    accepts_lines=True,
    start=_indented_code_start,
    add_line=_indented_code_add_line,
    finalize=_indented_code_finalize,
)


FENCE_CHARS = "`~"
FENCE_MIN_LENGTH = 3
BACKTICK = "`"


@dataclass
class Fence:
    """The opening fence of a fenced code block, and the state it keeps while the block is open.

    `indent` is the columns of indentation on the opening fence; up to that many are removed from
    each content line. `language` is the first word of the decoded info string. `opening` is True
    until the opening line reaches the add-line rule, which skips it. `closed` is set when a closing
    fence matches; the closing line adds nothing and the block closes on the following line.
    """

    char: str
    length: int
    indent: int
    language: str
    opening: bool = True
    closed: bool = False


def _run_end(line: str, start: int, char: str) -> int:
    """Index just past the run of `char` that begins at `start`."""
    end = start
    while end < len(line) and line[end] == char:
        end += 1
    return end


def _language(info: str) -> str:
    """The first word of the info string after backslash unescape and entity decoding, or ""."""
    words = unescape_and_decode(info).split()
    return words[0] if words else ""


def _fenced_code_start(cursor: Cursor, container: Block) -> Block | None:
    """Start a fenced code block when the line opens with three or more backticks or tildes.

    The fence may be indented up to three columns. The info string is the rest of the line, trimmed.
    A backtick fence whose info string holds a backtick is not a fence, so the line is left to the
    paragraph, where the backticks form a code span.
    """
    if cursor.indent >= CODE_INDENT:
        return None
    line = cursor.line
    start = cursor.next_nonspace()
    if start == len(line) or line[start] not in FENCE_CHARS:
        return None
    char = line[start]
    end = _run_end(line, start, char)
    if end - start < FENCE_MIN_LENGTH:
        return None
    info = line[end:].strip(SPACE_CHARS)
    if char == BACKTICK and BACKTICK in info:
        return None
    fence = Fence(char=char, length=end - start, indent=cursor.indent, language=_language(info))
    cursor.advance_to(len(line))
    block = Block(FENCED_CODE)
    block.fence = fence
    return block


def _is_closing_fence(cursor: Cursor, fence: Fence) -> bool:
    """True when the line is a closing fence for `fence`.

    It uses the same character, is at least as long as the opening fence, is indented up to three
    columns, and is followed only by spaces or tabs.
    """
    if cursor.indent >= CODE_INDENT:
        return False
    line = cursor.line
    start = cursor.next_nonspace()
    end = _run_end(line, start, fence.char)
    return end - start >= fence.length and not line[end:].strip(SPACE_CHARS)


def _fenced_code_continues(block: Block, cursor: Cursor) -> bool:
    """Every line continues the block except one after a closing fence.

    A matching closing fence is consumed here and marked. Any other line loses up to the opening
    fence's indentation, and the rest reaches the add-line rule.
    """
    fence = block.fence
    assert fence is not None
    if fence.closed:
        return False
    if _is_closing_fence(cursor, fence):
        fence.closed = True
        cursor.advance_to(len(cursor.line))
        return True
    cursor.advance_columns(fence.indent)
    return True


def _fenced_code_add_line(block: Block, cursor: Cursor) -> None:
    """Keep the literal rest of a content line. The opening and closing fence lines add nothing."""
    fence = block.fence
    assert fence is not None
    if fence.opening:
        fence.opening = False
        return
    if fence.closed:
        return
    block.lines.append(cursor.rest)


def _fenced_code_finalize(block: Block) -> None:
    """Join the content lines, each with a line ending, as the content.

    An unclosed block keeps every line up to the end of its container.
    """
    block.content = "".join(line + "\n" for line in block.lines)


# A fenced code block is a leaf that takes lines. It is not interruptible, so no start rule runs
# while it is open. It can interrupt a paragraph, because its start rule is tried in the paragraph's
# container.
FENCED_CODE = BlockType(
    "fenced_code",
    continues=_fenced_code_continues,
    accepts_lines=True,
    start=_fenced_code_start,
    add_line=_fenced_code_add_line,
    finalize=_fenced_code_finalize,
)


HTML_TAG_NAME = r"[A-Za-z][A-Za-z0-9\-]*"
HTML_ATTRIBUTE = (
    r"[ \t]+[A-Za-z_:][A-Za-z0-9_.:\-]*"
    r"(?:[ \t]*=[ \t]*(?:[^\"'=<>`\x00-\x20]+|'[^']*'|\"[^\"]*\"))?"
)
# A complete open tag or closing tag, with its name captured, as the raw HTML grammar defines it. Only
# spaces and tabs may follow it on the line.
COMPLETE_OPEN_TAG = re.compile(rf"<({HTML_TAG_NAME})(?:{HTML_ATTRIBUTE})*[ \t]*/?>[ \t]*")
COMPLETE_CLOSE_TAG = re.compile(rf"</({HTML_TAG_NAME})[ \t]*>[ \t]*")
# Start condition 1 names. Type 7 excludes them, because type 1 owns them.
RAW_TEXT_TAG_NAMES = frozenset(("pre", "script", "style", "textarea"))
RAW_TEXT_START = re.compile(r"<(?:pre|script|style|textarea)(?=[ \t>]|$)", re.IGNORECASE)
RAW_TEXT_END = re.compile(r"</(?:pre|script|style|textarea)>", re.IGNORECASE)
# Start condition 6 names, matched case-insensitively.
BLOCK_TAG_NAMES = (
    "address", "article", "aside", "base", "basefont", "blockquote", "body", "caption", "center",
    "col", "colgroup", "dd", "details", "dialog", "dir", "div", "dl", "dt", "fieldset", "figcaption",
    "figure", "footer", "form", "frame", "frameset", "h1", "h2", "h3", "h4", "h5", "h6", "head",
    "header", "hr", "html", "iframe", "legend", "li", "link", "main", "menu", "menuitem", "nav",
    "noframes", "ol", "optgroup", "option", "p", "param", "search", "section", "summary", "table",
    "tbody", "td", "tfoot", "th", "thead", "title", "tr", "track", "ul",
)
BLOCK_TAG_START = re.compile(
    rf"</?(?:{'|'.join(BLOCK_TAG_NAMES)})(?=[ \t]|/?>|$)", re.IGNORECASE
)
DECLARATION_START = re.compile(r"<![A-Za-z]")


HtmlStart = Callable[[str], bool]
HtmlEnd = Callable[[str], bool]


def _prefix_test(pattern: re.Pattern[str]) -> HtmlStart:
    """A start test that holds when `pattern` matches at the start of the line text."""
    return lambda text: pattern.match(text) is not None


def _search_test(pattern: re.Pattern[str]) -> HtmlEnd:
    """An end test that holds when `pattern` matches anywhere in the line text."""
    return lambda text: pattern.search(text) is not None


def _contains_test(marker: str) -> HtmlEnd:
    """An end test that holds when `marker` appears anywhere in the line text."""
    return lambda text: marker in text


def _is_complete_tag_line(text: str) -> bool:
    """True when the line text is one complete open or closing tag, then spaces and tabs only.

    The tag name may not be `pre`, `script`, `style` or `textarea`.
    """
    match = COMPLETE_OPEN_TAG.fullmatch(text) or COMPLETE_CLOSE_TAG.fullmatch(text)
    if match is None:
        return False
    return match.group(1).lower() not in RAW_TEXT_TAG_NAMES


@dataclass(frozen=True)
class HtmlKind:
    """One of the seven HTML block types, given by its start test and end test.

    `ends` is the end test for types 1 to 5, which is checked on each line. It is None for types 6
    and 7, which end before a blank line. `can_interrupt` is False only for type 7, which cannot
    start while a paragraph is open.
    """

    starts: HtmlStart
    ends: HtmlEnd | None
    can_interrupt: bool = True


# The seven HTML block types, in spec order. A line starts the first type whose start test holds.
HTML_KINDS = (
    HtmlKind(starts=_prefix_test(RAW_TEXT_START), ends=_search_test(RAW_TEXT_END)),
    HtmlKind(starts=_prefix_test(re.compile(r"<!--")), ends=_contains_test("-->")),
    HtmlKind(starts=_prefix_test(re.compile(r"<\?")), ends=_contains_test("?>")),
    HtmlKind(starts=_prefix_test(DECLARATION_START), ends=_contains_test(">")),
    HtmlKind(starts=_prefix_test(re.compile(r"<!\[CDATA\[")), ends=_contains_test("]]>")),
    HtmlKind(starts=_prefix_test(BLOCK_TAG_START), ends=None),
    HtmlKind(starts=_is_complete_tag_line, ends=None, can_interrupt=False),
)


@dataclass
class HtmlState:
    """The start condition of an HTML block, and whether its end condition has been met.

    `ended` is set when a line meets the end test of types 1 to 5. The block closes on the line after
    that line, so the line holding the end condition is kept.
    """

    kind: HtmlKind
    ended: bool = False


def _html_block_start(cursor: Cursor, container: Block) -> Block | None:
    """Start an HTML block when the line opens with one of the seven start conditions.

    The line may be indented up to three columns. Type 7 cannot start while a paragraph is open, which
    is the case when the container takes lines or the line lazily continues the open paragraph.
    """
    if cursor.indent >= CODE_INDENT:
        return None
    text = cursor.rest.lstrip(SPACE_CHARS)
    for kind in HTML_KINDS:
        if not kind.can_interrupt and (container.kind.accepts_lines or cursor.lazy_paragraph):
            continue
        if kind.starts(text):
            block = Block(HTML_BLOCK)
            block.html = HtmlState(kind=kind)
            return block
    return None


def _html_block_continues(block: Block, cursor: Cursor) -> bool:
    """Types 1 to 5 continue until their end line. Types 6 and 7 continue until a blank line."""
    state = block.html
    assert state is not None
    if state.kind.ends is not None:
        return not state.ended
    return not cursor.is_blank()


def _html_block_add_line(block: Block, cursor: Cursor) -> None:
    """Keep the whole line, unchanged and unescaped, and note when it meets the end condition."""
    state = block.html
    assert state is not None
    line = cursor.rest
    block.lines.append(line)
    if state.kind.ends is not None and state.kind.ends(line):
        state.ended = True


def _html_block_finalize(block: Block) -> None:
    """Join the raw lines, each with a line ending, as the content."""
    block.content = "".join(line + "\n" for line in block.lines)


# An HTML block is a leaf that takes lines. It is not interruptible, so no start rule runs while it is
# open. It can interrupt a paragraph, except for type 7, which the start rule refuses in that case.
HTML_BLOCK = BlockType(
    "html_block",
    continues=_html_block_continues,
    accepts_lines=True,
    start=_html_block_start,
    add_line=_html_block_add_line,
    finalize=_html_block_finalize,
)


BLOCK_QUOTE_MARKER = ">"


def _consume_block_quote_marker(cursor: Cursor) -> bool:
    """Consume a `>` marker with up to three columns of indentation and one optional following column.

    The optional column may be part of a tab, which leaves its remaining columns as content. Returns
    False and leaves the cursor untouched when the line has no marker.
    """
    if cursor.indent >= CODE_INDENT:
        return False
    marker = cursor.next_nonspace()
    if marker == len(cursor.line) or cursor.line[marker] != BLOCK_QUOTE_MARKER:
        return False
    cursor.advance_to(marker + 1)
    cursor.consume_columns(1)
    return True


def _block_quote_continues(block: Block, cursor: Cursor) -> bool:
    """A line continues the quote when it has a marker. A line without one is left to the lazy rule."""
    return _consume_block_quote_marker(cursor)


def _block_quote_start(cursor: Cursor, container: Block) -> Block | None:
    """Start a block quote when the line opens with a `>` marker."""
    if not _consume_block_quote_marker(cursor):
        return None
    return Block(BLOCK_QUOTE)


# A block quote is a container. A line without a marker still reaches a paragraph inside the quote
# through the engine's lazy rule, and any other unmatched block closes.
BLOCK_QUOTE = BlockType(
    "block_quote",
    continues=_block_quote_continues,
    is_container=True,
    start=_block_quote_start,
)


# A bullet, or one to nine digits and `.` or `)`. The marker must end the line or be followed by a space
# or tab, so `-foo` and `1.foo` are not items.
LIST_MARKER = re.compile(r"(?:([-+*])|([0-9]{1,9})([.)]))(?=[ \t]|\Z)")
LIST_MAX_SPACING = 4


@dataclass(frozen=True)
class ListItem:
    """The marker of a list item, and the absolute column where its content begins.

    `delimiter` is the bullet character, or the `.` or `)` after a number. Items with the same kind of
    marker and the same delimiter share a list. `start` is the number of an ordered marker, and 0 for a
    bullet. `content_column` is the absolute column where the content begins. `padding` is the same
    distance measured from the container's content column, so a continuation line is judged against the
    column its own enclosing containers leave, not the column of the line where the item started.
    """

    ordered: bool
    delimiter: str
    start: int
    content_column: int
    padding: int


def _list_item_start(cursor: Cursor, container: Block) -> Block | None:
    """Start a list item when the line opens with a bullet or an ordered marker.

    The marker may have up to three columns of indentation. Inside a paragraph, an item may not start
    with a blank line, and an ordered item must start at 1. One to four spaces after the marker set the
    content column. Five or more make the content an indented code block, so the content column is one
    column after the marker.
    """
    if cursor.indent >= CODE_INDENT:
        return None
    line = cursor.line
    start = cursor.next_nonspace()
    match = LIST_MARKER.match(line, start)
    if match is None:
        return None
    ordered = match.group(1) is None
    number = int(match.group(2)) if ordered else 0
    empty = not line[match.end() :].strip(SPACE_CHARS)
    if container.kind.accepts_lines and (empty or (ordered and number != 1)):
        return None
    container_column = cursor.col
    marker_column = cursor.col + cursor.indent
    width = match.end() - start
    cursor.advance_to(match.end())
    if empty:
        cursor.advance_to(len(line))
        spacing = 1
    else:
        spacing = indent_columns(line, cursor.pos, cursor.col)
        if spacing > LIST_MAX_SPACING:
            spacing = 1
        cursor.consume_columns(spacing)
    block = Block(LIST_ITEM)
    block.item = ListItem(
        ordered=ordered,
        delimiter=match.group(3) if ordered else match.group(1),
        start=number,
        content_column=marker_column + width + spacing,
        padding=marker_column + width + spacing - container_column,
    )
    return block


def _list_item_continues(block: Block, cursor: Cursor) -> bool:
    """A blank line continues an item that has content. Any other line must reach the content column.

    The column is measured from the cursor, which sits at the content column of the enclosing containers
    on this line. An empty item ends at the first blank line after its marker, so a blank line cannot give
    it a second.
    """
    if cursor.is_blank():
        return bool(block.children)
    item = block.item
    assert item is not None
    if cursor.indent < item.padding:
        return False
    cursor.consume_columns(item.padding)
    return True


# A list item is a container. Its start rule runs in any container that can hold a block, so a new item
# at the same level closes the previous one through the engine. Grouping items into lists happens at
# render time.
LIST_ITEM = BlockType(
    "list_item",
    continues=_list_item_continues,
    is_container=True,
    start=_list_item_start,
)


class BlockRegistry:
    """The block types a parse may use: the document root, the fallback paragraph, and start rules.

    Start rules are tried in registration order. The fallback type is the paragraph created when no
    start rule matches a line of text.
    """

    def __init__(self, root: BlockType, fallback: BlockType) -> None:
        self.root = root
        self.fallback = fallback
        self._names: set[str] = set()
        self._starts: list[BlockType] = []
        self.register(root)
        self.register(fallback)

    def register(self, block_type: BlockType) -> None:
        """Add a block type. Its start rule, if any, joins the start rules in order."""
        if block_type.name in self._names:
            raise ValueError(f"block type already registered: {block_type.name!r}")
        self._names.add(block_type.name)
        if block_type.start is not None:
            self._starts.append(block_type)

    def starts(self) -> tuple[BlockType, ...]:
        """The registered block types that have a start rule, in registration order."""
        return tuple(self._starts)


DEFAULT_REGISTRY = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
# Setext is registered before thematic break so that dashes after paragraph text make a heading.
DEFAULT_REGISTRY.register(SETEXT_HEADING)
DEFAULT_REGISTRY.register(THEMATIC_BREAK)
DEFAULT_REGISTRY.register(ATX_HEADING)
DEFAULT_REGISTRY.register(INDENTED_CODE)
DEFAULT_REGISTRY.register(FENCED_CODE)
DEFAULT_REGISTRY.register(HTML_BLOCK)
DEFAULT_REGISTRY.register(BLOCK_QUOTE)
# After thematic break, so `* * *` is a break and never an item.
DEFAULT_REGISTRY.register(LIST_ITEM)


class DocumentParser:
    """Runs the phase 1 per-line procedure over a document, one line at a time."""

    def __init__(self, registry: BlockRegistry = DEFAULT_REGISTRY) -> None:
        self.registry = registry
        self.root = Block(registry.root)
        self.root.references = ReferenceMap()

    def incorporate_line(self, line: str) -> None:
        """Match open blocks, look for new starts, then add the remaining text."""
        cursor = Cursor(line)

        # 1. Match open blocks. Unmatched blocks stay open: the line may be a lazy continuation.
        container = self._match_open_blocks(cursor)
        all_closed = container.open_last_child() is None
        blank_line = cursor.is_blank()

        # 2. Look for new block starts. Unmatched blocks are closed only once a start succeeds. A line that
        # can only lazily continue the open paragraph may start only a block that can interrupt one.
        cursor.lazy_paragraph = not all_closed and not cursor.is_blank() and self._tip().kind.lazy
        started = False
        while not self._is_text_leaf(container):
            new_block = self._try_starts(cursor, container)
            if new_block is None:
                break
            if not started:
                started = True
                all_closed = True
                cursor.lazy_paragraph = False
                self._close_below(container)
            self._attach(new_block, container)
            container = new_block

        # 3. Add the remaining text to the deepest open block.
        tip = self._tip()
        if not all_closed and not cursor.is_blank() and tip.kind.lazy:
            self._add_line(tip, cursor)
        else:
            self._close_below(container)
            if container.kind.accepts_lines:
                self._add_line(container, cursor)
            elif not cursor.is_blank():
                paragraph = Block(self.registry.fallback)
                self._attach(paragraph, container)
                self._add_line(paragraph, cursor)
        self._record_blankness(container, blank_line)

    def finish(self) -> Block:
        """Close every open block and return the document root."""
        self._close_below(self.root)
        self.root.is_open = False
        return self.root

    def _record_blankness(self, container: Block, blank_line: bool) -> None:
        """Note whether this line ended blank in the blocks it reached, which decides list looseness.

        A blank line marks the last child of the container it matched, since that child now ends with a
        blank line. The block that took the line, and each of its ancestors, takes the flag. A blank line in
        a block quote or a fenced code block is not a gap between blocks, so it does not set the flag.
        """
        if blank_line and container.children:
            container.children[-1].last_line_blank = True
        receiver = self._tip()
        flag = blank_line and receiver.kind is not BLOCK_QUOTE and receiver.kind is not FENCED_CODE
        node: Block | None = receiver
        while node is not None:
            node.last_line_blank = flag
            node = node.parent

    def _match_open_blocks(self, cursor: Cursor) -> Block:
        container = self.root
        while True:
            child = container.open_last_child()
            if child is None or not child.kind.continues(child, cursor):
                return container
            container = child

    def _try_starts(self, cursor: Cursor, container: Block) -> Block | None:
        for block_type in self.registry.starts():
            assert block_type.start is not None
            new_block = block_type.start(cursor, container)
            if new_block is not None:
                return new_block
        return None

    def _is_text_leaf(self, block: Block) -> bool:
        return block.kind.accepts_lines and not block.kind.interruptible

    def _attach(self, new_block: Block, container: Block) -> None:
        """Add `new_block` under `container`, closing any leaf that cannot hold it."""
        while not container.kind.is_container:
            self._finalize(container)
            assert container.parent is not None
            container = container.parent
        container.children.append(new_block)
        new_block.parent = container

    def _add_line(self, block: Block, cursor: Cursor) -> None:
        assert block.kind.add_line is not None
        block.kind.add_line(block, cursor)

    def _tip(self) -> Block:
        """The deepest open block."""
        tip = self.root
        while (child := tip.open_last_child()) is not None:
            tip = child
        return tip

    def _close_below(self, container: Block) -> None:
        child = container.open_last_child()
        if child is None:
            return
        self._close_below(child)
        self._finalize(child)

    def _finalize(self, block: Block) -> None:
        block.is_open = False
        if block.kind.finalize is not None:
            block.kind.finalize(block)


def parse_lines(lines: Iterable[str], registry: BlockRegistry = DEFAULT_REGISTRY) -> Block:
    """Build the block tree for `lines`, which hold no line-ending characters."""
    parser = DocumentParser(registry)
    for line in lines:
        parser.incorporate_line(line)
    return parser.finish()
