"""Convert selected real house photos to EXIF-free WebP in several widths."""
from PIL import Image
import os, json
SRC='/workspace/ascon-photos'
OUT=os.path.join(os.path.dirname(__file__),'..','docs','assets','img')
os.makedirs(OUT,exist_ok=True)
PICK={'hero':'021','roof-dining':'063','roof-river':'064','roof-night':'047','roof-lounge-night':'033',
'roof-evening':'068','roof-lounge':'093','roof-sofa':'098','skyline-night':'046','river-view':'080',
'river-boat':'069','balcony-river':'019','balcony':'012','living':'006','living-2':'016','living-3':'090',
'living-tv':'039','lounge':'001','dining':'029','dining-2':'058','kitchen':'014','kitchen-2':'018',
'kitchen-3':'052','bedroom-1':'020','bedroom-2':'026','bedroom-3':'095','bedroom-4':'003','bedroom-5':'008',
'bedroom-6':'083','bath':'035','bath-2':'043','projector':'094','bbq':'030','laundry':'078','stairs':'054'}
WIDTHS=[480,960,1440]
meta={}
for name,num in PICK.items():
    im=Image.open(f'{SRC}/{num}.jpg').convert('RGB')  # convert drops EXIF/GPS
    w,h=im.size; meta[name]={'w':w,'h':h,'widths':[]}
    for W in WIDTHS:
        if W>w: continue
        r=im.resize((W,round(h*W/w)),Image.LANCZOS)
        r.save(f'{OUT}/{name}-{W}.webp','WEBP',quality=70,method=6)
        meta[name]['widths'].append(W)
# OG image 1200x630 jpg
im=Image.open(f'{SRC}/021.jpg').convert('RGB'); w,h=im.size
t=1200/630; cw=min(w,int(h*t)); ch=int(cw/t); x=(w-cw)//2; y=(h-ch)//2
im.crop((x,y,x+cw,y+ch)).resize((1200,630),Image.LANCZOS).save(f'{OUT}/og.jpg','JPEG',quality=78,optimize=True,progressive=True)
# logo mark + favicon
lg=Image.open('/workspace/brand/ascon_logo_transparent.png').convert('RGBA')
mark=lg.crop((0,0,lg.width,int(lg.height*0.48))); mark=mark.crop(mark.getbbox())
m=mark.copy(); m.thumbnail((200,96)); m.save(f'{OUT}/logo-mark.webp','WEBP',quality=90); meta['logo-mark']={'w':m.width,'h':m.height}
m.save(f'{OUT}/logo-mark.png',optimize=True)
f=mark.copy(); f.thumbnail((180,180)); c=Image.new('RGBA',(180,180),(255,255,255,0)); c.paste(f,((180-f.width)//2,(180-f.height)//2),f); c.save(os.path.join(OUT,'..','..','favicon.png'))
full=lg.crop(lg.getbbox()); full.thumbnail((400,600)); full.save(f'{OUT}/logo-full.webp','WEBP',quality=90); meta['logo-full']={'w':full.width,'h':full.height}
json.dump(meta,open(os.path.join(os.path.dirname(__file__),'images.json'),'w'),indent=1)
print(len(PICK),'images')
