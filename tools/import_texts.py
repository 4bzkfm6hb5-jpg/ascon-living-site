"""Import Market Researcher texts (/workspace/ascon-texts/<lang>/*.md) into content/<lang>.json."""
import json,re,sys
SRC='/workspace/ascon-texts'
def rows(lines):
    out=[]
    for l in lines:
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        if all(re.fullmatch(r'-*',x) for x in c): continue
        out.append(c)
    return out[1:]  # drop header
def parse(text):
    """returns meta dict and list of sections (each: h2,p,ul,note,imgs,table,cards,raw)"""
    meta={}; secs=[]; cur=None; tbl=[]
    def flush_tbl():
        nonlocal tbl
        if tbl and cur is not None:
            hdr=[x.strip().lower() for x in tbl[0].strip().strip('|').split('|')]
            r=rows(tbl)
            if hdr[0] in('image','bild'): cur.setdefault('imgs',[]).extend([x[0],x[1]] for x in r)
            elif hdr[0] in('card','karte'): cur['cards']=r
            else: cur['table']=r
        tbl=[]
    for line in text.split('\n'):
        s=line.rstrip()
        if s.startswith('|'): tbl.append(s); continue
        flush_tbl()
        m=re.match(r'\*\*(Title tag|Meta description|H1|Lead[^:]*):\*\*\s*(.*)',s)
        if m and cur is None:
            k={'Title tag':'title','Meta description':'description','H1':'h1'}.get(m.group(1),'lead'); meta[k]=m.group(2).strip(); continue
        if re.match(r'#{2,3} ',s):
            if re.match(r'## [AB]\. ',s): secs.append({'_page':s}); cur=None; continue
            cur={'_hdr':s}; secs.append(cur); continue
        if cur is None:
            continue
        m=re.match(r'\*\*H2:\*\*\s*(.*)',s)
        if m: cur['h2']=m.group(1).strip(); continue
        m=re.match(r'\*\*(Note|Hinweis)[^*]*:\*\*\s*(.*)',s)
        if m: cur['note']=m.group(2).strip(); continue
        if re.match(r'\*\*(CTA)',s): cur['cta']=True; continue
        if s.startswith('**') or s.startswith('>') or s.startswith('---') or s.startswith('(') or not s.strip(): continue
        if s.startswith('- '): cur.setdefault('ul',[]).append(s[2:].strip()); continue
        cur.setdefault('p',[]).append(s.strip())
    flush_tbl()
    return meta,secs
def split_pages(text):
    """travel-guide has A./B. pages"""
    parts=re.split(r'\n(?=## [AB]\. )',text)
    return parts[1:] if len(parts)>1 else [text]
