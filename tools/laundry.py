"""Laundry service price (owner-confirmed 18 Oct 2026): 30 EUR per load, shown in every language.
Applied by build.py to the loaded content, so re-running the per-language import builders never loses it.
1) Inserts the price right after every 'laundry service' phrase in body text/FAQ answers (not titles/descriptions/headings).
2) Washing-machine FAQ answers without a laundry price get one sentence appended (visible text and FAQ schema stay identical).
Idempotent; languages that already state 30 EUR (en, de, vi, hi, ur, pa) are untouched."""
import re
P={ # lang: (service-phrase regex, price tag inserted after it, sentence for FAQ answers, washing-machine question regex)
 'ar':(r'خدمة غسيل الملابس',' (30 EUR لكل غسلة)',' وتتوفر أيضًا خدمة غسيل الملابس (30 EUR لكل غسلة).',r'غسال'),
 'es':(r'[Ss]ervicio de lavandería',' (30 EUR por carga)',' También hay servicio de lavandería (30 EUR por carga).',r'lavadora'),
 'fr':(r'[Ss]ervice de blanchisserie',' (30 EUR par machine)',' Un service de blanchisserie est aussi proposé (30 EUR par machine).',r'lave-linge|lessive'),
 'it':(r'[Ss]ervizio lavanderia',' (30 EUR a lavaggio)',' Su richiesta c\'è anche il servizio lavanderia (30 EUR a lavaggio).',r'lavatrice|bucato'),
 'pt':(r'[Ss]erviço de lavanderia',' (30 EUR por lavagem)',' Também há serviço de lavanderia (30 EUR por lavagem).',r'máquina de lavar|lavar roupa'),
 'nl':(r'[Ww]asservice',' (30 EUR per wasbeurt)',' Er is ook een wasservice (30 EUR per wasbeurt).',r'wasmachine|wassen'),
 'pl':(r'usług[aęi] prania',' (30 EUR za pranie)',' Na życzenie dostępna jest też usługa prania (30 EUR za pranie).',r'pralk|prać|pranie'),
 'sv':(r'[Tt]vättservice',' (30 EUR per maskin)',' Tvättservice finns också (30 EUR per maskin).',r'tvättmaskin|tvätta'),
 'ru':(r'[Уу]слуг[аи] стирки|^Стирка(?= — по запросу)',' (30 EUR за загрузку)',' Также есть услуга стирки (30 EUR за загрузку).',r'стиральн|стира'),
 'tr':(r'[Çç]amaşır hizmeti',' (yıkama başına 30 EUR)',' Çamaşır hizmeti de var (yıkama başına 30 EUR).',r'çamaşır makine'),
 'id':(r'[Ll]ayanan laundry',' (30 EUR per muatan)',' Layanan laundry juga tersedia (30 EUR per muatan).',r'mesin cuci'),
 'ms':(r'[Ss]ervis dobi',' (30 EUR setiap muatan)',' Servis dobi juga tersedia (30 EUR setiap muatan).',r'mesin basuh'),
 'th':(r'บริการซักรีด',' (30 EUR ต่อครั้ง)',' มีบริการซักรีดด้วย (30 EUR ต่อครั้ง)',r'เครื่องซักผ้า'),
 'ko':(r'세탁 서비스','(1회 30 EUR)',' 세탁 서비스(1회 30 EUR)도 요청할 수 있습니다.',r'세탁기'),
 'ja':(r'ランドリーサービス','（1回30 EUR）','ランドリーサービス（1回30 EUR）もご依頼いただけます。',r'洗濯'),
 'zh':(r'洗衣服务','（每次 30 EUR）','也可申请洗衣服务（每次 30 EUR）。',r'洗衣机'),
 'zh-tw':(r'洗衣服務','（每次 30 EUR）','也可以安排洗衣服務（每次 30 EUR）。',r'洗衣機'),
}
SKIP={'title','description','h1','h2','meta','alt'}
def _tag(s,rx,tag):
    if '30 EUR' in s: return s
    return re.sub(rx,lambda m:m.group(0)+tag,s,flags=re.M)
def _walk(o,rx,tag,sent,qrx,key=None):
    if isinstance(o,dict):
        return {k:(v if k in SKIP else _walk(v,rx,tag,sent,qrx,k)) for k,v in o.items()}
    if isinstance(o,list):
        if key=='faq':
            out=[]
            for qa in o:
                if isinstance(qa,list) and len(qa)>=2 and isinstance(qa[0],str) and isinstance(qa[1],str):
                    q,a=qa[0],_tag(qa[1],rx,tag)
                    if re.search(qrx,q,re.I) and '30 EUR' not in a: a=a.rstrip()+sent
                    out.append([q,a]+qa[2:])
                else: out.append(_walk(qa,rx,tag,sent,qrx))
            return out
        if len(o)==2 and o[0] in ('h2','h3','h4') : return o
        return [_walk(v,rx,tag,sent,qrx,key) for v in o]
    if isinstance(o,str): return _tag(o,rx,tag)
    return o
def apply(lang,data):
    if lang not in P: return data
    rx,tag,sent,qrx=P[lang]
    out=dict(data)
    if 'pages' in out: out['pages']=_walk(out['pages'],rx,tag,sent,qrx)
    return out
