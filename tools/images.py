"""Convert selected real house photos to EXIF-free WebP in several widths."""
from PIL import Image
import os, json
SRC='/workspace/photos/fertig_v2'
OUT=os.path.join(os.path.dirname(__file__),'..','docs','assets','img')
os.makedirs(OUT,exist_ok=True)
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
BLUE={'hero':'064','roof-terrace':'064','river-balcony':'019','river-city':'080'}  # blue-water river shots from /workspace/ascon-photos (owner-approved exception)
WIDTHS=[480,960,1440]
BLUR={'kitchen-laundry':(690,285,1040,500)}  # hide appliance brand logo (no brand names), coords on the exif-rotated original
meta={}
for name,num in PICK.items():
    im=Image.open(f'{SRC}/{num}.jpg'); from PIL import ImageOps; im=ImageOps.exif_transpose(im).convert('RGB')  # drops EXIF/GPS
    if name in BLUR:
        from PIL import ImageFilter; b=BLUR[name]; im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(28)),b[:2])
    im.thumbnail((1440,1440)); w,h=im.size; meta[name]={'w':w,'h':h,'widths':[]}
    for W in WIDTHS:
        if W>w: continue
        r=im.resize((W,round(h*W/w)),Image.LANCZOS)
        r.save(f'{OUT}/{name}-{W}.webp','WEBP',quality=70,method=6)
        meta[name]['widths'].append(W)
for name,num in BLUE.items():
    im=Image.open(f'/workspace/ascon-photos/{num}.jpg').convert('RGB'); w,h=im.size; meta[name]={'w':w,'h':h,'widths':[]}
    for W in WIDTHS:
        if W>w: continue
        im.resize((W,round(h*W/w)),Image.LANCZOS).save(f'{OUT}/{name}-{W}.webp','WEBP',quality=70,method=6); meta[name]['widths'].append(W)
# OG image 1200x630 jpg
im=Image.open('/workspace/ascon-photos/064.jpg').convert('RGB'); w,h=im.size
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
for n in ['app-category','app-place','app-map','app-practical','app-place@de','app-category@de','app-practical@de','app-map@de']+[f'tg-{k}{v}' for k in ('welcome','picker','categories','map','practical') for v in ('','@de','@vi','@ko','@ja','@zh','@fr','@es','@pt')]:  # tg-*: travel-guide app screenshots (live PWA, 390px phone), see /workspace/tg
    ws=[w for w in (390,780,366) if os.path.exists(f'{OUT}/{n}-{w}.webp')]; im2=Image.open(f'{OUT}/{n}-{ws[0]}.webp'); meta[n]={'w':im2.width,'h':im2.height,'widths':ws}
json.dump(meta,open(os.path.join(os.path.dirname(__file__),'images.json'),'w'),indent=1)
print(len(PICK),'images')
