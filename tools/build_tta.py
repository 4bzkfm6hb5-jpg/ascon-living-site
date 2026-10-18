"""ZH-TW / TR / AR from MR texts: extends tools/build_cjk.py (same pipeline and rules).
Travel-guide screenshots: ar = app's Arabic screenshots, zh-tw = zh (Simplified) screenshots, tr = EN."""
import re,sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
import build_cjk as B
import build_sea, build_vrf, build_epi, build_nps  # noqa: shared pattern extensions
def ext(rx,more): return re.compile(rx.pattern+'|'+more,rx.flags)
R=re.compile
B.REP.update({
 'zh-tw':[("確認後，你會收到入住資訊和ASCON Guide App的密碼。","確認後，你會收到入住資訊。ASCON Guide App免費，不需要密碼。"),
   ("密碼在預訂後提供。","免費使用，不需要密碼。"),("房客專屬ASCON Guide App","免費ASCON Guide App"),("訂房後提供密碼，出發前就能先排行程。","免費、不需密碼，出發前就能先排行程。"),
   ("訂房後就會收到密碼。","免費使用，不需要密碼。"),("訂房確認後我們會傳密碼給你。","App免費，不需要密碼。"),("什麼時候拿到密碼？","App需要密碼嗎？"),("訂房確認後。","不需要。免費，用手機瀏覽器直接打開。"),
   ("你會收到大門密碼、鐵門鑰匙說明和ASCON Guide密碼，可以提前排好每天的行程。","你會收到大門密碼和鐵門鑰匙說明；用免費的ASCON Guide App可以提前排好每天的行程。"),
   ("訂房後會收到ASCON Guide App的密碼：","免費的ASCON Guide App："),
   ("訂房確認後，會收到大門密碼、鐵門鑰匙說明，以及ASCON Guide App的密碼，裡面有地圖和實用提醒。","訂房確認後，會收到大門密碼和鐵門鑰匙說明。免費的ASCON Guide App裡有地圖和實用提醒。"),
   ("，每層樓都有煙霧偵測器與急救箱。","。"),("點歌後，歌詞會出現在4K投影布幕上，麥克風一個傳一個。","點歌後，麥克風一個傳一個。"),("有，麥克風加螢幕歌詞。","有，附卡拉OK麥克風。"),
   ("麥克風就在家裡，歌詞直接投在4K投影布幕上。","麥克風就在家裡，還有4K投影機。"),("主臥有自己的陽台，另外還有一個擺了藤椅的有頂陽台。","主臥有自己的陽台。"),
   ("、花崗岩樓梯，以及每層樓都有的安全設備。","和花崗岩樓梯。"),("、藤編沙發和串燈。","和串燈。"),("別墅","整棟房子")],
 'tr':[("Onaydan sonra giriş bilgilerini ve ASCON Guide uygulamasının şifresini alırsınız.","Onaydan sonra giriş bilgilerini alırsınız. ASCON Guide uygulaması ücretsizdir, şifre gerekmez."),
   ("Rezervasyondan sonra restoranlar, harita ve pratik bilgiler içeren ASCON Guide uygulamasının şifresi gönderilir.","Restoranlar, harita ve pratik bilgiler içeren ASCON Guide uygulaması ücretsizdir, şifre gerekmez."),
   ("ASCON Guide uygulaması, şifresi rezervasyondan sonra gönderilir.","ASCON Guide uygulaması ücretsizdir, şifre gerekmez."),
   ("Kapı şifresini, dış kapı anahtarıyla ilgili bilgileri ve ASCON Guide şifresini alırsınız.","Kapı şifresini ve dış kapı anahtarıyla ilgili bilgileri alırsınız; ücretsiz ASCON Guide uygulamasıyla günlerinizi önceden planlayabilirsiniz."),
   ("Rezervasyon onaylandıktan sonra kapı şifresini, dış kapı anahtarıyla ilgili bilgileri ve harita ile pratik notlar içeren ASCON Guide uygulamasının şifresini alırsınız.","Rezervasyon onaylandıktan sonra kapı şifresini ve dış kapı anahtarıyla ilgili bilgileri alırsınız. Ücretsiz ASCON Guide uygulamasında harita ve pratik notlar var."),
   ("Rezervasyon onaylandığında size şifreyi gönderiyoruz.","Uygulama ücretsizdir, şifre gerekmez."),
   (", her katta duman dedektörü.","."),(", rattan kanepe ve ışık zincirleri."," ve ışık zincirleri."),("Kiralık villa","Kiralık ev"),("kiralık villa","kiralık ev"),("Villa","Ev"),("villa","ev")],
 'ar':[("تحصلون على كلمة المرور بعد الحجز.","التطبيق مجاني ولا يحتاج إلى كلمة مرور."),("وتُرسل كلمة المرور بعد الحجز.","والتطبيق مجاني ولا يحتاج إلى كلمة مرور."),("كلمة المرور بعد الحجز.","مجاني ولا يحتاج إلى كلمة مرور."),
   ("بعد التأكيد تحصلون على معلومات الدخول وكلمة مرور تطبيق ASCON Guide.","بعد التأكيد تحصلون على معلومات الدخول. تطبيق ASCON Guide مجاني ولا يحتاج إلى كلمة مرور."),
   ("وبعد الحجز نرسل كلمة مرور تطبيق ASCON Guide الذي يضم","وتطبيق ASCON Guide المجاني يضم"),
   ("بعد تأكيد الحجز تحصلون على رمز الباب، ومعلومات مفتاح البوابة الخارجية، وكلمة مرور تطبيق ASCON Guide الذي يضم خريطة وملاحظات عملية.","بعد تأكيد الحجز تحصلون على رمز الباب ومعلومات مفتاح البوابة الخارجية. ويضم تطبيق ASCON Guide المجاني خريطة وملاحظات عملية."),
   ("تحصلون على رمز الباب، ومعلومات مفتاح البوابة الخارجية، وكلمة مرور ASCON Guide، فتستطيعون تخطيط","تحصلون على رمز الباب ومعلومات مفتاح البوابة الخارجية، ومع تطبيق ASCON Guide المجاني تستطيعون تخطيط"),
   ("، وتُرسل كلمة مروره بعد الحجز.","، وهو مجاني ولا يحتاج إلى كلمة مرور."),
   ("عند تأكيد الحجز نرسل إليكم كلمة المرور.","التطبيق مجاني ولا يحتاج إلى كلمة مرور."),("متى أحصل على كلمة المرور؟","هل يحتاج التطبيق إلى كلمة مرور؟"),("بعد تأكيد الحجز.","لا. التطبيق مجاني ويُفتح مباشرة في متصفح الهاتف."),
   ("تطبيق ASCON Guide الخاص بالضيوف","تطبيق ASCON Guide المجاني"),("فيلا للإيجار","منزل للإيجار"),("فيلا","منزل")]})
B.CAMN.update({'zh-tw':'入口處裝有室外監視器。','tr':'Girişte dış mekân kameraları var.','ar':'توجد كاميرات خارجية عند المدخل.'})
B.CAMCELL.update({'zh-tw':'入口處室外監視器','tr':'Girişte dış mekân kameraları','ar':'كاميرات خارجية عند المدخل'})
B.CAMX.update({'zh-tw':R(r'監視器|攝影機|鏡頭|監控'),'tr':R(r'(?i:\bkamera)'),'ar':R(r'كاميرا|كاميرات')})
B.DROP=ext(B.DROP,r'(?i:歌詞|煙霧偵測器|偵煙器|急救箱|滅火器|緊急出口|緊急照明|逃生|停車|泳池|游泳池|寵物|行李寄放|\d+\s*分鐘|'
 r'şarkı söz|duman dedektör|yangın söndür|ilk yardım|acil çıkış|acil aydınlatma|otopark|park yeri|havuz|evcil|bagaj emanet|\d+\s*dakika|'
 r'كلمات الأغاني|كلمات الأغنية|كاشف الدخان|كواشف الدخان|طفاية|الإسعافات|مخرج الطوارئ|إنارة الطوارئ|إضاءة الطوارئ|موقف سيارات|مواقف|مسبح|حمام سباحة|حيوانات أليفة|الحيوانات الأليفة|حفظ الأمتعة|\d+\s*دقيق|'
 r'有遮陽台|有頂陽台|kapalı balkon|الشرفة المغطاة|شرفة مغطاة)')
B.DROPQ=ext(B.DROPQ,r'(?i:安全|室內有監視器|室內.*監視器|güvenlik|içeride kamera|الأمان|السلامة|كاميرات داخل)')
B.DROP_SECS=R(B.DROP_SECS.pattern[:-2]+'|安全|Güvenlik|الأمان|السلامة)$')
B.DROP_ROWS=R(B.DROP_ROWS.pattern[:-2]+'|安全|Güvenlik|الأمان|السلامة)$')
B.CAMROW=R(B.CAMROW.pattern[:-2]+'|監視器|Kameralar|الكاميرات)$')
B.PAGE_DROP={'room-outside':ext(B.PAGE_DROP['room-outside'],r'(?i:陽台|藤|船|balkon|rattan|hasır|tekne|kayık|sandal|شرفة|بلكونة|الخيزران|الروطان|قارب|قوارب)'),'room-hallway':ext(B.PAGE_DROP['room-hallway'],r'(?i:陽台|balkon|شرفة|بلكونة)')}
B.RV=ext(B.RV,r'(?i:河景|nehir manzarası|إطلالة على النهر|إطلالة النهر)')
B.RVNEUT.update({'zh-tw':'景色','tr':'manzara','ar':'إطلالة'})
B.SPLIT['ar']=R(r'.+?(?:[!?؟]+\s*|\.(?:\s+|$)|$)')
B.PHOTO=R(B.PHOTO.pattern.replace('|zdjęcie|bild)','|zdjęcie|bild|圖|fotoğraf|görsel|صورة)'),B.PHOTO.flags)
B.LOC.update({'zh-tw':('常見問題','圖片'),'tr':('Sık sorulan sorular','Görseller'),'ar':('الأسئلة الشائعة','الصور')})
B.FAQSECREN.update({'zh-tw':{'安全':'其他'},'tr':{'Güvenlik':'Diğer'},'ar':{'الأمان':'أخرى','السلامة':'أخرى'}})
ui=build_epi.ui
B.UI.update({'zh-tw':ui('跳到主要內容','語言','在 Airbnb 預訂','在 Trip.com 預訂','透過 WhatsApp 預訂','透過 Zalo 預訂','地址','聯絡','更多','房客指南 App','閱讀更多','來源','估計','首頁','找不到頁面','這個頁面不存在。前往首頁：'),
 'tr':ui('İçeriğe geç','Dil','Airbnb’de rezervasyon','Trip.com’da rezervasyon','WhatsApp ile rezervasyon','Zalo ile rezervasyon','Adres','İletişim','Daha fazla','Misafir rehber uygulaması','Devamını oku','Kaynak','tahmini','Ana sayfa','Sayfa bulunamadı','Bu sayfa yok. Ana sayfaya git:'),
 'ar':ui('انتقل إلى المحتوى','اللغة','احجز على Airbnb','احجز على Trip.com','احجز عبر WhatsApp','احجز عبر Zalo','العنوان','التواصل','المزيد','تطبيق الدليل للضيوف','اقرأ المزيد','المصدر','تقدير','الرئيسية','الصفحة غير موجودة','هذه الصفحة غير موجودة. انتقل إلى الرئيسية:')})
B.NAV.update({'zh-tw':['首頁','房屋介紹','屋頂露台','家庭旅遊','團體旅遊','位置','預訂與聯絡','常見問題','住宿規則','旅遊指南','指南 App'],
 'tr':['Ana sayfa','Ev','Çatı terası','Aileler','Gruplar','Konum','Rezervasyon ve iletişim','SSS','Ev kuralları','Gezi rehberi','Rehber uygulaması'],
 'ar':['الرئيسية','المنزل','السطح','العائلات','المجموعات','الموقع','الحجز والتواصل','الأسئلة الشائعة','قواعد المنزل','دليل السفر','تطبيق الدليل']})
B.CARD.update({'zh-tw':['卡拉OK娛樂室','客廳','廚房與餐廳','主臥室','臥室 2','臥室 3','浴室','走廊與工作區','戶外與河畔','屋頂露台'],
 'tr':['Karaoke ve eğlence','Salon','Mutfak ve yemek alanı','Ebeveyn yatak odası','Yatak odası 2','Yatak odası 3','Banyolar','Koridor ve çalışma alanı','Dış mekân ve nehir','Çatı terası'],
 'ar':['الكاريوكي والترفيه','غرفة المعيشة','المطبخ وغرفة الطعام','غرفة النوم الرئيسية','غرفة النوم 2','غرفة النوم 3','الحمّامات','الممر ومساحة العمل','الخارج والنهر','السطح']})
B.ROOMSH.update({'zh-tw':'各空間介紹','tr':'Odalar ayrıntılı','ar':'الغرف بالتفصيل'})
B.FAQH.update({'zh-tw':'常見問題','tr':'Sık sorulan sorular','ar':'الأسئلة الشائعة'})
B.ROOMSEC.update({'zh-tw':'房子一覽','tr':'Kısaca ev','ar':'المنزل باختصار'})
B.CONTACTH.update({'zh-tw':'聯絡方式','tr':'İletişim','ar':'التواصل'})
T,Z,E=build_vrf.T,build_vrf.Z,build_vrf.E
B.CONTACT.update({'zh-tw':['電話與 WhatsApp：'+T,'Zalo：'+Z,'Email：'+E],'tr':['Telefon ve WhatsApp: '+T,'Zalo: '+Z,'E-posta: '+E],'ar':['الهاتف وWhatsApp: <span dir="ltr">'+T+'</span>','Zalo: <span dir="ltr">'+Z+'</span>','البريد الإلكتروني: '+E]})
M=B.MAPS
B.MAPSEC.update({'zh-tw':{'h2':'地圖','p':[f'<a href="{M}" rel="noopener">在 Google 地圖開啟地址</a>。詳細的抵達說明會在訂房後提供。']},
 'tr':{'h2':'Harita','p':[f'<a href="{M}" rel="noopener">Adresi Google Haritalar’da aç</a>. Ayrıntılı varış bilgilerini rezervasyondan sonra gönderiyoruz.']},
 'ar':{'h2':'الخريطة','p':[f'<a href="{M}" rel="noopener">افتحوا العنوان في خرائط Google</a>. نرسل تعليمات الوصول المفصلة بعد الحجز.']}})
B.APPBTN.update({'zh-tw':'打開指南 App','tr':'Rehber uygulamasını aç','ar':'افتحوا تطبيق الدليل'})
B.TG.update({'zh-tw':{'h2':'免費旅遊指南 App','p':'用ASCON免費指南App規劃每一天：在地推薦、美食與景點，還有地圖，用手機瀏覽器直接打開。','card':['免費指南 App','胡志明市在地推薦與地圖，瀏覽器免費使用。']},
 'tr':{'h2':'Ücretsiz gezi rehberi uygulaması','p':'Günlerinizi ASCON’un ücretsiz rehber uygulamasıyla planlayın: yerel öneriler, yeme içme ve gezilecek yerler ve harita, doğrudan telefonun tarayıcısında.','card':['Ücretsiz rehber uygulaması','Ho Chi Minh için öneriler ve harita, tarayıcıda ücretsiz.']},
 'ar':{'h2':'تطبيق دليل سفر مجاني','p':'خطّطوا أيامكم مع تطبيق الدليل المجاني من ASCON: نصائح محلية وأماكن للأكل والزيارة وخريطة، مباشرة في متصفح الهاتف.','card':['تطبيق دليل مجاني','نصائح وخريطة هو تشي منه، مجانًا في المتصفح.']}})
B.HOUSE.update({
 'zh-tw':dict(title='胡志明市包棟民宿：每個空間一次看 | ASCON',description='三層樓加屋頂露台：3間附衛浴的臥室、約40㎡客廳、設備齊全的廚房，以及有4K投影機的卡拉OK娛樂室。',h1='房屋介紹：胡志明市的包棟住宿',lead='三層樓、屋頂露台，超過250㎡只屬於你們這一團。這裡有每個空間的照片和設備。'),
 'tr':dict(title='Ho Chi Minh’te kiralık ev, oda oda | ASCON',description='Üç kat ve çatı terası: banyolu 3 yatak odası, yaklaşık 40 m² salon, tam donanımlı mutfak ve 4K projektörlü karaoke odası.',h1='Ev: Ho Chi Minh’teki konaklamanız, oda oda',lead='Üç kat, çatı terası ve yalnızca grubunuza ait 250 m²’den fazla alan. Burada her odanın fotoğraflarını ve donanımını bulabilirsiniz.'),
 'ar':dict(title='منزل كامل في هو تشي منه، غرفة بغرفة | ASCON',description='ثلاثة طوابق وسطح: 3 غرف نوم بحمّامات خاصة، وغرفة معيشة بنحو 40 م²، ومطبخ مجهّز بالكامل، وغرفة كاريوكي بجهاز عرض 4K.',h1='المنزل: إقامتكم في هو تشي منه، غرفة بغرفة',lead='ثلاثة طوابق وسطح وأكثر من 250 م² لمجموعتكم وحدها. هنا صور كل غرفة وتجهيزاتها.')})
B.OUTSIDE.update({'zh-tw':dict(h1='河畔戶外：露台與河景頂樓',lead='西貢的天氣適合待在戶外。ASCON LIVING有白色欄杆的露台和頂樓露台，白天晚上都有地方坐。',description='胡志明市河畔包棟民宿：白色欄杆與遮雨棚的露台，面對河流與第一郡天際線。'),
 'tr':dict(title='Nehir Kenarında Dış Mekan ve Teras | ASCON LIVING',h1='Nehir kenarında dış mekan: teras ve manzaralı çatı',lead='Saygon’un havası dışarıda oturmaya davet eder. ASCON LIVING’de beyaz korkuluklu bir teras ve bir çatı terası var; gündüz de akşam da oturacak bir yer bulunur.',description='Ho Chi Minh’te nehir kenarında ev: beyaz korkuluklu ve tenteli teras, karşıda nehir ve 1. Bölge silueti.'),
 'ar':dict(title='منزل على ضفة النهر: التراس والسطح | ASCON LIVING',h1='على ضفة النهر: التراس والسطح المطل على النهر',lead='طقس سايغون يدعو إلى الجلوس في الخارج. في ASCON LIVING تراس بدرابزين أبيض وسطح، فتجدون مكانًا للجلوس نهارًا ومساءً.',description='منزل على ضفة النهر في هو تشي منه: تراس بدرابزين أبيض ومظلة، أمامها النهر وأفق المنطقة 1.')})
tgp=build_epi.tgp
B.TGP.update({
 'zh-tw':tgp('胡志明市免費旅遊指南 App | ASCON','ASCON免費指南App：在地推薦、吃什麼看什麼、地圖和胡志明市實用資訊，用手機瀏覽器就能打開。','胡志明市免費旅遊指南 App','ASCON Guide是免費的網頁App，收錄胡志明市的在地推薦和好去處。用手機瀏覽器直接打開：不需要密碼，也不用安裝。',
   'App 畫面一覽','以下是App在手機上的實際截圖（App目前沒有繁體中文，所以畫面顯示簡體中文版）。',['ASCON LIVING標誌與標語的歡迎畫面','選擇語言：App提供十種語言','分類：美食、咖啡、酒吧、親子出遊等','房子周邊地點的地圖','實用資訊與緊急協助'],
   '在地推薦與好去處',['地點依分類整理：美食、咖啡與甜點、酒吧與夜生活、親子、景點與文化、活動、放鬆、購物、一日遊，以及實用與緊急資訊。地圖顯示房子周邊的地點，點「路線」即可開始導航。','可以把App加到手機主畫面。更多點子請看我們的<a href="{L}guide/">胡志明市旅遊指南</a>。']),
 'tr':tgp('Ho Chi Minh için ücretsiz rehber uygulaması | ASCON','ASCON’un ücretsiz rehber uygulaması: yerel öneriler, nerede yenir ve ne görülür, harita ve Ho Chi Minh için pratik yardım. Telefon tarayıcısında açılır.','Ho Chi Minh için ücretsiz gezi rehberi uygulaması','ASCON Guide, Ho Chi Minh’teki yerel öneriler ve mekânlarla dolu ücretsiz bir web uygulamasıdır. Doğrudan telefonun tarayıcısında açılır: şifre yok, kurulum yok.',
   'Uygulamaya göz atın','Bunlar uygulamanın telefondaki gerçek ekran görüntüleridir (uygulamada henüz Türkçe yok, bu yüzden ekranlar İngilizce).',['ASCON LIVING logosu ve sloganıyla karşılama ekranı','Dil seçimi: uygulama on dilde','Kategoriler: yemek, kafeler, barlar, aile gezileri ve daha fazlası','Evin çevresindeki yerlerin haritası','Pratik bilgiler ve acil durum yardımı'],
   'Yerel öneriler ve mekânlar',['Mekânlar kategorilere ayrılmıştır: yemek, kafeler ve tatlılar, barlar ve gece hayatı, çocuklar ve aile, turistik yerler ve kültür, aktiviteler, dinlenme, alışveriş, günübirlik geziler ile pratik ve acil durum bilgileri. Harita evin çevresindeki yerleri gösterir; Yol tarifi düğmesi navigasyonu başlatır.','Uygulamayı ana ekrana ekleyebilirsiniz. Daha fazla fikir için <a href="{L}guide/">Ho Chi Minh gezi rehberimize</a> göz atın.']),
 'ar':tgp('تطبيق دليل مجاني لهو تشي منه | ASCON','تطبيق الدليل المجاني من ASCON: نصائح محلية وأين تأكلون وماذا تشاهدون وخريطة ومساعدة عملية في هو تشي منه. يُفتح في متصفح الهاتف.','تطبيق دليل سفر مجاني لهو تشي منه','ASCON Guide تطبيق ويب مجاني فيه نصائح محلية وأماكن في هو تشي منه. يُفتح مباشرة في متصفح الهاتف: بلا كلمة مرور وبلا تثبيت.',
   'هكذا يبدو التطبيق','هذه لقطات شاشة حقيقية للتطبيق على الهاتف.',['شاشة الترحيب مع شعار ASCON LIVING وعبارتها','اختيار اللغة: التطبيق متاح بعشر لغات','الفئات: الطعام والمقاهي والحانات ونزهات العائلة وغيرها','خريطة الأماكن حول المنزل','معلومات عملية ومساعدة في حالات الطوارئ'],
   'نصائح وأماكن محلية',['الأماكن مرتبة في فئات: الطعام، المقاهي والحلويات، الحانات والحياة الليلية، الأطفال والعائلة، المعالم والثقافة، الأنشطة، الاسترخاء، التسوق، الرحلات اليومية، والمعلومات العملية ومعلومات الطوارئ. تعرض الخريطة الأماكن حول المنزل، ويبدأ زر الاتجاهات الملاحة.','يمكنكم إضافة التطبيق إلى الشاشة الرئيسية. لمزيد من الأفكار اطّلعوا على <a href="{L}guide/">دليل السفر إلى هو تشي منه</a>.'])})
B.RULES.update({
 'zh-tw':{'h2':'基本規則','flow':[['ul',['入住 14:00–23:00，退房 12:00。','依越南法律，房客須辦理住宿登記。','室內禁菸，只能在指定的戶外區域吸菸。','大聲音樂只到 21:30。','禁止喧鬧派對。','只有登記的房客可以入住。']]]},
 'tr':{'h2':'Temel kurallar','flow':[['ul',['Giriş 14:00–23:00, çıkış 12:00.','Vietnam yasalarına göre misafirlerin kaydı zorunludur.','Ev içinde sigara içilmez; yalnızca belirlenmiş açık alanlarda.','Yüksek sesli müzik 21:30’a kadar.','Gürültülü parti yok.','Yalnızca kayıtlı misafirler konaklayabilir.']]]},
 'ar':{'h2':'القواعد الأساسية','flow':[['ul',['تسجيل الدخول 14:00–23:00، وتسجيل المغادرة 12:00.','وفق القانون الفيتنامي يجب تسجيل الضيوف.','يُمنع التدخين داخل المنزل؛ التدخين فقط في الأماكن الخارجية المخصصة.','الموسيقى الصاخبة حتى 21:30 فقط.','لا حفلات صاخبة.','الإقامة للضيوف المسجلين فقط.']]]}})
B.KWCAP.update({'zh-tw':[("第七郡整棟住宿的廚房：","整棟住宿的廚房："),("第七郡的步調","這裡的步調"),("Tân Hưng, 胡志明市第七郡。","Tân Hưng, 胡志明市。")],
 'tr':[("7. Bölge'deki kiralık evin mutfağı:","Kiralık evin mutfağı:"),("7. Bölge'de hayat daha çok yerel","Burada hayat daha çok yerel"),("Tân Hưng, 7. Bölge, Ho Chi Minh şehri.","Tân Hưng, Ho Chi Minh şehri."),("Ho Chi Minh şehri, 7. Bölge, Tân Hưng,","Ho Chi Minh şehri, Tân Hưng,"),("Ho Chi Minh 7. Bölge'deki evden","Evden")],
 'ar':[("مطبخ المنزل في المنطقة 7:","مطبخ المنزل:"),("تان هونغ، المنطقة 7، مدينة هو تشي منه.","تان هونغ، مدينة هو تشي منه."),("أما في المنطقة 7 فتسير","أما هنا فتسير"),("من المنزل في المنطقة 7 بمدينة هو تشي منه","من المنزل")]})
LANGS=('zh-tw','tr','ar')
if __name__=='__main__':
    for l in (sys.argv[1:] or LANGS): B.build(l)
    for x in B.LOG: print(*x,sep=' | ')
