"""Build KO / JA / ZH (zh-Hans) content from Market Researcher texts (/workspace/ascon-texts/{ko,ja,zh}) with all
Website Ops / owner rules applied. Writes content/{ko,ja,zh}.json. Re-runnable."""
import json,re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from import_long import parse
SRC='/workspace/ascon-texts'; LOG=[]
LANGS=('ko','ja','zh')
IMG=json.load(open('tools/images.json'))
ip=open('tools/images.py').read()
PICK=dict(re.findall(r"'([a-z0-9-]+)':'([A-Za-z_0-9]+/[A-Za-z_0-9]+)'",ip)); BYFILE={v:k for k,v in PICK.items()}; FOLDER={k:v.split('/')[0] for k,v in PICK.items()}
BLUE={'hero','roof-terrace','river-balcony','river-city'}
# ---------------- text rules ----------------
REP={'ko':[("열쇠)와 ASCON 가이드 앱 비밀번호를 보내드립니다.","열쇠)를 보내드립니다. ASCON 가이드 앱은 무료이며 비밀번호가 필요 없습니다."),
  ("ASCON LIVING 투숙객 전용 앱으로, 예약 후 비밀번호를 드립니다.","무료 앱이며 비밀번호가 필요 없습니다."),
  ("앱 비밀번호는 언제 받나요?","앱에 비밀번호가 필요한가요?"),("예약 후 보내드립니다. ASCON LIVING 투숙객 전용입니다.","아니요. 무료이며 휴대폰 브라우저에서 바로 열립니다."),
  ("예약하시면 가이드 앱 비밀번호를 함께 드립니다.","가이드 앱은 무료로 바로 쓸 수 있습니다."),("ASCON 가이드 앱 (예약 후 비밀번호 제공)","ASCON 가이드 앱 (무료, 비밀번호 불필요)"),
  ("투숙객 전용 ASCON 가이드 앱","무료 ASCON 가이드 앱"),("투숙객 전용 앱","무료 앱"),("가이드와 전용 앱으로","가이드와 무료 앱으로"),
  ("카카오톡 채널 아스콘리빙 (http://pf.kakao.com/_UuhmX)",'카카오톡 채널 <a href="http://pf.kakao.com/_UuhmX" rel="noopener">아스콘리빙</a>'),
  ("도착과 안전","도착과 체크인"),("안심하고 머무는 집","도착과 체크인"),("집과 설비 관리, 안전 설비 안내.","집과 설비 관리 안내."),("세탁기는 투숙객이 자유롭게 사용할 수 있고, 층마다 화재경보기와 구급상자가 있습니다.","세탁기는 투숙객이 자유롭게 사용할 수 있습니다."),("한국어로 먼저 상담","카카오톡으로 먼저 문의")],
 'ja':[("外門の鍵）と、ASCONガイドアプリのパスワードをお送りします。","外門の鍵）をお送りします。ASCONガイドアプリは無料で、パスワードは不要です。"),
  ("ASCON LIVINGのゲスト専用アプリで、ご予約後にパスワードをお送りします。","無料のアプリで、パスワードは不要です。"),
  ("アプリのパスワードはいつ届きますか。","アプリにパスワードは必要ですか。"),("ご予約後にお送りします。ASCON LIVINGのゲスト専用です。","いいえ。無料で、スマートフォンのブラウザですぐに開けます。"),
  ("ご予約いただくと、ガイドアプリのパスワードをお送りします。","ガイドアプリは無料ですぐにお使いいただけます。"),("ASCONガイドアプリ（ご予約後にパスワードをお送りします）","ASCONガイドアプリ（無料、パスワード不要）"),
  ("ゲスト専用のASCONガイドアプリ","無料のASCONガイドアプリ"),("ゲスト専用アプリ","無料アプリ"),("ガイドと専用アプリに","ガイドと無料アプリに"),
  ("到着と安全","到着とチェックイン"),("安心して過ごせる家","到着とチェックイン"),("家と設備の扱い、安全設備についてご案内します。","家と設備の扱いについてご案内します。"),("各階に火災警報器と救急箱があり、カメラは建物の外側のみに設置しています。","入口には屋外カメラがあります。")],
 'zh':[("外大门钥匙）和 ASCON 指南 App 密码。","外大门钥匙）。ASCON 指南 App 免费，无需密码。"),
  ("ASCON LIVING 住客专属，预订后提供密码。","免费使用，无需密码。"),
  ("App 密码什么时候给？","App 需要密码吗？"),("预订后发送，仅限 ASCON LIVING 住客。","不需要。免费，在手机浏览器中直接打开。"),
  ("预订后即可获得指南 App 密码。","指南 App 免费，打开即可使用。"),("ASCON 指南 App（预订后提供密码）","ASCON 指南 App（免费，无需密码）"),
  ("住客专属 ASCON 指南 App","免费 ASCON 指南 App"),("住客专属指南App","免费指南App"),("住客专属指南 App","免费指南 App"),("整理成攻略和专属 App","整理成攻略和免费 App"),
  ("入住与安全","入住须知"),("住得安心","入住与到达"),("爱护房屋设施、安全设施说明。","爱护房屋设施。"),("每层都有烟雾报警器和急救箱，摄像头只装在室外。","入口处装有室外摄像头。"),("每层有烟雾报警器、急救箱和灭火器，摄像头只在室外。","入口处装有室外摄像头。")]}
CAMN={'ko':'입구에는 실외 카메라가 있습니다.','ja':'入口には屋外カメラがあります。','zh':'入口处装有室外摄像头。'}
CAMCELL={'ko':'입구 실외 카메라','ja':'入口の屋外カメラ','zh':'入口处室外摄像头'}
CAMX={}
CAM=re.compile(r'카메라|カメラ|摄像头|監視|监控')
DROP=re.compile(r'(?i)가사|歌詞|歌词|화재경보기|화재 ?감지|연기 ?감지|구급상자|소화기|비상구|비상등|火災警報器|煙感知器|救急箱|消火器|非常口|非常灯|烟雾报警器|急救箱|灭火器|安全出口|应急灯|안전 설비|安全設備|安全设施|'
 r'카드키|카드 ?잠금|카드 ?리더|カードキー|カードロック|カードリーダー|房卡|门卡|刷卡|스마트 ?도어락|スマートロック|智能锁|智能门锁|\d+\s*(분|分钟|分)(?![子析配野別])|Landmark ?81|랜드마크 ?81|ランドマーク ?81|地标 ?81|'
 r'Phú Mỹ Hưng|Phu My Hung|푸미흥|フーミーフン|富美兴|富美興|빌라|ヴィラ|別墅|别墅|\bvilla\b|주차|駐車|パーキング|停车|泊车|parking|수영장|プール|泳池|游泳池|\bpool\b|PS5|Hisense|Optoma|\bFPT\b|\bLG\b|'
 r'Agoda|아고다|アゴダ|Vrbo|할랄|ハラール|清真|halal|짐 ?보관|荷物(の)?(お)?預か|手荷物預|行李寄存|寄存行李|반려동물|애완|(?<!カー)ペット|宠物|(?<!30 )\bEUR\b|유로|ユーロ|欧元|€|비밀번호를 (드립|보내)|パスワードをお送り|提供密码')
DROPQ=re.compile(r'안전|安全|집 안에 카메라|室内にカメラ|室内有摄像头')
DROP_SECS=re.compile(r'^(\d+\.\s*)?(안전|安全)$')
DROP_ROWS=re.compile(r'^(안전|安全)$')
CAMROW=re.compile(r'^(카메라|カメラ|摄像头)$')
PAGE_DROP={'room-outside':re.compile(r'발코니|バルコニー|阳台|라탄|ラタン|藤|나무배|배가 지나|보트|ボート|舟|船'),'room-hallway':re.compile(r'발코니|バルコニー|阳台')}
RV=re.compile(r'강 전망|강이 보이는|리버뷰|川の眺め|リバービュー|川が見える|川を望む|河景|江景')
PHOTO=re.compile(r'(?i)\s*[（(](?:사진|写真|照片|photo|foto|ภาพ|รูป|фото|ảnh|imagem|immagine|imagen)\s*\d+[)）]')
NOTE=re.compile(r'\s*[（(][^()（）]*(버튼|ボタン|按钮|유지|維持|保留)[^()（）]*[)）]')
SPLIT={}
FAQSECREN={}  # FAQ-page section renames (applied before DROP_SECS)  # per-language clause splitter (e.g. Thai: whitespace)
SENT=re.compile(r'.+?(?:[!?。！？]+\s*|\.(?:\s+|$)|$)')
def light(l,s):
    s=NOTE.sub('',PHOTO.sub('',s.replace('[live]','').replace('**','').strip()))
    for a,b in REP[l]: s=a.sub(b,s) if hasattr(a,'sub') else s.replace(a,b)
    return s
def clean(l,s,w,pid=None,cam_ok=True):
    if not isinstance(s,str): return s
    o=s; s=s.replace('[live]','').replace('**','').strip()
    s=NOTE.sub('',s); s=PHOTO.sub('',s)
    for a,b in REP[l]: s=a.sub(b,s) if hasattr(a,'sub') else s.replace(a,b)
    pd=PAGE_DROP.get(pid)
    out=[]; cam=False
    for p in SPLIT.get(l,SENT).findall(s):
        if DROP.search(p) or (pd and pd.search(p)): LOG.append((l,w,'DROPPED: '+p.strip()[:100])); continue
        if cam_ok and CAMX.get(l,CAM).search(p):
            if not cam: out.append(CAMN[l]+('' if l in ('ja','zh') else ' ')); cam=True
            LOG.append((l,w,'camera->neutral: '+p.strip()[:80])); continue
        out.append(p)
    s=''.join(out).strip()
    return s
def cl_flow(l,flow,w,pid):
    out=[]
    for k,v in flow:
        if k in('p','h3'):
            v=clean(l,v,w,pid,k=='p')
            if v: out.append([k,v])
        elif k=='ul':
            v=[clean(l,x,w,pid) for x in v]; v=[x for x in v if x]
            if v: out.append([k,v])
        elif k=='table':
            rows=[]; pd=PAGE_DROP.get(pid)
            for r in v['rows']:
                r=[light(l,c) for c in r]
                if DROP_ROWS.match(r[0]) or not r[0] or DROP.search(r[0]) or (pd and pd.search(r[0])): LOG.append((l,w,'DROPPED ROW: '+' | '.join(r))); continue
                if CAMROW.match(r[0]): rows.append([r[0],CAMCELL[l]]); continue
                cells=[r[0]]
                for c in r[1:]:
                    parts=re.findall(r'[^,，、]+(?:[,，、]\s*|$)',c) or [c]; keep=[x for x in parts if not (DROP.search(x) or (pd and pd.search(x)) or CAMX.get(l,CAM).search(x))]
                    if len(keep)<len(parts): LOG.append((l,w,'DROPPED CELL ITEMS: '+' / '.join(x for x in parts if x not in keep)))
                    cells.append(''.join(keep).rstrip(',，、 '))
                if not any(cells[1:]): LOG.append((l,w,'DROPPED ROW (empty): '+' | '.join(r))); continue
                rows.append(cells)
            out.append([k,{'head':[clean(l,h,w) for h in v['head']] if v.get('head') else None,'rows':rows}])
    fl2=[]
    for i,(k,v) in enumerate(out):
        if k=='h3' and (i+1==len(out) or out[i+1][0]=='h3'): continue
        fl2.append([k,v])
    return fl2
def cl_faq(l,faq,w,pid=None):
    out=[]; pd=PAGE_DROP.get(pid)
    for q,a in faq:
        q2=clean(l,q,w,pid,False)
        if DROPQ.search(q) or DROP.search(q) or (pd and pd.search(q)) or not q2: LOG.append((l,w,'DROPPED Q: '+q)); continue
        a=CAMN[l] if CAMX.get(l,CAM).search(q) else clean(l,a,w,pid)
        if not a: LOG.append((l,w,'DROPPED Q (empty): '+q)); continue
        out.append([q2,a])
    return out
LOC={'ko':('자주 묻는 질문','이미지'),'ja':('よくあるご質問','画像'),'zh':('常见问题','图片')}
def load(l,f,pid=None,faq_page=False):
    t=open(f'{SRC}/{l}/{f}.md').read()
    fq,im=LOC[l]
    t=re.sub(rf'^## {fq}\s*$','## FAQ',t,flags=re.M); t=re.sub(rf'^## {im}(?!\w).*$','## Images',t,flags=re.M)
    m,S,I,F,C=parse(t,faq_page); w=f
    m={k:clean(l,v,w,pid) for k,v in m.items()}
    secs=[]
    for s in S:
        if faq_page and s['h2'] in FAQSECREN.get(l,{}): s['h2']=FAQSECREN[l][s['h2']]
        h=clean(l,s['h2'],w,pid,False)
        if DROP_SECS.match(s['h2']) or not h or (PAGE_DROP.get(pid) and PAGE_DROP[pid].search(s['h2'])): LOG.append((l,w,'DROPPED SECTION: '+s['h2'])); continue
        sec={'h2':h}; fl=cl_flow(l,s['flow'],w,pid)
        if fl: sec['flow']=fl
        if s['faq']:
            fq2=cl_faq(l,s['faq'],w,pid)
            if fq2: sec['faq']=fq2
        if sec.get('flow') or sec.get('faq'): secs.append(sec)
    imgs=[[i.strip(),PHOTO.sub('',a.replace('**','')).strip()] for i,a in I]
    faq=cl_faq(l,F,w,pid); cta=[clean(l,c,w) for c in C]; cta=[c for c in cta if c]
    return m,secs,imgs,faq,cta
def resolve(raw,folder,pid,l):
    mm=re.match(r'([a-z0-9-]+)\s*(?:\((?:new|neu|신규|新規|新)[,，、]\s*([^)]+)\))?',raw.strip())
    if not mm: return None
    iid,f=mm.group(1),mm.group(2)
    if pid=='room-outside':
        if iid in BLUE and not f: return iid
        LOG.append((l,pid,'DROPPED IMAGE (Ops: only 064/019/080 on outside page): '+raw)); return None
    if f:
        f=f.strip().rsplit('.',1)[0]
        if f in BYFILE and (folder is None or f.split('/')[0]==folder): return BYFILE[f]
        LOG.append((l,pid,'DROPPED IMAGE (no approved id / wrong folder): '+raw)); return None
    if iid in IMG and (folder is None or iid in BLUE or FOLDER.get(iid)==folder): return iid
    LOG.append((l,pid,'DROPPED IMAGE (unknown / not own folder): '+raw)); return None
def images(l,imgs,folder,pid):
    out=[]
    for raw,alt in imgs:
        i=resolve(raw,folder,pid,l)
        alt=light(l,alt) if alt else alt
        if i and alt and not (PAGE_DROP.get(pid) and PAGE_DROP[pid].search(alt)) and not DROP.search(alt): out.append([i,alt])
    return out
# ---------------- localized UI / structure ----------------
KAKAO='http://pf.kakao.com/_UuhmX'
UI={'ko':{"skip":"본문으로 건너뛰기","languages":"언어","book_airbnb":"Airbnb에서 예약","book_trip":"Trip.com에서 예약","whatsapp":"WhatsApp으로 예약","zalo":"Zalo로 예약","address_label":"주소","contact_label":"연락처","more_label":"더 보기","guest_guide":"게스트 가이드 앱","read_more":"자세히 보기","source":"출처","estimate":"추정","home":"홈","not_found_title":"페이지를 찾을 수 없습니다","not_found_text":"이 페이지는 없습니다. 홈으로 이동:","extra_contact":f'<br><a href="{KAKAO}" rel="noopener">카카오톡 채널</a>'},
 'ja':{"skip":"本文へスキップ","languages":"言語","book_airbnb":"Airbnbで予約","book_trip":"Trip.comで予約","whatsapp":"WhatsAppで予約","zalo":"Zaloで予約","address_label":"住所","contact_label":"お問い合わせ","more_label":"その他","guest_guide":"ゲストガイドアプリ","read_more":"続きを読む","source":"出典","estimate":"推定","home":"ホーム","not_found_title":"ページが見つかりません","not_found_text":"このページは存在しません。ホームへ：" },
 'zh':{"skip":"跳到正文","languages":"语言","book_airbnb":"在 Airbnb 预订","book_trip":"在 Trip.com 预订","whatsapp":"通过 WhatsApp 预订","zalo":"通过 Zalo 预订","address_label":"地址","contact_label":"联系方式","more_label":"更多","guest_guide":"住客指南 App","read_more":"阅读更多","source":"来源","estimate":"估算","home":"首页","not_found_title":"页面不存在","not_found_text":"此页面不存在。返回首页：" }}
NAVK=['home','house','rooftop','families','groups','location','booking','faq','rules','guide','travel-guide']
NAV={'ko':['홈','집 소개','루프탑','가족여행','단체여행','위치','예약·문의','자주 묻는 질문','하우스 룰','여행 가이드','가이드 앱'],
 'ja':['ホーム','家のご案内','ルーフトップ','ご家族で','グループで','アクセス','予約・お問い合わせ','よくあるご質問','ハウスルール','旅行ガイド','ガイドアプリ'],
 'zh':['首页','房屋介绍','屋顶露台','家庭出游','团体出游','位置','预订与联系','常见问题','住宿规则','旅游攻略','指南 App']}
ROOMF={'room-entertainment':('entertainment-karaoke','Karaoke'),'room-living':('living-room','Wohnzimmer'),'room-kitchen':('kitchen-dining','Kueche'),'room-master':('master-bedroom','Schlafzimmer_1'),
 'room-bedroom-2':('bedroom-2','Schlafzimmer_2'),'room-bedroom-3':('bedroom-3','Schlafzimmer_3'),'room-bathrooms':('bathrooms','Bad'),'room-hallway':('hallway-workspace','Vorraum_Flur'),'room-outside':('outdoor-river',None)}
RP=list(ROOMF)+['rooftop']
CARD={'ko':['노래방·엔터테인먼트룸','거실','주방·다이닝','마스터 침실','침실 2','침실 3','욕실','전실·작업 공간','외부·강변','루프탑 테라스'],
 'ja':['カラオケ・エンタメルーム','リビング','キッチン・ダイニング','マスターベッドルーム','ベッドルーム2','ベッドルーム3','バスルーム','前室・ワークスペース','屋外・川沿い','ルーフトップテラス'],
 'zh':['卡拉OK娱乐室','客厅','厨房与餐厅','主卧','卧室2','卧室3','浴室','前厅与办公区','户外与河畔','屋顶露台']}
ROOMSH={'ko':'방별로 자세히 보기','ja':'お部屋ごとの詳細','zh':'各房间详情'}
FAQH={'ko':'자주 묻는 질문','ja':'よくあるご質問','zh':'常见问题'}
ROOMSEC={'ko':'공간별','ja':'お部屋の構成','zh':'房屋配置'}
CONTACTH={'ko':'연락처','ja':'連絡先','zh':'联系方式'}
CONTACT={'ko':['전화·WhatsApp: <a href="tel:{phone_e164}">{phone}</a>','Zalo: <a href="https://zalo.me/84909410382" rel="noopener">{phone}</a>',f'카카오톡 채널: <a href="{KAKAO}" rel="noopener">아스콘리빙</a>','이메일: <a href="mailto:{email}">{email}</a>'],
 'ja':['電話・WhatsApp：<a href="tel:{phone_e164}">{phone}</a>','Zalo：<a href="https://zalo.me/84909410382" rel="noopener">{phone}</a>','メール：<a href="mailto:{email}">{email}</a>'],
 'zh':['电话・WhatsApp：<a href="tel:{phone_e164}">{phone}</a>','Zalo：<a href="https://zalo.me/84909410382" rel="noopener">{phone}</a>','邮箱：<a href="mailto:{email}">{email}</a>']}
MAPS='https://www.google.com/maps/search/?api=1&query=389A+Tr%E1%BA%A7n+Xu%C3%A2n+So%E1%BA%A1n+T%C3%A2n+H%C6%B0ng+Ho+Chi+Minh+City'
MAPSEC={'ko':{'h2':'지도','p':[f'<a href="{MAPS}" rel="noopener">Google 지도에서 주소 열기</a>. 자세한 도착 안내는 예약 후 보내드립니다.']},
 'ja':{'h2':'地図','p':[f'<a href="{MAPS}" rel="noopener">Googleマップで住所を開く</a>。詳しい到着案内はご予約後にお送りします。']},
 'zh':{'h2':'地图','p':[f'<a href="{MAPS}" rel="noopener">在 Google 地图中打开地址</a>。详细的到达说明会在预订后发送。']}}
APPBTN={'ko':'여행 가이드 앱 열기','ja':'旅行ガイドアプリを開く','zh':'打开旅游指南 App'}
TG={'ko':{'h2':'무료 여행 가이드 앱','p':'무료 ASCON 여행 가이드 앱으로 일정을 짜 보세요. 현지 추천, 맛집과 볼거리, 지도를 휴대폰 브라우저에서 바로 볼 수 있습니다.','card':['무료 여행 가이드 앱','호치민 현지 추천과 지도를 휴대폰 브라우저에서 무료로.']},
 'ja':{'h2':'無料の旅行ガイドアプリ','p':'無料のASCON旅行ガイドアプリで旅の計画を。地元のおすすめ、グルメや見どころ、地図をスマートフォンのブラウザですぐに見られます。','card':['無料の旅行ガイドアプリ','ホーチミンの地元情報と地図を、スマホのブラウザで無料で。']},
 'zh':{'h2':'免费旅游指南 App','p':'用免费的 ASCON 旅游指南 App 规划行程：本地推荐、美食和景点、地图，在手机浏览器中直接打开。','card':['免费旅游指南 App','胡志明本地推荐和地图，在手机浏览器中免费使用。']}}
HOUSE={'ko':dict(title='집 소개 – 호치민 7군 독채 방별 안내 | ASCON',description='3층 집과 루프탑 전체: 전용 욕실이 있는 침실 3개, 약 40㎡ 거실, 주방, 노래방 엔터테인먼트룸. 방별 사진과 설비 안내.',h1='집 소개: 호치민 독채를 방별로 살펴보기',lead='3층과 루프탑, 250㎡가 넘는 공간을 우리 일행만 씁니다. 각 방의 사진과 설비를 확인하세요.'),
 'ja':dict(title='家のご案内 ホーチミン7区の一軒家 | ASCON',description='3階建てとルーフトップを貸切。専用バスルーム付き寝室3室、約40㎡のリビング、キッチン、カラオケのエンタメルーム。',h1='家のご案内：ホーチミンの一軒家をお部屋ごとに',lead='3フロアとルーフトップ、250㎡を超える空間を1組だけでお使いいただけます。各部屋の写真と設備をご覧ください。'),
 'zh':dict(title='房屋介绍 胡志明第七郡整栋民宿 | ASCON',description='三层楼加屋顶露台整栋包下：3间带独立浴室的卧室、约40㎡客厅、厨房、卡拉OK娱乐室。逐个房间查看照片和设施。',h1='房屋介绍：逐个房间看胡志明整栋民宿',lead='三层楼加屋顶露台，超过250㎡的空间只属于你们一行人。来看看每个房间的照片和设施。')}
OUTSIDE={'ko':dict(title='강변 독채 – 테라스와 강 | ASCON LIVING',description='강가에 있는 호치민 7군 독채. 흰 난간과 어닝이 있는 테라스에서 강과 1군 스카이라인이 보입니다.',h1='호치민 강변 숙소: 테라스에서 보는 강',lead='ASCON LIVING은 강가에 있는 집입니다. 흰 난간의 테라스에서 강 건너 1군 스카이라인을 바라보세요.'),
 'ja':dict(title='川沿いの一軒家 テラスと川 | ASCON LIVING',description='川沿いにあるホーチミン7区の一軒家。白い手すりとオーニングのテラスから、川と1区のスカイラインを望めます。',h1='ホーチミンの川沿いの宿：テラスから眺める川',lead='ASCON LIVINGは川沿いに建つ一軒家です。白い手すりのテラスから、川の向こうの1区のスカイラインを眺められます。'),
 'zh':dict(title='河畔整栋民宿 露台与河景 | ASCON LIVING',description='位于河边的胡志明第七郡整栋民宿：白色栏杆和遮阳篷的露台，可眺望河流与第一郡天际线。',h1='胡志明河畔民宿：在露台上看河',lead='ASCON LIVING 是一栋建在河边的房子。在白色栏杆的露台上，眺望河对岸的第一郡天际线。')}
TGP={'ko':dict(title='무료 호치민 여행 가이드 앱 | ASCON',description='무료 ASCON 여행 가이드 앱: 호치민 현지 추천, 맛집과 볼거리, 지도와 실용 정보. 휴대폰 브라우저에서 바로 열립니다.',h1='무료 호치민 여행 가이드 앱',lead='ASCON 가이드는 호치민 현지 추천과 장소를 담은 무료 웹 앱입니다. 휴대폰 브라우저에서 바로 열리며 비밀번호도 설치도 필요 없습니다.',
   h2a='앱 미리 보기',pa='휴대폰에서 찍은 실제 앱 화면입니다.',caps=['ASCON LIVING 로고와 모토가 있는 시작 화면','언어 선택: 앱은 10개 언어로 제공됩니다','카테고리: 음식, 카페, 바, 가족 나들이 등','집 주변 장소가 표시된 지도','생활 정보와 긴급 도움'],
   h2b='현지 추천과 장소',pb=['장소는 음식, 카페·디저트, 바·나이트라이프, 아이·가족, 명소·문화, 액티비티, 휴식, 쇼핑, 근교 여행, 생활 정보·응급 등 카테고리로 나뉩니다. 지도에서 집 주변 장소를 보고, 경로를 누르면 길 안내가 열립니다.','앱은 홈 화면에 추가할 수 있습니다. 더 많은 아이디어는 <a href="{L}guide/">호치민 여행 가이드</a>에 있습니다.']),
 'ja':dict(title='無料のホーチミン旅行ガイドアプリ | ASCON',description='無料のASCON旅行ガイドアプリ：ホーチミンの地元情報、グルメや見どころ、地図と実用情報。スマホのブラウザですぐ開けます。',h1='無料のホーチミン旅行ガイドアプリ',lead='ASCONガイドは、ホーチミンの地元のおすすめとスポットをまとめた無料のウェブアプリです。スマートフォンのブラウザですぐに開け、パスワードもインストールも不要です。',
   h2a='アプリの中身',pa='スマートフォンで撮影した実際のアプリ画面です。',caps=['ASCON LIVINGのロゴとモットーが表示されるウェルカム画面','言語選択：アプリは10言語に対応','カテゴリー：グルメ、カフェ、バー、家族のお出かけなど','家の周辺スポットを表示した地図','実用情報と緊急時のサポート'],
   h2b='地元のおすすめとスポット',pb=['スポットはグルメ、カフェ・デザート、バー・ナイトライフ、子ども・家族、観光・文化、アクティビティ、リラックス、ショッピング、日帰り旅行、実用情報・緊急などのカテゴリーに分かれています。地図で家の周辺スポットを確認し、ルートをタップすると道案内が開きます。','アプリはホーム画面に追加できます。滞在のアイデアは<a href="{L}guide/">ホーチミン旅行ガイド</a>でもご紹介しています。']),
 'zh':dict(title='免费胡志明旅游指南 App | ASCON',description='免费的 ASCON 旅游指南 App：胡志明本地推荐、美食和景点、地图与实用信息，在手机浏览器中直接打开。',h1='免费胡志明旅游指南 App',lead='ASCON 指南是一款免费网页 App，收录胡志明本地推荐和好去处。在手机浏览器中直接打开，无需密码，也无需安装。',
   h2a='App 界面一览',pa='以下是手机上的真实 App 截图。',caps=['带 ASCON LIVING 标志和口号的欢迎页','语言选择：App 支持10种语言','分类：美食、咖啡、酒吧、亲子出游等','标出房子周边地点的地图','实用信息与紧急求助'],
   h2b='本地推荐与好去处',pb=['地点按类别整理：美食、咖啡与甜品、酒吧与夜生活、亲子、景点与文化、活动、休闲、购物、一日游，以及实用信息与紧急求助。地图上可以看到房子周边的地点，点一下路线即可打开导航。','App 可以添加到手机主屏幕。更多行程灵感请看<a href="{L}guide/">胡志明旅游攻略</a>。'])}
META={('ja','room-bedroom-2'):{'description':'ホーチミン7区の一棟貸しのベッドルーム2。160×200cmベッド、スマートテレビ、専用バスルーム、エアコン、カーテン付きの窓。前室から入るお部屋。'}}  # width cap
RULES={'ko':{'h2':'기본 규칙','flow':[['ul',['체크인 14:00–23:00, 체크아웃 12:00.','베트남 법에 따라 투숙객 등록이 필요합니다.','실내 금연입니다. 흡연은 지정된 실외 공간에서만 가능합니다.','큰 음악 소리는 21:30까지입니다.','소란스러운 파티는 금지입니다.','등록된 투숙객만 머물 수 있습니다.']]]},
 'ja':{'h2':'基本ルール','flow':[['ul',['チェックイン14:00〜23:00、チェックアウト12:00。','ベトナムの法律により、宿泊者登録が必要です。','屋内は禁煙です。喫煙は指定の屋外スペースでお願いします。','大きな音の音楽は21:30までです。','騒がしいパーティーは禁止です。','ご宿泊は登録済みのゲストのみです。']]]},
 'zh':{'h2':'基本规则','flow':[['ul',['入住时间14:00–23:00，退房时间12:00。','根据越南法律，住客需要登记。','室内禁止吸烟，请在指定的室外区域吸烟。','大声播放音乐请在21:30前结束。','禁止喧闹派对。','仅限已登记的住客入住。']]]}}  # owner-confirmed rules (same as EN/DE)
KWCAP={'ko':[("호치민 7군 독채의 ","이 독채의 "),("호치민 7군 독채 ","이 독채 "),("호치민 7군 독채","이 독채"),("7군(떤흥)","떤흥"),("떤흥(7군)","떤흥"),("Tân Hưng(7군)","Tân Hưng"),("7군 떤흥","떤흥"),("7군 강변 독채","강변 독채"),("을 7군에서","을 이곳에서"),("여행 중에는 7군이라고 말하는 편이","여행 중에는 이렇게 말하는 편이")],
 'ja':[("ホーチミン7区の一棟貸しの","この一棟貸しの"),("ホーチミン7区の一軒家","この一軒家"),("7区（タンフン）","タンフン"),("7区タンフン","タンフン"),("Tân Hưng（7区）","Tân Hưng"),("7区の川沿いの一軒家","川沿いの一軒家"),("旅行中は「7区」と伝えるのがいちばん確実です","旅行中はこの呼び方がいちばん確実です")],
 'zh':[("胡志明第七郡整栋民宿的","这栋民宿的"),("胡志明第七郡整栋民宿里","这栋民宿里"),("胡志明第七郡整栋民宿","这栋民宿"),("第七郡新兴坊","新兴坊"),("Tân Hưng（第七郡）","Tân Hưng"),("想住第七郡河畔整栋民宿","想住河畔整栋民宿"),("打车时说第七郡最方便","打车时这样说最方便"),("第七郡能让您看到","这里能让您看到")]}
def kwcap(l,x):
    if isinstance(x,str):
        for a,b in KWCAP[l]: x=x.replace(a,b)
        return x
    if isinstance(x,list): return [kwcap(l,y) for y in x]
    if isinstance(x,dict): return {k:kwcap(l,v) for k,v in x.items()}
    return x
RVNEUT={'ko':'전망','ja':'眺め','zh':'景色'}
def tail(l,faq,cta):
    t=[]
    if faq: t.append({'h2':FAQH[l],'faq':faq})
    t.append({'p':cta,'cta':True} if cta else {'cta':True}); return t
def setmeta(pg,m):
    for k in('title','description','h1','lead'):
        if m.get(k): pg[k]=m[k]
def roomcards(l,P):
    return {'h2':ROOMSH[l],'cards':[[CARD[l][i],p,P[p]['description'] if p in P else ''] for i,p in enumerate(RP)]}
def tgblock(l): return {'h2':TG[l]['h2'],'p':[TG[l]['p']],'cards':[[TG[l]['card'][0],'travel-guide',TG[l]['card'][1]]],'_tg':1}
def rvcap(l,pid,pg):
    seen=False; lists=[]
    if pg.get('hero'): lists.append([pg['hero']])
    if pg.get('cover'): lists.append([pg['cover']])
    for s in pg['sections']:
        if s.get('imgs'): lists.append(s['imgs'])
    for L in lists:
        for im in L:
            if RV.search(im[1]):
                if im[0] in BLUE and not seen: seen=True; continue
                new=RV.sub(RVNEUT[l],im[1]); LOG.append((l,pid,f'alt river-view neutralised: {im[1]} -> {new}')); im[1]=new
def build(l):
    P={}
    for pid,(f,folder) in ROOMF.items():
        m,secs,imgs,faq,cta=load(l,'rooms/'+f,pid)
        im=images(l,imgs,folder,pid)
        pg={'title':m['title'],'description':m['description'],'h1':m['h1'],'lead':m.get('lead','')}
        if pid=='room-outside': pg.update(OUTSIDE[l])
        if im: pg['cover']=im[0]
        if len(im)>1 and secs: secs[0]['imgs']=im[1:]
        pg['sections']=secs+tail(l,faq,cta); P[pid]=pg
    m,secs,imgs,faq,cta=load(l,'rooms/rooftop','rooftop'); im=images(l,imgs,'Rooftop','rooftop')
    P['rooftop']={'title':m['title'],'description':m['description'],'h1':m['h1'],'lead':m.get('lead','')}
    if im: secs[0]['imgs']=im
    P['rooftop']['sections']=secs+tail(l,faq,cta)
    # house overview: room cards + MR entertainment text + travel guide block
    m,secs,imgs,faq,cta=load(l,'entertainment','house'); im=images(l,imgs,'Karaoke','house')
    if im: secs[0]['imgs']=im
    P['house']=dict(HOUSE[l]); P['house']['sections']=[roomcards(l,P)]+secs+[tgblock(l)]+tail(l,faq,cta)
    # home
    m,secs,imgs,faq,cta=load(l,'index','home'); im=images(l,imgs,None,'home')
    P['home']={'title':m['title'],'description':m['description'],'h1':m['h1'],'lead':m['lead']}
    hero=[x for x in im if x[0]=='hero']; P['home']['hero']=hero[0] if hero else ['hero','ASCON LIVING']
    gal=[x for x in im if x[0]!='hero']
    if gal: secs[0]['imgs']=gal
    for s in secs:
        if ROOMSEC[l] in s['h2']: s['cards']=roomcards(l,P)['cards']
    P['home']['sections']=secs+[tgblock(l)]+tail(l,faq,cta)
    for pid in('families','groups'):
        m,secs,imgs,faq,cta=load(l,pid,pid); im=images(l,imgs,None,pid)
        P[pid]={}; setmeta(P[pid],m)
        if im: secs[0]['imgs']=im
        P[pid]['sections']=secs+[roomcards(l,P)]+tail(l,faq,cta)
    m,secs,imgs,faq,cta=load(l,'location','location'); im=images(l,imgs,None,'location')
    P['location']={}; setmeta(P['location'],m)
    if im: secs[0]['imgs']=im
    P['location']['sections']=secs+[MAPSEC[l]]+tail(l,faq,cta)
    m,secs,imgs,faq,cta=load(l,'travel-guide','guide')  # MR image rows here are for the guide-app subpage (old place-card shots with minutes): not used
    P['guide']={}; setmeta(P['guide'],m)
    btn={'p':[f'<a class="btn b1" href="{{guide}}" rel="noopener">{APPBTN[l]}</a>'],'cards':[[TG[l]['card'][0],'travel-guide',TG[l]['card'][1]]]}
    P['guide']['sections']=secs[:1]+[btn]+secs[1:]+tail(l,faq,cta)
    m,secs,imgs,faq,cta=load(l,'faq','faq',True)
    P['faq']={}; setmeta(P['faq'],m); P['faq']['sections']=secs+[{'p':cta,'cta':True} if cta else {'cta':True}]
    m,secs,imgs,faq,cta=load(l,'booking','booking')
    P['booking']={}; setmeta(P['booking'],m)
    secs=[s for s in secs if s['h2']!=CONTACTH[l]]
    P['booking']['sections']=secs+[{'cta':True},{'h2':CONTACTH[l],'p':CONTACT[l]}]+([{'h2':FAQH[l],'faq':faq}] if faq else [])
    m,secs,imgs,faq,cta=load(l,'house-rules','rules')
    P['rules']={}; setmeta(P['rules'],m); P['rules']['sections']=secs[:1]+[RULES[l]]+secs[1:]+tail(l,faq,cta)
    t=TGP.get(l) or TGP['ko']; ids=['tg-welcome','tg-picker','tg-categories','tg-map','tg-practical']
    P['travel-guide']={'title':t['title'],'description':t['description'],'h1':t['h1'],'lead':t['lead'],'sections':[
        {'p':[f'<a class="btn b1" href="{{guide}}" rel="noopener">{APPBTN[l]}</a>']},
        {'h2':t['h2a'],'p':[t['pa']],'imgs':[[i,c] for i,c in zip(ids,t['caps'])]},
        {'h2':t['h2b'],'p':t['pb']+[f'<a class="btn b1" href="{{guide}}" rel="noopener">{APPBTN[l]}</a>']},{'cta':True}]}
    for pid in ('home','location'): P[pid]['sections']=kwcap(l,P[pid]['sections'])  # keyword cap: District 7 max 3 in body (H1+lead kept)
    for (ll,pid),mm in META.items():
        if ll==l: P[pid].update(mm)
    for pid,pg in P.items(): rvcap(l,pid,pg)
    d={'ui':dict(UI[l],motto=json.load(open('content/en.json'))['ui']['motto']),'nav':[[k,v] for k,v in zip(NAVK,NAV[l])],'pages':P}
    json.dump(d,open(f'content/{l}.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    for l in (sys.argv[1:] or LANGS): build(l)
    for x in LOG: print(*x,sep=' | ')
