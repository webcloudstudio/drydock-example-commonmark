"""Inline parsing for block text, with document-wide references."""
import html, re, unicodedata
from urllib.parse import quote
from html.entities import html5
from .model import Document

ESC=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
ENTITY=re.compile(r'&(?:#[xX][0-9A-Fa-f]{1,6}|#[0-9]{1,7}|[A-Za-z][A-Za-z0-9]+);')
_NAME = r'[A-Za-z][A-Za-z0-9-]*'
_ATTR = r'''[A-Za-z_:][A-Za-z0-9_.:-]*(?:[ \t\n]*=[ \t\n]*(?:[^\s"'=<>`]+|'[^']*'|"[^"]*"))?'''
TAG=re.compile(
    r'(?:<!-->|<!--->|<!--(?:.|\n)*?-->|<\?(?:.|\n)*?\?>|'
    r'<![A-Za-z](?:.|\n)*?>|<!\[CDATA\[(?:.|\n)*?\]\]>|'
    r'</'+_NAME+r'[ \t\n]*>|<'+_NAME+r'(?:[ \t\n]+'+_ATTR+r')*[ \t\n]*/?>)'
)
AUTO=re.compile(r'<((?:[A-Za-z][A-Za-z0-9+.-]{1,31}:[^ <>\x00-\x20]*|[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+))>')

def parse_inlines(document: Document) -> Document:
    def walk(blocks):
        for b in blocks:
            t=b['type']
            if t in ('paragraph','heading'): b['html']=inline(b['text'], document.references)
            if t in ('quote',): walk(b['children'])
            if t=='list':
                for item in b['items']: walk(item)
    walk(document.blocks); return document

def _dest(s):
    # Destinations are decoded before HTML rendering; preserve valid URL syntax
    # and percent-encode Unicode and otherwise unsafe characters as UTF-8.
    s=html.unescape(s)
    s=re.sub(r'\\([!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])',r'\1',s)
    return quote(s, safe=";/?:@&=+$,#-_.!~*'()%")
def _esc(s): return html.escape(s, quote=True).replace('&#x27;', '&#39;')
def _label(s): return ' '.join(s.split()).casefold()

def inline(src, refs, depth=0):
    if depth>12: return _esc(src)
    out=[]; i=0; n=len(src)
    while i<n:
        if src[i]=='\\' and i+1<n and src[i+1] in ESC:
            out.append(html.escape(src[i+1], quote=True).replace('&#x27;', '&#39;')); i+=2; continue
        if src[i]=='\n':
            # two trailing spaces or slash introduce a hard break
            trailing=0
            for part in reversed(out):
                if not part: continue
                if part.isspace() and '\n' not in part: trailing += len(part); continue
                break
            if trailing >= 2:
                while out and out[-1].isspace() and '\n' not in out[-1]: out.pop()
                out.append('<br />\n')
            elif out and out[-1].endswith('\\'): out[-1]=out[-1][:-1]; out.append('<br />\n')
            else: out.append('\n')
            i+=1
            while i<n and src[i] in ' \t': i+=1
            continue
        if src[i]=='`':
            m=re.match(r'`+',src[i:]); run=m.group(); end=src.find(run,i+len(run))
            while end>=0 and ((end+len(run)<n and src[end+len(run)]=='`') or (end>0 and src[end-1]=='`')): end=src.find(run,end+len(run))
            if end>=0:
                val=src[i+len(run):end].replace('\n',' ')
                if val.startswith(' ') and val.endswith(' ') and val.strip(): val=val[1:-1]
                out.append('<code>'+html.escape(val,quote=False)+'</code>'); i=end+len(run); continue
        am=AUTO.match(src,i)
        if am:
            x=am.group(1); url=x if ':' in x else 'mailto:'+x
            auto_url=quote(url, safe=";/?:@&=+$,#-_.!~*'()%")
            out.append('<a href="'+html.escape(auto_url,quote=True)+'">'+html.escape(x,quote=False)+'</a>'); i=am.end(); continue
        tm=TAG.match(src,i)
        if tm:
            tag=tm.group()
            # HTML comments with the two permitted short forms end at the
            # first >; any trailing characters remain ordinary inline text.
            if tag in ('<!-->', '<!--->'):
                out.append(tag)
                i += len(tag)
                continue
            # The HTML tag grammar requires whitespace between attributes;
            # reject malformed tag-shaped text instead of passing it raw.
            if tag.startswith('</'):
                # A closing tag has no attributes: only whitespace may occur
                # between its name and the final angle bracket.
                if not re.fullmatch(r'</'+_NAME+r'[ \t\n]*>', tag):
                    out.append(_esc(src[i])); i+=1; continue
                after=src[i+len(tag)-1:]
                if re.match(r'[^>]', after):
                    out.append(_esc(src[i])); i+=1; continue
            if tag.startswith('<') and not tag.startswith(('<!--','<?','<!','</')):
                inside=tag[1:-1].rstrip('/')
                # Backslash has no escaping role in HTML attributes. A quote
                # preceded by a backslash still closes the value; if that
                # leaves an unterminated/adjacent attribute, the whole tag is
                # invalid CommonMark raw HTML and must be emitted as text.
                # Backslashes do not escape HTML quotes. Validate attributes
                # with a small scanner so a quote immediately after a slash
                # still closes its value and any following quote is rejected.
                # TAG already recognizes only complete tags with the CommonMark
                # attribute grammar.  The secondary scanner used to reject
                # valid quoted values containing markup-like text.
            out.append(tag); i=tm.end(); continue
        em=ENTITY.match(src,i)
        if em:
            name=em.group()[1:-1]
            try:
                if name.startswith('#x') or name.startswith('#X'): c=chr(int(name[2:],16))
                elif name.startswith('#'): c=chr(int(name[1:]))
                else: c=html5.get(name+';')
                if isinstance(c, tuple): c=''.join(c)
                if c is None: out.append('&amp;'+name+';')
                else:
                    if not c or any(ord(ch)==0 or ord(ch)>0x10ffff or 0xd800<=ord(ch)<=0xdfff for ch in c): c='�'
                    out.append(html.escape(c,quote=True).replace('&#x27;', '&#39;'))
            except (ValueError, OverflowError): out.append('&amp;'+name+';')
            i=em.end(); continue
        if src[i]=='[' or src.startswith('![',i):
            image=src.startswith('![',i); st=i+2 if image else i+1
            close=_closing_bracket(src,st)
            if close>=0:
                label=src[st:close]; end=close+1; dest=title=None; nxt=end
                if nxt<len(src) and src[nxt]=='(':
                    parsed=_inline_target(src,nxt)
                    if parsed: dest,title,end=parsed
                if dest is None:
                    ref_label=None
                    if end<len(src) and src[end]=='[':
                        cl=_closing_bracket(src,end+1)
                        if cl>=0:
                            ref_label=src[end+1:cl] or label; end=cl+1
                    else: ref_label=label
                    if ref_label and _label(ref_label) in refs: dest,title=refs[_label(ref_label)]
                if dest is not None:
                    val=inline(label,refs,depth+1)
                    attr=' src' if image else ' href'
                    tag='img' if image else 'a'
                    attrs=attr+'="'+html.escape(_dest(dest),quote=True)+'"'
                    if image:
                        attrs+=' alt="'+html.escape(_plain_text(label, refs),quote=True)+'"'
                    if title is not None: attrs+=' title="'+html.escape(html.unescape(title),quote=True)+'"'
                    out.append('<'+tag+attrs+' />' if image else '<a'+attrs+'>'+val+'</a>')
                    i=end; continue
        # emphasis: find a valid matching delimiter and recurse
        if src[i] in '*_':
            ch=src[i]; run=re.match(re.escape(ch)+'+',src[i:]).group(); length=len(run)
            before=src[i-1] if i else '\n'; after=src[i+length] if i+length<n else '\n'
            punct=lambda c: unicodedata.category(c)[0] in ('P','S')
            left=(not after.isspace() and (not punct(after) or before.isspace() or punct(before)))
            can_open=left and (ch=='*' or not (not before.isspace() and not punct(before)))
            if can_open:
                close=_find_em(src,i+length,ch,length)
                if close != -1:
                    # Link text brackets bind more tightly than emphasis. If
                    # this delimiter would close inside a bracketed link
                    # label, leave it for the link parser to consume.
                    if '[' in src[i+length:close[0]] and re.match(r'\]\s*(?:\(|\[)', src[close[0]+close[1]:]):
                        close = -1
                if close != -1:
                    use=2 if length>=2 and close[1]>=2 else 1
                    tag='strong' if use==2 else 'em'
                    inner=src[i+use:close[0]]
                    out.append('<'+tag+'>'+inline(inner,refs,depth+1)+'</'+tag+'>'); i=close[0]+use; continue
        out.append(_esc(src[i])); i+=1
    return ''.join(out)

def _closing_bracket(s,start):
    level=0; i=start
    while i<len(s):
        if s[i]=='\\': i+=2; continue
        if s[i]=='`':
            m=re.match(r'`+',s[i:]); e=s.find(m.group(),i+len(m.group()))
            if e>=0: i=e+len(m.group()); continue
        if s[i]=='[': level+=1
        elif s[i]==']':
            if level==0:return i
            level-=1
        i+=1
    return -1

def _plain_text(source, refs):
    """Extract rendered text for an image description, including nested links."""
    rendered = inline(source, refs, 1)
    rendered = re.sub(r'<br\s*/?>', '', rendered)
    rendered = re.sub(r'<img\b[^>]*\balt="([^"]*)"[^>]*/?>', r'\1', rendered)
    rendered = re.sub(r'<[^>]*>', '', rendered)
    return html.unescape(rendered)

def _valid_open_tag(tag):
    m=re.match(r'<'+_NAME, tag)
    if not m: return False
    i=m.end(); end=len(tag)-1
    while i<end:
        if tag[i] in ' \t\n': i+=1; continue
        if tag[i]=='/' and i==end-1: return True
        a=re.match(r'[A-Za-z_:][A-Za-z0-9_.:-]*',tag[i:end])
        if not a: return False
        i+=len(a.group())
        while i<end and tag[i] in ' \t\n': i+=1
        if i<end and tag[i]=='=':
            i+=1
            while i<end and tag[i] in ' \t\n': i+=1
            if i>=end: return False
            if tag[i] in "'\"":
                q=tag[i]; i+=1; j=tag.find(q,i,end)
                if j<0: return False
                i=j+1
            else:
                v=re.match(r'[^\s"\'=<>`]+',tag[i:end])
                if not v: return False
                i+=len(v.group())
        if i<end and tag[i] not in ' \t\n/': return False
    return True

def _inline_target(s,pos):
    i=pos+1
    while i<len(s) and s[i] in ' \t\n': i+=1
    if i<len(s) and s[i]=='<':
        e=i+1
        while e<len(s) and s[e]!='>' and s[e]!='\n': e+=1
        if e>=len(s) or s[e]!='>':return None
        dest=s[i+1:e]; i=e+1
    else:
        st=i; level=0
        while i<len(s):
            if s[i]=='\\':i+=2;continue
            if s[i]=='(':level+=1
            elif s[i]==')':
                if level==0:break
                level-=1
            elif s[i].isspace():break
            i+=1
        dest=s[st:i]
    while i<len(s) and s[i] in ' \t\n':i+=1
    title=None
    if i<len(s) and s[i] in '"\'(':
        close={"\"":"\"","'":"'",'(':')'}[s[i]]; j=i+1
        while j<len(s):
            if s[j]=='\\':j+=2;continue
            if s[j]==close:break
            if s[j]=='\n\n':return None
            j+=1
        if j>=len(s):return None
        title=s[i+1:j]; i=j+1
        while i<len(s) and s[i] in ' \t\n':i+=1
    if i<len(s) and s[i]==')':
        dest=re.sub(r'\\([!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])',r'\1',dest)
        title=re.sub(r'\\([!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])',r'\1',title) if title is not None else None
        return dest,title,i+1
    return None

def _find_em(s,start,ch,length):
    i=start
    while i<len(s):
        if s[i]=='\\':i+=2;continue
        if s[i]==ch:
            m=re.match(re.escape(ch)+'+',s[i:]); r=len(m.group())
            before=s[i-1] if i else '\n'; after=s[i+r] if i+r<len(s) else '\n'
            close_ok=not before.isspace() and (not unicodedata.category(before).startswith(('P','S')) or after.isspace() or unicodedata.category(after).startswith(('P','S')))
            if i>start and close_ok:
                if ch=='_' and i+r<len(s) and s[i+r].isalnum():
                    i+=r; continue
                return i,r
            i+=r
        else:i+=1
    return -1
