"""Assemble Market Researcher long texts (EN/DE) into content JSON, applying hard-rule cleaning. Prints every cleaning action."""
import json,re,sys,copy
sys.path.insert(0,'tools'); from import_long import parse
SRC='/workspace/ascon-texts'; LOG=[]
REP={'en':[
 ("Karaoke night: lyrics on the big screen","Karaoke night in your own room"),
 ("Kids love seeing the words on the big screen, grandparents","Kids love grabbing the microphone, grandparents"),
 ("No audience except each other, lyrics on the big screen, and nobody","No audience except each other, and nobody"),
 ("Duets, a karaoke contest among friends, lyrics on the big screen, then","Duets, a karaoke contest among friends, then"),
 ("Karaoke with lyrics on the big 4K projector screen, PlayStation","Karaoke, PlayStation"),
 ("Start with karaoke: lyrics big on the 4K projector screen, duets to warm up","Start with karaoke: duets to warm up"),
 ("a family karaoke contest with lyrics on the big screen,","a family karaoke contest,"),
 ("a friendly karaoke competition with the lyrics on the big screen","a friendly karaoke competition"),
 ("karaoke with lyrics big on the 4K projector screen, PlayStation","karaoke, 4K projector, PlayStation"),
 ("4K projector screen for karaoke lyrics and movie nights","4K projector screen for movie nights"),
 ("There is a smoke detector and a first-aid kit on every floor, a safe for valuables, and cameras","There is a safe for valuables, and cameras"),
 ("There is a smoke detector and a first-aid kit on every floor, and cameras are installed outdoors only","Cameras are installed outdoors only"),
 (", a laundry service is available, and there is a smoke detector and first-aid kit on every floor",", and a laundry service is available"),
 ("Smoke detector and first-aid kit on every floor, outdoor cameras only","Cameras outdoors only, none inside the house"),
 ("No parties or events","No wild parties"),("quick party game","quick group game"),
 ("guest registration takes place at check-in.","guest registration at check-in is required by Vietnamese law."),
 ("Good to know: quiet from 21:30","Good to know: loud music only until 21:30"),("Good neighbours: quiet from 21:30","Good neighbours: loud music only until 21:30"),
 ("the house rules ask for loud music to go down from 21:30","the house rules allow loud music only until 21:30"),
 ("Loud music goes down from 21:30","Loud music only until 21:30"),("loud music goes down from 21:30","loud music only until 21:30"),
 ("Loud music down from 21:30","Loud music only until 21:30"),("Quiet hours from 21:30 keep","Loud music only until 21:30 keeps"),
 ("Quiet hours from 21:30 mean","Loud music only until 21:30 means"),("The house quiet hours from 21:30 help keep","The house rule of loud music only until 21:30 helps keep"),
 ("The house has quiet hours from 21:30, so","Loud music is only allowed until 21:30, so"),("quiet from 21:30","loud music only until 21:30"),("Quiet from 21:30","Loud music only until 21:30"),
 ("Are there quiet hours?","Is there a rule for loud music?"),("Quiet hours","Loud music"),("From 21:30","Only until 21:30"),
 ("If you have been looking for a villa for groups in Ho Chi Minh City, this is a private house with exactly that kind of space","If you have been looking for a private house for groups in Ho Chi Minh City, this is a home with exactly that kind of space"),
 ("in the Ho Chi Minh villa","in the private house in Ho Chi Minh City"),("a villa with karaoke","a house with karaoke"),
 ("about your Ho Chi Minh villa","about your private house in Ho Chi Minh City"),
 ("Villa with Karaoke in Ho Chi Minh City | ASCON LIVING","House with Karaoke in Ho Chi Minh City | ASCON LIVING"),
 ("A villa with karaoke in Ho Chi Minh City: your private entertainment room","A house with karaoke in Ho Chi Minh City: your private entertainment room"),
 ("Within a few minutes the room","Soon the room"),("within a few minutes","soon"),
 (", no smoking indoors and no pets"," and no smoking indoors"),
],'de':[
 ("Karaoke-Abend: die Liedtexte groß auf der Leinwand","Karaoke-Abend im eigenen Raum"),
 ("Kinder lieben die großen Texte auf der Leinwand, Großeltern","Kinder lieben es, ans Mikrofon zu dürfen, Großeltern"),
 ("Kein Publikum außer euch, die Texte groß auf der Leinwand, und niemand","Kein Publikum außer euch, und niemand"),
 ("Duette, ein Karaoke-Wettbewerb unter Freunden, Liedtexte auf großer Leinwand, danach","Duette, ein Karaoke-Wettbewerb unter Freunden, danach"),
 ("Karaoke mit Liedtexten groß über den 4K-Projektor, PlayStation-Abende","Karaoke, PlayStation-Abende"),
 ("Fangt mit Karaoke an: Liedtexte groß über den 4K-Projektor, ein paar Duette","Fangt mit Karaoke an: ein paar Duette"),
 ("Karaoke mit Liedtexten groß über den 4K-Projektor, PlayStation","Karaoke, 4K-Projektor, PlayStation"),
 ("Leinwand für den 4K-Projektor, für Karaoke-Texte und Filmabende","Leinwand für den 4K-Projektor für Filmabende"),
 ("Auf jeder Etage gibt es Rauchmelder und Erste-Hilfe-Kasten, einen Safe für Wertsachen und Kameras","Es gibt einen Safe für Wertsachen und Kameras"),
 ("Auf jeder Etage gibt es Rauchmelder und Erste-Hilfe-Kasten, und Kameras sind ausschließlich außen","Kameras sind ausschließlich außen"),
 (", ein Wäscheservice ist möglich, und auf jeder Etage gibt es Rauchmelder und Erste-Hilfe-Kasten",", und ein Wäscheservice ist möglich"),
 ("Rauchmelder und Erste-Hilfe-Kasten gibt es auf jeder Etage, Kameras nur außen","Kameras nur außen, keine im Haus"),
 ("Ein paar einfache Hausregeln für einen entspannten Aufenthalt bei ASCON LIVING in Ho Chi Minh-Stadt","Einfache Hausregeln für euren Aufenthalt bei ASCON LIVING in Ho-Chi-Minh-Stadt"),("Ein paar einfache Hausregeln für einen entspannten Aufenthalt bei ASCON LIVING in Ho-Chi-Minh-Stadt","Einfache Hausregeln für euren Aufenthalt bei ASCON LIVING in Ho-Chi-Minh-Stadt"),
 ("die Gästeregistrierung erfolgt beim Check-in.","die Gästeregistrierung beim Check-in ist in Vietnam gesetzlich vorgeschrieben."),
 ("Keine Partys oder Veranstaltungen","Keine wilden Partys"),("Partyspiel","Gruppenspiel"),
 ("laut Hausregeln wird laute Musik ab 21:30 Uhr leiser gestellt","laut Hausregeln ist laute Musik nur bis 21:30 Uhr erlaubt"),
 ("Ab 21:30 Uhr wird laute Musik leiser gestellt","Laute Musik nur bis 21:30 Uhr"),("ab 21:30 Uhr wird laute Musik leiser gestellt","laute Musik nur bis 21:30 Uhr"),
 ("Gut zu wissen: ab 21:30 Uhr wird es ruhiger","Gut zu wissen: laute Musik nur bis 21:30 Uhr"),("Ab 21:30 Uhr wird es ruhiger","Laute Musik nur bis 21:30 Uhr"),
 ("Die Ruhezeiten ab 21:30 Uhr halten","Laute Musik nur bis 21:30 Uhr hält"),("Die Ruhezeiten ab 21:30 Uhr sorgen","Laute Musik nur bis 21:30 Uhr sorgt"),
 ("Laute Musik ab 21:30 Uhr leiser","Laute Musik nur bis 21:30 Uhr"),("Gute Nachbarschaft: ab 21:30 Uhr leiser","Gute Nachbarschaft: laute Musik nur bis 21:30 Uhr"),
 ("ab 21:30 Uhr leiser","laute Musik nur bis 21:30 Uhr"),("Ab 21:30 Uhr gelten im Haus Ruhezeiten, die Abende","Laute Musik ist nur bis 21:30 Uhr erlaubt, die Abende"),
 ("Gibt es Ruhezeiten?","Gibt es eine Regel für laute Musik?"),("Ruhezeiten","Laute Musik"),
 ("in der Villa in","im privaten Haus in"),("Villa mit Karaoke","Ferienhaus mit Karaoke"),
 ("eurer Ho Chi Minh Unterkunft","eurer Unterkunft in Ho-Chi-Minh-Stadt"),
 ("Nach ein paar Minuten ist der Raum","Schnell ist der Raum"),("Ein paar ruhige Minuten","Ein paar ruhige Momente"),
 (", Self-Check-in, keine Haustiere",", Self-Check-in, Rauchverbot im Haus"),
]}
DROP=re.compile(r'(?i)luggage storage|store luggage|Gepäckaufbewahrung|Gepäck aufbewahren|\bpets?\b|Haustier|lyrics|Liedtext|Songtext|Karaoke-Texte|Texte groß|smoke detector|first-aid|Rauchmelder|Erste-Hilfe|\bEUR\b|price|Preis|\bminutes?\b|\bMinuten?\b|Landmark 81|Phú Mỹ Hưng|villa\b|Villa\b|smart ?lock|parking|Parkplatz|\bpool\b|PS5|Agoda|Vrbo|halal')
def clean(l,s,where):
    if not isinstance(s,str): return s
    o=s
    s=s.replace('[live]','').replace('  ',' ').strip()
    s=re.sub(r'\s*\((Keep|Bestehende|Bestehenden)[^)]*\)','',s)
    for a,b in REP[l]:
        if a in s: s=s.replace(a,b)
    if l=='de':
        s=re.sub(r'Ho Chi Minh(?: Stadt| City)?(?![-\w])','Ho-Chi-Minh-Stadt',s)
    if DROP.search(s):
        parts=re.split(r'(?<=[.!?])\s+',s); keep=[p for p in parts if not DROP.search(p)]
        for p in parts:
            if DROP.search(p): LOG.append((l,where,'DROPPED: '+p[:110]))
        s=' '.join(keep)
    if s!=o.replace('[live]','').strip() and not DROP.search(o): LOG.append((l,where,'edit: '+o[:60]+' -> '+s[:60]))
    return s
def cl_flow(l,flow,w):
    out=[]
    for k,v in flow:
        if k in('p','h3'):
            v=clean(l,v,w)
            if v: out.append([k,v])
        elif k=='ul':
            v=[clean(l,x,w) for x in v]; v=[x for x in v if x]
            if v: out.append([k,v])
        elif k=='table':
            rows=[]
            for r in v['rows']:
                if any(DROP.search(c.replace('[live]','')) and not re.search(r'(?i)villa|Villa',c) for c in r): LOG.append((l,w,'DROPPED ROW: '+' | '.join(r))); continue
                rows.append([clean(l,c,w) for c in r])
            out.append([k,{'head':[clean(l,h,w) for h in v['head']] if v.get('head') else None,'rows':rows}])
    return out
def cl_faq(l,faq,w):
    out=[]
    for q,a in faq:
        if DROP.search(q) and not re.search('villa',q,re.I): LOG.append((l,w,'DROPPED Q: '+q)); continue
        q=clean(l,q,w); a=clean(l,a,w)
        if not a: LOG.append((l,w,'DROPPED Q (empty answer): '+q)); continue
        out.append([q,a])
    return out
FAQH={'en':'Frequently asked questions','de':'Häufige Fragen'}
ROOMF={'room-entertainment':'entertainment-karaoke','room-living':'living-room','room-kitchen':'kitchen-dining','room-master':'master-bedroom','room-bedroom-2':'bedroom-2','room-bedroom-3':'bedroom-3','room-bathrooms':'bathrooms'}
CARD={'en':{'room-entertainment':'Karaoke & entertainment','room-living':'Living room','room-kitchen':'Kitchen & dining','room-master':'Master bedroom','room-bedroom-2':'Bedroom 2','room-bedroom-3':'Bedroom 3','room-bathrooms':'Bathrooms','rooftop':'Rooftop terrace'},
      'de':{'room-entertainment':'Karaoke & Entertainment','room-living':'Wohnzimmer','room-kitchen':'Küche & Essbereich','room-master':'Hauptschlafzimmer','room-bedroom-2':'Schlafzimmer 2','room-bedroom-3':'Schlafzimmer 3','room-bathrooms':'Bäder','rooftop':'Dachterrasse'}}
ROOMSH={'en':'The rooms in detail','de':'Die Räume im Detail'}
def load(l,f,faq_page=False):
    m,S,I,F,C=parse(open(f'{SRC}/{l}/{f}.md').read(),faq_page)
    w=f
    m={k:clean(l,v,w) for k,v in m.items()}
    secs=[]
    for s in S:
        sec={'h2':clean(l,s['h2'],w)}
        fl=cl_flow(l,s['flow'],w)
        if fl: sec['flow']=fl
        if s['faq']: sec['faq']=cl_faq(l,s['faq'],w)
        secs.append(sec)
    imgs=[[i,clean(l,a,w)] for i,a in I]
    faq=cl_faq(l,F,w); cta=[clean(l,c,w) for c in C]; cta=[c for c in cta if c]
    return m,secs,imgs,faq,cta
def tail(l,faq,cta):
    t=[]
    if faq: t.append({'h2':FAQH[l],'faq':faq})
    t.append({'p':cta,'cta':True} if cta else {'cta':True})
    return t
def setmeta(P,m,keep=()):
    for k in('title','description','h1','lead'):
        if k in m and k not in keep: P[k]=m[k]
def roomcards(l,C,pids):
    return {'h2':ROOMSH[l],'cards':[[CARD[l][p],p,C['pages'][p]['description'] if p in C['pages'] else ''] for p in pids]}
for l in('en','de'):
    path=f'content/{l}.json'; d=json.load(open(path)); P=d['pages']; old=copy.deepcopy(P)
    # rooms
    for pid,f in ROOMF.items():
        m,secs,imgs,faq,cta=load(l,'rooms/'+f)
        pg={'title':m['title'],'description':m['description'],'h1':m['h1'],'lead':m.get('lead','')}
        if imgs: pg['cover']=imgs[0]
        if len(imgs)>1: secs[0]['imgs']=imgs[1:]
        pg['sections']=secs+tail(l,faq,cta); P[pid]=pg
    rp=list(ROOMF)+['rooftop']
    # rooftop
    m,secs,imgs,faq,cta=load(l,'rooms/rooftop'); setmeta(P['rooftop'],m)
    if imgs: secs[0]['imgs']=imgs
    P['rooftop']['sections']=secs+tail(l,faq,cta)
    # house overview: room cards + entertainment long text in place of the entertainment section
    m,esecs,eimgs,efaq,ecta=load(l,'entertainment')
    if eimgs: esecs[0]['imgs']=eimgs
    hs=[]
    for s in old['house']['sections']:
        if any(i[0]=='ent' for i in s.get('imgs',[])): hs.extend(esecs)
        else: hs.append(s)
    P['house']['sections']=[roomcards(l,d,rp)]+hs
    # home
    m,secs,imgs,faq,cta=load(l,'index'); setmeta(P['home'],m,keep=('title','h1'))
    hero=[a for i,a in imgs if i=='hero']; 
    if hero: P['home']['hero']=['hero',re.sub(r'\s*\(photo \d+\)','',hero[0])]
    gal=[[i,a] for i,a in imgs if i!='hero']
    if gal: secs[0]['imgs']=gal
    explore=[s for s in old['home']['sections'] if 'cards' in s]
    for s in secs:
        if re.search(r'room by room|Raum für Raum',s['h2']): s['cards']=roomcards(l,d,rp)['cards']
    P['home']['sections']=secs+explore+tail(l,faq,cta)
    # families / groups
    for pid in('families','groups'):
        m,secs,imgs,faq,cta=load(l,pid); setmeta(P[pid],m,keep=('h1',) if (l=='de' and pid=='groups') else ())
        if imgs: secs[0]['imgs']=imgs
        P[pid]['sections']=secs+[roomcards(l,d,rp)]+tail(l,faq,cta)
    # location
    m,secs,imgs,faq,cta=load(l,'location'); setmeta(P['location'],m)
    if imgs: secs[0]['imgs']=imgs
    mp=[s for s in old['location']['sections'] if 'google.com/maps' in json.dumps(s)]
    P['location']['sections']=secs+mp+tail(l,faq,cta)
    # guide hub
    m,secs,imgs,faq,cta=load(l,'travel-guide'); setmeta(P['guide'],m)
    cards=[s for s in old['guide']['sections'] if 'cards' in s]; btn=[s for s in old['guide']['sections'] if 'note' in s]
    P['guide']['sections']=secs[:1]+cards+secs[1:2]+btn+secs[2:]+tail(l,faq,cta)
    alt=dict(imgs)
    for s in P['guide-app']['sections']:
        for i in s.get('imgs',[]):
            if i[0] in alt: i[1]=alt[i[0]]
    # faq
    m,secs,imgs,faq,cta=load(l,'faq',True); setmeta(P['faq'],m)
    P['faq']['sections']=secs+[{'p':cta,'cta':True} if cta else {'cta':True}]
    # booking: MR sections, then booking buttons + existing contact block (+ Zalo)
    m,secs,imgs,faq,cta=load(l,'booking'); setmeta(P['booking'],m)
    contact=[s for s in old['booking']['sections'] if 'tel:' in json.dumps(s)]
    for c in contact:
        if not any('zalo' in x.lower() for x in c['p']): c['p'].insert(1,'Zalo: <a href="https://zalo.me/84909410382" rel="noopener">{phone}</a>')
        c['h2']=[s['h2'] for s in secs if re.search(r'Contact|Kontakt',s['h2'])][0] if any(re.search(r'Contact|Kontakt',s['h2']) for s in secs) else c['h2']
    secs=[s for s in secs if not re.search(r'^(Contact|Kontakt)$',s['h2'])]
    P['booking']['sections']=secs+[{'cta':True}]+contact+([{'h2':FAQH[l],'faq':faq}] if faq else [])
    # house rules
    m,secs,imgs,faq,cta=load(l,'house-rules'); setmeta(P['rules'],m)
    P['rules']['sections']=secs+tail(l,faq,cta)
    json.dump(d,open(path,'w'),ensure_ascii=False,indent=1)
for x in LOG: print(*x,sep=' | ')
