"""Publish house photos as EXIF-free WebP and AVIF at several widths.

Originals live in photos/fertig_v2 and ascon-photos when present. Otherwise the
WebP files already in docs/assets/img are reused (renamed, not recompressed)
and an AVIF sibling is encoded beside each one.
"""
import os, json, sys
from PIL import Image, ImageOps, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
from house_alts import SLUG

ROOT=os.path.join(os.path.dirname(__file__), '..')
OUT=os.path.join(ROOT, 'docs', 'assets', 'img')
META_PATH=os.path.join(os.path.dirname(__file__), 'images.json')
os.makedirs(OUT, exist_ok=True)
SRC=os.environ.get('ASCON_PHOTOS', '/workspace/photos/fertig_v2')
BLUE_DIR=os.environ.get('ASCON_BLUE', '/workspace/ascon-photos')
WIDTHS=[480, 960, 1440]
AVIF_Q=50
WEBP_Q=70

PICK={'roof-lounge':'Rooftop/020_746A9684','roof-day':'Rooftop/021_746A9696',
'roof-night':'Rooftop/022_746A9772','roof-evening':'Rooftop/023_746A9778','roof-evening-2':'Rooftop/024_746A9782',
'roof-skyline':'Rooftop/104_IMG_74314ee3','roof-bbq':'Rooftop/036_746A9682',
'living':'Wohnzimmer/002_746A9488','living-2':'Wohnzimmer/003_746A9486','living-tv':'Wohnzimmer/004_746A9482','living-3':'Wohnzimmer/006_746A9498',
'kitchen':'Kueche/007_IMG_593f8e35','kitchen-dining':'Kueche/010_746A9517','kitchen-2':'Kueche/009_746A9522','kitchen-3':'Kueche/038_746A9528','kitchen-fridge':'Kueche/060_IMG_f524b050','kitchen-dishes':'Kueche/039_746A9533','kitchen-rice':'Kueche/042_746A9539','kitchen-micro':'Kueche/059_IMG_3b30a3b4',
'bed1':'Schlafzimmer_1/011_746A9548','bed1-2':'Schlafzimmer_1/012_746A9578','bed1-3':'Schlafzimmer_1/043_746A9561',
'bed2':'Schlafzimmer_2/013_746A9623','bed2-2':'Schlafzimmer_2/014_746A9632','bed2-3':'Schlafzimmer_2/044_746A9631',
'bed3':'Schlafzimmer_3/015_746A9660','bed3-2':'Schlafzimmer_3/016_746A9650','bed3-3':'Schlafzimmer_3/045_746A9657',
'bath':'Bad/017_746A9570','bath-2':'Bad/018_746A9668','bath-3':'Bad/019_746A9641','bath-4':'Bad/136_746A9639','bath-5':'Bad/148_746A9671','bath-6':'Bad/124_746A9575',
'ent':'Karaoke/030_746A9717','ent-karaoke':'Karaoke/031_746A9715','ent-cinema':'Karaoke/032_746A9748','ent-tv':'Karaoke/033_746A9723','ent-mics':'Karaoke/034_746A9724','ent-ps':'Karaoke/035_746A9726',
'hall-desk':'Vorraum_Flur/056_IMG_f7f68425','hall-landing':'Vorraum_Flur/130_746A9605','hall-vanity':'Vorraum_Flur/048_746A9598','hall-window':'Vorraum_Flur/129_746A9602','hall-prints':'Vorraum_Flur/057_IMG_8aa67c29','hall-entry':'Vorraum_Flur/051_746A9514','hall-shoes':'Vorraum_Flur/052_746A9506','hall-stairs-2':'Vorraum_Flur/151_746A9675','hall-lamp':'Vorraum_Flur/053_746A9703',
'kitchen-counter':'Kueche/111_746A9532','living-tvwall':'Wohnzimmer/005_746A9795','bed1-vanity':'Schlafzimmer_1/118_746A9554','bed1-charge':'Schlafzimmer_1/120_746A9562','bed1-wardrobe':'Schlafzimmer_1/121_746A9567','bed2-wardrobe':'Schlafzimmer_2/138_746A9643','bed3-wardrobe':'Schlafzimmer_3/143_746A9656','bath-dryer':'Bad/137_746A9642','ent-led':'Karaoke/067_IMG_ca58fea3',
'workspace-2':'Vorraum_Flur/065_IMG_df507390',
'kitchen-laundry':'Kueche/041_IMG_b0373da4','kitchen-laundry-2':'Kueche/113_746A9538',
'hall':'Vorraum_Flur/047_746A9604','stairs':'Vorraum_Flur/049_746A9790','entrance':'Vorraum_Flur/050_746A9502'}
BLUE={'hero':'064','roof-terrace':'064','river-balcony':'019','river-city':'080'}
BLUR={'kitchen-laundry':(690,285,1040,500)}

def save_variants(im, slug, meta):
    im=im.convert('RGB')
    im.thumbnail((1440, 1440))
    w, h=im.size
    widths=[]
    for W in WIDTHS:
        if W>w: continue
        r=im if W==w else im.resize((W, round(h*W/w)), Image.LANCZOS)
        r.save(f'{OUT}/{slug}-{W}.webp', 'WEBP', quality=WEBP_Q, method=6)
        r.save(f'{OUT}/{slug}-{W}.avif', 'AVIF', quality=AVIF_Q, speed=6)
        widths.append(W)
    return {'w':w, 'h':h, 'widths':widths, 'file':slug}

def from_existing(name, slug):
    # Reuse already-published WebP (do not recompress) and add AVIF.
    widths=[]
    size=None
    for W in WIDTHS:
        src=None
        for stem in (name, slug):
            p=f'{OUT}/{stem}-{W}.webp'
            if os.path.exists(p):
                src=p
                break
        if not src:
            continue
        im=Image.open(src).convert('RGB')
        if size is None or W>=max(widths or [0]):
            size=im.size
        dest=f'{OUT}/{slug}-{W}.webp'
        if os.path.abspath(src)!=os.path.abspath(dest):
            __import__('shutil').copyfile(src, dest)
        im.save(f'{OUT}/{slug}-{W}.avif', 'AVIF', quality=AVIF_Q, speed=6)
        widths.append(W)
    if not widths:
        raise SystemExit(f'no source for {name}')
    w, h=size
    return {'w':w, 'h':h, 'widths':widths, 'file':slug}

def open_jpg(path):
    im=Image.open(path)
    im=ImageOps.exif_transpose(im).convert('RGB')
    return im

meta={}
written=set()
for name in list(PICK)+list(BLUE):
    slug=SLUG[name]
    if slug in written:
        # Same pixels as an earlier id (hero/roof-terrace, hall-prints/workspace-2).
        meta[name]=dict(next(v for k,v in meta.items() if v['file']==slug))
        continue
    jpg=None
    if name in PICK and os.path.isfile(f'{SRC}/{PICK[name]}.jpg'):
        jpg=open_jpg(f'{SRC}/{PICK[name]}.jpg')
        if name in BLUR:
            b=BLUR[name]
            jpg.paste(jpg.crop(b).filter(ImageFilter.GaussianBlur(28)), b[:2])
    elif name in BLUE and os.path.isfile(f'{BLUE_DIR}/{BLUE[name]}.jpg'):
        jpg=open_jpg(f'{BLUE_DIR}/{BLUE[name]}.jpg')
    if jpg is not None:
        meta[name]=save_variants(jpg, slug, meta)
    else:
        meta[name]=from_existing(name, slug)
    written.add(slug)

# Drop the old short filenames once the descriptive file is in place.
for name, slug in SLUG.items():
    if name==slug:
        continue
    info=meta[name]
    for W in info['widths']:
        old=f'{OUT}/{name}-{W}.webp'
        new=f'{OUT}/{slug}-{W}.webp'
        if os.path.isfile(old) and os.path.abspath(old)!=os.path.abspath(new):
            os.remove(old)

# Logos and favicon when the brand master is available; otherwise keep published files.
brand='/workspace/brand/ascon_logo_transparent.png'
if os.path.isfile(brand):
    lg=Image.open(brand).convert('RGBA')
    mark=lg.crop((0,0,lg.width,int(lg.height*0.48))); mark=mark.crop(mark.getbbox())
    m=mark.copy(); m.thumbnail((200,96)); m.save(f'{OUT}/logo-mark.webp','WEBP',quality=90)
    m.save(f'{OUT}/logo-mark.png', optimize=True)
    meta['logo-mark']={'w':m.width,'h':m.height}
    f=mark.copy(); f.thumbnail((180,180)); c=Image.new('RGBA',(180,180),(255,255,255,0)); c.paste(f,((180-f.width)//2,(180-f.height)//2),f)
    c.save(os.path.join(OUT,'..','..','favicon.png'))
    full=lg.crop(lg.getbbox()); full.thumbnail((400,600)); full.save(f'{OUT}/logo-full.webp','WEBP',quality=90)
    meta['logo-full']={'w':full.width,'h':full.height}
    if os.path.isfile(f'{BLUE_DIR}/064.jpg'):
        im=Image.open(f'{BLUE_DIR}/064.jpg').convert('RGB'); w,h=im.size
        t=1200/630; cw=min(w,int(h*t)); ch=int(cw/t); x=(w-cw)//2; y=(h-ch)//2
        im.crop((x,y,x+cw,y+ch)).resize((1200,630), Image.LANCZOS).save(f'{OUT}/og.jpg','JPEG',quality=78,optimize=True,progressive=True)
else:
    prev=json.load(open(META_PATH))
    for k in ('logo-mark','logo-full'):
        meta[k]=prev[k]

# App and travel-guide screenshots stay on their current names; add AVIF beside each WebP.
import glob
for p in glob.glob(f'{OUT}/*.webp'):
    base=os.path.basename(p)
    if base.startswith('logo-'):
        continue
    stem, width=base.rsplit('-',1)
    width=int(width[:-5])
    if stem in SLUG or any(v['file']==stem for v in meta.values() if 'file' in v):
        continue
    av=p[:-5]+'.avif'
    if not os.path.isfile(av):
        Image.open(p).convert('RGB').save(av,'AVIF',quality=AVIF_Q,speed=6)

for n in ['app-category','app-place','app-map','app-practical','app-place@de','app-category@de','app-practical@de','app-map@de']+[f'tg-{k}{v}' for k in ('welcome','picker','categories','map','practical') for v in ('','@de','@vi','@ko','@ja','@zh','@fr','@es','@pt','@ar','@zh-tw')]:
    ws=[w for w in (390,780,366) if os.path.exists(f'{OUT}/{n}-{w}.webp')]
    if not ws:
        continue
    im2=Image.open(f'{OUT}/{n}-{ws[0]}.webp')
    meta[n]={'w':im2.width,'h':im2.height,'widths':ws,'file':n}
    for w in ws:
        av=f'{OUT}/{n}-{w}.avif'
        if not os.path.isfile(av):
            Image.open(f'{OUT}/{n}-{w}.webp').convert('RGB').save(av,'AVIF',quality=AVIF_Q,speed=6)

json.dump(meta, open(META_PATH,'w'), indent=1)
print(len(PICK)+len(BLUE), 'house photos;', sum(1 for v in meta.values() if 'widths' in v), 'with widths')
