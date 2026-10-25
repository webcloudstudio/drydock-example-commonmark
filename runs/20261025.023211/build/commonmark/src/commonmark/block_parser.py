"""Block parsing and document-wide reference collection."""
import html
import re
from .model import Document

REF = re.compile(r'^ {0,3}\[([^\]]+)\]:[ \t]*(<[^>]*>|[^\s]+)(?:[ \t]+(?:"([^\"]*)"|\'([^\']*)\'|\(([^)]*)\)))?[ \t]*$')
FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')
LIST = re.compile(r'^( {0,3})([-+*]|[0-9]{1,9}[.)])(?:[ \t]+(.*)|[ \t]*)$')
HR = re.compile(r'^ {0,3}(?:(?:\*[ \t]*){3,}|(?:-[ \t]*){3,}|(?:_[ \t]*){3,})$')
ATX = re.compile(r'^ {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$')

def _refkey(s): return ' '.join(s.split()).casefold()

def _node(kind, **kw): return {'type': kind, **kw}

def parse_blocks(markdown: str) -> Document:
    source=markdown.replace('\r\n','\n').replace('\r','\n').replace('\x00','\ufffd')
    lines=source.split('\n')
    if lines and lines[-1]=='': lines.pop()
    doc=Document(); doc.blocks=_parse(lines, doc.references)
    return doc

def _parse(lines, refs):
    out=[]; i=0; n=len(lines)
    while i<n:
        line=lines[i]
        if not line.strip(): i+=1; continue
        m=REF.match(line)
        if m:
            label,dest,*titles=m.groups(); title=next((x for x in titles if x is not None),None)
            refs.setdefault(_refkey(label), (dest[1:-1] if dest.startswith('<') else dest, title)); i+=1; continue
        if line.startswith('>') or re.match(r'^ {0,3}>',line):
            q=[]
            while i<n and (re.match(r'^ {0,3}>',lines[i]) or
                            (lines[i].strip() and q and q[-1].strip() and
                             len(q[-1])-len(q[-1].lstrip(' ')) < 4 and
                             not re.match(r'^ {0,3}(?:`{3,}|~{3,})', q[-1]) and
                             not re.match(r'^ {0,3}(?:#|`{3,}|~{3,}|[-+*] |[0-9]{1,9}[.)] |>)(?:.*)$', lines[i])
                             and not HR.match(lines[i])
                             )):
                x=lines[i]
                if re.match(r'^ {0,3}>',x): x=re.sub(r'^ {0,3}> ?', '',x, count=1)
                q.append(x); i+=1
            out.append(_node('quote', children=_parse(q,refs))); continue
        fm=FENCE.match(line)
        if fm and not (fm.group(1).startswith('`') and '`' in fm.group(2)):
            fence,info=fm.groups(); ch=fence[0]; j=i+1; body=[]
            while j<n and not re.match(r'^ {0,3}'+re.escape(ch)+'{'+str(len(fence))+r',}[ \t]*$',lines[j]): body.append(re.sub(r'^ {0,'+str(len(line)-len(line.lstrip()))+'}', '',lines[j])); j+=1
            lang=info.strip().split()[0] if info.strip() else ''
            out.append(_node('code', text='\n'.join(body)+ ('\n' if body else ''), lang=lang)); i=min(j+1,n); continue
        if len(line)-len(line.lstrip(' '))>=4:
            body=[]
            while i<n and (lines[i].startswith('    ') or not lines[i].strip()):
                body.append(lines[i][4:] if lines[i].startswith('    ') else ''); i+=1
            while body and not body[-1]: body.pop()
            out.append(_node('code',text='\n'.join(body)+('\n' if body else ''),lang='')); continue
        if HR.match(line): out.append(_node('hr')); i+=1; continue
        am=ATX.match(line)
        if am:
            text=(am.group(2) or '')
            # A closing hash run is recognized only when preceded by whitespace.
            if re.fullmatch(r'#+[ \t]*', text): text=''
            else: text=re.sub(r'[ \t]+#+[ \t]*$','',text)
            text=text.strip(' \t'); out.append(_node('heading',level=len(am.group(1)),text=text)); i+=1; continue
        lm=LIST.match(line)
        if HR.match(line):
            out.append(_node('hr')); i+=1; continue
        if lm:
            indent,mark,first=lm.groups(); ordered=mark[0].isdigit(); delim=mark[-1]; items=[]; loose=False; start=int(mark[:-1]) if ordered else 1
            while i<n:
                if HR.match(lines[i]): break
                mm=LIST.match(lines[i])
                if not mm or mm.group(2)[-1]!=delim or mm.group(2)[0].isdigit()!=ordered: break
                content=mm.group(3) or ''
                marker_end=len(mm.group(1))+len(mm.group(2))
                raw_spaces=len(lines[i][marker_end:])-len(lines[i][marker_end:].lstrip(' \t'))
                if raw_spaces >= 2:
                    # The first separator is structural.  For a first block
                    # that is indented code, the remaining indentation is
                    # measured from the list item's content edge.
                    content=lines[i][marker_end+raw_spaces:]
                i+=1
                # When the first block is indented code, the list marker's
                # single required separator is structural; four additional
                # columns belong to the code block and are removed by its
                # normal indentation rule.
                item=[content] if content else []
                while i<n:
                    # A thematic break is never a list item or list continuation.
                    if HR.match(lines[i]): break
                    if not lines[i].strip():
                        if i+1<n and LIST.match(lines[i+1]) and LIST.match(lines[i+1]).group(2)[-1]==delim: loose=True; i+=1; break
                        if i+1<n and (lines[i+1].startswith('  ') or lines[i+1].startswith('    ')): loose=True; item.append(''); i+=1; continue
                        break
                    if LIST.match(lines[i]) and len(LIST.match(lines[i]).group(1))<=len(indent): break
                    if len(lines[i])-len(lines[i].lstrip(' ')) >= 4 and item:
                        item.append(lines[i][4:])
                    elif lines[i].startswith('  '): item.append(lines[i][min(2,len(lines[i])-len(lines[i].lstrip())):])
                    else: item.append(lines[i])
                    i+=1
                items.append(_parse(item,refs))
                if i<n and not lines[i].strip(): i+=1
            out.append(_node('list',ordered=ordered,start=start,loose=loose,items=items,delimiter=delim)); continue
        # HTML block types 1-7. Types 1-5 have explicit terminators, type 6
        # ends at a blank line, and type 7 is a complete standalone tag.
        h = line.lstrip(' ')
        kind = 0
        endmark = None
        if len(line)-len(h) <= 3:
            if re.match(r'(?i)^<(pre|script|style|textarea)(?:[ \t>]|$)',h): kind=1; endmark=r'</(?:pre|script|style|textarea)\s*>'
            elif h.startswith('<!--'): kind=2; endmark='-->'
            elif h.startswith('<?'): kind=3; endmark=r'\?>'
            elif re.match(r'^<![A-Za-z]',h): kind=4; endmark='>'
            elif h.startswith('<![CDATA['): kind=5; endmark=r']]>'
            elif re.match(r'(?i)^</?(?:address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem|nav|noframes|ol|optgroup|option|p|param|search|section|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul)(?:[ \t]|$|>|/>)',h): kind=6
            elif _standalone_tag(h): kind=7
        if kind:
            body=[]
            while i<n:
                cur=lines[i]
                if kind in (6,7) and not cur.strip(): break
                body.append(cur); i+=1
                if kind in (1,2,3,4,5) and re.search(endmark,cur,re.I if kind==1 else 0): break
                if kind in (6,7) and (i>=n or not lines[i].strip()): break
            out.append(_node('html',text='\n'.join(body)+'\n')); continue
        para=[line.lstrip(' \t')]; i+=1
        while i<n and lines[i].strip():
            if re.match(r'^ {0,3}(?:=+|-+)[ \t]*$',lines[i]):
                # An unmarked line can lazily continue a quoted paragraph;
                # an underline then belongs to that paragraph too.
                if out and out[-1]['type'] == 'quote' and para:
                    para.append(lines[i].lstrip(' \t')); i+=1
                    if i<n and re.match(r'^ {0,3}(?:=+|-+)[ \t]*$', lines[i]):
                        para.append(lines[i].lstrip(' \t')); i+=1
                    out[-1]['children'].append(_node('paragraph', text='\n'.join(para).strip(' \t')))
                    para=[]; break
                out.append(_node('heading',level=1 if '=' in lines[i] else 2,text='\n'.join(para).strip(' \t')))
                i+=1; para=[]; break
            if REF.match(lines[i]) or HR.match(lines[i]) or ATX.match(lines[i]) or FENCE.match(lines[i]) or re.match(r'^ {0,3}>',lines[i]): break
            lm_next=LIST.match(lines[i])
            if lm_next:
                marker=lm_next.group(2)
                if marker[0].isdigit():
                    if marker[:-1]=='1' and lm_next.group(3): break
                elif lm_next.group(3): break
            # HTML block types 1-6 can interrupt a paragraph.
            stripped=lines[i].lstrip(' ')
            html_interrupt = (
                re.match(r'(?i)^<(pre|script|style|textarea)(?:[ \t>]|$)', stripped)
                or stripped.startswith(('<!--', '<?', '<![CDATA['))
                or re.match(r'^<![A-Za-z]', stripped)
                or re.match(r'(?i)^</?(?:address|article|aside|base|basefont|blockquote|body|caption|center|col|colgroup|dd|details|dialog|dir|div|dl|dt|fieldset|figcaption|figure|footer|form|frame|frameset|h[1-6]|head|header|hr|html|iframe|legend|li|link|main|menu|menuitem|nav|noframes|ol|optgroup|option|p|param|search|section|summary|table|tbody|td|tfoot|th|thead|title|tr|track|ul)(?:[ \t]|$|>|/>)', stripped)
            )
            if len(lines[i])-len(stripped)<=3 and html_interrupt: break
            para.append(lines[i].lstrip(' \t')); i+=1
        # definitions at beginning of a closed paragraph are collected
        joined='\n'.join(para).strip(' \t')
        if para: out.append(_node('paragraph',text=joined))
    return out

def _standalone_tag(s):
    s=s.rstrip(' \t')
    if re.fullmatch(r'</[A-Za-z][A-Za-z0-9-]*[ \t]*>',s): return True
    m=re.match(r'<([A-Za-z][A-Za-z0-9-]*)',s)
    if not m or not s.endswith('>'): return False
    i=m.end(); end=len(s)-1
    # Attribute productions begin with whitespace.  In particular, a colon
    # immediately after the tag name is not an attribute separator.
    if i < end and s[i] not in ' \t/': return False
    while i<end:
        if s[i] in ' \t\n': i+=1; continue
        if s[i]=='/' and i==end-1: return True
        a=re.match(r'[A-Za-z_:][A-Za-z0-9_.:-]*',s[i:end])
        if not a: return False
        i+=len(a.group())
        while i<end and s[i] in ' \t\n': i+=1
        if i<end and s[i]=='=':
            i+=1
            while i<end and s[i] in ' \t\n': i+=1
            if i>=end: return False
            if s[i] in "'\"":
                q=s[i]; j=s.find(q,i+1,end)
                if j<0: return False
                i=j+1
            else:
                v=re.match(r'[^\s"\'=<>`]+',s[i:end])
                if not v:return False
                i+=len(v.group())
        if i<end and s[i] not in ' \t/': return False
    return True
