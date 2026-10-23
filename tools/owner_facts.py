"""Owner-confirmed 23 Oct 2026: guests have a washing machine, a dryer, an iron and an ironing board;
the laundry service (30 EUR per load) is done outside the house. Applied to body text after laundry.py.
Headings/titles/descriptions are untouched. Strings that already name the ironing board (wardrobe details) stay as they are."""
import re
SKIP={'title','description','h1','h2','meta','alt','lead_title'}
# lang: (iron regex incl. optional article, full phrase, phrase without washing machine, ironing-board word, washing-machine regex)
IRON={
 'en':(r'\b(?:an )?(?<![Ii]roning )iron\b(?! your)','a washing machine, a dryer, an iron and an ironing board','a dryer, an iron and an ironing board','ironing board',r'washing machine'),
 'de':(r'\b(?:[Ee]in )?Bügeleisen','Waschmaschine, Trockner, Bügeleisen und Bügelbrett','Trockner, Bügeleisen und Bügelbrett','Bügelbrett',r'Waschmaschine'),
 'vi':(r'[Bb]àn ủi(?! quần)','máy giặt, máy sấy, bàn ủi và bàn để ủi','máy sấy, bàn ủi và bàn để ủi','bàn để ủi',r'máy giặt'),
 'zh':(r'熨斗','洗衣机、烘干机、熨斗和熨衣板','烘干机、熨斗和熨衣板','熨衣板',r'洗衣机'),
 'zh-tw':(r'熨斗','洗衣機、烘乾機、熨斗和燙衣板','烘乾機、熨斗和燙衣板','燙衣板',r'洗衣機'),
 'ko':(r'다리미(?!판)','세탁기, 건조기, 다리미와 다리미판','건조기, 다리미와 다리미판','다리미판',r'세탁기'),
 'ja':(r'アイロン(?!台)','洗濯機、乾燥機、アイロンとアイロン台','乾燥機、アイロンとアイロン台','アイロン台',r'洗濯機'),
 'fr':(r"\b(?:[Uu]n |[Ll]e )?[Ff]er à repasser",'un lave-linge, un sèche-linge, un fer et une planche à repasser','un sèche-linge, un fer et une planche à repasser','planche à repasser',r'lave-linge'),
 'es':(r'\b(?:la )?[Pp]lancha\b','lavadora, secadora, plancha y tabla de planchar','secadora, plancha y tabla de planchar','tabla de planchar',r'lavadora'),
 'pt':(r'\b(?:[Oo] )?[Ff]erro de passar','máquina de lavar, secadora, ferro e tábua de passar','secadora, ferro e tábua de passar','tábua de passar',r'máquina de lavar'),
 'it':(r'\b(?:[Uu]n |[Ii]l )?[Ff]erro da stiro','lavatrice, asciugatrice, ferro e asse da stiro','asciugatrice, ferro e asse da stiro','asse da stiro',r'lavatrice'),
 'nl':(r'\b(?:[Ee]en |[Hh]et )?[Ss]trijkijzer\b','wasmachine, droger, strijkijzer en strijkplank','droger, strijkijzer en strijkplank','strijkplank',r'wasmachine'),
 'pl':(r'[Żż]elazko\b','pralka, suszarka, żelazko i deska do prasowania','suszarka, żelazko i deska do prasowania','deska do prasowania',r'pralk'),
 'sv':(r'[Ss]trykjärn\b','tvättmaskin, torktumlare, strykjärn och strykbräda','torktumlare, strykjärn och strykbräda','strykbräda',r'tvättmaskin'),
 'ru':(r'[Уу]тюг\b','стиральная машина, сушильная машина, утюг и гладильная доска','сушильная машина, утюг и гладильная доска','гладильн',r'стиральн'),
 'tr':(r'(?<![Bb])[Üü]tü\b','çamaşır makinesi, kurutma makinesi, ütü ve ütü masası','kurutma makinesi, ütü ve ütü masası','ütü masası',r'çamaşır makine'),
 'id':(r'[Ss]etrika\b','mesin cuci, pengering, setrika dan papan setrika','pengering, setrika dan papan setrika','papan setrika',r'mesin cuci'),
 'ms':(r'[Ss]eterika\b','mesin basuh, mesin pengering, seterika dan papan seterika','mesin pengering, seterika dan papan seterika','papan seterika',r'mesin basuh'),
 'th':(r'เตารีด','เครื่องซักผ้า เครื่องอบผ้า เตารีดและโต๊ะรีดผ้า','เครื่องอบผ้า เตารีดและโต๊ะรีดผ้า','โต๊ะรีดผ้า',r'เครื่องซักผ้า'),
 'ar':(r'(?:ال)?مكواة','غسالة ومجفف ومكواة وطاولة كي','مجفف ومكواة وطاولة كي','طاولة كي',r'غسال'),
 'hi':(r'प्रेस','वॉशिंग मशीन, ड्रायर, प्रेस और इस्त्री बोर्ड','ड्रायर, प्रेस और इस्त्री बोर्ड','इस्त्री बोर्ड',r'वॉशिंग मशीन'),
 'ur':(r'استری(?! بورڈ)','واشنگ مشین، ڈرائر، استری اور استری بورڈ','ڈرائر، استری اور استری بورڈ','استری بورڈ',r'واشنگ مشین'),
 'pa':(r'ਪ੍ਰੈੱਸ','ਵਾਸ਼ਿੰਗ ਮਸ਼ੀਨ, ਡਰਾਇਰ, ਪ੍ਰੈੱਸ ਅਤੇ ਪ੍ਰੈੱਸ ਬੋਰਡ','ਡਰਾਇਰ, ਪ੍ਰੈੱਸ ਅਤੇ ਪ੍ਰੈੱਸ ਬੋਰਡ','ਪ੍ਰੈੱਸ ਬੋਰਡ',r'ਵਾਸ਼ਿੰਗ ਮਸ਼ੀਨ'),
}
# laundry service done outside the house (only where the 30 EUR service is named)
OUT={
 'en':(r'[Ll]aundry service',r'\g<0> outside the house'),'de':(r'Wäscheservice',r'\g<0> außer Haus'),
 'vi':(r'dịch vụ giặt ủi',r'\g<0> bên ngoài'),'hi':(r'लॉन्ड्री सर्विस',r'घर से बाहर \g<0>'),'ur':(r'لانڈری سروس',r'گھر سے باہر \g<0>'),
 'pa':(r'ਲਾਂਡਰੀ ਸੇਵਾ',r'ਘਰ ਤੋਂ ਬਾਹਰ \g<0>'),'ar':(r'خدمة غسيل الملابس',r'\g<0> خارج المنزل'),'es':(r'[Ss]ervicio de lavandería',r'\g<0> externo'),
 'fr':(r'[Ss]ervice de blanchisserie',r'\g<0> extérieur'),'it':(r'[Ss]ervizio( di)? lavanderia',r'\g<0> esterno'),'pt':(r'[Ss]erviço de lavanderia',r'\g<0> externo'),
 'nl':(r'[Ww]asservice',r'\g<0> buiten de deur'),'pl':(r'usług[aęi] prania',r'\g<0> poza domem'),'sv':(r'[Tt]vättservice',r'\g<0> utanför huset'),
 'ru':(r'[Уу]слуг[аи] стирки',r'\g<0> вне дома'),'tr':(r'[Çç]amaşır hizmeti',r'\g<0> (ev dışında)'),'id':(r'[Ll]ayanan laundry',r'\g<0> di luar rumah'),
 'ms':(r'[Ss]ervis dobi',r'\g<0> di luar rumah'),'th':(r'บริการซักรีด',r'\g<0>นอกบ้าน'),'ko':(r'세탁 서비스',r'외부 \g<0>'),
 'ja':(r'ランドリーサービス',r'外部\g<0>'),'zh':(r'洗衣服务',r'外送\g<0>'),'zh-tw':(r'洗衣服務',r'外送\g<0>'),
}
MARK={'en':'outside the house','de':'außer Haus','vi':'bên ngoài','hi':'घर से बाहर','ur':'گھر سے باہر','pa':'ਘਰ ਤੋਂ ਬਾਹਰ','ar':'خارج المنزل','es':'externo','fr':'extérieur','it':'esterno','pt':'externo','nl':'buiten de deur','pl':'poza domem','sv':'utanför huset','ru':'вне дома','tr':'ev dışında','id':'di luar rumah','ms':'di luar rumah','th':'นอกบ้าน','ko':'외부','ja':'外部','zh':'外送','zh-tw':'外送'}
POST={'en':[('ironing board is','ironing board are')],'fr':[('planche à repasser est','planche à repasser sont')],
 'ko':[('다리미판가','다리미판이'),('다리미판는','다리미판은'),('다리미판를','다리미판을')],'tr':[('ütü masası de','ütü masası da')],
 'vi':[('bàn để ủi để ủi','bàn để ủi')]}
def _fix(lang,s):
    if lang in OUT and '30 EUR' in s and MARK[lang] not in s:
        s=re.sub(OUT[lang][0],OUT[lang][1],s)
        s=s.replace('(ev dışında) (','(ev dışında, ')
    if lang in IRON:
        rx,full,red,board,wm=IRON[lang]
        if re.search(rx,s) and board.lower() not in s.lower() and not s.startswith('<'):
            rep=red if re.search(wm,s,re.I) else full
            done=[False]
            def r(m):
                if done[0]: return ''  # name the set once per string
                done[0]=True
                t=rep
                if m.group(0)[:1].isupper() and m.start()==0 or (m.start()>=2 and s[m.start()-2] in '.!?'): t=t[:1].upper()+t[1:]
                return t
            s=re.sub(rx,r,s)
            if lang=='de': s=re.sub(r'Bügelbrett (ist|steht)',lambda m:'Bügelbrett '+{'ist':'sind','steht':'stehen'}[m.group(1)],s)
            for a,b in POST.get(lang,()): s=s.replace(a,b)
            s=re.sub(r'(, ){2,}',', ',s).replace(' ,',',')
    return s
def _walk(lang,o,key=None):
    if isinstance(o,dict): return {k:(v if k in SKIP else _walk(lang,v,k)) for k,v in o.items()}
    if isinstance(o,list):
        if len(o)==2 and o[0] in ('h2','h3','h4'): return o
        return [_walk(lang,v,key) for v in o]
    if isinstance(o,str): return _fix(lang,o)
    return o
def apply(lang,data):
    out=dict(data)
    if 'pages' in out: out['pages']=_walk(lang,out['pages'])
    return out
