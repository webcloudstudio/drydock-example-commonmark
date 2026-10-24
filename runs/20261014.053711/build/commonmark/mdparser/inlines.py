"""Phase 2: inline parsing.

Responsibility: parse the raw text of paragraphs and headings into inline nodes with the
delimiter-stack algorithms (look for link or image, process emphasis), using the reference map
from `mdparser.refs`.
"""

import re
import unicodedata
from dataclasses import dataclass, field

from mdparser.entities import ASCII_PUNCTUATION, match_reference
from mdparser.links import LinkTail, match_inline_link, match_reference_tail
from mdparser.refs import ReferenceMap
from mdparser.render import escape_html, percent_encode_url

# Inline nodes. A delimiter run is a `Text` node until emphasis consumes some of its characters;
# whatever is left over is literal text. Everything else is already-rendered `Html`.
# The bracket openers `[` and `![` are also `Text` nodes until a link or image closes over them.
BRACKET_MARKERS = ("[", "![")


@dataclass
class Text:
    """An unconsumed run of `*` or `_` characters, escaped on output."""

    literal: str


@dataclass
class Html:
    """Rendered inline HTML: text, a code span, an autolink, raw HTML, or a decoded reference.

    `text` is the node's plain-text value, used for image alt text: markup is dropped, and the
    characters are unescaped.
    """

    html: str
    text: str


@dataclass
class Element:
    """An emphasis element. Its children are the nodes that sat between its opener and closer."""

    tag: str
    children: list["Node"] = field(default_factory=list)


@dataclass
class Link:
    """A link element. Its children are the nodes that sat between its brackets, already processed."""

    href: str
    title: str | None
    children: list["Node"] = field(default_factory=list)


@dataclass
class Image:
    """An image. Its children are the nodes of its description, already processed; they give the alt text."""

    destination: str
    title: str | None
    children: list["Node"] = field(default_factory=list)


Node = Text | Html | Element | Link | Image


@dataclass(eq=False)
class Delimiter:
    """A delimiter stack entry. Identity matters, so entries compare by object, not by value.

    `previous` and `next` link the stack from the bottom sentinel upward. `node` is the `Text` node
    holding the run, or None for the bottom sentinel. A bracket opener is an entry whose `char` is
    `[` or `![`, and `position` is the source index where that opener starts.
    """

    node: Text | None
    char: str
    length: int
    original_length: int
    can_open: bool
    can_close: bool
    active: bool = True
    previous: "Delimiter | None" = None
    next: "Delimiter | None" = None
    position: int = 0

# The body of an autolink: everything between `<` and `>` except ASCII control characters, space,
# `<` and `>`. The URI and email rules are checked against this body.
AUTOLINK_PATTERN = re.compile(r"<([^\x00-\x20\x7f<>]*)>")
# A scheme is 2 to 32 characters: an ASCII letter, then letters, digits, `+`, `.` or `-`.
URI_SCHEME_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]{1,31}:")
# The non-normative HTML5 email address regex from the spec, without its anchors.
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
)

# A backtick string is a maximal run of backticks. Code spans open and close on equal-length runs.
BACKTICK_RUN_PATTERN = re.compile(r"`+")

# Whitespace in a raw HTML tag: spaces and tabs, with at most one line ending.
_WS = r"[ \t]*(?:\n[ \t]*)?"
# Whitespace that must be present: an attribute cannot follow its tag name or value directly.
_WS_REQUIRED = r"(?=[ \t\n])" + _WS
_TAG_NAME = r"[A-Za-z][A-Za-z0-9\-]*"
_ATTR_NAME = r"[A-Za-z_:][A-Za-z0-9_.:\-]*"
# An unquoted value is nonempty and has no whitespace, quote, `=`, `<`, `>` or backtick.
_UNQUOTED_VALUE = r"[^ \t\n\r\"'=<>`]+"
_ATTR_VALUE = rf"(?:{_UNQUOTED_VALUE}|'[^']*'|\"[^\"]*\")"
_ATTRIBUTE = rf"{_WS_REQUIRED}{_ATTR_NAME}(?:{_WS}={_WS}{_ATTR_VALUE})?"
# The raw HTML grammars from the spec, tried in order. Each one is anchored at the `<` by `match`.
RAW_HTML_PATTERNS = tuple(
    re.compile(pattern)
    for pattern in (
        rf"<{_TAG_NAME}(?:{_ATTRIBUTE})*{_WS}/?>",
        rf"</{_TAG_NAME}{_WS}>",
        # `<!-->` and `<!--->` are complete comments; any other comment ends at the first `-->`.
        r"<!--(?:>|->|(?s:.*?)-->)",
        r"<\?(?s:.*?)\?>",
        r"<![A-Za-z][^>]*>",
        r"<!\[CDATA\[(?s:.*?)\]\]>",
    )
)


def parse_inline(raw: str, references: ReferenceMap | None = None) -> str:
    """Inline parser hook: return the HTML for a block's raw content.

    The scan runs left to right. At each special character the constructs that start there are
    tried, and the first one that matches is taken whole. Code spans, autolinks and raw HTML have
    equal precedence, so whichever starts first wins. A backtick string with no closing run of the
    same length is literal text, and the whole run is consumed. An autolink or raw HTML tag is taken
    whole, so a backslash inside it stays literal. A backslash before ASCII punctuation yields that
    character, so `\\<` and `\\`` do not open a construct. A recognized character reference is
    decoded and its character is escaped text, so `&#42;` never opens structure. A run of `*` or `_`
    becomes a delimiter run: a text node pushed on the delimiter stack, which process_emphasis then
    pairs into emphasis. A `[` or `![` pushes a bracket opener on the same stack, and a `]` runs the
    look-for-link-or-image procedure against the nearest opener, using `references` for reference
    forms. Two or more spaces, or a backslash, before a line ending that is not at the end of the
    text make a hard break. Any other line ending is a soft break, and spaces before it are dropped.
    Everything else is escaped text.
    """
    references = ReferenceMap() if references is None else references
    nodes: list[Node] = []
    stack = DelimiterStack(nodes)
    index = 0
    while index < len(raw):
        char = raw[index]
        if char == "`":
            code_span = _match_code_span(raw, index)
            if code_span is not None:
                node, index = code_span
                nodes.append(node)
                continue
            run_end = BACKTICK_RUN_PATTERN.match(raw, index).end()
            nodes.append(_text(raw[index:run_end]))
            index = run_end
            continue
        if char == "<":
            autolink = _match_autolink(raw, index)
            if autolink is not None:
                node, index = autolink
                nodes.append(node)
                continue
            raw_html_end = _match_raw_html(raw, index)
            if raw_html_end is not None:
                nodes.append(_raw(raw[index:raw_html_end]))
                index = raw_html_end
                continue
        elif char == "\\" and index + 1 < len(raw) and raw[index + 1] in ASCII_PUNCTUATION:
            nodes.append(_text(raw[index + 1]))
            index += 2
            continue
        elif char == "\\" and raw[index + 1 : index + 2] == "\n" and index + 2 < len(raw):
            # A backslash before a line ending is a hard break. The backslash and line ending are consumed.
            nodes.append(_hard_break())
            index = _skip_spaces(raw, index + 2)
            continue
        elif char == " " and (newline := _line_ending_after_spaces(raw, index)) is not None:
            # Two or more spaces before a line ending make a hard break; fewer make a soft break.
            # Either way the spaces are consumed, so they never reach the output.
            nodes.append(_hard_break() if newline - index >= 2 else _soft_break())
            index = _skip_spaces(raw, newline + 1)
            continue
        elif char == "\n":
            nodes.append(_soft_break())
            index = _skip_spaces(raw, index + 1)
            continue
        elif char in "*_":
            run_end = _delimiter_run_end(raw, index)
            _push_delimiter_run(stack, raw, index, run_end)
            index = run_end
            continue
        elif char == "&":
            reference = match_reference(raw, index)
            if reference is not None:
                # A decoded character is text, so it is escaped like any other text.
                value, index = reference
                nodes.append(_text(value))
                continue
        elif char == "[":
            _push_bracket(stack, "[", index)
            index += 1
            continue
        elif char == "!" and raw[index + 1 : index + 2] == "[":
            _push_bracket(stack, "![", index)
            index += 2
            continue
        elif char == "]":
            index = _close_bracket(stack, raw, index, references)
            continue
        nodes.append(_text(char))
        index += 1
    stack.process_emphasis()
    return render_nodes(nodes)


def _text(value: str) -> Html:
    """A literal run of text: escaped in the output, and its own plain text."""
    return Html(escape_html(value), value)


def _hard_break() -> Html:
    """A hard line break: `<br />` followed by a line ending. Its plain text, used for alt, is the line ending."""
    return Html("<br />\n", "\n")


def _soft_break() -> Html:
    """A soft line break: the line ending, output as written. Its plain text is the line ending."""
    return Html("\n", "\n")


def _skip_spaces(raw: str, start: int) -> int:
    """Return the index of the first character at or after `start` that is not a space.

    Used after a line ending: the spaces that begin the next line are dropped.
    """
    end = start
    while end < len(raw) and raw[end] == " ":
        end += 1
    return end


def _line_ending_after_spaces(raw: str, start: int) -> int | None:
    """Return the index of the line ending that ends the run of spaces at `start`, or None.

    Only U+0020 counts as a space. A line ending at the very end of the text is not a break, since
    the block has no following line.
    """
    end = start
    while end < len(raw) and raw[end] == " ":
        end += 1
    if raw[end : end + 1] == "\n" and end + 1 < len(raw):
        return end
    return None


def _raw(value: str) -> Html:
    """Raw HTML, output as written. Its plain text is the same source, escaped only when used as alt."""
    return Html(value, value)


def render_nodes(nodes: list[Node]) -> str:
    """Render a node list to HTML. Leftover delimiter runs and brackets are escaped literal text."""
    parts: list[str] = []
    for node in nodes:
        if isinstance(node, Html):
            parts.append(node.html)
        elif isinstance(node, Text):
            parts.append(escape_html(node.literal))
        elif isinstance(node, Link):
            parts.append(_render_link(node))
        elif isinstance(node, Image):
            parts.append(_render_image(node))
        else:
            parts.append(f"<{node.tag}>{render_nodes(node.children)}</{node.tag}>")
    return "".join(parts)


def _render_link(link: Link) -> str:
    """Render a link element. The href is percent-encoded then escaped; an empty title is omitted."""
    href = escape_html(percent_encode_url(link.href))
    title = f' title="{escape_html(link.title)}"' if link.title else ""
    return f'<a href="{href}"{title}>{render_nodes(link.children)}</a>'


def _render_image(image: Image) -> str:
    """Render an image. The src is percent-encoded then escaped; alt is the escaped plain text of the description."""
    src = escape_html(percent_encode_url(image.destination))
    alt = escape_html(_plain_text(image.children))
    title = f' title="{escape_html(image.title)}"' if image.title else ""
    return f'<img src="{src}" alt="{alt}"{title} />'


def _plain_text(nodes: list[Node]) -> str:
    """The plain text of a node list: emphasis, links and images keep their text, and markup is dropped."""
    parts: list[str] = []
    for node in nodes:
        if isinstance(node, Html):
            parts.append(node.text)
        elif isinstance(node, Text):
            parts.append(node.literal)
        else:
            parts.append(_plain_text(node.children))
    return "".join(parts)


def _push_bracket(stack: "DelimiterStack", marker: str, start: int) -> None:
    """Push a bracket opener for `[` or `![`, which starts at `start`, as literal text until closed."""
    stack.push(Text(marker), marker, len(marker), True, False)
    stack.top.position = start


def _close_bracket(stack: "DelimiterStack", raw: str, close: int, references: ReferenceMap) -> int:
    """The look-for-link-or-image procedure at the `]` at `close`. Return the index to resume at.

    The nearest opener is used. With no opener, or an inactive one, the `]` is literal. Otherwise the
    inline form, then the reference forms, are tried after the `]`. A match becomes a link, or an
    image construct, over the nodes after the opener. A failed match removes the opener and leaves
    the `]` literal. A link also deactivates every earlier `[` opener, so links never nest.
    """
    opener = stack.nearest_bracket()
    if opener is None or not opener.active:
        if opener is not None:
            stack.remove_bracket(opener)
        stack.nodes.append(_text("]"))
        return close + 1
    text = raw[opener.position + len(opener.char) : close]
    tail: LinkTail | None = match_inline_link(raw, close + 1)
    if tail is None:
        tail = match_reference_tail(raw, close + 1, text, references)
    if tail is None:
        stack.remove_bracket(opener)
        stack.nodes.append(_text("]"))
        return close + 1
    if opener.char == "![":
        children = stack.close_bracket(opener)
        stack.nodes.append(Image(tail.destination, tail.title, children))
    else:
        stack.deactivate_bracket_openers(opener)
        children = stack.close_bracket(opener)
        stack.nodes.append(Link(tail.destination, tail.title, children))
    return tail.end


def _delimiter_run_end(raw: str, start: int) -> int:
    """Return the index just past the maximal run of the delimiter character at `start`."""
    end = start + 1
    while end < len(raw) and raw[end] == raw[start]:
        end += 1
    return end


def _push_delimiter_run(stack: "DelimiterStack", raw: str, start: int, end: int) -> None:
    """Append the run raw[start:end] as a text node and push its stack entry with flanking flags.

    The characters before and after the run decide flanking. The start and end of the line count
    as whitespace, so a missing neighbour is passed as None.
    """
    char = raw[start]
    before = raw[start - 1] if start > 0 else None
    after = raw[end] if end < len(raw) else None
    left_flanking, right_flanking = _flanking(before, after)
    if char == "*":
        can_open, can_close = left_flanking, right_flanking
    else:
        can_open = left_flanking and (not right_flanking or _is_punctuation(before))
        can_close = right_flanking and (not left_flanking or _is_punctuation(after))
    stack.push(Text(char * (end - start)), char, end - start, can_open, can_close)


def _is_whitespace(char: str | None) -> bool:
    """Unicode whitespace: tab, line feed, form feed, carriage return, or a Zs character.

    The start and end of the line are passed as None and count as whitespace.
    """
    return char is None or char in "\t\n\f\r" or unicodedata.category(char) == "Zs"


def _is_punctuation(char: str | None) -> bool:
    """Unicode punctuation or symbol: categories P* and S*. None (the line edge) is not one."""
    return char is not None and unicodedata.category(char)[0] in "PS"


def _flanking(before: str | None, after: str | None) -> tuple[bool, bool]:
    """Return (left-flanking, right-flanking) for a delimiter run with these neighbours."""
    left_flanking = not _is_whitespace(after) and (
        not _is_punctuation(after) or _is_whitespace(before) or _is_punctuation(before)
    )
    right_flanking = not _is_whitespace(before) and (
        not _is_punctuation(before) or _is_whitespace(after) or _is_punctuation(after)
    )
    return left_flanking, right_flanking


class DelimiterStack:
    """The delimiter stack: a doubly linked list of `Delimiter` entries over a sibling node list.

    The bottom sentinel is never removed, so `stack_bottom` is always an entry. `process_emphasis`
    wraps the nodes between a matched pair inside `nodes`, so every delimiter it touches must be a
    sibling of the others in that list.
    """

    def __init__(self, nodes: list[Node]) -> None:
        self.nodes = nodes
        self.bottom = Delimiter(None, "", 0, 0, False, False)
        self.top = self.bottom

    def push(self, node: Text, char: str, length: int, can_open: bool, can_close: bool) -> None:
        """Append a delimiter entry for a run that is already a `Text` node in `nodes`."""
        self.nodes.append(node)
        entry = Delimiter(node, char, length, length, can_open, can_close, previous=self.top)
        self.top.next = entry
        self.top = entry

    def process_emphasis(self, stack_bottom: Delimiter | None = None) -> None:
        """Pair delimiter runs above `stack_bottom` into em and strong (Appendix algorithm).

        `openers_bottom` is keyed by delimiter character, the closer's original length mod 3, and
        whether the closer can also open. Each key holds the lowest entry an opener search may
        reach, so a failed search is not repeated. Unmatched runs stay as literal text.
        """
        bottom = self.bottom if stack_bottom is None else stack_bottom
        openers_bottom: dict[tuple[str, int, bool], Delimiter] = {}
        closer = self._first_closer(bottom.next)
        while closer is not None:
            key = (closer.char, closer.original_length % 3, closer.can_open)
            opener = self._find_opener(closer, bottom, openers_bottom.get(key, bottom))
            if opener is None:
                openers_bottom[key] = closer.previous
                following = closer.next
                if not closer.can_open:
                    self._unlink(closer)
                closer = self._first_closer(following)
                continue
            strong = opener.length >= 2 and closer.length >= 2
            used = 2 if strong else 1
            opener.length -= used
            closer.length -= used
            self._unlink_between(opener, closer)
            self._sync_literal(opener)
            self._sync_literal(closer)
            self._wrap(opener.node, closer.node, "strong" if strong else "em")
            if opener.length == 0:
                self._drop(opener)
            if closer.length == 0:
                following = closer.next
                self._drop(closer)
                closer = self._first_closer(following)
        bottom.next = None
        self.top = bottom

    def nearest_bracket(self) -> Delimiter | None:
        """The bracket opener nearest the top of the stack, or None when there is none."""
        entry = self.top
        while entry is not None and entry.char not in BRACKET_MARKERS:
            entry = entry.previous
        return entry

    def remove_bracket(self, opener: Delimiter) -> None:
        """Remove a bracket opener from the stack. Its `[` or `![` text stays as literal text."""
        self._unlink(opener)

    def deactivate_bracket_openers(self, opener: Delimiter) -> None:
        """Mark every `[` opener below `opener` inactive, so a link cannot form around a link."""
        entry = opener.previous
        while entry is not None:
            if entry.char == "[":
                entry.active = False
            entry = entry.previous

    def close_bracket(self, opener: Delimiter) -> list[Node]:
        """Process emphasis inside a matched bracket and take its content out of the node list.

        Every delimiter above the opener leaves the stack, and the opener's own text node is removed.
        Return the nodes that sat after the opener, in order, as the content of the new element.
        """
        self.process_emphasis(stack_bottom=opener)
        start = self._index_of(opener.node)
        content = self.nodes[start + 1 :]
        del self.nodes[start:]
        self._unlink(opener)
        return content

    def _first_closer(self, entry: Delimiter | None) -> Delimiter | None:
        while entry is not None and not entry.can_close:
            entry = entry.next
        return entry

    def _find_opener(
        self, closer: Delimiter, bottom: Delimiter, openers_bottom: Delimiter
    ) -> Delimiter | None:
        """Search back from the closer for a matching opener above both lower bounds, or None.

        Under the multiple-of-3 rule a pair is skipped when one run can both open and close and the
        original lengths sum to a multiple of 3, unless both lengths are multiples of 3.
        """
        potential = closer.previous
        while potential is not None and potential is not bottom and potential is not openers_bottom:
            odd_match = (
                (closer.can_open or potential.can_close)
                and closer.original_length % 3 != 0
                and (potential.original_length + closer.original_length) % 3 == 0
            )
            if potential.char == closer.char and potential.can_open and not odd_match:
                return potential
            potential = potential.previous
        return None

    def _unlink(self, entry: Delimiter) -> None:
        """Remove an entry from the stack. Its node stays in `nodes` as text."""
        entry.previous.next = entry.next
        if entry.next is not None:
            entry.next.previous = entry.previous
        else:
            self.top = entry.previous

    def _unlink_between(self, opener: Delimiter, closer: Delimiter) -> None:
        """Remove every entry strictly between an opener and a closer from the stack."""
        opener.next = closer
        closer.previous = opener

    def _drop(self, entry: Delimiter) -> None:
        """Remove an exhausted run from the stack and from `nodes`."""
        self._unlink(entry)
        del self.nodes[self._index_of(entry.node)]

    def _sync_literal(self, entry: Delimiter) -> None:
        entry.node.literal = entry.char * entry.length

    def _wrap(self, opener_node: Text, closer_node: Text, tag: str) -> None:
        """Move the nodes between opener and closer into a new element after the opener."""
        start = self._index_of(opener_node) + 1
        end = self._index_of(closer_node)
        self.nodes[start:end] = [Element(tag, self.nodes[start:end])]

    def _index_of(self, node: Node) -> int:
        for index, candidate in enumerate(self.nodes):
            if candidate is node:
                return index
        raise ValueError("delimiter node is not in the node list")


def _match_code_span(raw: str, start: int) -> tuple[Html, int] | None:
    """Return the code span node for a backtick string at `start` and the index just past it.

    The span closes at the next backtick string of exactly the same length. Returns None when no
    such closing run exists, so the opening run is literal text.
    """
    opener = BACKTICK_RUN_PATTERN.match(raw, start)
    width = len(opener.group())
    content_start = opener.end()
    for closer in BACKTICK_RUN_PATTERN.finditer(raw, content_start):
        if len(closer.group()) == width:
            content = _normalize_code_content(raw[content_start : closer.start()])
            return Html(f"<code>{escape_html(content)}</code>", content), closer.end()
    return None


def _normalize_code_content(text: str) -> str:
    """Turn line endings into spaces, then strip one space from each end when both ends are spaces.

    Stripping is skipped when the content is entirely spaces. Only U+0020 counts as a space.
    """
    text = text.replace("\n", " ")
    if len(text) >= 2 and text[0] == " " and text[-1] == " " and text.strip(" "):
        return text[1:-1]
    return text


def _match_autolink(raw: str, start: int) -> tuple[Html, int] | None:
    """Return the link node for an autolink at `start` and the index just past it, or None."""
    match = AUTOLINK_PATTERN.match(raw, start)
    if match is None:
        return None
    body = match.group(1)
    if URI_SCHEME_PATTERN.match(body):
        href = body
    elif EMAIL_PATTERN.fullmatch(body):
        href = "mailto:" + body
    else:
        return None
    return Html(_link_html(href, body), body), match.end()


def _match_raw_html(raw: str, start: int) -> int | None:
    """Return the index just past the raw HTML construct at `start`, or None if none matches."""
    for pattern in RAW_HTML_PATTERNS:
        match = pattern.match(raw, start)
        if match is not None:
            return match.end()
    return None


def _link_html(href: str, text: str) -> str:
    """Render a link: the href is percent-encoded then escaped; the label is escaped text."""
    return f'<a href="{escape_html(percent_encode_url(href))}">{escape_html(text)}</a>'
