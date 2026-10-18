"""VI / RU / FR from MR texts: extends tools/build_cjk.py (same pipeline and rules). VI keeps its existing ui and extra pages (imprint, privacy, guide subpages)."""
import re,sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
import build_cjk as B
import build_sea  # noqa: loads TH/MS/ID regex extensions (shared patterns)
def ext(rx,more): return re.compile(rx.pattern+'|'+more,rx.flags)
B.REP.update({
 'vi':[("dịch vụ giặt ủi theo yêu cầu","dịch vụ giặt ủi theo yêu cầu (30 EUR mỗi mẻ)"),("Dịch vụ giặt ủi theo yêu cầu","Dịch vụ giặt ủi theo yêu cầu (30 EUR mỗi mẻ)"),("Villa sân thượng","Sân thượng"),("villa","nhà nguyên căn"),("Villa","Nhà nguyên căn"),("biệt thự","nhà nguyên căn"),
   ("bạn nhận thông tin vào nhà và mật khẩu ứng dụng ASCON Guide.","bạn nhận thông tin vào nhà. Ứng dụng ASCON Guide miễn phí, không cần mật khẩu."),
   ("thông tin chìa khóa cổng ngoài và mật khẩu ứng dụng ASCON Guide để bắt đầu","thông tin chìa khóa cổng ngoài; ứng dụng ASCON Guide miễn phí giúp bạn bắt đầu"),
   ("xem phim máy chiếu 4K, két sắt, camera chỉ lắp bên ngoài.","xem phim máy chiếu 4K và két sắt."),
   ("Sau khi đặt phòng, bạn nhận mật khẩu ứng dụng ASCON Guide, trong đó có","Ứng dụng ASCON Guide miễn phí có"),
   ("Ứng dụng ASCON Guide cho khách lưu trú:","Ứng dụng ASCON Guide miễn phí:"),(" Mật khẩu gửi sau khi đặt phòng."," Không cần mật khẩu."),(" Mật khẩu được gửi sau khi đặt phòng."," Ứng dụng miễn phí, không cần mật khẩu."),
   ("Mật khẩu được gửi sau khi xác nhận đặt phòng. Bạn có thể mở","Ứng dụng miễn phí, không cần mật khẩu. Bạn có thể mở"),("Cách nhận mật khẩu","Mở ứng dụng"),
   ("Khi nào tôi nhận được mật khẩu?","Ứng dụng có cần mật khẩu không?"),("Sau khi đặt phòng được xác nhận.","Không. Ứng dụng miễn phí và mở ngay trên trình duyệt điện thoại."),
   ("Từ sân thượng và ban công","Từ sân thượng và hiên"),(", thỉnh thoảng có thuyền gỗ đi ngang,",","),
   (", lời bài hát hiện lớn trên màn chiếu 4K,",", màn chiếu 4K,"),("Chọn bài, lời hiện to trên màn chiếu 4K, micro chuyền tay nhau.","Chọn bài, micro chuyền tay nhau."),
   ("Chọn bài, lời hiện to trên màn chiếu 4K, micro chuyền tay.","Chọn bài, micro chuyền tay."),("Micro và lời bài hát trên màn chiếu 4K","Micro và màn chiếu 4K"),
   ("Có, với micro và lời bài hát trên màn chiếu.","Có, kèm micro karaoke."),(", kèm bếp nướng BBQ và sofa mây.",", kèm bếp nướng BBQ."),
   ("hàng xóm và an toàn.","và hàng xóm."),(", bếp, an toàn và đặt",", bếp và đặt"),("An toàn là trên hết","Tiện ích thiết thực"),("Cầu thang và an toàn","Cầu thang"),("Riêng tư được bảo đảm","Camera ở lối vào"),("lan can ban công","lan can hiên")],
 'ru':[("Вилла","Дом"),("вилла","дом"),("виллы","дома"),("вилле","доме"),("виллу","дом"),("виллой","домом"),
   ("вы получите данные для входа и пароль от приложения ASCON Guide.","вы получите данные для входа. Приложение ASCON Guide бесплатное и без пароля."),
   ("информацию о ключе от ворот и пароль от ASCON Guide, чтобы","информацию о ключе от ворот, а бесплатное приложение ASCON Guide поможет"),
   ("кино на 4K-проекторе, сейф и камеры только снаружи.","кино на 4K-проекторе и сейф."),
   ("После бронирования вы получаете пароль от приложения ASCON Guide, где есть","В бесплатном приложении ASCON Guide есть"),
   ("Приложение ASCON Guide для гостей:","Бесплатное приложение ASCON Guide:"),(" Пароль присылаем после бронирования."," Без пароля."),(" Пароль приходит после бронирования."," Приложение бесплатное, пароль не нужен."),
   ("Пароль приходит после подтверждения бронирования. Приложение можно открыть","Приложение бесплатное, пароль не нужен. Его можно открыть"),
   ("С крыши и балкона видно, как течёт вода, иногда проплывают деревянные лодки, а","С крыши и террас видно, как течёт вода, а"),
   (", тексты песен на экране 4K-проектора,",", 4K-проектор,"),("Выбираете песню, текст появляется на большом экране, микрофон идёт по кругу.","Выбираете песню, микрофон идёт по кругу."),
   ("Выбираете песню, текст появляется на экране 4K-проектора, микрофон идёт по кругу.","Выбираете песню, микрофон идёт по кругу."),("Микрофоны, тексты на экране 4K-проектора","Микрофоны и экран 4K-проектора"),
   (", а ещё там гриль и плетёный диван.",", а ещё там гриль."),("У главной спальни свой балкон, а на крытом балконе стоят серые плетёные кресла, плетёная скамья и стеклянный столик.","У главной спальни свой балкон."),
   ("соседи и безопасность.","и соседи."),(", кухня, безопасность и бронирование",", кухня и бронирование"),("Безопасность прежде всего","Практичные мелочи"),("Лестница и безопасность","Лестница"),("Приватность под защитой","Камеры у входа"),("Как получить доступ","Как открыть приложение"),("перил балкона","перил террасы")],
 'fr':[("Une villa","Une maison"),("une villa","une maison"),("Villa","Maison"),("villa","maison"),
   ("vous recevez les informations d'accès et le mot de passe de l'application ASCON Guide.","vous recevez les informations d'accès. L'application ASCON Guide est gratuite, sans mot de passe."),
   ("les indications pour la clé du portail et le mot de passe d'ASCON Guide pour préparer","les indications pour la clé du portail ; l'application gratuite ASCON Guide vous aide à préparer"),
   ("séances ciné en 4K, coffre-fort et caméras uniquement à l'extérieur.","séances ciné en 4K et coffre-fort."),
   ("Après la réservation, vous recevez le mot de passe de l'application ASCON Guide, qui propose","L'application gratuite ASCON Guide propose"),
   ("L'application ASCON Guide pour nos hôtes :","L'application gratuite ASCON Guide :"),(" Mot de passe envoyé après réservation."," Sans mot de passe."),(" Le mot de passe vous est envoyé après la réservation."," Elle est gratuite et sans mot de passe."),
   ("Le mot de passe arrive après la confirmation de la réservation. Vous pouvez ouvrir","L'application est gratuite et sans mot de passe. Vous pouvez l'ouvrir"),
   ("Quand reçoit-on le mot de passe ?","Faut-il un mot de passe ?"),("Après la confirmation de la réservation.","Non. L'application est gratuite et s'ouvre directement dans le navigateur du téléphone."),
   ("Depuis le toit et le balcon, on voit l'eau couler, parfois une barque en bois passer, et","Depuis le toit et les terrasses, on voit l'eau couler et"),
   (", des paroles affichées sur l'écran du vidéoprojecteur 4K,",", d'un vidéoprojecteur 4K,"),("On choisit une chanson, les paroles s'affichent en grand, le micro passe de main en main.","On choisit une chanson, le micro passe de main en main."),
   ("On choisit une chanson, les paroles s'affichent sur l'écran du vidéoprojecteur 4K, le micro tourne.","On choisit une chanson, le micro tourne."),("Micros, paroles sur l'écran du vidéoprojecteur 4K","Micros et vidéoprojecteur 4K"),
   ("Oui, avec micros et paroles à l'écran.","Oui, avec micros de karaoké."),(", avec barbecue et canapé en rotin en prime.",", avec le barbecue en prime."),
   (", voisinage, sécurité.",", voisinage."),(", cuisine, sécurité et réservation",", cuisine et réservation"),("Sécurité avant tout","Côté pratique"),("Escalier et sécurité","Escalier"),("Une intimité préservée","Caméras à l'entrée"),("La sécurité d'abord","Côté pratique"),("rambarde du balcon","rambarde de la terrasse")]})
B.CAMN.update({'vi':'Có camera ngoài trời ở lối vào.','ru':'У входа установлены наружные камеры.','fr':"Des caméras extérieures sont installées à l'entrée."})
B.CAMCELL.update({'vi':'Camera ngoài trời ở lối vào','ru':'Наружные камеры у входа','fr':"Caméras extérieures à l'entrée"})
B.CAM=ext(B.CAM,r'(?i:\bcamera\b|камер|caméra)')
B.DROP=ext(B.DROP,r'lời bài hát|báo khói|chữa cháy|sơ cứu|lối thoát|đèn khẩn cấp|\d+\s*phút|đỗ xe|đậu xe|bãi xe|hồ bơi|bể bơi|thú cưng|gửi hành lý|thẻ từ|khóa thông minh|mật khẩu ứng dụng|nhận mật khẩu|ban công có mái|'
 r'текст[ыа]? песен|датчик[а-я]* дыма|огнетушител|аптечк|аварийн|эвакуац|знак выхода|\d+\s*мин\b|парковк|бассейн|халял|животн|питомц|хранени[ея] багажа|ключ-карт|умн[а-я]+ замок|\bевро\b|пароль от|получу пароль|крыт[а-я]+ балкон|'
 r'paroles|détecteur[s]? de fumée|extincteur|trousse de secours|premiers secours|sortie de secours|éclairage de secours|\d+\s*min\b|parking|stationnement|piscine|animaux|bagagerie|consigne à bagages|carte magnétique|serrure connectée|serrure intelligente|mot de passe d|balcon couvert')
B.DROPQ=ext(B.DROPQ,r'(?i:an toàn|camera trong nhà|trong nhà có camera|безопасн|камеры внутри|камер[ыа]? внутри|sécurité|caméras à l.intérieur)')
B.DROP_SECS=re.compile(B.DROP_SECS.pattern[:-2]+'|An toàn|Безопасность|Sécurité)$')
B.DROP_ROWS=re.compile(B.DROP_ROWS.pattern[:-2]+'|An toàn|Безопасность|Sécurité)$')
B.CAMROW=re.compile(B.CAMROW.pattern[:-2]+'|Camera|Камеры|Caméras)$')
B.PAGE_DROP={'room-outside':ext(B.PAGE_DROP['room-outside'],r'(?i:ban công|ghế mây|sofa mây|\bmây\b|thuyền|ghe|балкон|плетён|ротанг|лодк|balcon|rotin|barque|bateau)'),'room-hallway':ext(B.PAGE_DROP['room-hallway'],r'(?i:ban công|балкон|balcon)')}
B.RV=ext(B.RV,r'(?i:view sông|вид на реку|vue sur la rivière|vue rivière)')
B.RVNEUT.update({'vi':lambda m:'View' if m.group(0)[0]=='V' else 'view','ru':lambda m:'Вид' if m.group(0)[0]=='В' else 'вид','fr':lambda m:'Vue' if m.group(0)[0]=='V' else 'vue'})
B.LOC.update({'vi':('Câu hỏi thường gặp','Hình ảnh'),'ru':('Частые вопросы','Фото'),'fr':('Questions fréquentes','Photos')})
B.FAQSECREN.update({'vi':{'An toàn ra sao?':'Tiện ích khác','An toàn':'Tiện ích khác'},'ru':{'Безопасность':'Другое'},'fr':{'Sécurité':'Divers'}})
vi=json.load(open('content/vi.json'))
B.UI.update({'vi':{k:v for k,v in vi['ui'].items() if k!='motto'},
 'ru':{"skip":"Перейти к содержанию","languages":"Язык","book_airbnb":"Забронировать на Airbnb","book_trip":"Забронировать на Trip.com","whatsapp":"Забронировать через WhatsApp","zalo":"Забронировать через Zalo","address_label":"Адрес","contact_label":"Контакты","more_label":"Ещё","guest_guide":"Приложение-гид для гостей","read_more":"Подробнее","source":"Источник","estimate":"оценка","home":"Главная","not_found_title":"Страница не найдена","not_found_text":"Такой страницы нет. Перейти на главную:"},
 'fr':{"skip":"Aller au contenu","languages":"Langue","book_airbnb":"Réserver sur Airbnb","book_trip":"Réserver sur Trip.com","whatsapp":"Réserver via WhatsApp","zalo":"Réserver via Zalo","address_label":"Adresse","contact_label":"Contact","more_label":"Plus","guest_guide":"Appli guide des voyageurs","read_more":"Lire la suite","source":"Source","estimate":"estimation","home":"Accueil","not_found_title":"Page introuvable","not_found_text":"Cette page n’existe pas. Aller à l’accueil :"}})
B.NAV.update({'vi':['Trang chủ','Ngôi nhà','Sân thượng','Gia đình','Nhóm','Vị trí','Đặt phòng & liên hệ','Hỏi đáp','Nội quy','Cẩm nang','Ứng dụng'],
 'ru':['Главная','Дом','Крыша','Семьям','Группам','Расположение','Бронирование','Вопросы','Правила дома','Путеводитель','Приложение-гид'],
 'fr':['Accueil','La maison','Rooftop','Familles','Groupes','Emplacement','Réservation & contact','FAQ','Règlement','Guide de voyage','Appli guide']})
B.CARD.update({'vi':['Karaoke & giải trí','Phòng khách','Bếp & phòng ăn','Phòng ngủ chính','Phòng ngủ 2','Phòng ngủ 3','Phòng tắm','Hành lang & góc làm việc','Bên ngoài & bờ sông','Sân thượng'],
 'ru':['Караоке и развлечения','Гостиная','Кухня и столовая','Главная спальня','Спальня 2','Спальня 3','Ванные комнаты','Холл и рабочее место','Снаружи и река','Терраса на крыше'],
 'fr':['Karaoké & loisirs','Salon','Cuisine & salle à manger','Chambre principale','Chambre 2','Chambre 3','Salles de bain','Couloir & espace de travail','Extérieur & rivière','Rooftop']})
B.ROOMSH.update({'vi':'Chi tiết từng phòng','ru':'Комнаты подробно','fr':'Les pièces en détail'})
B.FAQH.update({'vi':'Câu hỏi thường gặp','ru':'Частые вопросы','fr':'Questions fréquentes'})
B.ROOMSEC.update({'vi':'Tổng quan căn nhà','ru':'Дом в цифрах','fr':'La maison en bref'})
B.CONTACTH.update({'vi':'Liên hệ','ru':'Контакты','fr':'Contact'})
T,Z,E='<a href="tel:{phone_e164}">{phone}</a>','<a href="https://zalo.me/84909410382" rel="noopener">{phone}</a>','<a href="mailto:{email}">{email}</a>'
B.CONTACT.update({'vi':['Điện thoại và WhatsApp: '+T,'Zalo: '+Z,'Email: '+E],'ru':['Телефон и WhatsApp: '+T,'Zalo: '+Z,'E-mail: '+E],'fr':['Téléphone et WhatsApp : '+T,'Zalo : '+Z,'E-mail : '+E]})
M=B.MAPS
B.MAPSEC.update({'vi':{'h2':'Bản đồ','p':[f'<a href="{M}" rel="noopener">Mở địa chỉ trên Google Maps</a>. Hướng dẫn đến nơi chi tiết được gửi sau khi đặt phòng.']},
 'ru':{'h2':'Карта','p':[f'<a href="{M}" rel="noopener">Открыть адрес в Google Картах</a>. Подробные инструкции по заезду мы отправим после бронирования.']},
 'fr':{'h2':'Carte','p':[f'<a href="{M}" rel="noopener">Ouvrir l’adresse dans Google Maps</a>. Les instructions d’arrivée détaillées sont envoyées après la réservation.']}})
B.APPBTN.update({'vi':'Mở ứng dụng cẩm nang','ru':'Открыть приложение-гид','fr':'Ouvrir l’appli guide'})
vtg=[s for s in vi['pages']['home']['sections'] if s.get('_tg')][0]
B.TG.update({'vi':{'h2':vtg['h2'],'p':vtg['p'][0],'card':vtg['cards'][0][::2]},
 'ru':{'h2':'Бесплатное приложение-гид','p':'Планируйте дни с бесплатным приложением-гидом ASCON: местные советы, где поесть и что посмотреть, карта — прямо в браузере телефона.','card':['Бесплатное приложение-гид','Местные советы и карта Хошимина, бесплатно в браузере телефона.']},
 'fr':{'h2':'Appli guide de voyage gratuite','p':'Préparez vos journées avec l’appli guide gratuite d’ASCON : bons plans locaux, adresses pour manger et visiter, et une carte, directement dans le navigateur du téléphone.','card':['Appli guide gratuite','Bons plans et carte de Hô Chi Minh-Ville, gratuits dans le navigateur.']}})
vh=vi['pages']['house']
B.HOUSE.update({'vi':{k:vh[k] for k in ('title','description','h1','lead')},
 'ru':dict(title='Дом в Хошимине: все комнаты по порядку | ASCON',description='Три этажа и крыша: 3 спальни со своими ванными, гостиная около 40 м², полностью оборудованная кухня и комната караоке с 4K-проектором.',h1='Дом: ваше жильё в Хошимине, комната за комнатой',lead='Три этажа, терраса на крыше и более 250 м², которые принадлежат только вашей компании. Здесь фото и оснащение каждой комнаты.'),
 'fr':dict(title='Maison entière à Saigon, pièce par pièce | ASCON',description='Trois étages et un toit-terrasse : 3 chambres avec salle de bain, salon d’environ 40 m², cuisine équipée et salle de karaoké avec vidéoprojecteur 4K.',h1='La maison : votre location à Saigon, pièce par pièce',lead='Trois étages, un toit-terrasse et plus de 250 m² rien que pour votre groupe. Voici les photos et l’équipement de chaque pièce.')})
B.OUTSIDE.update({'vi':dict(description='Nhà nguyên căn ven sông ở Sài Gòn: hiên lan can trắng có mái che, nhìn ra sông và đường chân trời Quận 1.'),
 'ru':dict(description='Дом на берегу реки в Хошимине: терраса с белыми перилами и навесом, вид на реку и небоскрёбы 1-го района.'),
 'fr':dict(description='Maison au bord de la rivière à Saigon : terrasse à rambarde blanche avec auvent, vue sur la rivière et les tours du District 1.')})
vt=vi['pages']['travel-guide']
B.TGP.update({'ru':dict(title='Бесплатное приложение-гид по Хошимину | ASCON',description='Бесплатное приложение-гид ASCON: местные советы, где поесть и что посмотреть, карта и практическая помощь в Хошимине. Открывается в браузере телефона.',h1='Бесплатное приложение-гид по Хошимину',lead='ASCON Guide — бесплатное веб-приложение с местными советами и интересными местами Хошимина. Открывается прямо в браузере телефона: без пароля и без установки.',
   h2a='Как выглядит приложение',pa='Это настоящие скриншоты приложения на телефоне (русского языка в приложении пока нет, поэтому экраны на английском).',caps=['Экран приветствия с логотипом и девизом ASCON LIVING','Выбор языка: приложение доступно на десяти языках','Категории: еда, кафе, бары, семейные прогулки и другое','Карта мест вокруг дома','Практическая информация и экстренная помощь'],
   h2b='Местные советы и места',pb=['Места разложены по понятным категориям: еда, кафе и десерты, бары и ночная жизнь, дети и семья, достопримечательности и культура, активности, отдых, шопинг, поездки на день, а также практическая и экстренная информация. Карта показывает места вокруг дома, а кнопка «Маршрут» открывает навигацию.','Приложение можно добавить на главный экран. Больше идей — в нашем <a href="{L}guide/">путеводителе по Хошимину</a>.']),
 'fr':dict(title='Appli guide gratuite pour Hô Chi Minh-Ville | ASCON',description='L’appli guide gratuite d’ASCON : bons plans locaux, restaurants et visites, carte et aide pratique à Hô Chi Minh-Ville. S’ouvre dans le navigateur du téléphone.',h1='Appli guide de voyage gratuite pour Hô Chi Minh-Ville',lead='ASCON Guide est une appli web gratuite avec des bons plans et des adresses à Hô Chi Minh-Ville. Elle s’ouvre directement dans le navigateur du téléphone : sans mot de passe, rien à installer.',
   h2a='Un aperçu de l’appli',pa='Voici de vraies captures d’écran de l’appli sur un téléphone.',caps=['Écran d’accueil avec le logo et la devise d’ASCON LIVING','Choix de la langue : l’appli existe en dix langues','Catégories : cuisine, cafés, bars, sorties en famille et plus','Carte des lieux autour de la maison','Infos pratiques et aide en cas d’urgence'],
   h2b='Bons plans et adresses',pb=['Les lieux sont classés par catégories : cuisine, cafés et desserts, bars et vie nocturne, enfants et famille, sites et culture, activités, détente, shopping, excursions d’une journée, ainsi qu’infos pratiques et urgences. La carte montre les lieux autour de la maison, et un appui sur Itinéraire ouvre le guidage.','Vous pouvez ajouter l’appli à l’écran d’accueil. D’autres idées dans notre <a href="{L}guide/">guide de voyage de Hô Chi Minh-Ville</a>.'])})
B.RULES.update({'vi':{'h2':'Quy định cơ bản','flow':[['ul',['Nhận phòng 14:00–23:00, trả phòng 12:00.','Theo luật Việt Nam, khách lưu trú cần đăng ký tạm trú.','Không hút thuốc trong nhà; chỉ hút ở khu vực ngoài trời được chỉ định.','Mở nhạc lớn đến 21:30.','Không tổ chức tiệc tùng ồn ào.','Chỉ khách đã đăng ký được lưu trú.']]]},
 'ru':{'h2':'Основные правила','flow':[['ul',['Заезд 14:00–23:00, выезд до 12:00.','По законам Вьетнама гостей необходимо зарегистрировать.','В доме не курят; курить можно только в отведённых местах на улице.','Громкая музыка — до 21:30.','Никаких шумных вечеринок.','Проживать могут только зарегистрированные гости.']]]},
 'fr':{'h2':'Règles de base','flow':[['ul',['Arrivée 14h00–23h00, départ 12h00.','L’enregistrement des voyageurs est obligatoire selon la loi vietnamienne.','Non-fumeur à l’intérieur ; fumer uniquement dans les espaces extérieurs prévus.','Musique forte jusqu’à 21h30.','Pas de fêtes bruyantes.','Seuls les voyageurs enregistrés peuvent séjourner.']]]}})
B.KWCAP.update({'vi':[("trong nhà nguyên căn Quận 7:","trong nhà:"),("Vì sao chọn Quận 7","Vì sao chọn khu này"),("Quận 7 có nhịp chậm hơn","Khu này có nhịp chậm hơn"),("Quận 7, TP.HCM.","TP.HCM.")],
 'fr':[("dans une maison du District 7 de Saigon :","dans la maison :"),("dans une maison du District 7 :","dans la maison :"),("Pourquoi le District 7","Pourquoi ce quartier"),("Le District 7 vit","Le quartier vit"),("District 7, Hô Chi Minh-Ville.","Hô Chi Minh-Ville.")],
 'ru':[("в доме в 7-м районе Хошимина:","в доме:"),("в доме в 7-м районе:","в доме:"),("Почему 7-й район","Почему этот район"),("7-й район живёт","Этот район живёт"),("District 7, Хошимин.","Хошимин.")]})
LANGS=('vi','fr','ru')
def run(l):
    if l=='vi':
        old=json.load(open('content/vi.json'))
        B.TGP['vi']=None
        B.build(l)
        d=json.load(open('content/vi.json'))
        d['pages']['travel-guide']=old['pages']['travel-guide']
        for k in ('imprint','privacy','guide-family','guide-airport','guide-app'): d['pages'][k]=old['pages'][k]
        for sec in d['pages']['guide-airport']['sections']:
            if sec.get('h2')=='Thời gian di chuyển': sec['p']=['Thời gian đi ô tô phụ thuộc nhiều vào giao thông; nên dự trù thêm thời gian, nhất là vào giờ cao điểm.']
        json.dump(d,open('content/vi.json','w'),ensure_ascii=False,indent=1)
    else: B.build(l)
if __name__=='__main__':
    for l in (sys.argv[1:] or LANGS): run(l)
    for x in B.LOG: print(*x,sep=' | ')
