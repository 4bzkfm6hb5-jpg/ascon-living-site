"""Static checks on docs/: forbidden wording, broken internal links/images, JSON-LD parse, SEO lengths, markdown leaks."""
import re,os,glob,json,html,sys
D=sys.argv[1] if len(sys.argv)>1 else 'docs'; B='/ascon-living-site'
bad=re.compile(r'(?i)\bvilla\b|\bpool\b|PS5|Hisense|Optoma|\bFPT\b|\bLG\b|Landmark 81|Agoda|Vrbo|halal|smart lock|smoke detector|Rauchmelder|first.aid|Erste.Hilfe|parking|Parkpl|three balcon|drei Balkon|password.protected|passwortgesch|exclusive for ASCON|Exklusiv für ASCON|luggage storage|Gepäckaufbewahrung|50 EUR|50 €|€50|card lock|Kartenschloss|fire.extinguisher|Feuerlöscher')
errs=[];n=0
for f in glob.glob(f'{D}/**/*.html',recursive=True):
    s=open(f).read(); n+=1
    txt=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    for m in bad.finditer(re.sub('<[^>]+>',' ',txt)): errs.append((f,'word',m.group(0)))
    for m in re.finditer(r'(?:href|src)="(/ascon-living-site/[^"#?]*)',s):
        p=m.group(1)[len(B):]; fp=D+p+('index.html' if p.endswith('/') else '')
        if not os.path.exists(fp): errs.append((f,'link',p))
    for m in re.finditer(r'srcset="([^"]+)"',s):
        for u in m.group(1).split(','):
            p=u.strip().split()[0][len(B):]
            if not os.path.exists(D+p): errs.append((f,'img',p))
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m.group(1).replace('<\\/','</'))
    t=re.search(r'<title>(.*?)</title>',s); d=re.search(r'<meta name="description" content="(.*?)"',s)
    if t and len(html.unescape(t.group(1)))>60: errs.append((f,'title',len(html.unescape(t.group(1)))))
    if d and len(html.unescape(d.group(1)))>160: errs.append((f,'desc',len(html.unescape(d.group(1)))))
    if '**' in txt or '[//]' in txt: errs.append((f,'markdown',''))
print(n,'pages'); [print(e) for e in errs[:60]]; print(len(errs),'issues')
