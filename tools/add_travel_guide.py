import json
BTN='<a class="btn b1" href="{guide}" rel="noopener">%s</a>'
SH=['welcome','picker','categories','map','practical']
T={
'en':dict(nav='Guide App',title='Free Travel Guide App for Ho Chi Minh City | ASCON',
 desc='See the free ASCON travel guide app: local tips, places to eat and visit, a map and practical help for Ho Chi Minh City. Opens in your phone browser.',
 h1='Free travel guide app for Ho Chi Minh City',
 lead='The ASCON Guide is a free web app with local tips and places around Ho Chi Minh City. It opens straight in your phone\'s browser: no password, nothing to install.',
 btn='Open the travel guide app',
 h_shots='A look inside the app',
 p_shots='These are real screenshots of the app on a phone.',
 caps=['Welcome screen with the ASCON LIVING logo and motto','Language picker: the app comes in ten languages','Categories: food, cafés, bars, family outings and more','Map with places around the house','Practical information and emergency help'],
 h_what='Local tips and places',
 p_what=['Places are sorted into clear categories: food, cafés and desserts, bars and nightlife, kids and family, sights and culture, activities, relaxation, shopping, day trips, and practical and emergency information. The map shows the places around the house, and one tap on Route opens directions.','You can add the app to your home screen. More ideas for your stay are in our <a href="{L}guide/">Ho Chi Minh City travel guide</a>.'],
 card_h='Free travel guide app',card_d='Local tips, places and a map for Ho Chi Minh City, free in your phone browser.',
 home_h='Free travel guide app',home_p='Plan your days with our free ASCON travel guide app: local tips, places to eat and visit, and a map, right in your phone\'s browser.'),
'de':dict(nav='Guide-App',title='Kostenlose Reiseführer-App für Ho-Chi-Minh-Stadt | ASCON',
 desc='Die kostenlose ASCON Reiseführer-App: lokale Tipps, Restaurants, Ausflugsziele, Karte und praktische Hilfe für Ho-Chi-Minh-Stadt. Direkt im Handy-Browser.',
 h1='Kostenlose Reiseführer-App für Ho-Chi-Minh-Stadt',
 lead='Der ASCON Guide ist eine kostenlose Web-App mit lokalen Tipps und Orten rund um Ho-Chi-Minh-Stadt. Er öffnet sich direkt im Browser eures Handys: kein Passwort, keine Installation.',
 btn='Reiseführer-App öffnen',
 h_shots='Ein Blick in die App',
 p_shots='Das sind echte Screenshots der App auf dem Handy.',
 caps=['Startbildschirm mit Logo und Motto von ASCON LIVING','Sprachauswahl: Die App gibt es in zehn Sprachen','Kategorien: Essen, Cafés, Bars, Ausflüge mit Kindern und mehr','Karte mit Orten rund ums Haus','Praktische Infos und Hilfe im Notfall'],
 h_what='Lokale Tipps und Orte',
 p_what=['Die Orte sind in übersichtliche Kategorien sortiert: Essen, Cafés und Desserts, Bars und Nachtleben, Kinder und Familie, Sehenswürdigkeiten und Kultur, Aktivitäten, Entspannung, Shopping, Tagesausflüge sowie praktische Infos und Notfall. Die Karte zeigt die Orte rund ums Haus, und ein Tipp auf Route öffnet die Wegbeschreibung.','Ihr könnt die App auf den Startbildschirm legen. Weitere Ideen für euren Aufenthalt findet ihr in unserem <a href="{L}guide/">Reiseführer für Ho-Chi-Minh-Stadt</a>.'],
 card_h='Kostenlose Reiseführer-App',card_d='Lokale Tipps, Orte und Karte für Ho-Chi-Minh-Stadt, kostenlos im Handy-Browser.',
 home_h='Kostenlose Reiseführer-App',home_p='Plant eure Tage mit unserer kostenlosen ASCON Reiseführer-App: lokale Tipps, Restaurants, Ausflugsziele und eine Karte, direkt im Browser eures Handys.'),
'vi':dict(nav='Ứng dụng',title='Ứng dụng cẩm nang du lịch TP. Hồ Chí Minh miễn phí',
 desc='Ứng dụng cẩm nang du lịch miễn phí của ASCON: mẹo địa phương, quán ăn, điểm tham quan, bản đồ và thông tin hữu ích tại TP. Hồ Chí Minh.',
 h1='Ứng dụng cẩm nang du lịch miễn phí cho TP. Hồ Chí Minh',
 lead='ASCON Guide là ứng dụng web miễn phí với mẹo địa phương và các địa điểm quanh TP. Hồ Chí Minh. Ứng dụng mở ngay trên trình duyệt điện thoại: không cần mật khẩu, không cần cài đặt.',
 btn='Mở ứng dụng cẩm nang',
 h_shots='Bên trong ứng dụng',
 p_shots='Đây là ảnh chụp màn hình thật của ứng dụng trên điện thoại.',
 caps=['Màn hình chào với logo và khẩu hiệu ASCON LIVING','Chọn ngôn ngữ: ứng dụng có mười ngôn ngữ','Danh mục: ẩm thực, cà phê, bar, vui chơi cùng trẻ em và nhiều hơn nữa','Bản đồ các địa điểm quanh nhà','Thông tin thực tế và trợ giúp khẩn cấp'],
 h_what='Mẹo địa phương và địa điểm',
 p_what=['Các địa điểm được chia thành danh mục rõ ràng: ẩm thực, cà phê và tráng miệng, bar và về đêm, trẻ em và gia đình, tham quan và văn hóa, hoạt động, thư giãn, mua sắm, đi chơi trong ngày, cùng thông tin thực tế và khẩn cấp. Bản đồ hiển thị các địa điểm quanh nhà, chạm vào Chỉ đường để mở hướng dẫn đường đi.','Bạn có thể thêm ứng dụng vào màn hình chính. Xem thêm gợi ý trong <a href="{L}guide/">cẩm nang du lịch TP. Hồ Chí Minh</a>.'],
 card_h='Ứng dụng cẩm nang miễn phí',card_d='Mẹo địa phương, địa điểm và bản đồ TP. Hồ Chí Minh, miễn phí trên trình duyệt.',
 home_h='Ứng dụng cẩm nang miễn phí',home_p='Lên kế hoạch cho chuyến đi với ứng dụng cẩm nang du lịch miễn phí của ASCON: mẹo địa phương, quán ăn, điểm tham quan và bản đồ, ngay trên trình duyệt điện thoại.'),
'hi':dict(nav='गाइड ऐप',title='हो ची मिन्ह सिटी के लिए मुफ़्त ट्रैवल गाइड ऐप | ASCON',
 desc='ASCON का मुफ़्त ट्रैवल गाइड ऐप: लोकल टिप्स, खाने और घूमने की जगहें, नक्शा और हो ची मिन्ह सिटी के लिए काम की जानकारी। फ़ोन के ब्राउज़र में खुलता है।',
 h1='हो ची मिन्ह सिटी के लिए मुफ़्त ट्रैवल गाइड ऐप',
 lead='ASCON Guide एक मुफ़्त वेब ऐप है, जिसमें हो ची मिन्ह सिटी की लोकल टिप्स और जगहें हैं। यह सीधे आपके फ़ोन के ब्राउज़र में खुलता है: न पासवर्ड, न इंस्टॉल।',
 btn='ट्रैवल गाइड ऐप खोलें',
 h_shots='ऐप की एक झलक',
 p_shots='ये फ़ोन पर ऐप के असली स्क्रीनशॉट हैं। ऐप हिंदी में उपलब्ध नहीं है, इसलिए स्क्रीनशॉट अंग्रेज़ी संस्करण के हैं।',
 caps=['ASCON LIVING लोगो और मोटो के साथ स्वागत स्क्रीन (अंग्रेज़ी)','भाषा चुनें: ऐप दस भाषाओं में है (अंग्रेज़ी)','श्रेणियाँ: खाना, कैफ़े, बार, बच्चों के साथ घूमना और भी बहुत कुछ (अंग्रेज़ी)','घर के आसपास की जगहों वाला नक्शा (अंग्रेज़ी)','काम की जानकारी और आपातकालीन मदद (अंग्रेज़ी)'],
 h_what='लोकल टिप्स और जगहें',
 p_what=['जगहें साफ़ श्रेणियों में बँटी हैं: खाना, कैफ़े और डेज़र्ट, बार और नाइटलाइफ़, बच्चे और परिवार, दर्शनीय स्थल और संस्कृति, गतिविधियाँ, आराम, शॉपिंग, एक दिन की यात्राएँ, और काम की व आपातकालीन जानकारी। नक्शा घर के आसपास की जगहें दिखाता है, और Route पर टैप करने से रास्ता खुल जाता है।','आप ऐप को होम स्क्रीन पर जोड़ सकते हैं। और सुझाव हमारी <a href="{L}guide/">हो ची मिन्ह सिटी ट्रैवल गाइड</a> में हैं।'],
 card_h='मुफ़्त ट्रैवल गाइड ऐप',card_d='हो ची मिन्ह सिटी की लोकल टिप्स, जगहें और नक्शा, फ़ोन के ब्राउज़र में मुफ़्त।',
 home_h='मुफ़्त ट्रैवल गाइड ऐप',home_p='हमारे मुफ़्त ASCON ट्रैवल गाइड ऐप के साथ अपने दिन प्लान करें: लोकल टिप्स, खाने और घूमने की जगहें और नक्शा, सीधे फ़ोन के ब्राउज़र में।'),
'ur':dict(nav='گائیڈ ایپ',title='ہو چی منہ سٹی کے لیے مفت ٹریول گائیڈ ایپ | ASCON',
 desc='ASCON کی مفت ٹریول گائیڈ ایپ: مقامی مشورے، کھانے اور گھومنے کی جگہیں، نقشہ اور ہو چی منہ سٹی کے لیے مفید معلومات۔ فون کے براؤزر میں کھلتی ہے۔',
 h1='ہو چی منہ سٹی کے لیے مفت ٹریول گائیڈ ایپ',
 lead='ASCON Guide ایک مفت ویب ایپ ہے جس میں ہو چی منہ سٹی کے مقامی مشورے اور جگہیں ہیں۔ یہ سیدھی آپ کے فون کے براؤزر میں کھلتی ہے: نہ پاس ورڈ، نہ انسٹال۔',
 btn='ٹریول گائیڈ ایپ کھولیں',
 h_shots='ایپ کی ایک جھلک',
 p_shots='یہ فون پر ایپ کے اصل اسکرین شاٹس ہیں۔ ایپ اردو میں دستیاب نہیں، اس لیے اسکرین شاٹس انگریزی ورژن کے ہیں۔',
 caps=['ASCON LIVING لوگو اور موٹو کے ساتھ خوش آمدید اسکرین (انگریزی)','زبان کا انتخاب: ایپ دس زبانوں میں ہے (انگریزی)','زمرے: کھانا، کیفے، بار، بچوں کے ساتھ سیر اور بہت کچھ (انگریزی)','گھر کے آس پاس کی جگہوں کا نقشہ (انگریزی)','مفید معلومات اور ہنگامی مدد (انگریزی)'],
 h_what='مقامی مشورے اور جگہیں',
 p_what=['جگہیں واضح زمروں میں ترتیب دی گئی ہیں: کھانا، کیفے اور میٹھا، بار اور نائٹ لائف، بچے اور خاندان، تاریخی مقامات اور ثقافت، سرگرمیاں، آرام، شاپنگ، ایک دن کے سفر، اور مفید و ہنگامی معلومات۔ نقشہ گھر کے آس پاس کی جگہیں دکھاتا ہے، اور Route پر ٹیپ کرنے سے راستہ کھل جاتا ہے۔','آپ ایپ کو ہوم اسکرین پر شامل کر سکتے ہیں۔ مزید مشورے ہماری <a href="{L}guide/">ہو چی منہ سٹی ٹریول گائیڈ</a> میں ہیں۔'],
 card_h='مفت ٹریول گائیڈ ایپ',card_d='ہو چی منہ سٹی کے مقامی مشورے، جگہیں اور نقشہ، فون کے براؤزر میں مفت۔',
 home_h='مفت ٹریول گائیڈ ایپ',home_p='ہماری مفت ASCON ٹریول گائیڈ ایپ کے ساتھ اپنے دن پلان کریں: مقامی مشورے، کھانے اور گھومنے کی جگہیں اور نقشہ، سیدھا فون کے براؤزر میں۔'),
'pa':dict(nav='ਗਾਈਡ ਐਪ',title='ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਲਈ ਮੁਫ਼ਤ ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ | ASCON',
 desc='ASCON ਦਾ ਮੁਫ਼ਤ ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ: ਲੋਕਲ ਟਿੱਪਸ, ਖਾਣ ਅਤੇ ਘੁੰਮਣ ਦੀਆਂ ਥਾਵਾਂ, ਨਕਸ਼ਾ ਅਤੇ ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਲਈ ਕੰਮ ਦੀ ਜਾਣਕਾਰੀ। ਫ਼ੋਨ ਦੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਖੁੱਲ੍ਹਦਾ ਹੈ।',
 h1='ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਲਈ ਮੁਫ਼ਤ ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ',
 lead='ASCON Guide ਇੱਕ ਮੁਫ਼ਤ ਵੈੱਬ ਐਪ ਹੈ, ਜਿਸ ਵਿੱਚ ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਦੀਆਂ ਲੋਕਲ ਟਿੱਪਸ ਅਤੇ ਥਾਵਾਂ ਹਨ। ਇਹ ਸਿੱਧਾ ਤੁਹਾਡੇ ਫ਼ੋਨ ਦੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਖੁੱਲ੍ਹਦਾ ਹੈ: ਨਾ ਪਾਸਵਰਡ, ਨਾ ਇੰਸਟਾਲ।',
 btn='ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ ਖੋਲ੍ਹੋ',
 h_shots='ਐਪ ਦੀ ਇੱਕ ਝਲਕ',
 p_shots='ਇਹ ਫ਼ੋਨ ਉੱਤੇ ਐਪ ਦੇ ਅਸਲ ਸਕ੍ਰੀਨਸ਼ਾਟ ਹਨ। ਐਪ ਪੰਜਾਬੀ ਵਿੱਚ ਉਪਲਬਧ ਨਹੀਂ, ਇਸ ਲਈ ਸਕ੍ਰੀਨਸ਼ਾਟ ਅੰਗਰੇਜ਼ੀ ਵਰਜ਼ਨ ਦੇ ਹਨ।',
 caps=['ASCON LIVING ਲੋਗੋ ਅਤੇ ਮੋਟੋ ਨਾਲ ਸਵਾਗਤ ਸਕ੍ਰੀਨ (ਅੰਗਰੇਜ਼ੀ)','ਭਾਸ਼ਾ ਚੁਣੋ: ਐਪ ਦਸ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਹੈ (ਅੰਗਰੇਜ਼ੀ)','ਸ਼੍ਰੇਣੀਆਂ: ਖਾਣਾ, ਕੈਫ਼ੇ, ਬਾਰ, ਬੱਚਿਆਂ ਨਾਲ ਘੁੰਮਣਾ ਅਤੇ ਹੋਰ (ਅੰਗਰੇਜ਼ੀ)','ਘਰ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਦੀਆਂ ਥਾਵਾਂ ਦਾ ਨਕਸ਼ਾ (ਅੰਗਰੇਜ਼ੀ)','ਕੰਮ ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਐਮਰਜੈਂਸੀ ਮਦਦ (ਅੰਗਰੇਜ਼ੀ)'],
 h_what='ਲੋਕਲ ਟਿੱਪਸ ਅਤੇ ਥਾਵਾਂ',
 p_what=['ਥਾਵਾਂ ਸਾਫ਼ ਸ਼੍ਰੇਣੀਆਂ ਵਿੱਚ ਵੰਡੀਆਂ ਹਨ: ਖਾਣਾ, ਕੈਫ਼ੇ ਅਤੇ ਮਿੱਠਾ, ਬਾਰ ਅਤੇ ਨਾਈਟਲਾਈਫ਼, ਬੱਚੇ ਅਤੇ ਪਰਿਵਾਰ, ਦੇਖਣਯੋਗ ਥਾਵਾਂ ਅਤੇ ਸੱਭਿਆਚਾਰ, ਗਤੀਵਿਧੀਆਂ, ਆਰਾਮ, ਸ਼ਾਪਿੰਗ, ਇੱਕ ਦਿਨ ਦੀਆਂ ਯਾਤਰਾਵਾਂ, ਅਤੇ ਕੰਮ ਦੀ ਤੇ ਐਮਰਜੈਂਸੀ ਜਾਣਕਾਰੀ। ਨਕਸ਼ਾ ਘਰ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਦੀਆਂ ਥਾਵਾਂ ਦਿਖਾਉਂਦਾ ਹੈ, ਅਤੇ Route ਉੱਤੇ ਟੈਪ ਕਰਨ ਨਾਲ ਰਸਤਾ ਖੁੱਲ੍ਹ ਜਾਂਦਾ ਹੈ।','ਤੁਸੀਂ ਐਪ ਨੂੰ ਹੋਮ ਸਕ੍ਰੀਨ ਉੱਤੇ ਜੋੜ ਸਕਦੇ ਹੋ। ਹੋਰ ਸੁਝਾਅ ਸਾਡੀ <a href="{L}guide/">ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਟ੍ਰੈਵਲ ਗਾਈਡ</a> ਵਿੱਚ ਹਨ।'],
 card_h='ਮੁਫ਼ਤ ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ',card_d='ਹੋ ਚੀ ਮਿਨ੍ਹ ਸ਼ਹਿਰ ਦੀਆਂ ਲੋਕਲ ਟਿੱਪਸ, ਥਾਵਾਂ ਅਤੇ ਨਕਸ਼ਾ, ਫ਼ੋਨ ਦੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਮੁਫ਼ਤ।',
 home_h='ਮੁਫ਼ਤ ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ',home_p='ਸਾਡੇ ਮੁਫ਼ਤ ASCON ਟ੍ਰੈਵਲ ਗਾਈਡ ਐਪ ਨਾਲ ਆਪਣੇ ਦਿਨ ਪਲਾਨ ਕਰੋ: ਲੋਕਲ ਟਿੱਪਸ, ਖਾਣ ਅਤੇ ਘੁੰਮਣ ਦੀਆਂ ਥਾਵਾਂ ਅਤੇ ਨਕਸ਼ਾ, ਸਿੱਧਾ ਫ਼ੋਨ ਦੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ।')}
for l,t in T.items():
    f=f'content/{l}.json'; d=json.load(open(f)); P=d['pages']
    assert len(t['title'])<=60 and len(t['desc'])<=160,(l,len(t['title']),len(t['desc']))
    P['travel-guide']={'title':t['title'],'description':t['desc'],'h1':t['h1'],'lead':t['lead'],'sections':[
      {'p':[BTN%t['btn']]},
      {'h2':t['h_shots'],'p':[t['p_shots']],'imgs':[[f'tg-{k}',c] for k,c in zip(SH,t['caps'])]},
      {'h2':t['h_what'],'p':t['p_what']+[BTN%t['btn']]},
      {'cta':True}]}
    if not any(k=='travel-guide' for k,_ in d['nav']): d['nav'].append(['travel-guide',t['nav']])
    blk={'h2':t['home_h'],'p':[t['home_p']],'cards':[[t['card_h'],'travel-guide',t['card_d']]],'_tg':1}
    for pid in ('home','house'):
        S=P[pid]['sections']; S[:]=[s for s in S if not s.get('_tg')]
        i=next(i for i,s in enumerate(S) if s.get('faq') or s.get('cta')) if pid=='home' else len(S)-1
        S.insert(i,blk)
    json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
print('ok')
