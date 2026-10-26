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
    # Preserve tabs in code contents; indentation-sensitive productions
    # expand tabs as needed by their own column calculations.
    source='\n'.join(_expand_indent(line) for line in source.split('\n'))
    lines=source.split('\n')
    if lines and lines[-1]=='': lines.pop()
    doc=Document(); doc.blocks=_parse(lines, doc.references)
    return doc

def _expand_indent(line):
    # Expand tabs in structural whitespace after quote/list markers as well
    # as at the start of a line, using the current visual column.
    out=[]; col=0; structural=True
    for ch in line:
        if structural and ch=='\t':
            count=4-col%4; out.append(' '*count); col+=count
        else:
            out.append(ch); col+=1
            if ch not in ' >-*+0123456789.)': structural=False
    return ''.join(out)

def _parse_reference(lines, start):
    """Parse one reference definition, allowing its destination/title to wrap."""
    if start >= len(lines): return None
    first=lines[start]
    m=re.match(r'^ {0,3}(\[)',first)
    if not m: return None
    # Labels can span lines and may contain escaped brackets.
    source=''; close=-1; j=start
    while j<len(lines) and j-start<8:
        source += ('\n' if j>start else '') + lines[j].lstrip(' ')
        k=0
        while k<len(source):
            if source[k]=='\\': k+=2; continue
            if source[k]==']': close=k; break
            k+=1
        if close>=0: break
        j+=1
    if close<0 or close==1 or close-1>999 or close+1>=len(source) or source[close+1]!=':': return None
    label=source[:close+1]
    tail=source[close+2:]
    if not label[1:-1].strip(' \t\n'): return None
    parts=[tail.strip(' \t')]
    consumed=j-start+1
    # A destination or title may occupy following indented lines. A blank
    # line terminates the candidate.
    while consumed < 8 and start+consumed < len(lines) and lines[start+consumed].strip():
        nxt=lines[start+consumed]
        prev=' '.join(parts)
        # A following quoted line continues only an unfinished title or a
        # definition with no destination. Otherwise it starts ordinary text.
        unfinished=bool(re.search(r'\s["\'(][^"\')]*$', prev))
        separated_title = bool(re.match(r'^\s*["\'(].*["\')][ \t]*$', nxt))
        if not (not prev.strip() or unfinished or separated_title): break
        trial=parts+[nxt.strip(' \t')]
        trial_text='\n'.join(trial)
        # A quoted line is a title only when the whole definition remains valid.
        if separated_title:
            check=re.match(r'^(<(?:(?:\\.)|[^<>\\\n])*>|(?:\\.|[^\s])*)[ \t\n]+(?:"((?:\\.|[^"])*)"|\'((?:\\.|[^\'])*)\'|\(((?:\\.|[^)])*)\))[ \t\n]*$','\n'.join(p for p in trial if p))
            if not check: break
        parts=trial; consumed+=1
    candidate='\n'.join(p for p in parts if p)
    m=re.match(r'^(<(?:(?:\\.)|[^<>\\\n])*>|(?:\\.|[^\s])*)(?:[ \t\n]+(?:"((?:\\.|[^"])*)"|\'((?:\\.|[^\'])*)\'|\(((?:\\.|[^)])*)\)))?[ \t\n]*$',candidate)
    if not m or not m.group(1): return None
    dest=m.group(1)
    if dest.startswith('<'):
        if not dest.endswith('>'): return None
        dest=dest[1:-1]
    title=next((x for x in m.groups()[1:] if x is not None),None)
    unescape=lambda s: re.sub(r'\\([!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])',r'\1',s) if s is not None else None
    return _refkey(label[1:-1]), unescape(dest), unescape(title), max(consumed, j-start+1)

def _parse(lines, refs):
    out=[]; i=0; n=len(lines)
    while i<n:
        line=lines[i]
        if not line.strip(): i+=1; continue
        parsed_ref=_parse_reference(lines, i)
        if parsed_ref:
            key,dest,title,consumed=parsed_ref
            refs.setdefault(key,(dest,title)); i+=consumed; continue
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
            # An unmarked lazy continuation line cannot supply a setext
            # underline inside a quote; preserve it as paragraph text.
            if len(q) >= 2 and re.match(r'^ {0,3}(?:=+|-+)[ \t]*$', q[-1]):
                q[-1] = '\\' + q[-1].lstrip(' ')
            out.append(_node('quote', children=_parse(q,refs))); continue
        fm=FENCE.match(line)
        if fm and not (fm.group(1).startswith('`') and '`' in fm.group(2)):
            fence,info=fm.groups(); ch=fence[0]; j=i+1; body=[]
            while j<n and not re.match(r'^ {0,3}'+re.escape(ch)+'{'+str(len(fence))+r',}[ \t]*$',lines[j]): body.append(re.sub(r'^ {0,'+str(len(line)-len(line.lstrip()))+'}', '',lines[j])); j+=1
            lang=info.strip().split()[0] if info.strip() else ''
            lang=re.sub(r'\\([!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~])',r'\1',lang)
            lang=html.unescape(lang)
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
                # Up to four columns after the marker establish the content
                # edge. Extra indentation is part of the first block (code).
                content_indent=len(mm.group(1))+len(mm.group(2))+min(raw_spaces,4)
                if raw_spaces > 4:
                    content=lines[i][marker_end+1:]
                    content_indent=marker_end+1
                elif raw_spaces:
                    content=lines[i][marker_end+raw_spaces:]
                i+=1
                # When the first block is indented code, the list marker's
                # single required separator is structural; four additional
                # columns belong to the code block and are removed by its
                # normal indentation rule.
                item=[content] if content else []
                while i<n:
                    # A thematic break is never a list item or list continuation.
                    # A thematic break interrupts a list item even when its
                    # spelling could also underline a setext heading.  The
                    # underline is only setext when it belongs to a paragraph
                    # in the same block container.
                    if HR.match(lines[i]):
                        break
                    if not lines[i].strip():
                        blank_end=i
                        while blank_end<n and not lines[blank_end].strip(): blank_end+=1
                        if blank_end<n and LIST.match(lines[blank_end]) and LIST.match(lines[blank_end]).group(2)[-1]==delim and LIST.match(lines[blank_end]).group(2)[0].isdigit()==ordered and len(LIST.match(lines[blank_end]).group(1)) <= 3:
                            # A blank between nested list items loosens that
                            # nested list only. It loosens this list only when
                            # the next marker is at this item's list level.
                            if len(LIST.match(lines[blank_end]).group(1)) <= len(indent):
                                loose=True
                            i=blank_end
                            break
                        # A blank line before a properly indented continuation
                        # separates blocks in this item.  It is not part of a
                        # nested list's looseness unless the next block is itself
                        # a direct continuation of this item.
                        if item and blank_end<n and len(lines[blank_end])-len(lines[blank_end].lstrip(' ')) >= content_indent:
                            # Preserve all intervening blank lines for literal
                            # code blocks; they also make direct item blocks loose.
                            open_fences = 0
                            for prior in item:
                                fm_prior = FENCE.match(prior)
                                if fm_prior:
                                    open_fences = 0 if open_fences else 1
                            if not open_fences:
                                loose=True
                            item.extend([''] * (blank_end-i)); i=blank_end; continue
                        break
                    next_list=LIST.match(lines[i])
                    if next_list and (len(next_list.group(1)) < content_indent or next_list.group(2)[-1]!=delim or next_list.group(2)[0].isdigit()!=ordered) : break
                    leading=len(lines[i])-len(lines[i].lstrip(' '))
                    if leading >= content_indent and item:
                        # For list items beginning with a blank marker line,
                        # the marker contributes one structural column; the
                        # following four columns are the code block indent.
                        # Subsequent lines are measured from the content
                        # column; for a first paragraph, this is the exact
                        # marker plus separator width (not the raw source
                        # indentation of the list marker).
                        trim = content_indent
                        if first and raw_spaces > 4:
                            # Rule 2: an item beginning with indented code
                            # has one structural separator column, then the
                            # normal four columns of code indentation.
                            trim = marker_end + 5
                        item.append(lines[i][min(trim, len(lines[i])):])
                    elif item and lines[i].strip() and leading < content_indent and not re.match(r'^ {0,3}(?:[-+*]|[0-9]{1,9}[.)])(?:[ \t]|$)',lines[i]):
                        item.append(lines[i].lstrip(' \t'))
                    else: item.append(lines[i])
                    i+=1
                items.append(_parse(item,refs))
                if i<n and not lines[i].strip():
                    while i<n and not lines[i].strip(): i+=1
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
                    out[-1]['children'].append(_node('paragraph', text='\n'.join(para).strip(' \t') + '\n' + lines[i-1].lstrip(' \t')))
                    para=[]; break
                out.append(_node('heading',level=1 if '=' in lines[i] else 2,text='\n'.join(para).strip(' \t')))
                i+=1; para=[]; break
            if HR.match(lines[i]) or ATX.match(lines[i]) or FENCE.match(lines[i]) or re.match(r'^ {0,3}>',lines[i]): break
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
