"""Oct 18 confirmations (Zishan via Madara): washing machine + laundry service 30 EUR/load, guest WC equipped like the other
bathrooms, bedrooms 2+3 open off the anteroom, entertainment-room TV is 4K."""
import json
def walk(o,fn):
    if isinstance(o,str): return fn(o)
    if isinstance(o,list): return [walk(x,fn) for x in o]
    if isinstance(o,dict): return {k:walk(v,fn) for k,v in o.items()}
    return o
def rep(d,pairs,exact=()):
    hits={a:0 for a,_ in pairs}; ex={a:0 for a,_ in exact}
    def fn(s):
        for a,b in exact:
            if s==a: ex[a]+=1; return b
        for a,b in pairs:
            if a in s: hits[a]+=1; s=s.replace(a,b)
        return s
    d=walk(d,fn); miss=[a for a,n in list(hits.items())+list(ex.items()) if n==0]
    assert not miss,miss; return d
EN=[("and a big TV in your house","and a big 4K TV in your house"),("and a big wall-mounted TV.","and a big wall-mounted 4K TV."),
 ("Large wall-mounted TV","Large wall-mounted 4K TV"),("a large wall-mounted TV, a sectional","a large wall-mounted 4K TV, a sectional"),
 ("Airport transfer with your booking, laundry service on request","Airport transfer with your booking, washing machine, laundry service (30 EUR per load)"),
 ("an iron is on hand, and a laundry service is available for longer stays.","an iron is on hand, guests may use the washing machine, and a laundry service is available for 30 EUR per load."),
 ("Bedding, towels, toiletries, slippers, hot water, iron, safe","Bedding, towels, toiletries, slippers, hot water, iron, washing machine, safe"),
 ("A laundry service is available on request, handy for longer stays or when you travel light.","Guests may use the washing machine in the kitchen area. A laundry service is also available for 30 EUR per load, handy for longer stays or when you travel light."),
 ("Is there a laundry service?","Is there a washing machine or a laundry service?"),
 ("Yes, a laundry service is available on request. There is also an iron in the house.","Yes. Guests may use the washing machine in the kitchen area, and a laundry service is available for 30 EUR per load. There is also an iron in the house."),
 ("hot water are ready, and a laundry service is available.","hot water are ready, guests may use the washing machine, and a laundry service is available for 30 EUR per load."),
 ("lead to a bright landing with two bedroom doors, a desk","lead to a bright landing with the doors to bedrooms 2 and 3 and a desk"),
 ("Two black panel doors stand side by side and lead into two of the bedrooms.","Two black panel doors stand side by side: one leads into bedroom 2, the other into bedroom 3."),
 ("3 private en-suite bathrooms plus guest WC","3 private en-suite bathrooms plus a guest WC equipped like the other bathrooms"),
 ("plus a guest WC in the living area.","plus a guest WC in the living area, equipped like the other bathrooms."),
 ("and there is a guest WC in the living area.","and there is a guest WC in the living area, equipped like the other bathrooms."),
 ("The guest WC is right in the living area.","The guest WC is right in the living area and is equipped like the other bathrooms."),
 ("Yes, there is a guest WC in the living area, in addition","Yes, there is a guest WC in the living area, equipped like the other bathrooms, in addition"),
 ("one per bedroom, plus a guest WC in the living area","one per bedroom, plus a guest WC in the living area, equipped like the other bathrooms"),
 ("The guest WC lies in the living area.","The guest WC lies in the living area and is equipped like the other bathrooms.")]
EN_EX=[("Laundry service","Washing machine and laundry service"),("Two black panel doors side by side","Two black panel doors side by side: bedroom 2 and bedroom 3"),
 ("In the living area","In the living area, equipped like the other bathrooms")]
DE=[("und großem Fernseher in eurem Haus","und großem 4K-Fernseher in eurem Haus"),("ein großer Fernseher an der Wand","ein großer 4K-Fernseher an der Wand"),
 ("Großer Fernseher an der Wand","Großer 4K-Fernseher an der Wand"),
 ("Flughafentransfer mit der Buchung, Wäscheservice auf Anfrage","Flughafentransfer mit der Buchung, Waschmaschine, Wäscheservice (30 EUR pro Ladung)"),
 ("ein Bügeleisen ebenfalls, und für längere Aufenthalte gibt es einen Wäscheservice.","ein Bügeleisen ebenfalls, die Waschmaschine dürft ihr nutzen, und es gibt einen Wäscheservice für 30 EUR pro Ladung."),
 ("Bettwäsche, Handtücher, Pflegeprodukte, Hausschuhe, Warmwasser, Bügeleisen, Safe","Bettwäsche, Handtücher, Pflegeprodukte, Hausschuhe, Warmwasser, Bügeleisen, Waschmaschine, Safe"),
 ("Auf Anfrage gibt es einen Wäscheservice, praktisch bei längeren Aufenthalten oder leichtem Gepäck.","Die Waschmaschine im Küchenbereich dürft ihr nutzen. Außerdem gibt es einen Wäscheservice für 30 EUR pro Ladung, praktisch bei längeren Aufenthalten oder leichtem Gepäck."),
 ("Gibt es einen Wäscheservice?","Gibt es eine Waschmaschine oder einen Wäscheservice?"),
 ("Ja, auf Anfrage. Ein Bügeleisen ist ebenfalls im Haus.","Ja. Die Waschmaschine im Küchenbereich dürft ihr nutzen, und der Wäscheservice kostet 30 EUR pro Ladung. Ein Bügeleisen ist ebenfalls im Haus."),
 ("warmes Wasser sind da, und ein Wäscheservice ist möglich.","warmes Wasser sind da, die Waschmaschine dürft ihr nutzen, und ein Wäscheservice ist für 30 EUR pro Ladung möglich."),
 ("führt in einen hellen Flur mit zwei Schlafzimmertüren, einem Schreibtisch","führt in einen hellen Flur mit den Türen zu Schlafzimmer 2 und 3 und einem Schreibtisch"),
 ("Zwei schwarze Kassettentüren stehen nebeneinander und führen in zwei der Schlafzimmer.","Zwei schwarze Kassettentüren stehen nebeneinander: Die eine führt in Schlafzimmer 2, die andere in Schlafzimmer 3."),
 ("3 eigene Bäder en suite plus Gäste-WC","3 eigene Bäder en suite plus ein Gäste-WC, ausgestattet wie die anderen Bäder"),
 ("dazu ein Gäste-WC im Wohnbereich.","dazu ein Gäste-WC im Wohnbereich, ausgestattet wie die anderen Bäder."),
 ("dazu gibt es ein Gäste-WC im Wohnbereich.","dazu gibt es ein Gäste-WC im Wohnbereich, ausgestattet wie die anderen Bäder."),
 ("dazu kommt ein Gäste-WC im Wohnbereich.","dazu kommt ein Gäste-WC im Wohnbereich, ausgestattet wie die anderen Bäder."),
 ("Das Gäste-WC liegt direkt im Wohnbereich.","Das Gäste-WC liegt direkt im Wohnbereich und ist ausgestattet wie die anderen Bäder."),
 ("Ja, ein Gäste-WC im Wohnbereich, zusätzlich","Ja, ein Gäste-WC im Wohnbereich, ausgestattet wie die anderen Bäder, zusätzlich"),
 ("eines pro Schlafzimmer, dazu ein Gäste-WC im Wohnbereich","eines pro Schlafzimmer, dazu ein Gäste-WC im Wohnbereich, ausgestattet wie die anderen Bäder"),
 ("Das Gäste-WC liegt im Wohnbereich.","Das Gäste-WC liegt im Wohnbereich und ist ausgestattet wie die anderen Bäder.")]
DE_EX=[("Wäscheservice","Waschmaschine und Wäscheservice"),("Zwei schwarze Kassettentüren nebeneinander","Zwei schwarze Kassettentüren nebeneinander: Schlafzimmer 2 und Schlafzimmer 3"),
 ("Im Wohnbereich","Im Wohnbereich, ausgestattet wie die anderen Bäder")]
K={'en':dict(row=['Laundry corner','Front-loading washing machine that guests may use, laundry bags beside it'],
  h2='Laundry corner',p=['A front-loading washing machine stands in the corner of the kitchen area, with laundry bags beside it. Guests may use it, which is practical on longer stays and for families with children.','Prefer not to wash yourself? A laundry service is available for 30 EUR per load.'],
  imgs=[['kitchen-laundry','Front-loading washing machine in the corner of the kitchen area'],['kitchen-laundry-2','Two laundry bags by the wall next to the kitchen area']],
  faq=['Can we wash clothes?','Yes. Guests may use the front-loading washing machine in the kitchen area, and a laundry service is available for 30 EUR per load.'],
  appl=('a kettle, air fryer, toaster','a kettle, air fryer, toaster'),
  house='Guests may also use the washing machine in the kitchen area, and a laundry service is available for 30 EUR per load.'),
 'de':dict(row=['Waschecke','Frontlader-Waschmaschine, die ihr nutzen dürft, daneben Wäschesäcke'],
  h2='Die Waschecke',p=['In der Ecke des Küchenbereichs steht eine Frontlader-Waschmaschine, daneben Wäschesäcke. Ihr dürft sie nutzen, praktisch bei längeren Aufenthalten und für Familien mit Kindern, die nach einem Tag am Spielplatz oder auf dem Markt frische Kleidung brauchen.','Lieber waschen lassen? Der Wäscheservice kostet 30 EUR pro Ladung.'],
  imgs=[['kitchen-laundry','Frontlader-Waschmaschine in der Ecke des Küchenbereichs'],['kitchen-laundry-2','Zwei Wäschesäcke an der Wand neben dem Küchenbereich']],
  faq=['Können wir Wäsche waschen?','Ja. Die Frontlader-Waschmaschine im Küchenbereich dürft ihr nutzen, und der Wäscheservice kostet 30 EUR pro Ladung.'],
  house='Die Waschmaschine im Küchenbereich dürft ihr ebenfalls nutzen, und der Wäscheservice kostet 30 EUR pro Ladung.')}
for l,pairs,ex in (('en',EN,EN_EX),('de',DE,DE_EX)):
    f=f'content/{l}.json'; d=json.load(open(f)); P=d['pages']
    # exact cell edits scoped to the right pages
    P['booking' if any(isinstance(x,list) and x==['h3','Laundry service' if l=='en' else 'Wäscheservice'] for s in P['booking']['sections'] for x in s.get('flow',[])) else 'booking']
    for pid in P:
        P[pid]=rep(P[pid],[(a,b) for a,b in pairs if any(a in json.dumps(P[pid],ensure_ascii=False) for _ in [0])]) if False else P[pid]
    d['pages']=rep(P,pairs)
    P=d['pages']
    # exact strings, scoped
    lab,new=ex[0]
    for pid,p in P.items():
        for s in p['sections']:
            for x in s.get('flow',[]):
                if x==['h3',lab]: x[1]=new
    hall=P['room-hallway']['sections'][0]['flow'][0][1]['rows']; r=[x for x in hall if x[1]==ex[1][0]]; assert r; r[0][1]=ex[1][1]
    liv=P['room-living']['sections'][0]['flow'][0][1]['rows']; r=[x for x in liv if x[1]==ex[2][0]]; assert r; r[0][1]=ex[2][1]
    k=K[l]; kp=P['room-kitchen']['sections']
    rows=kp[0]['flow'][0][1]['rows']
    if not any(x[0]==k['row'][0] for x in rows):
        i=[n for n,x in enumerate(rows) if x[0] in('Coffee machine','Kaffeemaschine')][0]; rows.insert(i+1,k['row'])
    if not any(s.get('h2')==k['h2'] for s in kp):
        i=[n for n,s in enumerate(kp) if s.get('h2','').startswith(('How the kitchen','So spielt'))][0]
        kp.insert(i,{'h2':k['h2'],'flow':[['p',x] for x in k['p']],'imgs':k['imgs']})
    fq=[s for s in kp if s.get('faq')][0]['faq']
    if not any(q==k['faq'][0] for q,_ in fq): fq.insert(1,k['faq'])
    fq[0][1]=fq[0][1].replace('kettle, air fryer, toaster and','kettle, air fryer, toaster, dishwasher, coffee machine, washing machine and').replace('Wasserkocher, Heißluftfritteuse, Toaster und','Wasserkocher, Heißluftfritteuse, Toaster, Geschirrspüler, Kaffeemaschine, Waschmaschine und')
    assert 'ashing' in fq[0][1] or 'Waschmaschine' in fq[0][1]
    hk=[s for s in P['house']['sections'] if s.get('h2','').startswith(('Kitchen','Küche'))][0]
    if k['house'] not in hk['p'][1]: hk['p'][1]+=' '+k['house']
    json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
# other languages
O={'vi':[("Bàn ủi; dịch vụ giặt ủi theo yêu cầu (30 EUR mỗi mẻ)","Máy giặt cho khách dùng, bàn ủi; dịch vụ giặt ủi (30 EUR mỗi mẻ)"),
  ("Có bàn ủi, và dịch vụ giặt ủi theo yêu cầu (30 EUR mỗi mẻ).","Có máy giặt cho khách dùng và bàn ủi, ngoài ra có dịch vụ giặt ủi (30 EUR mỗi mẻ)."),
  ("ngoài ra có WC cho khách ở khu sinh hoạt chung.","ngoài ra có WC cho khách ở khu sinh hoạt chung, trang bị như các phòng tắm khác."),
  ("karaoke, máy chiếu, TV và PlayStation","karaoke, máy chiếu, TV 4K và PlayStation"),("Hành lang với cửa các phòng","Hành lang với cửa phòng ngủ 2 và 3")],
 'hi':[("इस्त्री; अनुरोध पर लॉन्ड्री सेवा (30 EUR प्रति लोड)","मेहमानों के लिए वॉशिंग मशीन, इस्त्री; लॉन्ड्री सेवा (30 EUR प्रति लोड)"),
  ("इस्त्री है, और अनुरोध पर लॉन्ड्री सेवा (30 EUR प्रति लोड)।","मेहमानों के लिए वॉशिंग मशीन और इस्त्री है, साथ ही लॉन्ड्री सेवा (30 EUR प्रति लोड)।"),
  ("एक अतिरिक्त गेस्ट WC है।","एक अतिरिक्त गेस्ट WC है, जो बाकी बाथरूम की तरह सुसज्जित है।"),
  ("कराओके, प्रोजेक्टर, TV और PlayStation","कराओके, प्रोजेक्टर, 4K TV और PlayStation"),("कमरों के दरवाज़ों वाला गलियारा","बेडरूम 2 और 3 के दरवाज़ों वाला गलियारा")],
 'ur':[("استری؛ درخواست پر لانڈری سروس (30 EUR فی لوڈ)","مہمانوں کے لیے واشنگ مشین، استری؛ لانڈری سروس (30 EUR فی لوڈ)"),
  ("استری موجود ہے، اور درخواست پر لانڈری سروس (30 EUR فی لوڈ)۔","مہمانوں کے لیے واشنگ مشین اور استری موجود ہیں، ساتھ ہی لانڈری سروس (30 EUR فی لوڈ)۔"),
  ("ایک اضافی گیسٹ WC ہے۔","ایک اضافی گیسٹ WC ہے، جو باقی باتھ رومز کی طرح آراستہ ہے۔"),
  ("کراؤکے، پروجیکٹر، TV اور PlayStation","کراؤکے، پروجیکٹر، 4K TV اور PlayStation"),("کمروں کے دروازوں والی راہداری","بیڈروم 2 اور 3 کے دروازوں والی راہداری")],
 'pa':[("ਪ੍ਰੈੱਸ; ਬੇਨਤੀ 'ਤੇ ਲਾਂਡਰੀ ਸੇਵਾ (30 EUR ਪ੍ਰਤੀ ਲੋਡ)","ਮਹਿਮਾਨਾਂ ਲਈ ਵਾਸ਼ਿੰਗ ਮਸ਼ੀਨ, ਪ੍ਰੈੱਸ; ਲਾਂਡਰੀ ਸੇਵਾ (30 EUR ਪ੍ਰਤੀ ਲੋਡ)"),
  ("ਪ੍ਰੈੱਸ ਹੈ, ਅਤੇ ਬੇਨਤੀ 'ਤੇ ਲਾਂਡਰੀ ਸੇਵਾ (30 EUR ਪ੍ਰਤੀ ਲੋਡ)।","ਮਹਿਮਾਨਾਂ ਲਈ ਵਾਸ਼ਿੰਗ ਮਸ਼ੀਨ ਅਤੇ ਪ੍ਰੈੱਸ ਹਨ, ਨਾਲ ਹੀ ਲਾਂਡਰੀ ਸੇਵਾ (30 EUR ਪ੍ਰਤੀ ਲੋਡ)।"),
  ("ਇੱਕ ਵਾਧੂ ਗੈਸਟ WC ਹੈ।","ਇੱਕ ਵਾਧੂ ਗੈਸਟ WC ਹੈ, ਜੋ ਬਾਕੀ ਬਾਥਰੂਮਾਂ ਵਾਂਗ ਸੁਸੱਜਿਤ ਹੈ।"),
  ("ਕਰਾਓਕੇ, ਪ੍ਰੋਜੈਕਟਰ, TV ਅਤੇ PlayStation","ਕਰਾਓਕੇ, ਪ੍ਰੋਜੈਕਟਰ, 4K TV ਅਤੇ PlayStation"),("ਕਮਰਿਆਂ ਦੇ ਦਰਵਾਜ਼ਿਆਂ ਵਾਲਾ ਗਲਿਆਰਾ","ਬੈੱਡਰੂਮ 2 ਅਤੇ 3 ਦੇ ਦਰਵਾਜ਼ਿਆਂ ਵਾਲਾ ਗਲਿਆਰਾ")]}
for l,pairs in O.items():
    f=f'content/{l}.json'; d=json.load(open(f)); d['pages']=rep(d['pages'],pairs); json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
    a=f'content/alts/{l}.json'; s=open(a).read()
    for x,y in pairs: s=s.replace(x,y)
    open(a,'w').write(s)
F=json.load(open('facts.json'))
am=F['amenities'] if 'amenities' in F else None
print(type(am))
