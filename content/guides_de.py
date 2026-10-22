"""German city guides and the whole-house audience page."""
from guide_lib import page, ui

UI = ui(
    "Auf dieser Seite",
    "Schreibt uns eure Daten über die Buchungsseite, dann bestätigen wir das Haus für euren Aufenthalt.",
    "Buchung und Kontakt",
    "Weiterlesen",
)
HUB = "Alle Saigon-Themen"
ALSO = {
    "guide-app": ["guide-sights", "guide-practical", "home"],
    "guide-family": ["guide-sights", "guide-weather", "home"],
    "guide-airport": ["guide-arrival", "guide-traffic", "home"],
}

def cards():
    return [
        ["ASCON LIVING Guide App", "guide-app", "Orte rund ums Haus, Routen und praktische Tipps im Browser."],
        ["Ho-Chi-Minh-Stadt mit Kindern", "guide-family", "Ideen und praktische Hinweise für eine Familienreise."],
        ["Flughafentransfer", "guide-airport", "Vom Tân Sơn Nhất zum Haus, Transfer nur auf Anfrage."],
        ["Sehenswürdigkeiten", "guide-sights", "Altstadt, Museen, Pagoden und der Fluss, in ruhigem Tempo."],
        ["Märkte", "guide-markets", "Ben Thanh, Viertelmärkte und was mit in die Küche darf."],
        ["Kaffee", "guide-coffee", "Phin, Kondensmilch und ein Tag, der sich an Tassen orientiert."],
        ["Saigon-Fluss", "guide-river", "Der Arbeitsfluss, eine Bootsfahrt und das Ufer."],
        ["Abende", "guide-evenings", "Fußgängerzonen, Flussluft und der Heimweg."],
        ["Mekong und Cu Chi", "guide-daytrips", "Ein ganzer Tag im Delta oder in den Cu-Chi-Tunneln."],
        ["Wetter", "guide-weather", "Hitze, Regen und welche Wochen sich lohnen."],
        ["Vom Flughafen", "guide-arrival", "Tân Sơn Nhất, Transfer auf Anfrage, Ankunft am Haus."],
        ["Geld, SIM, Apps", "guide-practical", "Bargeld, eine lokale SIM und die Apps für den Alltag."],
        ["Verkehr und Sicherheit", "guide-traffic", "Überqueren, Fahrten und die ruhigen Gewohnheiten."],
        ["Ganzes Haus", "audience", "Warum ein privates Haus zu Familie, Freunden und längeren Aufenthalten passt."],
    ]

PAGES = {}

PAGES["guide-sights"] = page(
    "Sehenswürdigkeiten in Saigon | ASCON LIVING",
    "Sehenswürdigkeiten in Saigon, praktisch erzählt: Altstadt, Museen, Pagoden und der Fluss, in einem Tempo, das einen Aufenthalt wirklich trägt.",
    "Sehenswürdigkeiten in Saigon, langsam angesehen",
    "Saigon belohnt Leute, die wenige Orte wählen und dazwischen Luft lassen. Das Zentrum lässt sich zu Fuß verbinden, die Museen wollen Aufmerksamkeit, und der Fluss erklärt, warum die Skyline so dasteht.",
    [
        ("Das historische Zentrum zu Fuß", [
            "Fangt bei der Kathedrale, dem zentralen Postamt und der Oper an. Die Häuser stehen nah beieinander, der Weg dazwischen ist der eigentliche Spaziergang. Das Postamt wirkt noch wie eine arbeitende Halle, mit hohem Dach und Karten an den Wänden. Der Platz davor ist die natürliche Pause, wenn die Hitze zunimmt. Bäume, Schulklassen und Postkarten teilen sich denselben Bürgersteig.",
            "Das Rathaus steht um die Ecke und ist vom Gehweg aus genug. Wenn ihr nur eine ruhige Runde habt, ist dieses Ensemble die richtige: Architektur, Schatten und genug Cafés, damit niemand durchmarschieren muss. Die schweren Museen hebt ihr euch für einen anderen Teil des Tages auf, wenn ihr bereit seid, drinnen zu sein.",
        ]),
        ("Museen und der Palast", [
            "Der Independence Palace, auch Wiedervereinigungspalast genannt, ist eine Folge von Staatsräumen, Lagezentren und einem Garten dazwischen. Geht hin, wenn ihr ein paar Räume wirklich lesen wollt, nicht wenn ihr jede Treppe fotografieren müsst. Das War Remnants Museum ist schwerer. Es ist ein Ort für Erwachsene, die Kontext wollen. Ob Kinder die härtesten Säle sehen sollen, entscheidet ihr vorher.",
            "Das Museum der Schönen Künste, in einem kolonialen Haus etwas weiter weg, ist ruhiger. Keramik, Lack und moderne Malerei liegen in Räumen, die man verlassen und wieder betreten kann. Keines dieser Häuser braucht allein einen ganzen Tag. Zwei davon, mit einem langen Essen dazwischen, ergeben einen vollständigen Bogen vom Vormittag bis zum Nachmittag.",
        ]),
        ("Pagoden und ruhigere Straßen", [
            "Die Jade-Kaiser-Pagode ist rauchig, voller Figuren und kleiner, als ihr Ruf. Weihrauch, Schildkröten im Teich und die Dichte der Besucher machen den Besuch kurz und bleibend. Schultern und Knie bleiben bedeckt. Wer betet, hat Vorrang. Der Hof ist kein Bühnenbild.",
            "Andere Pagoden liegen in gewöhnlichen Straßen, oft zwischen Häusern und Werkstätten. Genau diese Mischung ist die Sehenswürdigkeit: ein Dach mit Drachen neben einer Werkstatt, einem Schultor, einer Obstverkäuferin. Ist ein Tor offen und der Hinweis freundlich, reicht ein leiser Blick. Läuft eine Zeremonie, bleibt ihr am Rand.",
        ]),
        ("Der Fluss als Teil der Ansicht", [
            "Der Saigon-Fluss ist keine Kulisse, die man von einer Brücke abhakt. Geht ein Stück am Ufer, seht den Lastkähnen zu und merkt, wie die Türme auf der anderen Seite stehen. Eine Bootsfahrt ist ein eigenes Thema, dazu gibt es einen eigenen Text. Vom Land aus geht es um Orientierung: Wenn ihr wisst, wohin das Wasser läuft, wird der Rest der Karte klarer.",
            "Der späte Nachmittag ist die freundliche Zeit, weil die Hitze nachlässt und der Himmel die Arbeit übernimmt. Ihr braucht keinen bezahlten Aussichtspunkt. Ein öffentliches Stück Gehweg, ein kaltes Getränk und ein ruhiger Blick sind die ganze Unternehmung.",
        ]),
        ("Wie ihr die Tage legt", [
            "Koppelt eine Runde draußen mit einer Runde drinnen. Das Zentrum, solange es erträglicher ist, ein Museum, wenn die Sonne hoch steht, eine Pagode oder der Fluss später. Lasst einen Tag fast ohne Plan, denn Saigon ist voller Straßen, die besser sind als das, was ihr beim Frühstück ausgedacht habt.",
            "Schuhe, in denen ihr laufen könnt, Wasser dabei, die Museumstasche leicht. Das Haus ist die Pause: Klimaanlage in den Schlafzimmern und im Wohnzimmer, eine Küche, wenn ihr Obst und Kaffee wollt, bevor ihr wieder hinausgeht, und eine Dachterrasse, wenn die Stadt genug war.",
        ]),
        ("Was dieser Text weglässt", [
            "Hier gibt es keine Rangliste und kein Versprechen, dass ein Ort leer sein wird. Zeiten ändern sich, genauso wie vorübergehende Schließungen. Schaut am Vortag nach, besonders um Feiertage, und nehmt eine geschlossene Tür als Grund, das Viertel zu Fuß zu nehmen.",
            "Märkte, Kaffee oder ein Tag außerhalb der Stadt haben eigene Seiten. Die Orte oben reichen für einen ersten Aufenthalt, und sie werden beim zweiten Mal besser, wenn ihr schon wisst, welche Straße euch gefallen hat.",
        ]),
    ],
    ["guide-markets", "guide-coffee", "guide-river", "home"],
)

PAGES["guide-markets"] = page(
    "Märkte in Saigon | ASCON LIVING",
    "Wie Märkte in Saigon für Besucher funktionieren: Ben Thanh, Viertelhallen, was Leute wirklich mitnehmen, und ein Einkauf, der kein Pflichtprogramm wird.",
    "Märkte in Saigon, von der bekannten Halle bis zur lokalen",
    "Märkte in Saigon sind nicht ein Ding. Manche sind für Besucher gebaut, manche versorgen die Straße davor, und die nützlichen tun ein bisschen von beidem. Geht mit einer kurzen Liste und Appetit hin, nicht mit dem Plan, jede Gasse zu sehen.",
    [
        ("Ben Thanh und die Besuchshallen", [
            "Ben Thanh ist der Markt, den Leute meinen, wenn sie sagen, sie seien auf dem Markt gewesen. Die Halle ist ein Raster aus Ständen: Kaffee, Trockenfrucht, Lack, Kleidung und eine Ecke mit Essen, die lauter riecht, als sie aussieht. Händler rufen euch heran. Ein Lächeln und ein Kopfschütteln sind eine vollständige Antwort, wenn ihr nur schaut.",
            "An Ständen, die sich an Besucher richten, ist Kaufen ein kurzes Gespräch. Entscheidet vorher, was ihr wollt, und geht weiter, wenn das Gespräch aufhört, freundlich zu sein. Das Gebäude selbst ist der Anker: ein Uhrturm, ein niedriges Dach und Straßen drumherum, die noch lange beschäftigt bleiben, nachdem ihr drinnen fertig seid.",
        ]),
        ("Märkte im Viertel", [
            "Jeder Teil der Stadt hat einen Markt, der für die Leute öffnet, die dort wohnen. Gemüse liegt auf Tischen, Fisch auf Eis, und am Rand gibt es gekochtes Frühstück für Menschen, die zur Arbeit müssen. Das ist keine Vorführung. Tretet vorsichtig, kauft etwas Kleines, wenn ihr Platz beansprucht, und tragt die Tasche vorn.",
            "Binh Tay, im chinesisch geprägten Cho Lon, ist die große Fassung: ein Hof, Großhandelsgänge und ein Dach, das man von weitem sieht. Ruhiger wird es, wenn ihr Architektur und Leute anseht. Interessanter, wenn ihr bemerkt, was in Menge verkauft wird. Ihr braucht keinen Führer. Ihr braucht Geduld an den Toren.",
        ]),
        ("Was sich lohnt mitzunehmen", [
            "Kaffee ist das einfache Mitbringsel: Bohnen oder gemahlen, reisetüchtig verpackt, von einem Stand, der euch an der Tüte riechen lässt. Achtet auf ein Röstdatum oder wenigstens auf einen Laden, der Ware bewegt, und nehmt zuerst eine kleine Menge. Trockenfrucht, Chili und Süßes reisen gut, wenn die Packung zu ist. Stoff und schlichte Kleidung machen Spaß, wenn ihr sie anprobieren könnt oder die Größe klar ist.",
            "Lasst weg, was auf einem langen Reisetag Kühlung braucht, und lasst Lack und Keramik weg, wenn ihr keine sichere Packweise habt. Die Küche im Haus ist das bessere Ziel für Obst, Kräuter und Frühstück. Eine Tomate vom Markt, am selben Tag gegessen, schlägt einen Koffer voller Snacks, die ihr nicht aufesst.",
        ]),
        ("Benehmen und Achtsamkeit", [
            "Fragt, bevor ihr eine Person fotografiert, besonders jemanden bei der Arbeit. Fasst kein Gemüse an, das ihr nicht kauft. Bietet man euch einen Platz an einem Essensstand, heißt Sitzen: ihr seid Gäste und bestellt. Kleine Scheine halten den Austausch einfach. Wie ihr Bargeld tragt, steht auf der Seite zu Geld und Apps.",
            "Taschen und Telefone sind das praktische Risiko, nicht das Essen. Tragt die Tasche quer und lasst das Telefon nicht an der Tischkante liegen. Hitze und nasse Böden zählen so sehr wie Gedränge. Schuhe mit Grip und die Bereitschaft, zur Seite zu treten, helfen mehr als jede Regelliste.",
        ]),
        ("Morgens oder später", [
            "Gemüse ist früher am klarsten, wenn die Stände noch gefüllt werden und am Rand Leute essen, die irgendwohin müssen. Später sind die Besuchshallen voller und die lokalen Märkte dünner. Beides ist richtig. Passt die Tageszeit an den Auftrag an: Einkauf früh, ein Blick durch Ben Thanh, wenn ihr schon im Zentrum seid.",
            "Versucht nicht, einen ernsthaften Marktvormittag mit Museum und Pagode zu stapeln. Der Markt ist der Ausflug. Zurück ins Haus, Obst waschen, Kaffee machen. Diese Folge ist mehr Saigon als ein Plan, der sich nie hinsetzt.",
        ]),
        ("Eine kurze Liste reicht", [
            "Ein Besuchermarkt und ein Viertelmarkt zeigen euch den Unterschied. Danach bemerkt ihr Märkte, die ihr nicht gesucht habt: eine Gasse mit Blumen, eine Reihe Stoffläden, eine Frau mit Korb, die der Markt ihrer Straße ist.",
            "Wenn der Tag nass ist, sind die überdachten Hallen die bequeme Fassung. Wenn ihr lieber den Fluss oder die Sehenswürdigkeiten wollt, hebt den Markt für einen anderen Morgen auf. Er ist dann noch da.",
        ]),
    ],
    ["guide-sights", "guide-coffee", "guide-practical", "home"],
)

PAGES["guide-coffee"] = page(
    "Kaffeekultur in Saigon | ASCON LIVING",
    "Kaffeekultur in Saigon ohne Jargon: Phin-Filter, Kondensmilch, Eiskaffee und ein Tag, der sich an Tassen orientiert statt an einer langen Liste.",
    "Wie Saigon seinen Kaffee trinkt",
    "Kaffee in Saigon ist ein Tempo, keine Mode. Leute sitzen auf niedrigen Hockern, in Ladenhäusern und in ruhigen Räumen mit Klimaanlage. Das Getränk ist meist stark, oft süß und fast immer einen zweiten Schluck wert.",
    [
        ("Der Phin und die Tasse", [
            "Der lokale Aufbrüher ist ein kleiner Metall-Phin über dem Glas. Heißes Wasser läuft durch gemahlenen Robusta, langsam genug, dass der Tisch zur Bestellung gehört. Ihr trinkt ihn schwarz oder mit einem Löffel Kondensmilch, die ihr selbst unterrührt. Eiskaffee, ca phe sua da, ist die gewöhnliche Wahl, sobald der Tag heiß ist: derselbe Tropf, über Eis.",
            "Bac xiu ist die mildere, milchigere Verwandte. Kokoskaffee und gesalzener Kaffee stehen heute auf vielen Karten und lohnen eine Tasse, wenn ihr ein Getränk mit Rezept wollt. Eierkaffee gehört eher in den Norden, taucht hier aber auf. Fangt mit dem Eiskaffee mit Milch an. Darauf läuft die Stadt.",
        ]),
        ("Wo Leute sitzen", [
            "Die Version auf dem Bürgersteig ist ein paar Hocker, ein Kessel und der Blick auf den Verkehr. Sie ist gesellig und ein wenig staubig und passt, wenn ihr zwischen zwei Wegen in Ruhe trinken wollt. Bestellen, sitzen, keine lange Karte erwarten. Sind die Hocker voll, ist der nächste Ort selten weit.",
            "Cafés drinnen sind die andere Hälfte: Räume für Gespräche, Laptops und den heißesten Teil des Tages. Manche sind ruhig und dämmrig, manche hell und süß. Wählt nach dem Stuhl, nicht nach dem Schild. Ein Café mit Platz zum Reden schenkt dieselbe Familie von Getränken aus wie der Bürgersteig, meist mit mehr Eis und mehr Zeit.",
        ]),
        ("Bestellen ohne Auftritt", [
            "Auf das Glas des Nachbarn zeigen funktioniert. Ebenso die kurze Liste: den da für schwarz auf Eis, sua da für Milch auf Eis, nong wenn ihr es heiß wollt. Zucker steckt oft schon in der Kondensmilch, also probiert, bevor ihr etwas dazutut. Wer weniger Süße will, sagt das am Anfang.",
            "Bezahlt, wenn die Tasse kommt oder wenn ihr geht, je nach Ort. Kleine Scheine helfen. Ihr müsst nicht viel Vietnamesisch sprechen, um ein guter Gast zu sein. Ihr stellt das Glas zurück auf das Tablett und schiebt keinen Hocker auf die Fahrbahn.",
        ]),
        ("Ein Tag aus Tassen", [
            "Eine Tasse nach dem Frühstück, eine wenn das Zentrum euch müde gemacht hat, eine am Ende des Nachmittags. Das ist ein voller Kaffeetag und lässt Raum für Markt oder Museum. Ein Dutzend Läden hintereinander macht aus dem Getränk eine Aufgabe. Besser ist, einen Ort zu merken, an den ihr wiederkommen würdet, und dann wirklich wiederzukommen.",
            "Kaffee ist auch die Pause mit Kindern oder mit Freunden, die keine weitere Sehenswürdigkeit wollen. Der Bürgersteig ist kurz. Der Raum drinnen ist der Ort, an dem ihr entscheidet, was als Nächstes kommt. Das Koffein ist echt. Robusta hier ist keine schüchterne Röstung.",
        ]),
        ("Bohnen für später", [
            "Wollt ihr Kaffee für zu Hause, kauft eine kleine verschlossene Tüte an einem Ort, der euch riechen lässt, und trinkt sie in den Wochen nach der Reise. Gemahlener Kaffee passt zum Phin. Bohnen lohnen sich, wenn ihr eine Mühle habt. Die Marktseite erzählt dieselbe Idee vom Stand aus.",
            "Im Haus steht eine Kaffeemaschine, also hängt die erste Tasse am Morgen nicht davon ab, einen Hocker zu finden. Nutzt sie, wenn ihr langsam anfangen wollt, und geht für das Glas sua da hinaus, wenn die Stadt in der Tasse sein soll. Beides gehört in denselben Aufenthalt.",
        ]),
        ("Worüber ihr euch nicht grämen müsst", [
            "Ihr verderbt nichts, wenn ihr die falsche Größe oder das falsche Eis bestellt. Saigons Kaffee verzeiht, solange ihr euch dafür hinsetzt. Es gibt keine Punktzahl und keinen Laden, den ihr gesehen haben müsst, um die Stadt verstanden zu haben.",
            "Die Abendfassung dieses Rhythmus steht auf der Seite zu den Abenden. Wollt ihr den Fluss am Ende des Wegs, ist das die nächste Seite.",
        ]),
    ],
    ["guide-markets", "guide-sights", "guide-evenings", "home"],
)

PAGES["guide-river"] = page(
    "Saigon-Fluss und Bootsfahrt | ASCON LIVING",
    "Der Saigon-Fluss für Besucher: was eine Bootsfahrt zeigt, wie ihr eine ruhige Tour wählt, und wie das Wasser den Rest der Stadt klarer ordnet.",
    "Der Saigon-Fluss und ein Boot darauf",
    "Der Fluss ist der Grund, warum die Stadt hier steht. Lastkähne bewegen noch Ware, Fähren kreuzen noch, und am Ufer öffnet sich endlich die Hitze der Straßen. Eine Bootsfahrt ist freiwillig. Hinschauen ist es nicht.",
    [
        ("Wofür der Fluss da ist", [
            "Vom Ufer seht ihr eine arbeitende Wasserstraße, keinen Kulissenkanal nur für Fotos. Frachtschiffe, Ausflugsdecks und gelegentlich ein Fischerboot teilen sich dieselbe Rinne. Das andere Ufer baut seit Jahren nach oben, also gehört die Skyline zur Ansicht, und sie ändert sich mit dem Licht mehr als mit einem einzelnen Turm.",
            "Ein Stück Gehweg ist die einfachste Fassung. Ihr bekommt die Brise, den Maßstab und ein klares Gefühl, wohin es flussab geht. Macht das, bevor ihr ein Boot bucht. Die Fahrt ergibt mehr Sinn, wenn ihr das Wasser vom Land schon kennt.",
        ]),
        ("Was eine Bootsfahrt zeigt", [
            "Die meisten Boote für Besucher legen an Stegen im Zentrum ab und fahren eine Schleife auf dem Hauptarm. Ihr kommt an Hafenkränen, Hausbooten, Brücken und dem Gegensatz zwischen älteren Speichern und neuen Türmen vorbei. Am Tag geht es um die Arbeit des Flusses. Später geht es um das Licht auf dem Wasser und die Stadt, die ihre Lichter anmacht.",
            "Die Begleitung ist unterschiedlich. Manche Boote erzählen Hafengeschichte, manche spielen Musik, manche reichen ein kaltes Getränk und lassen euch an der Reling stehen. Wählt die ruhigere Variante, wenn ihr schauen wollt, und die lebhaftere, wenn eure Runde einen gemeinsamen Abend will. In beiden Fällen sind die Ufer der Punkt, nicht eine Show an Deck.",
        ]),
        ("Wählen ohne Drängen", [
            "Bucht bei einem Anbieter, der euch Steg, Art des Boots und den Umfang nennt, bevor ihr zahlt. Eine kurze Schleife auf einem kleinen Boot fühlt sich anders an als ein großes Deck mit festem Menü. Wollt ihr kein Essen, sagt das. Wollt ihr sitzen statt tanzen, nehmt das Boot, das nach Sitzen aussieht.",
            "Fahrt an einem Tag, an dem ihr nicht schon erschöpft seid. Der Weg zum Steg kann voll sein, und das Einsteigen braucht Geduld. Nehmt eine leichte Schicht mit, wenn ihr schnell verbrennt, auch wenn die Stadt heiß wirkt, denn die Brise auf dem Wasser ist stärker, als sie von der Straße aussieht. Taschen bleiben zu, während ihr zwischen Steg und Deck wechselt.",
        ]),
        ("Wetter, Licht und Bequemlichkeit", [
            "Ein klarer später Nachmittag ist die leichte Wahl. In den Regenmonaten kann ein Schauer kommen und wieder gehen, und viele Boote warten ihn ab oder kürzen die Schleife. Das ist keine misslungene Fahrt. Der Fluss unter Wolken ist immer noch der Fluss, und die Stadt sieht ohne hartes Sonnenlicht anders aus.",
            "Ist der Himmel ein Dauerregen, nehmt das Ufer an einem anderen Tag zu Fuß und lasst das Boot aus. Es gibt keinen Preis dafür, in ein Unwetter zu fahren. Die Wetterseite erklärt die beiden Jahreszeiten genauer, ohne zu behaupten, eine einzelne Woche sei vorhersehbar.",
        ]),
        ("Nachdem ihr an Land seid", [
            "Das Zentrum liegt direkt da, wenn ihr anlegt. Ein Kaffee, ein kurzer Weg am Wasser oder eine direkte Fahrt zurück zum Haus sind vernünftige Enden. Stapelt keinen Museumsbesuch auf denselben Abend. Lasst die Fahrt das Ereignis sein.",
            "Die Dachterrasse des Hauses blickt auf Fluss und Skyline, ein anderer Winkel als das Deck: still, privat, und da an den Abenden, an denen ihr gar nicht hinauswollt. Ein Boot an einem Tag und die Terrasse an einem anderen sind ein vollständiger Fluss-Aufenthalt.",
        ]),
        ("Das Delta ist ein anderes Wasser", [
            "Das Mekong-Delta ist keine längere Fassung dieser Schleife. Es ist ein Tag außerhalb der Stadt, mit Obstgärten, schmaleren Armen und Dörfern. Wenn ihr das wollt, nehmt die Seite zu den Tagesausflügen und lasst den Saigon-Fluss das Wasser der Stadt sein.",
            "Beides passt in einen Aufenthalt. Es sollte nicht derselbe Tag sein. Der Stadtfluss ist ein Abend oder ein leichter Nachmittag. Das Delta verlangt den ganzen Tag und einen ruhigeren Morgen danach.",
        ]),
    ],
    ["guide-sights", "guide-daytrips", "guide-evenings", "home"],
)

PAGES["guide-evenings"] = page(
    "Abende in Saigon | ASCON LIVING",
    "Abende in Saigon, wenn ihr in einem ganzen Haus wohnt: Fußgängerzonen, Flussluft, Musik und ein Heimweg, der die Nacht nicht zum Projekt macht.",
    "Abende und Ausgehen in Saigon",
    "Saigon wechselt, wenn das Licht fällt. Die Gehwege füllen sich, die Flussbrise wird wichtig, und der Tag in den Museen wird ein Grund, sich zu setzen. Ihr braucht kein Nachtprogramm. Ihr braucht einen Plan und einen Weg nach Hause.",
    [
        ("Was die Stadt nach Einbruch tut", [
            "Die Fußgängerzonen im Zentrum, besonders um Nguyen Hue, sind die einfache Fassung des Ausgehens. Familien, Paare und Gruppen teilen denselben offenen Raum. Er ist beleuchtet, er ist öffentlich, und er reicht, wenn ihr nur draußen sein wollt. Ein Getränk oder ein Happen vom Rand dazu, und der Abend ist einer.",
            "Das Flussufer ist die ruhigere Alternative. Dasselbe Wasser, das ihr vom Boot sehen könnt, liegt für einen Spaziergang da, mit weniger Entscheidungen. War der Tag heiß, wird die Stadt jetzt wieder angenehm. Geht, solange ihr noch Lust habt zu schlendern, nicht als erzwungenen letzten Punkt.",
        ]),
        ("Sitzen, nicht abarbeiten", [
            "Ein guter Abend hier ist meist ein Viertel und ein oder zwei Stopps. Ein Café, das zur Bar wird, wenn die Karte kippt. Ein kleiner Raum mit Live-Musik. Eine späte Schüssel von etwas, das ihr schon bestellen könnt. Der Punkt ist der Tisch, die Leute, mit denen ihr da seid, und dass euch niemand in ein drittes Lokal schiebt.",
            "Laute Straßen für Besucher gibt es, und sie sind absichtlich laut. Geht durch, wenn ihr neugierig seid, und geht, wenn ihr genug gesehen habt. Ihr verpasst kein Geheimnis, wenn ihr den lautesten Block auslasst. Die besseren Räume sind die, in denen ihr die Person neben euch hört.",
        ]),
        ("Musik und ein eigener Raum", [
            "Live-Musik taucht in kleinen Räumen im Zentrum auf: eine Stimme, eine Gitarre, ein Saal für ein paar Dutzend Leute. Schaut am Vortag nach, wenn euch die Art wichtig ist, und kommt mit dem Gedanken, dass ihr einfach zuhören und gehen könnt. Das ist ein vollständiger Abend.",
            "Will eure Runde lieber singen als zusehen, hat Saigon private Singräume, und im Haus steht Karaoke. Die Fassung im Haus heißt: Der Raum, das Gerät und die Dachterrasse für Luft zwischen den Liedern sind schon da. Nehmt die Stadt, wenn ihr hinauswollt. Nehmt das Haus, wenn der Abend die Leute sind, mit denen ihr gekommen seid.",
        ]),
        ("Essen, ohne es zum Thema zu machen", [
            "Abends wollen viele einen richtigen Tisch: eine Karte, einen Ventilator oder Klimaanlage, und genug Stühle. Wählt den Ort am Nachmittag, nicht während ihr an einer Ecke steht. Märkte und Kaffee decken die Tagesfassung von Essen und Trinken ab. Nachts zählt Bequemlichkeit mehr als Neuheit.",
            "Ist jemand müde, teilt den Plan. Ein Teil kann hinaus. Das Haus hat Küche, einen großen Kühlschrank und ein Wohnzimmer mit großem Bildschirm, also ist Dableiben eine echte Wahl und kein Ausgleich. Ein Grill auf der Dachterrasse ist der mittlere Weg, wenn ihr Abendluft wollt, ohne eine Fahrt.",
        ]),
        ("Zurückkommen", [
            "Einigt euch auf die Fahrt, bevor ihr sie braucht. Ein Auto über eine Fahr-App oder ein Taxi von einem Stand, dem ihr schon traut, ist leichter als ein Handel auf lautem Pflaster. Die Seite zu Verkehr und Sicherheit erklärt die Gewohnheiten. Für den Abend selbst gilt: Entscheidet den Heimweg, solange ihr noch froh seid, dass ihr gegangen seid.",
            "Das Haus nutzt zur Anreise einen Zahlencode, das Außentor einen Schlüssel. Der Schlüssel bleibt in einer Tasche, die ihr später noch kennt, und liegt nicht auf einem Cafétisch. Die Ankunft nach einem Abend soll langweilig sein. Langweilig ist das Ziel.",
        ]),
        ("Eine Woche Abende", [
            "Ihr braucht nicht jeden Abend ein anderes Schauspiel. Wiederholt die Fußgängerzone. Wiederholt die Dachterrasse. Seht den Fluss einmal vom Wasser und einmal vom Ufer. Der Aufenthalt wird besser, wenn die Abende vertraut werden.",
            "Seid ihr länger da, skaliert dieselbe Logik: zwei Abende draußen, der Rest zu Hause, und am Morgen Kaffee. Das Wetter wird Pläne streichen. Lasst es. Saigon ist morgen noch draußen.",
        ]),
    ],
    ["guide-river", "guide-coffee", "guide-traffic", "home"],
)

PAGES["guide-daytrips"] = page(
    "Mekong-Delta und Cu-Chi-Tunnel | ASCON LIVING",
    "Zwei klassische Tage außerhalb von Saigon: Wasser und Obstgärten im Mekong-Delta, die Cu-Chi-Tunnel, und wie ihr für den Aufenthalt zwischen beiden wählt.",
    "Tagesausflüge: Mekong-Delta und Cu-Chi-Tunnel",
    "Das sind die beiden Ausflüge, die Leute meinen, wenn sie fragen, was es jenseits von Saigon gibt. Es sind verschiedene Tage. Einer ist Wasser, Obst und Dörfer. Der andere ist Geschichte unter der Erde. Wählt einen, gebt ihm den ganzen Tag, und lasst die Stadt für die Tage drumherum.",
    [
        ("Zwei Fahrten, zwei Stimmungen", [
            "Das Mekong-Delta ist eine Landschaft. Ihr fahrt aus der Stadt zu schmaleren Armen, Obstgärten, Werkstätten und Häusern, die zum Wasser zeigen. Die Freude ist, weg vom Verkehr zu sein und zu sehen, wie das Flusssystem den Süden ernährt. Es ist sanft, wenn ihr einen ruhigen Anbieter wählt, und anstrengend, wenn der Tag zu viele Stopps stapelt.",
            "Cu Chi ist eine historische Stätte. Die Tunnel sind ein Rest der Kriege des zwanzigsten Jahrhunderts, erhalten und stellenweise erweitert, damit Besucher ein kurzes Stück kriechen können. Es ist ernst mehr als hübsch. Fahrt hin, weil ihr die Geschichte wollt, nicht weil ihr einen hübschen Nachmittag sucht.",
        ]),
        ("Das Delta, ohne Drehbuch", [
            "Ein typischer Deltatag enthält ein Boot auf einem schmalen Arm, einen Weg durch Obstbäume und einen Blick in eine kleine Werkstatt: Kokosbonbons, Reispapier oder etwas Ähnliches. Man bietet euch Obst an. Man bietet euch einen Platz an. Nehmt die Teile, die ihr wollt, und behandelt den Rest als freiwillig.",
            "Die Landschaft ist der Punkt, also wählt einen Anbieter, der Zeit auf dem Wasser verbringt und nicht nur im Laden. Eine kleinere Gruppe fühlt sich mehr nach Besuch an und weniger nach Kolonne. Zieht Kleidung an, in der ihr auf einem Holzboot sitzen könnt, und nehmt einen Hut mit. Die Sonne auf dem Wasser ist stärker als die Sonne zwischen Häusern.",
        ]),
        ("Cu Chi, und wie ihr es nehmt", [
            "Über der Erde seht ihr Eingänge, Fallen, die als Geschichte erklärt werden, und eine Landschaft aus Eukalyptus und Gestrüpp, die verbirgt, was darunter gegraben wurde. Unter der Erde sind die für Besucher geöffneten Stücke kurz, niedrig und warm. Ihr könnt das Kriechen auslassen und den Ort trotzdem von den Tafeln und den freigelegten Gräben her verstehen.",
            "Schuhe mit Grip, Kleidung, der Staub nichts ausmacht. Ist jemand in engen Räumen unwohl, sagt das, bevor die Person am Eingang steht. Die Stätte ist Gedenkort und Museum. Laute Witze werden schnell dünn. Lest am Vorabend ein wenig, damit der Boden Sinn ergibt, wenn ihr ankommt.",
        ]),
        ("Wählen und kombinieren", [
            "Habt ihr einen Tag, wählt nach den Leuten, mit denen ihr reist. Gärten und Boote passen zu einer gemischten Runde, die einen leichten gemeinsamen Tag will. Cu Chi passt zu Leuten, die nach dem Krieg gefragt haben und eine ernsthafte Antwort aushalten. Keines ist die Belohnung dafür, das andere geschafft zu haben.",
            "Beides am selben Tag macht beides schlechter. Sie liegen in verschiedenen Richtungen und verlangen verschiedene Aufmerksamkeit. Ist der Aufenthalt lang genug, legt einen ruhigen Stadttag dazwischen. Ist er es nicht, wählt eines und lasst das andere für ein Wiederkommen.",
        ]),
        ("Die Form des Tages", [
            "Behandelt es als ganzen Tag draußen. Frühstückt im Haus, wo Küche und Kaffeemaschine einen frühen Start einfach machen, und kommt rechtzeitig für einen langsamen Abend zurück. Bucht an dem Datum keine Flussrundfahrt und keine späte Musik. Der Ausflug ist der Tag.",
            "Wasser, eine leichte Schicht gegen die Sonne, und etwas Bargeld für Obst oder ein Getränk unterwegs. Den Abholpunkt klärt ihr am Vortag. Self-Check-in im Haus heißt, ihr müsst bei der Rückkehr keinen Empfang einholen. So endet ein langer Ausflug richtig.",
        ]),
        ("Ordentlich buchen", [
            "Nehmt einen benannten Anbieter, der Treffpunkt und Umfang bestätigt, bevor ihr zahlt. Fragt, ob die Zeit auf dem Boot ein echtes Stück Wasser ist oder nur ein kurzer Wechsel zwischen Läden. Fragt, ob der Tunnelbesuch das Kriechen einschließt oder nur das Gelände. Klare Antworten sind das Zeichen, das ihr wollt.",
            "Die Stadt hat mehr zu tun als diese beiden Fahrten, und ein Aufenthalt ist ohne sie nicht unvollständig. Es sind gute Tage. Sie sind nicht Pflicht. Sehenswürdigkeiten, Märkte und der Fluss in Saigon füllen allein eine Woche.",
        ]),
    ],
    ["guide-river", "guide-sights", "guide-weather", "home"],
)

PAGES["guide-weather"] = page(
    "Wetter und Reisezeit Saigon | ASCON LIVING",
    "Wetter in Saigon in klarer Sprache: die trockeneren Monate, die Regenmonate, Hitze, die bleibt, und was ihr für ein ganzes Haus einpacken solltet.",
    "Wetter in Saigon und wann ihr kommt",
    "Saigon ist in jedem Monat warm, der euren Namen trägt. Die nützliche Frage ist nicht, ob es heiß sein wird. Sie ist, ob ihr lieber trockene Gehwege oder dramatische Himmel wollt, und wie ihr die Mitte des Tages verbringt.",
    [
        ("Zwei Jahreszeiten, ein Klima", [
            "Die trockeneren Monate laufen meist etwa von Dezember bis April. Der Himmel ist klarer, Regen seltener, und das Zentrum lässt sich leichter gehen. Es bleibt heiß, besonders vom späten Vormittag bis in den Nachmittag. Der Unterschied ist, dass ihr einen Vormittag draußen mit mehr Vertrauen planen könnt.",
            "Die Regenmonate laufen meist etwa von Mai bis November. Regen kommt oft als kräftiger Schauer und nicht als ein ganzer Tag Niesel, obwohl manche Tage einfach grau bleiben. Straßen können an tiefen Stellen kurz unter Wasser stehen und sich dann leeren. Ihr plant mit einem Ersatz, nicht mit einer gestrichenen Woche.",
        ]),
        ("Die trockeneren Monate", [
            "Dezember bis Februar finden viele Besucher am leichtesten. Die Hitze ist echt, aber weniger hart, und die Abende taugen für Fluss und Fußgängerzonen. März und April werden heißer, bevor der Regen zurückkehrt. Wer in großer Hitze nachlässt, zielt auf den früheren Teil der trockenen Zeit und hält die Mitte des Tages drinnen.",
            "In diesen Monaten reisen auch mehr Leute. Bucht das Haus für die Daten, die ihr wollt, statt anzunehmen, eine Woche sei offen. Die Stadt ist nicht interessanter, weil sie voller ist. Sie ist einfach voller, und Tet, das Mondneujahr, kann Verkehr und Essen für einige Tage um den Feiertag herum umstellen.",
        ]),
        ("Die Regenmonate", [
            "Ein Aufenthalt in der Regenzeit ist kein Fehler. Vormittage sind oft klar genug fürs Zentrum oder einen Markt, und der Schauer wird das Zeichen, in einem Museum, einem Café oder zurück im Haus zu sein. Die Luft kann schwer wirken. Der Gewinn sind grünere Straßen und weniger Anspruch, jede Zeit draußen zu verbringen.",
            "Packt eine leichte Regenjacke ein statt eines Schirms, den ihr an einer windigen Ecke bekämpft, und Schuhe, die nass werden und wieder trocknen dürfen. Ein Tag im Delta oder in Cu Chi bleibt möglich. Schaut auf den Morgenhimmel und die Notiz des Anbieters, und seid bereit, den Ausflug um einen Tag zu verschieben. Tunnel und Obstgärten laufen nicht ab.",
        ]),
        ("Hitze und die Mitte des Tages", [
            "In jedem Monat baut den Tag um die Hitze. Draußen gehen, solange es früher ist, ein langes Essen oder eine Pause, wenn die Sonne hoch steht, und der Fluss oder ein Viertel später. Das ist keine Faulheit. So legen Leute, die hier leben, einen gewöhnlichen Dienstag.",
            "Das Haus gehört zu diesem Plan. Klimaanlage läuft in jedem Schlafzimmer und im Wohnzimmer. Ein dunkles, ruhiges Zimmer in der Mitte des Tages ist eine Eigenschaft des Aufenthalts, kein Scheitern des Plans. Trinkt Wasser, bevor es dramatisch wird. Die Sonne hier ist stärker, als ein bewölkter Morgen vermuten lässt.",
        ]),
        ("Was ihr einpackt", [
            "Leichte Kleidung, die ihr waschen könnt, einen Hut, Sonnenschutz und eine Schicht für kräftige Klimaanlagen drinnen. Für Pagoden bedeckte Schultern und Knie. Schuhe, in denen ihr auf unebenen nassen Fliesen lauft. Eine kleine Tasche, die ihr quer tragt.",
            "Im Haus stehen Waschmaschine und Bügeleisen, also braucht eine Woche Kleidung keinen großen Koffer. Eine Wäsche kann man auch abgeben, wenn ihr die Tasche lieber aus der Hand gebt. Packt trotzdem für die ersten Tage, und lasst die Maschine den Rest übernehmen.",
        ]),
        ("Welche Wochen ihr wählt", [
            "Kommt in den trockeneren Monaten, wenn Gehen draußen das Herz der Reise ist. Kommt in den Regenmonaten, wenn ihr Cafés, Museen und das Haus gern mit den Schauern mischt. Kommt außerhalb des Tet-Drangs, wenn ihr mehr Wahl bei den Daten wollt. Keine dieser Städte ist die falsche.",
            "Sehenswürdigkeiten, Märkte und Tagesausflüge funktionieren in beiden Zeiten. Sie ändern nur die Form. Lest auch die Seite zum Verkehr, wenn die Straßen neu für euch sind, denn nasse und trockene Fahrbahnen verlangen dieselben Gewohnheiten, mit etwas mehr Geduld, wenn es gerade geregnet hat.",
        ]),
    ],
    ["guide-sights", "guide-daytrips", "guide-traffic", "home"],
)

PAGES["guide-arrival"] = page(
    "Anreise vom Flughafen Saigon | ASCON LIVING",
    "Ankunft am Tân Sơn Nhất und der Weg zum Haus: privater Transfer nur auf Anfrage, Fahr-Apps, offizielle Taxis und Self-Check-in an der Haustür.",
    "Vom Flughafen bis zum Haus",
    "Der Hauptflughafen von Ho-Chi-Minh-Stadt ist Tân Sơn Nhất, Kennung SGN. Er liegt im Stadtgebiet, mit getrennten Bereichen für internationale und innere Flüge. Die nützliche Frage nach der Landung ist nicht, welche Sehenswürdigkeit zuerst kommt. Sie ist, wie ihr das letzte Stück zurücklegt und was an der Tür passiert.",
    [
        ("Bevor ihr landet", [
            "Habt die Adresse auf Vietnamesisch: 389A Duong Tran Xuan Soan, Tan Hung, Ho-Chi-Minh-Stadt. Ein Screenshot reicht, wenn eure Daten noch nicht laufen. Speichert unsere Telefonnummer, bevor ihr fliegt, damit ein Fahrer oder ein Formular nicht der Moment ist, in dem ihr danach sucht.",
            "Die wichtigen Dinge gehören ins Handgepäck: Pass, Adresse und jede Notiz, die wir zur Ankunft geschickt haben. Aufgabegepäck kann dauern. Ihr müsst keinen Stadtplan anfangen, bevor ihr mit den Taschen wirklich vor dem Terminal steht.",
        ]),
        ("Ein Transfer auf Anfrage", [
            "Einen privaten Transfer vom Flughafen gibt es auf Anfrage. Er wird einem Aufenthalt nicht hinzugefügt, wenn ihr nicht fragt. Schreibt uns Flugnummer und Landezeit, wenn ihr bucht oder sobald der Flug feststeht, und wir bestätigen, ob wir diese Ankunft übernehmen können.",
            "Auf Anfrage heißt: Geht nicht davon aus, dass ein Fahrer wartet, wenn ihr keine Rückmeldung habt. Verschiebt sich der Flug, sagt uns Bescheid. Wollt ihr selbst fahren, ist das eine normale Wahl und braucht keine Entschuldigung. Das Haus ist dasselbe.",
        ]),
        ("Fahr-Apps und offizielle Taxis", [
            "Fahr-Apps holen euch an ausgewiesenen Stellen vor den Terminals ab. Verbindet euch zuerst mit den Daten des Flughafens oder einer lokalen SIM, bestellt das Auto in der App und gleicht das Kennzeichen ab, bevor ihr einsteigt. Die App ist Beleg und Route. Am Bordstein müsst ihr keinen Preis aushandeln.",
            "Offizielle Taxis stehen an markierten Reihen. Nehmt diese Wagen, lasst euch bestätigen, dass das Taxameter läuft, und ignoriert Angebote von Leuten, die euch in der Ankunftshalle ansprechen. Fühlt sich ein Gespräch wie Drängen an, geht zurück zur Reihe. Dieselben Gewohnheiten für den Rest des Aufenthalts stehen auf der Verkehrsseite.",
        ]),
        ("Die Fahrt selbst", [
            "Ihr durchquert eine beschäftigte Stadt. Der Verkehr ändert sich mit der Tageszeit, mit Regen und mit dem, was die Straßen an dem Nachmittag tun. Lasst Spielraum, wenn euch jemand erwartet oder wenn ihr am selben Abend noch etwas vorhabt. Es gibt keine eine Dauer, die sich zu merken lohnt, denn die Stadt schuldet euch keine.",
            "Lehnt euch zurück, haltet die Adresse sichtbar und lasst die Person fahren. Eine Übersetzungs-App hilft, wenn ihr eine Abbiegung bestätigen wollt. Ihr müsst nicht navigieren. Sieht die Route seltsam aus, ist die Karte in der App die ruhige Prüfung, kein Streit an einer Kreuzung.",
        ]),
        ("Am Haus", [
            "Der Check-in läuft von 14:00 bis 23:00. Der Check-out ist um 12:00. Der Self-Check-in nutzt ein Tastenfeld. Das Außentor nutzt einen eigenen Schlüssel. Wir schicken die Angaben zu eurem Aufenthalt, bevor ihr kommt, damit ihr nicht auf dem Gehweg auf eine Person mit Klemmbrett wartet.",
            "Landet euer Flug außerhalb dieses Fensters, sagt uns das vor dem Tag selbst. Kameras draußen erfassen den Eingang. Das ist eine Tatsache des Hauses, kein Versprechen über die Straße. Drinnen zählen Küche, Klimaanlage und eine Dusche mehr als jeder weitere Plan.",
        ]),
        ("Der erste Abend", [
            "Haltet die erste Nacht klein. Ein Spaziergang, wenn ihr Kraft habt, oder Essen in der Nähe und ein frühes Ende, wenn nicht. Die Seite zu Geld, SIM und Apps lest ihr im Flugzeug, wenn ihr Daten und Bargeld schnell ordnen wollt. Die Sehenswürdigkeiten können bis zum Morgen warten. Das Haus ist schon da, auch wenn der Flug später war als gedacht, und ein Glas Wasser zählt mehr als ein weiterer Plan.",
            "Das ganze Haus gehört euch ab dem Check-in. Das ist der Sinn, irgendwo anzukommen, das keine Lobby ist. Tor schließen, das Tastenfeld einmal lernen, und den Rest der Stadt auf morgen legen.",
        ]),
    ],
    ["guide-practical", "guide-traffic", "guide-weather", "home"],
)

PAGES["guide-practical"] = page(
    "Geld, SIM und Apps in Saigon | ASCON LIVING",
    "Geld, SIM und Apps für Saigon, praktisch: Dong und Karten, eine lokale SIM oder eSIM, und Karten- sowie Fahr-Apps für ganz gewöhnliche Tage.",
    "Geld, eine SIM und die Apps, die helfen",
    "Saigon wird leicht, sobald das Telefon Daten hat und die Tasche kleine Scheine. Alles andere ist eine Variation dieser zwei Tatsachen. Richtet sie früh ein, und die übrigen Seiten werden einfacher.",
    [
        ("Dong, Bargeld und Karten", [
            "Die Währung ist der Dong, und die Zahlen sind lang. Zählt die Nullen, bevor ihr einen Schein abgebt, und zählt sie noch einmal, wenn ihr Wechselgeld bekommt. Karten funktionieren in vielen größeren Restaurants und Läden. Märkte, Bürgersteigkaffee und kleine Schüsseln erwarten noch Bargeld. Tragt beides, und verlasst euch bei dem Stand, den ihr wirklich wollt, nicht auf die Karte.",
            "Geldautomaten stehen dicht im Zentrum und an größeren Häusern. Nehmt Geräte an einer Bank, wenn ihr könnt, und deckt das Feld ab. Sagt eurer Bank, dass ihr reist, damit die Karte nicht am ersten Tag sperrt. Ihr müsst am Flughafen keine große Summe tauschen, wenn ein kleinerer Betrag euch zum Haus und durch die ersten Mahlzeiten bringt.",
        ]),
        ("Kleine Scheine und der Alltag", [
            "Wechselt große Scheine früh, in einem Café oder Laden, der das ohne Rede tun kann. Fahrer und Marktstände haben nicht immer Wechselgeld für die größten Noten. Eine eigene Tasche für das Geld, das ihr an dem Tag ausgeben wollt, und eine tiefere für den Rest.",
            "Fragt, was ihr schuldet, bevor ihr euch an einen Ort ohne Karte setzt, und schaut auf die Summe, bevor ihr zahlt. Das ist gewöhnliche Sorgfalt, kein Misstrauen. Die Verkehrsseite deckt die Fassung für Fahrten ab. Bei Essen und Kaffee verhindert eine klare Zahl am Anfang den einzigen Streit, der sich zu vermeiden lohnt.",
        ]),
        ("SIM und eSIM", [
            "Eine lokale SIM oder eine eSIM ist der Unterschied zwischen einem sicheren Tag und einem Tag, an dem ihr nach WLAN sucht. Eine eSIM könnt ihr vor dem Flug einrichten, wenn das Telefon das kann, oder eine Besucher-SIM am Flughafen oder in der Stadt kaufen. Nehmt den Pass mit. Das Personal tut das den ganzen Tag und hat meist eine kurze Auswahl an Datenpaketen.",
            "Prüft die Daten, bevor ihr den Schalter verlasst. Ladet eine Karte, schickt euch eine Nachricht und speichert die Hausadresse offline. Das WLAN im Haus ist schnell, Glasfaser bis zu 1 Gbit/s mit Mesh auf jeder Etage, also hängt ihr zu Hause nicht an mobilen Daten. Für die Rückfahrt wollt ihr sie trotzdem.",
        ]),
        ("Karten, Übersetzung und Fahrten", [
            "Ladet eine Offline-Karte der Stadt, bevor ihr sie braucht. Markiert das Haus, den Flughafen und jeden Ort, den ihr schon besuchen wollt. Eine Übersetzungs-App mit Kamera hilft bei Speisen und Schildern. Ladet das Sprachpaket, damit es in einem Treppenhaus ohne Empfang funktioniert.",
            "Eine Fahr-App ist der einfachste Weg, mit Gepäck oder im Regen zu fahren. Richtet sie im WLAN des Flughafens ein, wenn ihr es nicht zu Hause getan habt, und zahlt in der App, wenn ihr könnt. Das Auto, dessen Kennzeichen zum Bildschirm passt, ist das Auto, das ihr wollt. Dieselbe App ist am Ende eines Abends nützlich, deshalb schickt euch die Abendseite hierher.",
        ]),
        ("Kontakte und Kopien", [
            "Speichert unsere Telefonnummer, und haltet ein Foto des Passes griffbereit, falls der Pass tief in der Tasche liegt. Teilt die Hausnadel mit den Leuten, mit denen ihr reist, damit niemand von einem einzigen Telefon abhängt. Die Adresse auf Vietnamesisch steht auf der Flughafenseite.",
            "Die Nachrichten-Apps, die ihr schon nutzt, reichen, um uns zu erreichen. Ihr braucht kein neues Konto nur der Form halber. Braucht ein Formular oder ein Fahrer eine lokale Nummer, ist die SIM, die ihr gerade gekauft habt, diese Nummer. Schreibt sie auf. Ihr werdet sie nicht behalten.",
        ]),
        ("Was diese Seite nicht leistet", [
            "Diese Seite ist keine Liste von Läden, Banken oder Tarifen, und sie nennt keinen Kurs, der nächsten Monat falsch wäre. Geld und Daten sind Werkzeuge. Sobald sie funktionieren, geht zu den Sehenswürdigkeiten, den Märkten oder zum Kaffee und benutzt sie.",
            "Wenn etwas scheitert, lösen ein zweiter Automat, ein zweites Café mit WLAN oder eine Nachricht an uns mehr als ein langer Ratgeber. Das Haus ist der Rückfall: Strom, Wasser, eine Küche und eine Verbindung, die nicht vom Stand draußen abhängt.",
        ]),
    ],
    ["guide-arrival", "guide-traffic", "guide-markets", "home"],
)

PAGES["guide-traffic"] = page(
    "Verkehr und Sicherheit in Saigon | ASCON LIVING",
    "Verkehr und Alltagssicherheit in Saigon: wie Straßen sich bewegen, wie ihr überquert, wie ihr fahrt, und ruhige Gewohnheiten für den ganzen Aufenthalt.",
    "Verkehr und Alltagssicherheit in Saigon",
    "Die Straßen sehen chaotisch aus und sind es meist nicht. Motorräder fließen, Autos schieben sich in die Lücken, und Leute überqueren, weil der Fluss eine Logik hat. Lernt die Logik einmal, und die Stadt hört auf, sich wie eine Mutprobe anzufühlen.",
    [
        ("Wie die Straßen sich bewegen", [
            "Motorräder sind das Hauptereignis. Sie bewegen sich in Strömen, schieben sich nach vorn und erwarten, dass Fußgänger berechenbar sind. Autos und Busse sind weniger und weniger wendig. Hupen sind eher ein Zeichen der Anwesenheit als ein Tadel. Der Lärm ist Information.",
            "Gehwege teilt ihr mit abgestellten Rädern, Kochen und gelegentlich einem Hocker. Ihr werdet auf die Fahrbahn treten. Das ist normal. Es ist kein Grund, zu erstarren oder zu sprinten. Der Abschnitt zum Überqueren ist die ganze Fertigkeit.",
        ]),
        ("Überqueren", [
            "Wählt einen Punkt, an dem andere schon gehen, wartet auf eine Lücke im nächsten Strom und geht in gleichmäßigem Tempo. Haltet die Linie gerade. Fahrer passen sich an, wenn ihr sie nicht überrascht. Blickkontakt hilft. Ein plötzlicher Schritt zurück ist gefährlicher als ein ruhiger Schritt nach vorn.",
            "Mit Kindern macht ihr das an der Hand und bewegt euch als eine Person, nicht als eine Kette, die in der Mitte zögert. Nachts überquert ihr, wo Licht ist. Seid ihr müde oder tragt Taschen, nehmt für die langen Stücke eine Fahrt und überquert nur das letzte kurze Stück. Stolz ist kein Verkehrsmittel.",
        ]),
        ("Fahrten", [
            "Für alles mit Gepäck, Regen oder einem Ziel, das ihr nicht kennt, nehmt ein Auto über eine Fahr-App oder ein offizielles Taxi. Gleicht das Kennzeichen ab. Legt den Gurt an, wenn einer da ist. Ein Motorradtaxi ist eine lokale Gewohnheit, die Besucher auslassen können, ohne etwas Wichtiges zu verpassen, besonders mit Taschen oder nach Einbruch.",
            "Schaut die Route auf dem eigenen Telefon an, wenn ihr wollt, und sagt früh Bescheid, wenn sie abweicht, mit einer Übersetzungs-App statt mit Lautstärke. Zahlt so, wie ihr es am Anfang vereinbart habt. Die Geldseite deckt Bargeld und Karten ab. Die Flughafenseite deckt die Reihe vor dem Terminal ab, dieselbe Idee an einem volleren Ort.",
        ]),
        ("Taschen, Telefone und Getränke", [
            "Tragt die Tasche quer und haltet die Öffnung in Gedränge und auf dem Gehweg an euch. Telefone verlassen Hände schnell, wenn sie an der Tischkante liegen oder auf der Fahrbahn benutzt werden. Tretet an den Rand eines Gehwegs, bevor ihr auf eine Karte schaut.",
            "Lasst ein Getränk oder ein Telefon nicht bei einer fremden Person, während ihr weggeht. Nehmt keine Fahrt von jemandem an, der weder Taxameter noch App nutzt. Das sind langweilige Regeln, weil sie funktionieren. Die Stadt ist kein Rätsel, das euch fangen soll. Sie ist ein voller Ort, an dem unbeaufsichtigte Dinge sich bewegen.",
        ]),
        ("Gesundheit und Papiere", [
            "Trinkt Wasser, nutzt Sonnenschutz und nehmt die Mittagshitze ernst. Magenfragen kommen meist vom Tempo, vom Eis und von neuem Essen, nicht von einem einzelnen gefährlichen Gericht. Esst, wo das Essen sich bewegt und wo andere Leute essen. Wascht die Hände. Die Küche im Haus ist da, wenn ihr eine einfache Mahlzeit selbst machen wollt.",
            "Tragt eine Kopie des Passes und haltet das Original sicher. Notiert die Nummer einer Klinik, die eure Versicherung empfiehlt, bevor ihr sie braucht. Im Notfall erreicht 113 die Polizei und 115 einen Krankenwagen. Speichert sie. Ihr werdet sie wahrscheinlich nie nutzen, und das ist das richtige Ergebnis.",
        ]),
        ("Das Haus als ruhiges Ende", [
            "Kameras draußen sehen den Eingang. Der Self-Check-in ist ein Tastenfeld, das Außentor ein Schlüssel. Das ist die Sicherung, die wir wirklich haben. Nutzt sie: Tor schließen, den Code nicht in einen Chat mit Leuten legen, die nicht zu eurer Reise gehören, und uns sagen, wenn an der Tür etwas falsch aussieht.",
            "Nichts davon soll die Reise kleiner machen. Überquert die Straße, nehmt den Fluss, setzt euch auf den kleinen Hocker. Die Gewohnheiten oben sorgen dafür, dass diese gewöhnlichen Freuden gewöhnlich bleiben. Die Abendseite ist die Nachtfassung, die Flughafenseite lest ihr noch im Flugzeug.",
        ]),
    ],
    ["guide-arrival", "guide-evenings", "guide-practical", "home"],
)

PAGES["audience"] = page(
    "Ganzes Haus für Familien und Freunde | ASCON LIVING",
    "Warum ein ganzes privates Haus in Ho-Chi-Minh-Stadt zu Familien, Freundesgruppen und längeren Aufenthalten passt: drei Etagen, eine Küche und keine Lobby.",
    "Ein ganzes Haus für Familien, Freunde und längere Aufenthalte",
    "Manche Reisen werden leichter, wenn der ganze Ort euch gehört. Familien brauchen Schlafzimmer, die nicht einen Flur voneinander entfernt sind. Freunde brauchen eine Küche und ein Dach. Ein längerer Aufenthalt braucht eine Waschmaschine und einen richtigen Kühlschrank. Dieses Haus ist ein privates Haus für eine Reisegruppe.",
    [
        ("Eine Reisegruppe, das ganze Haus", [
            "Ihr mietet das gesamte Haus, nicht ein Zimmer darin. Es gibt drei Etagen plus eine Dachterrasse und mehr als 250 Quadratmeter. Keine anderen Reisenden teilen Küche, Wohnzimmer oder Treppe. Am Eingang hängen Kameras draußen. Der Self-Check-in läuft über ein Tastenfeld, das Außentor über einen Schlüssel, also hängt die Ankunft nicht davon ab, jemanden in einer Lobby zu treffen.",
            "Der Check-in läuft von 14:00 bis 23:00. Der Check-out ist um 12:00. Die Sprachen im Haus sind Deutsch, Englisch, Hindi, Punjabi, Urdu und Vietnamesisch. Das sind die praktischen Ränder des Aufenthalts. Der Grund, das Haus zu wählen, ist, was ihr darin tun könnt, sobald das Tor zu ist.",
        ]),
        ("Für Familien", [
            "Es gibt drei Schlafzimmer, jedes mit eigenem Bad, plus ein Gäste-WC. Eltern und Kinder oder drei Generationen können sich auf die Etagen verteilen und sich trotzdem in der Küche treffen. Klimaanlage deckt jedes Schlafzimmer und das Wohnzimmer ab, vier Geräte insgesamt, und das zählt in jedem Monat, den Saigon anbietet.",
            "Die Küche ist privat: ein Kühlschrank von etwa 540 Litern, eine Spülmaschine, ein Ofen, eine Mikrowelle und eine Kaffeemaschine. Frühstück kann an dem Tisch stattfinden, den ihr nicht teilt. Das Wohnzimmer hat etwa 40 Quadratmeter, mit einem 75-Zoll-4K-Fernseher. Ein 4K-Projektor macht einen Filmabend, ohne das Haus zu verlassen. Das Hauptschlafzimmer hat etwa 55 Quadratmeter, also hält ein Raum tatsächlich einen Familienstapel Taschen aus.",
        ]),
        ("Für eine Runde Freunde", [
            "Freunde wollen oft den Abend mehr als den Plan. Die Dachterrasse hat etwa 56 Quadratmeter, mit Blick auf Fluss und Skyline, einem Grill und einem Smoker. Karaoke ist im Haus, also braucht das Singen keine Buchung irgendwo in der Stadt. Eine Spielkonsole ist da für die Zeit, in der niemand hinauswill.",
            "Drei Etagen heißen: Eine Person kann schlafen, eine kochen, eine auf dem Dach sein. Glasfaser läuft bis zu 1 Gbit/s, mit Mesh-WLAN auf allen Etagen, also hängt ein Anruf nach Hause nicht davon ab, wer gerade streamt. Das Gäste-WC hält die Schlange am Morgen kürzer. Nichts davon ist ein Programm. Es ist Raum.",
        ]),
        ("Für einen längeren Aufenthalt", [
            "Ein längerer Aufenthalt ist eine Reihe gewöhnlicher Tage. Waschmaschine und Bügeleisen machen das möglich, und ein Wäscheservice ist für 30 EUR pro Waschgang da, wenn ihr die Kleidung abgeben wollt. Der große Kühlschrank und der Ofen heißen, dass nicht jede Mahlzeit draußen stattfinden muss. Die Kaffeemaschine deckt die frühe Zeit ab, bevor die Stadt sich lohnt.",
            "WLAN auf jeder Etage und Klimaanlage in den Räumen, in denen ihr wirklich sitzt, machen eine zweite Woche zu Wohnen statt zu Camping. Self-Check-in heißt, eine späte Rückkehr vom Flughafen oder vom Delta braucht keinen Empfang. Ihr kommt an euer eigenes Tor zurück.",
        ]),
        ("Was wirklich da ist", [
            "Die bestätigte Liste ist konkret. Das ganze Haus, allein für euch. Drei Etagen und eine Dachterrasse. Drei Schlafzimmer mit eigenem Bad und ein Gäste-WC. Klimaanlage in den Schlafzimmern und im Wohnzimmer. Glasfaser und Mesh-WLAN. Eine Küche mit den Geräten, die oben genannt sind. Ein 75-Zoll-4K-Fernseher, weitere 4K-Bildschirme, ein Projektor, Karaoke und eine Spielkonsole. Eine Dachterrasse mit Fluss- und Skylineblick, Grill und Smoker. Check-in per Tastenfeld, ein Schlüssel fürs Tor, Kameras am Eingang.",
            "Braucht ihr ein Detail, das nicht auf dieser Liste steht, fragt auf der Buchungsseite, bevor ihr es annehmt. Das Haus ist das auf den Fotos. Die Stadtseiten hier decken Sehenswürdigkeiten, Märkte, Kaffee, den Fluss, Abende, Tagesausflüge, Wetter, den Flughafen, Geld und die Straßen ab, für die Zeit, in der ihr nicht zu Hause seid.",
        ]),
        ("Wie ihr entscheidet", [
            "Wählt das Haus, wenn eure Runde eine Haustür will. Eine Familie, die mittags neu starten will, Freunde, die Dach und Küche wollen, oder ein längerer Aufenthalt, der Wäsche und WLAN braucht, sind die Aufenthalte, zu denen es passt. Auf der Buchungsseite werden die Daten bestätigt.",
            "Lest den Flughafentext vor dem Flug und den Wettertext vor dem Packen. Dann hört auf zu lesen und kommt. Die Stadt ist der Grund der Reise. Das Haus ist der Grund, warum die Reise ruhig bleiben kann.",
        ]),
    ],
    ["guide-sights", "guide-weather", "guide-coffee", "home"],
)
