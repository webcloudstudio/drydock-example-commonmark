"""HTML rendering boundary."""

from html import escape

from blocks import Block, Document
from inlines import parse_inlines


def render_document(document: Document) -> str:
    """Serialize completed blocks and their inline content as HTML."""
    output: list[str] = []
    for block in document.blocks:
        if block.kind == "heading":
            output.append(f"<h{block.level}>{_render_inline(block.content, document)}</h{block.level}>")
        elif block.kind == "paragraph":
            output.append(f"<p>{_render_inline(block.content, document)}</p>")
        elif block.kind == "code":
            output.append(f"<pre><code>{escape(block.content)}</code></pre>")
        elif block.kind == "fence":
            info = block.children[0].content if block.children else ""
            attr = f' class="language-{escape(info, quote=True)}"' if info else ""
            output.append(f"<pre><code{attr}>{escape(block.content)}</code></pre>")
        elif block.kind == "html":
            output.append(block.content)
        elif block.kind == "hr":
            output.append("<hr />")
        elif block.kind in {"blockquote", "list", "ordered", "bullet", "list_item"}:
            output.append(_render_container(block, document))
    return "\n".join(output) + ("\n" if output else "")


def _render_inline(text: str, document: Document) -> str:
    return _inline_html(text, document)


def _inline_html(text: str, document: Document | None = None) -> str:
    """Small structural inline renderer used by leaf blocks."""
    import re
    text, link_nodes = _replace_references(text, document)
    parts: list[str] = []
    raw_tags: list[str] = []
    pos = 0
    token = re.compile(r"(`+)(.*?)\1|(<(?:https?://|mailto:)[^ >]+>)|(<[A-Za-z/][^>]*>)|(\\[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", re.S)
    for match in token.finditer(text):
        parts.append(_inline_text(text[pos:match.start()]))
        if match.group(2) is not None:
            code = match.group(2).replace("\n", " ")
            if len(code) >= 2 and code.startswith(" ") and code.endswith(" ") and code.strip():
                code = code[1:-1]
            parts.append("<code>" + escape(code) + "</code>")
        elif match.group(3):
            target = match.group(3)[1:-1]
            parts.append('<a href="' + escape(target, quote=True) + '">' + escape(target) + "</a>")
        elif match.group(4):
            raw_tags.append(match.group(4))
            parts.append("\ue010" + str(len(raw_tags) - 1) + "\ue011")
        else:
            parts.append(_inline_text(match.group(5)))
        pos = match.end()
    parts.append(_inline_text(text[pos:]))
    rendered = _emphasis("".join(parts))
    rendered = re.sub("\\ue000([0-9a-f]+)\\ue001", lambda m: escape(chr(int(m.group(1), 16))), rendered)
    rendered = re.sub("\\ue030(\\d+)\\ue031", lambda m: link_nodes[int(m.group(1))], rendered)
    return re.sub("\\ue010(\\d+)\\ue011", lambda m: raw_tags[int(m.group(1))], rendered)


def _replace_references(text: str, document: Document | None) -> tuple[str, list[str]]:
    import re
    if document is None:
        return text, []
    from urllib.parse import quote, unquote
    nodes: list[str] = []
    out: list[str] = []
    pos = 0
    while pos < len(text):
        start = text.find("[", pos)
        image = start > 0 and text[start - 1] == "!"
        if start < 0:
            out.append(text[pos:]); break
        end = start + 1
        depth = 1
        while end < len(text) and depth:
            if text[end] == "\\": end += 2; continue
            if text[end] == "[": depth += 1
            elif text[end] == "]": depth -= 1
            end += 1
        if depth or end == start + 1:
            out.append(text[pos:start + 1]); pos = start + 1; continue
        label_text = text[start + 1:end - 1]
        suffix_end = end
        ref_label = None
        destination = title = None
        if suffix_end < len(text) and text[suffix_end] == "(" and not image:
            close = _matching_paren(text, suffix_end)
            if close is not None:
                parsed = _inline_destination(text[suffix_end + 1:close])
                if parsed:
                    destination, title = parsed; suffix_end = close + 1
        if destination is None and suffix_end < len(text) and text[suffix_end] == "[":
            close = text.find("]", suffix_end + 1)
            if close >= 0:
                ref_label = text[suffix_end + 1:close] or label_text
                suffix_end = close + 1
        if destination is None and ref_label is None:
            ref_label = label_text
        definition = document.references.get(ref_label) if ref_label is not None else None
        if destination is None and definition is not None:
            destination, title = definition
        if destination is None:
            out.append(text[pos:end]); pos = end; continue
        visible = _inline_html(label_text, document)
        if image:
            plain = re.sub(r"<[^>]+>|[*_`\\]", "", label_text)
            node = '<img src="' + escape(_url(destination), quote=True) + '" alt="' + escape(plain, quote=True) + '"'
            if title is not None:
                node += ' title="' + escape(title, quote=True) + '"'
            node += " />"
        else:
            node = '<a href="' + escape(_url(destination), quote=True) + '"'
            if title is not None:
                node += ' title="' + escape(title, quote=True) + '"'
            node += '>' + visible + "</a>"
        nodes.append(node)
        out.append(text[pos:start - 1] if image else text[pos:start])
        out.append("\ue030" + str(len(nodes) - 1) + "\ue031")
        pos = suffix_end
    return "".join(out), nodes


def _matching_paren(text: str, start: int) -> int | None:
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "\\": continue
        if text[i] == "(": depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0: return i
    return None


def _inline_destination(value: str) -> tuple[str, str | None] | None:
    import re
    value = value.strip(" \t\r\n")
    match = re.match(r"^(?:<([^\r\n<>]*)>|([^ \t\r\n]+))(?:[ \t\r\n]+([\"'])(.*?)\3)?[ \t\r\n]*$", value, re.S)
    if not match: return None
    destination = match.group(1) if match.group(1) is not None else match.group(2)
    title = match.group(4)
    destination = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", destination)
    if title is not None:
        title = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", r"\1", title)
    return destination, title


def _url(value: str) -> str:
    from urllib.parse import quote, unquote
    return quote(unquote(value), safe="/:?#[]@!$&'()*+,;=%~-._")


def _inline_text(text: str) -> str:
    import re
    import html
    protected: list[str] = []
    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(1))
        return "\ue000" + format(ord(match.group(1)), "x") + "\ue001"
    text = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~])", protect, text)
    rendered = escape(html.unescape(text), quote=True)
    return rendered


def _emphasis(text: str) -> str:
    import re
    protected: list[str] = []
    def protect_run(match: re.Match[str]) -> str:
        protected.append(match.group(2))
        return match.group(1) + f"\ue020{len(protected) - 1}\ue021"
    text = re.sub(r"(?m)(^|[ \t\n])([*_]{3,})(?=$|[ \t\n])", protect_run, text)
    # Apply strong before emphasis; recursive substitution handles nesting
    for marker, tag in (("**", "strong"), ("__", "strong"), ("*", "em"), ("_", "em")):
        pattern = re.escape(marker) + r"(?=\S)(?s:(.*?\S))" + re.escape(marker)
        text = re.sub(pattern, lambda m: f"<{tag}>" + _emphasis(m.group(1)) + f"</{tag}>", text)
    return re.sub(r"\ue020(\d+)\ue021", lambda m: protected[int(m.group(1))], text)


def _render_container(block: Block, document: Document, tight: bool = False) -> str:
    if block.kind == "blockquote":
        return "<blockquote>\n" + _render_children(block, document) + "\n</blockquote>"
    if block.kind in {"list", "ordered", "bullet"}:
        tag = "ol" if block.kind == "ordered" else "ul"
        attr = f' start="{block.content}"' if tag == "ol" and block.content != "1" else ""
        tight = block.level == 0
        return f"<{tag}{attr}>\n" + "\n".join(_render_container(item, document, tight) for item in block.children) + f"\n</{tag}>"
    return "<li>" + _render_children(block, document, tight=tight) + "</li>"


def _render_children(block: Block, document: Document, tight: bool = False) -> str:
    rendered = []
    for child in block.children:
        if child.kind == "paragraph":
            content = _render_inline(child.content, document)
            rendered.append(content if tight else f"<p>{content}</p>")
        elif child.kind == "heading":
            rendered.append(f"<h{child.level}>{_render_inline(child.content, document)}</h{child.level}>")
        elif child.kind == "code":
            rendered.append(f"<pre><code>{escape(child.content)}</code></pre>")
        elif child.kind == "fence":
            info = child.children[0].content if child.children else ""
            attr = f' class="language-{escape(info, quote=True)}"' if info else ""
            rendered.append(f"<pre><code{attr}>{escape(child.content)}</code></pre>")
        elif child.kind == "html":
            rendered.append(child.content)
        elif child.kind == "hr":
            rendered.append("<hr />")
        else:
            rendered.append(_render_container(child, document))
    return "\n".join(rendered)
