"""Static checks on docs/: forbidden wording, broken internal links/images, JSON-LD parse, SEO lengths, markdown leaks."""
import re,os,glob,json,html,sys
D=sys.argv[1] if len(sys.argv)>1 else 'docs'
_F=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','facts.json')))
B=_F.get('base_path','').rstrip('/'); SITE=_F['site_url'].rstrip('/')
bad=re.compile(r'(?i)\bvilla\b|\bpool\b|PS5|Hisense|Optoma|\bFPT\b|\bLG\b|Landmark 81|Agoda|Vrbo|halal|smart lock|smoke detector|Rauchmelder|first.aid|Erste.Hilfe|parking|Parkpl|three balcon|drei Balkon|password.protected|passwortgesch|exclusive for ASCON|Exklusiv für ASCON|luggage storage|Gepäckaufbewahrung|50 EUR|50 €|€50|card lock|Kartenschloss|fire.extinguisher|Feuerlöscher')
# KO/JA/ZH (+TH/MS/ID) equivalents: villa, parking, pool, safety devices, lyrics, minutes, Landmark 81, Phu My Hung, card/smart lock, pets, luggage, app password, EUR
bad2=re.compile(r'빌라|ヴィラ|別墅|别墅|주차|駐車|パーキング|停车|泊车|수영장|プール|泳池|游泳池|화재경보기|구급상자|소화기|비상구|비상등|火災警報器|救急箱|消火器|非常口|非常灯|烟雾报警器|急救箱|灭火器|安全出口|应急灯|가사|歌詞|歌词|'
 r'\d+\s*(?:분|分钟|分(?![子析配野別]))|랜드마크|ランドマーク|地标|푸미흥|フーミーフン|富美兴|카드키|カードキー|房卡|스마트 ?도어락|スマートロック|智能锁|반려동물|(?<!カー)ペット|宠物|짐 ?보관|行李寄存|'
 r'앱 비밀번호|アプリのパスワード|App 密码|유로|ユーロ|欧元|€|'
 r'วิลล่า|ที่จอดรถ|จอดรถ|สระว่ายน้ำ|\d+\s*นาที|ถังดับเพลิง|เครื่องตรวจจับควัน|ชุดปฐมพยาบาล|เนื้อเพลง|สัตว์เลี้ยง|ฝากกระเป๋า|'
 r'(?i:\bvila\b|tempat letak kereta|letak kereta|parkir|kolam renang|\d+\s*minit|\d+\s*menit|alat pemadam|pemadam api|pengesan asap|detektor asap|kotak pertolongan|P3K|lirik|haiwan peliharaan|hewan peliharaan|penyimpanan bagasi|simpan bagasi|kata laluan aplikasi|kata sandi aplikasi)'
 r'|(?i:biệt thự|bãi đỗ xe|chỗ đậu xe|đỗ xe|đậu xe|hồ bơi|bể bơi|\d+\s*phút|bình chữa cháy|báo khói|sơ cứu|lời bài hát|thú cưng|gửi hành lý|mật khẩu ứng dụng|'
 r'вилл[аыуеой]|парков|бассейн|\d+\s*мин|огнетушител|датчик[а-я]* дыма|аптечк|тексты? песен|домашн[а-я]+ животн|хранени[ея] багажа|пароль для приложения|'
 r'piscine|extincteur|détecteur de fumée|trousse de secours|paroles|animaux|bagagerie|consigne à bagages|'
 r'piscina|aparcamiento|estacionamiento|extintor|detector de humo|detector de fumaça|botiquín|letras de canciones|letras das músicas|mascota|animais de estimação|guarda-volumes|consigna de equipaje|'
 r'parcheggio|estintore|rilevatore di fumo|pronto soccorso|testi delle canzoni|animali domestici|deposito bagagli|'
 r'別墅|停車|泳池|寵物|煙霧偵測器|急救箱|滅火器|歌詞|\d+\s*分鐘|\bvilla\b|otopark|havuz|evcil|duman dedektör|yangın söndür|ilk yardım|şarkı söz|\d+\s*dakika|فيلا|موقف سيارات|مسبح|حيوانات أليفة|كاشف الدخان|طفاية|الإسعافات|كلمات الأغاني|\d+\s*دقيق|'
 r'\bwill[aię]\b|zwembad|parkeerplaats|parkering|songtekst|teksty piosenek|låttext|rookmelder|EHBO|brandblusser|czujnik dymu|apteczk|gaśnic|brandvarnare|första hjälpen|brandsläckare|huisdier|husdjur|'
 r'विला|पार्किंग|स्विमिंग|स्विमिंग पूल|\d+\s*मिनट|अग्निशामक|धुएँ|धुआँ|प्राथमिक चिकित्सा|लिरिक्स|गीत के बोल|पालतू|सामान रखने)')
import unicodedata
def width(x): return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in x)
CJKL=('/ko/','/ja/','/zh/','/zh-tw/')
errs=[];n=0
for f in glob.glob(f'{D}/**/*.html',recursive=True):
    s=open(f).read(); n+=1
    txt=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    plain=re.sub('<[^>]+>',' ',txt)
    if 'noindex' not in s and '"inLanguage"' not in s: errs.append((f,'inLanguage','missing'))
    for m in bad.finditer(plain): errs.append((f,'word',m.group(0)))
    for m in bad2.finditer(plain):
        if m.group(0).lower()=='vila' and '/sv/' in f: continue  # Swedish 'vila' = rest
        errs.append((f,'word',m.group(0)))
    for m in re.finditer(r'alt="([^"]*)"',s):
        if bad2.search(m.group(1)) or bad.search(m.group(1)): errs.append((f,'alt',m.group(1)))
    if 'hreflang="x-default"' not in s and 'noindex' not in s: errs.append((f,'hreflang','no x-default'))
    for m in re.finditer(r'(?:href|src)="('+re.escape(B)+r'/(?!/)[^"#?]*)',s):
        p=m.group(1)[len(B):]; fp=D+p+('index.html' if p.endswith('/') else '')
        if not os.path.exists(fp): errs.append((f,'link',p))
    for m in re.finditer(r'srcset="([^"]+)"',s):
        for u in m.group(1).split(','):
            p=u.strip().split()[0][len(B):]
            if not os.path.exists(D+p): errs.append((f,'img',p))
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(m.group(1).replace('<\\/','</'))
    t=re.search(r'<title>(.*?)</title>',s); d=re.search(r'<meta name="description" content="(.*?)"',s)
    cj=any(c in f for c in CJKL); L=(lambda x:width(x)) if cj else (lambda x:sum(1 for ch in x if unicodedata.category(ch)!='Mn')) if '/th/' in f else len; tl,dl=(64,160) if cj else (60,160)
    if t and L(html.unescape(t.group(1)))>tl: errs.append((f,'title',L(html.unescape(t.group(1)))))
    if d and L(html.unescape(d.group(1)))>dl: errs.append((f,'desc',L(html.unescape(d.group(1)))))
    # every meta description: at most 155 characters (Market Researcher / Website Ops, 19 Oct 2026)
    if d and len(html.unescape(d.group(1)))>155: errs.append((f,'desc>155',len(html.unescape(d.group(1)))))
    if '**' in txt or '[//]' in txt: errs.append((f,'markdown',''))
# laundry service 30 EUR per load must be stated in every published language
for d in sorted(glob.glob(f'{D}/*/index.html')):
    ld=os.path.dirname(d)
    if 'noindex' in open(d).read(): continue
    if not any('30 EUR' in open(f).read() for f in glob.glob(f'{ld}/**/*.html',recursive=True)): errs.append((ld,'laundry','no 30 EUR'))
# base URL / custom domain: canonicals on SITE, no leftovers of the old github.io project path
OLD=('4bzkfm6hb5-jpg.github.io/ascon-living-site','/ascon-living-site/')
for f in glob.glob(f'{D}/**/*',recursive=True):
    if not os.path.isfile(f) or not f.endswith(('.html','.xml','.txt','.css','.js','.json','.webmanifest')): continue
    s=open(f,errors='ignore').read()
    for o in OLD:
        if (B=='' or o!='/'+B.strip('/')+'/') and o in s: errs.append((f,'old-base',o))
    if f.endswith('.html'):
        for m in re.finditer(r'<link rel="(?:canonical|alternate)"[^>]*href="([^"]+)"',s):
            if not m.group(1).startswith(SITE+'/'): errs.append((f,'abs-url',m.group(1)))
from urllib.parse import urlparse
dom=urlparse(SITE).netloc
if not dom.endswith('.github.io'):
    cn=open(f'{D}/CNAME').read().strip() if os.path.exists(f'{D}/CNAME') else None
    if cn!=dom: errs.append((f'{D}/CNAME','cname',str(cn)))
if f'Sitemap: {SITE}/sitemap.xml' not in open(f'{D}/robots.txt').read(): errs.append((f'{D}/robots.txt','sitemap','wrong base'))
# IndexNow key file: docs/<key>.txt containing exactly the key
_k=_F.get('indexnow_key','')
if not re.fullmatch(r'[0-9a-f]{32}',_k) or not os.path.isfile(f'{D}/{_k}.txt') or open(f'{D}/{_k}.txt').read()!=_k: errs.append((D,'indexnow','key file missing/wrong'))
# /llms.txt: byte-identical to tools/llms.txt, every asconliving.com link must exist
_lt=os.path.join(os.path.dirname(os.path.abspath(__file__)),'llms.txt')
if not os.path.isfile(f'{D}/llms.txt') or open(f'{D}/llms.txt','rb').read()!=open(_lt,'rb').read(): errs.append((f'{D}/llms.txt','llms','missing or differs from tools/llms.txt'))
else:
    for u in re.findall(re.escape(SITE)+r'(/[^)\s]*)',open(_lt,encoding='utf-8').read()):
        if not os.path.exists(D+u+('index.html' if u.endswith('/') else '')): errs.append((f'{D}/llms.txt','llms-link',u))
for u in re.findall(r'<loc>([^<]+)</loc>',open(f'{D}/sitemap.xml').read()):
    if not u.startswith(SITE+'/'): errs.append(('sitemap.xml','loc',u)); break
# VacationRental JSON-LD (Search Console): >=8 own absolute image URLs, House, confirmed floorSize values only, no ratings/reviews/occupancy
for f in glob.glob(f'{D}/**/*.html',recursive=True):
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',open(f).read(),re.S):
        v=json.loads(b)
        if v.get('@type')!='VacationRental': continue
        im=v.get('image',[])
        if len(im)<8 or any(not u.startswith(SITE+'/assets/img/') or 'logo' in u or not os.path.exists(D+u[len(SITE):]) for u in im): errs.append((f,'vr-image',len(im)))
        if v.get('additionalType')!='House': errs.append((f,'vr-type',v.get('additionalType')))
        t=json.dumps({k:x for k,x in v.items() if k!='containsPlace'})  # occupancy allowed on EntirePlace (= sum of bedrooms) and per bedroom
        cp=v.get('containsPlace',{}); _o=(cp.get('occupancy') or {}).get('value')
        if _o!=sum((r.get('occupancy') or {}).get('value',0) for r in cp.get('containsPlace',[])): errs.append((f,'vr-occ-total',_o))
        for k in ('aggregateRating','"review','occupancy','minValue','maxValue'):  # occupancy only on EntirePlace + bedrooms
            if k in json.dumps(v) if k!='occupancy' else k in t: errs.append((f,'vr-field',k))
        if v.get('identifier')!=_F['identifier']: errs.append((f,'vr-id',v.get('identifier')))
        for r in v.get('containsPlace',{}).get('containsPlace',[]):
            o=r.get('occupancy')
            if o and not ('bedroom' in r.get('name','').lower() and o.get('value')==2): errs.append((f,'vr-occ',r.get('name')))
        for r in v.get('containsPlace',{}).get('containsPlace',[]):
            fs=r.get('floorSize')
            if fs and not (isinstance(fs.get('value'),(int,float)) and fs.get('unitCode')=='MTK'): errs.append((f,'vr-floor',r.get('name')))
# LCP hero/cover: fetchpriority=high, not lazy, and a matching <link rel=preload> in <head> (same srcset/sizes -> single download)
for f in glob.glob(f'{D}/*/**/index.html',recursive=True):
    s=open(f).read()
    if 'noindex' in s: continue
    m=re.search(r'<img [^>]*fetchpriority="high"[^>]*>',s)
    if not m: continue
    im=m.group(0)
    if 'loading="lazy"' in im: errs.append((f,'lcp','lazy'))
    g=lambda t,a: (re.search(a+r'="([^"]*)"',t) or [None,None])[1]
    head=s.split('</head>')[0]; pl=re.search(r'<link rel="preload" as="image"[^>]*>',head)
    if not pl or g(pl.group(0),'imagesrcset')!=g(im,'srcset') or g(pl.group(0),'imagesizes')!=g(im,'sizes') or g(pl.group(0),'href')!=g(im,'src'): errs.append((f,'lcp','preload mismatch'))
# no district names in <title>, <h1> or first 60 chars of meta description
import importlib.util as _ilu
_sp=_ilu.spec_from_file_location('district_scan',os.path.join(os.path.dirname(os.path.abspath(__file__)),'district_scan.py'))
_ds=_ilu.module_from_spec(_sp); _sp.loader.exec_module(_ds)
# run as library: collect hits
_hits=[]
import html as _html
for f in sorted(glob.glob(f'{D}/*/**/index.html',recursive=True)):
    s=open(f).read()
    if 'noindex' in s: continue
    t=_html.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
    h=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S); h=_html.unescape(re.sub('<[^>]+>','',h.group(1))) if h else ''
    d=_html.unescape(re.search(r'<meta name="description" content="([^"]*)"',s).group(1))
    for k,v in (('title',t),('h1',h),('desc',d)):
        m=_ds.DIST.search(v)
        if m: errs.append((f,'district',f'{k}:{m.group(0)}'))
print(n,'pages'); [print(e) for e in errs[:60]]; print(len(errs),'issues')
