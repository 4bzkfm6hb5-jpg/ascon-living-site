"""Trust signals: Organization JSON-LD, host section, legal name in footer. Facts only from facts.json / owner brief."""
import html
LEGAL='CONG TY TNHH ASCON LIVING VIET NAM'
# (menu label, heading, text, languages, reviews link)
ABOUT={
'en':('About us','About the host','Your host is Zishan. ASCON LIVING is run by CONG TY TNHH ASCON LIVING VIET NAM, and Zishan looks after every stay personally.','Languages: German, English, Hindi, Punjabi, Urdu, Vietnamese','Read our Google reviews'),
'de':('Über uns','Über den Gastgeber','Dein Gastgeber ist Zishan. ASCON LIVING wird von der CONG TY TNHH ASCON LIVING VIET NAM betrieben, und Zishan kümmert sich persönlich um jeden Aufenthalt.','Sprachen: Deutsch, Englisch, Hindi, Punjabi, Urdu, Vietnamesisch','Unsere Google-Bewertungen lesen'),
'vi':('Về chúng tôi','Về chủ nhà','Chủ nhà của bạn là Zishan. ASCON LIVING do CONG TY TNHH ASCON LIVING VIET NAM vận hành, và Zishan trực tiếp chăm lo cho từng kỳ lưu trú.','Ngôn ngữ: tiếng Đức, tiếng Anh, tiếng Hindi, tiếng Punjab, tiếng Urdu, tiếng Việt','Xem đánh giá Google của chúng tôi'),
'zh':('关于我们','关于房东','您的房东是 Zishan。ASCON LIVING 由 CONG TY TNHH ASCON LIVING VIET NAM 运营，Zishan 亲自照顾每一次入住。','语言：德语、英语、印地语、旁遮普语、乌尔都语、越南语','查看我们的 Google 评价'),
'zh-tw':('關於我們','關於房東','您的房東是 Zishan。ASCON LIVING 由 CONG TY TNHH ASCON LIVING VIET NAM 經營，Zishan 親自照顧每一次入住。','語言：德語、英語、印地語、旁遮普語、烏爾都語、越南語','查看我們的 Google 評價'),
'hi':('हमारे बारे में','मेज़बान के बारे में','आपके मेज़बान Zishan हैं। ASCON LIVING का संचालन CONG TY TNHH ASCON LIVING VIET NAM करती है, और Zishan हर ठहराव का ध्यान ख़ुद रखते हैं।','भाषाएँ: जर्मन, अंग्रेज़ी, हिन्दी, पंजाबी, उर्दू, वियतनामी','हमारी Google समीक्षाएँ पढ़ें'),
'es':('Sobre nosotros','Sobre el anfitrión','Tu anfitrión es Zishan. ASCON LIVING está gestionado por CONG TY TNHH ASCON LIVING VIET NAM, y Zishan se ocupa personalmente de cada estancia.','Idiomas: alemán, inglés, hindi, panyabí, urdu, vietnamita','Leer nuestras reseñas de Google'),
'ar':('من نحن','عن المضيف','مضيفك هو Zishan. تدير ASCON LIVING شركة CONG TY TNHH ASCON LIVING VIET NAM، ويهتم Zishan شخصيًا بكل إقامة.','اللغات: الألمانية، الإنجليزية، الهندية، البنجابية، الأردية، الفيتنامية','اقرأ تقييماتنا على Google'),
'fr':('À propos','À propos de l’hôte','Votre hôte est Zishan. ASCON LIVING est exploité par CONG TY TNHH ASCON LIVING VIET NAM, et Zishan s’occupe personnellement de chaque séjour.','Langues : allemand, anglais, hindi, pendjabi, ourdou, vietnamien','Lire nos avis Google'),
'pt':('Sobre nós','Sobre o anfitrião','Seu anfitrião é Zishan. O ASCON LIVING é administrado pela CONG TY TNHH ASCON LIVING VIET NAM, e Zishan cuida pessoalmente de cada estadia.','Idiomas: alemão, inglês, hindi, punjabi, urdu, vietnamita','Leia nossas avaliações no Google'),
'ru':('О нас','О хозяине','Ваш хозяин — Zishan. ASCON LIVING управляет компания CONG TY TNHH ASCON LIVING VIET NAM, и Zishan лично заботится о каждом проживании.','Языки: немецкий, английский, хинди, панджаби, урду, вьетнамский','Читать наши отзывы в Google'),
'ur':('ہمارے بارے میں','میزبان کے بارے میں','آپ کے میزبان Zishan ہیں۔ ASCON LIVING کو CONG TY TNHH ASCON LIVING VIET NAM چلاتی ہے، اور Zishan ہر قیام کا خیال خود رکھتے ہیں۔','زبانیں: جرمن، انگریزی، ہندی، پنجابی، اردو، ویتنامی','ہمارے Google ریویوز پڑھیں'),
'id':('Tentang kami','Tentang tuan rumah','Tuan rumah Anda adalah Zishan. ASCON LIVING dikelola oleh CONG TY TNHH ASCON LIVING VIET NAM, dan Zishan mengurus setiap masa inap secara pribadi.','Bahasa: Jerman, Inggris, Hindi, Punjabi, Urdu, Vietnam','Baca ulasan Google kami'),
'ja':('私たちについて','ホストについて','ホストは Zishan です。ASCON LIVING は CONG TY TNHH ASCON LIVING VIET NAM が運営しており、Zishan がすべての滞在を自ら担当します。','対応言語：ドイツ語、英語、ヒンディー語、パンジャーブ語、ウルドゥー語、ベトナム語','Google のレビューを読む'),
'ko':('소개','호스트 소개','호스트는 Zishan입니다. ASCON LIVING은 CONG TY TNHH ASCON LIVING VIET NAM이 운영하며, Zishan이 모든 숙박을 직접 챙깁니다.','언어: 독일어, 영어, 힌디어, 펀자브어, 우르두어, 베트남어','Google 리뷰 보기'),
'pa':('ਸਾਡੇ ਬਾਰੇ','ਮੇਜ਼ਬਾਨ ਬਾਰੇ','ਤੁਹਾਡੇ ਮੇਜ਼ਬਾਨ Zishan ਹਨ। ASCON LIVING ਨੂੰ CONG TY TNHH ASCON LIVING VIET NAM ਚਲਾਉਂਦੀ ਹੈ, ਅਤੇ Zishan ਹਰ ਠਹਿਰ ਦਾ ਖ਼ਿਆਲ ਆਪ ਰੱਖਦੇ ਹਨ।','ਭਾਸ਼ਾਵਾਂ: ਜਰਮਨ, ਅੰਗਰੇਜ਼ੀ, ਹਿੰਦੀ, ਪੰਜਾਬੀ, ਉਰਦੂ, ਵੀਅਤਨਾਮੀ','ਸਾਡੀਆਂ Google ਸਮੀਖਿਆਵਾਂ ਪੜ੍ਹੋ'),
'th':('เกี่ยวกับเรา','เกี่ยวกับเจ้าของที่พัก','เจ้าของที่พักของคุณคือ Zishan ASCON LIVING ดำเนินการโดย CONG TY TNHH ASCON LIVING VIET NAM และ Zishan ดูแลทุกการเข้าพักด้วยตนเอง','ภาษา: เยอรมัน อังกฤษ ฮินดี ปัญจาบ อูรดู เวียดนาม','อ่านรีวิวของเราบน Google'),
'ms':('Tentang kami','Tentang tuan rumah','Tuan rumah anda ialah Zishan. ASCON LIVING dikendalikan oleh CONG TY TNHH ASCON LIVING VIET NAM, dan Zishan menjaga setiap penginapan sendiri.','Bahasa: Jerman, Inggeris, Hindi, Punjabi, Urdu, Vietnam','Baca ulasan Google kami'),
'it':('Chi siamo','L’host','Il tuo host è Zishan. ASCON LIVING è gestito da CONG TY TNHH ASCON LIVING VIET NAM e Zishan segue personalmente ogni soggiorno.','Lingue: tedesco, inglese, hindi, punjabi, urdu, vietnamita','Leggi le nostre recensioni Google'),
'nl':('Over ons','Over de host','Je host is Zishan. ASCON LIVING wordt beheerd door CONG TY TNHH ASCON LIVING VIET NAM, en Zishan zorgt persoonlijk voor elk verblijf.','Talen: Duits, Engels, Hindi, Punjabi, Urdu, Vietnamees','Lees onze Google-reviews'),
'tr':('Hakkımızda','Ev sahibi hakkında','Ev sahibiniz Zishan. ASCON LIVING, CONG TY TNHH ASCON LIVING VIET NAM tarafından işletilir ve Zishan her konaklamayla bizzat ilgilenir.','Diller: Almanca, İngilizce, Hintçe, Pencapça, Urduca, Vietnamca','Google yorumlarımızı okuyun'),
'pl':('O nas','O gospodarzu','Twoim gospodarzem jest Zishan. ASCON LIVING prowadzi CONG TY TNHH ASCON LIVING VIET NAM, a Zishan osobiście dba o każdy pobyt.','Języki: niemiecki, angielski, hindi, pendżabski, urdu, wietnamski','Przeczytaj nasze opinie w Google'),
'sv':('Om oss','Om värden','Din värd är Zishan. ASCON LIVING drivs av CONG TY TNHH ASCON LIVING VIET NAM, och Zishan tar personligen hand om varje vistelse.','Språk: tyska, engelska, hindi, punjabi, urdu, vietnamesiska','Läs våra Google-omdömen'),
}
def t(code): return ABOUT.get(code, ABOUT['en'])
def nav_link(code, home_url):
    return f'<a href="{home_url}#about-host">{html.escape(t(code)[0])}</a>'
def section(code):
    _,h,p,langs,rev=t(code)
    return (f'<section class="about-host" id="about-host"><h2>{html.escape(h)}</h2><p>{html.escape(p)}</p>'
            f'<p>{html.escape(langs)}</p><p><a href="#guest-reviews">{html.escape(rev)} ★★★★★</a></p></section>')
def org_ld(F, SITE):
    same=[F['airbnb'], F['trip']]
    return {"@context":"https://schema.org","@type":["Organization","LodgingBusiness"],"@id":SITE+'/#organization',
      "name":F['name'],"legalName":LEGAL,"url":SITE+'/',"logo":SITE+'/assets/img/logo-mark.png',"image":SITE+'/assets/img/og.jpg',
      "telephone":F['phone_e164'],"email":F['email'],
      "address":{"@type":"PostalAddress","streetAddress":F['street'],"addressLocality":"Tân Hưng","addressRegion":"Ho Chi Minh City","addressCountry":"VN"},
      "geo":{"@type":"GeoCoordinates","latitude":10.7516358,"longitude":106.7103995},
      "founder":{"@type":"Person","name":"Zishan","knowsLanguage":["de","en","hi","pa","ur","vi"]},
      "knowsLanguage":["de","en","hi","pa","ur","vi"],"sameAs":same}
def footer_legal():
    return f'{LEGAL}<br>'
