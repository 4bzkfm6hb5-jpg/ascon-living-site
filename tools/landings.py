"""Booking-intent landing pages for en, de, ko, ja and vi.

Copy is the Market Researcher pack of 23 Oct 2026. The Vietnamese daily-rental
page uses homestay / nguyên căn. The word villa is not published.
Karaoke and PlayStation stay in body copy and meta descriptions. Two titles
that led with them are worded around the stay so headlines stay on the house.
"""
import html

LANGS = ('en', 'de', 'ko', 'ja', 'vi')
HL = {'en': 'en', 'de': 'de', 'ko': 'ko', 'ja': 'ja', 'vi': 'vi'}

# pid, slug. Slugs differ by language; hreflang groups them by intent.
PAGE_SLUGS = [
    ('en-stay-house', 'saigon-house-rental/'),
    ('en-stay-home', 'ho-chi-minh-city-homestay/'),
    ('en-stay-group', 'group-accommodation-saigon/'),
    ('de-stay-house', 'ferienhaus-ho-chi-minh-stadt/'),
    ('de-stay-home', 'unterkunft-saigon/'),
    ('de-stay-group', 'gruppenunterkunft-saigon/'),
    ('ko-stay-house', 'hochiminh-dokchae/'),
    ('ko-stay-family', 'hochiminh-family-stay/'),
    ('ko-stay-group', 'hochiminh-group-stay/'),
    ('ja-stay-house', 'hochiminh-ikkenya-kashikiri/'),
    ('ja-stay-group', 'hochiminh-group-stay/'),
    ('ja-stay-family', 'hochiminh-family-long-stay/'),
    ('vi-stay-house', 'homestay-sai-gon-nguyen-can/'),
    ('vi-stay-group', 'homestay-sai-gon-cho-nhom/'),
    ('vi-stay-day', 'homestay-sai-gon-theo-ngay/'),
]
SLUG = dict(PAGE_SLUGS)
# Equivalent pages across languages. x-default is the English URL.
CLUSTERS = {
    'house': {
        'en': 'en-stay-house', 'de': 'de-stay-house', 'ko': 'ko-stay-house',
        'ja': 'ja-stay-house', 'vi': 'vi-stay-house',
    },
    'group': {
        'en': 'en-stay-group', 'de': 'de-stay-group', 'ko': 'ko-stay-group',
        'ja': 'ja-stay-group', 'vi': 'vi-stay-group',
    },
    'home': {
        'en': 'en-stay-home', 'de': 'de-stay-home', 'ko': 'ko-stay-family',
        'ja': 'ja-stay-family', 'vi': 'vi-stay-day',
    },
}
CLUSTER_OF = {pid: name for name, group in CLUSTERS.items() for pid in group.values()}

BOOK = {
    'en': 'Check availability', 'de': 'Jetzt buchen', 'ko': '예약 가능일 확인',
    'ja': '空室を確認', 'vi': 'Kiểm tra phòng trống',
}
FAQ_H = {
    'en': 'FAQ', 'de': 'Häufige Fragen', 'ko': '자주 묻는 질문',
    'ja': 'よくある質問', 'vi': 'Câu hỏi thường gặp',
}
LINK_H = {
    'en': 'Book the whole house', 'de': 'Das ganze Haus buchen', 'ko': '호치민 숙소 예약',
    'ja': '一軒家を予約する', 'vi': 'Đặt homestay nguyên căn',
}
STAY_H = {
    'en': 'Where to stay in Saigon',
    'de': 'Wo übernachten in Saigon',
    'ko': '호치민 숙소 추천',
    'ja': 'ホーチミンの宿泊先',
    'vi': 'Ở đâu khi đến Sài Gòn',
}


def _btn(lang, label):
    return f'<a class="btn primary" href="/{lang}/booking/">{html.escape(label)}</a>'


def _page(lang, title, description, h1, cover, cta_top, parts, faqs, cta_bottom):
    sections = [{'p': [_btn(lang, cta_top)]}]
    for h2, paras in parts:
        block = {'p': paras}
        if h2:
            block = {'h2': h2, 'p': paras}
        sections.append(block)
    sections.append({'h2': FAQ_H[lang], 'faq': faqs})
    sections.append({'p': [_btn(lang, cta_bottom)]})
    sections.append({'cta': True})
    return {
        'title': title,
        'description': description,
        'h1': h1,
        'cover': [cover, h1],
        'sections': sections,
    }


def _pages():
    en = {
        'en-stay-house': _page('en',
            'Whole House Rental in Saigon for Groups | ASCON LIVING',
            'Whole house rental in Saigon with 3 bedrooms, each with en-suite bathroom and AC, a rooftop terrace with BBQ and a full kitchen. Check dates.',
            'Whole house rental in Saigon', 'living',
            'Check your dates and book the whole house',
            [
                (None, [
                    'Looking for a house rental in Saigon rather than several hotel rooms? ASCON LIVING is a whole house at 389A Tran Xuan Soan, Tan Hung, Ho Chi Minh City. Your group books all of it: three floors plus a rooftop, more than 250 m² of space, and no other guests.',
                ]),
                ('What you get', [
                    'Three bedrooms, each with its own en-suite bathroom and air conditioning. The master bedroom has a 180x200 bed, a balcony and a 55" TV. The two other bedrooms have 160x200 beds and smart TVs. A separate guest WC is on the ground floor, so nobody queues in the morning.',
                    'The living room has a 75" TV and space for everyone. In the entertainment room you find a 4K projector, karaoke, PlayStation and Netflix. The full kitchen has an oven, a microwave, a rice cooker and a large fridge, and there is a washing machine for longer trips.',
                ]),
                ('The rooftop', [
                    'On top of the house sits a rooftop terrace of about 56 to 60 m² with a BBQ, an outdoor sofa and a view over the river and the city skyline. It is the place where evenings in Saigon end.',
                ]),
                ('Arrival made simple', [
                    'Check in yourself with the keypad lock, whenever your flight lands. An airport transfer can be arranged on request. Your host speaks English, German, Vietnamese and more, and answers before and during your stay at +84 909 410 382.',
                    'A whole house rental in Saigon suits families, groups of friends, colleagues and anyone who wants a real home base in Ho Chi Minh City.',
                ]),
                ('Why a whole house instead of hotel rooms', [
                    'With one booking you get bedrooms, bathrooms, a kitchen, a living room, an entertainment room and a rooftop. Nobody waits for the others in a lobby, children can sleep while adults talk upstairs, and you can share meals at home whenever you like.',
                ]),
            ],
            [
                ['Do we rent the whole house?', 'Yes. The house and the rooftop are used only by your group.'],
                ['How many bedrooms are there?', 'Three, each with an en-suite bathroom and AC, plus a guest WC.'],
                ['Can we cook?', 'Yes, the full kitchen has an oven, microwave, rice cooker and a large fridge.'],
                ['How does check-in work?', 'Self check-in with a keypad lock; instructions follow after booking.'],
            ],
            'Ready to have a house in Saigon to yourselves? Check availability'),
        'en-stay-home': _page('en',
            'Ho Chi Minh City Homestay – Entire House | ASCON LIVING',
            'Homestay in Ho Chi Minh City with the whole house to yourselves: 3 en-suite bedrooms, rooftop, karaoke room, kitchen and a host who speaks EN, DE, VI.',
            'Ho Chi Minh City homestay with the entire house to yourselves', 'bed1',
            'See free dates for this homestay',
            [
                (None, [
                    "A homestay in Ho Chi Minh City usually means a room in someone's home. At ASCON LIVING you get the personal side of a homestay, a host who knows the city, and the privacy of having the entire house to yourselves.",
                ]),
                ('A host, not a reception desk', [
                    'Your host speaks English, German, Vietnamese and more. Questions about food, markets or getting around are answered by message or at +84 909 410 382. An airport transfer can be arranged on request, and self check-in with a keypad means you arrive on your own schedule.',
                ]),
                ('A house, not a room', [
                    'The house at 389A Tran Xuan Soan, Tan Hung has three floors and a rooftop, more than 250 m² in total. Three bedrooms each have an en-suite bathroom and AC. The master bedroom comes with a 180x200 bed, a balcony and a 55" TV; the other two have 160x200 beds and smart TVs. A guest WC means visitors never need to use your bathroom.',
                ]),
                ('Living like a local', [
                    'Shop at a nearby market and cook in the full kitchen with oven, microwave, rice cooker and large fridge. Do laundry in the washing machine. In the evening, grill on the rooftop BBQ, relax on the outdoor sofa and look out over the river and the city skyline.',
                ]),
                ('Rainy day or late night', [
                    'The 75" TV in the living room, the 4K projector, karaoke, PlayStation and Netflix keep everyone busy when you stay in.',
                    'This homestay in Ho Chi Minh City works well for families visiting relatives, friends travelling together and anyone staying for more than a few nights.',
                ]),
                ('Good for longer stays too', [
                    'If you stay a week or more, the washing machine, the full kitchen and the quiet bedrooms make daily life easy. Your host can help with tips for markets, food and getting around the city.',
                ]),
            ],
            [
                ['Does the host live in the house?', 'No, the house is yours. The host is available by phone and message.'],
                ['Which languages does the host speak?', 'English, German, Vietnamese and more.'],
                ['Is there an airport transfer?', 'Yes, on request.'],
                ['Is it suitable for longer stays?', 'Yes, with a full kitchen and a washing machine.'],
            ],
            'Book your Ho Chi Minh City homestay'),
        'en-stay-group': _page('en',
            'Group Accommodation in Saigon – Whole House | ASCON LIVING',
            'Group accommodation in Saigon: one house with 3 en-suite bedrooms, karaoke, PlayStation, 4K projector and a rooftop BBQ terrace. Book direct.',
            'Group accommodation in Saigon: one house for everyone', 'roof-day',
            'Check dates for your group',
            [
                (None, [
                    'Travelling to Saigon with family or friends? Group accommodation in hotels splits everyone across floors and corridors. At ASCON LIVING your group stays together in one house, with three bedrooms for sleeping and plenty of shared space for everything else.',
                ]),
                ('Private rooms for everyone', [
                    'Each of the three bedrooms has an en-suite bathroom and its own AC. The master bedroom has a 180x200 bed, a balcony and a 55" TV. The two other bedrooms have 160x200 beds and smart TVs. A separate guest WC on the side keeps mornings relaxed.',
                ]),
                ('Shared space that actually fits a group', [
                    'The house has more than 250 m² over three floors. The living room has a 75" TV. The entertainment room has a 4K projector, karaoke, PlayStation and Netflix, so a movie night or a karaoke evening happens at home. The full kitchen with oven, microwave, rice cooker and large fridge makes group breakfasts and dinners easy.',
                ]),
                ('Evenings on the rooftop', [
                    'The rooftop terrace of about 56 to 60 m² has a BBQ and an outdoor sofa, with a view over the river and the city skyline.',
                ]),
                ('Easy logistics', [
                    'Self check-in with a keypad lock, an airport transfer on request and a host who speaks English, German, Vietnamese and more, reachable at +84 909 410 382. The address is 389A Tran Xuan Soan, Tan Hung, Ho Chi Minh City.',
                    "Birthdays, family reunions, friends' trips or a team stay: this group accommodation in Saigon gives you one place to come home to.",
                ]),
                ('One booking for the whole group', [
                    'One reservation covers the entire house, so there is no need to coordinate several hotel bookings. Everyone has a private bedroom with bathroom, and the shared rooms are big enough to spend time together.',
                ]),
            ],
            [
                ['Is the house only for our group?', 'Yes, there are no other guests.'],
                ['Is there entertainment in the house?', 'Yes: karaoke, PlayStation, 4K projector, Netflix and a 75" TV.'],
                ['Can we have a BBQ?', 'Yes, on the rooftop terrace.'],
                ['Can you organise an airport transfer?', 'Yes, on request.'],
            ],
            'Bring your group under one roof'),
    }
    de = {
        'de-stay-house': _page('de',
            'Ferienhaus Ho Chi Minh Stadt mieten | ASCON LIVING',
            'Ganzes Ferienhaus in Ho Chi Minh Stadt mieten: über 250 m², 3 Schlafzimmer mit Bad und Klimaanlage, Dachterrasse mit Flussblick. Gastgeber spricht Deutsch.',
            'Ferienhaus in Ho Chi Minh Stadt mieten', 'living',
            'Freie Termine prüfen und das ganze Haus buchen',
            [
                (None, [
                    'Ihr sucht ein Ferienhaus in Ho Chi Minh Stadt statt mehrerer Hotelzimmer? ASCON LIVING ist ein ganzes Haus in der 389A Tran Xuan Soan, Tan Hung, Ho Chi Minh Stadt. Ihr bucht alles: drei Etagen plus Dachterrasse, über 250 m² Fläche und keine anderen Gäste.',
                ]),
                ('Was euch erwartet', [
                    'Drei Schlafzimmer, jedes mit eigenem Bad und Klimaanlage. Das Hauptschlafzimmer hat ein Bett mit 180x200, einen Balkon und einen 55-Zoll-Fernseher. Die beiden anderen Schlafzimmer haben Betten mit 160x200 und Smart-TVs. Dazu kommt ein separates Gäste-WC.',
                    'Im Wohnzimmer steht ein 75-Zoll-Fernseher. Im Unterhaltungsraum gibt es einen 4K-Beamer, Karaoke, PlayStation und Netflix. Die voll ausgestattete Küche hat Backofen, Mikrowelle, Reiskocher und einen großen Kühlschrank, außerdem gibt es eine Waschmaschine.',
                ]),
                ('Die Dachterrasse', [
                    'Ganz oben liegt die Dachterrasse mit etwa 56 bis 60 m², BBQ und Outdoor-Sofa. Von hier blickt ihr auf den Fluss und die Skyline der Stadt.',
                ]),
                ('Ankommen ohne Stress', [
                    'Self-Check-in per Zahlenschloss, egal wann euer Flug landet. Ein Flughafentransfer ist auf Anfrage möglich. Euer Gastgeber spricht Deutsch, Englisch, Vietnamesisch und weitere Sprachen und ist unter +84 909 410 382 erreichbar.',
                    'Für Familien, Freundesgruppen und alle, die in Saigon ein echtes Zuhause auf Zeit suchen, ist dieses Ferienhaus in Ho Chi Minh Stadt die passende Basis.',
                ]),
                ('Warum ein ganzes Haus statt Hotelzimmer', [
                    'Mit einer einzigen Buchung habt ihr Schlafzimmer, Bäder, Küche, Wohnzimmer, Unterhaltungsraum und Dachterrasse. Niemand wartet in einer Lobby, Kinder schlafen, während die Erwachsenen oben auf dem Dach sitzen, und gegessen wird, wann ihr wollt. Gerade für Familien und Freundesgruppen ist das entspannter als mehrere Hotelzimmer auf verschiedenen Etagen. Für eure Reise heißt das: weniger Organisation und mehr gemeinsame Zeit.',
                ]),
            ],
            [
                ['Mieten wir das ganze Haus?', 'Ja. Haus und Dachterrasse nutzt nur eure Gruppe.'],
                ['Spricht der Gastgeber Deutsch?', 'Ja, dazu Englisch, Vietnamesisch und weitere Sprachen.'],
                ['Wie viele Schlafzimmer gibt es?', 'Drei, jedes mit eigenem Bad und Klimaanlage, plus Gäste-WC.'],
                ['Wie funktioniert der Check-in?', 'Per Zahlenschloss; die Anleitung kommt nach der Buchung.'],
            ],
            'Lust auf ein eigenes Haus in Saigon? Verfügbarkeit prüfen'),
        'de-stay-home': _page('de',
            'Unterkunft in Saigon – ganzes Haus | ASCON LIVING',
            'Unterkunft in Saigon mit deutschsprachigem Gastgeber: ganzes Haus, 3 Schlafzimmer mit Bad, Küche, Dachterrasse mit BBQ, Flughafentransfer auf Anfrage.',
            'Unterkunft in Saigon mit deutschsprachigem Gastgeber', 'bed1',
            'Termine für eure Unterkunft in Saigon ansehen',
            [
                (None, [
                    'Eine gute Unterkunft in Saigon zu finden, ist auf Deutsch gar nicht so einfach. Bei ASCON LIVING bekommt ihr ein ganzes Haus in Ho Chi Minh Stadt und einen Gastgeber, der Deutsch spricht. Fragen zu Essen, Märkten oder dem Weg durch die Stadt klärt ihr ohne Sprachbarriere. Schon vor der Anreise könnt ihr alles Wichtige in Ruhe auf Deutsch besprechen, von der Ankunftszeit bis zum Flughafentransfer.',
                ]),
                ('Das Haus', [
                    'Die Adresse ist 389A Tran Xuan Soan, Tan Hung. Auf drei Etagen und über 250 m² gibt es drei Schlafzimmer mit eigenem Bad und Klimaanlage. Das Hauptschlafzimmer hat ein 180x200-Bett, einen Balkon und einen 55-Zoll-Fernseher, die beiden weiteren Zimmer haben 160x200-Betten und Smart-TVs. Ein Gäste-WC ist ebenfalls vorhanden.',
                ]),
                ('Wohnen wie zu Hause', [
                    'Die Küche ist komplett: Backofen, Mikrowelle, Reiskocher und ein großer Kühlschrank. Eine Waschmaschine macht auch längere Aufenthalte bequem. Im Wohnzimmer läuft der 75-Zoll-Fernseher, im Unterhaltungsraum warten 4K-Beamer, Karaoke, PlayStation und Netflix.',
                ]),
                ('Abends auf dem Dach', [
                    'Die Dachterrasse mit etwa 56 bis 60 m² hat einen BBQ-Grill und ein Outdoor-Sofa, dazu den Blick auf den Fluss und die Skyline.',
                ]),
                ('Unkompliziert anreisen', [
                    'Self-Check-in per Zahlenschloss, Flughafentransfer auf Anfrage, Gastgeber erreichbar unter +84 909 410 382.',
                    'Diese Unterkunft in Saigon passt zu Familien, Paaren mit Freunden, Verwandtenbesuchen und allen, die länger bleiben wollen.',
                ]),
                ('Ideal auch für längere Aufenthalte', [
                    'Wer eine Woche oder länger in Saigon bleibt, profitiert von Waschmaschine, voller Küche und ruhigen Schlafzimmern. Der Alltag fühlt sich an wie zu Hause, nur in Vietnam. Euer Gastgeber gibt euch auf Deutsch Tipps zu Märkten, Essen und dem Weg durch die Stadt, damit ihr euch schnell zurechtfindet und nicht lange suchen müsst.',
                ]),
            ],
            [
                ['Wohnt der Gastgeber im Haus?', 'Nein, das Haus gehört während des Aufenthalts euch. Der Gastgeber ist per Telefon und Nachricht erreichbar.'],
                ['Gibt es einen Flughafentransfer?', 'Ja, auf Anfrage.'],
                ['Eignet sich die Unterkunft für längere Aufenthalte?', 'Ja, mit voller Küche und Waschmaschine.'],
                ['Kann man selbst kochen?', 'Ja, die Küche ist komplett ausgestattet.'],
            ],
            'Eure Unterkunft in Saigon jetzt anfragen'),
        'de-stay-group': _page('de',
            'Gruppenunterkunft Saigon – ganzes Haus | ASCON LIVING',
            'Gruppenunterkunft in Saigon: ein ganzes Haus mit 3 Schlafzimmern samt Bad, Karaoke, PlayStation, 4K-Beamer und Dachterrasse mit BBQ. Direkt buchen.',
            'Gruppenunterkunft in Saigon: ein Haus für die ganze Gruppe', 'roof-day',
            'Termine für eure Gruppe prüfen',
            [
                (None, [
                    'Mit Familie oder Freunden nach Saigon? Im Hotel landet die Gruppe auf verschiedenen Fluren. Bei ASCON LIVING bleibt ihr zusammen: ein ganzes Haus, drei Schlafzimmer zum Zurückziehen und viel gemeinsamer Platz für alles andere. Statt Treffpunkt in der Hotellobby gibt es Wohnzimmer, Küche und Dachterrasse nur für euch, und niemand muss nachts durch fremde Flure zurück ins Zimmer.',
                ]),
                ('Eigenes Zimmer, eigenes Bad', [
                    'Jedes der drei Schlafzimmer hat ein eigenes Bad und Klimaanlage. Hauptschlafzimmer mit 180x200-Bett, Balkon und 55-Zoll-Fernseher, zwei weitere Zimmer mit 160x200-Betten und Smart-TVs. Das Gäste-WC entlastet morgens zusätzlich.',
                ]),
                ('Gemeinsam statt nebeneinander', [
                    'Über 250 m² auf drei Etagen. Im Wohnzimmer ein 75-Zoll-Fernseher, im Unterhaltungsraum 4K-Beamer, Karaoke, PlayStation und Netflix. Filmabend oder Karaoke-Abend findet einfach zu Hause statt. In der Küche mit Backofen, Mikrowelle, Reiskocher und großem Kühlschrank kocht ihr gemeinsam.',
                ]),
                ('Dachterrasse mit BBQ', [
                    'Die Dachterrasse mit etwa 56 bis 60 m² hat einen Grill und ein Outdoor-Sofa, mit Blick auf den Fluss und die Skyline der Stadt.',
                ]),
                ('Organisation leicht gemacht', [
                    'Self-Check-in per Zahlenschloss, Flughafentransfer auf Anfrage, Gastgeber spricht Deutsch, Englisch, Vietnamesisch und mehr, Telefon +84 909 410 382. Adresse: 389A Tran Xuan Soan, Tan Hung, Ho Chi Minh Stadt.',
                    'Ob Familientreffen, Geburtstag, Freundesreise oder Teamaufenthalt: Diese Gruppenunterkunft in Saigon gibt euch einen gemeinsamen Ort.',
                ]),
                ('Eine Buchung für die ganze Gruppe', [
                    'Eine Reservierung umfasst das ganze Haus. Ihr müsst also nicht mehrere Hotelbuchungen abstimmen. Alle haben ein eigenes Schlafzimmer mit Bad, und die gemeinsamen Räume sind groß genug, um Zeit miteinander zu verbringen. Das spart Kosten für mehrere Zimmer und macht die Planung für alle Beteiligten einfacher.',
                ]),
            ],
            [
                ['Sind wir allein im Haus?', 'Ja, es gibt keine anderen Gäste.'],
                ['Welche Unterhaltung gibt es?', 'Karaoke, PlayStation, 4K-Beamer, Netflix und ein 75-Zoll-Fernseher.'],
                ['Können wir grillen?', 'Ja, auf der Dachterrasse.'],
                ['Organisiert ihr einen Flughafentransfer?', 'Ja, auf Anfrage.'],
            ],
            'Die ganze Gruppe unter einem Dach'),
    }
    ko = {
        'ko-stay-house': _page('ko',
            '호치민 독채 숙소 – 단독주택 한 채 통째로 | ASCON LIVING',
            '호치민 독채 숙소. 250㎡ 넘는 3층 단독주택과 루프탑을 우리 일행만 사용. 침실 3개 모두 전용 욕실·에어컨, 노래방, 풀 주방. 날짜 확인하기.',
            '호치민 독채 숙소, 단독주택 한 채를 통째로', 'living',
            '빈 날짜 확인하고 집 전체 예약하기',
            [
                (None, [
                    '호치민 숙소를 찾을 때 호텔 방 여러 개를 따로 잡는 대신 집 한 채를 통째로 쓰는 방법이 있습니다. ASCON LIVING은 호치민 떤흥(Tan Hung), 389A Tran Xuan Soan에 있는 단독주택입니다. 3층과 루프탑, 250㎡가 넘는 공간 전체를 예약한 일행만 사용하며 다른 투숙객은 없습니다.',
                ]),
                ('침실과 욕실', [
                    '침실은 3개이고 모두 전용 욕실과 개별 에어컨이 있습니다. 마스터 침실에는 180×200cm 침대, 전용 발코니, 55인치 TV가 있고, 나머지 두 침실에는 160×200cm 침대와 스마트 TV가 있습니다. 별도의 게스트 화장실도 있어 아침에 욕실 앞에서 기다릴 일이 없습니다.',
                ]),
                ('함께 쓰는 공간', [
                    '거실에는 75인치 TV가 있고, 엔터테인먼트룸에는 4K 프로젝터, 노래방, PlayStation, Netflix가 준비되어 있습니다. 주방에는 오븐, 전자레인지, 밥솥, 대형 냉장고가 있어 직접 요리할 수 있고, 세탁기도 있습니다.',
                ]),
                ('루프탑', [
                    '약 56–60㎡ 루프탑 테라스에는 BBQ 그릴과 야외 소파가 있으며, 강과 도시 스카이라인이 내려다보입니다.',
                ]),
                ('체크인', [
                    '키패드 도어락으로 셀프 체크인하므로 늦은 비행기도 걱정 없습니다. 공항 픽업은 요청 시 준비해 드립니다. 호스트는 영어, 독일어, 베트남어 등을 하며 +84 909 410 382로 연락할 수 있습니다.',
                ]),
                ('호텔 대신 독채를 고르는 이유', [
                    '한 번의 예약으로 침실, 욕실, 주방, 거실, 엔터테인먼트룸, 루프탑까지 모두 생깁니다. 로비에서 서로를 기다릴 필요가 없고, 아이들이 일찍 잠든 뒤에도 어른들은 루프탑에서 이야기를 나눌 수 있습니다. 식사 시간도 일행이 원하는 대로 정하면 됩니다. 호텔 방 여러 개를 따로 예약하는 것보다 일정 조율도 훨씬 간단합니다.',
                ]),
            ],
            [
                ['집 전체를 쓰나요?', '네, 집과 루프탑 모두 예약한 일행만 사용합니다.'],
                ['침실은 몇 개인가요?', '3개이며 모두 전용 욕실과 에어컨이 있고, 게스트 화장실이 따로 있습니다.'],
                ['요리할 수 있나요?', '네, 오븐·전자레인지·밥솥·대형 냉장고가 있는 풀 주방이 있습니다.'],
                ['체크인은 어떻게 하나요?', '키패드 도어락 셀프 체크인이며, 안내는 예약 후 보내 드립니다.'],
            ],
            '호치민에서 우리만의 집을 원한다면, 예약 가능 날짜 보기'),
        'ko-stay-family': _page('ko',
            '호치민 가족 숙소 – 침실마다 욕실 있는 독채 | ASCON LIVING',
            '호치민 가족 숙소로 독채 단독주택. 전용 욕실 딸린 침실 3개, 75인치 TV 거실, 풀 주방, 세탁기, 루프탑 BBQ. 공항 픽업 요청 가능.',
            '호치민 가족 숙소, 침실마다 욕실이 있는 독채', 'bed1',
            '가족 여행 날짜 확인하기',
            [
                (None, [
                    '부모님, 아이들과 함께하는 호치민 가족여행이라면 숙소에서 가장 중요한 것은 각자 쉴 수 있는 방과 함께 모일 공간입니다. ASCON LIVING은 집 한 채를 가족이 통째로 쓰는 독채 숙소입니다.',
                ]),
                ('세 침실, 세 개의 욕실', [
                    '마스터 침실은 180×200cm 침대와 발코니, 55인치 TV가 있어 부모님께 잘 맞습니다. 다른 두 침실에도 160×200cm 침대와 스마트 TV, 전용 욕실, 에어컨이 있습니다. 게스트 화장실도 따로 있습니다.',
                ]),
                ('집처럼 지내는 주방과 세탁', [
                    '오븐, 전자레인지, 밥솥, 대형 냉장고가 있는 주방에서 아이 식사나 한식도 직접 준비할 수 있습니다. 세탁기가 있어 짐을 줄일 수 있습니다.',
                ]),
                ('가족이 함께하는 저녁', [
                    '75인치 TV가 있는 거실, 4K 프로젝터와 Netflix로 영화 보기, 노래방과 PlayStation, 그리고 루프탑 BBQ. 루프탑에서는 강과 도시 스카이라인이 보입니다.',
                ]),
                ('도착부터 편하게', [
                    '공항 픽업은 요청 시 준비해 드리고, 키패드 셀프 체크인이라 도착 시간에 구애받지 않습니다. 주소는 호치민 떤흥, 389A Tran Xuan Soan이며 호스트 연락처는 +84 909 410 382입니다.',
                ]),
                ('한달살기·장기 체류에도', [
                    '일주일 이상 머문다면 세탁기와 풀 주방, 조용한 침실 덕분에 일상이 집처럼 편해집니다. 호스트가 시장, 맛집, 시내 이동 방법도 알려 드려 처음 가는 호치민에서도 금방 익숙해질 수 있습니다. 호치민 한달살기 숙소를 찾는 분들께도 잘 맞는 구성입니다.',
                ]),
            ],
            [
                ['아이와 함께 묵어도 되나요?', '네, 가족 여행을 위한 독채입니다.'],
                ['밥솥이 있나요?', '네, 밥솥과 오븐, 전자레인지, 대형 냉장고가 있습니다.'],
                ['세탁할 수 있나요?', '네, 세탁기가 있습니다.'],
                ['공항 픽업이 되나요?', '네, 요청 시 가능합니다.'],
            ],
            '가족 모두 한 집에서 예약하기'),
        'ko-stay-group': _page('ko',
            '호치민 단체 숙소 – 한 집 독채 | ASCON LIVING',
            '호치민 단체 숙소로 집 한 채를 통째로. 전용 욕실 딸린 침실 3개, 노래방·PlayStation·4K 프로젝터, 루프탑 BBQ 테라스. 친구·동료 여행에.',
            '호치민 단체 숙소, 한 집에서 함께 머무는 독채', 'roof-day',
            '일행 날짜 확인하기',
            [
                (None, [
                    '친구나 동료와 호치민에 간다면 호텔에서는 방이 층마다 흩어지고 밤에 모일 곳이 마땅치 않습니다. ASCON LIVING은 일행 전체가 한 집에 머무는 단독주택 숙소입니다.',
                ]),
                ('각자의 방', [
                    '침실 3개 모두 전용 욕실과 에어컨이 있습니다. 마스터 침실은 180×200cm 침대, 발코니, 55인치 TV, 나머지 두 침실은 160×200cm 침대와 스마트 TV입니다. 게스트 화장실이 따로 있습니다.',
                ]),
                ('함께 노는 공간', [
                    '250㎡가 넘는 3층 집에 75인치 TV 거실과 엔터테인먼트룸이 있습니다. 노래방, PlayStation, 4K 프로젝터, Netflix가 있어 밖에 나가지 않아도 저녁이 즐겁습니다. 풀 주방에서 함께 요리하고 식사할 수 있습니다.',
                ]),
                ('루프탑 BBQ', [
                    '약 56–60㎡ 루프탑에 BBQ 그릴과 야외 소파가 있고, 강과 도시 스카이라인이 펼쳐집니다.',
                ]),
                ('편한 진행', [
                    '키패드 셀프 체크인, 요청 시 공항 픽업, 영어·독일어·베트남어 등을 하는 호스트(+84 909 410 382). 주소: 호치민 떤흥, 389A Tran Xuan Soan.',
                    '생일, 동창 여행, 회사 워크숍 등 한 지붕 아래 모이고 싶은 일행에게 맞는 호치민 단체 숙소입니다.',
                ]),
                ('일행 전체를 한 번에 예약', [
                    '예약 한 번이면 집 전체가 우리 일행 것이 됩니다. 여러 호텔 방을 맞춰 예약할 필요가 없고, 모두가 전용 욕실 딸린 개인 침실을 쓰면서도 넓은 공용 공간에서 함께 시간을 보낼 수 있습니다. 비용을 나누기도 간단해서 단체 여행 준비가 한결 수월해집니다.',
                ]),
            ],
            [
                ['다른 투숙객이 있나요?', '아니요, 집 전체를 일행만 사용합니다.'],
                ['노래방이 있나요?', '네, 엔터테인먼트룸에 노래방과 PlayStation, 4K 프로젝터가 있습니다.'],
                ['BBQ를 할 수 있나요?', '네, 루프탑 테라스에서 가능합니다.'],
                ['공항 픽업이 되나요?', '네, 요청 시 가능합니다.'],
            ],
            '일행 모두 한 집으로 예약하기'),
    }
    ja = {
        'ja-stay-house': _page('ja',
            'ホーチミン 一軒家 貸切 – 3寝室とルーフトップ | ASCON LIVING',
            'ホーチミンの一軒家貸切。250㎡超の3階建てとルーフトップをグループだけで利用。寝室3室すべてに専用バスとエアコン。空き日程を確認。',
            'ホーチミンの一軒家を貸切で', 'living',
            '空き日程を確認して一軒家を予約',
            [
                (None, [
                    'ホーチミンで宿泊先を探すなら、ホテルの部屋を何室も取る代わりに一軒家を貸切にする方法があります。ASCON LIVINGはホーチミン市タンフン（Tan Hung）、389A Tran Xuan Soanにある一軒家です。3階建てとルーフトップ、250㎡を超える空間すべてを予約したグループだけで使えます。他の宿泊客はいません。',
                ]),
                ('寝室とバスルーム', [
                    '寝室は3室で、すべてに専用バスルームと個別エアコンがあります。主寝室には180×200cmのベッド、バルコニー、55インチテレビ。他の2室には160×200cmのベッドとスマートテレビがあります。ゲスト用トイレも別にあります。',
                ]),
                ('共用スペース', [
                    'リビングには75インチテレビ。エンターテインメントルームには4Kプロジェクター、カラオケ、PlayStation、Netflixがあります。キッチンにはオーブン、電子レンジ、炊飯器、大型冷蔵庫がそろい、洗濯機もあります。',
                ]),
                ('ルーフトップ', [
                    '約56〜60㎡のルーフトップテラスにはBBQグリルと屋外ソファがあり、川と街のスカイラインを眺められます。',
                ]),
                ('チェックイン', [
                    'キーパッド式ロックでセルフチェックイン。遅い便でも安心です。空港送迎はご希望に応じて手配します。ホストは英語、ドイツ語、ベトナム語などを話し、+84 909 410 382で連絡できます。',
                ]),
                ('ホテルではなく一軒家を選ぶ理由', [
                    '一度の予約で、寝室、バスルーム、キッチン、リビング、エンターテインメントルーム、ルーフトップまでそろいます。ロビーで待ち合わせる必要はなく、子どもが早く寝たあとも大人はルーフトップで過ごせます。食事の時間も自由です。ホテルの部屋をいくつも予約するより、手配もずっと簡単になります。',
                ]),
            ],
            [
                ['家全体を使えますか？', 'はい、家とルーフトップはご予約のグループ専用です。'],
                ['寝室はいくつですか？', '3室で、すべて専用バスとエアコン付き。ゲスト用トイレもあります。'],
                ['自炊できますか？', 'はい、オーブン・電子レンジ・炊飯器・大型冷蔵庫のあるキッチンがあります。'],
                ['チェックイン方法は？', 'キーパッド式のセルフチェックインで、案内は予約後にお送りします。'],
            ],
            'ホーチミンで自分たちだけの家に泊まる'),
        'ja-stay-group': _page('ja',
            'ホーチミン グループ宿泊 – 一軒家貸切 | ASCON LIVING',
            'ホーチミンでのグループ宿泊に一軒家を貸切。専用バス付き寝室3室、カラオケ・PlayStation・4Kプロジェクター、ルーフトップBBQ。友人・社員旅行に。',
            'ホーチミンのグループ宿泊は一軒家貸切で', 'roof-day',
            'グループの日程を確認',
            [
                (None, [
                    '友人や同僚とホーチミンへ行くとき、ホテルでは部屋がばらばらになり、夜に集まる場所もありません。ASCON LIVINGならグループ全員がひとつの家に泊まれます。',
                ]),
                ('それぞれの部屋', [
                    '寝室3室はすべて専用バスルームとエアコン付き。主寝室は180×200cmのベッド、バルコニー、55インチテレビ。他の2室は160×200cmのベッドとスマートテレビです。ゲスト用トイレもあります。',
                ]),
                ('みんなで過ごす空間', [
                    '250㎡を超える3階建てに、75インチテレビのリビングとエンターテインメントルーム。カラオケ、PlayStation、4Kプロジェクター、Netflixで、外に出なくても夜を楽しめます。フルキッチンでみんなで料理もできます。',
                ]),
                ('ルーフトップBBQ', [
                    '約56〜60㎡のルーフトップにBBQグリルと屋外ソファ。川と街のスカイラインが広がります。',
                ]),
                ('スムーズな滞在', [
                    'キーパッドでセルフチェックイン、空港送迎はご希望に応じて手配、英語・ドイツ語・ベトナム語などを話すホスト（+84 909 410 382）。住所：ホーチミン市タンフン、389A Tran Xuan Soan。',
                    '誕生日、同窓旅行、社員旅行など、ひとつ屋根の下に集まりたいグループのための宿泊先です。',
                ]),
                ('一度の予約でグループ全員', [
                    '一回の予約で家全体がグループ専用になります。複数のホテル予約を調整する必要はなく、全員が専用バス付きの個室を使いながら、広い共用スペースで一緒に過ごせます。費用の割り勘もしやすく、幹事さんの負担も軽くなります。',
                ]),
            ],
            [
                ['他の宿泊客はいますか？', 'いいえ、家全体をグループだけで使います。'],
                ['カラオケはありますか？', 'はい、エンターテインメントルームにカラオケ、PlayStation、4Kプロジェクターがあります。'],
                ['BBQはできますか？', 'はい、ルーフトップテラスでできます。'],
                ['空港送迎はありますか？', 'はい、ご希望に応じて手配します。'],
            ],
            'グループ全員でひとつの家へ'),
        'ja-stay-family': _page('ja',
            'ホーチミン 家族旅行・長期滞在の宿泊先 | ASCON LIVING',
            'ホーチミンでの家族旅行や長期滞在に一軒家貸切。寝室3室すべて専用バス付き、炊飯器・オーブンのあるキッチン、洗濯機、ルーフトップ。空港送迎あり。',
            'ホーチミンの家族旅行・長期滞在に一軒家を', 'bed1',
            '家族旅行・長期滞在の日程を確認',
            [
                (None, [
                    '小さな子ども連れやご両親との旅行、あるいは数週間の滞在なら、ホテルより家のほうがずっと楽です。ASCON LIVINGはホーチミンで一軒家をまるごと使える宿泊先です。',
                ]),
                ('3つの寝室、3つのバスルーム', [
                    '主寝室は180×200cmのベッド、バルコニー、55インチテレビ。他の2室は160×200cmのベッドとスマートテレビ。すべての寝室に専用バスルームとエアコンがあり、ゲスト用トイレも別にあります。',
                ]),
                ('暮らすように泊まる', [
                    'キッチンにはオーブン、電子レンジ、炊飯器、大型冷蔵庫。ご飯を炊いて、市場で買った食材で料理ができます。洗濯機があるので長期滞在でも荷物が少なくて済みます。',
                ]),
                ('家族の時間', [
                    '75インチテレビのリビング、4KプロジェクターとNetflixで映画、カラオケやPlayStation。夕方はルーフトップでBBQをしながら川と街のスカイラインを眺められます。',
                ]),
                ('到着から安心', [
                    '空港送迎はご希望に応じて手配し、キーパッドでセルフチェックイン。ホストは英語、ドイツ語、ベトナム語などを話します（+84 909 410 382）。住所：ホーチミン市タンフン、389A Tran Xuan Soan。',
                ]),
                ('長期滞在にもぴったり', [
                    '1週間以上の滞在なら、洗濯機、フルキッチン、静かな寝室のおかげで毎日の生活が自宅のように快適です。ホストが市場や食事、市内の移動についてアドバイスするので、初めてのホーチミンでもすぐに慣れることができます。',
                ]),
            ],
            [
                ['子ども連れでも泊まれますか？', 'はい、家族旅行のための一軒家です。'],
                ['炊飯器はありますか？', 'はい、炊飯器、オーブン、電子レンジ、大型冷蔵庫があります。'],
                ['長期滞在はできますか？', 'はい、キッチンと洗濯機があり長期滞在にも向いています。'],
                ['空港送迎はありますか？', 'はい、ご希望に応じて手配します。'],
            ],
            '家族でゆったり滞在する'),
    }
    vi = {
        'vi-stay-house': _page('vi',
            'Thuê homestay nguyên căn Sài Gòn theo ngày | ASCON LIVING',
            'Thuê homestay nguyên căn ở Sài Gòn theo ngày: nhà 3 tầng hơn 250 m², 3 phòng ngủ có WC riêng và máy lạnh, sân thượng view sông. Xem lịch trống.',
            'Thuê homestay nguyên căn Sài Gòn theo ngày', 'living',
            'Xem lịch trống và đặt cả ngôi nhà',
            [
                (None, [
                    'Bạn muốn thuê homestay nguyên căn ở Sài Gòn thay vì đặt nhiều phòng khách sạn? ASCON LIVING là một ngôi nhà nguyên căn tại 389A Trần Xuân Soạn, phường Tân Hưng, TP. Hồ Chí Minh. Cả nhóm dùng trọn ngôi nhà: 3 tầng cộng sân thượng, hơn 250 m², không có khách khác.',
                ]),
                ('Phòng ngủ', [
                    '3 phòng ngủ, phòng nào cũng có WC riêng và máy lạnh. Phòng master có giường 180x200, ban công và TV 55 inch. Hai phòng còn lại có giường 160x200 và smart TV. Ngoài ra còn có một WC cho khách riêng.',
                ]),
                ('Không gian chung', [
                    'Phòng khách có TV 75 inch. Phòng giải trí có máy chiếu 4K, karaoke, PlayStation và Netflix. Bếp đầy đủ với lò nướng, lò vi sóng, nồi cơm điện và tủ lạnh lớn, cùng máy giặt.',
                ]),
                ('Sân thượng', [
                    'Sân thượng khoảng 56–60 m² có bếp BBQ, sofa ngoài trời và view sông cùng đường chân trời thành phố.',
                ]),
                ('Nhận phòng', [
                    'Tự check-in bằng khóa mã số, đến giờ nào cũng được. Đưa đón sân bay theo yêu cầu. Chủ nhà nói tiếng Việt, tiếng Anh, tiếng Đức và nhiều thứ tiếng khác, liên hệ +84 909 410 382.',
                    'Homestay nguyên căn Sài Gòn phù hợp cho gia đình, nhóm bạn, đồng nghiệp hay người thân từ xa về thăm nhà.',
                ]),
                ('Vì sao nên thuê nguyên căn thay vì khách sạn', [
                    'Chỉ với một lần đặt, bạn có đủ phòng ngủ, WC, bếp, phòng khách, phòng giải trí và sân thượng. Không ai phải chờ ở sảnh, trẻ nhỏ ngủ sớm trong khi người lớn trò chuyện trên sân thượng, và cả nhà ăn uống lúc nào cũng được. So với đặt nhiều phòng khách sạn, thuê nguyên căn vừa riêng tư vừa tiết kiệm công sắp xếp.',
                ]),
            ],
            [
                ['Có được dùng cả ngôi nhà không?', 'Có. Ngôi nhà và sân thượng chỉ dành cho nhóm của bạn.'],
                ['Có mấy phòng ngủ?', '3 phòng, đều có WC riêng và máy lạnh, thêm một WC cho khách.'],
                ['Có nấu ăn được không?', 'Được, bếp có lò nướng, lò vi sóng, nồi cơm điện và tủ lạnh lớn.'],
                ['Check-in thế nào?', 'Tự check-in bằng khóa mã số, hướng dẫn gửi sau khi đặt.'],
            ],
            'Muốn có cả một ngôi nhà ở Sài Gòn cho riêng mình? Xem lịch trống'),
        'vi-stay-group': _page('vi',
            'Homestay Sài Gòn cho nhóm bạn | ASCON LIVING',
            'Homestay Sài Gòn cho nhóm bạn: cả ngôi nhà, 3 phòng ngủ có WC riêng, karaoke, PlayStation, máy chiếu 4K và sân thượng BBQ. Đặt trực tiếp.',
            'Homestay Sài Gòn cho nhóm bạn, cả nhà chỉ dành cho nhóm bạn', 'roof-day',
            'Xem lịch trống cho nhóm',
            [
                (None, [
                    'Đi chơi cùng nhóm bạn hay đồng nghiệp ở Sài Gòn, ở khách sạn thì mỗi người một phòng, tối không có chỗ tụ tập. Ở ASCON LIVING, cả nhóm ở chung một ngôi nhà nguyên căn.',
                ]),
                ('Phòng riêng cho từng người', [
                    '3 phòng ngủ đều có WC riêng và máy lạnh. Phòng master giường 180x200, ban công, TV 55 inch; hai phòng còn lại giường 160x200 và smart TV. Có thêm WC cho khách.',
                ]),
                ('Chơi cùng nhau', [
                    'Nhà 3 tầng hơn 250 m² có phòng khách TV 75 inch và phòng giải trí với karaoke, PlayStation, máy chiếu 4K, Netflix. Không cần ra ngoài cũng có một buổi tối vui. Bếp đầy đủ để cả nhóm nấu ăn chung.',
                ]),
                ('BBQ trên sân thượng', [
                    'Sân thượng khoảng 56–60 m² có bếp BBQ, sofa ngoài trời, nhìn ra sông và đường chân trời thành phố.',
                ]),
                ('Tiện lợi', [
                    'Tự check-in bằng khóa mã số, đưa đón sân bay theo yêu cầu, chủ nhà liên hệ +84 909 410 382. Địa chỉ: 389A Trần Xuân Soạn, phường Tân Hưng, TP. Hồ Chí Minh.',
                    'Sinh nhật, họp lớp, team building hay chuyến đi cuối tuần: homestay Sài Gòn cho nhóm này là nơi cả nhóm ở chung một mái nhà.',
                ]),
                ('Một lần đặt cho cả nhóm', [
                    'Một đơn đặt phòng là có trọn ngôi nhà, không cần chia nhau đặt nhiều phòng khách sạn. Ai cũng có phòng ngủ riêng với WC riêng, còn không gian chung đủ rộng để cả nhóm vui chơi cùng nhau. Việc chia chi phí trong nhóm cũng đơn giản hơn nhiều.',
                ]),
            ],
            [
                ['Có khách khác không?', 'Không, cả ngôi nhà chỉ dành cho nhóm bạn.'],
                ['Có karaoke không?', 'Có, phòng giải trí có karaoke, PlayStation và máy chiếu 4K.'],
                ['Có nướng BBQ được không?', 'Được, trên sân thượng.'],
                ['Có đưa đón sân bay không?', 'Có, theo yêu cầu.'],
            ],
            'Cả nhóm chung một nhà'),
        'vi-stay-day': _page('vi',
            'Thuê homestay Sài Gòn theo ngày cho gia đình | ASCON LIVING',
            'Thuê homestay nguyên căn ở Sài Gòn theo ngày cho gia đình: 3 phòng ngủ có WC riêng, bếp đầy đủ, máy giặt, sân thượng BBQ view sông. Đưa đón sân bay.',
            'Thuê homestay Sài Gòn theo ngày cho gia đình', 'bed1',
            'Xem lịch trống cho gia đình',
            [
                (None, [
                    'Gia đình về Sài Gòn thăm người thân, hay đi du lịch cùng ông bà và con nhỏ, cần nhiều phòng riêng và một chỗ để cả nhà quây quần. ASCON LIVING là ngôi nhà nguyên căn 3 tầng cộng sân thượng, cho thuê theo ngày, dành trọn cho gia đình bạn.',
                ]),
                ('Ba phòng ngủ, ba WC riêng', [
                    'Phòng master có giường 180x200, ban công và TV 55 inch. Hai phòng còn lại có giường 160x200 và smart TV. Phòng nào cũng có WC riêng và máy lạnh, thêm một WC cho khách.',
                ]),
                ('Sống như ở nhà', [
                    'Bếp có lò nướng, lò vi sóng, nồi cơm điện và tủ lạnh lớn để nấu cơm nhà. Có máy giặt, tiện cho kỳ nghỉ dài ngày.',
                ]),
                ('Thời gian bên nhau', [
                    'Phòng khách TV 75 inch, máy chiếu 4K và Netflix để xem phim, karaoke và PlayStation cho cả nhà. Buổi tối lên sân thượng nướng BBQ, ngắm sông và đường chân trời thành phố.',
                ]),
                ('Đến nơi thật dễ', [
                    'Đưa đón sân bay theo yêu cầu, tự check-in bằng khóa mã số. Chủ nhà nói tiếng Việt, tiếng Anh, tiếng Đức và nhiều thứ tiếng khác, liên hệ +84 909 410 382. Địa chỉ: 389A Trần Xuân Soạn, phường Tân Hưng.',
                ]),
                ('Phù hợp cả cho kỳ nghỉ dài ngày', [
                    'Nếu ở một tuần hoặc lâu hơn, máy giặt, bếp đầy đủ và phòng ngủ yên tĩnh giúp sinh hoạt hằng ngày thoải mái như ở nhà. Chủ nhà có thể gợi ý chợ, quán ăn ngon và cách đi lại trong thành phố để cả gia đình nhanh chóng quen nơi ở mới.',
                ]),
            ],
            [
                ['Đi cùng trẻ nhỏ được không?', 'Được, ngôi nhà rất phù hợp cho gia đình.'],
                ['Có thuê theo ngày không?', 'Có, thuê theo đêm, ngắn ngày hoặc dài ngày.'],
                ['Có máy giặt không?', 'Có.'],
                ['Có đưa đón sân bay không?', 'Có, theo yêu cầu.'],
            ],
            'Cả gia đình chung một nhà ở Sài Gòn'),
    }
    return {**en, **de, **ko, **ja, **vi}


PAGES = _pages()

STAY = {
    'en': (
        'If you travel as a family or group, ASCON LIVING is a whole house in Ho Chi Minh City with three en-suite bedrooms, a karaoke room and a rooftop BBQ terrace. Self check-in, airport transfer on request.',
        'Check dates for the house →', 'en-stay-house',
    ),
    'de': (
        'Für Familien und Gruppen ist ASCON LIVING ein ganzes Ferienhaus in Ho Chi Minh Stadt mit drei Schlafzimmern samt Bad, Karaoke-Raum und Dachterrasse mit BBQ. Der Gastgeber spricht Deutsch.',
        'Freie Termine ansehen →', 'de-stay-house',
    ),
    'ko': (
        '가족이나 단체 여행이라면 ASCON LIVING은 전용 욕실 딸린 침실 3개, 노래방, 루프탑 BBQ가 있는 호치민 독채 단독주택입니다. 셀프 체크인, 요청 시 공항 픽업.',
        '예약 가능 날짜 보기 →', 'ko-stay-house',
    ),
    'ja': (
        '家族やグループ旅行なら、ASCON LIVINGは専用バス付き寝室3室、カラオケ、ルーフトップBBQのあるホーチミンの一軒家貸切です。セルフチェックイン、空港送迎はご希望に応じて手配。',
        '空き日程を見る →', 'ja-stay-house',
    ),
    'vi': (
        'Nếu đi cùng gia đình hoặc nhóm bạn, ASCON LIVING là homestay Sài Gòn nguyên căn với 3 phòng ngủ có WC riêng, phòng karaoke và sân thượng BBQ. Tự check-in, đưa đón sân bay theo yêu cầu.',
        'Xem lịch trống →', 'vi-stay-house',
    ),
}

CARDS = {
    'en': [
        ('Whole house rental in Saigon', 'en-stay-house', 'Three en-suite bedrooms, a full kitchen and a rooftop terrace.'),
        ('Ho Chi Minh City homestay', 'en-stay-home', 'The entire house, with a host you can message or call.'),
        ('Group accommodation in Saigon', 'en-stay-group', 'One house for the whole group, with a rooftop BBQ.'),
    ],
    'de': [
        ('Ferienhaus in Ho Chi Minh Stadt', 'de-stay-house', 'Drei Schlafzimmer mit eigenem Bad, Küche und Dachterrasse.'),
        ('Unterkunft in Saigon', 'de-stay-home', 'Ganzes Haus und ein Gastgeber, der Deutsch spricht.'),
        ('Gruppenunterkunft in Saigon', 'de-stay-group', 'Ein Haus für die ganze Gruppe, mit Dachterrasse und BBQ.'),
    ],
    'ko': [
        ('호치민 독채 숙소', 'ko-stay-house', '단독주택 한 채, 침실 3개 모두 전용 욕실.'),
        ('호치민 가족 숙소', 'ko-stay-family', '가족이 통째로 쓰는 집, 풀 주방과 세탁기.'),
        ('호치민 단체 숙소', 'ko-stay-group', '일행이 한 집에서 머무는 독채, 루프탑 BBQ.'),
    ],
    'ja': [
        ('ホーチミンの一軒家貸切', 'ja-stay-house', '寝室3室すべて専用バス、ルーフトップ付き。'),
        ('グループ宿泊', 'ja-stay-group', 'グループ全員でひとつの家を貸切。'),
        ('家族旅行・長期滞在', 'ja-stay-family', '炊飯器と洗濯機のある一軒家。'),
    ],
    'vi': [
        ('Homestay nguyên căn Sài Gòn', 'vi-stay-house', '3 phòng ngủ có WC riêng, bếp và sân thượng.'),
        ('Homestay cho nhóm bạn', 'vi-stay-group', 'Cả ngôi nhà cho một nhóm, có sân thượng BBQ.'),
        ('Homestay theo ngày cho gia đình', 'vi-stay-day', 'Nhà nguyên căn cho gia đình, có bếp và máy giặt.'),
    ],
}


def hreflang_html(pid, site):
    group = CLUSTERS.get(CLUSTER_OF.get(pid, ''), {})
    if not group:
        return None
    tags = ''.join(
        f'<link rel="alternate" hreflang="{HL[code]}" href="{site}/{code}/{SLUG[group[code]]}">'
        for code in LANGS if code in group
    )
    return tags + f'<link rel="alternate" hreflang="x-default" href="{site}/en/{SLUG[group["en"]]}">'


def hreflang_sitemap(pid, site):
    group = CLUSTERS.get(CLUSTER_OF.get(pid, ''), {})
    if not group:
        return None
    tags = ''.join(
        f'<xhtml:link rel="alternate" hreflang="{HL[code]}" href="{site}/{code}/{SLUG[group[code]]}"/>'
        for code in LANGS if code in group
    )
    return tags + f'<xhtml:link rel="alternate" hreflang="x-default" href="{site}/en/{SLUG[group["en"]]}"/>'


def picker_slug(pid, dest):
    """Slug for a language switch. None if this page is not a landing."""
    name = CLUSTER_OF.get(pid)
    if not name:
        return None
    mate = CLUSTERS[name].get(dest)
    return SLUG[mate] if mate else ''


def _stay_block(lang):
    text, link, pid = STAY[lang]
    href = f'/{lang}/{SLUG[pid]}'
    return {
        'h2': STAY_H[lang],
        'p': [
            f'{html.escape(text)} <a href="{href}">{html.escape(link)}</a>',
            _btn(lang, BOOK[lang]),
        ],
    }


def _is_guide(pid):
    return pid == 'guide' or pid == 'travel-guide' or str(pid).startswith('guide-')


def install(C):
    if 'villa' in repr(PAGES).lower() or 'villa' in repr(STAY).lower() or 'villa' in repr(CARDS).lower():
        raise SystemExit('landing copy still contains villa')
    for lang in LANGS:
        pack = C.get(lang)
        if not isinstance(pack, dict):
            continue
        pages = pack.setdefault('pages', {})
        for pid, page in PAGES.items():
            if pid.startswith(lang + '-'):
                pages[pid] = page
        home = pages.get('home')
        if isinstance(home, dict):
            sections = home.setdefault('sections', [])
            if not any(isinstance(s, dict) and s.get('h2') == LINK_H[lang] for s in sections):
                sections.insert(0, {'h2': LINK_H[lang], 'cards': CARDS[lang]})
        block = _stay_block(lang)
        for pid, page in list(pages.items()):
            if not _is_guide(pid) or not isinstance(page, dict):
                continue
            sections = page.setdefault('sections', [])
            if any(isinstance(s, dict) and s.get('h2') == STAY_H[lang] for s in sections):
                continue
            sections.insert(0, block)
