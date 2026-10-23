"""Booking-page copy and headline rules.

Karaoke, PS5 and gaming stay in body copy, amenities and captions.
They are removed from <title> and <h1> only. Korean karaoke is 노래방.
The cinema setup is named in full, with Netflix beside it.
Agoda is not linked: Airbnb listing 1789707041970520479 and Trip.com 136163015 only.
"""
import os, re, json, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Bright, real house photos for the hero (not the dusk rooftop).
HERO = ['living', 'bed1', 'roof-day', 'river-city', 'kitchen']
NAV = ['booking', 'house', 'rooftop', 'location', 'faq']
# Trip.com leads where it is the stronger of the two allowed platforms.
TRIP_FIRST = {'ko', 'ja', 'vi', 'zh', 'zh-tw'}

CJK = {'ko', 'ja', 'zh', 'zh-tw'}

CINEMA = {
    'en': '4K cinema system (Optoma 4K projector)',
    'de': '4K-Kinosystem (Optoma 4K-Projektor)',
    'vi': 'hệ thống rạp 4K (máy chiếu Optoma 4K)',
    'zh': '4K影院系统（Optoma 4K投影仪）',
    'zh-tw': '4K影院系統（Optoma 4K投影機）',
    'hi': '4K सिनेमा सिस्टम (Optoma 4K प्रोजेक्टर)',
    'es': 'sistema de cine 4K (proyector Optoma 4K)',
    'ar': 'نظام سينما 4K (جهاز عرض Optoma 4K)',
    'fr': 'système cinéma 4K (projecteur Optoma 4K)',
    'pt': 'sistema de cinema 4K (projetor Optoma 4K)',
    'ru': 'киносистема 4K (проектор Optoma 4K)',
    'ur': '4K سنیما سسٹم (Optoma 4K پروجیکٹر)',
    'id': 'sistem bioskop 4K (proyektor Optoma 4K)',
    'ja': '4Kシネマシステム（Optoma 4Kプロジェクター）',
    'ko': '4K 시네마 시스템 (Optoma 4K 프로젝터)',
    'pa': '4K ਸਿਨੇਮਾ ਸਿਸਟਮ (Optoma 4K ਪ੍ਰੋਜੈਕਟਰ)',
    'th': 'ระบบโรงภาพยนตร์ 4K (โปรเจ็กเตอร์ Optoma 4K)',
    'ms': 'sistem pawagam 4K (projektor Optoma 4K)',
    'it': 'sistema cinema 4K (proiettore Optoma 4K)',
    'nl': '4K-bioscoopsysteem (Optoma 4K-projector)',
    'tr': '4K sinema sistemi (Optoma 4K projektör)',
    'pl': 'system kinowy 4K (projektor Optoma 4K)',
    'sv': '4K-biosystem (Optoma 4K-projektor)',
}
# Shorter names already in copy, longest first. Not applied to title or h1.
CINEMA_SHORT = {
    'en': ['4K cinema projector', 'cinema projector', '4K projector'],
    'de': ['4K-Kinoprojektor', 'Kinoprojektor', '4K-Projektor'],
    'vi': ['máy chiếu phim 4K', 'máy chiếu 4K', '4K projector'],
    'zh': ['4K投影仪', '4K投影机', '投影仪'],
    'zh-tw': ['4K投影機', '4K投影儀'],
    'hi': ['4K प्रोजेक्टर'],
    'es': ['proyector 4K', 'proyector de cine'],
    'ar': ['جهاز عرض 4K', 'بروجيكتور 4K'],
    'fr': ['vidéoprojecteur 4K', 'projecteur 4K', 'projecteur cinéma'],
    'pt': ['projetor 4K'],
    'ru': ['4K-проектор', 'проектор 4K'],
    'ur': ['4K پروجیکٹر'],
    'id': ['proyektor 4K'],
    'ja': ['4Kプロジェクター', '4Kプロジェクタ'],
    'ko': ['4K 프로젝터', '4K 프로젝터'],
    'pa': ['4K ਪ੍ਰੋਜੈਕਟਰ'],
    'th': ['โปรเจ็กเตอร์ 4K', 'โปรเจคเตอร์ 4K'],
    'ms': ['projektor 4K'],
    'it': ['proiettore 4K'],
    'nl': ['4K-projector'],
    'tr': ['4K projektör', '4K projektörü'],
    'pl': ['projektor 4K'],
    'sv': ['4K-projektor'],
}

PS = {
    'en': 'PS5 (PlayStation 5) with PlayStation Plus',
    'de': 'PS5 (PlayStation 5) mit PlayStation Plus',
    'vi': 'PS5 (PlayStation 5) với PlayStation Plus',
    'zh': 'PS5（PlayStation 5）与 PlayStation Plus',
    'zh-tw': 'PS5（PlayStation 5）與 PlayStation Plus',
    'hi': 'PS5 (PlayStation 5) और PlayStation Plus',
    'es': 'PS5 (PlayStation 5) con PlayStation Plus',
    'ar': 'PS5 (PlayStation 5) مع PlayStation Plus',
    'fr': 'PS5 (PlayStation 5) avec PlayStation Plus',
    'pt': 'PS5 (PlayStation 5) com PlayStation Plus',
    'ru': 'PS5 (PlayStation 5) с PlayStation Plus',
    'ur': 'PS5 (PlayStation 5) مع PlayStation Plus',
    'id': 'PS5 (PlayStation 5) dengan PlayStation Plus',
    'ja': 'PS5（PlayStation 5）と PlayStation Plus',
    'ko': 'PS5 (PlayStation 5), PlayStation Plus',
    'pa': 'PS5 (PlayStation 5) ਅਤੇ PlayStation Plus',
    'th': 'PS5 (PlayStation 5) พร้อม PlayStation Plus',
    'ms': 'PS5 (PlayStation 5) dengan PlayStation Plus',
    'it': 'PS5 (PlayStation 5) con PlayStation Plus',
    'nl': 'PS5 (PlayStation 5) met PlayStation Plus',
    'tr': 'PS5 (PlayStation 5) ve PlayStation Plus',
    'pl': 'PS5 (PlayStation 5) z PlayStation Plus',
    'sv': 'PS5 (PlayStation 5) med PlayStation Plus',
}
KARAOKE = {
    'en': 'Karaoke', 'de': 'Karaoke', 'vi': 'Karaoke', 'zh': '卡拉OK', 'zh-tw': '卡拉OK',
    'hi': 'कराओके', 'es': 'Karaoke', 'ar': 'كاريوكي', 'fr': 'Karaoké', 'pt': 'Karaokê',
    'ru': 'Караоке', 'ur': 'کراؤکے', 'id': 'Karaoke', 'ja': 'カラオケ', 'ko': '노래방',
    'pa': 'ਕਰਾਓਕੇ', 'th': 'คาราโอเกะ', 'ms': 'Karaoke', 'it': 'Karaoke', 'nl': 'Karaoke',
    'tr': 'Karaoke', 'pl': 'Karaoke', 'sv': 'Karaoke',
}
GAMING = {
    'en': 'Gaming', 'de': 'Gaming', 'vi': 'Gaming', 'zh': '游戏 (Gaming)', 'zh-tw': '遊戲 (Gaming)',
    'hi': 'गेमिंग (Gaming)', 'es': 'Gaming', 'ar': 'ألعاب (Gaming)', 'fr': 'Gaming', 'pt': 'Gaming',
    'ru': 'игры (Gaming)', 'ur': 'Gaming', 'id': 'Gaming', 'ja': 'ゲーム (Gaming)', 'ko': '게임 (Gaming)',
    'pa': 'Gaming', 'th': 'เกม (Gaming)', 'ms': 'Gaming', 'it': 'Gaming', 'nl': 'Gaming',
    'tr': 'Gaming', 'pl': 'Gaming', 'sv': 'Gaming',
}
ENT_H2 = {
    'en': 'In the entertainment room',
    'de': 'Im Entertainment-Raum',
    'vi': 'Trong phòng giải trí',
    'zh': '娱乐室里有',
    'zh-tw': '娛樂室裡有',
    'hi': 'एंटरटेनमेंट रूम में',
    'es': 'En la sala de ocio',
    'ar': 'في غرفة الترفيه',
    'fr': 'Dans la salle de loisirs',
    'pt': 'Na sala de lazer',
    'ru': 'В комнате отдыха',
    'ur': 'تفریحی کمرے میں',
    'id': 'Di ruang hiburan',
    'ja': 'エンタメルーム',
    'ko': '엔터테인먼트룸',
    'pa': 'ਮਨੋਰੰਜਨ ਕਮਰੇ ਵਿੱਚ',
    'th': 'ในห้องบันเทิง',
    'ms': 'Dalam bilik hiburan',
    'it': 'Nella sala svago',
    'nl': 'In de entertainmentkamer',
    'tr': 'Eğlence odasında',
    'pl': 'W pokoju rekreacji',
    'sv': 'I underhållningsrummet',
}

# title, h1 — accommodation words only. description may name the room's real gear.
ENT = {
    'en': ('Whole House Rental Saigon: Entertainment | ASCON',
           'Entertainment room in the whole house in Ho Chi Minh City',
           'Whole house in Saigon: karaoke, PS5, gaming, a 4K cinema system (Optoma 4K projector) and Netflix.'),
    'de': ('Ferienhaus Saigon: Entertainment-Raum | ASCON',
           'Ferienhaus in Ho-Chi-Minh-Stadt: euer Entertainment-Raum',
           'Ferienhaus in Saigon: Karaoke, PS5, Gaming, ein 4K-Kinosystem (Optoma 4K-Projektor) und Netflix.'),
    'vi': ('Homestay nguyên căn: phòng giải trí | ASCON',
           'Phòng giải trí trong nhà nguyên căn tại Sài Gòn',
           'Nhà nguyên căn tại Sài Gòn: karaoke, PS5, gaming, hệ thống rạp 4K (máy chiếu Optoma 4K) và Netflix.'),
    'zh': ('胡志明包栋民宿 娱乐室 | ASCON LIVING',
           '胡志明包栋民宿里的娱乐室',
           '整栋民宿的娱乐室：卡拉OK、PS5、游戏、4K影院系统（Optoma 4K投影仪）和 Netflix。'),
    'zh-tw': ('胡志明包棟民宿 娛樂室 | ASCON LIVING',
             '胡志明包棟民宿裡的娛樂室',
             '整棟民宿的娛樂室：卡拉OK、PS5、遊戲、4K影院系統（Optoma 4K投影機）和 Netflix。'),
    'hi': ('Ho Chi Minh में पूरा घर: मनोरंजन कक्ष | ASCON',
           'पूरे घर का एंटरटेनमेंट रूम, हो ची मिन्ह',
           'पूरे घर में कराओके, PS5, गेमिंग, 4K सिनेमा सिस्टम (Optoma 4K प्रोजेक्टर) और Netflix।'),
    'es': ('Casa entera en Saigón: sala de ocio | ASCON',
           'Sala de ocio en la casa entera, Ho Chi Minh',
           'Casa entera en Saigón: karaoke, PS5, gaming, sistema de cine 4K (proyector Optoma 4K) y Netflix.'),
    'ar': ('منزل كامل في سايغون: غرفة الترفيه | ASCON',
           'غرفة الترفيه في المنزل الكامل، هو تشي منه',
           'منزل كامل: كاريوكي وPS5 وألعاب ونظام سينما 4K (جهاز عرض Optoma 4K) وNetflix.'),
    'fr': ('Maison entière à Saigon : salle de loisirs | ASCON',
           'Salle de loisirs dans la maison entière à Hô Chi Minh-Ville',
           'Maison entière à Saigon : karaoké, PS5, gaming, système cinéma 4K (projecteur Optoma 4K) et Netflix.'),
    'pt': ('Casa inteira em Saigon: sala de lazer | ASCON',
           'Sala de lazer na casa inteira em Ho Chi Minh',
           'Casa inteira em Saigon: karaokê, PS5, gaming, sistema de cinema 4K (projetor Optoma 4K) e Netflix.'),
    'ru': ('Дом целиком в Хошимине: комната отдыха | ASCON',
           'Комната отдыха в целом доме в Хошимине',
           'Весь дом: караоке, PS5, игры, киносистема 4K (проектор Optoma 4K) и Netflix.'),
    'ur': ('ہو چی منہ میں پورا گھر: تفریحی کمرہ | ASCON',
           'پورے گھر کا تفریحی کمرہ، ہو چی منہ',
           'پورا گھر: کراؤکے، PS5، گیمنگ، 4K سنیما سسٹم (Optoma 4K پروجیکٹر) اور Netflix۔'),
    'id': ('Rumah utuh di Saigon: ruang hiburan | ASCON',
           'Ruang hiburan di rumah utuh, Ho Chi Minh',
           'Rumah utuh: karaoke, PS5, gaming, sistem bioskop 4K (proyektor Optoma 4K) dan Netflix.'),
    'ja': ('ホーチミン 一軒家のエンタメルーム | ASCON LIVING',
           'ホーチミンの一軒家：貸切のエンタメルーム',
           '一軒家のエンタメルーム：カラオケ、PS5、ゲーム、4Kシネマシステム（Optoma 4Kプロジェクター）、Netflix。'),
    'ko': ('호치민 독채 숙소 엔터테인먼트룸 | ASCON LIVING',
           '호치민 숙소의 엔터테인먼트룸',
           '독채 엔터테인먼트룸: 노래방, PS5, 게임, 4K 시네마 시스템 (Optoma 4K 프로젝터), Netflix.'),
    'pa': ('Ho Chi Minh ਵਿੱਚ ਪੂਰਾ ਘਰ: ਮਨੋਰੰਜਨ ਕਮਰਾ | ASCON',
           'ਪੂਰੇ ਘਰ ਦਾ ਮਨੋਰੰਜਨ ਕਮਰਾ',
           'ਪੂਰਾ ਘਰ: ਕਰਾਓਕੇ, PS5, ਗੇਮਿੰਗ, 4K ਸਿਨੇਮਾ ਸਿਸਟਮ (Optoma 4K ਪ੍ਰੋਜੈਕਟਰ) ਅਤੇ Netflix।'),
    'th': ('ที่พักทั้งหลังโฮจิมินห์: ห้องบันเทิง | ASCON',
           'ห้องบันเทิงในบ้านทั้งหลังที่โฮจิมินห์',
           'บ้านทั้งหลัง: คาราโอเกะ, PS5, เกม, ระบบโรงภาพยนตร์ 4K (โปรเจ็กเตอร์ Optoma 4K) และ Netflix'),
    'ms': ('Rumah penuh di Saigon: bilik hiburan | ASCON',
           'Bilik hiburan dalam rumah penuh di Ho Chi Minh',
           'Rumah penuh: karaoke, PS5, gaming, sistem pawagam 4K (projektor Optoma 4K) dan Netflix.'),
    'it': ('Casa intera a Saigon: sala svago | ASCON',
           'Sala svago nella casa intera a Ho Chi Minh',
           'Casa intera: karaoke, PS5, gaming, sistema cinema 4K (proiettore Optoma 4K) e Netflix.'),
    'nl': ('Heel huis in Saigon: entertainmentkamer | ASCON',
           'Entertainmentkamer in het hele huis in Ho Chi Minh',
           'Heel huis: karaoke, PS5, gaming, een 4K-bioscoopsysteem (Optoma 4K-projector) en Netflix.'),
    'tr': ('Ho Chi Minh\'te bütün ev: eğlence odası | ASCON',
           'Bütün evin eğlence odası, Ho Chi Minh',
           'Bütün ev: karaoke, PS5, gaming, 4K sinema sistemi (Optoma 4K projektör) ve Netflix.'),
    'pl': ('Cały dom w Sajgonie: pokój rekreacji | ASCON',
           'Pokój rekreacji w całym domu w Ho Chi Minh',
           'Cały dom: karaoke, PS5, gaming, system kinowy 4K (projektor Optoma 4K) i Netflix.'),
    'sv': ('Hela huset i Saigon: underhållningsrum | ASCON',
           'Underhållningsrummet i hela huset i Ho Chi Minh',
           'Hela huset: karaoke, PS5, gaming, ett 4K-biosystem (Optoma 4K-projektor) och Netflix.'),
}

# Market Researcher, 23 Oct 2026. These replace the earlier homepage title suggestions.
HOME = {
    'en': {
        'title': 'Saigon House Rental – Whole Homestay | ASCON LIVING',
        'h1': 'Saigon house rental: a whole homestay just for your group',
        'description': 'Rent a whole house in Saigon: 3 en-suite bedrooms, rooftop with BBQ, karaoke and PlayStation room, full kitchen, self check-in. Book direct.',
    },
    'de': {
        'title': 'Ferienhaus Ho Chi Minh Stadt – ganzes Haus | ASCON LIVING',
        'h1': 'Ferienhaus in Ho Chi Minh Stadt – das ganze Haus für euch',
        'description': 'Ferienhaus in Ho Chi Minh Stadt (Saigon) ganz für euch: 3 Schlafzimmer mit eigenem Bad, Dachterrasse mit BBQ, Karaoke, Küche, Self-Check-in.',
    },
    'ja': {
        'title': 'ホーチミンの一軒家貸切宿泊 | ASCON LIVING',
        'h1': 'ホーチミンで一軒家まるごと貸切の宿泊先',
        'description': 'ホーチミンで一軒家をまるごと貸切。専用バス付き寝室3室、ルーフトップBBQ、カラオケ・PlayStation、フルキッチン、セルフチェックイン。家族・グループ旅行に。',
    },
    'vi': {
        'title': 'Homestay Sài Gòn nguyên căn – cả ngôi nhà | ASCON LIVING',
        'h1': 'Homestay Sài Gòn nguyên căn dành riêng cho nhóm của bạn',
        'description': 'Homestay Sài Gòn nguyên căn: 3 phòng ngủ có WC riêng, sân thượng BBQ, phòng karaoke và PlayStation, bếp đầy đủ, tự check-in. Đặt trực tiếp.',
    },
    'ko': {
        'title': '호치민 숙소 추천 – 독채 단독주택 통째로 | ASCON LIVING',
        'h1': '호치민 숙소 추천: 우리 일행만 쓰는 독채 ASCON LIVING',
        'description': '호치민 숙소 추천, 집 한 채를 통째로 쓰는 독채. 전용 욕실 딸린 침실 3개, 루프탑 BBQ, 노래방·PlayStation, 풀 주방, 셀프 체크인. 가족·단체 여행에.',
    },
}

KICKER = {
    'en': 'Check availability', 'de': 'Jetzt buchen', 'vi': 'Kiểm tra phòng trống',
    'zh': '查看可订日期', 'zh-tw': '查看可訂日期', 'hi': 'उपलब्धता देखें',
    'es': 'Comprobar disponibilidad', 'ar': 'تحقق من التوفر', 'fr': 'Vérifier les disponibilités',
    'pt': 'Verificar disponibilidade', 'ru': 'Проверить даты', 'ur': 'دستیابی دیکھیں',
    'id': 'Cek ketersediaan', 'ja': '空室を確認', 'ko': '예약 가능일 확인',
    'pa': 'ਉਪਲਬਧਤਾ ਵੇਖੋ', 'th': 'ดูวันว่าง', 'ms': 'Semak kekosongan',
    'it': 'Verifica disponibilità', 'nl': 'Beschikbaarheid', 'tr': 'Müsaitliği kontrol et',
    'pl': 'Sprawdź dostępność', 'sv': 'Se lediga datum',
}
# No nightly number. The hero line asks the guest to contact the host.
PRICE = {
    'en': 'Contact us for a price',
    'de': 'Preis auf Anfrage – kontaktieren Sie uns',
    'vi': 'Liên hệ để biết giá',
    'ko': '가격 문의',
    'ja': '料金はお問い合わせください',
    'zh': '价格请联系我们',
    'zh-tw': '價格請聯絡我們',
    'hi': 'कीमत के लिए हमसे संपर्क करें',
    'es': 'Precio a consultar – contáctenos',
    'ar': 'تواصلوا معنا لمعرفة السعر',
    'fr': 'Prix sur demande – contactez-nous',
    'pt': 'Preço sob consulta – fale conosco',
    'ru': 'Цена по запросу — свяжитесь с нами',
    'ur': 'قیمت کے لیے ہم سے رابطہ کریں',
    'id': 'Hubungi kami untuk harga',
    'pa': 'ਕੀਮਤ ਲਈ ਸਾਡੇ ਨਾਲ ਸੰਪਰਕ ਕਰੋ',
    'th': 'ติดต่อเราเพื่อสอบถามราคา',
    'ms': 'Hubungi kami untuk harga',
    'it': 'Prezzo su richiesta – contattateci',
    'nl': 'Prijs op aanvraag – neem contact op',
    'tr': 'Fiyat için bize ulaşın',
    'pl': 'Cena na zapytanie – skontaktuj się z nami',
    'sv': 'Pris på förfrågan – kontakta oss',
}
FACTS = {
    'en': [('Whole house', 'One group, the entire house'), ('3 bedrooms', 'Each with a private bath'), ('250+ m²', 'Three floors plus rooftop'), ('Rooftop terrace', 'Open air above the house'), ('River view', 'From the rooftop')],
    'de': [('Ganzes Haus', 'Eine Gruppe, das ganze Haus'), ('3 Schlafzimmer', 'Jedes mit eigenem Bad'), ('250+ m²', 'Drei Etagen plus Dach'), ('Dachterrasse', 'Unter freiem Himmel'), ('Flussblick', 'Von der Dachterrasse')],
    'vi': [('Nhà nguyên căn', 'Một nhóm, cả căn nhà'), ('3 phòng ngủ', 'Mỗi phòng một phòng tắm'), ('250+ m²', 'Ba tầng và sân thượng'), ('Sân thượng', 'Không gian ngoài trời'), ('View sông', 'Từ sân thượng')],
    'ja': [('一軒家', '一組だけで貸切'), ('寝室3室', 'それぞれ専用バス'), ('250㎡超', '3階＋ルーフトップ'), ('ルーフトップ', '屋上のテラス'), ('川の眺め', '屋上から')],
    'ko': [('독채', '한 팀이 집 전체'), ('침실 3개', '각 방 전용 욕실'), ('250㎡ 이상', '3층과 루프탑'), ('루프탑', '옥상 테라스'), ('강 전망', '루프탑에서')],
    'zh': [('整栋房子', '一组客人包栋'), ('3间卧室', '每间独立卫浴'), ('250㎡以上', '三层加屋顶'), ('屋顶露台', '户外平台'), ('河景', '从屋顶看出去')],
    'zh-tw': [('整棟房子', '一組客人包棟'), ('3間臥室', '每間獨立衛浴'), ('250㎡以上', '三層加屋頂'), ('屋頂露台', '戶外平台'), ('河景', '從屋頂看出去')],
    'fr': [('Maison entière', 'Un groupe, toute la maison'), ('3 chambres', 'Chacune avec salle de bain'), ('250+ m²', 'Trois étages plus toit'), ('Toit-terrasse', 'En plein air'), ('Vue sur la rivière', 'Depuis le toit')],
    'es': [('Casa entera', 'Un grupo, toda la casa'), ('3 dormitorios', 'Cada uno con baño'), ('250+ m²', 'Tres plantas y azotea'), ('Azotea', 'Al aire libre'), ('Vista al río', 'Desde la azotea')],
    'it': [('Casa intera', 'Un gruppo, tutta la casa'), ('3 camere', 'Ognuna con bagno'), ('250+ m²', 'Tre piani e terrazza'), ('Terrazza', 'All\'aperto'), ('Vista fiume', 'Dalla terrazza')],
    'nl': [('Heel huis', 'Eén gezelschap, het hele huis'), ('3 slaapkamers', 'Elk een eigen badkamer'), ('250+ m²', 'Drie verdiepingen plus dak'), ('Dakterras', 'Buitenlucht'), ('Rivierzicht', 'Vanaf het dak')],
    'pt': [('Casa inteira', 'Um grupo, a casa toda'), ('3 quartos', 'Cada um com banheiro'), ('250+ m²', 'Três andares e terraço'), ('Terraço', 'Ao ar livre'), ('Vista do rio', 'Do terraço')],
    'pl': [('Cały dom', 'Jedna grupa, cały dom'), ('3 sypialnie', 'Każda z własną łazienką'), ('250+ m²', 'Trzy piętra i taras'), ('Taras na dachu', 'Pod gołym niebem'), ('Widok na rzekę', 'Z tarasu')],
    'sv': [('Hela huset', 'Ett sällskap, hela huset'), ('3 sovrum', 'Vart och ett med badrum'), ('250+ m²', 'Tre våningar och tak'), ('Takterrass', 'Utomhus'), ('Flodutsikt', 'Från taket')],
    'ru': [('Весь дом', 'Одна компания, весь дом'), ('3 спальни', 'У каждой своя ванная'), ('250+ м²', 'Три этажа и крыша'), ('Терраса', 'На крыше'), ('Вид на реку', 'С террасы')],
    'tr': [('Bütün ev', 'Bir grup, evin tamamı'), ('3 yatak odası', 'Her birinin kendi banyosu'), ('250+ m²', 'Üç kat ve çatı'), ('Çatı terası', 'Açık hava'), ('Nehir manzarası', 'Çatıdan')],
    'id': [('Rumah utuh', 'Satu kelompok, seluruh rumah'), ('3 kamar tidur', 'Masing-masing kamar mandi'), ('250+ m²', 'Tiga lantai plus atap'), ('Rooftop', 'Teras terbuka'), ('Pemandangan sungai', 'Dari atap')],
    'ms': [('Rumah penuh', 'Satu kumpulan, seluruh rumah'), ('3 bilik tidur', 'Setiap satu bilik air sendiri'), ('250+ m²', 'Tiga tingkat dan bumbung'), ('Rooftop', 'Teres terbuka'), ('Pemandangan sungai', 'Dari bumbung')],
    'th': [('บ้านทั้งหลัง', 'หนึ่งกลุ่ม ทั้งหลัง'), ('3 ห้องนอน', 'ทุกห้องมีห้องน้ำในตัว'), ('250+ ตร.ม.', 'สามชั้นและดาดฟ้า'), ('ดาดฟ้า', 'ระเบียงโล่ง'), ('วิวแม่น้ำ', 'จากดาดฟ้า')],
    'hi': [('पूरा घर', 'एक समूह, पूरा घर'), ('3 बेडरूम', 'हर कमरे का अपना बाथ'), ('250+ m²', 'तीन मंज़िल और छत'), ('रूफटॉप', 'खुली छत'), ('नदी का दृश्य', 'छत से')],
    'ar': [('منزل كامل', 'مجموعة واحدة، المنزل كله'), ('3 غرف نوم', 'لكل غرفة حمّام'), ('250+ م²', 'ثلاثة طوابق وسطح'), ('سطح', 'تراس في الهواء'), ('إطلالة على النهر', 'من السطح')],
    'ur': [('پورا گھر', 'ایک گروپ، سارا گھر'), ('3 بیڈروم', 'ہر کمرے کا اپنا باتھ'), ('250+ m²', 'تین منزل اور چھت'), ('چھت', 'کھلا ٹیرس'), ('دریا کا منظر', 'چھت سے')],
    'pa': [('ਪੂਰਾ ਘਰ', 'ਇੱਕ ਗਰੁੱਪ, ਸਾਰਾ ਘਰ'), ('3 ਬੈੱਡਰੂਮ', 'ਹਰੇਕ ਦਾ ਆਪਣਾ ਬਾਥ'), ('250+ m²', 'ਤਿੰਨ ਮੰਜ਼ਿਲ ਅਤੇ ਛੱਤ'), ('ਛੱਤ', 'ਖੁੱਲ੍ਹੀ ਟੈਰਸ'), ('ਦਰਿਆ ਦਾ ਨਜ਼ਾਰਾ', 'ਛੱਤ ਤੋਂ')],
}
GALLERY_H = {
    'en': 'The house in photos', 'de': 'Das Haus in Fotos', 'vi': 'Ảnh từng không gian trong nhà',
    'ja': '写真で見る一軒家', 'ko': '사진으로 보는 집', 'zh': '房屋照片', 'zh-tw': '房屋照片',
    'fr': 'La maison en photos', 'es': 'La casa en fotos', 'it': 'La casa in foto',
    'nl': 'Het huis in foto\'s', 'pt': 'A casa em fotos', 'pl': 'Dom na zdjęciach',
    'sv': 'Huset i bilder', 'ru': 'Дом на фотографиях', 'tr': 'Evin fotoğrafları',
    'id': 'Rumah dalam foto', 'ms': 'Rumah dalam foto', 'th': 'บ้านในรูปถ่าย',
    'hi': 'तस्वीरों में घर', 'ar': 'المنزل في صور', 'ur': 'تصویروں میں گھر', 'pa': 'ਤਸਵੀਰਾਂ ਵਿੱਚ ਘਰ',
}
REV_H = {
    'en': 'Google reviews', 'de': 'Google-Bewertungen', 'vi': 'Đánh giá Google',
    'ja': 'Googleのクチコミ', 'ko': 'Google 리뷰', 'zh': 'Google 评价', 'zh-tw': 'Google 評價',
    'fr': 'Avis Google', 'es': 'Reseñas de Google', 'it': 'Recensioni Google',
    'nl': 'Google-beoordelingen', 'pt': 'Avaliações no Google', 'pl': 'Opinie Google',
    'sv': 'Google-omdömen', 'ru': 'Отзывы Google', 'tr': 'Google yorumları',
    'id': 'Ulasan Google', 'ms': 'Ulasan Google', 'th': 'รีวิว Google',
    'hi': 'Google समीक्षाएँ', 'ar': 'مراجعات Google', 'ur': 'Google جائزے', 'pa': 'Google ਸਮੀਖਿਆਵਾਂ',
}
ARIA = {
    'en': ('Previous photo', 'Next photo', 'Close'),
    'de': ('Vorheriges Foto', 'Nächstes Foto', 'Schließen'),
    'vi': ('Ảnh trước', 'Ảnh sau', 'Đóng'),
    'ja': ('前の写真', '次の写真', '閉じる'),
    'ko': ('이전 사진', '다음 사진', '닫기'),
    'zh': ('上一张', '下一张', '关闭'),
    'zh-tw': ('上一張', '下一張', '關閉'),
    'fr': ('Photo précédente', 'Photo suivante', 'Fermer'),
    'es': ('Foto anterior', 'Foto siguiente', 'Cerrar'),
    'it': ('Foto precedente', 'Foto successiva', 'Chiudi'),
    'nl': ('Vorige foto', 'Volgende foto', 'Sluiten'),
    'pt': ('Foto anterior', 'Próxima foto', 'Fechar'),
    'pl': ('Poprzednie zdjęcie', 'Następne zdjęcie', 'Zamknij'),
    'sv': ('Föregående bild', 'Nästa bild', 'Stäng'),
    'ru': ('Предыдущее фото', 'Следующее фото', 'Закрыть'),
    'tr': ('Önceki fotoğraf', 'Sonraki fotoğraf', 'Kapat'),
    'id': ('Foto sebelumnya', 'Foto berikutnya', 'Tutup'),
    'ms': ('Foto sebelum', 'Foto seterusnya', 'Tutup'),
    'th': ('รูปก่อนหน้า', 'รูปถัดไป', 'ปิด'),
    'hi': ('पिछली तस्वीर', 'अगली तस्वीर', 'बंद करें'),
    'ar': ('الصورة السابقة', 'الصورة التالية', 'إغلاق'),
    'ur': ('پچھلی تصویر', 'اگلی تصویر', 'بند کریں'),
    'pa': ('ਪਿਛਲੀ ਤਸਵੀਰ', 'ਅਗਲੀ ਤਸਵੀਰ', 'ਬੰਦ ਕਰੋ'),
}
# Three Google reviews, each 5 of 5. Names and wording are the guest's.
# The third quote is Vietnamese on /vi/, German on /de/, and English on every other page.
REVIEWS = [
    {
        'name': 'Irsa Mazhar',
        'text': {'en': 'Excellent House, I love to visit it again. Amazing Place.'},
    },
    {
        'name': 'Azeem Jutt',
        'text': {'en': 'A Beautiful Place with an Amazing View! We had a wonderful stay at this beautiful holiday home. The house is lovely, clean, comfortable, and well maintained. The view is absolutely stunning, especially being able to see the water and enjoy the peaceful surroundings. It\'s the perfect place to relax, unwind, and enjoy a little getaway. Everything was great, and we would definitely recommend this place to anyone looking for a relaxing stay with beautiful views. We would love to come back again! ❤️'},
    },
    {
        'name': 'an nguyen',
        'text': {
            'vi': 'Căn nhà có sân thượng cho buổi tối trọn vẹn, các dịp lễ có thể xem pháo hoa, dùng bếp nướng rồi thư giãn cùng bạn bè. Dưới tầng có cả phòng chiếu phim kèm karaoke. Với đầy đủ mọi thứ như vậy còn gì tuyệt vời hơn. Có dịp chắc chắn sẽ quay lại với gia đình.',
            'de': 'Das Haus hat eine Dachterrasse, die perfekt für Abende ist, wo man Feuerwerk schauen, grillen und mit Freunden entspannen kann. Unten gibt es sogar ein Heimkino mit Karaoke. Mit allem, was man sich wünschen kann – was will man mehr? Wir kommen auf jeden Fall mit unserer Familie wieder!',
            'en': 'The house has a rooftop terrace that\'s perfect for evenings — on holidays you can watch the fireworks, use the BBQ and relax with friends. Downstairs there\'s even a home cinema with karaoke. With everything you could wish for, what more could you want? We\'ll definitely be back with our family!',
        },
    },
]
def review_quote(code, item):
    texts = item['text']
    if code in texts:
        return texts[code], code
    return texts['en'], 'en'

_HEAD = re.compile(
    r'(?i)(?:play\s*station(?:\s*5|\s*plus)?|\bps5\b|optoma|'
    r'karaok[eéê]\w*|노래방|가라오케|カラオケ|卡拉\s*OK|\bKTV\b|คาราโอเกะ|'
    r'كاريوكي|كاراوكي|کراؤکے|کراوکی|караоке|कराओके|ਕਰਾਓਕੇ|'
    r'\bnoraebang\b|\bgaming\b|ゲーミング|게임)'
)
_PHRASES = [
    (re.compile(r'(?i)karaoke-\s*und\s+'), ''),
    (re.compile(r'(?i)karaoke-raum'), 'Entertainment-Raum'),
    (re.compile(r'(?i)karaoke- en '), ''),
    (re.compile(r'(?i)karaoke- och '), ''),
    (re.compile(r'(?i)hát karaoke,?\s*'), ''),
    (re.compile(r'(?i)\b(?:with|mit|avec|con|met|och|en|y|e|et|und|and|và)\s+karaok\w*\s*'), ''),
    (re.compile(r'(?i)karaok\w*\s+(?:and|und|et|e|y|och|en|i|és)\s+'), ''),
    (re.compile(r'(?i)karaok\w*,\s*'), ''),
    (re.compile(r'노래방과\s*'), ''),
    (re.compile(r'노래방 있는\s*'), ''),
    (re.compile(r'노래방\s*'), ''),
    (re.compile(r'カラオケと'), ''),
    (re.compile(r'カラオケのある'), ''),
    (re.compile(r'カラオケ'), ''),
    (re.compile(r'卡拉OK和|卡拉OK与|卡拉OK＋|卡拉OK\+'), ''),
    (re.compile(r'卡拉OK'), ''),
    (re.compile(r'KTV[+＋]'), ''),
    (re.compile(r'(?i)\bgaming\b'), ''),
    (re.compile(r'(?i)optoma'), ''),
    (re.compile(r'(?i)\bps5\b'), ''),
    (re.compile(r'(?i)play\s*station(?:\s*5|\s*plus)?'), ''),
]


def _width(s):
    return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in s)


def _glen(s):
    return sum(1 for ch in s if unicodedata.category(ch) != 'Mn')


def too_long_title(lang, s):
    if lang in CJK:
        return _width(s) > 64
    if lang == 'th':
        return _glen(s) > 60
    return len(s) > 60


def too_long_desc(lang, s):
    if len(s) > 155:
        return True
    if lang in CJK and _width(s) > 160:
        return True
    if lang == 'th' and _glen(s) > 160:
        return True
    return False


def _tidy(s):
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.;:|])', r'\1', s)
    s = re.sub(r'\(\s*\)|（\s*）', '', s)
    s = re.sub(r'[:：]\s*\|', ' |', s)
    s = re.sub(r'\s+\|', ' |', s)
    s = re.sub(r'^\s*[,.:;|–—\-]+\s*', '', s)
    s = re.sub(r'\s*[,:]\s*\|', ' |', s)
    s = re.sub(r'(?i)\b(and|und|y|et|e|och|en|with|mit|và|와|과)\s*(\||$)', r'\2', s)
    s = re.sub(r'\s{2,}', ' ', s).strip(' -–—|')
    if s[:1].islower() and 'a' <= s[:1] <= 'z':
        s = s[0].upper() + s[1:]
    return s


def _broken(s):
    if not s or len(s) < 8:
        return True
    if re.search(r'[:：]\s*(\||$)', s):
        return True
    if re.search(r'\(\s*\)|（\s*）', s):
        return True
    if re.search(r'(?i)\b(and|und|y|et|with|mit|con|avec|e)\s*(\||$)', s):
        return True
    if re.search(r'\s{2,}', s):
        return True
    return False


def clean_headline(s):
    if not isinstance(s, str) or not _HEAD.search(s):
        return s
    for cre, rep in _PHRASES:
        s = cre.sub(rep, s)
    s = _HEAD.sub('', s)
    s = _tidy(s)
    return s


# Inflected forms the base phrase does not cover. Longest first.
CINEMA_EXTRA = {
    'de': [('4K-Projektors', '4K-Kinosystems (Optoma 4K-Projektor)')],
    'sv': [
        ('4K-projektorns', '4K-biosystemets (Optoma 4K-projektor)'),
        ('4K-projektorn', '4K-biosystemet (Optoma 4K-projektor)'),
    ],
}


def _phrase_sub(s, phrase, repl, guards):
    if not phrase or not s:
        return s
    pat = re.compile(r'(?<![\w])' + re.escape(phrase) + r'(?![\w])', re.IGNORECASE)
    def _repl(m):
        out = repl
        if m.group(0)[:1].isupper() and out[:1].islower():
            out = out[0].upper() + out[1:]
        guards.append(out)
        return f'\x00G{len(guards)-1}\x00'
    return pat.sub(_repl, s)


def _cinema_agree(s, lang):
    if lang == 'de':
        s = re.sub(r'\bden 4K-Kinosystem', 'das 4K-Kinosystem', s)
        s = re.sub(r'\beinen 4K-Kinosystem', 'ein 4K-Kinosystem', s)
        s = re.sub(r'\bDer 4K-Kinosystem', 'Das 4K-Kinosystem', s)
    elif lang == 'nl':
        s = re.sub(r'\bde 4K-bioscoopsysteem', 'het 4K-bioscoopsysteem', s)
        s = re.sub(r'\bDe 4K-bioscoopsysteem', 'Het 4K-bioscoopsysteem', s)
    elif lang == 'sv':
        s = re.sub(r'\ben 4K-biosystem\b', 'ett 4K-biosystem', s)
        s = re.sub(r'\bEn 4K-biosystem\b', 'Ett 4K-biosystem', s)
    return s


def label_cinema(s, lang):
    full = CINEMA.get(lang, CINEMA['en'])
    guards = []
    if full in s:
        s = _phrase_sub(s, full, full, guards)
    for phrase, repl in CINEMA_EXTRA.get(lang, []):
        s = _phrase_sub(s, phrase, repl, guards)
    for short in CINEMA_SHORT.get(lang, []):
        s = _phrase_sub(s, short, full, guards)
    for i, text in enumerate(guards):
        s = s.replace(f'\x00G{i}\x00', text)
    return _cinema_agree(s, lang)


def ps_name(s):
    if 'PS5' in s or 'PlayStation 5' in s:
        return s
    token = '\x00PP\x00'
    s = s.replace('PlayStation Plus', token)
    s = s.replace('PlayStation', 'PS5 (PlayStation 5)')
    return s.replace(token, 'PlayStation Plus')


def _body(s, lang, key):
    if not isinstance(s, str):
        return s
    n = s.replace('가라오케', '노래방')
    if key in ('title', 'h1'):
        return n
    n = ps_name(n)
    n = label_cinema(n, lang)
    if key == 'description' and too_long_desc(lang, n):
        return s.replace('가라오케', '노래방')
    return n


def _walk(o, lang, key=None):
    if isinstance(o, dict):
        return {k: _walk(v, lang, k) for k, v in o.items()}
    if isinstance(o, list):
        return [_walk(v, lang, key) for v in o]
    if isinstance(o, str):
        return _body(o, lang, key)
    return o


def gallery_keys():
    img = json.load(open(os.path.join(HERE, 'images.json'), encoding='utf-8'))
    pref = ['living', 'bed1', 'roof-day', 'river-city', 'kitchen', 'bath', 'ent', 'ent-cinema',
            'ent-karaoke', 'ent-tv', 'ent-led', 'ent-mics', 'ent-ps', 'bed2', 'bed3',
            'kitchen-dining', 'roof-bbq', 'roof-lounge', 'living-tv', 'entrance', 'stairs']
    seen, out = set(), []

    def add(k):
        if k not in img:
            return
        if k.startswith(('app-', 'tg-', 'logo')) or 'logo' in k:
            return
        stem = img[k].get('file') or k
        if stem in seen:
            return
        seen.add(stem)
        out.append(k)

    for k in pref:
        add(k)
    for k in img:
        add(k)
    return out


def _check_set(lang, pid, title, h1, desc):
    if too_long_title(lang, title):
        raise SystemExit(f'front title too long {lang}/{pid} {len(title)} {_width(title)}: {title}')
    if h1 and _HEAD.search(h1):
        raise SystemExit(f'front h1 still names gear {lang}/{pid}: {h1}')
    if _HEAD.search(title):
        raise SystemExit(f'front title still names gear {lang}/{pid}: {title}')
    if desc and too_long_desc(lang, desc):
        raise SystemExit(f'front desc too long {lang}/{pid} {len(desc)}: {desc}')


def prepare(C):
    for lang, pack in list(C.items()):
        if not isinstance(pack, dict) or 'pages' not in pack:
            continue
        pack['pages'] = _walk(pack['pages'], lang)
        for pid, page in pack['pages'].items():
            if not isinstance(page, dict):
                continue
            for key in ('title', 'h1'):
                if isinstance(page.get(key), str):
                    nxt = clean_headline(page[key])
                    if nxt and not _broken(nxt) and not _HEAD.search(nxt) and not (key == 'title' and too_long_title(lang, nxt)):
                        page[key] = nxt
            if pid == 'guide-ko-sing':
                page['title'] = '호치민 숙소에서 보내는 밤 | ASCON LIVING'
            if pid == 'room-entertainment' and lang in ENT:
                title, h1, desc = ENT[lang]
                page['title'], page['h1'], page['description'] = title, h1, desc
                _check_set(lang, pid, title, h1, desc)
                h2 = ENT_H2.get(lang, ENT_H2['en'])
                ul = [PS.get(lang, PS['en']), KARAOKE.get(lang, 'Karaoke'), GAMING.get(lang, 'Gaming'), CINEMA.get(lang, CINEMA['en']), 'Netflix']
                sections = page.setdefault('sections', [])
                if not any(s.get('h2') == h2 for s in sections if isinstance(s, dict)):
                    sections.insert(0, {'h2': h2, 'ul': ul})
        home = pack['pages'].get('home')
        if lang in HOME and isinstance(home, dict):
            home.update(HOME[lang])
            _check_set(lang, 'home', home['title'], home['h1'], home['description'])
        if lang == 'ko':
            # UI strings are outside pages; keep 노래방, never 가라오케.
            pack['ui'] = _walk(pack.get('ui', {}), lang)
    import landings
    landings.install(C)
    return C
