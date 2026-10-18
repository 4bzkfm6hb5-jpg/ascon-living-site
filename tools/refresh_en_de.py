"""Apply MR's 18 Oct EN/DE text revisions to content/en.json + de.json (idempotent).
Kept on purpose: 'loud music only until 21:30' (owner house rule), all earlier Ops/owner fixes."""
import json
R={'en':[("That makes it dark and quiet, which many guests find ideal for sleeping, especially","That makes it dark and quiet, which suits sleeping, especially"),
         ("The top of the house is a rooftop terrace of about 56–60 m², and it's where many guests spend their favourite hours.","The top of the house is a rooftop terrace of about 56–60 m².")],
   'de':[("Dadurch ist es dunkel und ruhig, was viele Gäste zum Schlafen ideal finden, besonders","Dadurch ist es dunkel und ruhig, ideal zum Schlafen, besonders"),
         ("Ganz oben im Haus liegt die rund 56–60 m² große Dachterrasse, und dort verbringen viele Gäste ihre schönsten Stunden.","Ganz oben im Haus liegt die rund 56–60 m² große Dachterrasse.")]}
def walk(x,l):
    if isinstance(x,str):
        for a,b in R[l]: x=x.replace(a,b)
        return x
    if isinstance(x,list): return [walk(y,l) for y in x]
    if isinstance(x,dict): return {k:walk(v,l) for k,v in x.items()}
    return x
for l in R:
    p=f'content/{l}.json'; d=json.load(open(p)); json.dump(walk(d,l),open(p,'w'),ensure_ascii=False,indent=1)
