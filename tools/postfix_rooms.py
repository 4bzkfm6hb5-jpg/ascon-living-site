"""Re-apply Website Ops / owner fixes on top of a fresh MR room build (idempotent). Run after build_rooms_mr2.py."""
import json
def sub_all(o,a,b):
    if isinstance(o,str): return o.replace(a,b) if a in o and b not in o else o
    if isinstance(o,list): return [sub_all(x,a,b) for x in o]
    if isinstance(o,dict): return {k:sub_all(v,a,b) for k,v in o.items()}
    return o
T={'en':dict(dish=[['Dishwasher','Yes'],['Coffee machine','Yes']],fryer='Air fryer and toaster',lrow=['Laundry service','30 EUR per load'],
   lh2='Laundry corner',lp='Prefer not to wash yourself? A laundry service is available for 30 EUR per load.',
   limgs=[['kitchen-laundry','Front-loading washing machine in the corner of the kitchen area'],['kitchen-laundry-2','Two laundry bags by the wall next to the kitchen area']],
   faqa=('kettle, air fryer, toaster and','kettle, air fryer, toaster, dishwasher, coffee machine, washing machine and'),
   faqn=['Can we wash clothes?','Yes. Guests are welcome to use the front-loading washing machine in the kitchen area, and a laundry service is available for 30 EUR per load.'],
   S=[('room-entertainment','a big TV in your house','a big 4K TV in your house'),('room-entertainment','Large wall-mounted TV,','Large wall-mounted 4K TV,'),
      ('room-living','Yes, there is a guest WC in the living area, in addition','Yes, there is a guest WC in the living area, equipped the same way as the other bathrooms, in addition'),
      ('room-bathrooms','and there is a guest WC in the living area. Matte','and there is a guest WC in the living area, equipped the same way as the other bathrooms. Matte'),
      ('room-bathrooms','one per bedroom, plus a guest WC in the living area','one per bedroom, plus a guest WC in the living area, equipped the same way as the other bathrooms'),
      ('room-bathrooms','and there is a guest WC in the living area.','and there is a guest WC in the living area, equipped the same way as the other bathrooms.'),
      ('room-hallway','Two black panel doors side by side','Two black panel doors side by side: bedroom 2 and bedroom 3')],
   hall_eq="What's here"),
 'de':dict(dish=[['Geschirrspüler','Ja'],['Kaffeemaschine','Ja']],fryer='Heißluftfritteuse und Toaster',lrow=['Wäscheservice','30 EUR pro Ladung'],
   lh2='Die Waschecke',lp='Lieber waschen lassen? Der Wäscheservice kostet 30 EUR pro Ladung.',
   limgs=[['kitchen-laundry','Frontlader-Waschmaschine in der Ecke des Küchenbereichs'],['kitchen-laundry-2','Zwei Wäschesäcke an der Wand neben dem Küchenbereich']],
   faqa=('Wasserkocher, Heißluftfritteuse, Toaster und','Wasserkocher, Heißluftfritteuse, Toaster, Geschirrspüler, Kaffeemaschine, Waschmaschine und'),
   faqn=['Können wir Wäsche waschen?','Ja. Gäste dürfen die Frontlader-Waschmaschine im Küchenbereich benutzen, und der Wäscheservice kostet 30 EUR pro Ladung.'],
   S=[('room-entertainment','und großem Fernseher in eurem Haus','und großem 4K-Fernseher in eurem Haus'),('room-entertainment','Großer Fernseher an der Wand,','Großer 4K-Fernseher an der Wand,'),
      ('room-living','Ja, ein Gäste-WC im Wohnbereich, zusätzlich','Ja, ein Gäste-WC im Wohnbereich, genauso ausgestattet wie die anderen Bäder, zusätzlich'),
      ('room-bathrooms','und im Wohnbereich gibt es ein Gäste-WC. Matt','und im Wohnbereich gibt es ein Gäste-WC, genauso ausgestattet wie die anderen Bäder. Matt'),
      ('room-bathrooms','eines pro Schlafzimmer, dazu ein Gäste-WC im Wohnbereich','eines pro Schlafzimmer, dazu ein Gäste-WC im Wohnbereich, genauso ausgestattet wie die anderen Bäder'),
      ('room-bathrooms','dazu kommt ein Gäste-WC im Wohnbereich.','dazu kommt ein Gäste-WC im Wohnbereich, genauso ausgestattet wie die anderen Bäder.'),
      ('room-hallway','Zwei schwarze Kassettentüren nebeneinander','Zwei schwarze Kassettentüren nebeneinander: Schlafzimmer 2 und Schlafzimmer 3')],
   hall_eq=None)}
for l,t in T.items():
    f=f'content/{l}.json'; d=json.load(open(f)); P=d['pages']
    for pid,a,b in t['S']:
        before=json.dumps(P[pid],ensure_ascii=False); P[pid]=sub_all(P[pid],a,b)
        assert b in json.dumps(P[pid],ensure_ascii=False),(l,pid,a)
    k=P['room-kitchen']['sections']; rows=k[0]['flow'][0][1]['rows']; names=[r[0] for r in rows]
    i=names.index(t['fryer'])+1
    for r in reversed(t['dish']):
        if r[0] not in names: rows.insert(i,r)
    names=[r[0] for r in rows]
    if t['lrow'][0] not in names:
        j=[n for n,r in enumerate(rows) if 'aschmaschine' in r[1] or 'washing machine' in r[1]][0]; rows.insert(j+1,t['lrow'])
    ls=[s for s in k if s.get('h2')==t['lh2']]; assert ls,(l,'laundry section')
    ls=ls[0]
    if not any(x==['p',t['lp']] for x in ls['flow']): ls['flow'].append(['p',t['lp']])
    have={i[0] for s in k for i in s.get('imgs',[])}
    if 'kitchen-laundry' not in have: ls['imgs']=t['limgs']
    fq=[s for s in k if s.get('faq')][0]['faq']
    fq[0][1]=fq[0][1].replace(*t['faqa']) if t['faqa'][1] not in fq[0][1] else fq[0][1]
    if not any(q==t['faqn'][0] for q,_ in fq): fq.insert(1,t['faqn'])
    if t['hall_eq']: P['room-hallway']['sections'][0]['h2']=t['hall_eq']
    for pg in P.values():
        for s in pg.get('sections',[]):
            for c in s.get('cards',[]):
                if c[1].startswith('room-') and c[1] in P: c[2]=P[c[1]]['description']
    json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
print('postfix ok')
