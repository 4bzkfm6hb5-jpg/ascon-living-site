#!/usr/bin/env python3
"""Static site builder. Add content/<code>.json to publish a language; nothing else needed."""
import json, os, glob, html, shutil, datetime, re
ROOT=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(ROOT,'docs')
F=json.load(open(f'{ROOT}/facts.json'))
# Single settings for where the site lives (facts.json): absolute origin for canonical/hreflang/og/JSON-LD/sitemap,
# and the root-relative path prefix for links/assets ('' on the custom domain; was '/ascon-living-site' on github.io).
SITE=F['site_url'].rstrip('/'); BASE=F.get('base_path','').rstrip('/')
from urllib.parse import urlparse as _up
DOMAIN=_up(SITE).netloc  # docs/CNAME for GitHub Pages custom domain (not written for *.github.io)
PAGES=[('home',''),('house','house/'),('rooftop','rooftop/'),('families','families/'),('groups','groups/'),
('location','location/'),('booking','booking/'),('faq','faq/'),('rules','house-rules/'),('guide','guide/'),
('guide-family','guide/hcmc-with-family/'),('guide-airport','guide/airport-transfer/'),('guide-app','guide/ascon-guide-app/'),
('guide-rain','guide/saigon-rainy-day/'),('guide-day','guide/saigon-one-day/'),('guide-party','guide/saigon-with-family/'),('guide-food','guide/saigon-street-food/'),
# City notes use guest-note-* slugs so they do not collide with the EN/DE/KO/JA guides on the same topics.
('guide-note-rain','guide/guest-note-rain-day/'),('guide-note-day','guide/guest-note-one-day/'),
('guide-note-group','guide/guest-note-together/'),('guide-note-food','guide/guest-note-street-eats/'),
('guide-sights','guide/saigon-sights/'),('guide-markets','guide/saigon-markets/'),('guide-coffee','guide/saigon-coffee/'),
('guide-river','guide/saigon-river/'),('guide-evenings','guide/saigon-evenings/'),('guide-daytrips','guide/mekong-cu-chi/'),
('guide-weather','guide/saigon-weather/'),('guide-arrival','guide/from-the-airport/'),('guide-practical','guide/money-sim-apps/'),
('guide-traffic','guide/traffic-safety/'),
('guide-ko-family','guide/ko-family-journey/'),('guide-ko-course','guide/ko-independent-route/'),('guide-ko-sing','guide/ko-noraebang/'),
('guide-ja-family','guide/ja-family-journey/'),('guide-ja-course','guide/ja-model-course/'),('guide-ja-long','guide/ja-long-stay/'),
('audience','whole-house/'),
('travel-guide','travel-guide/'),
('imprint','imprint/'),('privacy','privacy/')]
# Room detail pages: published per language only once content/<code>.json has pages.<id> (no placeholders)
ROOMS=[('room-entertainment','house/karaoke-entertainment/'),('room-living','house/living-room/'),('room-kitchen','house/kitchen/'),('room-master','house/master-bedroom/'),
('room-bedroom-2','house/bedroom-2/'),('room-bedroom-3','house/bedroom-3/'),('room-bathrooms','house/bathrooms/'),('room-hallway','house/hallway/'),('room-outside','house/outside/')]
PAGES+=ROOMS
SLUG=dict(PAGES)
if len(SLUG)!=len(PAGES) or len(set(SLUG.values()))!=len(PAGES): raise SystemExit('duplicate page id or slug')
IMG=json.load(open(f'{ROOT}/tools/images.json'))
LANGS=json.load(open(f'{ROOT}/languages.json'))
_CSS_RAW=open(f'{ROOT}/tools/style.css').read()
if '/*@deferred*/' not in _CSS_RAW: raise SystemExit('style.css missing /*@deferred*/ marker')
CRIT,REST=_CSS_RAW.split('/*@deferred*/',1)
PUB=[l for l in LANGS if os.path.exists(f'{ROOT}/content/{l[0]}.json')]
C={l[0]:json.load(open(f'{ROOT}/content/{l[0]}.json')) for l in PUB}
import sys as _s; _s.path.insert(0,f'{ROOT}/tools'); import laundry as _laundry
import house_alts
FONTS=json.load(open(f'{ROOT}/tools/fonts/metrics.json')) if os.path.exists(f'{ROOT}/tools/fonts/metrics.json') else {}
C={k:_laundry.apply(k,v) for k,v in C.items()}
# home-page SEO wording overrides (tools/seo_overrides.json): survive content re-imports
_SEO=json.load(open(f'{ROOT}/tools/seo_overrides.json'))
for _l,_o in _SEO.items():
    if _l.startswith('_') or _l not in C: continue
    _h=C[_l]['pages']['home']
    _h.update(_o.get('set',{}))
    for _k,(_old,_new) in _o.get('replace',{}).items():
        if _old not in _h[_k]: raise SystemExit(f'seo_overrides: {_l} {_k} text not found: {_old}')
        if _new not in _h[_k]: _h[_k]=_h[_k].replace(_old,_new,1)
    for _k,_add in _o.get('append',{}).items():
        if _add.strip() not in _h[_k]: _h[_k]=_h[_k].rstrip()+_add
for _l,_rules in _SEO.get('_rewrite',{}).items():
    if _l not in C: continue
    for _pg in C[_l]['pages'].values():
        for _k in ('title','h1','description'):
            if isinstance(_pg.get(_k),str):
                for _old,_new in _rules: _pg[_k]=_pg[_k].replace(_old,_new)
for _l,_pp in _SEO.get('_pages',{}).items():
    for _pid,_v in _pp.items():
        if _l in C and _pid in C[_l]['pages']: C[_l]['pages'][_pid].update(_v)
# '_body' {lang:{page_id:[[old,new],...]}}: wording edits anywhere in a page (body, captions, FAQ), applied last; old text must exist
def _sub(o,a,b):
    if isinstance(o,str): return o.replace(a,b)
    if isinstance(o,list): return [_sub(x,a,b) for x in o]
    if isinstance(o,dict): return {k:_sub(v,a,b) for k,v in o.items()}
    return o
for _l,_pp in _SEO.get('_body',{}).items():
    for _pid,_rules in _pp.items():
        if _l not in C or _pid not in C[_l]['pages']: continue
        for _old,_new in _rules:
            if _old not in json.dumps(C[_l]['pages'][_pid],ensure_ascii=False): raise SystemExit(f'seo_overrides _body: {_l}/{_pid} text not found: {_old}')
            C[_l]['pages'][_pid]=_sub(C[_l]['pages'][_pid],_old,_new)
# Extra short guides (KO, JA, EN, DE). Cards are attached after the city hub is built.
_GP=json.load(open(f'{ROOT}/tools/guide_pages.json'))
for _l,_pp in _GP.items():
    if _l not in C: continue
    C[_l]['pages'].update({k:v for k,v in _pp.items() if not str(k).startswith('_')})
import seo_market as _seo_market
_seo_market.apply(C)
import site_copy as _copy
import front
import landings
PAGES.extend(landings.PAGE_SLUGS)
SLUG=dict(PAGES)
# Landing slugs may repeat across languages (ko and ja both use hochiminh-group-stay/).
# Each id is published in only one language, so the files do not collide.
if len(SLUG)!=len(PAGES): raise SystemExit('duplicate page id')
# Language-switcher flags: self-hosted SVGs from flag-icons (MIT, tools/flags/LICENSE), copied to docs/assets/flags on every build.
# Not emoji: Windows does not render emoji flags. pa is Gurmukhi (Indian Punjab) -> IN; ur -> PK.
FLAG={'en':'gb','de':'de','vi':'vn','zh':'cn','zh-tw':'tw','ko':'kr','ja':'jp','th':'th','ms':'my','id':'id','ru':'ru','fr':'fr','es':'es','pt':'br','it':'it','hi':'in','ur':'pk','pa':'in','nl':'nl','pl':'pl','sv':'se','tr':'tr','ar':'sa'}
def flag(code,lazy=True):
    f=FLAG.get(code)
    return f'<img class="flag" src="{BASE}/assets/flags/{f}.svg" width="20" height="15" alt=""'+(' loading="lazy"' if lazy else '')+' decoding="async">' if f else ''
  # laundry service 30 EUR per load in every language
def HAS(pid): return [x for x in PUB if pid in C[x[0]]['pages']]
def xdef(pid):
    # x-default must be a language that publishes the page. English when it does.
    hs=HAS(pid)
    return next((x[0] for x in hs if x[0]=='en'), hs[0][0])
def _merge_city():
    # Long-form city guides and hubs for en/de/ko/ja (content/city_guides.py).
    import importlib.util as _iu
    _p=f'{ROOT}/content/city_guides.py'
    if not os.path.exists(_p): return
    _spec=_iu.spec_from_file_location('city_guides',_p)
    _mod=_iu.module_from_spec(_spec); _spec.loader.exec_module(_mod)
    for code,pack in _mod.GUIDES.items():
        if code not in C: continue
        C[code]['ui'].update(pack.get('ui',{}))
        C[code]['pages'].update(pack.get('pages',{}))
        g=C[code]['pages'].get('guide')
        if not g or not pack.get('hub_cards'): continue
        for s in g['sections']:
            s.pop('cards',None)
        g['sections']=[s for s in g['sections'] if s]
        g['sections'].insert(1 if g['sections'] else 0, {'h2':pack['hub_h2'],'cards':pack['hub_cards']})
        g['toc']=True
        g['book']=True
        g['related']=pack.get('hub_related',['home'])
        for pid,rel in pack.get('also',{}).items():
            if pid in C[code]['pages']:
                C[code]['pages'][pid]['book']=True
                C[code]['pages'][pid]['related']=rel
def _append_market_cards():
    # PR 23 guide-index cards. Re-applied after the city hub replaces earlier card lists.
    for lang,pp in _GP.items():
        if lang not in C or 'guide' not in C[lang]['pages']: continue
        h2=pp.get('_heading')
        pages={k:v for k,v in pp.items() if not str(k).startswith('_') and k in C[lang]['pages']}
        if not h2 or not pages: continue
        cards=[[v['card_title'],k,v['card_text']] for k,v in pages.items()]
        secs=C[lang]['pages']['guide']['sections']
        if any(s.get('h2')==h2 and s.get('cards')==cards for s in secs): continue
        secs.append({'h2':h2,'cards':cards})
TODAY=datetime.date.today().isoformat()
WA_SVG='<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 0 0 2.1-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.2-.3-.3-.7-.5z"/></svg>'
def url(code,pid): return f'{BASE}/{code}/{SLUG[pid]}'
def sub(s,code): return s.replace('{L}',f'{BASE}/{code}/').replace('{phone_e164}',F['phone_e164']).replace('{phone}',F['phone']).replace('{email}',F['email']).replace('{guide}',F['guide'])
def stem(name):
    return IMG[name].get('file') or house_alts.SLUG.get(name) or name
def alt_of(name, code, fallback):
    row=house_alts.ALTS.get(name)
    alt=(row.get(code) or row.get('en') or fallback) if row else fallback
    if code=='ko': alt=alt.replace('가라오케','노래방')
    return alt
def pic(name,alt,eager=False,sizes='(min-width:900px) 380px, 100vw', code='en'):
    m=IMG[name]; ws=m['widths']; src=f'{BASE}/assets/img/{stem(name)}-'
    webp=', '.join(f'{src}{w}.webp {w}w' for w in ws)
    avif=', '.join(f'{src}{w}.avif {w}w' for w in ws)
    w=ws[-1]; h=round(m['h']*w/m['w']); mid=ws[min(1,len(ws)-1)]
    attrs='fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    # aspect-ratio locks the box for lazy images; the hero is absolutely positioned and sized by CSS
    ratio='' if eager else f' style="aspect-ratio:{w}/{h}"'
    alt=alt_of(name, code, alt)
    return (f'<picture><source type="image/avif" srcset="{avif}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
            f'<img src="{src}{mid}.webp" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt)}" {attrs}{ratio}></picture>')
def preload(name,sizes):
    # <head> preload for the LCP image. Chrome fetches the AVIF candidate; the <img> keeps a WebP fallback.
    m=IMG[name]; ws=m['widths']; src=f'{BASE}/assets/img/{stem(name)}-'
    mid=ws[min(1,len(ws)-1)]
    ss=', '.join(f'{src}{w}.avif {w}w' for w in ws)
    return f'<link rel="preload" as="image" href="{src}{mid}.avif" imagesrcset="{ss}" imagesizes="{sizes}" type="image/avif" fetchpriority="high">'
def parse_rules(css):
    rules=[]; i=0; n=len(css)
    while i<n:
        while i<n and css[i].isspace(): i+=1
        if i>=n: break
        if css.startswith('/*', i):
            j=css.find('*/', i)
            i=n if j<0 else j+2
            continue
        start=i; j=css.find('{', i)
        if j<0: break
        depth=0; k=j
        while k<n:
            if css[k]=='{': depth+=1
            elif css[k]=='}':
                depth-=1
                if depth==0:
                    rules.append(css[start:k+1].strip()); i=k+1; break
            k+=1
        else:
            break
    return rules
def _part_used(sel, html, lang, direction):
    langs=re.findall(r'\[lang=([^\]]+)\]', sel)
    if langs and not any(x==lang for x in langs): return False
    if '[dir=rtl]' in sel and direction!='rtl': return False
    for c in re.findall(r'\.([A-Za-z_][\w-]*)', sel):
        if not re.search(r'class="[^"]*\b%s\b'%re.escape(c), html): return False
    return True
def _rule_used(rule, html, lang, direction):
    head, body=rule.split('{', 1)
    if head.strip().startswith('@media'):
        kept=[r for r in (_rule_used(x, html, lang, direction) for x in parse_rules(body[:-1])) if r]
        return (head.strip()+'{'+''.join(kept)+'}') if kept else ''
    parts=[p.strip() for p in head.split(',') if p.strip()]
    return rule if any(_part_used(p, html, lang, direction) for p in parts) else ''
def filter_css(css, html, lang, direction):
    return ''.join(r for r in (_rule_used(x, html, lang, direction) for x in parse_rules(css)) if r)
def minify_css(s):
    s=re.sub(r'/\*.*?\*/','',s,flags=re.S)
    s=re.sub(r'\s+',' ',s).strip()
    s=re.sub(r'\s*([{}:;,])\s*', r'\1', s)
    return s.replace(';}','}')
def minify_html(s):
    return re.sub(r'>\s+<','><',s)
def font_css(spec):
    fam=spec['family']; fb=fam+' Fallback'
    asc,desc,gap=spec['ascent'],spec['descent'],spec['lineGap']
    locs=','.join(f'local("{x}")' for x in spec['locals'])
    out=[]
    for weight, fn in (('400', spec['files']['400']), ('600', spec['files']['700']), ('700', spec['files']['700'])):
        out.append(f'@font-face{{font-family:"{fam}";font-style:normal;font-weight:{weight};font-display:swap;src:url({BASE}/assets/fonts/{fn}) format("woff2")}}')
        out.append(f'@font-face{{font-family:"{fb}";font-style:normal;font-weight:{weight};font-display:swap;src:{locs};ascent-override:{asc};descent-override:{desc};line-gap-override:{gap};size-adjust:100%}}')
    return ''.join(out)
# Agoda is not a live booking link. Owner rule: only Airbnb (1789707041970520479)
# and Trip.com (136163015) until the owner supplies a real Agoda URL and approves it.
def cta(u, code):
    air=(F['airbnb'], u['book_airbnb'])
    trip=(F['trip'], u['book_trip'])
    pair=[trip, air] if code in front.TRIP_FIRST else [air, trip]
    books=''.join(f'<a class="btn primary{" second" if n else ""}" href="{href}" rel="noopener">{html.escape(label)}</a>' for n,(href,label) in enumerate(pair))
    contacts=(f'<a class="btn channel wa" href="{F["wa"]}" rel="noopener">{html.escape(u["whatsapp"])}</a>'
              f'<a class="btn channel zl" href="{F["zalo"]}" rel="noopener">{html.escape(u["zalo"])}</a>')
    reach=(f'<p class="reach"><a href="tel:{F["phone_e164"]}">{F["phone"]}</a>'
           f' · <a href="mailto:{F["email"]}">{F["email"]}</a></p>')
    return (f'<p class="kicker">{html.escape(front.KICKER.get(code, front.KICKER["en"]))}</p>'
            f'<div class="book-primary">{books}</div><div class="channels">{contacts}</div>{reach}')
def price_line(code):
    # Nightly rate is not published. This link goes to the booking page, which has WhatsApp, Zalo, phone and email.
    label=html.escape(front.PRICE.get(code, front.PRICE['en']))
    return f'<p class="price"><a href="{url(code,"booking")}">{label}</a></p>'
PHOTO_SIZES='(min-width:900px) 560px, 100vw'
def hero_still(code):
    key=front.HERO_PHOTO
    alt=alt_of(key, code, 'Rooftop terrace looking over the river to the city skyline')
    return f'<div class="hero-still">{pic(key, alt, True, "100vw", code)}</div>'
def aria(code):
    return front.ARIA.get(code, front.ARIA['en'])
def carousel(keys, code, kind, lead=False):
    prev,nxt,_close=aria(code)
    slides=[]
    for i,key in enumerate(keys):
        alt=alt_of(key, code, 'ASCON LIVING')
        eager=(kind=='hero' or lead) and i==0
        sizes='100vw' if kind=='hero' else PHOTO_SIZES
        slides.append(f'<div class="car-slide" data-index="{i}"><figure>{pic(key, alt, eager, sizes, code)}<figcaption>{html.escape(alt)}</figcaption></figure></div>')
    thumbs=''
    if kind=='gallery':
        bits=[]
        for i,key in enumerate(keys):
            m=IMG[key]; w=m['widths'][0]
            bits.append(f'<button type="button" data-go="{i}" aria-label="{i+1}"><img src="{BASE}/assets/img/{stem(key)}-{w}.webp" alt="" loading="lazy" decoding="async"></button>')
        thumbs=f'<div class="car-thumbs">{"".join(bits)}</div>'
    auto=' data-auto="5500"' if kind=='hero' else ''
    light=' data-lightbox="1"' if kind in ('gallery','mini') else ''
    count=f'<p class="car-count">1 / {len(keys)}</p>' if kind=='gallery' else ''
    return (f'<div class="carousel {kind}" data-carousel{auto}{light} tabindex="0">'
            f'<div class="car-viewport"><div class="car-track">{"".join(slides)}</div></div>'
            f'<button type="button" class="car-btn prev" aria-label="{html.escape(prev)}"></button>'
            f'<button type="button" class="car-btn next" aria-label="{html.escape(nxt)}"></button>'
            f'<div class="car-dots"></div>{count}{thumbs}</div>')
_ICON={
 'house':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-5v-6H10v6H5a1 1 0 0 1-1-1z"/></svg>',
 'bed':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18V8m0 6h18v4M3 14h10a4 4 0 0 1 4-4h4"/></svg>',
 'size':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8V4h4M20 8V4h-4M4 16v4h4M20 16v4h-4"/></svg>',
 'roof':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 14 12 6l9 8M6 13v7h12v-7"/></svg>',
 'river':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8c2 0 2 2 4 2s2-2 4-2 2 2 4 2 2-2 4-2M3 14c2 0 2 2 4 2s2-2 4-2 2 2 4 2 2-2 4-2"/></svg>',
}
def facts_html(code):
    rows=front.FACTS.get(code, front.FACTS['en'])
    icons=('house','bed','size','roof','river')
    cells=''.join(f'<li class="fact">{_ICON[icons[i]]}<strong>{html.escape(a)}</strong><span>{html.escape(b)}</span></li>' for i,(a,b) in enumerate(rows))
    return f'<ul class="facts">{cells}</ul>'
def reviews_html(code):
    h=front.REV_H.get(code, front.REV_H['en'])
    cards=[]
    for item in front.REVIEWS:
        text, lang=front.review_quote(code, item)
        lang_attr=f' lang="{lang}"' if lang!=code else ''
        cards.append(
            f'<article class="review-card"><p class="stars" aria-label="5/5">★★★★★</p>'
            f'<p class="review-quote"{lang_attr}>{html.escape(text)}</p>'
            f'<p class="review-meta">{html.escape(item["name"])} · Google</p></article>')
    return (f'<section class="reviews" id="guest-reviews"><h2>{html.escape(h)}</h2>'
            f'<div class="review-grid">{"".join(cards)}</div></section>')
def gallery_html(code):
    h=front.GALLERY_H.get(code, front.GALLERY_H['en'])
    keys=[k for k in front.gallery_keys() if k in IMG]
    first,rest=keys[:12],keys[12:]
    more=f'<details class="pg-more"><summary>+{len(rest)}</summary><div class="pgrid">{_pg(rest,code)}</div></details>' if rest else ''
    return f'<section class="gallery-block" id="gallery" data-pgrid><h2>{html.escape(h)}</h2><div class="pgrid">{_pg(first,code)}</div>{more}</section>'
def lightbox(code):
    _prev,nxt,close=aria(code)
    return (f'<div class="lb" hidden><button type="button" class="lb-x" aria-label="{html.escape(close)}">×</button>'
            f'<button type="button" class="lb-prev car-btn prev" aria-label="{html.escape(_prev)}"></button>'
            f'<figure><img alt=""><figcaption></figcaption></figure>'
            f'<button type="button" class="lb-next car-btn next" aria-label="{html.escape(nxt)}"></button></div>')
def is_guide(pid): return pid=='guide' or pid=='travel-guide' or str(pid).startswith('guide-')
def related_block(code,pid,c):
    ids=[p for p,_s in PAGES if is_guide(p) and p in c['pages']]
    i=ids.index(pid) if pid in ids else 0
    sibs=(ids[i+1:]+ids[:i])[:3]
    items=[f'<li><a href="{url(code,p)}">{html.escape(c["pages"][p]["h1"])}</a></li>' for p in sibs]
    items.append(f'<li><a href="{url(code,"home")}">{html.escape(c["pages"]["home"]["h1"])}</a></li>')
    h2=_copy.MORE.get(code,_copy.MORE['en'])
    return f'<section class="related"><h2>{html.escape(h2)}</h2><ul class="chk">{"".join(items)}</ul></section>'
def book_box(code,c):
    sent=_copy.BOOK.get(code,_copy.BOOK['en'])
    label=dict(c['nav']).get('booking',c['ui'].get('book_airbnb',''))
    return f'<aside class="bookbox"><p>{html.escape(sent)}</p><p><a class="btn b1" href="{url(code,"booking")}">{html.escape(label)}</a></p></aside>'
def section(s,code,u,guide=False,skip_imgs=False):
    o=[]
    if 'h2' in s:
        _ida=f' id="{s["_id"]}"' if s.get('_id') else ''
        o.append(f'<h2{_ida}>{html.escape(s["h2"])}</h2>')
    if 'note' in s: o.append(f'<p class="note">{sub(s["note"],code)}</p>')
    for p in s.get('p',[]): o.append(f'<p>{sub(p,code)}</p>')
    for kind,val in s.get('flow',[]):
        if kind=='p': o.append(f'<p>{sub(val,code)}</p>')
        elif kind=='h3': o.append(f'<h3>{html.escape(val)}</h3>')
        elif kind=='ul': o.append('<ul class="chk">'+''.join(f'<li>{sub(x,code)}</li>' for x in val)+'</ul>')
        elif kind=='table': o.append('<div class="tbl"><table>'+(('<thead><tr>'+''.join(f'<th scope="col">{html.escape(h)}</th>' for h in val['head'])+'</tr></thead>') if val.get('head') else '')+'<tbody>'+''.join('<tr>'+f'<th scope="row">{sub(r[0],code)}</th>'+''.join(f'<td>{sub(x,code)}</td>' for x in r[1:])+'</tr>' for r in val['rows'])+'</tbody></table></div>')
    for bl in s.get('blocks',[]):
        if bl.get('h3'): o.append(f'<h3>{html.escape(bl["h3"])}</h3>')
        for p in bl.get('p',[]): o.append(f'<p>{sub(p,code)}</p>')
    if 'ul' in s: o.append('<ul class="chk">'+''.join(f'<li>{sub(x,code)}</li>' for x in s['ul'])+'</ul>')
    if 'table' in s: o.append('<div class="tbl"><table>'+''.join(f'<tr><th scope="row">{html.escape(k)}</th><td>{sub(v,code)}</td></tr>' for k,v in s['table'])+'</table></div>'+(f'<p class="note">{html.escape(s["table_note"])}</p>' if s.get('table_note') else ''))
    if 'imgs' in s and not skip_imgs:
        keys=[(i[0]+'@'+code if i[0]+'@'+code in IMG else i[0]) for i in s['imgs']]
        if len(keys)>=2: o.append(carousel(keys, code, 'mini'))
        else: o.append('<div class="grid">'+''.join(f'<figure>{pic(i[0]+"@"+code if i[0]+"@"+code in IMG else i[0],i[1],code=code)}<figcaption>{html.escape(i[2] if len(i)>2 and i[2] else i[1])}</figcaption></figure>' for i in s['imgs'])+'</div>')
    if 'faq' in s: o.append('<div class="faq">'+''.join(f'<details><summary><h2 class="q">{html.escape(q)}</h2></summary><p>{sub(a,code)}</p></details>' for q,a in s['faq'])+'</div>')
    if 'cards' in s: o.append('<div class="cards">'+''.join(f'<div class="card"><a href="{url(code,pid)}">{html.escape(t)}</a><p>{html.escape(d)}</p></div>' for t,pid,d in s['cards'] if pid in C[code]['pages'])+'</div>')
    if s.get('cta') and not guide: o.append(cta(u, code))
    return '<section>'+''.join(o)+'</section>'
def lodging_images():
    # VacationRental.image: absolute URLs of our own house photos only (facts.json jsonld_images; no logos, no blurred/excluded shots).
    # floorSize only where confirmed (facts.json jsonld_rooms[].m2); postalCode only when facts.json postal_code is set.
    out=[]
    for i in F['jsonld_images']:
        w=max(IMG[i]['widths']); fn=f'{stem(i)}-{w}.webp'; p=f'{OUT}/assets/img/{fn}'
        if not os.path.exists(p): raise SystemExit(f'jsonld image missing: {p}')
        out.append(SITE+f'/assets/img/{fn}')
    if len(out)<8: raise SystemExit('VacationRental needs at least 8 images')
    return out
def lodging(code,c):
    g=F.get('geo') or {}; geo=all(isinstance(g.get(k),(int,float)) for k in ('latitude','longitude'))
    return {"@context":"https://schema.org","@type":"VacationRental","@id":SITE+'/#lodging',"identifier":F['identifier'],"name":F['name'],
      "url":SITE+f'/{code}/',"additionalType":"House","image":lodging_images(),"logo":SITE+'/assets/img/logo-mark.png',
      "description":c['pages']['home']['description'],"telephone":F['phone_e164'],"email":F['email'],
      "address":{"@type":"PostalAddress","streetAddress":F['street'],"addressLocality":"Tân Hưng","addressRegion":F['region'],"addressCountry":F['country'],**({"postalCode":F['postal_code']} if F.get('postal_code') else {})},
      **({"geo":{"@type":"GeoCoordinates","latitude":g['latitude'],"longitude":g['longitude']},"latitude":g['latitude'],"longitude":g['longitude']} if geo else {}),
      "checkinTime":F['checkin'],"checkoutTime":F['checkout'],
      "knowsLanguage":F['languages'],"sameAs":[F['airbnb'],F['trip']],
      "contactPoint":[{"@type":"ContactPoint","contactType":"reservations","telephone":F['phone_e164'],"email":F['email'],"url":F['wa']},{"@type":"ContactPoint","contactType":"reservations","telephone":F['phone_e164'],"url":F['zalo']}],
      "amenityFeature":[{"@type":"LocationFeatureSpecification","name":a,"value":True} for a in F['amenities']],
      "containsPlace":{"@type":"Accommodation","additionalType":"EntirePlace","occupancy":{"@type":"QuantitativeValue","value":F['occupancy_total']},"name":F['name'],"numberOfRooms":F['rooms'],"numberOfBedrooms":F['rooms'],
        "numberOfBathroomsTotal":F['bathrooms_full']+F['bathrooms_partial'],"numberOfFullBathrooms":F['bathrooms_full'],"numberOfPartialBathrooms":F['bathrooms_partial'],
        "bed":[{"@type":"BedDetails","numberOfBeds":1,"typeOfBed":"180×200 cm"},{"@type":"BedDetails","numberOfBeds":2,"typeOfBed":"160×200 cm"}],
        "containsPlace":[dict({"@type":r['type'],"name":r['name']},**({"floorSize":{"@type":"QuantitativeValue","value":r['m2'],"unitCode":"MTK"}} if r.get('m2') else {}),**({"occupancy":{"@type":"QuantitativeValue","value":r['occupancy']}} if r.get('occupancy') else {})) for r in F['jsonld_rooms']],
        "amenityFeature":[{"@type":"LocationFeatureSpecification","name":"Self check-in via keypad; the outer gate uses a key","value":True}]}}
def legal(code):
    # imprint/privacy fall back to English where a language has no legal pages (lang attribute marks the switch)
    o=[]
    for k in ('imprint','privacy'):
        if k in C[code]['pages']: o.append(f'<a href="{url(code,k)}">{C[code]["pages"][k]["h1"]}</a>')
        else: o.append(f'<a href="{url("en",k)}" hreflang="en" lang="en">{C["en"]["pages"][k]["h1"]}</a>')
    return '<br>'.join(o)
import unicodedata
CJK={'ko','ja','zh','zh-tw'}
def width(s): return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in s)
def glen(s): return sum(1 for ch in s if unicodedata.category(ch)!='Mn')  # Thai: combining vowel/tone marks are not counted
def seo_bad(code,p,suffix):
    # Latin scripts: characters (title<=60, desc<=160). CJK: display width, full-width chars count 2 (title<=64 ~ 32 CJK chars, desc<=160 ~ 80 CJK chars)
    t=p['title']+suffix; d=p['description']
    if code in CJK: return width(t)>64 or width(d)>160 or len(d)>155
    if code=='th': return glen(t)>60 or glen(d)>160 or len(d)>155
    return len(t)>60 or len(d)>160 or len(d)>155
NAV_GROUPS=[('house',['house','rooftop']),('families',['families','groups']),('location',['location','guide']),('travel-guide',[]),('faq',['faq','rules'])]
BURGER='<input type="checkbox" id="navt" class="navt" aria-hidden="true" tabindex="-1"><label for="navt" class="burger" aria-label="Menu"><span></span></label>'
def nav_html(code, cur=''):
    lab=dict(C[code]['nav'])
    def a(k, cls=''):
        return f'<a href="{url(code,k)}"'+(f' class="{cls}"' if cls else '')+(' aria-current="page"' if k==cur else '')+f'>{html.escape(lab[k])}</a>'
    o=[a('home')] if 'home' in lab else []
    for head,kids in NAV_GROUPS:
        if head not in lab: continue
        kids=[k for k in kids if k in lab and k!=head]
        if not kids: o.append(a(head)); continue
        on=' on' if cur in [head]+kids else ''
        o.append(f'<div class="dd{on}">'+a(head)+'<div class="ddm">'+''.join(a(k) for k in kids)+'</div></div>')
    if 'booking' in lab: o.append(a('booking','navbook'))
    return ''.join(o)
_AICON={
 'ps':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9h12a3 3 0 0 1 3 3v3a2 2 0 0 1-3.6 1.2L16 14H8l-1.4 2.2A2 2 0 0 1 3 15v-3a3 3 0 0 1 3-3zM8 11v2M7 12h2M16 11.5h.01M18 12.5h.01"/></svg>',
 'mic':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a3 3 0 0 1 3 3v5a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v4M9 21h6"/></svg>',
 'game':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
 'film':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="14" height="12" rx="2"/><path d="m17 10 4-2v8l-4-2"/></svg>',
 'bbq':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10h16a8 8 0 0 1-16 0zM8 17l-2 4M16 17l2 4M9 3c1 1 1 2 0 3M12 2c1 1 1 3 0 4M15 3c1 1 1 2 0 3"/></svg>',
}
BBQ={'en':'Rooftop BBQ','de':'Grill auf der Dachterrasse','vi':'BBQ trên sân thượng','zh':'屋顶烧烤','zh-tw':'屋頂烤肉','hi':'छत पर BBQ','es':'Barbacoa en la azotea','ar':'شواء على السطح','fr':'Barbecue sur le toit','pt':'Churrasco no terraço','ru':'Барбекю на крыше','ur':'چھت پر BBQ','id':'BBQ di rooftop','ja':'屋上BBQ','ko':'루프탑 바비큐','pa':'ਛੱਤ ਤੇ BBQ','th':'บาร์บีคิวบนดาดฟ้า','ms':'BBQ di bumbung','it':'Barbecue in terrazza','nl':'BBQ op het dakterras','tr':'Çatıda barbekü','pl':'Grill na dachu','sv':'Grill på takterrassen'}
def amen_html(code):
    g=lambda d: d.get(code, d['en'])
    fx=front.FACTS.get(code, front.FACTS['en'])
    items=[('ps','PS5',g(front.PS)),('mic',g(front.KARAOKE),''),('game',g(front.GAMING),''),('film',g(front.CINEMA),'Netflix'),('bbq',g(BBQ),''),('river',fx[4][0],fx[4][1])]
    cells=''.join(f'<li>{(_AICON.get(k) or _ICON[k])}<strong>{html.escape(a)}</strong>'+(f'<span>{html.escape(b)}</span>' if b and b!=a else '')+'</li>' for k,a,b in items)
    return f'<section class="amen"><h2>{html.escape(g(front.ENT_H2))}</h2><ul class="amen-grid">{cells}</ul></section>'
def _pg(keys, code, eager_n=0):
    o=[]
    for key in keys:
        alt=alt_of(key, code, 'ASCON LIVING')
        full=f'{BASE}/assets/img/{stem(key)}-{max(IMG[key]["widths"])}.webp'
        o.append(f'<figure class="pg-item" data-full="{full}" tabindex="0">{pic(key, alt, False, "(min-width:900px) 380px, 50vw", code)}<figcaption>{html.escape(alt)}</figcaption></figure>')
    return ''.join(o)

def page(l,pid):
    code,hl,lname,dirn,font=l; c=C[code]; u=c['ui']; p=c['pages'][pid]
    title=p['title']+c.get('title_suffix',''); canon=SITE+f'/{code}/{SLUG[pid]}'
    _alt=landings.hreflang_html(pid, SITE)
    alts=_alt if _alt else ''.join(f'<link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/{SLUG[pid]}">' for x in HAS(pid))+f'<link rel="alternate" hreflang="x-default" href="{SITE}/{xdef(pid)}/{SLUG[pid]}">'
    fontlink=''; fontfaces=''
    if font and font in FONTS:
        spec=FONTS[font]; fam=spec['family']
        fontfaces=font_css(spec)
        fontlink=''.join(f'<link rel="preload" href="{BASE}/assets/fonts/{fn}" as="font" type="font/woff2" crossorigin fetchpriority="low">' for fn in dict.fromkeys(spec['files'].values()))
    elif font:
        fontlink=f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={font.replace(" ","+")}:wght@400;600&display=swap" media="print" onload="this.media=&#39;all&#39;">'
    ld=[]
    if pid in ('home','house','booking','location'): ld.append(lodging(code,c))
    crumbs=[{"@type":"ListItem","position":1,"name":u['home'],"item":SITE+f'/{code}/'}]
    if pid!='home':
        if pid.startswith('room-'): crumbs.append({"@type":"ListItem","position":2,"name":c['pages']['house']['h1'],"item":SITE+f'/{code}/house/'})
        if pid.startswith('guide-'): crumbs.append({"@type":"ListItem","position":2,"name":c['pages']['guide']['h1'],"item":SITE+f'/{code}/guide/'})
        crumbs.append({"@type":"ListItem","position":len(crumbs)+1,"name":p['h1'],"item":canon})
    ld.append({"@context":"https://schema.org","@type":"WebPage","name":title,"description":p['description'],"url":canon,"inLanguage":hl,"isPartOf":{"@type":"WebSite","name":F['name'],"url":SITE+'/'}})
    ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs})
    if pid=='guide' or pid.startswith('guide-'): ld.append({"@context":"https://schema.org","@type":"Article","headline":p['h1'],"description":p['description'],"inLanguage":hl,"image":SITE+'/assets/img/og.jpg',"datePublished":"2026-10-22","dateModified":TODAY,"author":{"@type":"Organization","name":"ASCON LIVING"},"mainEntityOfPage":canon})
    if any(s.get('faq') for s in p['sections']): ld.append({"@context":"https://schema.org","@type":"FAQPage","inLanguage":hl,"mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for s in p['sections'] for q,a in s.get('faq',[])]})
    ldh=''.join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False).replace('</','<\\/')+'</script>' for x in ld)
    navcur=pid if pid in dict(c['nav']) else ('guide' if pid.startswith('guide') else 'house' if pid.startswith('room-') else '')
    _labels=dict(c['nav'])
    nav=nav_html(code, navcur if navcur else ('home' if pid=='home' else ''))
    def _switch(dest):
        custom=landings.picker_slug(pid, dest)
        if custom is None: path=SLUG[pid] if pid in C[dest]['pages'] else ''
        else: path=custom
        return f'{BASE}/{dest}/{path}'
    picker=('<details class="lang"><summary>🌐 '+flag(code,False)+lname+'</summary><ul>'+''.join(f'<li><a href="{_switch(x[0])}" hreflang="{x[1]}" lang="{x[1]}"'+(' aria-current="true"' if x[0]==code else '')+f'>{flag(x[0])}<span>{x[2]}</span></a></li>' for x in PUB)+'</ul></details>')
    lm=IMG['logo-mark']; lf=IMG['logo-full']
    roomish=pid.startswith('room-') or pid=='rooftop'
    room_keys=[]
    if roomish:
        if p.get('cover'): room_keys.append(p['cover'][0])
        for _s in p['sections']:
            for _im in _s.get('imgs') or []:
                _k=_im[0].split('@')[0]
                if _k not in room_keys: room_keys.append(_k)
    use_room=roomish and len(room_keys)>=2
    if pid=='home':
        pre=preload(front.HERO_PHOTO,'100vw')
        top=(f'<div class="hero-wrap">{hero_still(code)}'
             f'<div class="in"><h1>{html.escape(p["h1"])}</h1>'
             f'<p>{html.escape(p["lead"])}</p>{price_line(code)}'
             f'<p class="motto" dir="ltr" lang="en">{u["motto"]}</p>{cta(u, code)}</div></div><div class="wrap">')
    else:
        pre=preload(room_keys[0] if use_room else p['cover'][0], PHOTO_SIZES) if (use_room or p.get('cover')) else ''
        booktop='' if pid=='booking' else f'<p class="topbook"><a class="btn primary" href="{url(code,"booking")}">{html.escape(dict(c["nav"]).get("booking",u.get("book_airbnb","")))}</a></p>'
        visual=carousel(room_keys, code, 'mini', True) if use_room else (f'<figure class="cover">{pic(p["cover"][0],p["cover"][1],True,PHOTO_SIZES,code)}</figure>' if p.get('cover') else '')
        top=f'<div class="wrap ph"><h1>{html.escape(p["h1"])}</h1>'+(f'<p class="lead">{html.escape(p["lead"])}</p>' if p.get('lead') else '')+booktop+visual
    guide=is_guide(pid)
    anchored=[]; toc=[]
    for s in p['sections']:
        s=dict(s)
        if 'h2' in s:
            s['_id']=f's{len(toc)+1}'
            toc.append((s['_id'],s['h2']))
        anchored.append(s)
    body=''.join(section(s,code,u,guide,use_room) for s in anchored)
    if pid=='home':
        body=facts_html(code)+amen_html(code)+body+gallery_html(code)+reviews_html(code)
    if p.get('toc') and len(toc)>=2 and u.get('toc_label'):
        _tl=html.escape(u['toc_label'])
        body=f'<nav class="toc" aria-label="{_tl}"><p>{_tl}</p><ol>'+''.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i,t in toc)+'</ol></nav>'+body
    if p.get('related'):
        _lis=[]
        for _rp in p['related']:
            if _rp not in C[code]['pages']: continue
            _lab=u['home'] if _rp=='home' else C[code]['pages'][_rp]['h1']
            _lis.append(f'<li><a href="{url(code,_rp)}">{html.escape(_lab)}</a></li>')
        if _lis:
            body+=f'<section class="rel"><h2>{html.escape(u.get("related_h","More to read"))}</h2><ul class="chk">{"".join(_lis)}</ul></section>'
    elif guide:
        body+=related_block(code,pid,c)
    if p.get('book') and (isinstance(p.get('book'),str) or u.get('book_line')):
        _line=p['book'] if isinstance(p['book'],str) else u['book_line']
        _btn=u.get('book_btn') or dict(c['nav']).get('booking',u.get('book_airbnb',''))
        body+=f'<aside class="bookbox"><p>{html.escape(_line)}</p><p><a class="btn b1" href="{url(code,"booking")}">{html.escape(_btn)}</a></p></aside>'
    elif guide:
        body+=book_box(code,c)
    inner=(f'<body><a class="skip" href="#main">{u["skip"]}</a><header class="site"><div class="bar"><a class="brand" href="{url(code,"home")}"><img src="{BASE}/assets/img/logo-mark.webp" width="{lm["w"]}" height="{lm["h"]}" alt="ASCON LIVING logo" decoding="async"><span>ASCON LIVING</span></a>{BURGER}<nav class="main" aria-label="Main">{nav}</nav>{picker}</div></header>'
           f'<main id="main">{top}{body}</div></main>'
           f'<footer><div class="wrap"><div><img src="{BASE}/assets/img/logo-full.webp" width="{lf["w"]}" height="{lf["h"]}" alt="ASCON LIVING" loading="lazy"><p class="motto" dir="ltr" lang="en">{u["motto"]}</p></div>'
           f'<div><strong>{u["address_label"]}</strong><br>{F["street"]}<br>{u.get("locality",F["locality"])}, Vietnam</div>'
           f'<div><strong>{u["contact_label"]}</strong><br><a href="tel:{F["phone_e164"]}">{F["phone"]}</a><br><a href="mailto:{F["email"]}">{F["email"]}</a><br><a href="{F["wa"]}" rel="noopener">WhatsApp</a> · <a href="{F["zalo"]}" rel="noopener">Zalo</a>{u.get("extra_contact","")}</div>'
           f'<div><strong>{u["more_label"]}</strong><br>{legal(code)}<br><a href="{F["guide"]}" rel="noopener">{u["guest_guide"]}</a></div></div></footer>'
           f'<a class="fab" href="{F["wa"]}" rel="noopener" aria-label="{u["whatsapp"]}">{WA_SVG}</a>'
           f'{lightbox(code)}'
           f'<div class="bookbar"><a class="btn primary" href="{F["airbnb"]}" rel="noopener">{html.escape(front.KICKER.get(code, front.KICKER["en"]))}</a></div></body>')
    css=filter_css(CRIT, inner, hl, dirn)
    if font and font in FONTS:
        fam=FONTS[font]['family']
        css=fontfaces+css.replace(':root{', f':root{{--ff:"{fam}","{fam} Fallback";', 1)
    elif font:
        css=css.replace(':root{', f':root{{--ff:"{font}";', 1)
    css=minify_css(css)
    defer=(f'<link rel="stylesheet" href="{BASE}/assets/site.css" media="print" onload="this.media=&#39;all&#39;">'
           f'<noscript><link rel="stylesheet" href="{BASE}/assets/site.css"></noscript>')
    return minify_html(f'''<!doctype html><html lang="{hl}" dir="{dirn}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{pre}{fontlink}
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(p['description'])}"><link rel="canonical" href="{canon}">{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="ASCON LIVING"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(p['description'])}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:locale" content="{hl.replace('-','_')}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/favicon.png"><meta name="theme-color" content="#14233f"><style>{css}</style>{defer}{ldh}<script src="{BASE}/assets/site.js" defer></script></head>
{inner}</html>''')
def root_page():
    code='en'; u=C['en']['ui']; hl,lname='en','English'
    title='Homestay Ho Chi Minh City – Whole House, 3 Bedrooms'
    h1='Homestay Ho Chi Minh City – Whole House, 3 Bedrooms Each With Private Bath'
    desc='Whole-house homestay in Ho Chi Minh City: 3 bedrooms, each with a private bathroom, rooftop terrace and river view.'
    lead='A whole house on the river in Ho Chi Minh City. Three floors, more than 250 m², and three bedrooms that each have their own bathroom.'
    gear='The entertainment room has karaoke, a PS5 (PlayStation 5) with PlayStation Plus, gaming, a 4K cinema system (Optoma 4K projector) and Netflix.'
    canon=SITE+'/'
    alts=''.join(f'<link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/">' for x in PUB)+f'<link rel="alternate" hreflang="x-default" href="{canon}">'
    labels=dict(C['en']['nav'])
    nav=nav_html('en','home')
    picker=('<details class="lang"><summary>🌐 '+flag('en',False)+lname+'</summary><ul>'+''.join(f'<li><a href="{BASE}/{x[0]}/" hreflang="{x[1]}" lang="{x[1]}">{flag(x[0])}<span>{x[2]}</span></a></li>' for x in PUB)+'</ul></details>')
    lm=IMG['logo-mark']; lf=IMG['logo-full']
    hero=(f'<div class="hero-wrap">{hero_still(code)}<div class="in"><h1>{html.escape(h1)}</h1>'
          f'<p>{html.escape(lead)}</p>{price_line("en")}'
          f'<p class="motto" dir="ltr" lang="en">{u["motto"]}</p>{cta(u, code)}</div></div>')
    body=facts_html(code)+amen_html(code)+f'<p class="lead">{html.escape(gear)}</p>'+gallery_html(code)+reviews_html(code)
    ld={"@context":"https://schema.org","@type":"WebPage","name":title,"description":desc,"url":canon,"inLanguage":"en","isPartOf":{"@type":"WebSite","name":F['name'],"url":SITE+'/'}}
    ldh='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False).replace('</','<\\/')+'</script>'
    inner=(f'<body><a class="skip" href="#main">{u["skip"]}</a><header class="site"><div class="bar"><a class="brand" href="{canon}"><img src="{BASE}/assets/img/logo-mark.webp" width="{lm["w"]}" height="{lm["h"]}" alt="ASCON LIVING logo" decoding="async"><span>ASCON LIVING</span></a>{BURGER}<nav class="main" aria-label="Main">{nav}</nav>{picker}</div></header>'
           f'<main id="main">{hero}<div class="wrap">{body}</div></main>'
           f'<footer><div class="wrap"><div><img src="{BASE}/assets/img/logo-full.webp" width="{lf["w"]}" height="{lf["h"]}" alt="ASCON LIVING" loading="lazy"><p class="motto" dir="ltr" lang="en">{u["motto"]}</p></div>'
           f'<div><strong>{u["address_label"]}</strong><br>{F["street"]}<br>{u.get("locality",F["locality"])}, Vietnam</div>'
           f'<div><strong>{u["contact_label"]}</strong><br><a href="tel:{F["phone_e164"]}">{F["phone"]}</a><br><a href="mailto:{F["email"]}">{F["email"]}</a><br><a href="{F["wa"]}" rel="noopener">WhatsApp</a> · <a href="{F["zalo"]}" rel="noopener">Zalo</a></div>'
           f'<div><strong>{u["more_label"]}</strong><br>{legal("en")}</div></div></footer>'
           f'<a class="fab" href="{F["wa"]}" rel="noopener" aria-label="{u["whatsapp"]}">{WA_SVG}</a>{lightbox(code)}'
           f'<div class="bookbar"><a class="btn primary" href="{F["airbnb"]}" rel="noopener">{html.escape(front.KICKER["en"])}</a></div></body>')
    css=minify_css(filter_css(CRIT, inner, hl, 'ltr'))
    defer=(f'<link rel="stylesheet" href="{BASE}/assets/site.css" media="print" onload="this.media=&#39;all&#39;">'
           f'<noscript><link rel="stylesheet" href="{BASE}/assets/site.css"></noscript>')
    pre=preload(front.HERO_PHOTO, '100vw')
    return minify_html(f'''<!doctype html><html lang="en" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{pre}
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}">{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="ASCON LIVING"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/favicon.png"><meta name="theme-color" content="#14233f"><style>{css}</style>{defer}{ldh}<script src="{BASE}/assets/site.js" defer></script></head>
{inner}</html>''')
def main():
    _merge_city()
    _append_market_cards()
    front.prepare(C)
    for code,*_ in LANGS: shutil.rmtree(f'{OUT}/{code}',ignore_errors=True)
    shutil.rmtree(f'{OUT}/assets/flags',ignore_errors=True); shutil.copytree(f'{ROOT}/tools/flags',f'{OUT}/assets/flags')
    errs=[f'{l[0]}/{pid}: title {len(C[l[0]]["pages"][pid]["title"])} chars, width {width(C[l[0]]["pages"][pid]["title"])} / desc {len(C[l[0]]["pages"][pid]["description"])} chars, width {width(C[l[0]]["pages"][pid]["description"])}' for l in PUB for pid,_ in PAGES if pid in C[l[0]]['pages'] and seo_bad(l[0],C[l[0]]['pages'][pid],C[l[0]].get('title_suffix',''))]
    if errs: raise SystemExit('SEO length errors:\n'+'\n'.join(errs))
    urls=[]
    for l in PUB:
        for pid,slug in PAGES:
            if pid not in C[l[0]]['pages']: continue
            d=f'{OUT}/{l[0]}/{slug}'; os.makedirs(d,exist_ok=True)
            open(f'{d}index.html','w').write(page(l,pid)); urls.append(f'{SITE}/{l[0]}/{slug}')
    # sitemap with hreflang alternates (published languages only). One loc per URL.
    sm=['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    root_alts=''.join(f'<xhtml:link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/"/>' for x in PUB)+f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>'
    sm.append(f'<url><loc>{SITE}/</loc><lastmod>{TODAY}</lastmod>{root_alts}</url>')
    seen=set()
    for l in PUB:
        for pid,slug in PAGES:
            if pid not in C[l[0]]['pages']: continue
            loc=f'{SITE}/{l[0]}/{slug}'
            if loc in seen: continue
            seen.add(loc)
            _alt=landings.hreflang_sitemap(pid, SITE)
            alts=_alt if _alt else ''.join(f'<xhtml:link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/{slug}"/>' for x in HAS(pid))+f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/{xdef(pid)}/{slug}"/>'
            sm.append(f'<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>{alts}</url>')
    sm.append('</urlset>'); open(f'{OUT}/sitemap.xml','w').write('\n'.join(sm))
    if DOMAIN.endswith('.github.io'):
        if os.path.exists(f'{OUT}/CNAME'): os.remove(f'{OUT}/CNAME')
    else: open(f'{OUT}/CNAME','w').write(DOMAIN+'\n')
    open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    open(f'{OUT}/.nojekyll','w').write('')
    for _f in glob.glob(f'{OUT}/'+'[0-9a-f]'*32+'.txt'): os.remove(_f)
    open(f"{OUT}/{F['indexnow_key']}.txt",'w').write(F['indexnow_key'])  # IndexNow key file
    shutil.copyfile(f'{ROOT}/tools/llms.txt',f'{OUT}/llms.txt')  # /llms.txt, byte-identical copy of tools/llms.txt
    links=''.join(f'<li><a href="{BASE}/{x[0]}/" hreflang="{x[1]}" lang="{x[1]}">{x[2]}</a></li>' for x in PUB)
    open(f'{OUT}/index.html','w').write(root_page())
    shutil.copyfile(f'{ROOT}/tools/site.js', f'{OUT}/assets/site.js')
    en=C['en']['ui']
    open(f'{OUT}/assets/site.css','w').write(minify_css(REST))
    os.makedirs(f'{OUT}/assets/fonts', exist_ok=True)
    for fn in glob.glob(f'{ROOT}/tools/fonts/*.woff2'): shutil.copy(fn, f'{OUT}/assets/fonts/')
    ofl=f'{ROOT}/tools/fonts/OFL.txt'
    if os.path.isfile(ofl): shutil.copy(ofl, f'{OUT}/assets/fonts/OFL.txt')
    open(f'{OUT}/404.html','w').write(minify_html(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{en['not_found_title']} | ASCON LIVING</title><meta name="robots" content="noindex"><style>{minify_css(CRIT+REST)}</style></head>
<body><main class="wrap ph" style="max-width:700px;margin:auto;padding:48px 16px"><h1>{en['not_found_title']}</h1><p>{en['not_found_text']} <a href="{BASE}/en/">ASCON LIVING</a></p><ul>{links}</ul></main></body></html>'''))
    print('published:',[x[0] for x in PUB],'pages:',len(urls))
if __name__=='__main__': main()
