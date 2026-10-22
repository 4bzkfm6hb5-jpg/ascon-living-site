"""Keyword-first titles and length-safe meta descriptions.

Latin (and Thai, by character length where it fits): description 140–155 characters.
CJK: display width 140–160 and at most 155 characters (a 140-character CJK string
would exceed the width cap in tools/check_site.py).

Applied by build.py after content load, SEO overrides and extra guide pages.
Only the fields listed here are replaced. Other languages keep their titles and
get a factual length top-up when a description is under the floor.
"""
import re, unicodedata
CJK = {'ko', 'ja', 'zh', 'zh-tw'}

def width(s):
    return sum(2 if unicodedata.east_asian_width(ch) in 'WF' else 1 for ch in s)

def glen(s):
    return sum(1 for ch in s if unicodedata.category(ch) != 'Mn')

def meas(code, s):
    if code in CJK:
        return width(s)
    if code == 'th':
        return glen(s)
    return len(s)

def in_range(code, s):
    if '!' in s or len(s) > 155:
        return False
    m = meas(code, s)
    if code in CJK:
        return 140 <= m <= 160
    if code == 'th':
        # Combining marks make glen lag behind len; never exceed either cap.
        return m <= 160 and len(s) <= 155 and (m >= 140 or len(s) >= 140)
    return 140 <= len(s) <= 155

# Second sentence: whole house, 3 bedrooms, private bathroom in each. Longest first.
BENEFIT = {
 'en': [
    'The whole house has 3 bedrooms, each with a private bathroom.',
    'It is a whole house with 3 bedrooms, each with a private bathroom.',
    'The 3 bedrooms each have a private bathroom.',
    '3 bedrooms, each with a private bathroom.',
 ],
 'de': [
    'Das ganze Haus hat 3 Schlafzimmer, und jedes hat ein eigenes Bad.',
    'Das ganze Haus hat 3 Schlafzimmer mit jeweils eigenem Bad.',
    'Ganzes Haus: 3 Schlafzimmer mit jeweils eigenem Bad.',
    '3 Schlafzimmer, jedes mit eigenem Bad.',
 ],
 'vi': [
    'Nhà nguyên căn có 3 phòng ngủ, mỗi phòng một phòng tắm riêng.',
    'Cả nhà có 3 phòng ngủ, mỗi phòng có phòng tắm riêng.',
 ],
 'zh': [
    '整栋房子只租给一组客人，里面有3间卧室，而且每间卧室都带独立卫浴。',
    '整栋只给一组客人住，有3间卧室，每间都带独立卫浴。',
    '整栋房子有3间卧室，每间都带独立卫浴。',
    '3间卧室，每间独立卫浴。',
 ],
 'zh-tw': [
    '整棟房子只租給一組客人居住，裡面有3間臥室，而且每間臥室都帶獨立衛浴，不與別人共用。',
    '整棟房子只租給一組客人，裡面有3間臥室，而且每間臥室都帶獨立衛浴。',
    '整棟只給一組客人住，有3間臥室，每間都有獨立衛浴。',
    '整棟房子有3間臥室，每間都有獨立衛浴。',
    '3間臥室，每間獨立衛浴。',
 ],
 'hi': [
    'पूरा घर आपके लिए है: 3 बेडरूम, हर एक का अपना बाथरूम।',
    '3 बेडरूम हैं और हर बेडरूम का अपना बाथरूम है।',
    'पूरा घर: 3 बेडरूम, निजी बाथरूम।',
    '3 बेडरूम और अपना बाथरूम।',
    '3 बेडरूम, अपना बाथरूम।',
 ],
 'es': [
    'La casa entera tiene 3 dormitorios, cada uno con baño privado.',
    'Casa entera: 3 dormitorios, cada uno con baño privado.',
 ],
 'ar': [
    'البيت كامل لمجموعة واحدة: 3 غرف نوم، ولكل غرفة حمامها الخاص.',
    'البيت كامل: 3 غرف نوم، ولكل غرفة حمامها الخاص.',
    '3 غرف نوم ولكل منها حمام خاص.',
    '3 غرف، لكل منها حمام خاص.',
 ],
 'fr': [
    'La maison entière a 3 chambres, chacune avec salle de bain privée.',
    'Maison entière : 3 chambres, chacune avec salle de bain privée.',
 ],
 'pt': [
    'A casa inteira tem 3 quartos, cada um com banheiro privativo.',
    'Casa inteira: 3 quartos, cada um com banheiro privativo.',
    '3 quartos, cada um com banheiro.',
 ],
 'ru': [
    'Весь дом ваш: 3 спальни, у каждой своя ванная комната.',
    '3 спальни, у каждой своя ванная, во всём доме.',
 ],
 'ur': [
    'پورا گھر آپ کا ہے: 3 خواب گاہیں، ہر ایک کا اپنا غسل خانہ۔',
    '3 خواب گاہیں ہیں اور ہر ایک کا اپنا غسل خانہ ہے۔',
 ],
 'id': [
    'Rumah utuh untuk Anda: 3 kamar tidur, masing-masing dengan kamar mandi sendiri.',
    '3 kamar tidur, masing-masing dengan kamar mandi sendiri.',
 ],
 'ko': [
    '오직 예약한 소규모 일행만 집 전체를 쓰며, 침실 3개에 각각 전용 욕실이 있습니다.',
    '예약한 일행만 집 전체를 쓰며 침실 3개에 각각 전용 욕실이 있습니다.',
    '집 전체를 쓰며 침실 3개에 각각 전용 욕실이 있습니다.',
    '침실 3개에 각각 전용 욕실이 있습니다.',
 ],
 'ja': [
    'ご予約の一組だけで一軒家を使い、寝室3室はそれぞれ専用バスルームです。',
    '一軒家を貸し切り、寝室3室はそれぞれ専用バスルームです。',
    '寝室3室はそれぞれ専用バスルームです。',
 ],
 'pa': [
    'ਪੂਰਾ ਘਰ ਤੁਹਾਡਾ ਹੈ: 3 ਬੈੱਡਰੂਮ, ਹਰੇਕ ਦਾ ਆਪਣਾ ਬਾਥਰੂਮ।',
    '3 ਬੈੱਡਰੂਮ ਹਨ ਅਤੇ ਹਰੇਕ ਦਾ ਆਪਣਾ ਬਾਥਰੂਮ ਹੈ।',
 ],
 'th': [
    'บ้านทั้งหลังมี 3 ห้องนอน แต่ละห้องมีห้องน้ำในตัว สำหรับหนึ่งกลุ่ม',
    'บ้านทั้งหลังมี 3 ห้องนอน แต่ละห้องมีห้องน้ำในตัว',
    'สำหรับกลุ่มเดียว',
    '3 ห้องนอน ห้องน้ำในตัว',
 ],
 'ms': [
    'Rumah penuh untuk anda: 3 bilik tidur, setiap satu dengan bilik air sendiri.',
    '3 bilik tidur, setiap satu dengan bilik air sendiri.',
 ],
 'it': [
    'La casa intera ha 3 camere, ognuna con bagno privato.',
    'Casa intera: 3 camere, ognuna con bagno privato.',
 ],
 'nl': [
    'Het hele huis is voor jullie: 3 slaapkamers, elk met een eigen badkamer.',
    '3 slaapkamers, elk met een eigen badkamer, in het hele huis.',
 ],
 'tr': [
    'Evin tamamı sizin: 3 yatak odası, her birinin özel banyosu var.',
    '3 yatak odası var ve her birinin özel banyosu var.',
    '3 oda, her birinin banyosu var.',
 ],
 'pl': [
    'Cały dom jest wasz: 3 sypialnie, każda z własną łazienką.',
    '3 sypialnie, każda z własną łazienką, w całym domu.',
 ],
 'sv': [
    'Hela huset är ert: 3 sovrum, vart och ett med eget badrum.',
    '3 sovrum, vart och ett med eget badrum, i hela huset.',
    'Hela huset: 3 sovrum, eget badrum.',
    '3 sovrum med eget badrum.',
 ],
}

# (title, meta head). Head is one sentence without the bedroom benefit.
# Brand stays last. Core keyword is the first words.
PRIORITY = {
 'en': {
  'home': ('Holiday House Ho Chi Minh City | ASCON LIVING',
           'Holiday house in Ho Chi Minh City: a homestay in Saigon where you rent the whole house.'),
  'booking': ('Whole House Rental Saigon: Book | ASCON LIVING',
              'Whole house rental in Saigon: book on Airbnb or Trip.com, or inquire on WhatsApp or Zalo.'),
  'house': ('Homestay Saigon: The Whole House | ASCON LIVING',
            'Homestay in Saigon: three floors, a rooftop and over 250 square metres, room by room.'),
  'families': ('Holiday House Ho Chi Minh City: Family | ASCON',
               'Holiday house in Ho Chi Minh City for a family homestay in Saigon, with a kitchen and a quiet bedroom.'),
  'groups': ('Whole House Rental Saigon for Groups | ASCON',
             'Whole house rental in Saigon for a small group: karaoke, a rooftop BBQ and separate bedrooms.'),
  'location': ('Homestay Saigon: Riverside Address | ASCON',
               'Homestay in Saigon at 389A Đường Trần Xuân Soạn, Tân Hưng, Ho Chi Minh City, by the river bank.'),
  'faq': ('Holiday House Ho Chi Minh City: FAQ | ASCON',
          'Holiday house in Ho Chi Minh City: answers on check-in, the kitchen, Wi-Fi and airport transfer.'),
  'rules': ('Homestay Saigon House Rules | ASCON LIVING',
            'Homestay in Saigon: house rules for the whole house, including quiet hours and self check-in.'),
  'guide': ('Whole House Rental Saigon Travel Guide | ASCON',
            'Whole house rental in Saigon: a Ho Chi Minh City travel guide, the free app, families and the airport.'),
  'guide-family': ('Holiday House Ho Chi Minh City: Kids | ASCON',
                   'Holiday house in Ho Chi Minh City with children: heat, street crossings, Grab and days in Saigon.'),
  'guide-airport': ('Homestay Saigon Airport Transfer | ASCON LIVING',
                    'Homestay in Saigon: airport transfer from Tân Sơn Nhất on request, or a ride-hailing car or taxi.'),
  'guide-app': ('Whole House Rental Saigon Guide App | ASCON',
                'Whole house rental in Saigon: the free guide app with places, a map and practical notes. Nothing to install.'),
  'travel-guide': ('Holiday House Ho Chi Minh City App | ASCON',
                   'Holiday house in Ho Chi Minh City: open the free Saigon guide app in your phone browser.'),
  'rooftop': ('Homestay Saigon Rooftop and River | ASCON',
              'Homestay in Saigon: a rooftop of about 56–60 m² with BBQ, seating and a river view to the skyline.'),
  'room-entertainment': ('Whole House Rental Saigon: Karaoke | ASCON',
                         'Whole house rental in Saigon: a private karaoke room with a 4K projector and a large 4K TV.'),
  'room-living': ('Holiday House Ho Chi Minh City: Living | ASCON',
                  'Holiday house in Ho Chi Minh City: a living room of about 40 m² with an L-shaped sofa and a 75-inch 4K TV.'),
  'room-kitchen': ('Homestay Saigon Kitchen and Dining | ASCON',
                   'Homestay in Saigon: a kitchen with stove, oven, rice cooker and a fridge of about 540 litres.'),
  'room-master': ('Whole House Rental Saigon: Master Room | ASCON',
                  'Whole house rental in Saigon: the master bedroom is about 55 m², with a 180×200 cm bed and a balcony.'),
  'room-bedroom-2': ('Holiday House Ho Chi Minh City: Room 2 | ASCON',
                     'Holiday house in Ho Chi Minh City: bedroom 2 has a 160×200 cm bed, a window and air conditioning.'),
  'room-bedroom-3': ('Homestay Saigon Quiet Bedroom 3 | ASCON LIVING',
                     'Homestay in Saigon: bedroom 3 has no window, so it stays dark and quiet, with a 160×200 cm bed.'),
  'room-bathrooms': ('Whole House Rental Saigon: Bathrooms | ASCON',
                     'Whole house rental in Saigon: a private bathroom for every bedroom, plus a guest WC.'),
  'room-hallway': ('Holiday House Ho Chi Minh City: Desk | ASCON',
                   'Holiday house in Ho Chi Minh City: a work area with a desk, a mesh chair and Wi-Fi up to 1 Gbit/s.'),
  'room-outside': ('Homestay Saigon Terraces by the River | ASCON',
                   'Homestay in Saigon: terraces with white railings look across the river to the city skyline.'),
  'imprint': ('Whole House Rental Saigon: Imprint | ASCON',
              'Whole house rental in Saigon: operator CONG TY TNHH ASCON LIVING VIET NAM, registration 0319549605.'),
  'privacy': ('Holiday House Ho Chi Minh City: Privacy | ASCON',
              'Holiday house in Ho Chi Minh City: this website uses no cookies and no analytics, and is hosted on GitHub Pages.'),
  'guide-rain': ('Homestay Saigon on a Rainy Day | ASCON LIVING',
                 'Homestay in Saigon on a rainy day: indoor time at the house, Ben Thanh Market and cafés.'),
  'guide-day': ('Holiday House Ho Chi Minh City: One Day | ASCON',
                'Holiday house in Ho Chi Minh City: one loose day in Saigon, with a market, a park and a meal.'),
  'guide-party': ('Whole House Rental Saigon: Family Trip | ASCON',
                  'Whole house rental in Saigon for a family or a small group, with separate bedrooms and a kitchen.'),
  'guide-food': ('Homestay Saigon Street Food Guide | ASCON',
                 'Homestay in Saigon: street food such as phở and bánh mì, Ben Thanh Market, and the house kitchen.'),
 },
 'de': {
  'home': ('Ferienhaus Ho-Chi-Minh-Stadt | ASCON LIVING',
           'Ferienhaus in Ho-Chi-Minh-Stadt: eine Unterkunft in Saigon, bei der ihr das ganze Haus mietet.'),
  'booking': ('Ferienhaus Saigon buchen | ASCON LIVING',
              'Ferienhaus in Saigon buchen: über Airbnb oder Trip.com, oder per WhatsApp oder Zalo anfragen.'),
  'house': ('Ferienhaus Ho-Chi-Minh-Stadt: Räume | ASCON',
            'Ferienhaus in Ho-Chi-Minh-Stadt: drei Etagen, Dachterrasse und über 250 Quadratmeter, Raum für Raum.'),
  'families': ('Ferienhaus Saigon für die Familie | ASCON',
               'Ferienhaus in Saigon für die Familie: Küche, Waschmaschine und ein dunkles Zimmer für den Mittagsschlaf.'),
  'groups': ('Unterkunft Saigon für Gruppen | ASCON LIVING',
             'Unterkunft in Saigon für eine kleine Gruppe: Karaoke, Grill auf dem Dach und getrennte Schlafzimmer.'),
  'location': ('Ferienhaus Ho-Chi-Minh-Stadt: Lage | ASCON',
               'Ferienhaus in Ho-Chi-Minh-Stadt: 389A Đường Trần Xuân Soạn, Tân Hưng, am Fluss.'),
  'faq': ('Unterkunft Saigon: häufige Fragen | ASCON',
          'Unterkunft in Saigon: Antworten zu Check-in, Küche, WLAN und Flughafentransfer.'),
  'rules': ('Ferienhaus Saigon: Hausregeln | ASCON LIVING',
            'Ferienhaus in Saigon: Hausregeln für das ganze Haus, unter anderem Ruhezeiten und Self-Check-in.'),
  'guide': ('Ferienhaus Ho-Chi-Minh-Stadt: Guide | ASCON',
            'Ferienhaus in Ho-Chi-Minh-Stadt: Reiseführer, kostenlose App, Familien und der Weg vom Flughafen.'),
  'guide-family': ('Ferienhaus Saigon mit Kindern | ASCON LIVING',
                   'Ferienhaus in Saigon mit Kindern: Hitze, Straßen, Grab und ein Tag in Ho-Chi-Minh-Stadt.'),
  'guide-airport': ('Unterkunft Saigon: Flughafen | ASCON LIVING',
                    'Unterkunft in Saigon: Flughafentransfer ab Tân Sơn Nhất auf Anfrage, Fahrdienst oder Taxi.'),
  'guide-app': ('Ferienhaus Saigon: Guide-App | ASCON LIVING',
                'Ferienhaus in Saigon: die kostenlose Guide-App mit Orten, Karte und Hinweisen. Nichts zu installieren.'),
  'travel-guide': ('Unterkunft Saigon: Reiseführer-App | ASCON',
                   'Unterkunft in Saigon: die kostenlose Reiseführer-App für Ho-Chi-Minh-Stadt im Handy-Browser.'),
  'rooftop': ('Ferienhaus Ho-Chi-Minh-Stadt: Dach | ASCON',
              'Ferienhaus in Ho-Chi-Minh-Stadt: etwa 56–60 m² Dach mit Grill, Sitzplätzen und Blick über den Fluss.'),
  'room-entertainment': ('Ferienhaus Saigon: Karaoke-Raum | ASCON',
                         'Ferienhaus in Saigon: privater Karaoke-Raum mit 4K-Projektor und großem 4K-Fernseher.'),
  'room-living': ('Unterkunft Saigon: Wohnzimmer | ASCON LIVING',
                  'Unterkunft in Saigon: Wohnzimmer von etwa 40 m² mit L-Sofa und 75-Zoll-4K-Fernseher.'),
  'room-kitchen': ('Ferienhaus Saigon: Küche | ASCON LIVING',
                   'Ferienhaus in Saigon: Küche mit Herd, Ofen, Reiskocher und Kühlschrank von etwa 540 Litern.'),
  'room-master': ('Ferienhaus Ho-Chi-Minh-Stadt: Schlafen | ASCON',
                  'Ferienhaus in Ho-Chi-Minh-Stadt: Schlafzimmer von etwa 55 m² mit Bett 180×200 cm und Balkon.'),
  'room-bedroom-2': ('Unterkunft Saigon: Schlafzimmer 2 | ASCON',
                     'Unterkunft in Saigon: Schlafzimmer 2 mit Bett 160×200 cm, Fenster und Klimaanlage.'),
  'room-bedroom-3': ('Ferienhaus Saigon: Schlafzimmer 3 | ASCON',
                     'Ferienhaus in Saigon: Schlafzimmer 3 ohne Fenster, dunkel und ruhig, mit Bett 160×200 cm.'),
  'room-bathrooms': ('Ferienhaus Saigon: eigene Bäder | ASCON',
                     'Ferienhaus in Saigon: ein eigenes Bad zu jedem Schlafzimmer, dazu ein Gäste-WC.'),
  'room-hallway': ('Unterkunft Saigon: Arbeitsplatz | ASCON',
                   'Unterkunft in Saigon: Arbeitsplatz mit Schreibtisch, Netzstuhl und WLAN bis 1 Gbit/s.'),
  'room-outside': ('Ferienhaus Ho-Chi-Minh-Stadt am Fluss | ASCON',
                   'Ferienhaus in Ho-Chi-Minh-Stadt: Terrassen mit weißem Geländer und Blick über den Fluss auf die Skyline.'),
  'imprint': ('Ferienhaus Saigon: Impressum | ASCON LIVING',
              'Ferienhaus in Saigon: Betreiber CONG TY TNHH ASCON LIVING VIET NAM, Registernummer 0319549605.'),
  'privacy': ('Unterkunft Saigon: Datenschutz | ASCON LIVING',
              'Unterkunft in Saigon: diese Website nutzt keine Cookies und keine Analyse und liegt auf GitHub Pages.'),
  'guide-rain': ('Ferienhaus Saigon bei Regen | ASCON LIVING',
                 'Ferienhaus in Saigon an einem Regentag: drinnen im Haus, Ben-Thanh-Markt und Cafés.'),
  'guide-day': ('Ferienhaus Saigon: ein Tag Stadt | ASCON',
                'Ferienhaus in Saigon: ein lockerer Tag in Ho-Chi-Minh-Stadt mit Markt, Park und einer Mahlzeit.'),
  'guide-party': ('Unterkunft Saigon für Familie & Gruppe | ASCON',
                  'Unterkunft in Saigon für Familie oder eine kleine Gruppe: getrennte Schlafzimmer und eine Küche.'),
  'guide-food': ('Ferienhaus Saigon: Streetfood | ASCON LIVING',
                 'Ferienhaus in Saigon: Streetfood wie Phở und Bánh mì, der Ben-Thanh-Markt und die Küche im Haus.'),
 },
 'ko': {
  'home': ('호치민 홈스테이 독채 숙소 | ASCON LIVING',
           '호치민 홈스테이는 사이공에서 집 한 채를 통째로 쓰는 독채 숙소입니다.'),
  'booking': ('호치민 독채 숙소 예약 | ASCON LIVING',
              '호치민 독채 숙소는 Airbnb, Trip.com에서 예약하거나 WhatsApp, Zalo, 카카오톡으로 문의합니다.'),
  'house': ('사이공 숙소 집 안내 | ASCON LIVING',
            '사이공 숙소는 3층과 루프탑, 250㎡가 넘는 집을 방마다 사진으로 안내합니다.'),
  'families': ('호치민 홈스테이 가족 여행 | ASCON LIVING',
               '호치민 홈스테이는 가족 여행에 맞습니다. 주방과 세탁기가 있고, 창 없는 침실은 낮잠에 조용합니다.'),
  'groups': ('호치민 독채 숙소 단체 | ASCON LIVING',
             '호치민 독채 숙소는 소규모 일행을 위한 집입니다. 노래방과 루프탑 바비큐, 나뉜 침실이 있습니다.'),
  'location': ('사이공 숙소 위치 강변 | ASCON LIVING',
               '사이공 숙소 위치는 389A Đường Trần Xuân Soạn, Tân Hưng, 강변입니다.'),
  'faq': ('호치민 홈스테이 자주 묻는 질문 | ASCON LIVING',
          '호치민 홈스테이의 체크인, 주방, 와이파이, 공항 픽업에 대한 답변입니다.'),
  'rules': ('호치민 독채 숙소 이용 안내 | ASCON LIVING',
            '호치민 독채 숙소의 이용 안내입니다. 셀프 체크인, 대문 열쇠, 밤 시간 소음 약속이 있습니다.'),
  'guide': ('사이공 숙소 여행 가이드 | ASCON LIVING',
            '사이공 숙소에서 쓰는 호치민 여행 가이드와 무료 앱, 가족 일정, 공항 이동을 모았습니다.'),
  'travel-guide': ('호치민 홈스테이 가이드 앱 | ASCON LIVING',
                   '호치민 홈스테이 손님을 위한 무료 가이드 앱입니다. 휴대폰 브라우저에서 바로 열립니다.'),
  'rooftop': ('호치민 독채 숙소 루프탑 | ASCON LIVING',
              '호치민 독채 숙소의 루프탑은 약 56–60㎡입니다. 바비큐와 좌석이 있고 강 건너 스카이라인이 보입니다.'),
  'room-entertainment': ('사이공 숙소 노래방 | ASCON LIVING',
                         '사이공 숙소의 노래방에는 마이크, 4K 프로젝터와 스크린, 대형 4K TV가 있습니다.'),
  'room-living': ('호치민 홈스테이 거실 | ASCON LIVING',
                  '호치민 홈스테이의 거실은 약 40㎡입니다. L자 소파와 75인치 4K TV가 있습니다.'),
  'room-kitchen': ('호치민 독채 숙소 주방 | ASCON LIVING',
                   '호치민 독채 숙소의 주방에는 레인지, 오븐, 밥솥, 약 540L 냉장고와 식탁이 있습니다.'),
  'room-master': ('사이공 숙소 마스터 침실 | ASCON LIVING',
                  '사이공 숙소의 마스터 침실은 약 55㎡입니다. 180×200cm 침대와 발코니가 있습니다.'),
  'room-bedroom-2': ('호치민 홈스테이 침실 2 | ASCON LIVING',
                     '호치민 홈스테이의 침실 2에는 160×200cm 침대, 창문, 에어컨이 있습니다.'),
  'room-bedroom-3': ('호치민 독채 숙소 침실 3 | ASCON LIVING',
                     '호치민 독채 숙소의 침실 3은 창문이 없어 낮에도 어둡고 조용합니다. 160×200cm 침대가 있습니다.'),
  'room-bathrooms': ('사이공 숙소 전용 욕실 | ASCON LIVING',
                     '사이공 숙소는 침실마다 전용 욕실이 있고, 거실에 게스트 화장실이 하나 더 있습니다.'),
  'room-hallway': ('호치민 홈스테이 작업 공간 | ASCON LIVING',
                   '호치민 홈스테이의 작업 공간에는 책상과 메시 의자가 있고, 와이파이는 최대 1Gbit/s입니다.'),
  'room-outside': ('호치민 독채 숙소 강변 | ASCON LIVING',
                   '호치민 독채 숙소는 강변에 있습니다. 흰 난간 테라스에서 강과 도시 스카이라인이 보입니다.'),
  'guide-rain': ('사이공 숙소 비 오는 날 | ASCON LIVING',
                 '사이공 숙소에서 비 오는 날을 보내는 방법입니다. 집 안, 벤탄 시장, 카페를 이용합니다.'),
  'guide-day': ('호치민 홈스테이 하루 일정 | ASCON LIVING',
                '호치민 홈스테이에서 사이공 하루를 느슨하게 보내는 안내입니다. 시장, 공원, 식사를 담았습니다.'),
  'guide-party': ('호치민 독채 숙소 가족 모임 | ASCON LIVING',
                  '호치민 독채 숙소는 가족이나 소규모 모임이 침실을 나누고 주방을 함께 씁니다.'),
  'guide-food': ('사이공 숙소 길거리 음식 | ASCON LIVING',
                 '사이공 숙소 근처의 길거리 음식과 반미, 쌀국수, 벤탄 시장, 집 주방을 안내합니다.'),
 },
 'ja': {
  'home': ('ホーチミン 一軒家の貸切 | ASCON LIVING',
           'ホーチミンの一軒家を、サイゴンのホームステイとして一組だけで使います。'),
  'booking': ('ホーチミン 貸別荘の予約 | ASCON LIVING',
              'ホーチミンの貸別荘はAirbnbかTrip.comで予約するか、WhatsAppかZaloで問い合わせます。'),
  'house': ('サイゴン ホームステイの部屋案内 | ASCON LIVING',
            'サイゴンのホームステイは3階とルーフトップ、250㎡超の一軒家を部屋ごとに案内します。'),
  'families': ('ホーチミン 一軒家で家族旅行 | ASCON LIVING',
               'ホーチミンの一軒家は家族旅行向きです。キッチンと洗濯機があり、窓のない寝室はお昼寝に静かです。'),
  'groups': ('ホーチミン 貸別荘を少人数で | ASCON LIVING',
             'ホーチミンの貸別荘は少人数の一組向けです。カラオケ、屋上のBBQ、分かれた寝室があります。'),
  'location': ('サイゴン ホームステイの場所 | ASCON LIVING',
               'サイゴンのホームステイの住所は389A Đường Trần Xuân Soạn, Tân Hưng、川沿いです。'),
  'faq': ('ホーチミン 一軒家のよくある質問 | ASCON LIVING',
          'ホーチミンの一軒家について、チェックイン、キッチン、Wi-Fi、空港送迎の答えです。'),
  'rules': ('ホーチミン 貸別荘のハウスルール | ASCON LIVING',
            'ホーチミンの貸別荘のハウスルールです。セルフチェックイン、外門の鍵、夜間の音の約束があります。'),
  'guide': ('サイゴン ホームステイの旅行ガイド | ASCON LIVING',
            'サイゴンのホームステイから使うホーチミン旅行ガイド、無料アプリ、家族の一日、空港からの移動です。'),
  'travel-guide': ('ホーチミン 一軒家のガイドアプリ | ASCON LIVING',
                   'ホーチミンの一軒家に滞在する方向けの無料ガイドアプリです。スマホのブラウザで開きます。'),
  'rooftop': ('ホーチミン 貸別荘のルーフトップ | ASCON LIVING',
              'ホーチミンの貸別荘のルーフトップは約56〜60㎡です。BBQと席があり、川の向こうの街が見えます。'),
  'room-entertainment': ('サイゴン ホームステイのカラオケ | ASCON LIVING',
                         'サイゴンのホームステイのカラオケ室にはマイク、4Kプロジェクターとスクリーン、大型4Kテレビがあります。'),
  'room-living': ('ホーチミン 一軒家のリビング | ASCON LIVING',
                  'ホーチミンの一軒家のリビングは約40㎡です。L字ソファと75インチ4Kテレビがあります。'),
  'room-kitchen': ('ホーチミン 貸別荘のキッチン | ASCON LIVING',
                   'ホーチミンの貸別荘のキッチンにはコンロ、オーブン、炊飯器、約540Lの冷蔵庫と食卓があります。'),
  'room-master': ('サイゴン ホームステイの主寝室 | ASCON LIVING',
                  'サイゴンのホームステイの主寝室は約55㎡です。180×200cmのベッドとバルコニーがあります。'),
  'room-bedroom-2': ('ホーチミン 一軒家の寝室2 | ASCON LIVING',
                     'ホーチミンの一軒家の寝室2には160×200cmのベッド、窓、エアコンがあります。'),
  'room-bedroom-3': ('ホーチミン 貸別荘の寝室3 | ASCON LIVING',
                     'ホーチミンの貸別荘の寝室3は窓がなく、日中も暗く静かです。160×200cmのベッドがあります。'),
  'room-bathrooms': ('サイゴン ホームステイの専用浴室 | ASCON LIVING',
                     'サイゴンのホームステイは各寝室に専用バスルームがあり、リビングにゲスト用トイレがもう一つあります。'),
  'room-hallway': ('ホーチミン 一軒家の作業スペース | ASCON LIVING',
                   'ホーチミンの一軒家の作業スペースにはデスクとメッシュチェアがあり、Wi-Fiは最大1Gbit/sです。'),
  'room-outside': ('ホーチミン 貸別荘の川沿い | ASCON LIVING',
                   'ホーチミンの貸別荘は川沿いにあります。白い手すりのテラスから川と街のスカイラインが見えます。'),
  'guide-rain': ('サイゴン ホームステイの雨の日 | ASCON LIVING',
                 'サイゴンのホームステイで雨の日を過ごす案内です。家の中、ベンタン市場、カフェを使います。'),
  'guide-day': ('ホーチミン 一軒家の一日 | ASCON LIVING',
                'ホーチミンの一軒家を拠点に、サイゴンを一日ゆるく回る案内です。市場、公園、食事を入れています。'),
  'guide-party': ('ホーチミン 貸別荘で家族と仲間 | ASCON LIVING',
                  'ホーチミンの貸別荘は、家族や少人数の仲間が寝室を分け、キッチンを一緒に使います。'),
  'guide-food': ('サイゴン ホームステイの屋台ごはん | ASCON LIVING',
                 'サイゴンのホームステイ周辺の屋台ごはん、バインミー、フォー、ベンタン市場、家のキッチンを案内します。'),
 },
}

# Titles must start with one of these (case-sensitive for CJK, casefold for Latin).
LEAD = {
 'en': ('Holiday House Ho Chi Minh City', 'Whole House Rental Saigon', 'Homestay Saigon'),
 'de': ('Ferienhaus Ho-Chi-Minh-Stadt', 'Ferienhaus Saigon', 'Unterkunft Saigon'),
 'ko': ('호치민 홈스테이', '호치민 독채 숙소', '사이공 숙소'),
 'ja': ('ホーチミン 一軒家', 'ホーチミン 貸別荘', 'サイゴン ホームステイ'),
}

_BANNED = re.compile(r'(?i)play ?station|hisense|optoma|\bpool\b|parking|halal|villa|빌라|ヴィラ|プール|수영장|주차|停车|游泳池|district\s*\d|7군|7区|第七郡|quận\s*\d')

def _join(code, head, benefit):
    head = head.strip()
    benefit = benefit.strip()
    return head + ' ' + benefit

def choose(code, head, benefits):
    head = head.strip()
    opts = []
    for b in benefits:
        opts.append(_join(code, head, b))
    # Head alone if it already carries the benefit and fits.
    opts.append(head)
    good = [s for s in opts if in_range(code, s) and not _BANNED.search(s)]
    if not good:
        return None
    # Prefer a candidate that actually contains the benefit sentence.
    with_b = [s for s in good if s != head]
    return (with_b or good)[0]

def debrand(s):
    s = re.sub(r'(?i)\s*,?\s*PlayStation(?:\s*(?:with|과|と|和|及)\s*PlayStation Plus|\s*Plus|\s*（PlayStation Plus）|\s*\(PlayStation Plus\))?', '', s)
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.replace(' ,', ',').replace(' .', '.').replace('、、', '、').replace('，，', '，')
    return s.strip()

def strip_ps(s):
    # Drop the console name from descriptions we have to rewrite for length.
    s = re.sub(r'(?i)و?\s*PlayStation\s+مع\s+PlayStation\s*Plus', '', s)
    s = re.sub(r'(?i)PlayStation\s*Plus\s*के साथ\s*PlayStation', '', s)
    s = re.sub(r'(?i)PlayStation\s+med\s+PlayStation\s*Plus', '', s)
    s = re.sub(r'(?i)PlayStation\s*(?:与|和|과|와|と|with|và|및)\s*PlayStation\s*Plus', '', s)
    s = re.sub(r'(?i)PlayStation\s*Plus', '', s)
    s = re.sub(r'(?i)PlayStation', '', s)
    s = re.sub(r'附\s*的\s*與', '', s)
    s = re.sub(r',\s*med\s+och', ',', s)
    s = re.sub(r'和\s*[，,]', '，', s)
    s = re.sub(r'[、,，]{2,}', '、', s)
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.replace(' ,', ',').replace(' .', '.').replace('、、', '、').replace(', और', ' और').replace(', och ', ' och ')
    return s.strip(' 、,，')

def clean_title(title):
    t = re.sub(r'(?i)\s*(?:och|and|en|et|e|и|ve|und|és|with|與|和|와|과|と|و)\s*PlayStation', '', title)
    t = re.sub(r'(?i)PlayStation', '', t)
    t = re.sub(r'\s{2,}', ' ', t).strip()
    return t

def fit_existing(code, desc):
    """Lengthen a short description. Keep the existing sentence."""
    if in_range(code, desc) and not _BANNED.search(desc):
        return desc
    if _BANNED.search(desc):
        desc = strip_ps(desc)
    if in_range(code, desc) and not _BANNED.search(desc):
        return desc
    benefits = BENEFIT.get(code) or BENEFIT['en']
    # Drop a duplicated benefit if we are about to add one.
    chosen = choose(code, desc.rstrip('.').rstrip('。') + ('.' if code not in CJK else '。'), benefits)
    if chosen:
        return chosen
    # Trim the existing sentence from the end, then add the shortest benefit.
    words = desc.split()
    short = benefits[-1]
    for n in range(len(words), 4, -1):
        base = ' '.join(words[:n]).rstrip(' ,;:，、')
        if code in CJK:
            if not base.endswith('。'):
                base = base.rstrip('.') + '。'
        elif not base.endswith('.'):
            base += '.'
        s = _join(code, base, short)
        if in_range(code, s) and not _BANNED.search(s):
            return s
    return desc

def apply(C):
    problems = []
    for lang, pages in PRIORITY.items():
        if lang not in C:
            continue
        benefits = BENEFIT[lang]
        leads = LEAD[lang]
        for pid, (title, head) in pages.items():
            if pid not in C[lang]['pages']:
                continue
            if not title.endswith('ASCON LIVING') and not title.endswith('| ASCON'):
                problems.append(f'{lang}/{pid} brand not last: {title}')
            if not any(title.startswith(x) for x in leads):
                problems.append(f'{lang}/{pid} keyword not first: {title}')
            limit = 64 if lang in CJK else 60
            got = width(title) if lang in CJK else len(title)
            if got > limit:
                problems.append(f'{lang}/{pid} title {got}>{limit}: {title}')
            desc = choose(lang, head, benefits)
            if not desc:
                problems.append(f'{lang}/{pid} desc no fit: {head} w={width(head)} n={len(head)}')
                continue
            if _BANNED.search(title) or _BANNED.search(desc):
                problems.append(f'{lang}/{pid} banned wording')
            C[lang]['pages'][pid]['title'] = title
            C[lang]['pages'][pid]['description'] = desc
    for lang, c in C.items():
        if lang.startswith('_'):
            continue
        for pid, page in c['pages'].items():
            if lang in PRIORITY and pid in PRIORITY[lang]:
                continue
            page['description'] = fit_existing(lang, page['description'])
            if not in_range(lang, page['description']) or _BANNED.search(page['description']):
                problems.append(f'{lang}/{pid} desc n={len(page["description"])} m={meas(lang, page["description"])}: {page["description"][:90]}')
            if 'PlayStation' in page.get('title', ''):
                nt = clean_title(page['title'])
                limit = 64 if lang in CJK else (60 if lang != 'th' else 60)
                got = width(nt) if lang in CJK else (glen(nt) if lang == 'th' else len(nt))
                if 'ASCON' in nt and got <= limit and 'PlayStation' not in nt:
                    page['title'] = nt
    if problems:
        raise SystemExit('seo_market:\n' + '\n'.join(problems[:40]))
    return C
