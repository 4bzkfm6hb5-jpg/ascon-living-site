"""Convert selected real house photos to EXIF-free WebP in several widths."""
from PIL import Image
import os, json
SRC='/workspace/photos/fertig_v2'
OUT=os.path.join(os.path.dirname(__file__),'..','docs','assets','img')
os.makedirs(OUT,exist_ok=True)
PICK={'hero':'Rooftop/021_746A9696','roof-lounge':'Rooftop/020_746A9684','roof-terrace':'Rooftop/021_746A9696',
'roof-night':'Rooftop/022_746A9772','roof-evening':'Rooftop/023_746A9778','roof-evening-2':'Rooftop/024_746A9782',
'roof-skyline':'Rooftop/104_IMG_74314ee3','roof-bbq':'Rooftop/036_746A9682',
'living':'Wohnzimmer/002_746A9488','living-2':'Wohnzimmer/003_746A9486','living-tv':'Wohnzimmer/004_746A9482','living-3':'Wohnzimmer/006_746A9498',
'kitchen':'Kueche/007_IMG_593f8e35','kitchen-dining':'Kueche/008_746A9521','kitchen-2':'Kueche/009_746A9522','kitchen-3':'Kueche/038_746A9528','kitchen-fridge':'Kueche/060_IMG_f524b050','kitchen-dishes':'Kueche/039_746A9533','kitchen-rice':'Kueche/042_746A9539','kitchen-micro':'Kueche/059_IMG_3b30a3b4',
'bed1':'Schlafzimmer_1/011_746A9548','bed1-2':'Schlafzimmer_1/012_746A9578','bed1-3':'Schlafzimmer_1/043_746A9561',
'bed2':'Schlafzimmer_2/013_746A9623','bed2-2':'Schlafzimmer_2/014_746A9632','bed2-3':'Schlafzimmer_2/044_746A9631',
'bed3':'Schlafzimmer_3/015_746A9660','bed3-2':'Schlafzimmer_3/016_746A9650','bed3-3':'Schlafzimmer_3/045_746A9657',
'bath':'Bad/017_746A9570','bath-2':'Bad/018_746A9668','bath-3':'Bad/019_746A9641','bath-4':'Bad/136_746A9639','bath-5':'Bad/148_746A9671','bath-6':'Bad/124_746A9575',
'ent':'Karaoke/030_746A9717','ent-karaoke':'Karaoke/031_746A9715','ent-cinema':'Karaoke/032_746A9748','ent-tv':'Karaoke/033_746A9723','ent-mics':'Karaoke/034_746A9724','ent-ps':'Karaoke/035_746A9726',
'hall':'Vorraum_Flur/047_746A9604','stairs':'Vorraum_Flur/049_746A9790','entrance':'Vorraum_Flur/050_746A9502'}
WIDTHS=[480,960,1440]
meta={}
for name,num in PICK.items():
    im=Image.open(f'{SRC}/{num}.jpg'); from PIL import ImageOps; im=ImageOps.exif_transpose(im).convert('RGB')  # drops EXIF/GPS
    im.thumbnail((1440,1440)); w,h=im.size; meta[name]={'w':w,'h':h,'widths':[]}
    for W in WIDTHS:
        if W>w: continue
        r=im.resize((W,round(h*W/w)),Image.LANCZOS)
        r.save(f'{OUT}/{name}-{W}.webp','WEBP',quality=70,method=6)
        meta[name]['widths'].append(W)
# OG image 1200x630 jpg
im=Image.open(f'{SRC}/Rooftop/021_746A9696.jpg').convert('RGB'); w,h=im.size
t=1200/630; cw=min(w,int(h*t)); ch=int(cw/t); x=(w-cw)//2; y=(h-ch)//2
im.crop((x,y,x+cw,y+ch)).resize((1200,630),Image.LANCZOS).save(f'{OUT}/og.jpg','JPEG',quality=78,optimize=True,progressive=True)
# logo mark + favicon
lg=Image.open('/workspace/brand/ascon_logo_transparent.png').convert('RGBA')
mark=lg.crop((0,0,lg.width,int(lg.height*0.48))); mark=mark.crop(mark.getbbox())
m=mark.copy(); m.thumbnail((200,96)); m.save(f'{OUT}/logo-mark.webp','WEBP',quality=90); meta['logo-mark']={'w':m.width,'h':m.height}
m.save(f'{OUT}/logo-mark.png',optimize=True)
f=mark.copy(); f.thumbnail((180,180)); c=Image.new('RGBA',(180,180),(255,255,255,0)); c.paste(f,((180-f.width)//2,(180-f.height)//2),f); c.save(os.path.join(OUT,'..','..','favicon.png'))
full=lg.crop(lg.getbbox()); full.thumbnail((400,600)); full.save(f'{OUT}/logo-full.webp','WEBP',quality=90); meta['logo-full']={'w':full.width,'h':full.height}
import glob
for n in ['app-categories','app-place','app-map','app-practical']:
    im2=Image.open(f'{OUT}/{n}-390.webp'); meta[n]={'w':390,'h':im2.height,'widths':[390,780]}
json.dump(meta,open(os.path.join(os.path.dirname(__file__),'images.json'),'w'),indent=1)
print(len(PICK),'images')
