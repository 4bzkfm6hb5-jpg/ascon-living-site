#!/usr/bin/env python3
"""Static site builder. Add content/<code>.json to publish a language; nothing else needed."""
import json, os, html, shutil, datetime
ROOT=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(ROOT,'docs')
F=json.load(open(f'{ROOT}/facts.json'))
# Single settings for where the site lives (facts.json): absolute origin for canonical/hreflang/og/JSON-LD/sitemap,
# and the root-relative path prefix for links/assets ('' on the custom domain; was '/ascon-living-site' on github.io).
SITE=F['site_url'].rstrip('/'); BASE=F.get('base_path','').rstrip('/')
from urllib.parse import urlparse as _up
DOMAIN=_up(SITE).netloc  # docs/CNAME for GitHub Pages custom domain (not written for *.github.io)
PAGES=[('home',''),('house','house/'),('rooftop','rooftop/'),('families','families/'),('groups','groups/'),
('location','location/'),('booking','booking/'),('faq','faq/'),('rules','house-rules/'),('guide','guide/'),
('guide-family','guide/hcmc-with-family/'),('guide-airport','guide/airport-transfer/'),('guide-app','guide/ascon-guide-app/'),('travel-guide','travel-guide/'),
('imprint','imprint/'),('privacy','privacy/')]
# Room detail pages: published per language only once content/<code>.json has pages.<id> (no placeholders)
ROOMS=[('room-entertainment','house/karaoke-entertainment/'),('room-living','house/living-room/'),('room-kitchen','house/kitchen/'),('room-master','house/master-bedroom/'),
('room-bedroom-2','house/bedroom-2/'),('room-bedroom-3','house/bedroom-3/'),('room-bathrooms','house/bathrooms/'),('room-hallway','house/hallway/'),('room-outside','house/outside/')]
PAGES+=ROOMS
SLUG=dict(PAGES)
IMG=json.load(open(f'{ROOT}/tools/images.json'))
LANGS=json.load(open(f'{ROOT}/languages.json'))
CSS=open(f'{ROOT}/tools/style.css').read().replace('\n','')
PUB=[l for l in LANGS if os.path.exists(f'{ROOT}/content/{l[0]}.json')]
C={l[0]:json.load(open(f'{ROOT}/content/{l[0]}.json')) for l in PUB}
import sys as _s; _s.path.insert(0,f'{ROOT}/tools'); import laundry as _laundry
C={k:_laundry.apply(k,v) for k,v in C.items()}
# Language-switcher flags: self-hosted SVGs from flag-icons (MIT, tools/flags/LICENSE), copied to docs/assets/flags on every build.
# Not emoji: Windows does not render emoji flags. pa is Gurmukhi (Indian Punjab) -> IN; ur -> PK.
FLAG={'en':'gb','de':'de','vi':'vn','zh':'cn','zh-tw':'tw','ko':'kr','ja':'jp','th':'th','ms':'my','id':'id','ru':'ru','fr':'fr','es':'es','pt':'br','it':'it','hi':'in','ur':'pk','pa':'in','nl':'nl','pl':'pl','sv':'se','tr':'tr','ar':'sa'}
def flag(code,lazy=True):
    f=FLAG.get(code)
    return f'<img class="flag" src="{BASE}/assets/flags/{f}.svg" width="20" height="15" alt=""'+(' loading="lazy"' if lazy else '')+' decoding="async">' if f else ''
  # laundry service 30 EUR per load in every language
def HAS(pid): return [x for x in PUB if pid in C[x[0]]['pages']]
TODAY=datetime.date.today().isoformat()
WA_SVG='<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.5-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7 0a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.8 1 3.9.8a3.3 3.3 0 0 0 2.1-1.5 2.7 2.7 0 0 0 .2-1.5c-.1-.2-.3-.3-.7-.5z"/></svg>'
def url(code,pid): return f'{BASE}/{code}/{SLUG[pid]}'
def sub(s,code): return s.replace('{L}',f'{BASE}/{code}/').replace('{phone_e164}',F['phone_e164']).replace('{phone}',F['phone']).replace('{email}',F['email']).replace('{guide}',F['guide'])
def pic(name,alt,eager=False,sizes='(min-width:900px) 380px, 100vw'):
    m=IMG[name]; ws=m['widths']; src=f'{BASE}/assets/img/{name}-'
    ss=', '.join(f'{src}{w}.webp {w}w' for w in ws); w=ws[-1]; h=round(m['h']*w/m['w'])
    attrs='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="{src}{ws[min(1,len(ws)-1)]}.webp" srcset="{ss}" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(alt)}" {attrs}>'
def cta(u):
    return (f'<p><a class="btn b1" href="{F["airbnb"]}" rel="noopener">{u["book_airbnb"]}</a>'
            f'<a class="btn b2" href="{F["trip"]}" rel="noopener">{u["book_trip"]}</a>'
            f'<a class="btn wa" href="{F["wa"]}" rel="noopener">{u["whatsapp"]}</a>'
            f'<a class="btn zl" href="{F["zalo"]}" rel="noopener">{u["zalo"]}</a></p>')
def section(s,code,u):
    o=[]
    if 'h2' in s: o.append(f'<h2>{html.escape(s["h2"])}</h2>')
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
    if 'imgs' in s: o.append('<div class="grid">'+''.join(f'<figure>{pic(i[0]+"@"+code if i[0]+"@"+code in IMG else i[0],i[1])}<figcaption>{html.escape(i[2] if len(i)>2 and i[2] else i[1])}</figcaption></figure>' for i in s['imgs'])+'</div>')
    if 'faq' in s: o.append('<div class="faq">'+''.join(f'<details><summary><h2 class="q">{html.escape(q)}</h2></summary><p>{sub(a,code)}</p></details>' for q,a in s['faq'])+'</div>')
    if 'cards' in s: o.append('<div class="cards">'+''.join(f'<div class="card"><a href="{url(code,pid)}">{html.escape(t)}</a><p>{html.escape(d)}</p></div>' for t,pid,d in s['cards'] if pid in C[code]['pages'])+'</div>')
    if s.get('cta'): o.append(cta(u))
    return '<section>'+''.join(o)+'</section>'
def lodging(code,c):
    region='Ho-Chi-Minh-Stadt' if code=='de' else 'Ho Chi Minh City'
    return {"@context":"https://schema.org","@type":"VacationRental","@id":SITE+'/#lodging',"name":F['name'],
      "url":SITE+f'/{code}/',"image":[SITE+'/assets/img/hero-1440.webp',SITE+'/assets/img/og.jpg'],"logo":SITE+'/assets/img/logo-mark.png',
      "description":c['pages']['home']['description'],"telephone":F['phone_e164'],"email":F['email'],
      "address":{"@type":"PostalAddress","streetAddress":F['street'],"addressLocality":"Tân Hưng","addressRegion":region,"addressCountry":F['country']},
      "checkinTime":F['checkin'],"checkoutTime":F['checkout'],
      "knowsLanguage":F['languages'],"sameAs":[F['airbnb'],F['trip']],
      "contactPoint":[{"@type":"ContactPoint","contactType":"reservations","telephone":F['phone_e164'],"email":F['email'],"url":F['wa']},{"@type":"ContactPoint","contactType":"reservations","telephone":F['phone_e164'],"url":F['zalo']}],
      "amenityFeature":[{"@type":"LocationFeatureSpecification","name":a,"value":True} for a in F['amenities']],
      "containsPlace":{"@type":"Accommodation","additionalType":"EntirePlace","name":F['name'],"numberOfRooms":F['rooms'],"numberOfBedrooms":F['rooms'],
        "numberOfBathroomsTotal":F['bathrooms_full']+F['bathrooms_partial'],"numberOfFullBathrooms":F['bathrooms_full'],"numberOfPartialBathrooms":F['bathrooms_partial'],
        "bed":[{"@type":"BedDetails","numberOfBeds":1,"typeOfBed":"180×200 cm"},{"@type":"BedDetails","numberOfBeds":2,"typeOfBed":"160×200 cm"}],
        "floorSize":{"@type":"QuantitativeValue","minValue":F['size_m2_min'],"unitCode":"MTK"},
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
    if code in CJK: return width(t)>64 or width(d)>160
    if code=='th': return glen(t)>60 or glen(d)>160
    return len(t)>60 or len(d)>160
def page(l,pid):
    code,hl,lname,dirn,font=l; c=C[code]; u=c['ui']; p=c['pages'][pid]
    title=p['title']+c.get('title_suffix',''); canon=SITE+f'/{code}/{SLUG[pid]}'
    alts=''.join(f'<link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/{SLUG[pid]}">' for x in HAS(pid))+f'<link rel="alternate" hreflang="x-default" href="{SITE}/en/{SLUG[pid]}">'
    fontlink=''; css=CSS
    if font:
        fontlink=f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={font.replace(" ","+")}:wght@400;600&display=swap" media="print" onload="this.media=&#39;all&#39;">'
        css=css.replace(':root{',f':root{{--ff:"{font}";',1)
    ld=[]
    if pid in ('home','house','booking','location'): ld.append(lodging(code,c))
    crumbs=[{"@type":"ListItem","position":1,"name":u['home'],"item":SITE+f'/{code}/'}]
    if pid!='home':
        if pid.startswith('room-'): crumbs.append({"@type":"ListItem","position":2,"name":c['pages']['house']['h1'],"item":SITE+f'/{code}/house/'})
        if pid.startswith('guide-'): crumbs.append({"@type":"ListItem","position":2,"name":c['pages']['guide']['h1'],"item":SITE+f'/{code}/guide/'})
        crumbs.append({"@type":"ListItem","position":len(crumbs)+1,"name":p['h1'],"item":canon})
    ld.append({"@context":"https://schema.org","@type":"WebPage","name":title,"description":p['description'],"url":canon,"inLanguage":hl,"isPartOf":{"@type":"WebSite","name":F['name'],"url":SITE+'/'}})
    ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs})
    if pid.startswith('guide-'): ld.append({"@context":"https://schema.org","@type":"Article","headline":p['h1'],"description":p['description'],"inLanguage":hl,"image":SITE+'/assets/img/og.jpg',"author":{"@type":"Organization","name":F['name']},"mainEntityOfPage":canon,"dateModified":TODAY})
    if any(s.get('faq') for s in p['sections']): ld.append({"@context":"https://schema.org","@type":"FAQPage","inLanguage":hl,"mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for s in p['sections'] for q,a in s.get('faq',[])]})
    ldh=''.join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False).replace('</','<\\/')+'</script>' for x in ld)
    navcur=pid if pid in dict(c['nav']) else ('guide' if pid.startswith('guide') else 'house' if pid.startswith('room-') else '')
    nav=''.join(f'<a href="{url(code,k)}"'+(' aria-current="page"' if k==navcur else '')+f'>{html.escape(v)}</a>' for k,v in c['nav'])
    picker=('<details class="lang"><summary>🌐 '+flag(code,False)+lname+'</summary><ul>'+''.join(f'<li><a href="{BASE}/{x[0]}/{SLUG[pid] if pid in C[x[0]]["pages"] else ""}" hreflang="{x[1]}" lang="{x[1]}"'+(' aria-current="true"' if x[0]==code else '')+f'>{flag(x[0])}<span>{x[2]}</span></a></li>' for x in PUB)+'</ul></details>')
    lm=IMG['logo-mark']; lf=IMG['logo-full']
    if pid=='home':
        top=(f'<div class="hero">{pic(p["hero"][0],p["hero"][1],True,"100vw")}<div class="in"><h1>{html.escape(p["h1"])}</h1>'
             f'<p>{html.escape(p["lead"])}</p><p class="motto" dir="ltr" lang="en">{u["motto"]}</p>{cta(u)}</div></div><div class="wrap">')
    else:
        top=f'<div class="wrap ph"><h1>{html.escape(p["h1"])}</h1>'+(f'<p class="lead">{html.escape(p["lead"])}</p>' if p.get('lead') else '')+(f'<figure class="cover">{pic(p["cover"][0],p["cover"][1],True,"(min-width:900px) 900px, 100vw")}</figure>' if p.get('cover') else '')
    body=''.join(section(s,code,u) for s in p['sections'])
    return f'''<!doctype html><html lang="{hl}" dir="{dirn}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(p['description'])}"><link rel="canonical" href="{canon}">{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="ASCON LIVING"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(p['description'])}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:locale" content="{hl.replace('-','_')}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/favicon.png"><meta name="theme-color" content="#14233f">{fontlink}<style>{css}</style>{ldh}</head>
<body><a class="skip" href="#main">{u['skip']}</a><header><div class="bar"><a class="brand" href="{url(code,'home')}"><img src="{BASE}/assets/img/logo-mark.webp" width="{lm['w']}" height="{lm['h']}" alt="ASCON LIVING logo">ASCON LIVING</a>{picker}</div><nav class="main" aria-label="Main">{nav}</nav></header>
<main id="main">{top}{body}</div></main>
<footer><div class="wrap"><div><img src="{BASE}/assets/img/logo-full.webp" width="{lf['w']}" height="{lf['h']}" alt="ASCON LIVING" loading="lazy"><p class="motto" dir="ltr" lang="en">{u['motto']}</p></div>
<div><strong>{u['address_label']}</strong><br>{F['street']}<br>{u.get('locality',F['locality'])}, Vietnam</div>
<div><strong>{u['contact_label']}</strong><br><a href="tel:{F['phone_e164']}">{F['phone']}</a><br><a href="mailto:{F['email']}">{F['email']}</a><br><a href="{F['wa']}" rel="noopener">WhatsApp</a> · <a href="{F['zalo']}" rel="noopener">Zalo</a>{u.get('extra_contact','')}</div>
<div><strong>{u['more_label']}</strong><br>{legal(code)}<br><a href="{F['guide']}" rel="noopener">{u['guest_guide']}</a></div></div></footer>
<a class="fab" href="{F['wa']}" rel="noopener" aria-label="{u['whatsapp']}">{WA_SVG}</a></body></html>'''
def main():
    for code,*_ in LANGS: shutil.rmtree(f'{OUT}/{code}',ignore_errors=True)
    shutil.rmtree(f'{OUT}/assets/flags',ignore_errors=True); shutil.copytree(f'{ROOT}/tools/flags',f'{OUT}/assets/flags')
    errs=[f'{l[0]}/{pid}: title {len(C[l[0]]["pages"][pid]["title"])} chars, width {width(C[l[0]]["pages"][pid]["title"])} / desc {len(C[l[0]]["pages"][pid]["description"])} chars, width {width(C[l[0]]["pages"][pid]["description"])}' for l in PUB for pid,_ in PAGES if pid in C[l[0]]['pages'] and seo_bad(l[0],C[l[0]]['pages'][pid],C[l[0]].get('title_suffix',''))]
    if errs: raise SystemExit('SEO length errors:\n'+'\n'.join(errs))
    urls=[]
    for l in PUB:
        for pid,slug in PAGES:
            if pid not in C[l[0]]['pages']: continue
            d=f'{OUT}/{l[0]}/{slug}'; os.makedirs(d,exist_ok=True)
            open(f'{d}index.html','w').write(page(l,pid)); urls.append((pid,slug))
    # sitemap with hreflang alternates (published languages only)
    sm=['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for l in PUB:
        for pid,slug in PAGES:
            if pid not in C[l[0]]['pages']: continue
            alts=''.join(f'<xhtml:link rel="alternate" hreflang="{x[1]}" href="{SITE}/{x[0]}/{slug}"/>' for x in HAS(pid))+f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/en/{slug}"/>'
            sm.append(f'<url><loc>{SITE}/{l[0]}/{slug}</loc><lastmod>{TODAY}</lastmod>{alts}</url>')
    sm.append('</urlset>'); open(f'{OUT}/sitemap.xml','w').write('\n'.join(sm))
    if DOMAIN.endswith('.github.io'):
        if os.path.exists(f'{OUT}/CNAME'): os.remove(f'{OUT}/CNAME')
    else: open(f'{OUT}/CNAME','w').write(DOMAIN+'\n')
    open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    open(f'{OUT}/.nojekyll','w').write('')
    codes=json.dumps([[x[0],x[1]] for x in PUB])
    links=''.join(f'<li><a href="{BASE}/{x[0]}/" hreflang="{x[1]}" lang="{x[1]}">{x[2]}</a></li>' for x in PUB)
    open(f'{OUT}/index.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ASCON LIVING – Ho Chi Minh City</title>
<link rel="canonical" href="{SITE}/en/"><meta http-equiv="refresh" content="2;url={BASE}/en/"><meta name="robots" content="noindex,follow">
<script>(function(){{var p={codes},n=(navigator.languages||[navigator.language||'en']);for(var i=0;i<n.length;i++){{var c=n[i].toLowerCase();for(var j=0;j<p.length;j++){{var h=p[j][1].toLowerCase();if(c===h||c.split('-')[0]===h.split('-')[0]){{location.replace('{BASE}/'+p[j][0]+'/');return}}}}}}location.replace('{BASE}/en/')}})()</script>
<style>body{{font-family:system-ui,sans-serif;padding:2rem;color:#14233f}}</style></head><body><h1>ASCON LIVING</h1><p>Choose your language:</p><ul>{links}</ul></body></html>''')
    en=C['en']['ui']
    open(f'{OUT}/404.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{en['not_found_title']} | ASCON LIVING</title><meta name="robots" content="noindex"><style>{CSS}</style></head>
<body><main class="wrap ph" style="max-width:700px;margin:auto;padding:48px 16px"><h1>{en['not_found_title']}</h1><p>{en['not_found_text']} <a href="{BASE}/en/">ASCON LIVING</a></p><ul>{links}</ul></main></body></html>''')
    print('published:',[x[0] for x in PUB],'pages:',len(urls))
if __name__=='__main__': main()
