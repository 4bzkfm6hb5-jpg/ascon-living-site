"""ES / PT (pt-BR) / IT / HI from MR texts: extends tools/build_cjk.py (same pipeline and rules).
HI keeps its existing ui, imprint, privacy, guide subpages and travel-guide page (EN app screenshots)."""
import re,sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
import build_cjk as B
import build_sea, build_vrf  # noqa: shared pattern extensions
def ext(rx,more): return re.compile(rx.pattern+'|'+more,rx.flags)
R=re.compile
B.REP.update({
 'es':[("Villa en Saigón","Casa en Saigón"),("Villa en Ho Chi Minh","Casa en Ho Chi Minh"),("Una villa","Una casa"),("una villa","una casa"),("Villa","Casa"),("villa","casa"),
   ("Sí, con micrófonos y letras en pantalla.","Sí, con micrófonos de karaoke."),(", las letras se ven en la pantalla del proyector 4K,"," y un proyector 4K,"),
   ("con barbacoa y sofá de ratán incluidos.","con barbacoa incluida."),("Sí, el dormitorio principal tiene balcón y hay un balcón cubierto con sillones de ratán.","Sí, el dormitorio principal tiene balcón."),
   (", cine en 4K, caja fuerte y cámaras solo en el exterior.",", cine en 4K y caja fuerte."),
   ("Contraseña tras la reserva.","Gratis, sin contraseña."),("La contraseña llega después de reservar.","La app es gratuita y no necesita contraseña."),
   ("Tras la confirmación recibes los datos de acceso y la contraseña de la aplicación ASCON Guide.","Tras la confirmación recibes los datos de acceso. La aplicación ASCON Guide es gratuita y no necesita contraseña."),
   ("¿Cuándo recibo la contraseña?","¿La app necesita contraseña?"),("La contraseña se envía tras confirmar la reserva.","No. Es gratuita y se abre directamente en el navegador del móvil."),
   ("Después de reservar recibes la contraseña de la aplicación ASCON Guide, con","La aplicación gratuita ASCON Guide tiene"),
   ("Recibes el código de la puerta, las indicaciones de la llave de la verja y la contraseña de ASCON Guide para preparar","Recibes el código de la puerta y las indicaciones de la llave de la verja; con la app gratuita ASCON Guide puedes preparar")],
 'pt':[("Villa em","Casa em"),("Uma villa","Uma casa"),("uma villa","uma casa"),("Villa","Casa"),("villa","casa"),
   ("Tem, com microfones e letras na tela.","Tem, com microfones de karaokê."),(", as letras aparecem na tela do projetor 4K,"," e um projetor 4K,"),
   (", sofá de rattan e luzes solares."," e luzes solares."),("O quarto principal tem varanda própria, e há uma varanda coberta com poltronas de rattan.","O quarto principal tem varanda própria."),
   (", cinema em 4K, cofre e câmeras só na área externa.",", cinema em 4K e cofre."),
   ("A senha chega depois da reserva.","O app é gratuito e não precisa de senha."),("Senha enviada após a reserva.","Gratuito, sem senha."),
   ("Depois da confirmação, você recebe os dados de acesso e a senha do aplicativo ASCON Guide.","Depois da confirmação, você recebe os dados de acesso. O aplicativo ASCON Guide é gratuito e não precisa de senha."),
   ("Quando recebo a senha?","O app precisa de senha?"),("A senha é enviada depois que a reserva é confirmada.","Não. É gratuito e abre direto no navegador do celular."),
   ("Depois da reserva você recebe a senha do aplicativo ASCON Guide, com","O aplicativo gratuito ASCON Guide tem"),
   ("Você recebe a senha da porta, as instruções da chave do portão e a senha do ASCON Guide para planejar","Você recebe a senha da porta e as instruções da chave do portão; com o app gratuito ASCON Guide dá para planejar")],
 'it':[("villa sul fiume","casa sul fiume"),("Villa a Saigon","Casa a Saigon"),("Villa intera","Casa intera"),("Una villa","Una casa"),("una villa","una casa"),("Villa","Casa"),("villa","casa"),
   ("Sì, con microfoni e testi sullo schermo.","Sì, con microfoni per il karaoke."),
   (", divano in rattan e luci solari."," e luci solari."),("La camera padronale ha il suo balcone e c'è anche un balcone coperto con poltrone in rattan.","La camera padronale ha il suo balcone."),
   ("Password inviata dopo la prenotazione.","Gratuita, senza password."),("La password arriva dopo la prenotazione.","L'app è gratuita e non serve una password."),
   ("Dopo la conferma ricevete i dati di accesso e la password dell'app ASCON Guide.","Dopo la conferma ricevete i dati di accesso. L'app ASCON Guide è gratuita e senza password."),
   ("Quando ricevo la password?","Serve una password per l'app?"),("Appena confermata la prenotazione ricevete la password.","No. È gratuita e si apre direttamente nel browser del telefono."),
   ("Dopo la conferma della prenotazione ricevete il codice della porta, le indicazioni per la chiave del cancello e la password dell'app ASCON Guide, con mappa e consigli pratici.","Dopo la conferma della prenotazione ricevete il codice della porta e le indicazioni per la chiave del cancello. L'app gratuita ASCON Guide offre mappa e consigli pratici."),
   ("Dopo la prenotazione ricevete la password dell'app ASCON Guide:","L'app gratuita ASCON Guide offre:"),
   ("Ricevete il codice della porta, le indicazioni per la chiave del cancello e la password di ASCON Guide, per pianificare","Ricevete il codice della porta e le indicazioni per la chiave del cancello; con l'app gratuita ASCON Guide potete pianificare")],
 'hi':[("लॉन्ड्री सर्विस","लॉन्ड्री सर्विस (30 EUR प्रति लोड)"),("Ho Chi Minh villa ग्रुप के लिए: कराओके, BBQ","Ho Chi Minh में ग्रुप के लिए घर: कराओके, BBQ"),
   ("गाना चुनिए, बोल 4K प्रोजेक्टर की स्क्रीन पर आते हैं और माइक एक हाथ से दूसरे हाथ जाता है।","गाना चुनिए और माइक एक हाथ से दूसरे हाथ जाता है।"),
   ("हाँ, माइक और स्क्रीन पर गानों के बोल के साथ।","हाँ, कराओके माइक के साथ।"),("हाँ, माइक और स्क्रीन पर बोल के साथ।","हाँ, कराओके माइक के साथ।"),
   ("माइक घर में हैं और गाने के बोल 4K प्रोजेक्टर की स्क्रीन पर आते हैं।","माइक घर में हैं, साथ में 4K प्रोजेक्टर भी है।"),
   ("स्मोकर वाला काला बैरल बारबेक्यू, रतन सोफ़ा और सोलर लाइट के साथ।","स्मोकर वाला काला बैरल बारबेक्यू और सोलर लाइट के साथ।"),
   ("हाँ। मास्टर बेडरूम की अपनी बालकनी है, और रतन कुर्सियों वाली एक ढकी हुई बालकनी भी है।","हाँ। मास्टर बेडरूम की अपनी बालकनी है।"),
   ("पक्का होने के बाद आपको एंट्री की जानकारी और ASCON Guide ऐप का पासवर्ड मिलता है।","पक्का होने के बाद आपको एंट्री की जानकारी मिलती है। ASCON Guide ऐप मुफ़्त है, पासवर्ड की ज़रूरत नहीं।"),
   ("पासवर्ड बुकिंग के बाद मिलता है।","ऐप मुफ़्त है, पासवर्ड की ज़रूरत नहीं।"),("बुकिंग के बाद पासवर्ड मिलता है.","मुफ़्त, पासवर्ड की ज़रूरत नहीं."),
   ("बुकिंग के बाद आपको ASCON Guide ऐप का पासवर्ड मिलता है:","मुफ़्त ASCON Guide ऐप में:"),
   ("पासवर्ड कब मिलेगा?","क्या ऐप के लिए पासवर्ड चाहिए?"),("बुकिंग पक्की होते ही आपको पासवर्ड भेजा जाता है।","नहीं। ऐप मुफ़्त है और फ़ोन के ब्राउज़र में सीधे खुलता है।"),
   ("बुकिंग पक्की होने के बाद आपको दरवाज़े का कोड, गेट की चाबी की जानकारी और ASCON Guide ऐप का पासवर्ड मिलता है, जिसमें मैप और ज़रूरी टिप्स हैं।","बुकिंग पक्की होने के बाद आपको दरवाज़े का कोड और गेट की चाबी की जानकारी मिलती है। मुफ़्त ASCON Guide ऐप में मैप और ज़रूरी टिप्स हैं।")]})
B.CAMX['it']=R(r'(?i:telecamer)')
B.CAMN.update({'es':'Hay cámaras exteriores en la entrada.','pt':'Há câmeras externas na entrada.','it':"All'ingresso ci sono telecamere esterne.",'hi':'प्रवेश द्वार पर बाहरी कैमरे लगे हैं।'})
B.CAMCELL.update({'es':'Cámaras exteriores en la entrada','pt':'Câmeras externas na entrada','it':"Telecamere esterne all'ingresso",'hi':'प्रवेश द्वार पर बाहरी कैमरे'})
B.CAM=ext(B.CAM,r'(?i:cámara|câmera|camera|telecamer|कैमरा|कैमरे)')
B.DROP=ext(B.DROP,r'(?i:letras de (?:las )?canciones|letras (?:das|de) músicas?|\bletras\b|testi delle canzoni|\btesti\b|लिरिक्स|गीत के बोल|\bबोल\b|'
 r'detector(?:es)? de humo|detector(?:es)? de fumaça|rilevator[ei] di fumo|extintor|estintor[ei]|botiquín|primeiros socorros|kit de primeiros|pronto soccorso|primeros auxilios|salida de emergencia|saída de emergência|uscita di emergenza|luz de emergencia|luz de emergência|luci di emergenza|illuminazione di emergenza|'
 r'स्मोक डिटेक्टर|धुएँ|धुआँ|अग्निशामक|फ़ायर एक्सटिंग्विशर|फर्स्ट[- ]एड|फ़र्स्ट[- ]एड|प्राथमिक चिकित्सा|इमरजेंसी|आपातकालीन|'
 r'\d+\s*(?:minutos?|minuti|मिनट)\b|aparcamiento|estacionamiento|estacionamento|parcheggio|पार्किंग|piscina|स्विमिंग|mascota|animais de estimação|animali domestici|पालतू|consigna de equipaje|guarda-volumes|deposito bagagli|सामान रख|'
 r'contraseña de la app|senha do app|password dell.app|ऐप (?:का|के) पासवर्ड|पासवर्ड भेज|recibirás la contraseña|receberá a senha|riceverete la password|riceverai la password|balcón cubierto|varanda coberta|balcone coperto)')
B.DROPQ=ext(B.DROPQ,r'(?i:seguridad|segurança|sicurezza|सुरक्षा|cámaras dentro|cámaras en el interior|câmeras dentro|câmeras na parte interna|telecamere all.interno|telecamere dentro|अंदर कैमरा|घर के अंदर कैमरे)')
B.DROP_SECS=R(B.DROP_SECS.pattern[:-2]+'|Seguridad|Segurança|Sicurezza|सुरक्षा)$')
B.DROP_ROWS=R(B.DROP_ROWS.pattern[:-2]+'|Seguridad|Segurança|Sicurezza|सुरक्षा)$')
B.CAMROW=R(B.CAMROW.pattern[:-2]+'|Cámaras|Câmeras|Telecamere|कैमरे|कैमरा)$')
B.PAGE_DROP={'room-outside':ext(B.PAGE_DROP['room-outside'],r'(?i:balc[oó]n|balcone|varanda|sacada|ratán|rattan|vime|barca|barco|barche|bote|बालकनी|रतन|बेंत|नाव)'),'room-hallway':ext(B.PAGE_DROP['room-hallway'],r'(?i:balc[oó]n|balcone|varanda|sacada|बालकनी)')}
B.RV=ext(B.RV,r'(?i:vistas? al río|vistas? del río|vista para o rio|vista do rio|vista sul fiume|vista fiume|नदी का नज़ारा|नदी के नज़ारे|रिवर व्यू)')
cap=lambda w:(lambda m:w[0].upper()+w[1:] if m.group(0)[0].isupper() else w)
B.RVNEUT.update({'es':cap('vista'),'pt':cap('vista'),'it':cap('vista'),'hi':'नज़ारा'})
B.SPLIT['hi']=R(r'.+?(?:[!?।]+\s*|\.(?:\s+|$)|$)')
B.LOC.update({'es':('Preguntas frecuentes','Fotos'),'pt':('Perguntas frequentes','Fotos'),'it':('Domande frequenti','Immagini'),'hi':('अक्सर पूछे जाने वाले सवाल','तस्वीरें')})
B.FAQSECREN.update({'es':{'Seguridad':'Otros'},'pt':{'Segurança':'Outros'},'it':{'Sicurezza':'Altro'},'hi':{'सुरक्षा':'अन्य'}})
hi=json.load(open('content/hi.json'))
def ui(skip,lang,air,trip,wa,za,addr,cont,more,gg,rm,src,est,home,nft,nfx): return dict(skip=skip,languages=lang,book_airbnb=air,book_trip=trip,whatsapp=wa,zalo=za,address_label=addr,contact_label=cont,more_label=more,guest_guide=gg,read_more=rm,source=src,estimate=est,home=home,not_found_title=nft,not_found_text=nfx)
B.UI.update({'hi':{k:v for k,v in hi['ui'].items() if k!='motto'},
 'es':ui('Ir al contenido','Idioma','Reservar en Airbnb','Reservar en Trip.com','Reservar por WhatsApp','Reservar por Zalo','Dirección','Contacto','Más','App guía para huéspedes','Leer más','Fuente','estimación','Inicio','Página no encontrada','Esta página no existe. Ir al inicio:'),
 'pt':ui('Pular para o conteúdo','Idioma','Reservar no Airbnb','Reservar no Trip.com','Reservar pelo WhatsApp','Reservar pelo Zalo','Endereço','Contato','Mais','App guia para hóspedes','Leia mais','Fonte','estimativa','Início','Página não encontrada','Esta página não existe. Ir para o início:'),
 'it':ui('Vai al contenuto','Lingua','Prenota su Airbnb','Prenota su Trip.com','Prenota su WhatsApp','Prenota su Zalo','Indirizzo','Contatti','Altro','App guida per gli ospiti','Leggi di più','Fonte','stima','Home','Pagina non trovata','Questa pagina non esiste. Vai alla home:')})
B.NAV.update({'es':['Inicio','La casa','Azotea','Familias','Grupos','Ubicación','Reserva y contacto','Preguntas frecuentes','Normas','Guía de viaje','App guía'],
 'pt':['Início','A casa','Terraço','Famílias','Grupos','Localização','Reserva e contato','Perguntas frequentes','Regras','Guia de viagem','App guia'],
 'it':['Home','La casa','Terrazza','Famiglie','Gruppi','Posizione','Prenota e contatti','Domande frequenti','Regole','Guida di viaggio','App guida'],
 'hi':['होम','घर','रूफ़टॉप','परिवार','ग्रुप','लोकेशन','बुकिंग और संपर्क','सवाल-जवाब','घर के नियम','ट्रैवल गाइड','गाइड ऐप']})
B.CARD.update({'es':['Karaoke y ocio','Salón','Cocina y comedor','Dormitorio principal','Dormitorio 2','Dormitorio 3','Baños','Pasillo y zona de trabajo','Exterior y río','Azotea'],
 'pt':['Karaokê e lazer','Sala de estar','Cozinha e sala de jantar','Quarto principal','Quarto 2','Quarto 3','Banheiros','Corredor e espaço de trabalho','Área externa e rio','Terraço'],
 'it':['Karaoke e svago','Soggiorno','Cucina e zona pranzo','Camera principale','Camera 2','Camera 3','Bagni','Corridoio e angolo lavoro','Esterno e fiume','Terrazza'],
 'hi':['कराओके और मनोरंजन','लिविंग रूम','किचन और डाइनिंग','मास्टर बेडरूम','बेडरूम 2','बेडरूम 3','बाथरूम','हॉलवे और वर्कस्पेस','बाहर और नदी','रूफ़टॉप टैरेस']})
B.ROOMSH.update({'es':'Las estancias en detalle','pt':'Os ambientes em detalhe','it':'Gli ambienti nel dettaglio','hi':'हर कमरा विस्तार से'})
B.FAQH.update({'es':'Preguntas frecuentes','pt':'Perguntas frequentes','it':'Domande frequenti','hi':'अक्सर पूछे जाने वाले सवाल'})
B.ROOMSEC.update({'es':'La casa de un vistazo','pt':'A casa em números','it':'La casa in breve','hi':'घर एक नज़र में'})
B.CONTACTH.update({'es':'Contacto','pt':'Contato','it':'Contatti','hi':'संपर्क'})
T,Z,E=build_vrf.T,build_vrf.Z,build_vrf.E
B.CONTACT.update({'es':['Teléfono y WhatsApp: '+T,'Zalo: '+Z,'Correo: '+E],'pt':['Telefone e WhatsApp: '+T,'Zalo: '+Z,'E-mail: '+E],'it':['Telefono e WhatsApp: '+T,'Zalo: '+Z,'E-mail: '+E],'hi':['फ़ोन और WhatsApp: '+T,'Zalo: '+Z,'ईमेल: '+E]})
M=B.MAPS
B.MAPSEC.update({'es':{'h2':'Mapa','p':[f'<a href="{M}" rel="noopener">Abrir la dirección en Google Maps</a>. Las instrucciones de llegada detalladas se envían después de reservar.']},
 'pt':{'h2':'Mapa','p':[f'<a href="{M}" rel="noopener">Abrir o endereço no Google Maps</a>. As instruções detalhadas de chegada são enviadas após a reserva.']},
 'it':{'h2':'Mappa','p':[f'<a href="{M}" rel="noopener">Apri l’indirizzo su Google Maps</a>. Le istruzioni dettagliate per l’arrivo vengono inviate dopo la prenotazione.']},
 'hi':{'h2':'नक्शा','p':[f'<a href="{M}" rel="noopener">Google Maps में पता खोलें</a>। पहुँचने के विस्तृत निर्देश बुकिंग के बाद भेजे जाते हैं।']}})
B.APPBTN.update({'es':'Abrir la app guía','pt':'Abrir o app guia','it':'Apri l’app guida','hi':'ट्रैवल गाइड ऐप खोलें'})
htg=[s for s in hi['pages']['home']['sections'] if s.get('_tg')][0]
B.TG.update({'hi':{'h2':htg['h2'],'p':htg['p'][0],'card':htg['cards'][0][::2]},
 'es':{'h2':'App guía de viaje gratuita','p':'Planifica tus días con la app guía gratuita de ASCON: consejos locales, sitios para comer y visitar y un mapa, directamente en el navegador del móvil.','card':['App guía gratuita','Consejos y mapa de Ho Chi Minh, gratis en el navegador.']},
 'pt':{'h2':'App guia de viagem gratuito','p':'Planeje seus dias com o app guia gratuito da ASCON: dicas locais, lugares para comer e passear e um mapa, direto no navegador do celular.','card':['App guia gratuito','Dicas e mapa de Ho Chi Minh, grátis no navegador.']},
 'it':{'h2':'App guida di viaggio gratuita','p':'Organizza le giornate con l’app guida gratuita di ASCON: consigli locali, posti dove mangiare e da visitare e una mappa, direttamente nel browser del telefono.','card':['App guida gratuita','Consigli e mappa di Ho Chi Minh, gratis nel browser.']}})
hh=hi['pages']['house']
B.HOUSE.update({'hi':{k:hh[k] for k in ('title','description','h1','lead')},
 'es':dict(title='Casa entera en Ho Chi Minh, estancia por estancia | ASCON',description='Tres plantas y azotea: 3 dormitorios con baño, salón de unos 40 m², cocina equipada y sala de karaoke con proyector 4K.',h1='La casa: tu alojamiento en Ho Chi Minh, estancia por estancia',lead='Tres plantas, azotea y más de 250 m² solo para tu grupo. Aquí tienes las fotos y el equipamiento de cada estancia.'),
 'pt':dict(title='Casa inteira em Ho Chi Minh, ambiente por ambiente | ASCON',description='Três andares e terraço: 3 quartos com banheiro, sala de cerca de 40 m², cozinha equipada e sala de karaokê com projetor 4K.',h1='A casa: sua hospedagem em Ho Chi Minh, ambiente por ambiente',lead='Três andares, terraço na cobertura e mais de 250 m² só para o seu grupo. Aqui estão as fotos e os equipamentos de cada ambiente.'),
 'it':dict(title='Casa intera a Ho Chi Minh, stanza per stanza | ASCON',description='Tre piani e terrazza: 3 camere con bagno, soggiorno di circa 40 m², cucina attrezzata e sala karaoke con proiettore 4K.',h1='La casa: il tuo alloggio a Ho Chi Minh, stanza per stanza',lead='Tre piani, terrazza sul tetto e oltre 250 m² solo per il vostro gruppo. Qui trovi foto e dotazioni di ogni stanza.')})
B.OUTSIDE.update({'es':dict(description='Casa junto al río en Ho Chi Minh: terraza con barandilla blanca y toldo, vistas al agua y al perfil del Distrito 1.'),
 'pt':dict(description='Casa à beira do rio em Ho Chi Minh: terraço com guarda-corpo branco e toldo, de frente para a água e o skyline do Distrito 1.'),
 'it':dict(description='Casa sul fiume a Ho Chi Minh: terrazza con ringhiera bianca e tettoia, affaccio sull’acqua e sullo skyline del Distretto 1.'),
 'hi':dict(description='हो ची मिन्ह सिटी में नदी किनारे घर: सफ़ेद रेलिंग और छत वाला टैरेस, सामने पानी और डिस्ट्रिक्ट 1 की स्काईलाइन।')})
def tgp(title,desc,h1,lead,h2a,pa,caps,h2b,pb): return dict(title=title,description=desc,h1=h1,lead=lead,h2a=h2a,pa=pa,caps=caps,h2b=h2b,pb=pb)
B.TGP.update({
 'es':tgp('App guía gratuita para Ho Chi Minh | ASCON','La app guía gratuita de ASCON: consejos locales, dónde comer y qué ver, mapa y ayuda práctica en Ho Chi Minh. Se abre en el navegador del móvil.','App guía de viaje gratuita para Ho Chi Minh','ASCON Guide es una app web gratuita con consejos locales y lugares de Ho Chi Minh. Se abre directamente en el navegador del móvil: sin contraseña y sin instalar nada.',
   'Así es la app','Estas son capturas reales de la app en un móvil.',['Pantalla de bienvenida con el logo y el lema de ASCON LIVING','Elección de idioma: la app está en diez idiomas','Categorías: comida, cafés, bares, planes en familia y más','Mapa de lugares alrededor de la casa','Información práctica y ayuda de emergencia'],
   'Consejos y lugares',['Los lugares están ordenados por categorías: comida, cafés y postres, bares y vida nocturna, niños y familia, monumentos y cultura, actividades, relax, compras, excursiones de un día e información práctica y de emergencia. El mapa muestra los lugares alrededor de la casa y el botón Cómo llegar abre la navegación.','Puedes añadir la app a la pantalla de inicio. Más ideas en nuestra <a href="{L}guide/">guía de viaje de Ho Chi Minh</a>.']),
 'pt':tgp('App guia gratuito para Ho Chi Minh | ASCON','O app guia gratuito da ASCON: dicas locais, onde comer e o que ver, mapa e ajuda prática em Ho Chi Minh. Abre no navegador do celular.','App guia de viagem gratuito para Ho Chi Minh','O ASCON Guide é um app web gratuito com dicas locais e lugares de Ho Chi Minh. Abre direto no navegador do celular: sem senha e sem instalar nada.',
   'Veja como é o app','Estas são capturas de tela reais do app em um celular.',['Tela de boas-vindas com o logo e o lema da ASCON LIVING','Escolha de idioma: o app está disponível em dez idiomas','Categorias: comida, cafés, bares, passeios em família e mais','Mapa dos lugares ao redor da casa','Informações práticas e ajuda de emergência'],
   'Dicas e lugares',['Os lugares estão organizados por categorias: comida, cafés e sobremesas, bares e vida noturna, crianças e família, pontos turísticos e cultura, atividades, relaxamento, compras, passeios de um dia e informações práticas e de emergência. O mapa mostra os lugares ao redor da casa, e o botão Como chegar abre a navegação.','Você pode adicionar o app à tela inicial. Mais ideias no nosso <a href="{L}guide/">guia de viagem de Ho Chi Minh</a>.']),
 'it':tgp('App guida gratuita per Ho Chi Minh | ASCON','L’app guida gratuita di ASCON: consigli locali, dove mangiare e cosa vedere, mappa e aiuto pratico a Ho Chi Minh. Si apre nel browser del telefono.','App guida di viaggio gratuita per Ho Chi Minh','ASCON Guide è un’app web gratuita con consigli locali e luoghi di Ho Chi Minh. Si apre direttamente nel browser del telefono: senza password e senza installare nulla.',
   'Ecco com’è l’app','Queste sono vere schermate dell’app su un telefono (l’app non è ancora disponibile in italiano, quindi le schermate sono in inglese).',['Schermata di benvenuto con il logo e il motto di ASCON LIVING','Scelta della lingua: l’app è disponibile in dieci lingue','Categorie: cibo, caffè, bar, gite in famiglia e altro','Mappa dei luoghi intorno alla casa','Informazioni pratiche e aiuto in caso di emergenza'],
   'Consigli e luoghi',['I luoghi sono divisi per categorie: cibo, caffè e dolci, bar e vita notturna, bambini e famiglia, monumenti e cultura, attività, relax, shopping, gite di un giorno e informazioni pratiche e di emergenza. La mappa mostra i luoghi intorno alla casa e il pulsante Indicazioni apre la navigazione.','Puoi aggiungere l’app alla schermata Home. Altre idee nella nostra <a href="{L}guide/">guida di viaggio di Ho Chi Minh</a>.'])})
B.RULES.update({
 'es':{'h2':'Normas básicas','flow':[['ul',['Entrada de 14:00 a 23:00, salida a las 12:00.','Por ley vietnamita, es obligatorio registrar a los huéspedes.','No se fuma dentro de la casa; solo en las zonas exteriores designadas.','Música alta hasta las 21:30.','No se permiten fiestas ruidosas.','Solo pueden alojarse los huéspedes registrados.']]]},
 'pt':{'h2':'Regras básicas','flow':[['ul',['Check-in das 14h às 23h, check-out às 12h.','Pela lei vietnamita, o registro dos hóspedes é obrigatório.','Proibido fumar dentro de casa; só nas áreas externas indicadas.','Música alta até as 21h30.','Nada de festas barulhentas.','Somente hóspedes registrados podem se hospedar.']]]},
 'it':{'h2':'Regole di base','flow':[['ul',['Check-in dalle 14:00 alle 23:00, check-out alle 12:00.','Per legge vietnamita la registrazione degli ospiti è obbligatoria.','Vietato fumare in casa; si fuma solo nelle aree esterne indicate.','Musica alta fino alle 21:30.','Niente feste rumorose.','Possono soggiornare solo gli ospiti registrati.']]]},
 'hi':{'h2':'बुनियादी नियम','flow':[['ul',['चेक-इन 14:00–23:00, चेक-आउट 12:00।','वियतनामी कानून के अनुसार मेहमानों का रजिस्ट्रेशन ज़रूरी है।','घर के अंदर धूम्रपान नहीं; सिर्फ़ तय बाहरी जगहों पर।','तेज़ संगीत 21:30 तक।','कोई शोर-शराबे वाली पार्टी नहीं।','सिर्फ़ रजिस्टर्ड मेहमान ही ठहर सकते हैं।']]]}})
B.KWCAP.update({'es':[("en una casa del Distrito 7 de Ho Chi Minh:","en la casa:"),("en una casa del Distrito 7:","en la casa:"),("Por qué el Distrito 7","Por qué este barrio"),("El Distrito 7 va a otro ritmo","El barrio va a otro ritmo"),("Tân Hưng, Distrito 7, Ho Chi Minh.","Tân Hưng, Ho Chi Minh.")],
 'pt':[("em casa no Distrito 7 de Ho Chi Minh:","na casa:"),("O Distrito 7 vai em outro compasso","O bairro vai em outro compasso"),("Tân Hưng, Distrito 7, Ho Chi Minh.","Tân Hưng, Ho Chi Minh.")],
 'it':[("in casa nel Distretto 7 di Ho Chi Minh:","in casa:"),("in casa nel Distretto 7:","in casa:"),("Il Distretto 7 offre","Questa zona offre"),("Tân Hưng, Distretto 7, Ho Chi Minh.","Tân Hưng, Ho Chi Minh.")],
 'hi':[("डिस्ट्रिक्ट 7 के घर में पूरा किचन:","घर में पूरा किचन:"),("डिस्ट्रिक्ट 7 के घर पर लगभग","घर पर लगभग"),("डिस्ट्रिक्ट 7 में रफ़्तार अलग है","यहाँ रफ़्तार अलग है"),("Tân Hưng, डिस्ट्रिक्ट 7, हो ची मिन्ह सिटी।","Tân Hưng, हो ची मिन्ह सिटी।")]})
LANGS=('es','pt','it','hi')
def run(l):
    if l=='hi':
        old=json.load(open('content/hi.json'))
        B.TGP['hi']=None
        B.build(l)
        d=json.load(open('content/hi.json'))
        d['pages']['travel-guide']=old['pages']['travel-guide']
        for k in ('imprint','privacy','guide-family','guide-airport','guide-app'): d['pages'][k]=old['pages'][k]
        for sec in d['pages']['guide-airport']['sections']:
            if sec.get('h2')=='यात्रा समय': sec['p']=['कार से लगने वाला समय ट्रैफ़िक पर बहुत निर्भर करता है; ख़ासकर भीड़ के समय अतिरिक्त समय रखें।']
        json.dump(d,open('content/hi.json','w'),ensure_ascii=False,indent=1)
    else: B.build(l)
if __name__=='__main__':
    for l in (sys.argv[1:] or LANGS): run(l)
    for x in B.LOG: print(*x,sep=' | ')
