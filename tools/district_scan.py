"""List district names in <title>, <h1> and the first 60 chars of meta description of every built page."""
import re,glob,html,sys,json
DIST=re.compile(r'(?i)(?:\b(?:district|distrikt|distrito|distretto|dystrykt\w*|distrik|distriktet|daerah|quận|quan|arrondissement|округ\w*|район\w*|bölge\w*)\s*\d+|\d+\.?\s*(?:bölge\w*|-?й район|e arrondissement)|\bQ\.?\s?\d\b|第\s*[一二三四五六七八九十\d]+\s*[郡区區]|[一二三四五六七八九十\d]+\s*[郡区區](?!域)|\d+\s*(?:군|구)|เขต\s*\d+|المنطقة\s*\d+|الحي\s+\S+|डिस्ट्रिक्ट\s*\d+|ڈسٹرکٹ\s*\d+|ضلع\s*\d+|ਡਿਸਟ੍ਰਿਕਟ\s*\d+|डिस्ट्रिक्ट|ڈسٹرکٹ|ਡਿਸਟ੍ਰਿਕਟ)')
if __name__=='__main__':
    D=sys.argv[1] if len(sys.argv)>1 else 'docs'
    out=[]
    for f in sorted(glob.glob(f'{D}/*/**/index.html',recursive=True)):
        s=open(f).read()
        if 'noindex' in s: continue
        t=html.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
        h=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S); h=html.unescape(re.sub('<[^>]+>','',h.group(1))) if h else ''
        d=html.unescape(re.search(r'<meta name="description" content="([^"]*)"',s).group(1))
        for k,v in (('title',t),('h1',h),('desc60',d[:60])):
            m=DIST.search(v)
            if m: out.append((f,k,m.group(0),v if k!='desc60' else d))
    for o in out: print(json.dumps(o,ensure_ascii=False))
    print(len(out),'hits',file=sys.stderr)
