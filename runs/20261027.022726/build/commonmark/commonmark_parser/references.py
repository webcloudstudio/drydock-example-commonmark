import re
from .inline import decode_escapes_and_entities

def normalize_label(label: str) -> str:
    return re.sub(r'[ \t\r\n]+', ' ', label.strip(' \t\r\n')).casefold()

def _title(text: str, pos: int):
    if pos >= len(text) or text[pos] not in '"\'(': return None
    op = text[pos]; cl = ')' if op == '(' else op; out=[]; i=pos+1
    while i < len(text):
        if text[i] == '\\' and i+1 < len(text):
            if text[i+1] not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~": out.append('\\')
            out.append(text[i+1]); i += 2; continue
        if text[i] == cl: return ''.join(out), i+1
        if text[i] == '\n' and op == '(': return None
        out.append(text[i]); i += 1
    return None

def _definition(text: str):
    m = re.match(r'^ {0,3}\[', text)
    if not m: return None
    i=m.end(); label=[]
    while i<len(text):
        if text[i]=='\\' and i+1<len(text): label.extend((text[i],text[i+1])); i+=2; continue
        if text[i]==']': break
        if text[i]=='[': return None
        label.append(text[i]); i+=1
    if i>=len(text) or not ''.join(label).strip(): return None
    i+=1
    if i>=len(text) or text[i]!=':': return None
    i+=1
    label=''.join(label)
    while i<len(text) and text[i] in ' \t': i+=1
    # Up to one newline may separate the colon from the destination.
    if i < len(text) and text[i] == '\n': i += 1
    if i >= len(text): return None
    if text[i] == '<':
        j=i+1; dest=[]
        while j<len(text) and text[j] != '>':
            if text[j]=='\\' and j+1<len(text):
                if text[j+1] not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~": dest.append('\\')
                dest.append(text[j+1]); j+=2; continue
            if text[j] in '<\n': return None
            dest.append(text[j]); j+=1
        if j==len(text): return None
        destination=''.join(dest); i=j+1
    else:
        dest=[]; depth=0; j=i
        while j<len(text):
            c=text[j]
            if c=='\\' and j+1<len(text):
                if text[j+1] not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~': dest.append('\\')
                dest.append(text[j+1]); j+=2; continue
            if c=='(':
                depth+=1
                if depth>32:return None
            elif c==')':
                if not depth: break
                depth-=1
            if c.isspace() and depth==0: break
            dest.append(c); j+=1
        if not dest:return None
        destination=''.join(dest); i=j
    had_space = i < len(text) and text[i] in ' \t\n'
    while i<len(text) and text[i] in ' \t':i+=1
    if i<len(text) and text[i]=='\n':
        i += 1
        if i >= len(text) or text[i] not in '"\'(':
            # The newline belongs to the following block line when no title
            # begins there.
            i += 1
            return normalize_label(label), decode_escapes_and_entities(destination), None, i
        had_space = True
    title_start = i
    title=None; parsed=_title(text,i) if had_space else None
    if parsed:
        title,i=parsed
        if '\n\n' in title: return None
        while i<len(text) and text[i] in ' \t':i+=1
    # A definition ends at the end of its physical line. Consecutive
    # definitions are parsed by collect_definitions one line at a time.
    if i<len(text) and text[i]=='\n': i+=1
    elif i<len(text) and text[i] not in ' \t':
        return None
    return normalize_label(label), decode_escapes_and_entities(destination), decode_escapes_and_entities(title) if title is not None else None, i

def collect_definitions(text: str, definitions: dict) -> str:
    # A block may begin with several definitions. Parse from the start of
    # the remaining text so a definition may span its label/destination/title.
    lines = text.splitlines(keepends=True)
    # A definition cannot interrupt an open paragraph. A block parser calls
    # this function when closing the paragraph, so only definitions at its
    # beginning are eligible; subsequent lines remain paragraph text.
    kept = []
    i = 0
    paragraph_started = False
    while i < len(lines):
        if paragraph_started:
            kept.extend(lines[i:])
            break
        parsed = _definition(''.join(lines[i:]))
        if parsed:
            label, destination, title, end = parsed
            if label not in definitions:
                definitions[label] = (destination, title)
            consumed = ''.join(lines[i:])[:end].count('\n')
            i += max(1, consumed)
        else:
            kept.append(lines[i]); i += 1
            if lines[i-1].strip():
                paragraph_started = True
    return ''.join(kept)
