"""Parse Market Researcher long-form markdown (17 Oct 2026 format) into page dicts."""
import re
def _cells(l): return [x.strip() for x in l.strip().strip('|').split('|')]
def _table(lines):
    rows=[_cells(l) for l in lines if not re.fullmatch(r'\|?[\s\-:|]+\|?',l.strip())]
    return rows[0],rows[1:]
def parse(text,faq_page=False):
    meta={}; secs=[]; imgs=[]; faq=[]; cta=[]; cur=None; mode=None; tbl=[]; q=None
    def flush():
        nonlocal tbl
        if not tbl: return
        hdr,rows=_table(tbl); tbl=[]
        if mode=='img': imgs.extend((r[0],r[1]) for r in rows if len(r)>1)
        elif cur is not None: cur['flow'].append(['table',{'head':hdr if any(hdr) else None,'rows':rows}])
    for raw in text.split('\n'):
        s=raw.rstrip()
        if s.startswith('|'): tbl.append(s); continue
        flush()
        m=re.match(r'\*\*(Title tag|Meta description|H1|Lead)[^*]*:\*\*\s*(.*)',s)
        if m and not secs and mode is None:
            meta[{'Title tag':'title','Meta description':'description','H1':'h1'}.get(m.group(1),'lead')]=m.group(2).strip(); continue
        if s.startswith('## '):
            h=s[3:].strip()
            if h in('FAQ',): mode='faq'; cur=None; continue
            if h=='CTA': mode='cta'; cur=None; continue
            if h.startswith(('Images','Bilder')): mode='img'; cur=None; continue
            mode='sec'; h=re.sub(r'^\d+\.\s*','',h); cur={'h2':h,'flow':[],'faq':[]}; secs.append(cur); continue
        if s.startswith('### ') and mode=='sec':
            h=s[4:].strip()
            if faq_page: q=[h,'']; cur['faq'].append(q); continue
            cur['flow'].append(['h3',h]); continue
        if not s.strip() or s.startswith(('>','---','#','Target','Ziel')): continue
        if mode=='faq':
            m=re.match(r'\*\*(.+?)\*\*\s*(.*)$',s)
            if m: q=[m.group(1).strip(),'']; faq.append(q); continue
            if q is not None: q[1]=(q[1]+' '+s.strip()).strip()
            continue
        if mode=='cta': cta.append(s.strip()); continue
        if mode=='sec':
            if faq_page and cur['faq']: cur['faq'][-1][1]=(cur['faq'][-1][1]+' '+s.strip()).strip(); continue
            if s.startswith('- '):
                if cur['flow'] and cur['flow'][-1][0]=='ul': cur['flow'][-1][1].append(s[2:].strip())
                else: cur['flow'].append(['ul',[s[2:].strip()]])
            else: cur['flow'].append(['p',s.strip()])
    flush()
    return meta,secs,imgs,faq,cta
