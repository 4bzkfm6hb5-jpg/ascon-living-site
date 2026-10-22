"""Subset the installed Noto fonts used by hi/ar/ur/pa and write woff2 + metrics.

The family name is "Site …", not Noto: a subset is a modified font under the SIL
Open Font License and must not reuse the reserved name. font-display:swap is
applied by build.py. See OFL.txt.
"""
import json, os
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

ROOT=os.path.join(os.path.dirname(__file__), '..')
OUT=os.path.join(os.path.dirname(__file__), 'fonts')
os.makedirs(OUT, exist_ok=True)
NOTO='/usr/share/fonts/truetype/noto'
SPECS=[
    ('Noto Sans Arabic', 'Site Arabic', 'site-arabic', 'NotoSansArabic',
     ['ar'], ['Noto Sans Arabic', 'Noto Naskh Arabic', 'Tahoma', 'Arial']),
    ('Noto Sans Devanagari', 'Site Devanagari', 'site-devanagari', 'NotoSansDevanagari',
     ['hi'], ['Noto Sans Devanagari', 'Nirmala UI', 'Mangal']),
    ('Noto Nastaliq Urdu', 'Site Urdu', 'site-urdu', 'NotoNastaliqUrdu',
     ['ur'], ['Noto Nastaliq Urdu']),
    ('Noto Sans Gurmukhi', 'Site Gurmukhi', 'site-gurmukhi', 'NotoSansGurmukhi',
     ['pa'], ['Noto Sans Gurmukhi', 'Nirmala UI']),
]

def text_for(codes):
    chars=set(map(chr, range(32, 127)))
    chars.update('ASCON LIVING WhatsApp Zalo Vietnam Main –—‘’“”…·×©')
    chars.update(open(f'{ROOT}/facts.json', encoding='utf-8').read())
    for c in codes:
        p=f'{ROOT}/content/{c}.json'
        if os.path.isfile(p):
            chars.update(open(p, encoding='utf-8').read())
    return ''.join(sorted(chars))

def rename(font, family, style):
    ps=(family+'-'+style).replace(' ', '')
    full=f'{family} {style}'
    name=font['name']
    def put(nameID, value):
        name.setName(value, nameID, 3, 1, 0x409)
        name.setName(value, nameID, 1, 0, 0)
    put(1, family); put(2, style); put(4, full); put(6, ps); put(16, family); put(17, style)

def subset(src, text, dest, family, style):
    font=TTFont(src)
    opt=Options()
    opt.flavor='woff2'
    opt.layout_features=['*']
    opt.name_IDs=['*']
    opt.notdef_outline=True
    opt.recommended_glyphs=True
    opt.drop_tables=['DSIG']
    opt.ignore_missing_glyphs=True
    opt.desubroutinize=True
    sub=Subsetter(options=opt)
    sub.populate(text=text)
    sub.subset(font)
    rename(font, family, style)
    font.flavor='woff2'
    font.save(dest)
    return os.path.getsize(dest)

def metrics(path):
    f=TTFont(path)
    os2=f['OS/2']; up=f['head'].unitsPerEm
    pct=lambda v: f'{abs(v)/up*100:.1f}%'
    return pct(os2.sTypoAscender), pct(os2.sTypoDescender), pct(os2.sTypoLineGap)

meta={}
for key, family, stem, file_stem, codes, locals_ in SPECS:
    text=text_for(codes)
    regular=f'{NOTO}/{file_stem}-Regular.ttf'
    bold=f'{NOTO}/{file_stem}-Bold.ttf'
    a=subset(regular, text, f'{OUT}/{stem}-400.woff2', family, 'Regular')
    b=subset(bold, text, f'{OUT}/{stem}-700.woff2', family, 'Bold')
    asc, desc, gap=metrics(f'{OUT}/{stem}-400.woff2')
    meta[key]={'family':family,'ascent':asc,'descent':desc,'lineGap':gap,
               'locals':locals_,'files':{'400':f'{stem}-400.woff2','700':f'{stem}-700.woff2'}}
    print(f'{family}: {a//1024}KB + {b//1024}KB  ascent {asc} descent {desc}')
json.dump(meta, open(f'{OUT}/metrics.json','w'), indent=1)
print('fonts ok')
