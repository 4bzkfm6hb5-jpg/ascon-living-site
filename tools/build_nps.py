"""NL / PL / SV from MR texts: extends tools/build_cjk.py (same pipeline and rules). App has no nl/pl/sv -> EN screenshots."""
import re,sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
import build_cjk as B
import build_sea, build_vrf, build_epi  # noqa: shared pattern extensions
def ext(rx,more): return re.compile(rx.pattern+'|'+more,rx.flags)
R=re.compile
B.REP.update({
 'nl':[("Villa in Saigon voor groepen","Huis in Saigon voor groepen"),(", villa met karaoke in Ho Chi Minh",", huis met karaoke in Ho Chi Minh"),(", villa in Saigon",", huis in Saigon"),("een villa","een huis"),("Een villa","Een huis"),("Villa","Huis"),("villa","huis"),
   ("De microfoons liggen in huis en de songteksten verschijnen op het scherm van de 4K-projector.","De microfoons liggen in huis en er is een 4K-projector."),("Ja, met microfoons en songteksten op het scherm.","Ja, met karaokemicrofoons."),
   (", een rotan bank en zonnelampjes."," en zonnelampjes."),("De hoofdslaapkamer heeft een eigen balkon en er is ook een overdekt balkon met rotan stoelen.","De hoofdslaapkamer heeft een eigen balkon."),
   ("Het wachtwoord krijg je na de boeking.","De app is gratis en heeft geen wachtwoord nodig."),("Wachtwoord na de boeking.","Gratis, zonder wachtwoord."),
   ("Na de bevestiging krijg je de toegangsgegevens en het wachtwoord van de ASCON Guide-app.","Na de bevestiging krijg je de toegangsgegevens. De ASCON Guide-app is gratis en zonder wachtwoord."),
   ("Wanneer krijg ik het wachtwoord?","Heeft de app een wachtwoord nodig?"),("Zodra je boeking bevestigd is, ontvang je het wachtwoord.","Nee. De app is gratis en opent direct in de browser van je telefoon."),
   ("Je krijgt de deurcode, uitleg over de sleutel van het hek en het wachtwoord van ASCON Guide, zodat je je dagen alvast kunt plannen.","Je krijgt de deurcode en uitleg over de sleutel van het hek; met de gratis ASCON Guide-app kun je je dagen alvast plannen."),
   ("Na de bevestiging krijg je de deurcode, uitleg over de sleutel van het hek en het wachtwoord van de ASCON Guide-app, met kaart en praktische tips.","Na de bevestiging krijg je de deurcode en uitleg over de sleutel van het hek. De gratis ASCON Guide-app heeft een kaart en praktische tips."),
   ("Na de boeking krijg je het wachtwoord van de ASCON Guide-app:","De gratis ASCON Guide-app:"),
   (", keuken, veiligheid, boeken.",", keuken, boeken."),(", buren en veiligheid.","en buren."),("Toegang en veiligheid","Toegang")],
 'pl':[("Willa w Ho Chi Minh dla grup","Dom w Ho Chi Minh dla grup"),(", willa w Sajgonie",", dom w Sajgonie"),(", willa z karaoke w Ho Chi Minh",", dom z karaoke w Ho Chi Minh"),("Willa","Dom"),("willa","dom"),("willi","domu"),("willę","dom"),("willą","domem"),
   ("Mikrofony są w domu, a teksty piosenek wyświetlają się na ekranie projektora 4K.","Mikrofony są w domu, jest też projektor 4K."),
   (", rattanową sofą i lampkami solarnymi."," i lampkami solarnymi."),("Sypialnia główna ma własny balkon, jest też zadaszony balkon z rattanowymi fotelami.","Sypialnia główna ma własny balkon."),
   ("Hasło dostaniecie po rezerwacji.","Aplikacja jest bezpłatna i nie wymaga hasła."),("Hasło po rezerwacji.","Bezpłatnie, bez hasła."),
   ("Po potwierdzeniu otrzymacie dane do wejścia i hasło do aplikacji ASCON Guide.","Po potwierdzeniu otrzymacie dane do wejścia. Aplikacja ASCON Guide jest bezpłatna i nie wymaga hasła."),
   ("Kiedy dostanę hasło?","Czy aplikacja wymaga hasła?"),("Gdy tylko rezerwacja zostanie potwierdzona, wysyłamy hasło.","Nie. Jest bezpłatna i otwiera się bezpośrednio w przeglądarce telefonu."),
   ("Dostaniecie kod do drzwi, informacje o kluczu do bramy i hasło do ASCON Guide, żeby z wyprzedzeniem zaplanować","Dostaniecie kod do drzwi i informacje o kluczu do bramy, a z bezpłatną aplikacją ASCON Guide z wyprzedzeniem zaplanujecie"),
   ("Po potwierdzeniu rezerwacji dostaniecie kod do drzwi, informacje o kluczu do bramy i hasło do aplikacji ASCON Guide z mapą i praktycznymi wskazówkami.","Po potwierdzeniu rezerwacji dostaniecie kod do drzwi i informacje o kluczu do bramy. Bezpłatna aplikacja ASCON Guide ma mapę i praktyczne wskazówki."),
   ("Po rezerwacji otrzymacie hasło do aplikacji ASCON Guide:","Bezpłatna aplikacja ASCON Guide:"),
   (", kuchnia, bezpieczeństwo, rezerwacja.",", kuchnia, rezerwacja."),(", sąsiedzi i bezpieczeństwo."," i sąsiedzi."),("Wejście i bezpieczeństwo","Wejście")],
 'sv':[("Villa i Saigon för grupper","Hus i Saigon för grupper"),(", villa med karaoke i Ho Chi Minh",", hus med karaoke i Ho Chi Minh"),(", villa i Saigon",", hus i Saigon"),("en villa","ett hus"),("En villa","Ett hus"),("villan","huset"),("Villa","Hus"),("villa","hus"),
   ("Mikrofonerna finns i huset och texterna visas på 4K-projektorns duk.","Mikrofonerna finns i huset, och det finns en 4K-projektor."),("Ja, med mikrofoner och texter på skärmen.","Ja, med karaokemikrofoner."),
   (", rottingsoffa och solcellslampor."," och solcellslampor."),("Huvudsovrummet har egen balkong och det finns också en övertäckt balkong med rottingfåtöljer.","Huvudsovrummet har egen balkong."),
   ("Lösenordet får ni efter bokningen.","Appen är gratis och kräver inget lösenord."),("Lösenord efter bokningen.","Gratis, utan lösenord."),
   ("Efter bekräftelsen får ni entréuppgifterna och lösenordet till appen ASCON Guide.","Efter bekräftelsen får ni entréuppgifterna. Appen ASCON Guide är gratis och kräver inget lösenord."),
   ("När får jag lösenordet?","Behöver appen ett lösenord?"),("Så fort bokningen är bekräftad skickar vi lösenordet.","Nej. Appen är gratis och öppnas direkt i mobilens webbläsare."),
   ("Ni får dörrkoden, information om grindnyckeln och lösenordet till ASCON Guide, så att ni kan planera","Ni får dörrkoden och information om grindnyckeln, och med den kostnadsfria appen ASCON Guide kan ni planera"),
   ("Efter bekräftelsen får ni dörrkoden, information om grindnyckeln och lösenordet till ASCON Guide, med karta och praktiska tips.","Efter bekräftelsen får ni dörrkoden och information om grindnyckeln. Den kostnadsfria appen ASCON Guide har karta och praktiska tips."),
   ("Efter bokningen får ni lösenordet till appen ASCON Guide med","Den kostnadsfria appen ASCON Guide har"),("Efter bokningen får ni lösenordet till appen ASCON Guide:","Den kostnadsfria appen ASCON Guide:"),
   (", kök, säkerhet och bokning.",", kök och bokning."),(", grannar och säkerhet."," och grannar."),("Entré och säkerhet","Entré")]})
B.CAMN.update({'nl':'Bij de ingang hangen buitencamera\u2019s.','pl':'Przy wejściu są kamery zewnętrzne.','sv':'Vid entrén finns utomhuskameror.'})
B.CAMCELL.update({'nl':'Buitencamera\u2019s bij de ingang','pl':'Kamery zewnętrzne przy wejściu','sv':'Utomhuskameror vid entrén'})
B.CAMX.update({'nl':R(r"(?i:camera)"),'pl':R(r'(?i:\bkamer[ayę]?\b|kamerami|monitoring)'),'sv':R(r'(?i:\bkamer(?:or|orna|a)\b|övervakning)')})
B.DROP=ext(B.DROP,r'(?i:songtekst|tekst\w* piosenek|teksty na ekranie|tekstami na ekranie|texterna visas|texter på skärmen|rookmelder|EHBO|brandblusser|nooduitgang|noodverlichting|czujnik\w* dymu|apteczk|gaśnic|wyjści\w* ewakuacyjn|oznaczenie wyjścia|oświetlenie awaryjne|brandvarnare|första hjälpen|brandsläckare|nödutgång|nödbelysning|'
 r'\d+\s*(?:minuten|minut|minuter)\b|parkeer|parkering|zwembad|\bbasen\b|huisdier|zwierz\w* domow|husdjur|bagageopslag|przechowalni\w* bagażu|bagageförvaring|overdekt balkon|zadaszon\w* balkon|övertäckt\w* balkong)')
B.DROPQ=ext(B.DROPQ,r"(?i:veiligheid|bezpiecz|säkerhet|binnen camera|camera's binnen|kamery w środku|kamery wewnątrz|kameror inne|kameror inomhus)")
B.DROP_SECS=R(B.DROP_SECS.pattern[:-2]+'|Veiligheid|Bezpieczeństwo|Säkerhet)$')
B.DROP_ROWS=R(B.DROP_ROWS.pattern[:-2]+'|Veiligheid|Bezpieczeństwo|Säkerhet)$')
B.CAMROW=R(B.CAMROW.pattern[:-2]+"|Camera's|Kamery|Kameror)$")
B.PAGE_DROP={'room-outside':ext(B.PAGE_DROP['room-outside'],r'(?i:balkon|balkong|rotan|rattan|rotting|\bboot|\bboten\b|łód|łodzi|łodzie|båt)'),'room-hallway':ext(B.PAGE_DROP['room-hallway'],r'(?i:balkon|balkong)')}
B.RV=ext(B.RV,r'(?i:uitzicht op de rivier|widok na rzekę|utsikt över floden)')
cap=build_epi.cap
B.RVNEUT.update({'nl':cap('uitzicht'),'pl':cap('widok'),'sv':cap('utsikt')})
B.PHOTO=R(B.PHOTO.pattern.replace('|imagen)','|imagen|zdjęcie|bild)'),B.PHOTO.flags)
B.LOC.update({'nl':('Veelgestelde vragen','Afbeeldingen'),'pl':('Najczęstsze pytania','Zdjęcia'),'sv':('Vanliga frågor','Bilder')})
B.FAQSECREN.update({'nl':{'Veiligheid':'Overig'},'pl':{'Bezpieczeństwo':'Inne'},'sv':{'Säkerhet':'Övrigt'}})
ui=build_epi.ui
B.UI.update({'nl':ui('Naar de inhoud','Taal','Boek op Airbnb','Boek op Trip.com','Boek via WhatsApp','Boek via Zalo','Adres','Contact','Meer','Gids-app voor gasten','Lees meer','Bron','schatting','Home','Pagina niet gevonden','Deze pagina bestaat niet. Naar de homepage:'),
 'pl':ui('Przejdź do treści','Język','Rezerwuj na Airbnb','Rezerwuj na Trip.com','Rezerwuj przez WhatsApp','Rezerwuj przez Zalo','Adres','Kontakt','Więcej','Aplikacja-przewodnik dla gości','Czytaj dalej','Źródło','szacunek','Strona główna','Nie znaleziono strony','Ta strona nie istnieje. Przejdź na stronę główną:'),
 'sv':ui('Till innehållet','Språk','Boka på Airbnb','Boka på Trip.com','Boka via WhatsApp','Boka via Zalo','Adress','Kontakt','Mer','Guideapp för gäster','Läs mer','Källa','uppskattning','Start','Sidan hittades inte','Sidan finns inte. Gå till startsidan:')})
B.NAV.update({'nl':['Home','Het huis','Dakterras','Gezinnen','Groepen','Locatie','Boeken & contact','Veelgestelde vragen','Huisregels','Reisgids','Gids-app'],
 'pl':['Start','Dom','Taras','Rodziny','Grupy','Lokalizacja','Rezerwacja i kontakt','Pytania','Zasady','Przewodnik','Aplikacja'],
 'sv':['Start','Huset','Takterrass','Familjer','Grupper','Läge','Bokning & kontakt','Vanliga frågor','Husregler','Reseguide','Guideapp']})
B.CARD.update({'nl':['Karaoke & entertainment','Woonkamer','Keuken & eethoek','Hoofdslaapkamer','Slaapkamer 2','Slaapkamer 3','Badkamers','Gang & werkplek','Buiten & rivier','Dakterras'],
 'pl':['Karaoke i rozrywka','Salon','Kuchnia i jadalnia','Sypialnia główna','Sypialnia 2','Sypialnia 3','Łazienki','Korytarz i miejsce do pracy','Na zewnątrz i rzeka','Taras na dachu'],
 'sv':['Karaoke & underhållning','Vardagsrum','Kök & matplats','Huvudsovrum','Sovrum 2','Sovrum 3','Badrum','Hall & arbetsplats','Utomhus & floden','Takterrass']})
B.ROOMSH.update({'nl':'De ruimtes in detail','pl':'Pomieszczenia w szczegółach','sv':'Rummen i detalj'})
B.FAQH.update({'nl':'Veelgestelde vragen','pl':'Najczęstsze pytania','sv':'Vanliga frågor'})
B.ROOMSEC.update({'nl':'Het huis in het kort','pl':'Dom w liczbach','sv':'Huset i korthet'})
B.CONTACTH.update({'nl':'Contact','pl':'Kontakt','sv':'Kontakt'})
T,Z,E=build_vrf.T,build_vrf.Z,build_vrf.E
B.CONTACT.update({'nl':['Telefoon en WhatsApp: '+T,'Zalo: '+Z,'E-mail: '+E],'pl':['Telefon i WhatsApp: '+T,'Zalo: '+Z,'E-mail: '+E],'sv':['Telefon och WhatsApp: '+T,'Zalo: '+Z,'E-post: '+E]})
M=B.MAPS
B.MAPSEC.update({'nl':{'h2':'Kaart','p':[f'<a href="{M}" rel="noopener">Open het adres in Google Maps</a>. Uitgebreide aankomstinstructies sturen we na de boeking.']},
 'pl':{'h2':'Mapa','p':[f'<a href="{M}" rel="noopener">Otwórz adres w Mapach Google</a>. Szczegółowe instrukcje dojazdu wysyłamy po rezerwacji.']},
 'sv':{'h2':'Karta','p':[f'<a href="{M}" rel="noopener">Öppna adressen i Google Maps</a>. Utförliga ankomstinstruktioner skickas efter bokningen.']}})
B.APPBTN.update({'nl':'Open de gids-app','pl':'Otwórz aplikację','sv':'Öppna guideappen'})
B.TG.update({'nl':{'h2':'Gratis reisgids-app','p':'Plan je dagen met de gratis gids-app van ASCON: lokale tips, plekken om te eten en te bezoeken en een kaart, direct in de browser van je telefoon.','card':['Gratis gids-app','Tips en kaart van Ho Chi Minh, gratis in de browser.']},
 'pl':{'h2':'Bezpłatna aplikacja-przewodnik','p':'Zaplanujcie dni z bezpłatną aplikacją ASCON: lokalne wskazówki, miejsca na jedzenie i zwiedzanie oraz mapa, prosto w przeglądarce telefonu.','card':['Bezpłatna aplikacja','Wskazówki i mapa Ho Chi Minh, za darmo w przeglądarce.']},
 'sv':{'h2':'Gratis reseguideapp','p':'Planera dagarna med ASCON:s kostnadsfria guideapp: lokala tips, ställen att äta på och besöka och en karta, direkt i mobilens webbläsare.','card':['Gratis guideapp','Tips och karta över Ho Chi Minh, gratis i webbläsaren.']}})
B.HOUSE.update({
 'nl':dict(title='Heel huis in Ho Chi Minh, ruimte voor ruimte | ASCON',description='Drie verdiepingen en een dakterras: 3 slaapkamers met badkamer, woonkamer van ca. 40 m², volledig uitgeruste keuken en karaokekamer met 4K-projector.',h1='Het huis: je verblijf in Ho Chi Minh, ruimte voor ruimte',lead='Drie verdiepingen, een dakterras en meer dan 250 m² alleen voor jullie groep. Hier zie je de foto’s en de uitrusting van elke ruimte.'),
 'pl':dict(title='Cały dom w Ho Chi Minh, pokój po pokoju | ASCON',description='Trzy piętra i taras na dachu: 3 sypialnie z łazienkami, salon ok. 40 m², w pełni wyposażona kuchnia i pokój karaoke z projektorem 4K.',h1='Dom: wasz nocleg w Ho Chi Minh, pokój po pokoju',lead='Trzy piętra, taras na dachu i ponad 250 m² tylko dla waszej grupy. Tu znajdziecie zdjęcia i wyposażenie każdego pomieszczenia.'),
 'sv':dict(title='Hela huset i Ho Chi Minh, rum för rum | ASCON',description='Tre våningar och takterrass: 3 sovrum med eget badrum, vardagsrum på ca 40 m², fullt utrustat kök och karaokerum med 4K-projektor.',h1='Huset: ert boende i Ho Chi Minh, rum för rum',lead='Tre våningar, takterrass och över 250 m² bara för ert sällskap. Här finns bilder och utrustning för varje rum.')})
B.OUTSIDE.update({'nl':dict(description='Huis aan de rivier in Ho Chi Minh: terras met witte reling en luifel, zicht op het water en de skyline van District 1.'),
 'pl':dict(description='Dom nad rzeką w Ho Chi Minh: taras z białą balustradą i zadaszeniem, z widokiem na wodę i panoramę Dystryktu 1.'),
 'sv':dict(description='Hus vid floden i Ho Chi Minh: terrass med vitt räcke och skärmtak, med vattnet och District 1:s skyline framför er.')})
tgp=build_epi.tgp
B.TGP.update({
 'nl':tgp('Gratis gids-app voor Ho Chi Minh | ASCON','De gratis gids-app van ASCON: lokale tips, waar je eet en wat je ziet, een kaart en praktische hulp in Ho Chi Minh. Opent in de browser van je telefoon.','Gratis reisgids-app voor Ho Chi Minh','ASCON Guide is een gratis web-app met lokale tips en plekken in Ho Chi Minh. Hij opent direct in de browser van je telefoon: zonder wachtwoord en zonder installatie.',
   'Zo ziet de app eruit','Dit zijn echte schermafbeeldingen van de app op een telefoon (de app is nog niet in het Nederlands beschikbaar, dus de schermen zijn in het Engels).',['Welkomstscherm met het logo en het motto van ASCON LIVING','Taalkeuze: de app is er in tien talen','Categorieën: eten, cafés, bars, uitjes met het gezin en meer','Kaart met plekken rond het huis','Praktische informatie en hulp bij noodgevallen'],
   'Lokale tips en plekken',['De plekken zijn ingedeeld in categorieën: eten, cafés en desserts, bars en nachtleven, kinderen en gezin, bezienswaardigheden en cultuur, activiteiten, ontspanning, winkelen, dagtrips en praktische en noodinformatie. De kaart toont plekken rond het huis en de knop Route start de navigatie.','Je kunt de app aan je beginscherm toevoegen. Meer ideeën vind je in onze <a href="{L}guide/">reisgids voor Ho Chi Minh</a>.']),
 'pl':tgp('Bezpłatna aplikacja-przewodnik po Ho Chi Minh | ASCON','Bezpłatna aplikacja ASCON: lokalne wskazówki, gdzie zjeść i co zobaczyć, mapa i praktyczna pomoc w Ho Chi Minh. Otwiera się w przeglądarce telefonu.','Bezpłatna aplikacja-przewodnik po Ho Chi Minh','ASCON Guide to bezpłatna aplikacja webowa z lokalnymi wskazówkami i miejscami w Ho Chi Minh. Otwiera się prosto w przeglądarce telefonu: bez hasła i bez instalacji.',
   'Tak wygląda aplikacja','To prawdziwe zrzuty ekranu aplikacji na telefonie (aplikacja nie ma jeszcze wersji polskiej, więc ekrany są po angielsku).',['Ekran powitalny z logo i mottem ASCON LIVING','Wybór języka: aplikacja jest dostępna w dziesięciu językach','Kategorie: jedzenie, kawiarnie, bary, wypady z rodziną i więcej','Mapa miejsc wokół domu','Praktyczne informacje i pomoc w nagłych wypadkach'],
   'Lokalne wskazówki i miejsca',['Miejsca są podzielone na kategorie: jedzenie, kawiarnie i desery, bary i życie nocne, dzieci i rodzina, zabytki i kultura, aktywności, relaks, zakupy, wycieczki jednodniowe oraz informacje praktyczne i alarmowe. Mapa pokazuje miejsca wokół domu, a przycisk Trasa uruchamia nawigację.','Aplikację można dodać do ekranu głównego. Więcej pomysłów w naszym <a href="{L}guide/">przewodniku po Ho Chi Minh</a>.']),
 'sv':tgp('Gratis guideapp för Ho Chi Minh | ASCON','ASCON:s kostnadsfria guideapp: lokala tips, var ni äter och vad ni ser, karta och praktisk hjälp i Ho Chi Minh. Öppnas i mobilens webbläsare.','Gratis reseguideapp för Ho Chi Minh','ASCON Guide är en kostnadsfri webbapp med lokala tips och platser i Ho Chi Minh. Den öppnas direkt i mobilens webbläsare: utan lösenord och utan installation.',
   'Så ser appen ut','Det här är riktiga skärmbilder av appen i en mobil (appen finns ännu inte på svenska, så skärmarna visas på engelska).',['Välkomstskärm med ASCON LIVING:s logga och motto','Språkval: appen finns på tio språk','Kategorier: mat, kaféer, barer, familjeutflykter och mer','Karta över platser runt huset','Praktisk information och hjälp i nödsituationer'],
   'Lokala tips och platser',['Platserna är sorterade i kategorier: mat, kaféer och desserter, barer och nattliv, barn och familj, sevärdheter och kultur, aktiviteter, avkoppling, shopping, dagsutflykter samt praktisk information och nödinformation. Kartan visar platser runt huset och knappen Vägbeskrivning startar navigeringen.','Ni kan lägga till appen på hemskärmen. Fler idéer finns i vår <a href="{L}guide/">reseguide för Ho Chi Minh</a>.'])})
B.RULES.update({
 'nl':{'h2':'Basisregels','flow':[['ul',['Inchecken 14:00–23:00, uitchecken 12:00.','Volgens de Vietnamese wet moeten gasten geregistreerd worden.','Niet roken in huis; alleen op de aangewezen plekken buiten.','Harde muziek tot 21:30.','Geen wilde feesten.','Alleen geregistreerde gasten mogen verblijven.']]]},
 'pl':{'h2':'Podstawowe zasady','flow':[['ul',['Zameldowanie 14:00–23:00, wymeldowanie do 12:00.','Zgodnie z prawem wietnamskim goście muszą zostać zarejestrowani.','W domu nie palimy; palenie tylko w wyznaczonych miejscach na zewnątrz.','Głośna muzyka do 21:30.','Żadnych hucznych imprez.','Nocować mogą tylko zarejestrowani goście.']]]},
 'sv':{'h2':'Grundregler','flow':[['ul',['Incheckning 14:00–23:00, utcheckning 12:00.','Enligt vietnamesisk lag måste gäster registreras.','Ingen rökning inomhus; bara på anvisade platser utomhus.','Hög musik till 21:30.','Inga vilda fester.','Endast registrerade gäster får bo här.']]]}})
B.KWCAP.update({'nl':[("Uitgeruste keuken in District 7:","Uitgeruste keuken:"),("van ca. 56–60 m² in District 7, Ho Chi Minh:","van ca. 56–60 m²:"),("In District 7 leef je","Hier leef je"),("Tân Hưng, District 7, Ho Chi Minh-stad.","Tân Hưng, Ho Chi Minh-stad.")],
 'pl':[],
 'sv':[("Fullt utrustat kök i District 7:","Fullt utrustat kök:"),("på ca 56–60 m² i District 7, Ho Chi Minh:","på ca 56–60 m²:"),("I District 7 lever ni","Här lever ni"),("Tân Hưng, District 7, Ho Chi Minh City.","Tân Hưng, Ho Chi Minh City.")]})
LANGS=('nl','pl','sv')
if __name__=='__main__':
    for l in (sys.argv[1:] or LANGS): B.build(l)
    for x in B.LOG: print(*x,sep=' | ')
