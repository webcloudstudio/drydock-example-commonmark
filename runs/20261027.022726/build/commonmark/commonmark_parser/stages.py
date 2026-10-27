from .model import Document, Node
from .references import collect_definitions
from .html_blocks import parse_html_block
from .block_quotes import parse_block_quote
from .lists import parse_list, parse_list_marker
from .inline import decode_escapes_and_entities, render_inline
import html
import re

_THEMATIC_BREAK = re.compile(r"(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,}\Z")


def _indent_columns(line: str) -> tuple[int, int]:
    columns = offset = 0
    while offset < len(line) and line[offset] in " \t":
        columns += 4 - columns % 4 if line[offset] == "\t" else 1
        offset += 1
    return columns, offset


def _remove_columns(line: str, amount: int) -> str:
    col = i = 0
    while i < len(line) and col < amount and line[i] in ' \t':
        n = 4 - col % 4 if line[i] == '\t' else 1
        if col + n > amount:
            return ' ' * (col + n - amount) + line[i+1:]
        col += n; i += 1
    return line[i:]


def _is_thematic_break(line: str) -> bool:
    columns, offset = _indent_columns(line)
    return columns <= 3 and bool(_THEMATIC_BREAK.fullmatch(line[offset:]))


def parse_blocks(markdown: str) -> Document:
    source = markdown.replace("\x00", "\ufffd").replace("\r\n", "\n").replace("\r", "\n")
    lines = source.splitlines(keepends=True)
    if source and not lines: lines = [source]
    children: list[Node] = []
    doc = Document(children=children)
    paragraph: list[str] = []

    def flush_paragraph():
        if paragraph:
            raw = '\n'.join(x.lstrip(' \t') for x in paragraph).lstrip(' \t')
            remainder = collect_definitions(raw + ('\n' if raw else ''), doc.references)
            if remainder.strip(): children.append(Node('paragraph', raw=remainder.rstrip('\n')))
            paragraph.clear()

    i = 0
    while i < len(lines):
        line = lines[i]; body = line.rstrip('\n')
        cols, off = _indent_columns(body)
        content = body[off:] if cols <= 3 else body
        quote = parse_block_quote(lines[i:])
        if quote:
            flush_paragraph()
            count, quote_lines = quote
            nested = parse_blocks(''.join(quote_lines))
            for key, value in nested.references.items():
                doc.references.setdefault(key, value)
            children.append(Node('block_quote', children=nested.children))
            i += count
            continue
        # Fenced code blocks.
        fm = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', body)
        if fm:
            flush_paragraph(); fence, info = fm.group(1), fm.group(2).strip(' \t')
            if fence[0] == '`' and '`' in info: fm = None
            else:
                i += 1; literal = []
                while i < len(lines):
                    candidate = lines[i].rstrip('\n')
                    close = re.match(r'^ {0,3}(' + re.escape(fence[0]) + r'{'+str(len(fence))+r',})[ \t]*$', candidate)
                    if close: i += 1; break
                    literal.append(_remove_columns(candidate, min(3, len(body)-len(body.lstrip(' ')))) + ('\n' if lines[i].endswith('\n') else ''))
                    i += 1
                children.append(Node('code_block', literal=''.join(literal), info=info)); continue
        # ATX heading.
        hm = re.match(r'^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$', body)
        if hm:
            flush_paragraph(); text = (hm.group(2) or '').strip(' \t')
            text = re.sub(r'[ \t]+#+[ \t]*$', '', text).strip(' \t')
            children.append(Node('heading', raw=text, level=len(hm.group(1)))); i += 1; continue
        # Setext underline converts the open paragraph.
        sm = re.match(r'^ {0,3}(=+|-+)[ \t]*$', body)
        if sm and paragraph:
            raw = '\n'.join(x.lstrip(' \t') for x in paragraph).lstrip(' \t')
            remainder = collect_definitions(raw + '\n', doc.references)
            # A definition-only paragraph is removed, but the underline still
            # becomes ordinary paragraph text when there is no heading text.
            if remainder.strip(): children.append(Node('heading', raw=remainder.rstrip('\n'), level=1 if sm.group(1)[0] == '=' else 2))
            else: children.append(Node('paragraph', raw=body.strip()))
            paragraph.clear(); i += 1; continue
        if not body.strip(' \t'):
            flush_paragraph(); i += 1; continue
        # HTML blocks.
        html_result = parse_html_block(lines[i:], paragraph_open=bool(paragraph))
        if html_result:
            flush_paragraph(); count, raw = html_result; children.append(Node('html_block', raw=raw)); i += count; continue
        if _is_thematic_break(body):
            flush_paragraph(); children.append(Node('thematic_break')); i += 1; continue
        parsed_list = parse_list(lines[i:], paragraph_open=bool(paragraph))
        if parsed_list:
            flush_paragraph()
            count, list_node = parsed_list
            children.append(list_node)
            i += count
            continue
        # Indented code, only outside paragraphs.
        if cols >= 4 and not paragraph:
            code=[]
            while i < len(lines):
                b=lines[i].rstrip('\n'); c,_=_indent_columns(b)
                if not b.strip(' \t'):
                    code.append(''); i += 1; continue
                if c < 4: break
                code.append(_remove_columns(b,4)); i += 1
            while code and code[-1] == '': code.pop()
            literal=''.join(x+'\n' for x in code)
            if literal: children.append(Node('code_block', literal=literal))
            continue
        if _is_thematic_break(body):
            flush_paragraph(); children.append(Node('thematic_break'))
        else:
            paragraph.append(content)
        i += 1
    flush_paragraph()
    return doc


def parse_inlines(document: Document) -> Document:
    return document


def render_html(document: Document) -> str:
    references = document.references
    out=[]
    for node in document.children:
        if node.type == 'heading':
            out.append(f'<h{node.level}>{render_inline(node.raw, references)}</h{node.level}>\n')
        elif node.type == 'paragraph': out.append(f'<p>{render_inline(node.raw, references)}</p>\n')
        elif node.type == 'thematic_break': out.append('<hr />\n')
        elif node.type == 'code_block':
            info = decode_escapes_and_entities(node.info)
            cls = f' class="language-{html.escape(info.split()[0], quote=True)}"' if info else ''
            out.append(f'<pre><code{cls}>{html.escape(node.literal)}</code></pre>\n')
        elif node.type == 'html_block': out.append(node.raw + ('' if node.raw.endswith('\n') else '\n'))
        elif node.type == 'block_quote':
            inner = render_html(Document(children=node.children, references=references))
            out.append('<blockquote>\n' + inner + '</blockquote>\n')
        elif node.type == 'list':
            parts = node.info.split(':')
            ordered = parts[0] == 'ordered'
            tight = len(parts) < 3 or parts[2] == 'tight'
            tag = 'ol' if ordered else 'ul'
            attr = f' start="{parts[1]}"' if ordered and parts[1] and parts[1] != '1' else ''
            out.append(f'<{tag}{attr}>\n')
            for item in node.children:
                inner = render_html(Document(children=item.children, references=references))
                if tight:
                    inner = re.sub(r'<p>(.*?)</p>\n', r'\1\n', inner, flags=re.S)
                out.append('<li>' + inner + '</li>\n')
            out.append(f'</{tag}>\n')
    return ''.join(out)
