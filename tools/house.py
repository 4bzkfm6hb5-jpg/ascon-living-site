"""Rebuild 'house' page imgs per room folder; alts per language. Usage: python3 tools/house.py en de vi"""
import json,sys
ORDER=[('living',['living','living-2','living-tv','living-3']),
('kitchen',['kitchen','kitchen-2','kitchen-3','kitchen-dishes','kitchen-rice','kitchen-micro','kitchen-fridge','kitchen-dining']),
('bed1',['bed1','bed1-3','bed1-2']),('bed2',['bed2','bed2-2','bed2-3']),('bed3',['bed3','bed3-2','bed3-3']),
('bath',['bath','bath-4','bath-2','bath-3','bath-5','bath-6']),
('ent',['ent','ent-karaoke','ent-cinema','ent-tv','ent-mics','ent-ps']),
('roof',['roof-terrace','roof-lounge','roof-night','roof-evening','roof-evening-2','roof-bbq','roof-skyline']),
('hall',['entrance','hall','stairs'])]
for code in sys.argv[1:]:
    c=json.load(open(f'content/{code}.json')); A=json.load(open(f'content/alts/{code}.json'))
    old=c['pages']['house']['sections']; H=A['_h']
    secs=[]
    for key,ids in ORDER:
        s={'h2':H[key][0]}
        if H[key][1]: s['p']=[H[key][1]]
        s['imgs']=[[i,A[i]] for i in ids]; secs.append(s)
    secs+= [x for x in old if 'ul' in x]+[{'cta':True}]
    c['pages']['house']['sections']=secs
    json.dump(c,open(f'content/{code}.json','w'),ensure_ascii=False,indent=1)
print('ok')
