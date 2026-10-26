"""HTML renderer for parsed block nodes."""
import html
from .model import Document

def render_html(document: Document) -> str:
    return ''.join(_render(b) for b in document.blocks)

def _render(b, tight=False):
    t=b['type']
    if t=='paragraph': return b.get('html','') if tight else '<p>'+b.get('html','')+'</p>\n'
    if t=='heading': return f"<h{b['level']}>{b.get('html','')}</h{b['level']}>\n"
    if t=='hr': return '<hr />\n'
    if t=='code':
        lang=b.get('lang',''); attr=' class="language-'+html.escape(lang,quote=True)+'"' if lang else ''
        return '<pre><code'+attr+'>'+html.escape(b['text'],quote=True).replace('&#x27;', '&#39;')+'</code></pre>\n'
    if t=='html': return b['text']
    if t=='quote': return '<blockquote>\n'+''.join(_render(x) for x in b['children'])+'</blockquote>\n'
    if t=='list':
        tag='ol' if b['ordered'] else 'ul'; attr=f' start="{b["start"]}"' if tag=='ol' and b['start']!=1 else ''
        items=[]
        for item in b['items']:
            content=''.join(_render(x, tight=(not b['loose'] and x['type']=='paragraph')) for x in item)
            # CommonMark wraps multi-block item contents with newlines.
            if content and not content.endswith('\n'): content+='\n'
            items.append('<li>'+content+'</li>\n')
        return f'<{tag}{attr}>\n'+''.join(items)+f'</{tag}>\n'
    return ''
