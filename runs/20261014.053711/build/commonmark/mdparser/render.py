"""HTML rendering.

Responsibility: turn the parsed tree into HTML, escape HTML text and attributes, and
percent-encode URLs. The conformance runner compares normalized HTML, so tag structure and
entities must match the spec examples.
"""

from __future__ import annotations

import string
from collections.abc import Callable

from mdparser.blocks import Block

InlineParser = Callable[[str], str]

ESCAPES = (("&", "&amp;"), ("<", "&lt;"), (">", "&gt;"), ('"', "&quot;"))
URL_SAFE_CHARS = frozenset(string.ascii_letters + string.digits + ";,/?:@&=+$-_.!~*'()#")
HEX_DIGITS = frozenset(string.hexdigits)


def escape_html(text: str) -> str:
    """Escape &, <, > and " so the text renders as literal characters. The ampersand goes first."""
    for raw, entity in ESCAPES:
        text = text.replace(raw, entity)
    return text


def percent_encode_url(url: str) -> str:
    """Percent-encode a URL for use in an attribute.

    URL-safe ASCII and existing %XX escapes are kept. Every other character is encoded as its
    UTF-8 bytes, so a lone % becomes %25.
    """
    out: list[str] = []
    index = 0
    while index < len(url):
        char = url[index]
        if char == "%" and _is_hex_pair(url[index + 1 : index + 3]):
            out.append(url[index : index + 3])
            index += 3
            continue
        if char in URL_SAFE_CHARS:
            out.append(char)
        else:
            out.extend(f"%{byte:02X}" for byte in char.encode("utf-8"))
        index += 1
    return "".join(out)


def _is_hex_pair(text: str) -> bool:
    return len(text) == 2 and all(char in HEX_DIGITS for char in text)


def render_document(root: Block, parse_inline: InlineParser) -> str:
    """Phase 2 walk: render the top-level blocks in order, one line ending after each block.

    `parse_inline` is the inline parser hook. It receives the raw content of each paragraph and
    returns that content's HTML.
    """
    return _render_children(root, parse_inline)


def _render_children(block: Block, parse_inline: InlineParser, tight: bool = False) -> str:
    """Render the children in order. A run of list items with the same marker becomes one list.

    In a tight list item a paragraph is its inline content, without a `<p>` wrapper. Each piece ends
    with a line ending unless it is inline text, so a line ending is added before the next piece.
    """
    pieces: list[str] = []
    children = block.children
    index = 0
    while index < len(children):
        child = children[index]
        if child.kind.name == "list_item":
            end = index + 1
            while end < len(children) and _same_list(child, children[end]):
                end += 1
            pieces.append(_render_list(children[index:end], parse_inline))
            index = end
            continue
        if tight and child.kind.name == "paragraph":
            pieces.append(parse_inline(child.content))
        else:
            pieces.append(_render_block(child, parse_inline))
        index += 1
    html = ""
    for piece in pieces:
        if html and not html.endswith("\n"):
            html += "\n"
        html += piece
    return html


def _same_list(first: Block, other: Block) -> bool:
    """True when `other` is a list item that continues the list `first` starts.

    A change of bullet character or of ordered delimiter starts a new list.
    """
    if other.kind.name != "list_item":
        return False
    assert first.item is not None and other.item is not None
    return (first.item.ordered, first.item.delimiter) == (other.item.ordered, other.item.delimiter)


def _render_list(items: list[Block], parse_inline: InlineParser) -> str:
    """One `<ul>` or `<ol>` holding an `<li>` per item. An ordered list states its start unless it is 1."""
    first = items[0].item
    assert first is not None
    tag = "ol" if first.ordered else "ul"
    open_tag = f'<ol start="{first.start}">' if first.ordered and first.start != 1 else f"<{tag}>"
    loose = _list_is_loose(items)
    body = "".join(_render_item(item, loose, parse_inline) for item in items)
    return f"{open_tag}\n{body}</{tag}>\n"


def _list_is_loose(items: list[Block]) -> bool:
    """A list is loose when a blank line separates two of its items, or two blocks inside one item.

    A gap between two items of a nested list is not a gap between blocks of this item: the nested list
    is one block, and its own looseness decides how its items are spaced.
    """
    for index, item in enumerate(items):
        has_next_item = index + 1 < len(items)
        if has_next_item and _ends_with_blank_line(item):
            return True
        for child_index, child in enumerate(item.children):
            if child_index + 1 < len(item.children):
                successor = item.children[child_index + 1]
                if child.kind.name == "list_item" and _same_list(child, successor):
                    continue
                has_next_block = True
            else:
                has_next_block = has_next_item
            if has_next_block and _ends_with_blank_line(child):
                return True
    return False


def _ends_with_blank_line(block: Block) -> bool:
    """True when `block` ends with a blank line, looking into the last child of each list item."""
    node: Block | None = block
    while node is not None:
        if node.last_line_blank:
            return True
        if node.kind.name != "list_item" or not node.children:
            return False
        node = node.children[-1]
    return False


def _render_item(item: Block, loose: bool, parse_inline: InlineParser) -> str:
    """One `<li>`. A loose item puts each block on its own line, after a line ending."""
    body = _render_children(item, parse_inline, tight=not loose)
    if loose and body:
        return f"<li>\n{body}</li>\n"
    return f"<li>{body}</li>\n"


def _render_block(block: Block, parse_inline: InlineParser) -> str:
    if block.kind.name == "block_quote":
        return f"<blockquote>\n{_render_children(block, parse_inline)}</blockquote>\n"
    if block.kind.name == "paragraph":
        return f"<p>{parse_inline(block.content)}</p>\n"
    if block.kind.name == "thematic_break":
        return "<hr />\n"
    if block.kind.name in ("atx_heading", "setext_heading"):
        return f"<h{block.level}>{parse_inline(block.content)}</h{block.level}>\n"
    if block.kind.name == "indented_code":
        return f"<pre><code>{escape_html(block.content)}</code></pre>\n"
    if block.kind.name == "fenced_code":
        return f"<pre>{_fenced_code_open_tag(block)}{escape_html(block.content)}</code></pre>\n"
    if block.kind.name == "html_block":
        # Raw lines pass through unchanged. The content already ends with a line ending.
        return block.content
    raise ValueError(f"no HTML renderer for block type {block.kind.name!r}")


def _fenced_code_open_tag(block: Block) -> str:
    """The `<code>` opening tag for a fenced block, with a language class when the info string has a word."""
    assert block.fence is not None
    language = block.fence.language
    if not language:
        return "<code>"
    return f'<code class="language-{escape_html(language)}">'
