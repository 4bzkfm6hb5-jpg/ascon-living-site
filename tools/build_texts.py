import json,re,sys,copy
sys.path.insert(0,'tools'); from import_texts import parse,split_pages
SRC='/workspace/ascon-texts'
FIX={ # Website Ops pre-check corrections (applied to delivered copy)
'en':[(" There is a smoke detector and a first-aid kit on every floor.",""),(" Every floor has a smoke detector and a first-aid kit.",""),
 (", a laundry service is available, and there's a smoke detector and first-aid kit on every floor.",", and a laundry service is available."),
 (" Solar lights keep the mood warm after dark.","",'groups'),
 ("Quiet hours from 21:30 mean everyone gets a good night's sleep.","Loud music only until 21:30 means everyone gets a good night's sleep."),
 ("Just remember the house quiet hours: loud music goes down from 21:30,","Just remember the house rule: loud music only until 21:30,"),
 ("Please keep in mind the house quiet hours: loud music goes down from 21:30,","Please keep in mind the house rule: loud music only until 21:30,"),
 ("and quiet hours from 21:30 keep things friendly with the neighbours.","and loud music only until 21:30 keeps things friendly with the neighbours."),
 ("Back at the house, quiet hours from 21:30 keep things relaxed","Back at the house, loud music only until 21:30 keeps things relaxed"),
 ("Smoke detector and first-aid kit on every floor, outdoor cameras only","Cameras outdoors only, none inside the house"),
 ("in the Ho Chi Minh villa","in the private house in Ho Chi Minh City"),("Entertainment room with sofas, a villa with karaoke in Ho Chi Minh City","Entertainment room with sofas, a private house with karaoke in Ho Chi Minh City"),
 ("Ho Chi Minh Villa: Entire Private House | ASCON LIVING","Ho Chi Minh Private House for Your Stay | ASCON LIVING"),("Ho Chi Minh villa: the entire private house, just for you","Ho Chi Minh private house: the entire home, just for you")],
'de':[(" Auf jeder Etage gibt es einen Rauchmelder und einen Erste-Hilfe-Kasten.",""),(", ein Wäscheservice ist möglich, und auf jeder Etage gibt es Rauchmelder und Erste-Hilfe-Kasten.",", und ein Wäscheservice ist möglich."),
 ("Die Ruhezeiten ab 21:30 Uhr sorgen dafür, dass alle gut schlafen.","Laute Musik nur bis 21:30 Uhr, so schlafen alle gut."),
 ("Denkt nur an die Ruhezeiten: Ab 21:30 Uhr wird laute Musik leiser gestellt,","Denkt nur an die Hausregel: laute Musik nur bis 21:30 Uhr,"),
 ("Bitte denkt an die Ruhezeiten: Ab 21:30 Uhr wird laute Musik leiser gestellt,","Bitte denkt an die Hausregel: laute Musik nur bis 21:30 Uhr,"),
 ("und die Ruhezeiten ab 21:30 Uhr sorgen für ein gutes Verhältnis zu den Nachbarn.","und laute Musik nur bis 21:30 Uhr sorgt für ein gutes Verhältnis zu den Nachbarn."),
 ("Im Haus sorgen die Ruhezeiten ab 21:30 Uhr für eine entspannte Atmosphäre,","Im Haus gilt: laute Musik nur bis 21:30 Uhr, das sorgt für eine entspannte Atmosphäre,"),
 ("Rauchmelder und Erste-Hilfe-Kasten auf jeder Etage, Kameras nur außen","Kameras nur außen, keine im Haus"),
 ("in der Villa in Ho-Chi-Minh-Stadt","im privaten Haus in Ho-Chi-Minh-Stadt"),("Entertainment-Raum mit Sofas, Villa mit Karaoke in Ho-Chi-Minh-Stadt","Entertainment-Raum mit Sofas, Ferienhaus mit Karaoke in Ho-Chi-Minh-Stadt")]}
LOG=[]
def fix(l,pid,s):
    if not isinstance(s,str): return s
    for f in FIX[l]:
        a,b=f[0],f[1]
        if len(f)>2 and f[2]!=pid: continue
        if a in s: s=s.replace(a,b); LOG.append((l,pid,a.strip()[:70],b.strip()[:70]))
    return s
def deep(l,pid,o):
    if isinstance(o,dict): return {k:deep(l,pid,v) for k,v in o.items()}
    if isinstance(o,list): return [deep(l,pid,v) for v in o]
    return fix(l,pid,o)
def apply_meta(P,m):
    for k in('title','description','h1','lead'):
        if k in m: P[k]=m[k]
def sec(s,keep=None):
    o={}
    for k in('h2','note','p','ul','imgs','table'):
        if k in s: o[k]=s[k]
    return o
CARDPID=['house','rooftop','families','groups','location','booking']
for l in ('en','de'):
    p=f'content/{l}.json'; d=json.load(open(p)); P=d['pages']; old=copy.deepcopy(P)
    rd=lambda f: open(f'{SRC}/{l}/{f}.md').read()
    # HOME
    m,S=parse(rd('index')); S=[s for s in S if '_hdr' in s]
    H=P['home']; apply_meta(H,m)
    hero=[s for s in S if 'imgs' in s and s['imgs'][0][0]=='hero'][0]; H['hero']=['hero',hero['imgs'][0][1]]
    H['sections']=[sec(S[0]),{'h2':S[1]['h2'],'ul':S[1]['ul']},{'h2':old['home']['sections'][2].get('h2'),'cards':[[t,CARDPID[i],dsc] for i,(t,dsc) in enumerate(S[2]['cards'])]},{'cta':True}]
    # HOUSE
    m,S=parse(rd('house')); S=[s for s in S if '_hdr' in s]; apply_meta(P['house'],m)
    P['house']['sections']=[sec(s) for s in S]+[{'cta':True}]
    # ROOFTOP
    m,S=parse(rd('rooftop')); S=[s for s in S if '_hdr' in s]; apply_meta(P['rooftop'],m)
    P['rooftop']['sections']=[sec(s) for s in S]+[{'cta':True}]
    # FAMILIES / GROUPS
    for pid in('families','groups'):
        m,S=parse(rd(pid)); S=[s for s in S if '_hdr' in s]
        P.setdefault(pid,{}); apply_meta(P[pid],m); P[pid]['sections']=[sec(s) for s in S if sec(s)]+[{'cta':True}]
    # LOCATION
    m,S=parse(rd('location')); S=[s for s in S if '_hdr' in s]; apply_meta(P['location'],m)
    mp=old['location']['sections'][2]; mp['h2']=S[2].get('h2',mp['h2'])
    P['location']['sections']=[sec(S[0]),sec(S[1]),mp,{'cta':True}]
    # GUIDE + GUIDE-APP
    A,B=split_pages(rd('travel-guide'))
    m,S=parse(A); S=[s for s in S if '_hdr' in s]; apply_meta(P['guide'],m)
    cards=old['guide']['sections'][0]['cards']; newc=[x for s in S if 'cards' in s for x in s['cards']]
    for c,(t,dsc) in zip(cards,newc): c[0]=t; c[2]=dsc
    notes=[s for s in S if s.get('p') and re.search(r'Note under|Hinweis unter',s['_hdr'])]
    btn=old['guide']['sections'][1]
    if notes: btn['note']=notes[0]['p'][0]
    P['guide']['sections']=[sec(S[0]),{'cards':cards},btn]
    m,S=parse(B); S=[s for s in S if '_hdr' in s]; apply_meta(P['guide-app'],m)
    og=old['guide-app']['sections']
    s1=sec(S[0]); s2=sec(S[1]); s2['ul']=og[1]['ul']
    s3=copy.deepcopy(og[2]); opt=re.search(r'["“](.+?)["”]\s*$',' '.join(S[2].get('p',[])))
    if opt and opt.group(1) not in ' '.join(s3['p']): s3['p'][-1]+=' '+opt.group(1)
    rest=og[3:]
    nb=[s for s in S if re.search(r'Note \+ button|Hinweis \+ Button',s['_hdr'])]
    if nb and rest:
        for r in rest:
            if 'note' in r: r['note']=re.sub(r'\s*\[.*\]\s*$','',nb[0]['p'][0])
    P['guide-app']['sections']=[s1,s2,s3]+rest
    for pid in list(P): P[pid]=deep(l,pid,P[pid])
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
for x in LOG: print(*x,sep=' | ')
