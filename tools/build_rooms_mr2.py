"""Build Market Researcher final room texts (17:08) into room pages, EN/DE. Website Ops rules win. One-shot."""
import json,re,sys,os
sys.path.insert(0,'tools')
src=open('tools/build_long.py').read(); exec(src[:src.index("for l in('en','de'):")])  # defs: REP, DROP, clean, cl_flow, cl_faq, load, tail, LOG ...
SRCF='/workspace/photos/fertig_v2'
EXTRA_REP={'en':[("ASCON LIVING Riverside","ASCON LIVING"),("in your Ho Chi Minh house","in your house in Ho Chi Minh City"),("your Saigon house","your house in Saigon"),
 ("Riverside in Ho Chi Minh City: terraces, balcony and the river in front of your house","Riverside in Ho Chi Minh City: terraces and the river in front of your house"),
 (" (photo 064)",""),(" (photo 019)",""),(" (photo 080)","")],
 'de':[("ASCON LIVING Riverside","ASCON LIVING"),
 ("Am Fluss in Ho-Chi-Minh-Stadt: Terrassen, Balkon und das Wasser vor eurem Haus","Am Fluss in Ho-Chi-Minh-Stadt: Terrassen und das Wasser vor eurem Haus"),
 (" (Foto 064)",""),(" (Foto 019)",""),(" (Foto 080)","")]}
for l in EXTRA_REP: REP[l][:0]=EXTRA_REP[l]
EXTRA_DROP=r'|card lock|card reader|Kartenschloss|Kartenleser|fire.extinguisher|Feuerlöscher|exit sign|Notausgang|emergency light|Notbeleuchtung|Notleuchte|Fluchtweg|safety notice|Sicherheitshinweis'
DROP=re.compile(DROP.pattern+EXTRA_DROP)
PAGE_DROP={'room-outside':re.compile(r'(?i)balcon|Balkon|\bboats?\b|\bBoot(e|en)?\b|Holzboot|rattan'),'room-hallway':re.compile(r'(?i)balcon|Balkon')}
DROP_SECS=re.compile(r'(?i)^(Safety on every floor|Sicherheit auf jeder Etage|The covered balcony.*|Der überdachte Balkon.*)$')
DROP_ROWS=re.compile(r'(?i)^(Access|Zugang|Safety|Sicherheit)$')
MAP={'room-living':('living-room','Wohnzimmer'),'room-kitchen':('kitchen-dining','Kueche'),'room-entertainment':('entertainment-karaoke','Karaoke'),'room-master':('master-bedroom','Schlafzimmer_1'),
'room-bedroom-2':('bedroom-2','Schlafzimmer_2'),'room-bedroom-3':('bedroom-3','Schlafzimmer_3'),'room-bathrooms':('bathrooms','Bad'),'rooftop':('rooftop','Rooftop'),'room-hallway':('hallway-workspace','Vorraum_Flur'),'room-outside':('outdoor-river',None)}
ONLY={'room-living','room-kitchen','room-entertainment','room-bedroom-2','room-bedroom-3','room-bathrooms','room-hallway'}
BLUE={'hero','roof-terrace','river-balcony','river-city'}
NOFILE=set()  # laundry photos: washing machine not approved
ip=open('tools/images.py').read()
PICK=dict(re.findall(r"'([a-z0-9-]+)':'([A-Za-z_0-9]+/[A-Za-z_0-9]+)'",ip))
BYFILE={v:k for k,v in PICK.items()}
FOLDER={k:v.split('/')[0] for k,v in PICK.items()}
newpick={}; DROPPED=[]
EQH={'en':"What's in this room",'de':'Ausstattung'}
NEUT={'en':{'river-balcony':'Terrace railing framed by plants, with the city beyond','river-city':'View towards the District 1 skyline from the house','roof-terrace':'Rooftop terrace with skyline view','hero':'Rooftop terrace with skyline view'},
      'de':{'river-balcony':'Terrassengeländer mit Pflanzen, dahinter die Stadt','river-city':'Blick vom Haus auf die Skyline von Distrikt 1','roof-terrace':'Dachterrasse mit Blick auf die Skyline von Distrikt 1','hero':'Dachterrasse mit Blick auf die Skyline von Distrikt 1'}}
CAP={'en':{'river-balcony':'From the terrace railing, framed by plants','river-city':'Towards the District 1 skyline','roof-terrace':'The rooftop terrace','hero':'The rooftop terrace'},'de':{'river-balcony':'Am Terrassengeländer, umrahmt von Pflanzen','river-city':'Richtung Skyline von Distrikt 1','roof-terrace':'Die Dachterrasse','hero':'Die Dachterrasse'}}
RV=re.compile(r'(?i)river view|Flussblick')
def resolve(pid,folder,raw,l):
    m=re.match(r'([a-z0-9-]+)\s*(?:\((?:new|neu),\s*([^)]+)\))?',raw.strip())
    iid,f=m.group(1),m.group(2)
    if pid=='room-outside':
        if iid in BLUE and not f: return iid
        DROPPED.append((l,pid,'image '+raw+' (Ops: only 064/019/080 on outside page)')); return None
    if f:
        f=f.strip().rsplit('.',1)[0]; fo=f.split('/')[0]
        if fo!=folder or f.split('/')[1] in NOFILE: DROPPED.append((l,pid,'image '+raw+(' (washing machine not approved)' if f.split('/')[1] in NOFILE else ' (wrong folder)'))); return None
        if f in BYFILE: return BYFILE[f]
        nid=iid if iid not in PICK else iid+'-mr'
        PICK[nid]=f; BYFILE[f]=nid; FOLDER[nid]=fo; newpick[nid]=f; return nid
    if iid in BLUE or FOLDER.get(iid)==folder: return iid
    DROPPED.append((l,pid,'image '+raw+' (not from own folder)')); return None
def page_filter(pid,l,secs):
    pd=PAGE_DROP.get(pid); out=[]
    for s in secs:
        if DROP_SECS.match(s['h2']): DROPPED.append((l,pid,'section: '+s['h2'])); continue
        fl=[]
        for k,v in s.get('flow',[]):
            if k=='table':
                rows=[]
                for r in v['rows']:
                    if DROP_ROWS.match(r[0]) or (pd and any(pd.search(c) for c in r)): DROPPED.append((l,pid,'row: '+' | '.join(r))); continue
                    rows.append(r)
                v['rows']=rows; fl.append([k,v]); continue
            if k in('p','h3') and pd and pd.search(v):
                parts=re.split(r'(?<=[.!?])\s+',v); keep=[x for x in parts if not pd.search(x)]
                DROPPED.append((l,pid,'text: '+v[:90])); 
                if k=='h3' or not keep: continue
                v=' '.join(keep)
            if k=='ul' and pd: v=[x for x in v if not pd.search(x)]
            fl.append([k,v])
        # remove h3 without following content
        fl2=[]
        for i,(k,v) in enumerate(fl):
            if k=='h3' and (i+1==len(fl) or fl[i+1][0]=='h3'): continue
            fl2.append([k,v])
        s['flow']=fl2
        if fl2 or s.get('faq'): out.append(s)
        else: DROPPED.append((l,pid,'empty section: '+s['h2']))
    return out
for l in ('en','de'):
    p=f'content/{l}.json'; d=json.load(open(p)); P=d['pages']
    for pid,(fn,folder) in MAP.items():
        if pid not in ONLY: continue
        m,secs,imgs,faq,cta=load(l,'rooms/'+fn)
        pd=PAGE_DROP.get(pid)
        if pd:
            for k in ('description','lead'):
                if pd.search(m.get(k,'')): DROPPED.append((l,pid,k+' rewritten (balcony/boat)'))
        secs=page_filter(pid,l,secs)
        faq=[q for q in faq if not (pd and (pd.search(q[0]) or pd.search(q[1])))]
        im=[]
        for raw,alt in imgs:
            iid=resolve(pid,folder,raw,l)
            if iid and alt: im.append([iid,alt])
        pg=P.get(pid,{})
        pg.update({'title':m['title'],'description':m['description'],'h1':m['h1'],'lead':m.get('lead','')})
        if secs: secs[0]['h2']=EQH[l]
        if im: pg['cover']=im[0]
        else: pg.pop('cover',None)
        if len(im)>1:
            tgt=secs[1] if len(secs)>1 else secs[0]; tgt['imgs']=im[1:]
        pg['sections']=secs+tail(l,faq,cta); P[pid]=pg
    # outside page meta (balcony/boat removed)
    o=P['room-outside']
    if l=='en':
        o['description']='House at the river in Ho Chi Minh City with terraces, white railings and a view across the water to the District 1 skyline.'
        o['lead']='ASCON LIVING stands at the river. Terraces with white metal railings and awnings look across the water to the District 1 skyline, and the private rooftop sits above it all.'
    else:
        o['description']='Haus am Fluss in Ho-Chi-Minh-Stadt mit Terrassen, weißen Geländern und Blick über das Wasser auf die Skyline von Distrikt 1.'
        o['lead']='ASCON LIVING steht am Fluss. Terrassen mit weißem Metallgeländer und Markisen blicken über das Wasser auf die Skyline von Distrikt 1, und darüber liegt die private Dachterrasse.'
    # river-view alt cap: one per page; the kept one gets a neutral caption
    for pid,pg in P.items():
        items=([pg['cover']] if pg.get('cover') else [])+[i for s in pg.get('sections',[]) for i in s.get('imgs',[])]
        seen=False
        for i in items:
            if RV.search(i[1]):
                if not seen:
                    seen=True
                    if i is not pg.get('cover') and i[0] in CAP[l]:
                        if len(i)==2: i.append(CAP[l][i[0]])
                        else: i[2]=CAP[l][i[0]]
                else: i[1]=NEUT[l].get(i[0],RV.sub('view',i[1]))
    # refresh room card descriptions
    for pg in P.values():
        for s in pg.get('sections',[]):
            for c in s.get('cards',[]):
                if c[1] in P and c[1] in MAP: c[2]=P[c[1]]['description']
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
if newpick:
    add=''.join(f"'{k}':'{v}'," for k,v in newpick.items())
    ip=ip.replace("'hall':",add+"\n'hall':",1); open('tools/images.py','w').write(ip)
print('NEW IMAGES',newpick)
for x in DROPPED: print('DROP',*x,sep=' | ')
for x in LOG:
    if 'DROPPED' in x[2]: print('CLEAN',*x,sep=' | ')
