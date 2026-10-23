"""Owner's original house photos -> web sizes. Resize + EXIF rotate only; no colour/brightness edits.
Source: /workspace/hausfertige-bilder/<room folder>. Output: docs/assets/img/orig-<room>-<n>-<w>.(webp|avif).
Guest-app screenshots: /workspace/ascon-app/lang/<lang>/<lang>-1-welcome-home.png and -2-amenities.png, copied fresh on every build."""
import os, json
from PIL import Image, ImageOps
SRC=os.environ.get('ORIG_SRC','/workspace/hausfertige-bilder')
APP=os.environ.get('APP_SRC','/workspace/ascon-app/lang')
# folder -> (slug, page id of the room)
ROOMS=[('rooftop','rooftop','rooftop'),('wohnzimmer','living','room-living'),('karaoke','entertainment','room-entertainment'),
       ('kuche','kitchen','room-kitchen'),('schlaf zimmer 1','bedroom-1','room-master'),('schlafzimmer 2','bedroom-2','room-bedroom-2'),
       ('sclaf zimmer 3','bedroom-3','room-bedroom-3'),('vorraum','hallway','room-hallway')]
HERO=('rooftop','75.jpg')
WIDTHS=[480,960,1440]
def _save(im, base, out, widths=WIDTHS):
    ws=[]
    for w in widths:
        if w>im.width and ws: break
        r=im if im.width<=w else im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
        r.save(f'{out}/{base}-{r.width}.webp','WEBP',quality=82,method=6)
        r.save(f'{out}/{base}-{r.width}.avif','AVIF',quality=60)
        ws.append(r.width)
    return ws
def _key(f): 
    n=os.path.splitext(f)[0]; return (0,int(n)) if n.isdigit() else (1,n)
def build(out):
    cache=f'{os.path.dirname(os.path.abspath(__file__))}/originals.json'
    if os.path.exists(cache) and not os.environ.get('ORIG_REBUILD'):
        meta=json.load(open(cache))
    else:
        meta={'rooms':{}, 'img':{}}
        for folder,slug,pid in ROOMS:
            keys=[]
            files=sorted([f for f in os.listdir(f'{SRC}/{folder}') if f.lower().endswith(('.jpg','.jpeg','.png'))], key=_key)
            for i,f in enumerate(files,1):
                im=ImageOps.exif_transpose(Image.open(f'{SRC}/{folder}/{f}')).convert('RGB')
                base=f'orig-{slug}-{i:02d}'
                ws=_save(im, base, out)
                key=base
                meta['img'][key]={'w':ws[-1],'h':round(im.height*ws[-1]/im.width),'widths':ws,'file':base,'room':pid}
                keys.append(key)
                if (folder,f)==HERO: meta['hero']=key
            meta['rooms'][slug]=keys
        json.dump(meta,open(cache,'w'),indent=1)
    # og image from the hero original
    h=meta['hero']
    if not os.path.exists(f'{out}/og.jpg') or os.environ.get('ORIG_REBUILD'):
        src=[f for f in os.listdir(f'{SRC}/rooftop') if f==HERO[1]][0]
        im=ImageOps.exif_transpose(Image.open(f'{SRC}/rooftop/{src}')).convert('RGB')
        im=ImageOps.fit(im,(1200,630)); im.save(f'{out}/og.jpg','JPEG',quality=85)
    return meta
APP_LANGS=['en','de','vi','zh','ko','ja','fr','es','pt','ar']
def app_shots(out):
    img={}
    for l in APP_LANGS:
        for n,name in ((1,'welcome-home'),(2,'amenities')):
            p=f'{APP}/{l}/{l}-{n}-{name}.png'
            if not os.path.exists(p): continue
            im=Image.open(p).convert('RGB'); base=f'guest-app-{l}-{n}'
            ws=_save(im, base, out, [390,780])
            key=f'ga-{n}' if l=='en' else f'ga-{n}@{l}'
            img[key]={'w':ws[-1],'h':round(im.height*ws[-1]/im.width),'widths':ws,'file':base}
    return img
