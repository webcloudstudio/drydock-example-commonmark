"""CommonMark parser integration interfaces."""

from .blocks import Document, parse_blocks
from html import escape, unescape
import re

from .inlines import parse_inlines
from .links import parse_links
from .images import parse_images
from .autolinks import parse_autolinks
from .inline_html_breaks import parse_inline_html_breaks
from urllib.parse import quote


def render(markdown: str) -> str:
    """Render a complete Markdown document to CommonMark HTML."""
    document = parse_blocks(markdown)
    return "".join(_render_block(block, document.references, tight=False) for block in document.children)


def _render_inlines(source: str, references: dict) -> str:
    """Render inline constructs, keeping code and raw HTML opaque."""
    pieces: list[str] = []
    for token in parse_inline_html_breaks(source):
        if token.type == "hardbreak":
            pieces.append("<br />\n")
            continue
        if token.type == "html":
            pieces.append(token.literal)
            continue
        # First resolve links and images against the document-wide definition map.
        links = parse_links(token.literal, references)
        for item in links:
            if item.type == "link":
                label = "".join(_render_inline_node(n, references) for n in (item.children or []))
                title = f' title="{escape(item.title, quote=True)}"' if item.title is not None else ""
                destination = quote(item.destination, safe="/:?#@!$&'()*+,;=%-._~")
                pieces.append(f'<a href="{escape(destination, quote=True)}"{title}>{label}</a>')
            else:
                # Image syntax is a distinct provider; preserve all intervening text.
                pieces.extend(_render_text_with_images(item.literal, references))
    return "".join(pieces)


def _render_text_with_images(source: str, references: dict) -> list[str]:
    from .images import _bracket_end, _destination_and_title, _normalize_label, _decode
    out: list[str] = []
    i = 0
    while i < len(source):
        if source.startswith("![", i):
            close = _bracket_end(source, i + 1)
            if close is not None:
                alt = source[i + 2:close]
                after = close + 1
                parsed = _destination_and_title(source, after + 1) if after < len(source) and source[after] == "(" else None
                if parsed:
                    dest, title, end = parsed
                    title_attr = f' title="{escape(title, quote=True)}"' if title is not None else ""
                    dest = quote(dest, safe="/:?#@!$&'()*+,;=%-._~")
                    out.append(f'<img src="{escape(dest, quote=True)}" alt="{escape(_plain_alt(alt, references), quote=True)}"{title_attr} />')
                    i = end; continue
                ref = alt
                end = after
                if after < len(source) and source[after] == "[":
                    rc = _bracket_end(source, after)
                    if rc is not None:
                        ref = source[after + 1:rc] or alt; end = rc + 1
                entry = references.get(_normalize_label(_decode(ref)))
                if entry is not None:
                    dest, title = (entry.get("destination", ""), entry.get("title")) if isinstance(entry, dict) else (entry[0], entry[1] if len(entry) > 1 else None)
                    title_attr = f' title="{escape(title, quote=True)}"' if title is not None else ""
                    dest = quote(dest, safe="/:?#@!$&'()*+,;=%-._~")
                    out.append(f'<img src="{escape(dest, quote=True)}" alt="{escape(_plain_alt(alt, references), quote=True)}"{title_attr} />')
                    i = end; continue
        end = source.find("![", i + 1)
        if end < 0: end = len(source)
        out.append(_render_plain(source[i:end], references)); i = end
    return out


def _plain_alt(source: str, references: dict) -> str:
    from .images import _plain_description
    return _plain_description(source, references)


def _render_plain(source: str, references: dict) -> str:
    # Recognize autolinks before escape processing. An escaped punctuation mark
    # inside a URI is part of the URI source and must not split its token.
    result: list[str] = []
    for auto in parse_autolinks(source):
        if auto.type == "link":
            destination = quote(auto.destination, safe=":/?#@!$&'()*+,;=%-._~")
            result.append(f'<a href="{escape(destination, quote=True)}">{escape(auto.label, quote=True)}</a>')
        else:
            result.append("".join(_render_inline_node(node, references) for node in parse_inlines(auto.literal, references)))
    return "".join(result)


def _render_inline_node(node, references: dict) -> str:
    if node.type == "text": return escape(node.literal, quote=True)
    if node.type == "escaped": return escape(node.literal, quote=True)
    if node.type == "entity": return escape(node.literal, quote=True)
    if node.type == "code": return f"<code>{escape(node.literal, quote=True)}</code>"
    if node.type == "softbreak": return "\n"
    if node.type == "em": return "<em>" + "".join(_render_inline_node(n, references) for n in node.children or []) + "</em>"
    if node.type == "strong": return "<strong>" + "".join(_render_inline_node(n, references) for n in node.children or []) + "</strong>"
    return escape(getattr(node, "literal", ""), quote=False)


def _render_block(block, references: dict, tight: bool) -> str:
    if block.kind == "paragraph":
        body = _render_inlines(block.literal, references)
        return body + "\n" if tight else f"<p>{body}</p>\n"
    if block.kind == "heading":
        return f"<h{block.level}>{_render_inlines(block.literal, references)}</h{block.level}>\n"
    if block.kind == "thematic_break": return "<hr />\n"
    if block.kind == "fenced_code":
        info = block.info.split(None, 1)[0] if block.info else ""
        info = unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", info))
        cls = f' class="language-{escape(info, quote=True)}"' if info else ""
        return f"<pre><code{cls}>{escape(block.literal, quote=False)}</code></pre>\n"
    if block.kind == "indented_code": return f"<pre><code>{escape(block.literal, quote=True)}</code></pre>\n"
    if block.kind == "html_block": return block.literal
    if block.kind == "block_quote":
        # Tightness suppresses only paragraphs that are direct list-item
        # children; paragraphs inside a nested quote retain their tags.
        inner = "".join(_render_block(child, references, False) for child in block.children)
        return "<blockquote>\n" + inner + "</blockquote>\n"
    if block.kind == "list":
        tag = "ol" if block.ordered else "ul"
        attr = f' start="{block.start}"' if block.ordered and block.start != 1 else ""
        def render_item(item):
            parts = []
            for child in item.children:
                if block.tight and child.kind == "paragraph":
                    parts.append(_render_inlines(child.literal, references) + "\n")
                else:
                    parts.append(_render_block(child, references, False))
            return "<li>" + "".join(parts) + "</li>\n"
        body = "".join(render_item(item) for item in block.children)
        return f"<{tag}{attr}>\n{body}</{tag}>\n"
    return ""


__all__ = ["Document", "parse_blocks", "parse_inlines", "render"]
