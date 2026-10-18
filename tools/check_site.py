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
for u in re.findall(r'<loc>([^<]+)</loc>',open(f'{D}/sitemap.xml').read()):
    if not u.startswith(SITE+'/'): errs.append(('sitemap.xml','loc',u)); break
print(n,'pages'); [print(e) for e in errs[:60]]; print(len(errs),'issues')
