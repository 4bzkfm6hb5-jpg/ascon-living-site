"""Remaining city-note languages. Imported by tools/add_guest_city_notes.py."""

def register(DATA, page, S, L):
    es(DATA, page, S, L)
    fr(DATA, page, S, L)
    pt(DATA, page, S, L)
    it(DATA, page, S, L)
    nl(DATA, page, S, L)
    pl(DATA, page, S, L)
    ru(DATA, page, S, L)
    sv(DATA, page, S, L)
    tr(DATA, page, S, L)
    id_(DATA, page, S, L)
    ms(DATA, page, S, L)
    th(DATA, page, S, L)
    hi(DATA, page, S, L)
    pa(DATA, page, S, L)
    ur(DATA, page, S, L)
    ar(DATA, page, S, L)
    zhtw(DATA, page, S, L)

def es(DATA, page, S, L):
    g, tg = 'guía de viaje de Saigón', 'guía de lugares para quien se aloja'
    home = 'La casa se presenta en la <a href="{L}">página de inicio</a>.'
    DATA['es'] = dict(
        btn='Reserva y contacto',
        book='Si quieres alojarte en Ciudad Ho Chi Minh, la página de reserva y contacto indica cómo reservar la casa.',
        more_h2='Más páginas en este sitio',
        hub_h2='Cuatro temas para un día en Saigón',
        hub_p='Cuatro páginas sobre la lluvia, un solo día en el centro, una salida en familia o en grupo, y la comida de calle.',
        cards=[
            ['Saigón en un día de lluvia', 'guide-note-rain', 'Museos, mercado cubierto y cafés cuando llueve.'],
            ['Saigón en un día', 'guide-note-day', 'Una vuelta por el centro, sin intentar verlo todo.'],
            ['Saigón en familia o en grupo', 'guide-note-group', 'Zoo, títeres de agua y una comida compartida.'],
            ['Comida de calle en Saigón', 'guide-note-food', 'Phở, bánh mì, cơm tấm y cómo elegir un puesto.'],
        ],
        links={
            'rain': L('Para completar un día de lluvia, abre la ', g, ' y la ', tg, home),
            'day': L('Para armar el día con más calma, abre la ', g, ' y la ', tg, home),
            'group': L('Si viajas en familia o en grupo, abre la ', g, ' y la ', tg, home),
            'food': L('Si buscas más sitios para comer y caminar, abre la ', g, ' y la ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigón bajo la lluvia: planes a cubierto',
                'En Ciudad Ho Chi Minh, los chaparrones son habituales de mayo a noviembre. Museos, palacio, correos y cafés permiten seguir el día bajo techo.',
                'Saigón en un día de lluvia',
                'La lluvia no tiene por qué cancelar un día en Ciudad Ho Chi Minh. Museos, un mercado cubierto y cafés son el plan habitual bajo techo.',
                [S('Los meses de lluvia', 'Ciudad Ho Chi Minh es tropical. Los chaparrones son habituales de mayo a noviembre, y el tiempo más seco es más típico de diciembre a abril. Tras una lluvia fuerte, los puntos bajos pueden retener agua un momento y luego drenar. En los meses húmedos conviene tener una parada bajo techo.'),
                 S('Lugares bajo techo', ul=[
                    'Museo de los Vestigios de la Guerra, Museo de Bellas Artes y Museo de Historia.',
                    'Palacio de la Independencia, con salas de recepción y exposiciones interiores.',
                    'La oficina central de correos y la catedral están en la misma zona central.',
                    'El mercado Ben Thanh es un mercado cubierto, con comida y pequeños artículos.',
                    'Templo del Emperador de Jade: se dejan los zapatos y se viste con recato, como en muchos templos.',
                    'Los títeres de agua se representan en una sala.',
                    'Cafés y tiendas con aire acondicionado sirven cuando empieza un chaparrón.']),
                 S('Cómo ordenar el día', 'Elige un museo o el palacio. Reserva el mercado cubierto o un café para el tramo de lluvia más intensa. La calle peatonal Nguyen Hue puede quedar para el final si la lluvia afloja. La catedral, correos y la calle peatonal están en la misma zona central. Los horarios cambian: confírmalos en el lugar.')]),
            'guide-note-day': page(
                'Saigón en un día por el centro',
                'Un día en Saigón alcanza para el centro: catedral, correos, calle del libro, calle peatonal y el mercado Ben Thanh, más un museo o el palacio.',
                'Saigón en un día',
                'Un día en Ciudad Ho Chi Minh da para el centro. Un día no da para cada museo y cada barrio.',
                [S('Una vuelta por el centro', 'La catedral, la oficina central de correos, la calle de los libros Nguyen Van Binh y la calle peatonal Nguyen Hue están en la misma zona central, así que mucha gente camina de un punto a otro. El mercado Ben Thanh es la parada habitual para comer o mirar los puestos. Añade el palacio o un museo, no todos los demás monumentos en el mismo día.'),
                 S('Moverse entre sitios', ul=[
                    'En el centro, varios de estos puntos están lo bastante cerca para ir a pie.',
                    'Los autobuses urbanos y el metro que sale de la zona de Ben Thanh cubren trayectos más largos.',
                    'Los taxis y los coches pedidos en una aplicación son muy habituales. Pide que enciendan el taxímetro, o confirma el viaje en la aplicación antes de salir.',
                    'Las motos forman parte del tráfico. Cruza al ritmo de los peatones y no te detengas en medio.']),
                 S('Qué dejar para otro día', 'El zoo, un templo, un segundo museo o un lugar fuera de la ciudad, como los túneles de Cu Chi, piden un día propio. En el día de centro bastan una comida de calle y un café. Phở, bánh mì o cơm tấm se encuentran con facilidad. El café con leche condensada y hielo es la versión local más común.')]),
            'guide-note-group': page(
                'Saigón con la familia o en grupo',
                'Saigón con niños o en grupo funciona mejor con un plan al aire libre y otro bajo techo: zoo, títeres de agua, un museo y una comida compartida.',
                'Saigón en familia o en grupo',
                'Ciudad Ho Chi Minh encaja con familias y con grupos si el día se reparte entre un sitio al aire libre y otro bajo techo.',
                [S('Con niños', ul=[
                    'El zoo y jardín botánico de Saigón es un parque antiguo de la ciudad, con caminos a la sombra.',
                    'Los títeres de agua se ven en una sala y se siguen sin mucho diálogo.',
                    'Los mercados cubiertos están llenos. Lleva de la mano a los niños junto a la calle y entre los puestos.',
                    'A mediodía suele hacer calor. La mañana y el final de la tarde sirven para el exterior. El mediodía sirve para un museo, un café o un descanso.',
                    'Bebe agua embotellada o filtrada.',
                    'En templos e iglesias conviene ropa recatada. En los templos se suelen dejar los zapatos.']),
                 S('Con un grupo', 'Un grupo puede pedir varios platos pequeños en un puesto, o unas raciones en un local de phở o cơm tấm. La calle peatonal Nguyen Hue y el espacio delante de la ópera son puntos de encuentro fáciles por la tarde. Elegid un museo o el palacio para seguir juntos, y dejad un rato sin horario en lugar de meter cada monumento en el mismo día.'),
                 S('Notas para todos', ul=[
                    'El tráfico de motos es denso. Cruza con otras personas, a un ritmo constante.',
                    'Los puestos pequeños suelen aceptar efectivo. Algunos también muestran un código QR para una transferencia.',
                    'De mayo a noviembre, ten a mano una lista de sitios bajo techo.'])]),
            'guide-note-food': page(
                'Comida de calle en Saigón',
                'La comida de calle en Saigón va del desayuno a la noche: phở, bánh mì, cơm tấm, bánh xèo y café con leche. Elige un puesto donde cocinen delante de ti.',
                'Comida de calle en Saigón',
                'Cocinar en la acera es una forma normal de comer en Ciudad Ho Chi Minh, del desayuno a bien entrada la noche.',
                [S('Platos que se ven a menudo', ul=[
                    'Phở: sopa de fideos de arroz, a menudo con ternera o pollo.',
                    'Bánh mì: baguette con carne, encurtidos, hierbas y chile.',
                    'Cơm tấm: arroz partido con costilla a la parrilla, huevo y acompañamientos.',
                    'Hủ tiếu y otras sopas de fideos en caldo claro.',
                    'Bánh xèo: crepe salada y crujiente, con hierbas.',
                    'Gỏi cuốn: rollitos frescos con hierbas.',
                    'Chè: postres en forma de sopa dulce.',
                    'El cà phê sữa đá es café helado con leche condensada. El bạc xỉu lleva menos café y más leche.']),
                 S('En el puesto', 'El puesto coloca taburetes bajos en la acera. Un puesto concurrido, con platos que salen rápido, es la elección habitual. Mira cómo cocinan delante de ti. Si quieres menos chile, dilo al pedir. La comida vegetariana suele marcarse con la palabra chay.'),
                 S('Hábitos útiles', ul=[
                    'El desayuno es una hora fuerte de comida de calle, sobre todo de phở y bánh mì. Por la noche hay más parrilla y caracoles.',
                    'El mercado Ben Thanh y muchas calles de barrio tienen puestos para sentarse y comida para llevar.',
                    'Los puestos pequeños suelen preferir efectivo. Algunos muestran un código QR para una transferencia.',
                    'Elige comida cocinada delante de ti y servida caliente. Bebe agua embotellada o filtrada.',
                    'No hace falta perseguir un nombre famoso. Un puesto normal y concurrido es la pauta de la ciudad.'])]),
        },
    )

def fr(DATA, page, S, L):
    g, tg = 'guide de voyage de Saigon', 'guide des adresses pour les hôtes'
    home = """La maison est présentée sur la <a href="{L}">page d'accueil</a>."""
    DATA['fr'] = dict(
        btn='Réservation et contact',
        book='Si vous voulez loger à Hô Chi Minh-Ville, la page de réservation et de contact indique comment réserver la maison.',
        more_h2='D’autres pages sur ce site',
        hub_h2='Quatre sujets pour une journée à Saigon',
        hub_p='Quatre pages sur la pluie, une seule journée dans le centre, une sortie en famille ou en groupe, et la cuisine de rue.',
        cards=[
            ['Saigon sous la pluie', 'guide-note-rain', 'Musées, marché couvert et cafés quand il pleut.'],
            ['Saigon en une journée', 'guide-note-day', 'Un tour du centre, sans vouloir tout voir.'],
            ['Saigon en famille ou en groupe', 'guide-note-group', 'Zoo, marionnettes sur l’eau et repas partagé.'],
            ['Cuisine de rue à Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm et le choix d’un étal.'],
        ],
        links={
            'rain': L('Pour compléter une journée de pluie, ouvrez le ', g, ' et le ', tg, home),
            'day': L('Pour composer la journée plus tranquillement, ouvrez le ', g, ' et le ', tg, home),
            'group': L('En famille ou en groupe, ouvrez le ', g, ' et le ', tg, home),
            'food': L('Pour d’autres adresses où manger et où marcher, ouvrez le ', g, ' et le ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon sous la pluie : à l’abri',
                'À Hô Chi Minh-Ville, les averses sont fréquentes de mai à novembre. Musées, palais, poste, marché couvert et cafés aident à continuer la journée au sec.',
                'Saigon sous la pluie',
                'La pluie n’annule pas forcément une journée à Hô Chi Minh-Ville. Musées, marché couvert et cafés sont le plan habituel à l’abri.',
                [S('Les mois de pluie', 'Hô Chi Minh-Ville a un climat tropical. Les fortes averses sont fréquentes de mai à novembre environ, et le temps plus sec est plus typique de décembre à avril. Après une grosse pluie, les points bas peuvent garder de l’eau un moment, puis elle s’écoule. Pendant les mois humides, une halte à l’abri a sa place dans la journée.'),
                 S('Lieux à l’abri', ul=[
                    'Musée des Vestiges de guerre, musée des Beaux-Arts et musée d’Histoire.',
                    'Palais de l’Indépendance, avec des salles de réception et des expositions intérieures.',
                    'La poste centrale et la cathédrale sont dans le même quartier central.',
                    'Le marché Ben Thanh est un marché couvert, avec de quoi manger et de petits articles.',
                    'Pagode de l’Empereur de jade : on retire ses chaussures et on s’habille simplement, comme dans beaucoup de pagodes.',
                    'Les marionnettes sur l’eau se jouent dans une salle.',
                    'Cafés et boutiques climatisées dépannent quand une averse commence.']),
                 S('Comment ranger la journée', 'Choisissez un musée ou le palais. Gardez le marché couvert ou un café pour le moment le plus mouillé. La rue piétonne Nguyen Hue peut attendre la fin si la pluie se calme. La cathédrale, la poste et la rue piétonne sont dans la même zone centrale. Les horaires changent : vérifiez-les sur place.')]),
            'guide-note-day': page(
                'Saigon en une journée au centre',
                'Une journée à Saigon couvre bien le centre : cathédrale, poste, rue des livres, rue piétonne et marché Ben Thanh, plus un musée ou le palais.',
                'Saigon en une journée',
                'Une journée à Hô Chi Minh-Ville permet de voir le centre. Elle ne permet pas de voir chaque musée et chaque quartier.',
                [S('Une boucle dans le centre', 'La cathédrale, la poste centrale, la rue des livres Nguyen Van Binh et la rue piétonne Nguyen Hue sont dans la même zone centrale : beaucoup de gens marchent de l’une à l’autre. Le marché Ben Thanh est l’arrêt habituel pour manger ou regarder les étals. Ajoutez le palais ou un musée, pas tous les autres monuments le même jour.'),
                 S('Aller d’un lieu à l’autre', ul=[
                    'Dans le centre, plusieurs de ces arrêts sont assez proches pour se faire à pied.',
                    'Les bus urbains et le métro qui part du secteur de Ben Thanh couvrent les trajets plus longs.',
                    'Taxis et voitures commandées dans une application sont très courants. Demandez le compteur, ou confirmez la course dans l’application avant de partir.',
                    'Les motos font partie du trafic. Traversez au rythme des piétons, sans vous arrêter au milieu.']),
                 S('À garder pour un autre jour', 'Le zoo, une pagode, un second musée ou un lieu hors de la ville, comme les tunnels de Cu Chi, demandent une journée à part. Pour la journée dans le centre, un repas de rue et un café suffisent. Phở, bánh mì ou cơm tấm se trouvent facilement. Le café glacé au lait concentré est la version locale la plus courante.')]),
            'guide-note-group': page(
                'Saigon en famille ou en groupe',
                'Saigon en famille ou en groupe se partage entre un arrêt dehors et un arrêt au sec : zoo, marionnettes sur l’eau, un musée et un repas en commun.',
                'Saigon en famille ou avec un groupe',
                'Hô Chi Minh-Ville convient aux familles et aux groupes si la journée mêle un arrêt dehors et un arrêt à l’abri.',
                [S('Avec des enfants', ul=[
                    'Le zoo et le jardin botanique de Saigon forment un parc ancien de la ville, avec des allées ombragées.',
                    'Les marionnettes sur l’eau se voient dans une salle et se suivent sans beaucoup de dialogue.',
                    'Les marchés couverts sont animés. Tenez les enfants par la main près de la rue et entre les étals.',
                    'Le milieu de la journée est souvent chaud. Le matin et la fin d’après-midi conviennent au dehors. Le milieu de journée convient à un musée, un café ou une pause.',
                    'Buvez de l’eau en bouteille ou filtrée.',
                    'Dans les pagodes et les églises, une tenue simple est de mise. On retire en général ses chaussures dans les pagodes.']),
                 S('Avec un groupe', 'Un groupe peut commander plusieurs petits plats à un étal, ou quelques assiettes dans un restaurant de phở ou de cơm tấm. La rue piétonne Nguyen Hue et l’espace devant l’opéra sont des points de rendez-vous simples le soir. Choisissez un musée ou le palais pour rester ensemble, et laissez un moment sans programme au lieu d’empiler chaque monument.'),
                 S('Notes pour tout le monde', ul=[
                    'Le trafic des motos est dense. Traversez avec les autres, d’un pas régulier.',
                    'Les petits étals acceptent en général les espèces. Certains affichent aussi un code QR pour un virement.',
                    'De mai à novembre environ, gardez une liste de lieux à l’abri.'])]),
            'guide-note-food': page(
                'Cuisine de rue à Saigon',
                'La cuisine de rue à Saigon va du petit-déjeuner au soir : phở, bánh mì, cơm tấm, bánh xèo et café au lait. Choisissez un étal où l’on cuisine devant vous.',
                'La cuisine de rue à Saigon',
                'Les cuisines de trottoir sont une façon ordinaire de manger à Hô Chi Minh-Ville, du petit-déjeuner à tard le soir.',
                [S('Plats que l’on croise souvent', ul=[
                    'Phở : soupe de nouilles de riz, souvent au bœuf ou au poulet.',
                    'Bánh mì : baguette avec viande, pickles, herbes et piment.',
                    'Cơm tấm : riz brisé avec travers grillé, œuf et accompagnements.',
                    'Hủ tiếu et d’autres soupes de nouilles au bouillon clair.',
                    'Bánh xèo : crêpe salée et croustillante, avec des herbes.',
                    'Gỏi cuốn : rouleaux frais aux herbes.',
                    'Chè : desserts en soupe sucrée.',
                    'Le cà phê sữa đá est un café glacé au lait concentré. Le bạc xỉu est plus laitier.']),
                 S('À l’étal', 'L’étal pose des tabourets bas sur le trottoir. Un étal fréquenté, où les plats sortent vite, est le choix habituel. Regardez la cuisine se faire devant vous. Si vous voulez moins de piment, dites-le en commandant. Le végétarien est souvent indiqué par le mot chay.'),
                 S('Habitudes utiles', ul=[
                    'Le petit-déjeuner est un grand moment de cuisine de rue, surtout pour le phở et le bánh mì. Le soir amène plus de grillades et d’escargots.',
                    'Le marché Ben Thanh et beaucoup de rues de quartier ont des places assises et de la vente à emporter.',
                    'Les petits étals préfèrent souvent les espèces. Certains montrent un code QR pour un virement.',
                    'Choisissez un plat cuisiné devant vous et servi chaud. Buvez de l’eau en bouteille ou filtrée.',
                    'Inutile de courir après un nom célèbre. Un étal ordinaire et fréquenté est la pratique de la ville.'])]),
        },
    )

def pt(DATA, page, S, L):
    g, tg = 'guia de viagem de Saigon', 'guia de lugares para quem se hospeda'
    home = 'A casa é apresentada na <a href="{L}">página inicial</a>.'
    DATA['pt'] = dict(
        btn='Reserva e contato',
        book='Se você quiser se hospedar em Ho Chi Minh, a página de reserva e contato mostra como reservar a casa.',
        more_h2='Mais páginas neste site',
        hub_h2='Quatro temas para um dia em Saigon',
        hub_p='Quatro páginas sobre a chuva, um único dia no centro, uma saída em família ou em grupo, e a comida de rua.',
        cards=[
            ['Saigon em dia de chuva', 'guide-note-rain', 'Museus, mercado coberto e cafés quando chove.'],
            ['Saigon em um dia', 'guide-note-day', 'Uma volta pelo centro, sem tentar ver tudo.'],
            ['Saigon em família ou em grupo', 'guide-note-group', 'Zoológico, marionetes de água e uma refeição compartilhada.'],
            ['Comida de rua em Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm e como escolher uma banca.'],
        ],
        links={
            'rain': L('Para completar um dia de chuva, abra o ', g, ' e o ', tg, home),
            'day': L('Para montar o dia com mais calma, abra o ', g, ' e o ', tg, home),
            'group': L('Em família ou em grupo, abra o ', g, ' e o ', tg, home),
            'food': L('Para mais lugares onde comer e caminhar, abra o ', g, ' e o ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon na chuva: planos cobertos',
                'Em Ho Chi Minh, os aguaceiros são comuns de maio a novembro. Museus, palácio, correios, mercado coberto e cafés permitem seguir o dia em local coberto.',
                'Saigon em um dia de chuva',
                'A chuva não precisa cancelar um dia em Ho Chi Minh. Museus, um mercado coberto e cafés são o plano habitual em local abrigado.',
                [S('Os meses de chuva', 'Ho Chi Minh tem clima tropical. Aguaceiros fortes são comuns de maio a novembro, e o tempo mais seco é mais típico de dezembro a abril. Depois de uma chuva forte, pontos baixos podem reter água por um momento e depois escoar. Nos meses úmidos, vale ter uma parada coberta no dia.'),
                 S('Lugares cobertos', ul=[
                    'Museu dos Vestígios de Guerra, Museu de Belas Artes e Museu de História.',
                    'Palácio da Independência, com salas de recepção e exposições internas.',
                    'Os correios centrais e a catedral ficam na mesma área central.',
                    'O mercado Ben Thanh é um mercado coberto, com comida e pequenos artigos.',
                    'Pagode do Imperador de Jade: tira-se o calçado e veste-se com discrição, como em muitos pagodes.',
                    'Os espetáculos de marionetes de água acontecem em uma sala.',
                    'Cafés e lojas com ar-condicionado servem quando um aguaceiro começa.']),
                 S('Como organizar o dia', 'Escolha um museu ou o palácio. Deixe o mercado coberto ou um café para a hora de chuva mais intensa. A rua de pedestres Nguyen Hue pode ficar para o fim se a chuva diminuir. A catedral, os correios e a rua de pedestres ficam na mesma área central. Os horários mudam: confirme no local.')]),
            'guide-note-day': page(
                'Saigon em um dia no centro',
                'Um dia em Saigon cobre bem o centro: catedral, correios, rua dos livros, rua de pedestres e o mercado Ben Thanh, mais um museu ou o palácio.',
                'Saigon em um dia',
                'Um dia em Ho Chi Minh dá para o centro. Um dia não dá para cada museu e cada bairro.',
                [S('Uma volta pelo centro', 'A catedral, os correios centrais, a rua dos livros Nguyen Van Binh e a rua de pedestres Nguyen Hue ficam na mesma área central, e muita gente caminha de um ponto a outro. O mercado Ben Thanh é a parada habitual para comer ou ver as bancas. Acrescente o palácio ou um museu, não todos os outros pontos no mesmo dia.'),
                 S('Ir de um lugar a outro', ul=[
                    'No centro, vários desses pontos ficam perto o bastante para ir a pé.',
                    'Ônibus urbanos e o metrô que sai da área de Ben Thanh cobrem trechos mais longos.',
                    'Táxis e carros pedidos em um aplicativo são muito usados. Peça o taxímetro, ou confirme a corrida no aplicativo antes de sair.',
                    'As motos fazem parte do trânsito. Atravesse no ritmo dos pedestres e não pare no meio.']),
                 S('O que deixar para outro dia', 'O zoológico, um pagode, um segundo museu ou um lugar fora da cidade, como os túneis de Cu Chi, pedem um dia próprio. No dia de centro, bastam uma refeição de rua e um café. Phở, bánh mì ou cơm tấm aparecem com facilidade. O café gelado com leite condensado é a versão local mais comum.')]),
            'guide-note-group': page(
                'Saigon com a família ou em grupo',
                'Saigon com crianças ou em grupo funciona melhor com um passeio ao ar livre e outro coberto: zoológico, marionetes, um museu e uma refeição compartilhada.',
                'Saigon em família ou em grupo',
                'Ho Chi Minh combina com famílias e com grupos quando o dia mistura um ponto ao ar livre e outro coberto.',
                [S('Com crianças', ul=[
                    'O zoológico e jardim botânico de Saigon é um parque antigo da cidade, com caminhos à sombra.',
                    'As marionetes de água são vistas em uma sala e acompanhadas sem muito diálogo.',
                    'Mercados cobertos são movimentados. Segure a mão das crianças perto da rua e entre as bancas.',
                    'O meio do dia costuma ser quente. Manhã e fim de tarde servem para o ar livre. O meio do dia serve para um museu, um café ou um descanso.',
                    'Beba água engarrafada ou filtrada.',
                    'Em pagodes e igrejas, roupa discreta é o esperado. Nos pagodes, em geral se tira o calçado.']),
                 S('Com um grupo', 'Um grupo pode pedir vários pratos pequenos em uma banca, ou algumas porções em uma casa de phở ou cơm tấm. A rua de pedestres Nguyen Hue e o espaço em frente à ópera são pontos de encontro fáceis à noite. Escolham um museu ou o palácio para permanecer juntos, e deixem um tempo sem roteiro em vez de encaixar cada monumento.'),
                 S('Notas para todos', ul=[
                    'O trânsito de motos é denso. Atravesse com outras pessoas, em ritmo constante.',
                    'Bancas pequenas em geral aceitam dinheiro. Algumas também mostram um código QR para uma transferência.',
                    'De maio a novembro, tenha à mão uma lista de lugares cobertos.'])]),
            'guide-note-food': page(
                'Comida de rua em Saigon',
                'A comida de rua em Saigon vai do café da manhã à noite: phở, bánh mì, cơm tấm, bánh xèo e café com leite. Escolha uma banca onde cozinhem na sua frente.',
                'Comida de rua em Saigon',
                'Cozinhar na calçada é um jeito comum de comer em Ho Chi Minh, do café da manhã até tarde da noite.',
                [S('Pratos que aparecem com frequência', ul=[
                    'Phở: sopa de macarrão de arroz, em geral com carne bovina ou frango.',
                    'Bánh mì: baguete com carne, picles, ervas e pimenta.',
                    'Cơm tấm: arroz quebrado com costela grelhada, ovo e acompanhamentos.',
                    'Hủ tiếu e outras sopas de macarrão em caldo claro.',
                    'Bánh xèo: panqueca salgada e crocante, com ervas.',
                    'Gỏi cuốn: rolinhos frescos com ervas.',
                    'Chè: sobremesas em forma de caldo doce.',
                    'O cà phê sữa đá é café gelado com leite condensado. O bạc xỉu leva menos café e mais leite.']),
                 S('Na banca', 'A banca põe bancos baixos na calçada. Uma banca movimentada, com pratos que saem rápido, é a escolha habitual. Veja a comida ser feita na sua frente. Se quiser menos pimenta, diga ao pedir. Comida vegetariana costuma ser marcada com a palavra chay.'),
                 S('Hábitos úteis', ul=[
                    'O café da manhã é um horário forte de comida de rua, sobretudo phở e bánh mì. À noite há mais grelhados e caracóis.',
                    'O mercado Ben Thanh e muitas ruas de bairro têm lugares para sentar e comida para levar.',
                    'Bancas pequenas em geral preferem dinheiro. Algumas mostram um código QR para uma transferência.',
                    'Escolha comida feita na sua frente e servida quente. Beba água engarrafada ou filtrada.',
                    'Não é preciso correr atrás de um nome famoso. Uma banca comum e cheia é o padrão da cidade.'])]),
        },
    )

def it(DATA, page, S, L):
    g, tg = 'guida di viaggio di Saigon', 'guida dei posti per chi alloggia'
    home = 'La casa è presentata nella <a href="{L}">pagina iniziale</a>.'
    DATA['it'] = dict(
        btn='Prenota e contatti',
        book='Se volete alloggiare a Ho Chi Minh, la pagina di prenotazione e contatti indica come riservare la casa.',
        more_h2='Altre pagine su questo sito',
        hub_h2='Quattro temi per una giornata a Saigon',
        hub_p='Quattro pagine sulla pioggia, una sola giornata in centro, un’uscita in famiglia o in gruppo, e il cibo di strada.',
        cards=[
            ['Saigon con la pioggia', 'guide-note-rain', 'Musei, mercato coperto e caffè quando piove.'],
            ['Saigon in un giorno', 'guide-note-day', 'Un giro in centro, senza voler vedere tutto.'],
            ['Saigon in famiglia o in gruppo', 'guide-note-group', 'Zoo, marionette sull’acqua e un pasto condiviso.'],
            ['Cibo di strada a Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm e come scegliere un banco.'],
        ],
        links={
            'rain': L('Per completare una giornata di pioggia, aprite la ', g, ' e la ', tg, home),
            'day': L('Per comporre la giornata con più calma, aprite la ', g, ' e la ', tg, home),
            'group': L('In famiglia o in gruppo, aprite la ', g, ' e la ', tg, home),
            'food': L('Per altri posti dove mangiare e camminare, aprite la ', g, ' e la ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon con la pioggia: al coperto',
                'A Ho Chi Minh i rovesci sono frequenti da maggio a novembre. Musei, palazzo, posta, mercato coperto e caffè fanno continuare la giornata all’asciutto.',
                'Saigon in un giorno di pioggia',
                'La pioggia non deve cancellare una giornata a Ho Chi Minh. Musei, un mercato coperto e caffè sono il piano abituale al coperto.',
                [S('I mesi di pioggia', 'Ho Chi Minh ha un clima tropicale. I rovesci forti sono frequenti da maggio a novembre circa, e il tempo più secco è più tipico da dicembre ad aprile. Dopo una pioggia intensa, i punti bassi possono trattenere acqua per un momento e poi drenare. Nei mesi umidi conviene avere una tappa al coperto.'),
                 S('Luoghi al coperto', ul=[
                    'Museo delle Vestigia di guerra, Museo delle Belle Arti e Museo di Storia.',
                    'Palazzo dell’Indipendenza, con sale di ricevimento e mostre interne.',
                    'L’ufficio postale centrale e la cattedrale stanno nella stessa zona centrale.',
                    'Il mercato Ben Thanh è un mercato coperto, con cibo e piccoli articoli.',
                    'Tempio dell’Imperatore di Giada: si tolgono le scarpe e ci si veste con modestia, come in molti templi.',
                    'Le marionette sull’acqua si vedono in una sala.',
                    'Caffè e negozi con aria condizionata servono quando inizia un rovescio.']),
                 S('Come ordinare la giornata', 'Scegliete un museo o il palazzo. Tenete il mercato coperto o un caffè per il momento di pioggia più intensa. La via pedonale Nguyen Hue può restare per la fine se la pioggia si calma. Cattedrale, posta e via pedonale stanno nella stessa zona centrale. Gli orari cambiano: verificateli sul posto.')]),
            'guide-note-day': page(
                'Saigon in un giorno in centro',
                'Un giorno a Saigon copre bene il centro storico: cattedrale, posta, via dei libri, via pedonale e mercato Ben Thanh, più un museo o il palazzo.',
                'Saigon in un giorno',
                'Un giorno a Ho Chi Minh basta per il centro. Un giorno non basta per ogni museo e ogni quartiere.',
                [S('Un giro in centro', 'La cattedrale, l’ufficio postale centrale, la via dei libri Nguyen Van Binh e la via pedonale Nguyen Hue stanno nella stessa zona centrale, e molte persone camminano da un punto all’altro. Il mercato Ben Thanh è la tappa abituale per mangiare o guardare i banchi. Aggiungete il palazzo o un museo, non tutti gli altri monumenti nello stesso giorno.'),
                 S('Spostarsi tra i luoghi', ul=[
                    'In centro, diversi di questi punti sono abbastanza vicini da raggiungerli a piedi.',
                    'Gli autobus urbani e la metro che parte dalla zona di Ben Thanh coprono i tratti più lunghi.',
                    'Taxi e auto prenotate in un’applicazione sono molto usati. Chiedete il tassametro, oppure confermate la corsa nell’applicazione prima di partire.',
                    'Le moto fanno parte del traffico. Attraversate al ritmo dei pedoni e non fermatevi in mezzo.']),
                 S('Cosa lasciare a un altro giorno', 'Lo zoo, un tempio, un secondo museo o un luogo fuori città, come i tunnel di Cu Chi, chiedono un giorno a parte. Nella giornata in centro bastano un pasto di strada e un caffè. Phở, bánh mì o cơm tấm si trovano facilmente. Il caffè ghiacciato con latte condensato è la versione locale più comune.')]),
            'guide-note-group': page(
                'Saigon in famiglia o in gruppo',
                'Saigon in famiglia o in gruppo si divide tra una tappa all’aperto e una al coperto: zoo, marionette sull’acqua, un museo e un pasto condiviso.',
                'Saigon in famiglia o con un gruppo',
                'Ho Chi Minh va bene per famiglie e gruppi se la giornata unisce una tappa all’aperto e una al coperto.',
                [S('Con i bambini', ul=[
                    'Lo zoo e il giardino botanico di Saigon sono un parco antico della città, con viali in ombra.',
                    'Le marionette sull’acqua si vedono in una sala e si seguono senza molto dialogo.',
                    'I mercati coperti sono animati. Tenete i bambini per mano vicino alla strada e tra i banchi.',
                    'A metà giornata fa spesso caldo. Mattina e tardo pomeriggio vanno bene all’aperto. Il mezzogiorno va bene per un museo, un caffè o una pausa.',
                    'Bevete acqua in bottiglia o filtrata.',
                    'In pagode e chiese si sta con un abbigliamento sobrio. Nelle pagode in genere si tolgono le scarpe.']),
                 S('Con un gruppo', 'Un gruppo può ordinare diversi piatti piccoli a un banco, o qualche porzione in un locale di phở o cơm tấm. La via pedonale Nguyen Hue e lo spazio davanti all’opera sono punti d’incontro semplici la sera. Scegliete un museo o il palazzo per restare insieme, e lasciate un momento senza programma invece di infilare ogni monumento.'),
                 S('Note per tutti', ul=[
                    'Il traffico delle moto è fitto. Attraversate con le altre persone, a passo costante.',
                    'I banchi piccoli di solito accettano contanti. Alcuni mostrano anche un codice QR per un bonifico.',
                    'Da maggio a novembre circa, tenete a portata una lista di luoghi al coperto.'])]),
            'guide-note-food': page(
                'Cibo di strada a Saigon',
                'Il cibo di strada a Saigon va dalla colazione alla sera: phở, bánh mì, cơm tấm, bánh xèo e caffè latte. Scegliete un banco dove cucinano davanti a voi.',
                'Il cibo di strada a Saigon',
                'Le cucine sul marciapiede sono un modo ordinario di mangiare a Ho Chi Minh, dalla colazione a tarda sera.',
                [S('Piatti che si incontrano spesso', ul=[
                    'Phở: zuppa di noodles di riso, spesso con manzo o pollo.',
                    'Bánh mì: baguette con carne, sottaceti, erbe e peperoncino.',
                    'Cơm tấm: riso spezzato con costine alla griglia, uovo e contorni.',
                    'Hủ tiếu e altre zuppe di noodles in brodo chiaro.',
                    'Bánh xèo: crêpe salata e croccante, con erbe.',
                    'Gỏi cuốn: involtini freschi con erbe.',
                    'Chè: dolci in forma di zuppa.',
                    'Il cà phê sữa đá è caffè ghiacciato con latte condensato. Il bạc xỉu è più latte e meno caffè.']),
                 S('Al banco', 'Il banco mette sgabelli bassi sul marciapiede. Un banco affollato, con piatti che escono in fretta, è la scelta abituale. Guardate il cibo cucinato davanti a voi. Se volete meno peperoncino, ditelo ordinando. Il vegetariano è spesso segnato con la parola chay.'),
                 S('Abitudini utili', ul=[
                    'La colazione è un orario forte del cibo di strada, soprattutto phở e bánh mì. La sera arrivano più grigliate e lumache.',
                    'Il mercato Ben Thanh e molte strade di quartiere hanno posti a sedere e cibo da asporto.',
                    'I banchi piccoli preferiscono spesso i contanti. Alcuni mostrano un codice QR per un bonifico.',
                    'Scegliete cibo cucinato davanti a voi e servito caldo. Bevete acqua in bottiglia o filtrata.',
                    'Non serve inseguire un nome famoso. Un banco ordinario e pieno è l’abitudine della città.'])]),
        },
    )

def nl(DATA, page, S, L):
    g, tg = 'reisgids voor Saigon', 'gids met plekken voor wie er verblijft'
    home = 'Het huis staat op de <a href="{L}">startpagina</a>.'
    DATA['nl'] = dict(
        btn='Boeken en contact',
        book='Als je in Ho Chi Minh wilt overnachten, legt de pagina voor boeken en contact uit hoe je het huis reserveert.',
        more_h2='Meer pagina’s op deze site',
        hub_h2='Vier onderwerpen voor een dag in Saigon',
        hub_p='Vier pagina’s over regen, één dag in het centrum, een uitstap met gezin of groep, en streetfood.',
        cards=[
            ['Saigon op een regendag', 'guide-note-rain', 'Musea, een overdekte markt en cafés als het regent.'],
            ['Saigon op één dag', 'guide-note-day', 'Een ronde door het centrum, zonder alles te willen zien.'],
            ['Saigon met gezin of groep', 'guide-note-group', 'Dierentuin, waterpoppen en een gedeelde maaltijd.'],
            ['Streetfood in Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm en hoe je een kraam kiest.'],
        ],
        links={
            'rain': L('Om een regendag af te maken, open je de ', g, ' en de ', tg, home),
            'day': L('Om de dag rustiger in te delen, open je de ', g, ' en de ', tg, home),
            'group': L('Met gezin of groep open je de ', g, ' en de ', tg, home),
            'food': L('Voor meer plekken om te eten en te lopen, open je de ', g, ' en de ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon in de regen: binnen blijven',
                'In het tropische Ho Chi Minh zijn buien gewoon van mei tot november. Musea, paleis, postkantoor, overdekte markt en cafés laten de dag droog verdergaan.',
                'Saigon op een regenachtige dag',
                'Regen hoeft een dag in Ho Chi Minh niet te schrappen. Musea, een overdekte markt en cafés zijn het gebruikelijke plan binnen.',
                [S('De regenmaanden', 'Ho Chi Minh heeft een tropisch klimaat. Zware buien zijn gebruikelijk van ongeveer mei tot november, en droger weer is typischer van december tot april. Na een harde bui kan water op lage plekken even blijven staan en daarna weglopen. In de nattere maanden hoort een stop onder dak in de dag.'),
                 S('Plekken onder dak', ul=[
                    'Oorlogsmuseum, museum voor schone kunsten en geschiedenismuseum.',
                    'Onafhankelijkheidspaleis, met ontvangstzalen en tentoonstellingen binnen.',
                    'Het centrale postkantoor en de kathedraal liggen in hetzelfde centrale gebied.',
                    'Ben Thanh-markt is een overdekte markt, met eten en kleine spullen.',
                    'Jade Emperor-pagode: schoenen uit en bedekt gekleed, zoals in veel pagodes.',
                    'Waterpoppen worden in een zaal opgevoerd.',
                    'Cafés en winkels met airco zijn handig als een bui begint.']),
                 S('De dag indelen', 'Kies één museum of het paleis. Bewaar de overdekte markt of een café voor het natste deel. De wandelstraat Nguyen Hue kan aan het eind als de regen afneemt. Kathedraal, postkantoor en wandelstraat liggen in hetzelfde centrale gebied. Openingstijden veranderen: controleer ze ter plaatse.')]),
            'guide-note-day': page(
                'Saigon op één dag in het centrum',
                'Eén dag in Saigon dekt het centrum: kathedraal, postkantoor, boekenstraat, wandelstraat en de Ben Thanh-markt, plus één museum of het paleis.',
                'Saigon op één dag',
                'Eén dag in Ho Chi Minh is genoeg voor het centrum. Eén dag is niet genoeg voor elk museum en elke buurt.',
                [S('Een ronde door het centrum', 'De kathedraal, het centrale postkantoor, boekenstraat Nguyen Van Binh en wandelstraat Nguyen Hue liggen in hetzelfde centrale gebied, en veel mensen lopen van de ene plek naar de andere. Ben Thanh-markt is de gebruikelijke stop om te eten of kramen te bekijken. Voeg het paleis of één museum toe, niet ook nog elk ander monument.'),
                 S('Van plek naar plek', ul=[
                    'In het centrum liggen verschillende van deze punten dicht genoeg bij elkaar om te lopen.',
                    'Stadsbussen en de metro vanuit het gebied van Ben Thanh dekken langere stukken.',
                    'Taxi’s en auto’s die je in een app bestelt zijn heel gebruikelijk. Vraag om de meter, of bevestig de rit in de app voordat je vertrekt.',
                    'Motoren horen bij het verkeer. Steek over in het tempo van de voetgangers en blijf niet midden op de weg stilstaan.']),
                 S('Bewaren voor een andere dag', 'De dierentuin, een pagode, een tweede museum of een plek buiten de stad, zoals de tunnels van Cu Chi, vragen een eigen dag. Op de centrumdag volstaan een maaltijd op straat en een koffie. Phở, bánh mì of cơm tấm zijn makkelijk te vinden. IJskoffie met gecondenseerde melk is de meest gewone lokale versie.')]),
            'guide-note-group': page(
                'Saigon met gezin of een groep',
                'Saigon met kinderen of een groep werkt beter met één stop buiten en één binnen: dierentuin, waterpoppen, een museum en een gedeelde maaltijd.',
                'Saigon met gezin of groep',
                'Ho Chi Minh past bij gezinnen en groepen als de dag één buitenstop en één binnenstop heeft.',
                [S('Met kinderen', ul=[
                    'De dierentuin en botanische tuin van Saigon is een oud stadspark, met schaduwrijke paden.',
                    'Waterpoppen zie je in een zaal, ook zonder veel gesproken tekst.',
                    'Overdekte markten zijn druk. Houd kinderen bij de hand bij de weg en tussen de kramen.',
                    'Midden op de dag is het vaak heet. Ochtend en late middag passen bij buiten. Het middaguur past bij een museum, een café of rust.',
                    'Drink water uit een fles of gefilterd water.',
                    'Bij pagodes en kerken past bedekte kleding. In pagodes doe je meestal je schoenen uit.']),
                 S('Met een groep', 'Een groep kan een paar kleine gerechten aan een kraam bestellen, of een paar borden in een zaak voor phở of cơm tấm. Wandelstraat Nguyen Hue en de ruimte voor de opera zijn eenvoudige ontmoetingspunten in de avond. Kies één museum of het paleis zodat de groep bij elkaar blijft, en laat tijd zonder programma in plaats van elk monument in dezelfde dag te proppen.'),
                 S('Voor iedereen', ul=[
                    'Het motorverkeer is dicht. Steek met anderen over, in een gelijkmatig tempo.',
                    'Kleine kramen nemen meestal contant geld aan. Sommige tonen ook een QR-code voor een overschrijving.',
                    'Van mei tot november is een lijst met plekken onder dak handig.'])]),
            'guide-note-food': page(
                'Streetfood in Saigon',
                'Streetfood in Saigon loopt van ontbijt tot avond: phở, bánh mì, cơm tấm, bánh xèo en koffie met melk. Kies een kraam waar ze voor je ogen koken.',
                'Eten op straat in Saigon',
                'Koken op de stoep is een gewone manier van eten in Ho Chi Minh, van het ontbijt tot laat in de avond.',
                [S('Gerechten die je vaak ziet', ul=[
                    'Phở: soep met rijstnoedels, vaak met rund of kip.',
                    'Bánh mì: stokbrood met vlees, pickles, kruiden en chili.',
                    'Cơm tấm: gebroken rijst met gegrilde rib, ei en bijgerechten.',
                    'Hủ tiếu en andere noedelsoepen op een heldere bouillon.',
                    'Bánh xèo: knapperige hartige pannenkoek, met kruiden.',
                    'Gỏi cuốn: verse rolletjes met kruiden.',
                    'Chè: zoete soepdesserts.',
                    'Cà phê sữa đá is ijskoffie met gecondenseerde melk. Bạc xỉu is melkiger.']),
                 S('Aan de kraam', 'De kraam zet lage krukjes op de stoep. Een drukke kraam, waar gerechten snel komen, is de gewone keuze. Kijk of er voor je ogen wordt gekookt. Wil je minder chili, zeg dat bij het bestellen. Vegetarisch eten staat vaak aangegeven met het woord chay.'),
                 S('Handige gewoonten', ul=[
                    'Het ontbijt is een belangrijk uur voor streetfood, vooral phở en bánh mì. ’s Avonds komen er meer grillgerechten en slakken.',
                    'Ben Thanh-markt en veel buurtstraten hebben zitplaatsen en eten om mee te nemen.',
                    'Kleine kramen willen vaak contant geld. Sommige tonen een QR-code voor een overschrijving.',
                    'Kies eten dat voor je ogen wordt gekookt en warm wordt geserveerd. Drink water uit een fles of gefilterd water.',
                    'Je hoeft geen beroemde naam achterna. Een gewone, drukke kraam is het patroon van de stad.'])]),
        },
    )

def pl(DATA, page, S, L):
    g, tg = 'przewodnik po Sajgonie', 'przewodnik po miejscach dla gości'
    home = 'Dom jest opisany na <a href="{L}">stronie głównej</a>.'
    DATA['pl'] = dict(
        btn='Rezerwacja i kontakt',
        book='Jeśli chcecie zostać w Ho Chi Minh, strona rezerwacji i kontaktu wyjaśnia, jak zarezerwować dom.',
        more_h2='Więcej stron w tym serwisie',
        hub_h2='Cztery tematy na dzień w Sajgonie',
        hub_p='Cztery strony o deszczu, jednym dniu w centrum, wyjściu z rodziną lub grupą oraz jedzeniu ulicznym.',
        cards=[
            ['Sajgon w deszczu', 'guide-note-rain', 'Muzea, zadaszony targ i kawiarnie, gdy pada.'],
            ['Sajgon w jeden dzień', 'guide-note-day', 'Pętla po centrum, bez próby zobaczenia wszystkiego.'],
            ['Sajgon z rodziną lub grupą', 'guide-note-group', 'Zoo, lalki wodne i wspólny posiłek.'],
            ['Jedzenie uliczne w Sajgonie', 'guide-note-food', 'Phở, bánh mì, cơm tấm i wybór stoiska.'],
        ],
        links={
            'rain': L('Aby dopełnić deszczowy dzień, otwórzcie ', g, ' i ', tg, home),
            'day': L('Aby ułożyć dzień spokojniej, otwórzcie ', g, ' i ', tg, home),
            'group': L('Z rodziną lub grupą otwórzcie ', g, ' i ', tg, home),
            'food': L('Po więcej miejsc do jedzenia i spaceru otwórzcie ', g, ' i ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Sajgon w deszczu: pod dachem',
                'W Ho Chi Minh ulewy są częste od maja do listopada. Muzea, pałac, poczta, zadaszony targ i kawiarnie pozwalają dokończyć dzień w suchym miejscu.',
                'Sajgon w deszczowy dzień',
                'Deszcz nie musi skreślać dnia w Ho Chi Minh. Muzea, zadaszony targ i kawiarnie to zwykły plan pod dachem.',
                [S('Miesiące deszczu', 'Ho Chi Minh ma klimat tropikalny. Silne ulewy są częste mniej więcej od maja do listopada, a suchsza pogoda jest typowsza od grudnia do kwietnia. Po dużym deszczu niższe miejsca mogą chwilę trzymać wodę, potem ona odpływa. W wilgotniejszych miesiącach w planie dnia powinien być przystanek pod dachem.'),
                 S('Miejsca pod dachem', ul=[
                    'Muzeum Śladów Wojny, Muzeum Sztuk Pięknych i Muzeum Historii.',
                    'Pałac Niepodległości, z salami przyjęć i wystawami w środku.',
                    'Poczta główna i katedra leżą w tej samej części centrum.',
                    'Targ Ben Thanh jest zadaszony: jest tam jedzenie i drobne towary.',
                    'Świątynia Nefrytowego Cesarza: zdejmuje się buty i ubiera spokojnie, jak w wielu świątyniach.',
                    'Teatr lalek wodnych gra w sali.',
                    'Kawiarnie i sklepy z klimatyzacją przydają się, gdy zaczyna się ulewa.']),
                 S('Jak ułożyć dzień', 'Wybierzcie jedno muzeum albo pałac. Zadaszony targ lub kawiarnię zostawcie na najmocniejszy deszcz. Deptak Nguyen Hue może być na koniec, jeśli deszcz słabnie. Katedra, poczta i deptak są w tej samej części centrum. Godziny otwarcia się zmieniają: sprawdźcie je na miejscu.')]),
            'guide-note-day': page(
                'Sajgon w jeden dzień w centrum',
                'Jeden dzień w Sajgonie wystarcza na centrum: katedra, poczta, ulica książek, deptak i targ Ben Thanh, plus jedno muzeum albo pałac. Sprawdźcie godziny.',
                'Sajgon w jeden dzień',
                'Jeden dzień w Ho Chi Minh wystarcza na centrum. Jeden dzień nie wystarcza na każde muzeum i każdą dzielnicę.',
                [S('Pętla po centrum', 'Katedra, poczta główna, ulica książek Nguyen Van Binh i deptak Nguyen Hue leżą w tej samej części centrum, więc wiele osób chodzi między nimi pieszo. Targ Ben Thanh to zwykły przystanek na posiłek albo obejrzenie stoisk. Dołóżcie pałac albo jedno muzeum, nie wszystkie pozostałe punkty tego samego dnia.'),
                 S('Między miejscami', ul=[
                    'W centrum kilka z tych punktów leży na tyle blisko, że da się iść pieszo.',
                    'Autobusy miejskie i metro z okolicy Ben Thanh obejmują dłuższe odcinki.',
                    'Taksówki i auta zamawiane w aplikacji są bardzo częste. Poproście o taksometr albo potwierdźcie kurs w aplikacji przed wyjazdem.',
                    'Motocykle są częścią ruchu. Przechodźcie w tempie pieszych i nie zatrzymujcie się w środku jezdni.']),
                 S('Na inny dzień', 'Zoo, świątynia, drugie muzeum albo miejsce poza miastem, takie jak tunele Cu Chi, potrzebują osobnego dnia. W dniu po centrum wystarczą jeden posiłek uliczny i kawa. Phở, bánh mì albo cơm tấm łatwo znaleźć. Mrożona kawa z mlekiem skondensowanym to najczęstsza lokalna wersja.')]),
            'guide-note-group': page(
                'Sajgon z rodziną albo grupą',
                'Sajgon z dziećmi albo grupą układa się lepiej, gdy dzień ma jeden punkt na zewnątrz i jeden pod dachem: zoo, lalki wodne, muzeum i wspólny posiłek.',
                'Sajgon z rodziną lub grupą',
                'Ho Chi Minh pasuje rodzinom i grupom, jeśli dzień łączy jeden punkt na zewnątrz i jeden pod dachem.',
                [S('Z dziećmi', ul=[
                    'Zoo i ogród botaniczny w Sajgonie to dawny park miejski, z cienistymi alejkami.',
                    'Lalki wodne ogląda się w sali, bez dużej ilości dialogu.',
                    'Zadaszone targi są pełne ludzi. Trzymajcie dzieci za rękę przy ulicy i między stoiskami.',
                    'W środku dnia bywa gorąco. Ranek i późne popołudnie pasują na zewnątrz. Południe pasuje na muzeum, kawiarnię albo odpoczynek.',
                    'Pijcie wodę butelkowaną albo filtrowaną.',
                    'W świątyniach i kościołach oczekuje się spokojnego stroju. W świątyniach zwykle zdejmuje się buty.']),
                 S('Z grupą', 'Grupa może zamówić kilka małych dań na stoisku albo kilka talerzy w lokalu z phở lub cơm tấm. Deptak Nguyen Hue i plac przed operą to proste wieczorne punkty zbiórki. Wybierzcie jedno muzeum albo pałac, żeby zostać razem, i zostawcie czas bez planu zamiast upychać każdy punkt w jeden dzień.'),
                 S('Dla wszystkich', ul=[
                    'Ruch motocykli jest gęsty. Przechodźcie razem z innymi, równym tempem.',
                    'Małe stoiska zwykle biorą gotówkę. Niektóre pokazują też kod QR do przelewu.',
                    'Od maja do listopada miejcie pod ręką listę miejsc pod dachem.'])]),
            'guide-note-food': page(
                'Jedzenie uliczne w Sajgonie',
                'Jedzenie uliczne w Sajgonie trwa od śniadania do wieczora: phở, bánh mì, cơm tấm, bánh xèo i kawa z mlekiem. Wybierzcie stoisko, gdzie gotują na oczach.',
                'Jedzenie uliczne w Sajgonie',
                'Kuchnia na chodniku to zwykły sposób jedzenia w Ho Chi Minh, od śniadania do późnego wieczora.',
                [S('Dania, które widać często', ul=[
                    'Phở: zupa z makaronem ryżowym, często z wołowiną albo kurczakiem.',
                    'Bánh mì: bagietka z mięsem, piklami, ziołami i chili.',
                    'Cơm tấm: kruszony ryż z grillowanym żeberkiem, jajkiem i dodatkami.',
                    'Hủ tiếu i inne zupy z makaronem na klarownym rosole.',
                    'Bánh xèo: chrupiący słony naleśnik, z ziołami.',
                    'Gỏi cuốn: świeże rolki z ziołami.',
                    'Chè: słodkie zupy deserowe.',
                    'Cà phê sữa đá to mrożona kawa z mlekiem skondensowanym. Bạc xỉu ma więcej mleka.']),
                 S('Przy stoisku', 'Stoisko stawia niskie stołki na chodniku. Zajęte stoisko, z którego dania wychodzą szybko, to zwykły wybór. Patrzcie, czy gotują na waszych oczach. Jeśli chcecie mniej chili, powiedzcie przy zamówieniu. Jedzenie wegetariańskie często oznaczają słowem chay.'),
                 S('Przydatne nawyki', ul=[
                    'Śniadanie to ważna pora jedzenia ulicznego, zwłaszcza phở i bánh mì. Wieczorem dochodzą grille i ślimaki.',
                    'Targ Ben Thanh i wiele ulic osiedlowych ma miejsca siedzące i jedzenie na wynos.',
                    'Małe stoiska często wolą gotówkę. Niektóre pokazują kod QR do przelewu.',
                    'Wybierajcie jedzenie gotowane na waszych oczach i podawane gorące. Pijcie wodę butelkowaną albo filtrowaną.',
                    'Nie trzeba gonić słynnej nazwy. Zwykłe, pełne stoisko to miejski zwyczaj.'])]),
        },
    )

def ru(DATA, page, S, L):
    g, tg = 'путеводитель по Сайгону', 'гид по местам для живущих в городе гостей'
    home = 'Дом представлен на <a href="{L}">главной странице</a>.'
    DATA['ru'] = dict(
        btn='Бронирование и контакт',
        book='Если вы хотите остановиться в Хошимине, страница бронирования и контакта объясняет, как забронировать дом.',
        more_h2='Другие страницы на этом сайте',
        hub_h2='Четыре темы на день в Сайгоне',
        hub_p='Четыре страницы о дожде, одном дне в центре, выходе с семьёй или компанией и уличной еде.',
        cards=[
            ['Сайгон в дождь', 'guide-note-rain', 'Музеи, крытый рынок и кафе, когда идёт дождь.'],
            ['Сайгон за один день', 'guide-note-day', 'Круг по центру, без попытки увидеть всё.'],
            ['Сайгон с семьёй или компанией', 'guide-note-group', 'Зоопарк, водные куклы и общий стол.'],
            ['Уличная еда в Сайгоне', 'guide-note-food', 'Phở, bánh mì, cơm tấm и как выбрать лоток.'],
        ],
        links={
            'rain': L('Чтобы дополнить дождливый день, откройте ', g, ' и ', tg, home),
            'day': L('Чтобы собрать день спокойнее, откройте ', g, ' и ', tg, home),
            'group': L('С семьёй или компанией откройте ', g, ' и ', tg, home),
            'food': L('Если нужны ещё места поесть и походить, откройте ', g, ' и ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Сайгон в дождь: под крышей',
                'В Хошимине ливни обычны с мая по ноябрь. Музеи, дворец, почта, крытый рынок и кафе позволяют продолжить день в сухом месте. Часы работы уточняйте на месте.',
                'Сайгон в дождливый день',
                'Дождь не обязан отменять день в Хошимине. Музеи, крытый рынок и кафе — обычный план под крышей.',
                [S('Дождливые месяцы', 'У Хошимина тропический климат. Сильные ливни обычны примерно с мая по ноябрь, а более сухая погода типичнее с декабря по апрель. После сильного дождя в низинах вода может ненадолго стоять, а потом уходить. Во влажные месяцы в дне стоит иметь остановку под крышей.'),
                 S('Места под крышей', ul=[
                    'Музей военных свидетельств, Музей изобразительных искусств и Музей истории.',
                    'Дворец независимости: парадные залы и экспозиции внутри.',
                    'Центральная почта и собор находятся в одной центральной части города.',
                    'Рынок Бен Тхань крытый: там есть еда и мелкие товары.',
                    'Пагода Нефритового императора: обувь снимают, одежда спокойная, как во многих пагодах.',
                    'Водные куклы показывают в зале.',
                    'Кафе и магазины с кондиционером выручают, когда начинается ливень.']),
                 S('Как собрать день', 'Выберите один музей или дворец. Крытый рынок или кафе оставьте на самый мокрый отрезок. Пешеходную улицу Нгуен Хюэ можно поставить в конец, если дождь стихает. Собор, почта и пешеходная улица в одной центральной части. Часы работы меняются: уточняйте на месте.')]),
            'guide-note-day': page(
                'Сайгон за день: только центр',
                'Одного дня в Сайгоне хватает на центр: собор, почта, книжная улица, пешеходная улица и рынок Бен Тхань, плюс один музей или дворец. Уточните часы.',
                'Сайгон за один день',
                'Одного дня в Хошимине хватает на центр. Одного дня не хватает на каждый музей и каждый квартал.',
                [S('Круг по центру', 'Собор, центральная почта, книжная улица Нгуен Ван Бинь и пешеходная улица Нгуен Хюэ лежат в одной центральной части, и многие ходят между ними пешком. Рынок Бен Тхань — обычная остановка, чтобы поесть или посмотреть лотки. Добавьте дворец или один музей, а не все остальные точки в тот же день.'),
                 S('Между точками', ul=[
                    'В центре несколько этих мест достаточно близко, чтобы идти пешком.',
                    'Городские автобусы и метро от района рынка Бен Тхань закрывают более дальние отрезки.',
                    'Такси и машины из приложения очень распространены. Попросите включить счётчик или подтвердите поездку в приложении до выезда.',
                    'Мотоциклы — часть движения. Переходите в ритме пешеходов и не останавливайтесь посередине.']),
                 S('На другой день', 'Зоопарк, пагода, второй музей или место за городом, например тоннели Кути, просят отдельный день. В день по центру достаточно одной уличной еды и одного кофе. Phở, bánh mì или cơm tấm находятся легко. Холодный кофе со сгущённым молоком — самая обычная местная версия.')]),
            'guide-note-group': page(
                'Сайгон с семьёй или компанией',
                'Сайгон с детьми или компанией спокойнее, если в дне есть точка на улице и точка под крышей: зоопарк, водные куклы, музей и общий стол. В полдень жарко.',
                'Сайгон с семьёй или компанией',
                'Хошимин подходит семьям и компаниям, если день делится на одну точку на воздухе и одну под крышей.',
                [S('С детьми', ul=[
                    'Зоопарк и ботанический сад Сайгона — старый городской парк с тенистыми дорожками.',
                    'Водных кукол смотрят в зале, без большого количества реплик.',
                    'Крытые рынки людные. Держите детей за руку у дороги и между лотками.',
                    'В середине дня обычно жарко. Утро и конец дня подходят для улицы. Середина дня — для музея, кафе или паузы.',
                    'Пейте бутилированную или фильтрованную воду.',
                    'В пагодах и церквях уместна спокойная одежда. В пагодах обычно снимают обувь.']),
                 S('Компанией', 'Компания может заказать несколько небольших блюд у лотка или несколько тарелок в заведении с phở или cơm tấm. Пешеходная улица Нгуен Хюэ и площадка перед оперой — простые вечерние точки встречи. Выберите один музей или дворец, чтобы оставаться вместе, и оставьте время без программы вместо того, чтобы втиснуть каждую точку в один день.'),
                 S('Для всех', ul=[
                    'Мотоциклов много. Переходите вместе с другими, ровным шагом.',
                    'Маленькие лотки обычно берут наличные. На некоторых есть QR-код для перевода.',
                    'Примерно с мая по ноябрь держите под рукой список мест под крышей.'])]),
            'guide-note-food': page(
                'Уличная еда в Сайгоне',
                'Уличная еда в Сайгоне идёт от завтрака до вечера: phở, bánh mì, cơm tấm, bánh xèo и кофе с молоком. Выбирайте лоток, где готовят у вас на глазах.',
                'Уличная еда в Сайгоне',
                'Кухня на тротуаре — обычный способ есть в Хошимине, от завтрака до позднего вечера.',
                [S('Блюда, которые встречаются часто', ul=[
                    'Phở: суп с рисовой лапшой, часто с говядиной или курицей.',
                    'Bánh mì: багет с мясом, маринадами, травами и перцем чили.',
                    'Cơm tấm: дроблёный рис с жареными рёбрышками, яйцом и добавками.',
                    'Hủ tiếu и другие супы с лапшой на прозрачном бульоне.',
                    'Bánh xèo: хрустящий солёный блин с травами.',
                    'Gỏi cuốn: свежие роллы с травами.',
                    'Chè: сладкие супы.',
                    'Cà phê sữa đá — холодный кофе со сгущённым молоком. Bạc xỉu более молочный.']),
                 S('У лотка', 'Лоток ставит низкие табуреты на тротуар. Занятый лоток, где блюда выходят быстро, — обычный выбор. Смотрите, готовят ли при вас. Если нужно меньше чили, скажите при заказе. Вегетарианское часто помечают словом chay.'),
                 S('Полезные привычки', ul=[
                    'Завтрак — важное время уличной еды, особенно phở и bánh mì. Вечером больше жареного на огне и улиток.',
                    'Рынок Бен Тхань и многие дворовые улицы дают места посидеть и еду с собой.',
                    'Маленькие лотки часто предпочитают наличные. На некоторых есть QR-код для перевода.',
                    'Выбирайте еду, приготовленную при вас и поданную горячей. Пейте бутилированную или фильтрованную воду.',
                    'Не нужно гнаться за знаменитым именем. Обычный занятый лоток — городская привычка.'])]),
        },
    )

def sv(DATA, page, S, L):
    g, tg = 'reseguide till Saigon', 'guide till platser för den som bor där'
    home = 'Huset presenteras på <a href="{L}">startsidan</a>.'
    DATA['sv'] = dict(
        btn='Bokning och kontakt',
        book='Om ni vill bo i Ho Chi Minh visar sidan för bokning och kontakt hur ni bokar huset.',
        more_h2='Fler sidor på den här webbplatsen',
        hub_h2='Fyra ämnen för en dag i Saigon',
        hub_p='Fyra sidor om regn, en enda dag i centrum, en utflykt med familj eller sällskap, och gatumat.',
        cards=[
            ['Saigon en regnig dag', 'guide-note-rain', 'Museer, täckt marknad och kaféer när det regnar.'],
            ['Saigon på en dag', 'guide-note-day', 'Ett varv i centrum, utan att försöka se allt.'],
            ['Saigon med familj eller sällskap', 'guide-note-group', 'Zoo, vattenmarionetter och en delad måltid.'],
            ['Gatumat i Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm och hur man väljer ett stånd.'],
        ],
        links={
            'rain': L('För att fylla ut en regnig dag, öppna ', g, ' och ', tg, home),
            'day': L('För att lägga dagen lugnare, öppna ', g, ' och ', tg, home),
            'group': L('Med familj eller sällskap, öppna ', g, ' och ', tg, home),
            'food': L('För fler ställen att äta och gå, öppna ', g, ' och ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon i regn: inomhus',
                'I tropiska Ho Chi Minh är skurar vanliga från maj till november. Museer, palats, post, täckt marknad och kaféer gör att dagen kan fortsätta inomhus.',
                'Saigon en regnig dag',
                'Regn behöver inte ställa in en dag i Ho Chi Minh. Museer, en täckt marknad och kaféer är den vanliga planen inomhus.',
                [S('Regnmånaderna', 'Ho Chi Minh har tropiskt klimat. Kraftiga skurar är vanliga ungefär från maj till november, och torrare väder är mer typiskt från december till april. Efter ett häftigt regn kan vatten stå kvar en stund på låga ställen och sedan rinna undan. Under de blötare månaderna hör ett stopp inomhus hemma i dagen.'),
                 S('Platser inomhus', ul=[
                    'Krigsmuseet, konstmuseet och historiska museet.',
                    'Självständighetspalatset, med representationsrum och utställningar inomhus.',
                    'Centralposten och katedralen ligger i samma centrala område.',
                    'Ben Thanh-marknaden är en täckt marknad, med mat och småvaror.',
                    'Jadekejsarens pagod: man tar av skorna och klär sig återhållsamt, som i många pagoder.',
                    'Vattenmarionetter spelas i en sal.',
                    'Kaféer och butiker med luftkonditionering fungerar när en skur börjar.']),
                 S('Så kan dagen läggas', 'Välj ett museum eller palatset. Spara den täckta marknaden eller ett kafé till den blötaste delen. Gågatan Nguyen Hue kan vänta till slutet om regnet lättar. Katedral, post och gågata ligger i samma centrala område. Öppettiderna ändras: kontrollera dem på plats.')]),
            'guide-note-day': page(
                'Saigon på en dag i centrum',
                'En dag i Saigon räcker för centrum: katedral, post, bokgata, gågata och Ben Thanh-marknaden, plus ett museum eller palatset. Kontrollera tiderna på plats.',
                'Saigon på en dag',
                'En dag i Ho Chi Minh räcker för centrum. En dag räcker inte för varje museum och varje kvarter.',
                [S('Ett varv i centrum', 'Katedralen, centralposten, bokgatan Nguyen Van Binh och gågatan Nguyen Hue ligger i samma centrala område, och många går till fots mellan dem. Ben Thanh-marknaden är det vanliga stoppet för en måltid eller en titt på stånden. Lägg till palatset eller ett museum, inte alla andra punkter samma dag.'),
                 S('Mellan platserna', ul=[
                    'I centrum ligger flera av punkterna nära nog för att gå.',
                    'Stadsbussar och metron från Ben Thanh-området täcker längre sträckor.',
                    'Taxibilar och bilar som beställs i en app är mycket vanliga. Be om taxametern, eller bekräfta resan i appen innan ni åker.',
                    'Motorcyklar är en del av trafiken. Gå över i fotgängarnas takt och stanna inte mitt i.']),
                 S('Spara till en annan dag', 'Djurparken, en pagod, ett andra museum eller en plats utanför staden, som tunnlarna i Cu Chi, behöver en egen dag. Under centrumdagen räcker en gatamåltid och ett kaffe. Phở, bánh mì eller cơm tấm är lätta att hitta. Iskaffe med kondenserad mjölk är den vanligaste lokala varianten.')]),
            'guide-note-group': page(
                'Saigon med familj eller sällskap',
                'Saigon med barn eller sällskap fungerar bättre med ett stopp utomhus och ett inomhus: zoo, vattenmarionetter, ett museum och en delad måltid.',
                'Saigon med familj eller i sällskap',
                'Ho Chi Minh passar familjer och sällskap om dagen har ett stopp utomhus och ett inomhus.',
                [S('Med barn', ul=[
                    'Saigons djurpark och botaniska trädgård är en gammal stadspark, med skuggiga gångar.',
                    'Vattenmarionetter ses i en sal och går att följa utan mycket tal.',
                    'Täckta marknader är livliga. Håll barn i handen vid gatan och mellan stånden.',
                    'Mitt på dagen är det ofta varmt. Morgon och sen eftermiddag passar utomhus. Mitt på dagen passar ett museum, ett kafé eller en paus.',
                    'Drick vatten på flaska eller filtrerat vatten.',
                    'Vid pagoder och kyrkor passar återhållsamma kläder. I pagoder tar man oftast av sig skorna.']),
                 S('Med ett sällskap', 'Ett sällskap kan beställa flera små rätter vid ett stånd, eller några tallrikar på ett ställe med phở eller cơm tấm. Gågatan Nguyen Hue och ytan framför operan är enkla mötesplatser på kvällen. Välj ett museum eller palatset så att sällskapet håller ihop, och lämna tid utan schema i stället för att pressa in varje punkt.'),
                 S('För alla', ul=[
                    'Motorcykeltrafiken är tät. Gå över tillsammans med andra, i jämn takt.',
                    'Små stånd tar oftast emot kontanter. En del visar också en QR-kod för en överföring.',
                    'Från ungefär maj till november är en lista med platser inomhus bra att ha.'])]),
            'guide-note-food': page(
                'Gatumat i Saigon',
                'Gatumat i Saigon pågår från frukost till kväll: phở, bánh mì, cơm tấm, bánh xèo och kaffe med mjölk. Välj ett stånd där de lagar maten framför er.',
                'Gatumat i Saigon',
                'Kök på trottoaren är ett vanligt sätt att äta i Ho Chi Minh, från frukost till sent på kvällen.',
                [S('Rätter som syns ofta', ul=[
                    'Phở: soppa med risnudlar, ofta med nötkött eller kyckling.',
                    'Bánh mì: baguette med kött, pickles, örter och chili.',
                    'Cơm tấm: brutet ris med grillat revben, ägg och tillbehör.',
                    'Hủ tiếu och andra nudelsoppor på klar buljong.',
                    'Bánh xèo: knaprig salt pannkaka, med örter.',
                    'Gỏi cuốn: färska rullar med örter.',
                    'Chè: söta soppdesserter.',
                    'Cà phê sữa đá är iskaffe med kondenserad mjölk. Bạc xỉu är mjölkigare.']),
                 S('Vid ståndet', 'Ståndet ställer låga pallar på trottoaren. Ett välbesökt stånd, där rätterna kommer snabbt, är det vanliga valet. Se att maten lagas framför er. Vill ni ha mindre chili, säg det när ni beställer. Vegetarisk mat markeras ofta med ordet chay.'),
                 S('Vana att ha med sig', ul=[
                    'Frukosten är en viktig tid för gatumat, särskilt phở och bánh mì. På kvällen kommer mer grillat och snäckor.',
                    'Ben Thanh-marknaden och många kvartersgator har sittplatser och mat att ta med.',
                    'Små stånd vill ofta ha kontanter. En del visar en QR-kod för en överföring.',
                    'Välj mat som lagas framför er och serveras varm. Drick vatten på flaska eller filtrerat vatten.',
                    'Ni behöver inte jaga ett känt namn. Ett vanligt, fullt stånd är stadens mönster.'])]),
        },
    )

def tr(DATA, page, S, L):
    g, tg = 'Saygon gezi rehberi', 'konaklayanlar için yer rehberi'
    home = 'Ev, <a href="{L}">ana sayfada</a> tanıtılır.'
    DATA['tr'] = dict(
        btn='Rezervasyon ve iletişim',
        book='Ho Chi Minh’de kalmak isterseniz, rezervasyon ve iletişim sayfası evin nasıl rezerve edileceğini anlatır.',
        more_h2='Bu sitedeki diğer sayfalar',
        hub_h2='Saygon’da bir gün için dört konu',
        hub_p='Yağmur, merkezde tek gün, aile veya grup çıkışı ve sokak yemeği üzerine dört sayfa.',
        cards=[
            ['Yağmurlu günde Saygon', 'guide-note-rain', 'Yağmurda müze, kapalı pazar ve kafeler.'],
            ['Saygon’u bir günde', 'guide-note-day', 'Merkezde bir tur, her yeri görmeye çalışmadan.'],
            ['Saygon aile veya grupla', 'guide-note-group', 'Hayvanat bahçesi, su kuklası ve ortak sofra.'],
            ['Saygon sokak lezzetleri', 'guide-note-food', 'Phở, bánh mì, cơm tấm ve tezgâh seçimi.'],
        ],
        links={
            'rain': L('Yağmurlu günü tamamlamak için ', g, ' ile ', tg, home),
            'day': L('Günü daha sakin kurmak için ', g, ' ile ', tg, home),
            'group': L('Aile veya grupla gidecekseniz ', g, ' ile ', tg, home),
            'food': L('Yemek ve yürümek için daha fazla yer arıyorsanız ', g, ' ile ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Yağmurlu günde Saygon: kapalı plan',
                'Ho Chi Minh’de sağanaklar mayıstan kasıma kadar sık görülür. Müze, saray, postane, kapalı pazar ve kafeler günü kuru yerde sürdürmeyi sağlar.',
                'Yağmurlu bir günde Saygon',
                'Yağmur, Ho Chi Minh’de bir günü iptal etmek zorunda değildir. Müze, kapalı pazar ve kafeler alışılmış kapalı plandır.',
                [S('Yağmur ayları', 'Ho Chi Minh tropikal iklimdedir. Şiddetli sağanaklar yaklaşık mayıstan kasıma kadar yaygındır; daha kuru hava aralıktan nisana daha tipiktir. Sert bir yağmurdan sonra alçak yerlerde su bir süre durup sonra çekilebilir. Nemli aylarda günün içinde kapalı bir durak bulundurmak yerinde olur.'),
                 S('Kapalı yerler', ul=[
                    'Savaş Kalıntıları Müzesi, Güzel Sanatlar Müzesi ve Tarih Müzesi.',
                    'Bağımsızlık Sarayı: kabul salonları ve iç mekân sergileri.',
                    'Merkez postane ile katedral aynı merkez bölgededir.',
                    'Ben Thanh Pazarı kapalı bir pazardır; yemek ve küçük eşya vardır.',
                    'Yeşim İmparator Tapınağı: birçok tapınakta olduğu gibi ayakkabı çıkarılır, sade giyinilir.',
                    'Su kuklası gösterileri bir salonda oynanır.',
                    'Sağanak başlayınca kafeler ve klimalı dükkânlar işe yarar.']),
                 S('Günü dizmek', 'Bir müze ya da sarayı seçin. Kapalı pazarı veya bir kafeyi en yoğun yağmura ayırın. Yağmur dinerse Nguyen Hue yürüyüş sokağı günün sonuna kalabilir. Katedral, postane ve yürüyüş sokağı aynı merkez bölgededir. Açılış saatleri değişir: yerinde kontrol edin.')]),
            'guide-note-day': page(
                'Saygon’da bir gün: merkez',
                'Saygon’da bir gün merkeze yeter: katedral, postane, kitap sokağı, yürüyüş sokağı ve Ben Thanh Pazarı, artı bir müze ya da saray. Saati yerinde sorun.',
                'Saygon’da bir gün',
                'Ho Chi Minh’de bir gün merkeze yeter. Bir gün her müzeye ve her mahalleye yetmez.',
                [S('Merkez turu', 'Katedral, merkez postane, Nguyen Van Binh kitap sokağı ve Nguyen Hue yürüyüş sokağı aynı merkez bölgededir; birçok kişi aralarında yürür. Ben Thanh Pazarı yemek ya da tezgâh bakmak için alışılmış duraktır. Aynı güne sarayı ya da bir müzeyi ekleyin, kalan her noktayı değil.'),
                 S('Noktalar arasında', ul=[
                    'Merkezde bu durakların bir kısmı yürünecek kadar yakındır.',
                    'Şehir otobüsleri ve Ben Thanh çevresinden kalkan metro daha uzun aralıkları kapsar.',
                    'Taksi ve uygulamadan çağrılan arabalar çok kullanılır. Şoförden taksimetreyi açmasını isteyin ya da yola çıkmadan önce uygulamada yolculuğu onaylayın.',
                    'Motosikletler trafiğin parçasıdır. Yayaların temposunda geçin, akışın ortasında durmayın.']),
                 S('Başka güne bırakın', 'Hayvanat bahçesi, bir tapınak, ikinci müze ya da Cu Chi tünelleri gibi kent dışındaki bir yer ayrı gün ister. Merkez gününde bir sokak yemeği ve bir kahve yeter. Phở, bánh mì ya da cơm tấm kolay bulunur. Kondanse sütlü buzlu kahve en yaygın yerel biçimdir.')]),
            'guide-note-group': page(
                'Saygon aile veya grupla',
                'Çocuklarla ya da grupla Saygon, günde bir açık hava ve bir kapalı durakla daha rahattır: hayvanat bahçesi, su kuklası, bir müze ve ortak sofra.',
                'Saygon’da aile veya grup',
                'Ho Chi Minh, gün bir açık hava durağı ve bir kapalı durak içerirse ailelere ve gruplara uyar.',
                [S('Çocuklarla', ul=[
                    'Saygon hayvanat bahçesi ve botanik bahçesi, gölgeli yolları olan eski bir kent parkıdır.',
                    'Su kuklaları bir salonda izlenir, çok konuşma olmadan da takip edilir.',
                    'Kapalı pazarlar kalabalıktır. Yol kenarında ve tezgâhlar arasında çocukların elini tutun.',
                    'Günün ortası genellikle sıcaktır. Sabah ve geç öğleden sonra dışarıya uyar. Öğle, müze, kafe ya da dinlenme için uygundur.',
                    'Şişe suyu ya da süzülmüş su için.',
                    'Tapınak ve kiliselerde sade giyim beklenir. Tapınaklarda genellikle ayakkabı çıkarılır.']),
                 S('Bir grupla', 'Grup, bir tezgahta birkaç küçük tabak ya da bir phở veya cơm tấm yerinde birkaç porsiyon isteyebilir. Nguyen Hue yürüyüş sokağı ve opera önündeki alan akşam için kolay buluşma noktalarıdır. Birlikte kalmak için bir müze ya da saray seçin; her noktayı aynı güne sıkıştırmak yerine programsız bir süre bırakın.'),
                 S('Herkes için notlar', ul=[
                    'Motosiklet trafiği yoğundur. Başkalarıyla birlikte, dengeli bir tempoda geçin.',
                    'Küçük tezgâhlar genellikle nakit alır. Bazılarında havale için bir QR kodu da vardır.',
                    'Mayıstan kasıma kadar kapalı yerlerin bir listesini el altında tutun.'])]),
            'guide-note-food': page(
                'Saygon sokak lezzetleri',
                'Saygon sokak yemeği kahvaltıdan akşama sürer: phở, bánh mì, cơm tấm, bánh xèo ve sütlü kahve. Yemeğin önünüzde piştiği kalabalık bir tezgâh seçin.',
                'Saygon’da sokak yemeği',
                'Kaldırımda pişirmek, Ho Chi Minh’de kahvaltıdan geceye kadar olağan bir yeme biçimidir.',
                [S('Sık görülen yemekler', ul=[
                    'Phở: pirinç eriştesi çorbası, çoğu zaman dana ya da tavukla.',
                    'Bánh mì: et, turşu, ot ve acı biberli baget.',
                    'Cơm tấm: ızgara pirzola, yumurta ve yanlarla kırık pirinç.',
                    'Hủ tiếu ve berrak sulu diğer erişte çorbaları.',
                    'Bánh xèo: otlarla yenilen çıtır tuzlu krep.',
                    'Gỏi cuốn: otlu taze sarma.',
                    'Chè: tatlı çorbalar.',
                    'Cà phê sữa đá, kondanse sütlü buzlu kahvedir. Bạc xỉu daha sütlüdür.']),
                 S('Tezgahta', 'Tezgâh kaldırıma alçak tabure koyar. Yemeklerin hızlı çıktığı kalabalık tezgâh alışılmış seçimdir. Yemeğin önünüzde pişmesine bakın. Daha az acı isterseniz siparişte söyleyin. Vejetaryen yemekler çoğu zaman chay sözcüğüyle işaretlenir.'),
                 S('İş gören alışkanlıklar', ul=[
                    'Kahvaltı, özellikle phở ve bánh mì için önemli bir sokak yemeği saatidir. Akşam ızgara ve salyangoz artar.',
                    'Ben Thanh Pazarı ve birçok mahalle sokağında oturarak yenen ve paket yerler vardır.',
                    'Küçük tezgâhlar çoğu zaman nakit ister. Bazılarında havale için QR kodu vardır.',
                    'Önünüzde pişen ve sıcak servis edilen yemeği seçin. Şişe suyu ya da süzülmüş su için.',
                    'Ünlü bir adın peşine düşmek gerekmez. Sıradan ve kalabalık bir tezgâh kentin biçimidir.'])]),
        },
    )

def id_(DATA, page, S, L):
    g, tg = 'panduan wisata Saigon', 'panduan tempat bagi yang menginap'
    home = 'Rumahnya diperkenalkan di <a href="{L}">beranda</a>.'
    DATA['id'] = dict(
        btn='Pemesanan dan kontak',
        book='Jika Anda ingin menginap di Ho Chi Minh, halaman pemesanan dan kontak menjelaskan cara memesan rumahnya.',
        more_h2='Halaman lain di situs ini',
        hub_h2='Empat topik untuk sehari di Saigon',
        hub_p='Empat halaman tentang hujan, satu hari di pusat kota, keluar bersama keluarga atau rombongan, dan makanan kaki lima.',
        cards=[
            ['Saigon saat hujan', 'guide-note-rain', 'Museum, pasar beratap, dan kafe ketika hujan.'],
            ['Saigon dalam satu hari', 'guide-note-day', 'Putaran di pusat kota, tanpa mencoba melihat semua.'],
            ['Saigon bersama keluarga atau rombongan', 'guide-note-group', 'Kebun binatang, wayang air, dan makan bersama.'],
            ['Makanan kaki lima di Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm, dan cara memilih gerobak.'],
        ],
        links={
            'rain': L('Untuk melengkapi hari hujan, buka ', g, ' dan ', tg, home),
            'day': L('Untuk menyusun hari dengan lebih tenang, buka ', g, ' dan ', tg, home),
            'group': L('Bersama keluarga atau rombongan, buka ', g, ' dan ', tg, home),
            'food': L('Jika ingin lebih banyak tempat makan dan berjalan, buka ', g, ' dan ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon saat hujan: di dalam ruangan',
                'Di Ho Chi Minh, hujan lebat biasa dari Mei sampai November. Museum, istana, kantor pos, pasar beratap, dan kafe membuat hari tetap jalan di tempat teduh.',
                'Saigon pada hari hujan',
                'Hujan tidak harus membatalkan sehari di Ho Chi Minh. Museum, pasar beratap, dan kafe adalah rencana yang biasa di dalam ruangan.',
                [S('Bulan-bulan hujan', 'Ho Chi Minh beriklim tropis. Hujan lebat biasa terjadi kira-kira dari Mei sampai November, dan cuaca lebih kering lebih khas dari Desember sampai April. Setelah hujan deras, bagian rendah bisa menahan air sebentar lalu mengalir. Pada bulan lembap, ada baiknya satu perhentian beratap masuk dalam rencana.'),
                 S('Tempat di dalam atau beratap', ul=[
                    'Museum Peninggalan Perang, Museum Seni Rupa, dan Museum Sejarah.',
                    'Istana Kemerdekaan, dengan ruang penerimaan dan pameran di dalam.',
                    'Kantor pos pusat dan katedral berada di kawasan pusat yang sama.',
                    'Pasar Ben Thanh adalah pasar beratap, dengan makanan dan barang kecil.',
                    'Kuil Kaisar Giok: sepatu dilepas dan pakaian sopan, seperti di banyak kuil.',
                    'Pertunjukan wayang air dimainkan di dalam ruangan.',
                    'Kafe dan toko berpendingin berguna saat hujan mulai.']),
                 S('Cara menyusun hari', 'Pilih satu museum atau istana. Simpan pasar beratap atau kafe untuk bagian hujan yang paling deras. Jalan pejalan kaki Nguyen Hue bisa di akhir jika hujan mereda. Katedral, kantor pos, dan jalan itu berada di kawasan pusat yang sama. Jam buka berubah: periksa di tempat.')]),
            'guide-note-day': page(
                'Saigon sehari di pusat kota',
                'Sehari di Saigon cukup untuk pusat kota: katedral, kantor pos, jalan buku, jalan pejalan kaki, dan Pasar Ben Thanh, plus satu museum atau istana.',
                'Saigon dalam satu hari',
                'Sehari di Ho Chi Minh cukup untuk pusat kota. Sehari tidak cukup untuk setiap museum dan setiap kawasan.',
                [S('Putaran di pusat', 'Katedral, kantor pos pusat, jalan buku Nguyen Van Binh, dan jalan pejalan kaki Nguyen Hue berada di kawasan pusat yang sama, jadi banyak orang berjalan di antaranya. Pasar Ben Thanh adalah perhentian biasa untuk makan atau melihat gerobak. Tambahkan istana atau satu museum, bukan semua titik lain pada hari yang sama.'),
                 S('Berpindah tempat', ul=[
                    'Di pusat, beberapa titik ini cukup dekat untuk ditempuh dengan berjalan.',
                    'Bus kota dan metro dari kawasan Ben Thanh mencakup jarak yang lebih jauh.',
                    'Taksi dan mobil yang dipesan lewat aplikasi sangat lazim. Minta sopir memakai argo, atau konfirmasi perjalanan di aplikasi sebelum berangkat.',
                    'Sepeda motor adalah bagian dari lalu lintas. Menyeberang mengikuti irama pejalan kaki, jangan berhenti di tengah arus.']),
                 S('Simpan untuk hari lain', 'Kebun binatang, sebuah kuil, museum kedua, atau tempat di luar kota seperti terowongan Cu Chi, minta hari sendiri. Pada hari di pusat, satu makan kaki lima dan satu kopi sudah cukup. Phở, bánh mì, atau cơm tấm mudah ditemukan. Kopi es dengan susu kental adalah bentuk lokal yang paling umum.')]),
            'guide-note-group': page(
                'Saigon bersama keluarga atau rombongan',
                'Saigon bersama anak atau rombongan lebih mudah bila hari punya titik di luar dan di dalam: kebun binatang, wayang air, satu museum, dan makan bersama.',
                'Saigon dengan keluarga atau rombongan',
                'Ho Chi Minh cocok untuk keluarga dan rombongan bila hari dibagi antara satu tempat terbuka dan satu tempat beratap.',
                [S('Bersama anak', ul=[
                    'Kebun binatang dan kebun raya Saigon adalah taman kota yang sudah lama, dengan jalur yang teduh.',
                    'Wayang air ditonton di dalam ruangan dan bisa diikuti tanpa banyak dialog.',
                    'Pasar beratap ramai. Pegang tangan anak di dekat jalan dan di antara gerobak.',
                    'Tengah hari biasanya panas. Pagi dan sore akhir cocok di luar. Tengah hari cocok untuk museum, kafe, atau istirahat.',
                    'Minum air kemasan atau air yang disaring.',
                    'Di kuil dan gereja, pakaian sopan diharapkan. Di kuil biasanya sepatu dilepas.']),
                 S('Bersama rombongan', 'Rombongan bisa memesan beberapa piring kecil di gerobak, atau beberapa porsi di tempat phở atau cơm tấm. Jalan pejalan kaki Nguyen Hue dan lahan di depan gedung opera adalah titik temu yang mudah pada malam hari. Pilih satu museum atau istana agar tetap bersama, dan sisakan waktu tanpa jadwal alih-alih memasukkan setiap titik.'),
                 S('Catatan untuk semua', ul=[
                    'Lalu lintas sepeda motor padat. Menyeberang bersama orang lain, dengan langkah yang rata.',
                    'Gerobak kecil biasanya menerima uang tunai. Sebagian juga menampilkan kode QR untuk transfer.',
                    'Dari sekitar Mei sampai November, siapkan daftar tempat beratap.'])]),
            'guide-note-food': page(
                'Makanan kaki lima di Saigon',
                'Makanan kaki lima di Saigon berjalan dari sarapan sampai malam: phở, bánh mì, cơm tấm, bánh xèo, dan kopi susu. Pilih gerobak yang memasak di depan Anda.',
                'Makanan kaki lima di Saigon',
                'Memasak di trotoar adalah cara makan yang biasa di Ho Chi Minh, dari sarapan sampai larut malam.',
                [S('Hidangan yang sering terlihat', ul=[
                    'Phở: sup mi beras, sering dengan daging sapi atau ayam.',
                    'Bánh mì: baguette dengan daging, acar, daun, dan cabai.',
                    'Cơm tấm: nasi patah dengan iga bakar, telur, dan lauk.',
                    'Hủ tiếu dan sup mi lain dengan kuah bening.',
                    'Bánh xèo: kue gurih renyah, dengan daun.',
                    'Gỏi cuốn: gulungan segar dengan daun.',
                    'Chè: hidangan manis berkuah.',
                    'Cà phê sữa đá adalah kopi es dengan susu kental. Bạc xỉu lebih banyak susunya.']),
                 S('Di gerobak', 'Gerobak menaruh bangku rendah di trotoar. Gerobak ramai, dengan piring yang keluar cepat, adalah pilihan yang biasa. Lihat makanan dimasak di depan Anda. Jika ingin lebih sedikit cabai, katakan saat memesan. Makanan vegetarian sering ditandai dengan kata chay.'),
                 S('Kebiasaan yang berguna', ul=[
                    'Sarapan adalah waktu penting makanan kaki lima, terutama phở dan bánh mì. Malam hari menambah panggangan dan siput.',
                    'Pasar Ben Thanh dan banyak jalan kampung punya tempat duduk dan makanan dibawa pulang.',
                    'Gerobak kecil sering lebih suka uang tunai. Sebagian menampilkan kode QR untuk transfer.',
                    'Pilih makanan yang dimasak di depan Anda dan dihidangkan panas. Minum air kemasan atau air yang disaring.',
                    'Tidak perlu mengejar nama yang terkenal. Gerobak biasa yang ramai adalah pola kota ini.'])]),
        },
    )

def ms(DATA, page, S, L):
    g, tg = 'panduan pelancongan Saigon', 'panduan tempat untuk tetamu yang menginap'
    home = 'Rumah diperkenalkan di <a href="{L}">halaman utama</a>.'
    DATA['ms'] = dict(
        btn='Tempahan dan hubungi',
        book='Jika anda ingin menginap di Ho Chi Minh, halaman tempahan dan hubungan menerangkan cara menempah rumah itu.',
        more_h2='Halaman lain di laman ini',
        hub_h2='Empat topik untuk sehari di Saigon',
        hub_p='Empat halaman tentang hujan, satu hari di pusat bandar, keluar bersama keluarga atau kumpulan, dan makanan jalanan.',
        cards=[
            ['Saigon pada hari hujan', 'guide-note-rain', 'Muzium, pasar beratap, dan kafe semasa hujan.'],
            ['Saigon dalam satu hari', 'guide-note-day', 'Pusingan di pusat bandar, tanpa cuba melihat semua.'],
            ['Saigon bersama keluarga atau kumpulan', 'guide-note-group', 'Zoo, wayang air, dan hidangan berkongsi.'],
            ['Makanan jalanan di Saigon', 'guide-note-food', 'Phở, bánh mì, cơm tấm, dan cara memilih gerai.'],
        ],
        links={
            'rain': L('Untuk melengkapkan hari hujan, buka ', g, ' dan ', tg, home),
            'day': L('Untuk menyusun hari dengan lebih tenang, buka ', g, ' dan ', tg, home),
            'group': L('Bersama keluarga atau kumpulan, buka ', g, ' dan ', tg, home),
            'food': L('Jika mahu lebih banyak tempat makan dan berjalan, buka ', g, ' dan ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'Saigon waktu hujan: di dalam bangunan',
                'Di Ho Chi Minh, hujan lebat biasa dari Mei hingga November. Muzium, istana, pejabat pos, pasar beratap dan kafe membantu meneruskan hari di tempat kering.',
                'Saigon pada hari hujan',
                'Hujan tidak semestinya membatalkan sehari di Ho Chi Minh. Muzium, pasar beratap dan kafe ialah pelan biasa di dalam bangunan.',
                [S('Bulan hujan', 'Ho Chi Minh beriklim tropika. Hujan lebat biasa kira-kira dari Mei hingga November, dan cuaca lebih kering lebih tipikal dari Disember hingga April. Selepas hujan deras, tempat rendah boleh menakung air seketika lalu mengalir. Pada bulan lembap, satu hentian beratap patut ada dalam hari itu.'),
                 S('Tempat beratap', ul=[
                    'Muzium Tinggalan Perang, Muzium Seni Halus dan Muzium Sejarah.',
                    'Istana Kemerdekaan, dengan dewan sambutan dan pameran di dalam.',
                    'Pejabat pos pusat dan katedral berada di kawasan pusat yang sama.',
                    'Pasar Ben Thanh ialah pasar beratap, dengan makanan dan barang kecil.',
                    'Tokong Maharaja Jed: kasut ditanggalkan dan pakaian sopan, seperti di banyak tokong.',
                    'Wayang air dipersembahkan di dalam dewan.',
                    'Kafe dan kedai berhawa dingin berguna apabila hujan bermula.']),
                 S('Cara susun hari', 'Pilih satu muzium atau istana. Simpan pasar beratap atau kafe untuk bahagian hujan yang paling lebat. Jalan pejalan kaki Nguyen Hue boleh di akhir jika hujan reda. Katedral, pejabat pos dan jalan itu berada di kawasan pusat yang sama. Waktu buka berubah: sahkan di tempat.')]),
            'guide-note-day': page(
                'Saigon sehari di pusat bandar',
                'Sehari di Saigon memadai untuk pusat bandar: katedral, pejabat pos, jalan buku, jalan pejalan kaki dan Pasar Ben Thanh, serta satu muzium atau istana.',
                'Saigon dalam satu hari',
                'Sehari di Ho Chi Minh memadai untuk pusat bandar. Sehari tidak memadai untuk setiap muzium dan setiap kawasan.',
                [S('Pusingan di pusat', 'Katedral, pejabat pos pusat, jalan buku Nguyen Van Binh dan jalan pejalan kaki Nguyen Hue berada di kawasan pusat yang sama, jadi ramai orang berjalan antara tempat itu. Pasar Ben Thanh ialah hentian biasa untuk makan atau melihat gerai. Tambah istana atau satu muzium, bukan semua tempat lain pada hari yang sama.'),
                 S('Dari satu tempat ke tempat lain', ul=[
                    'Di pusat, beberapa tempat ini cukup dekat untuk berjalan kaki.',
                    'Bas bandar dan metro dari kawasan Ben Thanh merangkumi jarak yang lebih jauh.',
                    'Teksi dan kereta yang ditempah melalui aplikasi sangat biasa. Minta pemandu menggunakan meter, atau sahkan perjalanan dalam aplikasi sebelum bertolak.',
                    'Motosikal ialah sebahagian daripada lalu lintas. Lintasi mengikut rentak pejalan kaki, jangan berhenti di tengah arus.']),
                 S('Simpan untuk hari lain', 'Zoo, sebuah tokong, muzium kedua, atau tempat di luar bandar seperti terowong Cu Chi, memerlukan hari sendiri. Pada hari di pusat, satu hidangan jalanan dan satu kopi sudah memadai. Phở, bánh mì atau cơm tấm mudah ditemui. Kopi ais dengan susu pekat ialah bentuk tempatan yang paling biasa.')]),
            'guide-note-group': page(
                'Saigon bersama keluarga atau kumpulan',
                'Saigon bersama kanak-kanak atau kumpulan lebih mudah jika ada tempat terbuka dan tempat beratap: zoo, wayang air, satu muzium dan hidangan bersama.',
                'Saigon dengan keluarga atau kumpulan',
                'Ho Chi Minh sesuai untuk keluarga dan kumpulan jika hari dibahagi antara satu tempat terbuka dan satu tempat beratap.',
                [S('Bersama kanak-kanak', ul=[
                    'Zoo dan taman botani Saigon ialah taman bandar yang lama, dengan laluan yang teduh.',
                    'Wayang air ditonton di dalam dewan dan boleh diikuti tanpa banyak dialog.',
                    'Pasar beratap sesak. Pegang tangan kanak-kanak berhampiran jalan dan antara gerai.',
                    'Tengah hari biasanya panas. Pagi dan lewat petang sesuai di luar. Tengah hari sesuai untuk muzium, kafe atau rehat.',
                    'Minum air berbotol atau air yang ditapis.',
                    'Di tokong dan gereja, pakaian sopan dijangka. Di tokong biasanya kasut ditanggalkan.']),
                 S('Bersama kumpulan', 'Kumpulan boleh memesan beberapa hidangan kecil di gerai, atau beberapa pinggan di kedai phở atau cơm tấm. Jalan pejalan kaki Nguyen Hue dan ruang di hadapan rumah opera ialah tempat bertemu yang mudah pada waktu malam. Pilih satu muzium atau istana supaya kekal bersama, dan tinggalkan masa tanpa jadual daripada memasukkan setiap tempat.'),
                 S('Nota untuk semua', ul=[
                    'Lalu lintas motosikal padat. Lintasi bersama orang lain, dengan langkah yang rata.',
                    'Gerai kecil biasanya menerima wang tunai. Sesetengahnya juga memaparkan kod QR untuk pindahan.',
                    'Dari sekitar Mei hingga November, sediakan senarai tempat beratap.'])]),
            'guide-note-food': page(
                'Makanan jalanan di Saigon',
                'Makanan jalanan di Saigon bermula dari sarapan hingga malam: phở, bánh mì, cơm tấm, bánh xèo dan kopi susu. Pilih gerai yang memasak di hadapan anda.',
                'Makanan jalanan di Saigon',
                'Memasak di kaki lima ialah cara makan yang biasa di Ho Chi Minh, dari sarapan hingga lewat malam.',
                [S('Hidangan yang kerap kelihatan', ul=[
                    'Phở: sup mi beras, selalunya dengan daging lembu atau ayam.',
                    'Bánh mì: baguette dengan daging, jeruk, herba dan cili.',
                    'Cơm tấm: nasi patah dengan rusuk bakar, telur dan lauk.',
                    'Hủ tiếu dan sup mi lain dengan kuah jernih.',
                    'Bánh xèo: lempeng masin yang rangup, dengan herba.',
                    'Gỏi cuốn: gulungan segar dengan herba.',
                    'Chè: hidangan manis berkuah.',
                    'Cà phê sữa đá ialah kopi ais dengan susu pekat. Bạc xỉu lebih banyak susu.']),
                 S('Di gerai', 'Gerai meletakkan bangku rendah di kaki lima. Gerai yang sesak, dengan hidangan yang keluar cepat, ialah pilihan biasa. Lihat makanan dimasak di hadapan anda. Jika mahu kurang cili, katakan semasa memesan. Makanan vegetarian sering ditanda dengan perkataan chay.'),
                 S('Tabiat yang berguna', ul=[
                    'Sarapan ialah waktu penting makanan jalanan, terutama phở dan bánh mì. Pada waktu malam ada lebih banyak hidangan bakar dan siput.',
                    'Pasar Ben Thanh dan banyak jalan kejiranan ada tempat duduk dan makanan bungkus.',
                    'Gerai kecil sering lebih suka wang tunai. Sesetengahnya memaparkan kod QR untuk pindahan.',
                    'Pilih makanan yang dimasak di hadapan anda dan dihidang panas. Minum air berbotol atau air yang ditapis.',
                    'Tidak perlu mengejar nama yang terkenal. Gerai biasa yang sesak ialah corak bandar ini.'])]),
        },
    )

def th(DATA, page, S, L):
    g, tg = 'คู่มือเที่ยวไซง่อน', 'คู่มือสถานที่สำหรับผู้เข้าพัก'
    home = 'บ้านถูกแนะนำไว้ที่<a href="{L}">หน้าแรก</a>.'
    DATA['th'] = dict(
        btn='จองและติดต่อ',
        book='หากต้องการพักในโฮจิมินห์ หน้าจองและติดต่ออธิบายวิธีจองบ้านหลังนี้.',
        more_h2='หน้าอื่นบนเว็บไซต์นี้',
        hub_h2='สี่เรื่องสำหรับหนึ่งวันในไซง่อน',
        hub_p='สี่หน้าเรื่องวันฝน หนึ่งวันในย่านกลางเมือง การออกไปกับครอบครัวหรือกลุ่ม และอาหารริมทาง.',
        cards=[
            ['ไซง่อนวันฝน', 'guide-note-rain', 'พิพิธภัณฑ์ ตลาดมีหลังคา และร้านกาแฟเมื่อฝนตก.'],
            ['ไซง่อนในหนึ่งวัน', 'guide-note-day', 'วนย่านกลางเมือง โดยไม่พยายามเก็บทุกจุด.'],
            ['ไซง่อนกับครอบครัวหรือกลุ่ม', 'guide-note-group', 'สวนสัตว์ หุ่นกระบอกน้ำ และมื้ออาหารร่วมกัน.'],
            ['อาหารริมทางในไซง่อน', 'guide-note-food', 'เฝอ บั่ญหมี่ ข้าวแตก และวิธีเลือกแผงลอย.'],
        ],
        links={
            'rain': L('เพื่อต่อวันฝนเข้ากับช่วงที่เหลือของการเดินทาง ดู', g, ' และ', tg, home),
            'day': L('เพื่อจัดหนึ่งวันให้สบายขึ้น ดู', g, ' และ', tg, home),
            'group': L('เมื่อไปกับครอบครัวหรือกลุ่ม ดู', g, ' และ', tg, home),
            'food': L('หากต้องการที่กินและที่เดินเพิ่ม ดู', g, ' และ', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'ไซง่อนวันฝน: อยู่ในร่ม',
                'ที่โฮจิมินห์ ฝนหนักพบได้บ่อยราวเดือนพฤษภาคมถึงพฤศจิกายน พิพิธภัณฑ์ พระราชวัง ที่ทำการไปรษณีย์ ตลาดมีหลังคา และร้านกาแฟทำให้วันนั้นไปต่อในที่แห้งได้.',
                'ไซง่อนในวันที่ฝนตก',
                'ฝนไม่จำเป็นต้องยกเลิกทั้งวันในโฮจิมินห์ พิพิธภัณฑ์ ตลาดมีหลังคา และร้านกาแฟเป็นแผนในร่มที่พบบ่อย.',
                [S('เดือนที่ฝนชุก', 'โฮจิมินห์เป็นเมืองร้อนชื้น ฝนหนักพบบ่อยราวเดือนพฤษภาคมถึงพฤศจิกายน ส่วนช่วงธันวาคมถึงเมษายนอากาศแห้งกว่า หลังฝนหนัก จุดต่ำอาจมีน้ำขังครู่หนึ่งแล้วไหลไป ในเดือนชื้น ควรวางจุดในร่มไว้ในแผนของวัน.'),
                 S('ที่ในร่มหรือมีหลังคา', ul=[
                    'พิพิธภัณฑ์หลักฐานสงคราม พิพิธภัณฑ์ศิลปกรรม และพิพิธภัณฑ์ประวัติศาสตร์.',
                    'พระราชวังอิสรภาพ มีห้องรับรองและส่วนจัดแสดงในอาคาร.',
                    'ที่ทำการไปรษณีย์กลางและโบสถ์ใหญ่อยู่ในย่านกลางเดียวกัน.',
                    'ตลาดเบ๊นถั่ญเป็นตลาดมีหลังคา มีอาหารและของชิ้นเล็ก.',
                    'วัดพระหยก: ถอดรองเท้าและแต่งกายสุภาพ เช่นเดียวกับวัดหลายแห่ง.',
                    'การแสดงหุ่นกระบอกน้ำจัดในอาคาร.',
                    'ร้านกาแฟและร้านที่มีเครื่องปรับอากาศใช้ได้เมื่อฝนเริ่มตก.']),
                 S('วิธีจัดวัน', 'เลือกพิพิธภัณฑ์หนึ่งแห่งหรือพระราชวัง เก็บตลาดมีหลังคาหรือร้านกาแฟไว้ช่วงฝนหนักที่สุด ถนนคนเดินเหงียนเว้ไว้ท้ายวันหากฝนเบาลง โบสถ์ ที่ทำการไปรษณีย์ และถนนคนเดินอยู่ในย่านกลางเดียวกัน เวลาเปิดเปลี่ยนได้ จึงควรตรวจที่จุดนั้น.')]),
            'guide-note-day': page(
                'ไซง่อนหนึ่งวันในย่านกลาง',
                'หนึ่งวันในไซง่อนพอสำหรับย่านกลาง: โบสถ์ใหญ่ ที่ทำการไปรษณีย์ ถนนหนังสือ ถนนคนเดิน และตลาดเบ๊นถั่ญ บวกพิพิธภัณฑ์หนึ่งแห่งหรือพระราชวัง เวลาเปิดตรวจที่จุด.',
                'ไซง่อนในหนึ่งวัน',
                'หนึ่งวันในโฮจิมินห์พอสำหรับย่านกลาง หนึ่งวันไม่พอสำหรับทุกพิพิธภัณฑ์และทุกย่าน.',
                [S('วนย่านกลาง', 'โบสถ์ใหญ่ ที่ทำการไปรษณีย์กลาง ถนนหนังสือเหงียนวันบิ่ญ และถนนคนเดินเหงียนเว้อยู่ในย่านกลางเดียวกัน จึงมีคนเดินระหว่างจุดเหล่านี้ ตลาดเบ๊นถั่ญเป็นจุดแวะกินหรือดูแผงที่พบบ่อย เพิ่มพระราชวังหรือพิพิธภัณฑ์หนึ่งแห่ง ไม่ใช่ทุกจุดในวันเดียวกัน.'),
                 S('การย้ายระหว่างจุด', ul=[
                    'ในย่านกลาง หลายจุดอยู่ใกล้กันพอที่จะเดิน.',
                    'รถโดยสารประจำทางและรถไฟฟ้าที่ออกจากย่านตลาดเบ๊นถั่ญใช้กับระยะที่ไกลกว่า.',
                    'แท็กซี่และรถที่เรียกผ่านแอปพบบ่อย ขอให้เปิดมิเตอร์ หรือยืนยันเที่ยวในแอปก่อนออก.',
                    'รถจักรยานยนต์เป็นส่วนหนึ่งของการจราจร ข้ามถนนตามจังหวะคนเดิน อย่าหยุดกลางกระแสรถ.']),
                 S('เก็บไว้อีกวัน', 'สวนสัตว์ วัดหนึ่งแห่ง พิพิธภัณฑ์แห่งที่สอง หรือที่นอกเมืองเช่นอุโมงค์กู๋จี ต้องการวันแยก ในวันที่ย่านกลาง มื้อริมทางหนึ่งมื้อและกาแฟหนึ่งแก้วพอ เฝอ บั่ญหมี่ หรือข้าวแตกหาได้ไม่ยาก กาแฟเย็นใส่นมข้นเป็นแบบท้องถิ่นที่พบบ่อย.')]),
            'guide-note-group': page(
                'ไซง่อนกับครอบครัวหรือกลุ่ม',
                'ไซง่อนกับเด็กหรือกลุ่มลงตัวกว่าเมื่อวันมีจุดกลางแจ้งหนึ่งจุดและจุดในร่มหนึ่งจุด: สวนสัตว์ หุ่นกระบอกน้ำ พิพิธภัณฑ์หนึ่งแห่ง และมื้ออาหารร่วมกัน.',
                'ไซง่อนกับครอบครัวหรือกลุ่มเพื่อน',
                'โฮจิมินห์เหมาะกับครอบครัวและกลุ่ม ถ้าวันนั้นแบ่งเป็นจุดกลางแจ้งหนึ่งจุดและจุดในร่มหนึ่งจุด.',
                [S('เมื่อไปกับเด็ก', ul=[
                    'สวนสัตว์และสวนพฤกษศาสตร์ไซง่อนเป็นสวนสาธารณะเก่าของเมือง มีทางเดินร่มไม้.',
                    'หุ่นกระบอกน้ำดูในอาคาร และติดตามได้โดยไม่ต้องมีบทพูดมาก.',
                    'ตลาดมีหลังคาคับคั่ง จับมือเด็กใกล้ถนนและระหว่างแผง.',
                    'กลางวันมักร้อน เช้าและบ่ายแก่เหมาะกับข้างนอก กลางวันเหมาะกับพิพิธภัณฑ์ ร้านกาแฟ หรือการพัก.',
                    'ดื่มน้ำขวดหรือน้ำที่กรองแล้ว.',
                    'ที่วัดและโบสถ์ควรแต่งกายสุภาพ ที่วัดมักถอดรองเท้า.']),
                 S('เมื่อไปเป็นกลุ่ม', 'กลุ่มสั่งอาหารจานเล็กหลายจานที่แผง หรือหลายที่ร้านเฝอหรือข้าวแตกได้ ถนนคนเดินเหงียนเว้และลานหน้าโรงละครเป็นจุดนัดตอนเย็นที่หาไม่ยาก เลือกพิพิธภัณฑ์หนึ่งแห่งหรือพระราชวังเพื่ออยู่ด้วยกัน และเหลือเวลาที่ไม่ได้จัดตาราง แทนการยัดทุกจุดในวันเดียว.'),
                 S('หมายเหตุสำหรับทุกคน', ul=[
                    'รถจักรยานยนต์หนาแน่น ข้ามไปกับคนอื่น ด้วยจังหวะสม่ำเสมอ.',
                    'แผงเล็กมักรับเงินสด บางแห่งมีคิวอาร์โค้ดสำหรับโอนเงิน.',
                    'ราวเดือนพฤษภาคมถึงพฤศจิกายน ควรมีรายชื่อที่ในร่มติดมือ.'])]),
            'guide-note-food': page(
                'อาหารริมทางในไซง่อน',
                'อาหารริมทางในไซง่อนมีตั้งแต่เช้าถึงค่ำ: เฝอ บั่ญหมี่ ข้าวแตก บั่ญแส่ว และกาแฟนม เลือกแผงที่เห็นเขาทำต่อหน้า แผงที่มีคนเยอะคือทางเลือกที่พบบ่อยในเมือง.',
                'อาหารริมทางในไซง่อน',
                'ครัวบนทางเท้าเป็นวิธีกินธรรมดาในโฮจิมินห์ ตั้งแต่เช้าจนดึก.',
                [S('อาหารที่พบบ่อย', ul=[
                    'เฝอ: ก๋วยเตี๋ยวน้ำซุปเส้นข้าว มักมีเนื้อวัวหรือไก่.',
                    'บั่ญหมี่: ขนมปังกับเนื้อ ของดอง สมุนไพร และพริก.',
                    'ข้าวแตก: ข้าวหักกับซี่โครงย่าง ไข่ และกับข้าว.',
                    'หูเตียวและก๋วยเตี๋ยวน้ำใสแบบอื่น.',
                    'บั่ญแส่ว: แพนเค้กเค็มกรอบ กินกับสมุนไพร.',
                    'ก๋อยกวน: ปอเปี๊ยะสดกับสมุนไพร.',
                    'เช่: ของหวานแบบซุป.',
                    'กาแฟนมเย็นคือกาแฟเย็นใส่นมข้น บักเสี่ยวมีนมมากกว่า.']),
                 S('ที่แผงลอย', 'แผงวางเก้าอี้เตี้ยบนทางเท้า แผงที่มีคนเยอะและอาหารออกเร็วเป็นทางเลือกที่พบบ่อย ดูอาหารที่ทำให้ต่อหน้า หากอยากเผ็ดน้อยกว่านั้น บอกตอนสั่ง อาหารมังสวิรัติมักเขียนว่า chay.'),
                 S('นิสัยที่มีประโยชน์', ul=[
                    'เช้าเป็นช่วงอาหารริมทางสำคัญ โดยเฉพาะเฝอและบั่ญหมี่ ตอนเย็นมีปิ้งย่างและหอยมากขึ้น.',
                    'ตลาดเบ๊นถั่ญและถนนในชุมชนหลายสายมีทั้งที่นั่งและแบบห่อกลับ.',
                    'แผงเล็กมักรับเงินสด บางแห่งมีคิวอาร์โค้ดสำหรับโอน.',
                    'เลือกอาหารที่ทำให้ต่อหน้าและเสิร์ฟร้อน ดื่มน้ำขวดหรือน้ำที่กรองแล้ว.',
                    'ไม่จำเป็นต้องไล่ชื่อดัง แผงธรรมดาที่มีคนเยอะคือรูปแบบของเมือง.'])]),
        },
    )

def hi(DATA, page, S, L):
    g, tg = 'साइगॉन यात्रा गाइड', 'ठहरने वालों के लिए जगहों की गाइड'
    home = 'घर का परिचय <a href="{L}">होम पेज</a> पर है।'
    fam, fam_mid = 'परिवार के साथ यात्रा के सुझाव', ' और '
    kw = dict(fam=fam, fam_mid=fam_mid)
    DATA['hi'] = dict(
        btn='बुकिंग और संपर्क',
        book='हो ची मिन्ह शहर में ठहरना हो, तो बुकिंग और संपर्क पेज बताता है कि घर कैसे बुक करें।',
        more_h2='इसी साइट के और पन्ने',
        hub_h2='साइगॉन के एक दिन के चार विषय',
        hub_p='चार पन्ने बारिश, केंद्र में एक दिन, परिवार या समूह के साथ निकलने, और सड़क के खाने पर हैं।',
        cards=[
            ['बारिश में साइगॉन', 'guide-note-rain', 'बारिश में संग्रहालय, ढका बाज़ार और कैफ़े।'],
            ['साइगॉन एक दिन में', 'guide-note-day', 'केंद्र का एक चक्कर, सब कुछ देखने की कोशिश के बिना।'],
            ['परिवार या समूह के साथ साइगॉन', 'guide-note-group', 'चिड़ियाघर, जल कठपुतली और साझा खाना।'],
            ['साइगॉन का स्ट्रीट फ़ूड', 'guide-note-food', 'फ़ो, बान मी, टूटा चावल, और ठेला चुनना।'],
        ],
        links={
            'rain': L('बारिश वाले दिन को बाकी यात्रा से जोड़ने के लिए देखें ', g, ', ', tg, home, **kw),
            'day': L('केंद्र के एक दिन को और विचारों से जोड़ने के लिए देखें ', g, ', ', tg, home, **kw),
            'group': L('परिवार या समूह के साथ जाते समय देखें ', g, ', ', tg, home, **kw),
            'food': L('खाने और चलने की और जगहें चाहिए हों तो देखें ', g, ', ', tg, home, **kw),
        },
        pages={
            'guide-note-rain': page(
                'बारिश में साइगॉन: अंदर की योजना',
                'हो ची मिन्ह में मई से नवंबर तक तेज़ बौछारें आम हैं। संग्रहालय, महल, डाकघर, ढका बाज़ार और कैफ़े दिन को सूखी जगह में आगे बढ़ाते हैं। समय वहीं जाँचें।',
                'बारिश वाले दिन साइगॉन',
                'बारिश हो ची मिन्ह के पूरे दिन को रद्द नहीं करती। संग्रहालय, ढका बाज़ार और कैफ़े अंदर का आम प्लान हैं।',
                [S('बारिश वाले महीने', 'हो ची मिन्ह की जलवायु उष्णकटिबंधीय है। तेज़ बौछारें लगभग मई से नवंबर तक आम हैं, और सूखा मौसम दिसंबर से अप्रैल में ज़्यादा दिखता है। भारी बारिश के बाद निचली जगहों पर पानी थोड़ी देर रुककर बह सकता है। नम महीनों में दिन में एक ढकी हुई जगह रखें।'),
                 S('अंदर या छत वाली जगहें', ul=[
                    'युद्ध अवशेष संग्रहालय, ललित कला संग्रहालय और इतिहास संग्रहालय।',
                    'स्वतंत्रता महल, स्वागत कक्ष और अंदर की प्रदर्शनी के साथ।',
                    'केंद्रीय डाकघर और गिरजाघर एक ही केंद्रीय इलाके में हैं।',
                    'बेन थान्ह बाज़ार ढका बाज़ार है, खाने और छोटी चीज़ों के साथ।',
                    'जेड एम्परर पगोडा: जूते उतारें और सादा لباس पहनें, जैसे कई पगोडा में होता है।',
                    'जल कठपुतली का प्रदर्शन एक हॉल में होता है।',
                    'बौछार शुरू हो तो कैफ़े और एयर-कंडीशन वाली दुकानें काम आती हैं।']),
                 S('दिन कैसे सजाएँ', 'एक संग्रहालय या महल चुनें। सबसे भारी बारिश के लिए ढका बाज़ार या कैफ़े रखें। बारिश हल्की हो तो न्गुयेन ह्वे पैदल सड़क दिन के अंत में रह सकती है। गिरजाघर, डाकघर और पैदल सड़क एक ही केंद्रीय इलाके में हैं। खुलने का समय बदलता है, जगह पर जाँच लें।')]),
            'guide-note-day': page(
                'साइगॉन एक दिन में, सिर्फ़ केंद्र',
                'साइगॉन का एक दिन केंद्र के लिए काफी है: गिरजाघर, डाकघर, किताबों की सड़क, पैदल सड़क और बेन थान्ह बाज़ार, साथ एक संग्रहालय या महल। खुलने का समय वहीं देखें।',
                'साइगॉन एक दिन में',
                'हो ची मिन्ह में एक दिन केंद्र के लिए काफी है। एक दिन हर संग्रहालय और हर इलाके के लिए काफी नहीं।',
                [S('केंद्र का चक्कर', 'गिरजाघर, केंद्रीय डाकघर, न्गुयेन वान बिन्ह पुस्तक सड़क और न्गुयेन ह्वे पैदल सड़क एक ही केंद्रीय इलाके में हैं, इसलिए कई लोग इनके बीच पैदल चलते हैं। बेन थान्ह बाज़ार खाने या ठेले देखने का आम पड़ाव है। उसी दिन महल या एक संग्रहालय जोड़ें, बाकी हर जगह नहीं।'),
                 S('जगहों के बीच', ul=[
                    'केंद्र में इनमें से कई जगहें पैदल जाने लायक पास हैं।',
                    'शहर की बसें और बेन थान्ह इलाके से चलने वाली मेट्रो लंबी दूरी के लिए हैं।',
                    'टैक्सी और ऐप से बुलाई गाड़ियाँ बहुत आम हैं। मीटर लगवाएँ, या निकलने से पहले ऐप में यात्रा की पुष्टि करें।',
                    'मोटरबाइक यातायात का हिस्सा हैं। पैदल चलने वालों की लय में सड़क पार करें, बीच में न रुकें।']),
                 S('किसी और दिन के लिए', 'चिड़ियाघर, एक पगोडा, दूसरा संग्रहालय, या शहर के बाहर की जगह जैसे कू ची सुरंगें, अलग दिन माँगती हैं। केंद्र वाले दिन में एक स्ट्रीट मील और एक कॉफ़ी काफी है। फ़ो, बान मी या टूटा चावल आसानी से मिलते हैं। कंडेंस्ड मिल्क वाली आइस कॉफ़ी स्थानीय रूप में सबसे आम है।')]),
            'guide-note-group': page(
                'परिवार या समूह के साथ साइगॉन',
                'बच्चों या समूह के साथ साइगॉन तब आसान है जब दिन में एक खुली जगह और एक अंदर की जगह हो: चिड़ियाघर, जल कठपुतली, एक संग्रहालय और साथ का खाना। दोपहर गर्म है।',
                'परिवार या समूह के साथ साइगॉन',
                'हो ची मिन्ह परिवार और समूह दोनों के लिए ठीक है, अगर दिन एक खुली जगह और एक ढकी जगह में बँटा हो।',
                [S('बच्चों के साथ', ul=[
                    'साइगॉन का चिड़ियाघर और वनस्पति उद्यान शहर का पुराना पार्क है, छायादार रास्तों के साथ।',
                    'जल कठपुतली एक हॉल में दिखती है और बिना बहुत संवाद के समझ आती है।',
                    'ढके बाज़ार भीड़ वाले होते हैं। सड़क के पास और ठेलों के बीच बच्चों का हाथ पकड़ें।',
                    'दोपहर अक्सर गर्म होती है। सुबह और देर दोपहर बाहर के लिए ठीक हैं। दोपहर संग्रहालय, कैफ़े या आराम के लिए ठीक है।',
                    'बोतल का या छना पानी पिएँ।',
                    'पगोडा और गिरजाघर में सादा कपड़ा उचित है। पगोडा में आमतौर पर जूते उतारते हैं।']),
                 S('समूह के साथ', 'समूह ठेले पर कई छोटी प्लेटें मँगवा सकता है, या फ़ो या टूटे चावल की दुकान पर कुछ हिस्से। न्गुयेन ह्वे पैदल सड़क और ऑपेरा के सामने की जगह शाम को मिलने के आसान बिंदु हैं। साथ रहने के लिए एक संग्रहालय या महल चुनें, और हर जगह को एक दिन में ठूँसने के बजाय बिना समय-सारणी का समय छोड़ें।'),
                 S('सबके लिए नोट', ul=[
                    'मोटरबाइक का यातायात घना है। दूसरों के साथ, समान गति से सड़क पार करें।',
                    'छोटे ठेले आमतौर पर नकद लेते हैं। कुछ पर ट्रांसफ़र के लिए क्यूआर कोड भी होता है।',
                    'मई से नवंबर तक अंदर की जगहों की सूची पास रखें।'])]),
            'guide-note-food': page(
                'साइगॉन का सड़क का खाना',
                'साइगॉन का सड़क का खाना नाश्ते से रात तक चलता है: फ़ो, बान मी, टूटा चावल, बान सेओ और दूध वाली कॉफ़ी। वह ठेला चुनें जहाँ आपके सामने पकाया जाए।',
                'साइगॉन में सड़क का खाना',
                'फुटपाथ पर पकाना हो ची मिन्ह में नाश्ते से देर रात तक खाने का आम तरीका है।',
                [S('जो व्यंजन अक्सर मिलते हैं', ul=[
                    'फ़ो: चावल की नूडल का सूप, अक्सर गाय या मुर्गे के साथ।',
                    'बान मी: बैगेट, मांस, अचार, जड़ी-बूटी और मिर्च के साथ।',
                    'टूटा चावल: ग्रिल की पसली, अंडा और साथ के व्यंजनों के साथ।',
                    'हू तिएउ और दूसरे साफ़ शोरबे वाले नूडल सूप।',
                    'बान सेओ: कुरकुरी नमकीन पैनकेक, जड़ी-बूटी के साथ।',
                    'गोई कुओन: जड़ी-बूटी वाले ताज़े रोल।',
                    'चे: मीठे सूप जैसे डेज़र्ट।',
                    'का फे सूआ दा कंडेंस्ड मिल्क वाली आइस कॉफ़ी है। बक सिउ में दूध ज़्यादा होता है।']),
                 S('ठेले पर', 'ठेला फुटपाथ पर नीची स्टूल रखता है। भीड़ वाला ठेला, जहाँ प्लेटें जल्दी आएँ, आम चुनाव है। देखें कि खाना आपके सामने पक रहा है। कम मिर्च चाहिए तो ऑर्डर करते समय कहें। शाकाहारी खाने पर अक्सर chay लिखा होता है।'),
                 S('काम आने वाली आदतें', ul=[
                    'नाश्ता सड़क के खाने का बड़ा समय है, खासकर फ़ो और बान मी। शाम को ग्रिल और घोंघे बढ़ते हैं।',
                    'बेन थान्ह बाज़ार और कई मोहल्ले की सड़कों पर बैठने और ले जाने दोनों हैं।',
                    'छोटे ठेले अक्सर नकद चाहते हैं। कुछ पर ट्रांसफ़र के लिए क्यूआर कोड होता है।',
                    'वह खाना चुनें जो सामने पके और गर्म परोसा जाए। बोतल का या छना पानी पिएँ।',
                    'किसी मशहूर नाम के पीछे भागना ज़रूरी नहीं। साधारण भीड़ वाला ठेला इस शहर का तरीका है।'])]),
        },
    )

def pa(DATA, page, S, L):
    g, tg = 'ਸਾਈਗਾਨ ਯਾਤਰਾ ਗਾਈਡ', 'ਠਹਿਰਨ ਵਾਲਿਆਂ ਲਈ ਥਾਵਾਂ ਦੀ ਗਾਈਡ'
    home = 'ਘਰ ਦੀ ਜਾਣ-ਪਛਾਣ <a href="{L}">ਹੋਮ ਸਫ਼ੇ</a> ਉੱਤੇ ਹੈ।'
    fam, fam_mid = 'ਪਰਿਵਾਰ ਨਾਲ ਯਾਤਰਾ ਦੇ ਸੁਝਾਅ', ' ਅਤੇ '
    kw = dict(fam=fam, fam_mid=fam_mid)
    DATA['pa'] = dict(
        btn='ਬੁਕਿੰਗ ਅਤੇ ਸੰਪਰਕ',
        book='ਜੇ ਤੁਸੀਂ ਹੋ ਚੀ ਮਿਨ੍ਹ ਵਿੱਚ ਰੁਕਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਬੁਕਿੰਗ ਅਤੇ ਸੰਪਰਕ ਸਫ਼ਾ ਦੱਸਦਾ ਹੈ ਕਿ ਘਰ ਕਿਵੇਂ ਬੁੱਕ ਕਰਨਾ ਹੈ।',
        more_h2='ਇਸ ਸਾਈਟ ਦੇ ਹੋਰ ਸਫ਼ੇ',
        hub_h2='ਸਾਈਗਾਨ ਦੇ ਇੱਕ ਦਿਨ ਲਈ ਚਾਰ ਵਿਸ਼ੇ',
        hub_p='ਚਾਰ ਸਫ਼ੇ ਮੀਂਹ, ਕੇਂਦਰ ਵਿੱਚ ਇੱਕ ਦਿਨ, ਪਰਿਵਾਰ ਜਾਂ ਟੋਲੀ ਨਾਲ ਜਾਣ, ਅਤੇ ਸੜਕ ਦੇ ਖਾਣੇ ਬਾਰੇ ਹਨ।',
        cards=[
            ['ਮੀਂਹ ਵਿੱਚ ਸਾਈਗਾਨ', 'guide-note-rain', 'ਮੀਂਹ ਵੇਲੇ ਅਜਾਇਬ ਘਰ, ਛੱਤ ਵਾਲਾ ਬਾਜ਼ਾਰ ਅਤੇ ਕੈਫ਼ੇ।'],
            ['ਸਾਈਗਾਨ ਇੱਕ ਦਿਨ ਵਿੱਚ', 'guide-note-day', 'ਕੇਂਦਰ ਦਾ ਇੱਕ ਚੱਕਰ, ਸਭ ਕੁਝ ਵੇਖਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਬਿਨਾਂ।'],
            ['ਪਰਿਵਾਰ ਜਾਂ ਟੋਲੀ ਨਾਲ ਸਾਈਗਾਨ', 'guide-note-group', 'ਚਿੜੀਆਘਰ, ਪਾਣੀ ਦੀਆਂ ਕਠਪੁਤਲੀਆਂ ਅਤੇ ਸਾਂਝਾ ਖਾਣਾ।'],
            ['ਸਾਈਗਾਨ ਦਾ ਗਲੀ ਖਾਣਾ', 'guide-note-food', 'ਫ਼ੋ, ਬਾਨ ਮੀ, ਟੁੱਟਿਆ ਚਾਵਲ, ਅਤੇ ਠੇਲਾ ਚੁਣਨਾ।'],
        ],
        links={
            'rain': L('ਮੀਂਹ ਵਾਲੇ ਦਿਨ ਨੂੰ ਬਾਕੀ ਯਾਤਰਾ ਨਾਲ ਜੋੜਨ ਲਈ ਵੇਖੋ ', g, ', ', tg, home, **kw),
            'day': L('ਕੇਂਦਰ ਦੇ ਇੱਕ ਦਿਨ ਨੂੰ ਹੋਰ ਵਿਚਾਰਾਂ ਨਾਲ ਜੋੜਨ ਲਈ ਵੇਖੋ ', g, ', ', tg, home, **kw),
            'group': L('ਪਰਿਵਾਰ ਜਾਂ ਟੋਲੀ ਨਾਲ ਜਾਂਦੇ ਸਮੇਂ ਵੇਖੋ ', g, ', ', tg, home, **kw),
            'food': L('ਖਾਣ ਅਤੇ ਤੁਰਨ ਦੀਆਂ ਹੋਰ ਥਾਵਾਂ ਚਾਹੀਦੀਆਂ ਹੋਣ ਤਾਂ ਵੇਖੋ ', g, ', ', tg, home, **kw),
        },
        pages={
            'guide-note-rain': page(
                'ਮੀਂਹ ਵਿੱਚ ਸਾਈਗਾਨ: ਅੰਦਰ ਦੀ ਯੋਜਨਾ',
                'ਹੋ ਚੀ ਮਿਨ੍ਹ ਵਿੱਚ ਮਈ ਤੋਂ ਨਵੰਬਰ ਤੱਕ ਤੇਜ਼ ਵਾਛੜ ਆਮ ਹਨ। ਅਜਾਇਬ ਘਰ, ਮਹਿਲ, ਡਾਕਘਰ, ਛੱਤ ਵਾਲਾ ਬਾਜ਼ਾਰ ਅਤੇ ਕੈਫ਼ੇ ਦਿਨ ਨੂੰ ਸੁੱਕੀ ਥਾਂ ਵਿੱਚ ਅੱਗੇ ਵਧਾਉਂਦੇ ਹਨ। ਸਮਾਂ ਉੱਥੇ ਵੇਖੋ।',
                'ਮੀਂਹ ਵਾਲੇ ਦਿਨ ਸਾਈਗਾਨ',
                'ਮੀਂਹ ਹੋ ਚੀ ਮਿਨ੍ਹ ਦਾ ਸਾਰਾ ਦਿਨ ਰੱਦ ਨਹੀਂ ਕਰਦਾ। ਅਜਾਇਬ ਘਰ, ਛੱਤ ਵਾਲਾ ਬਾਜ਼ਾਰ ਅਤੇ ਕੈਫ਼ੇ ਅੰਦਰ ਦੀ ਆਮ ਯੋਜਨਾ ਹਨ।',
                [S('ਮੀਂਹ ਵਾਲੇ ਮਹੀਨੇ', 'ਹੋ ਚੀ ਮਿਨ੍ਹ ਦਾ ਮੌਸਮ ਗਰਮ ਖੰਡੀ ਹੈ। ਤੇਜ਼ ਵਾਛੜ ਲਗਭਗ ਮਈ ਤੋਂ ਨਵੰਬਰ ਤੱਕ ਆਮ ਹਨ, ਅਤੇ ਸੁੱਕਾ ਮੌਸਮ ਦਸੰਬਰ ਤੋਂ ਅਪ੍ਰੈਲ ਵਿੱਚ ਵਧੇਰੇ ਦਿਖਦਾ ਹੈ। ਭਾਰੀ ਮੀਂਹ ਮਗਰੋਂ ਨੀਵੀਆਂ ਥਾਵਾਂ ਉੱਤੇ ਪਾਣੀ ਥੋੜ੍ਹੀ ਦੇਰ ਰੁਕ ਕੇ ਵਹਿ ਸਕਦਾ ਹੈ। ਨਮ ਮਹੀਨਿਆਂ ਵਿੱਚ ਦਿਨ ਵਿੱਚ ਇੱਕ ਛੱਤ ਵਾਲੀ ਥਾਂ ਰੱਖੋ।'),
                 S('ਅੰਦਰ ਜਾਂ ਛੱਤ ਵਾਲੀਆਂ ਥਾਵਾਂ', ul=[
                    'ਜੰਗੀ ਅਵਸ਼ੇਸ਼ ਅਜਾਇਬ ਘਰ, ਲਲਿਤ ਕਲਾ ਅਜਾਇਬ ਘਰ ਅਤੇ ਇਤਿਹਾਸ ਅਜਾਇਬ ਘਰ।',
                    'ਆਜ਼ਾਦੀ ਮਹਿਲ, ਸਵਾਗਤ ਕਮਰਿਆਂ ਅਤੇ ਅੰਦਰ ਦੀ ਪ੍ਰਦਰਸ਼ਨੀ ਨਾਲ।',
                    'ਕੇਂਦਰੀ ਡਾਕਘਰ ਅਤੇ ਗਿਰਜਾਘਰ ਇੱਕੋ ਕੇਂਦਰੀ ਇਲਾਕੇ ਵਿੱਚ ਹਨ।',
                    'ਬੇਨ ਥਾਨ੍ਹ ਬਾਜ਼ਾਰ ਛੱਤ ਵਾਲਾ ਬਾਜ਼ਾਰ ਹੈ, ਖਾਣੇ ਅਤੇ ਛੋਟੀਆਂ ਚੀਜ਼ਾਂ ਨਾਲ।',
                    'ਜੇਡ ਸਮਰਾਟ ਪਗੋਡਾ: ਜੁੱਤੀਆਂ ਲਾਹੋ ਅਤੇ ਸਾਦਾ ਕੱਪੜਾ ਪਾਓ, ਜਿਵੇਂ ਕਈ ਪਗੋਡਿਆਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।',
                    'ਪਾਣੀ ਦੀਆਂ ਕਠਪੁਤਲੀਆਂ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਇੱਕ ਹਾਲ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।',
                    'ਵਾਛੜ ਸ਼ੁਰੂ ਹੋਵੇ ਤਾਂ ਕੈਫ਼ੇ ਅਤੇ ਠੰਡੀ ਹਵਾ ਵਾਲੀਆਂ ਦੁਕਾਨਾਂ ਕੰਮ ਆਉਂਦੀਆਂ ਹਨ।']),
                 S('ਦਿਨ ਕਿਵੇਂ ਸਜਾਈਏ', 'ਇੱਕ ਅਜਾਇਬ ਘਰ ਜਾਂ ਮਹਿਲ ਚੁਣੋ। ਸਭ ਤੋਂ ਭਾਰੀ ਮੀਂਹ ਲਈ ਛੱਤ ਵਾਲਾ ਬਾਜ਼ਾਰ ਜਾਂ ਕੈਫ਼ੇ ਰੱਖੋ। ਮੀਂਹ ਹੌਲਾ ਹੋਵੇ ਤਾਂ ਨਗੁਏਨ ਹੁਏ ਪੈਦਲ ਗਲੀ ਦਿਨ ਦੇ ਅੰਤ ਵਿੱਚ ਰਹਿ ਸਕਦੀ ਹੈ। ਗਿਰਜਾਘਰ, ਡਾਕਘਰ ਅਤੇ ਪੈਦਲ ਗਲੀ ਇੱਕੋ ਕੇਂਦਰੀ ਇਲਾਕੇ ਵਿੱਚ ਹਨ। ਖੁੱਲ੍ਹਣ ਦਾ ਸਮਾਂ ਬਦਲਦਾ ਹੈ, ਥਾਂ ਉੱਤੇ ਜਾਂਚ ਲਵੋ।')]),
            'guide-note-day': page(
                'ਸਾਈਗਾਨ ਇੱਕ ਦਿਨ ਵਿੱਚ, ਸਿਰਫ਼ ਕੇਂਦਰ',
                'ਸਾਈਗਾਨ ਦਾ ਇੱਕ ਦਿਨ ਕੇਂਦਰ ਲਈ ਕਾਫ਼ੀ ਹੈ: ਗਿਰਜਾਘਰ, ਡਾਕਘਰ, ਕਿਤਾਬਾਂ ਦੀ ਗਲੀ, ਪੈਦਲ ਗਲੀ ਅਤੇ ਬੇਨ ਥਾਨ੍ਹ ਬਾਜ਼ਾਰ, ਨਾਲ ਇੱਕ ਅਜਾਇਬ ਘਰ ਜਾਂ ਮਹਿਲ। ਖੁੱਲ੍ਹਣ ਦਾ ਸਮਾਂ ਉੱਥੇ ਵੇਖੋ।',
                'ਸਾਈਗਾਨ ਇੱਕ ਦਿਨ ਵਿੱਚ',
                'ਹੋ ਚੀ ਮਿਨ੍ਹ ਵਿੱਚ ਇੱਕ ਦਿਨ ਕੇਂਦਰ ਲਈ ਕਾਫ਼ੀ ਹੈ। ਇੱਕ ਦਿਨ ਹਰ ਅਜਾਇਬ ਘਰ ਅਤੇ ਹਰ ਇਲਾਕੇ ਲਈ ਕਾਫ਼ੀ ਨਹੀਂ।',
                [S('ਕੇਂਦਰ ਦਾ ਚੱਕਰ', 'ਗਿਰਜਾਘਰ, ਕੇਂਦਰੀ ਡਾਕਘਰ, ਨਗੁਏਨ ਵਾਨ ਬਿਨ੍ਹ ਕਿਤਾਬ ਗਲੀ ਅਤੇ ਨਗੁਏਨ ਹੁਏ ਪੈਦਲ ਗਲੀ ਇੱਕੋ ਕੇਂਦਰੀ ਇਲਾਕੇ ਵਿੱਚ ਹਨ, ਇਸ ਲਈ ਕਈ ਲੋਕ ਇਨ੍ਹਾਂ ਵਿਚਕਾਰ ਪੈਦਲ ਤੁਰਦੇ ਹਨ। ਬੇਨ ਥਾਨ੍ਹ ਬਾਜ਼ਾਰ ਖਾਣ ਜਾਂ ਠੇਲੇ ਵੇਖਣ ਦਾ ਆਮ ਪੜਾਅ ਹੈ। ਉਸੇ ਦਿਨ ਮਹਿਲ ਜਾਂ ਇੱਕ ਅਜਾਇਬ ਘਰ ਜੋੜੋ, ਬਾਕੀ ਹਰ ਥਾਂ ਨਹੀਂ।'),
                 S('ਥਾਵਾਂ ਵਿਚਕਾਰ', ul=[
                    'ਕੇਂਦਰ ਵਿੱਚ ਇਨ੍ਹਾਂ ਵਿੱਚੋਂ ਕਈ ਥਾਵਾਂ ਪੈਦਲ ਜਾਣ ਜੋਗੀਆਂ ਨੇੜੇ ਹਨ।',
                    'ਸ਼ਹਿਰ ਦੀਆਂ ਬੱਸਾਂ ਅਤੇ ਬੇਨ ਥਾਨ੍ਹ ਇਲਾਕੇ ਤੋਂ ਚੱਲਣ ਵਾਲੀ ਮੈਟਰੋ ਲੰਮੀ ਦੂਰੀ ਲਈ ਹਨ।',
                    'ਟੈਕਸੀ ਅਤੇ ਐਪ ਤੋਂ ਬੁਲਾਈਆਂ ਗੱਡੀਆਂ ਬਹੁਤ ਆਮ ਹਨ। ਮੀਟਰ ਲਗਵਾਓ, ਜਾਂ ਨਿਕਲਣ ਤੋਂ ਪਹਿਲਾਂ ਐਪ ਵਿੱਚ ਯਾਤਰਾ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।',
                    'ਮੋਟਰਸਾਈਕਲ ਆਵਾਜਾਈ ਦਾ ਹਿੱਸਾ ਹਨ। ਪੈਦਲ ਚੱਲਣ ਵਾਲਿਆਂ ਦੀ ਲੈਅ ਵਿੱਚ ਸੜਕ ਪਾਰ ਕਰੋ, ਵਿਚਕਾਰ ਨਾ ਰੁਕੋ।']),
                 S('ਕਿਸੇ ਹੋਰ ਦਿਨ ਲਈ', 'ਚਿੜੀਆਘਰ, ਇੱਕ ਪਗੋਡਾ, ਦੂਜਾ ਅਜਾਇਬ ਘਰ, ਜਾਂ ਸ਼ਹਿਰ ਤੋਂ ਬਾਹਰ ਦੀ ਥਾਂ ਜਿਵੇਂ ਕੂ ਚੀ ਸੁਰੰਗਾਂ, ਵੱਖਰਾ ਦਿਨ ਮੰਗਦੀਆਂ ਹਨ। ਕੇਂਦਰ ਵਾਲੇ ਦਿਨ ਇੱਕ ਗਲੀ ਭੋਜਨ ਅਤੇ ਇੱਕ ਕੌਫ਼ੀ ਕਾਫ਼ੀ ਹੈ। ਫ਼ੋ, ਬਾਨ ਮੀ ਜਾਂ ਟੁੱਟਿਆ ਚਾਵਲ ਆਸਾਨੀ ਨਾਲ ਮਿਲਦੇ ਹਨ। ਕੰਡੈਂਸਡ ਦੁੱਧ ਵਾਲੀ ਆਈਸ ਕੌਫ਼ੀ ਸਥਾਨਕ ਰੂਪ ਵਿੱਚ ਸਭ ਤੋਂ ਆਮ ਹੈ।')]),
            'guide-note-group': page(
                'ਪਰਿਵਾਰ ਜਾਂ ਟੋਲੀ ਨਾਲ ਸਾਈਗਾਨ',
                'ਬੱਚਿਆਂ ਜਾਂ ਟੋਲੀ ਨਾਲ ਸਾਈਗਾਨ ਉਦੋਂ ਆਸਾਨ ਹੈ ਜਦੋਂ ਦਿਨ ਵਿੱਚ ਇੱਕ ਖੁੱਲ੍ਹੀ ਥਾਂ ਅਤੇ ਇੱਕ ਅੰਦਰ ਦੀ ਥਾਂ ਹੋਵੇ: ਚਿੜੀਆਘਰ, ਪਾਣੀ ਦੀਆਂ ਕਠਪੁਤਲੀਆਂ, ਇੱਕ ਅਜਾਇਬ ਘਰ ਅਤੇ ਸਾਂਝਾ ਖਾਣਾ।',
                'ਪਰਿਵਾਰ ਜਾਂ ਟੋਲੀ ਨਾਲ ਸਾਈਗਾਨ',
                'ਹੋ ਚੀ ਮਿਨ੍ਹ ਪਰਿਵਾਰ ਅਤੇ ਟੋਲੀ ਦੋਵਾਂ ਲਈ ਠੀਕ ਹੈ, ਜੇ ਦਿਨ ਇੱਕ ਖੁੱਲ੍ਹੀ ਥਾਂ ਅਤੇ ਇੱਕ ਛੱਤ ਵਾਲੀ ਥਾਂ ਵਿੱਚ ਵੰਡਿਆ ਹੋਵੇ।',
                [S('ਬੱਚਿਆਂ ਨਾਲ', ul=[
                    'ਸਾਈਗਾਨ ਦਾ ਚਿੜੀਆਘਰ ਅਤੇ ਬਨਸਪਤੀ ਉਦਿਆਨ ਸ਼ਹਿਰ ਦਾ ਪੁਰਾਣਾ ਪਾਰਕ ਹੈ, ਛਾਂ ਵਾਲੇ ਰਾਹਾਂ ਨਾਲ।',
                    'ਪਾਣੀ ਦੀਆਂ ਕਠਪੁਤਲੀਆਂ ਇੱਕ ਹਾਲ ਵਿੱਚ ਦਿਖਦੀਆਂ ਹਨ ਅਤੇ ਬਿਨਾਂ ਬਹੁਤ ਸੰਵਾਦ ਦੇ ਸਮਝ ਆਉਂਦੀਆਂ ਹਨ।',
                    'ਛੱਤ ਵਾਲੇ ਬਾਜ਼ਾਰ ਭੀੜ ਵਾਲੇ ਹੁੰਦੇ ਹਨ। ਸੜਕ ਕੋਲ ਅਤੇ ਠੇਲਿਆਂ ਵਿਚਕਾਰ ਬੱਚਿਆਂ ਦਾ ਹੱਥ ਫੜੋ।',
                    'ਦੁਪਹਿਰ ਅਕਸਰ ਗਰਮ ਹੁੰਦੀ ਹੈ। ਸਵੇਰ ਅਤੇ ਦੇਰ ਦੁਪਹਿਰ ਬਾਹਰ ਲਈ ਠੀਕ ਹਨ। ਦੁਪਹਿਰ ਅਜਾਇਬ ਘਰ, ਕੈਫ਼ੇ ਜਾਂ ਆਰਾਮ ਲਈ ਠੀਕ ਹੈ।',
                    'ਬੋਤਲ ਦਾ ਜਾਂ ਛਾਣਿਆ ਪਾਣੀ ਪੀਓ।',
                    'ਪਗੋਡਾ ਅਤੇ ਗਿਰਜਾਘਰ ਵਿੱਚ ਸਾਦਾ ਕੱਪੜਾ ਉਚਿਤ ਹੈ। ਪਗੋਡਾ ਵਿੱਚ ਆਮ ਤੌਰ ਉੱਤੇ ਜੁੱਤੀਆਂ ਲਾਹੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।']),
                 S('ਟੋਲੀ ਨਾਲ', 'ਟੋਲੀ ਠੇਲੇ ਉੱਤੇ ਕਈ ਛੋਟੀਆਂ ਪਲੇਟਾਂ ਮੰਗਵਾ ਸਕਦੀ ਹੈ, ਜਾਂ ਫ਼ੋ ਜਾਂ ਟੁੱਟੇ ਚਾਵਲ ਦੀ ਦੁਕਾਨ ਉੱਤੇ ਕੁਝ ਹਿੱਸੇ। ਨਗੁਏਨ ਹੁਏ ਪੈਦਲ ਗਲੀ ਅਤੇ ਓਪੇਰਾ ਦੇ ਸਾਹਮਣੇ ਦੀ ਥਾਂ ਸ਼ਾਮ ਨੂੰ ਮਿਲਣ ਦੇ ਆਸਾਨ ਬਿੰਦੂ ਹਨ। ਇਕੱਠੇ ਰਹਿਣ ਲਈ ਇੱਕ ਅਜਾਇਬ ਘਰ ਜਾਂ ਮਹਿਲ ਚੁਣੋ, ਅਤੇ ਹਰ ਥਾਂ ਨੂੰ ਇੱਕ ਦਿਨ ਵਿੱਚ ਠੂਸਣ ਦੀ ਥਾਂ ਬਿਨਾਂ ਸਮਾਂ-ਸਾਰਣੀ ਦਾ ਸਮਾਂ ਛੱਡੋ।'),
                 S('ਸਭ ਲਈ ਨੋਟ', ul=[
                    'ਮੋਟਰਸਾਈਕਲ ਦੀ ਆਵਾਜਾਈ ਸੰਘਣੀ ਹੈ। ਦੂਜਿਆਂ ਨਾਲ, ਇੱਕੋ ਗਤੀ ਨਾਲ ਸੜਕ ਪਾਰ ਕਰੋ।',
                    'ਛੋਟੇ ਠੇਲੇ ਆਮ ਤੌਰ ਉੱਤੇ ਨਕਦ ਲੈਂਦੇ ਹਨ। ਕੁਝ ਉੱਤੇ ਟ੍ਰਾਂਸਫ਼ਰ ਲਈ ਕਿਊਆਰ ਕੋਡ ਵੀ ਹੁੰਦਾ ਹੈ।',
                    'ਮਈ ਤੋਂ ਨਵੰਬਰ ਤੱਕ ਅੰਦਰ ਦੀਆਂ ਥਾਵਾਂ ਦੀ ਸੂਚੀ ਕੋਲ ਰੱਖੋ।'])]),
            'guide-note-food': page(
                'ਸਾਈਗਾਨ ਦਾ ਗਲੀ ਖਾਣਾ',
                'ਸਾਈਗਾਨ ਦਾ ਗਲੀ ਖਾਣਾ ਨਾਸ਼ਤੇ ਤੋਂ ਰਾਤ ਤੱਕ ਚੱਲਦਾ ਹੈ: ਫ਼ੋ, ਬਾਨ ਮੀ, ਟੁੱਟਿਆ ਚਾਵਲ, ਬਾਨ ਸੇਓ ਅਤੇ ਦੁੱਧ ਵਾਲੀ ਕੌਫ਼ੀ। ਉਹ ਠੇਲਾ ਚੁਣੋ ਜਿੱਥੇ ਤੁਹਾਡੇ ਸਾਹਮਣੇ ਪਕਾਇਆ ਜਾਵੇ।',
                'ਸਾਈਗਾਨ ਵਿੱਚ ਗਲੀ ਦਾ ਖਾਣਾ',
                'ਫੁੱਟਪਾਥ ਉੱਤੇ ਪਕਾਉਣਾ ਹੋ ਚੀ ਮਿਨ੍ਹ ਵਿੱਚ ਨਾਸ਼ਤੇ ਤੋਂ ਦੇਰ ਰਾਤ ਤੱਕ ਖਾਣ ਦਾ ਆਮ ਤਰੀਕਾ ਹੈ।',
                [S('ਜੋ ਪਕਵਾਨ ਅਕਸਰ ਮਿਲਦੇ ਹਨ', ul=[
                    'ਫ਼ੋ: ਚਾਵਲ ਦੀ ਨੂਡਲ ਦਾ ਸੂਪ, ਅਕਸਰ ਗਾਂ ਜਾਂ ਮੁਰਗੇ ਨਾਲ।',
                    'ਬਾਨ ਮੀ: ਬੈਗੇਟ, ਮੀਟ, ਅਚਾਰ, ਜੜੀ-ਬੂਟੀ ਅਤੇ ਮਿਰਚ ਨਾਲ।',
                    'ਟੁੱਟਿਆ ਚਾਵਲ: ਗ੍ਰਿੱਲ ਦੀ ਪਸਲੀ, ਆਂਡਾ ਅਤੇ ਨਾਲ ਦੇ ਪਕਵਾਨਾਂ ਨਾਲ।',
                    'ਹੂ ਤਿਏਉ ਅਤੇ ਹੋਰ ਸਾਫ਼ ਸ਼ੋਰਬੇ ਵਾਲੇ ਨੂਡਲ ਸੂਪ।',
                    'ਬਾਨ ਸੇਓ: ਕੁਰਕੁਰੀ ਨਮਕੀਨ ਪੈਨਕੇਕ, ਜੜੀ-ਬੂਟੀ ਨਾਲ।',
                    'ਗੋਈ ਕੁਓਨ: ਜੜੀ-ਬੂਟੀ ਵਾਲੇ ਤਾਜ਼ੇ ਰੋਲ।',
                    'ਚੇ: ਮਿੱਠੇ ਸੂਪ ਵਰਗੇ ਮਿਠਾਈ।',
                    'ਕਾ ਫ਼ੇ ਸੂਆ ਦਾ ਕੰਡੈਂਸਡ ਦੁੱਧ ਵਾਲੀ ਆਈਸ ਕੌਫ਼ੀ ਹੈ। ਬਕ ਸਿਉ ਵਿੱਚ ਦੁੱਧ ਵਧੇਰੇ ਹੁੰਦਾ ਹੈ।']),
                 S('ਠੇਲੇ ਉੱਤੇ', 'ਠੇਲਾ ਫੁੱਟਪਾਥ ਉੱਤੇ ਨੀਵੀਆਂ ਸਟੂਲ ਰੱਖਦਾ ਹੈ। ਭੀੜ ਵਾਲਾ ਠੇਲਾ, ਜਿੱਥੇ ਪਲੇਟਾਂ ਜਲਦੀ ਆਉਣ, ਆਮ ਚੋਣ ਹੈ। ਵੇਖੋ ਕਿ ਖਾਣਾ ਤੁਹਾਡੇ ਸਾਹਮਣੇ ਪੱਕ ਰਿਹਾ ਹੈ। ਘੱਟ ਮਿਰਚ ਚਾਹੀਦੀ ਹੋਵੇ ਤਾਂ ਆਰਡਰ ਕਰਦੇ ਸਮੇਂ ਕਹੋ। ਸ਼ਾਕਾਹਾਰੀ ਖਾਣੇ ਉੱਤੇ ਅਕਸਰ chay ਲਿਖਿਆ ਹੁੰਦਾ ਹੈ।'),
                 S('ਕੰਮ ਆਉਣ ਵਾਲੀਆਂ ਆਦਤਾਂ', ul=[
                    'ਨਾਸ਼ਤਾ ਗਲੀ ਦੇ ਖਾਣੇ ਦਾ ਵੱਡਾ ਸਮਾਂ ਹੈ, ਖ਼ਾਸਕਰ ਫ਼ੋ ਅਤੇ ਬਾਨ ਮੀ। ਸ਼ਾਮ ਨੂੰ ਗ੍ਰਿੱਲ ਅਤੇ ਘੋਗੇ ਵਧਦੇ ਹਨ।',
                    'ਬੇਨ ਥਾਨ੍ਹ ਬਾਜ਼ਾਰ ਅਤੇ ਕਈ ਮੁਹੱਲਿਆਂ ਦੀਆਂ ਗਲੀਆਂ ਉੱਤੇ ਬੈਠਣ ਅਤੇ ਲੈ ਜਾਣ ਦੋਵੇਂ ਹਨ।',
                    'ਛੋਟੇ ਠੇਲੇ ਅਕਸਰ ਨਕਦ ਚਾਹੁੰਦੇ ਹਨ। ਕੁਝ ਉੱਤੇ ਟ੍ਰਾਂਸਫ਼ਰ ਲਈ ਕਿਊਆਰ ਕੋਡ ਹੁੰਦਾ ਹੈ।',
                    'ਉਹ ਖਾਣਾ ਚੁਣੋ ਜੋ ਸਾਹਮਣੇ ਪੱਕੇ ਅਤੇ ਗਰਮ ਪਰੋਸਿਆ ਜਾਵੇ। ਬੋਤਲ ਦਾ ਜਾਂ ਛਾਣਿਆ ਪਾਣੀ ਪੀਓ।',
                    'ਕਿਸੇ ਮਸ਼ਹੂਰ ਨਾਮ ਦੇ ਪਿੱਛੇ ਭੱਜਣਾ ਜ਼ਰੂਰੀ ਨਹੀਂ। ਸਾਧਾਰਨ ਭੀੜ ਵਾਲਾ ਠੇਲਾ ਇਸ ਸ਼ਹਿਰ ਦਾ ਤਰੀਕਾ ਹੈ।'])]),
        },
    )

def ur(DATA, page, S, L):
    g, tg = 'سائگون سفری گائیڈ', 'ٹھہرنے والوں کے لیے جگہوں کی گائیڈ'
    home = 'گھر کا تعارف <a href="{L}">ہوم پیج</a> پر ہے۔'
    fam, fam_mid = 'فیملی کے ساتھ سفر کے مشورے', ' اور '
    kw = dict(fam=fam, fam_mid=fam_mid)
    DATA['ur'] = dict(
        btn='بکنگ اور رابطہ',
        book='اگر آپ ہو چی منہ میں ٹھہرنا چاہتے ہیں تو بکنگ اور رابطے کا صفحہ بتاتا ہے کہ گھر کیسے بک ہوتا ہے۔',
        more_h2='اسی سائٹ کے مزید صفحات',
        hub_h2='سائگون کے ایک دن کے چار موضوع',
        hub_p='چار صفحات بارش، مرکز میں ایک دن، فیملی یا گروہ کے ساتھ نکلنے، اور سڑک کے کھانے پر ہیں۔',
        cards=[
            ['بارش میں سائگون', 'guide-note-rain', 'بارش میں عجائب گھر، چھتا بازار اور کیفے۔'],
            ['سائگون ایک دن میں', 'guide-note-day', 'مرکز کا ایک چکر، سب کچھ دیکھنے کی کوشش کے بغیر۔'],
            ['فیملی یا گروہ کے ساتھ سائگون', 'guide-note-group', 'چڑیا گھر، پانی کی کٹھ پتلی اور مشترکہ کھانا۔'],
            ['سائگون کا سٹریٹ فوڈ', 'guide-note-food', 'فو، بان می، ٹوٹا چاول، اور ٹھیلہ چننا۔'],
        ],
        links={
            'rain': L('بارش والے دن کو باقی سفر سے جوڑنے کے لیے دیکھیں ', g, '، ', tg, home, **kw),
            'day': L('مرکز کے ایک دن کو مزید خیالات سے جوڑنے کے لیے دیکھیں ', g, '، ', tg, home, **kw),
            'group': L('فیملی یا گروہ کے ساتھ جاتے وقت دیکھیں ', g, '، ', tg, home, **kw),
            'food': L('کھانے اور چلنے کی مزید جگہیں چاہییں تو دیکھیں ', g, '، ', tg, home, **kw),
        },
        pages={
            'guide-note-rain': page(
                'بارش میں سائگون: اندر کی منصوبہ',
                'ہو چی منہ میں مئی سے نومبر تک تیز بارشیں عام ہیں۔ عجائب گھر، محل، ڈاک خانہ، چھتا بازار اور کیفے دن کو خشک جگہ میں آگے بڑھاتے ہیں۔ وقت وہیں جانچ لیں۔',
                'بارش والے دن سائگون',
                'بارش ہو چی منہ کے پورے دن کو منسوخ نہیں کرتی۔ عجائب گھر، چھتا بازار اور کیفے اندر کا عام منصوبہ ہیں۔',
                [S('بارش والے مہینے', 'ہو چی منہ کی آب و ہوا حارہ ہے۔ تیز بارشیں تقریباً مئی سے نومبر تک عام ہیں، اور خشک موسم دسمبر سے اپریل میں زیادہ نظر آتا ہے۔ بھاری بارش کے بعد نشیبی جگہوں پر پانی تھوڑی دیر رک کر بہہ سکتا ہے۔ نم مہینوں میں دن میں ایک چھتی جگہ رکھیں۔'),
                 S('اندر یا چھت والی جگہیں', ul=[
                    'جنگی آثار عجائب گھر، فنون لطیفہ عجائب گھر اور تاریخ عجائب گھر۔',
                    'آزادی محل، استقبال کے کمروں اور اندر کی نمائش کے ساتھ۔',
                    'مرکزی ڈاک خانہ اور گرجا ایک ہی مرکزی علاقے میں ہیں۔',
                    'بین تھانہ بازار چھتا بازار ہے، کھانے اور چھوٹی چیزوں کے ساتھ۔',
                    'جیڈ ایمپرر پگوڈا: جوتے اتاریں اور سادہ لباس پہنیں، جیسا کئی پگوڈا میں ہوتا ہے۔',
                    'پانی کی کٹھ پتلی کی پیشکش ایک ہال میں ہوتی ہے۔',
                    'بارش شروع ہو تو کیفے اور ٹھنڈی ہوا والی دکانیں کام آتی ہیں۔']),
                 S('دن کیسے سجائیں', 'ایک عجائب گھر یا محل چنیں۔ سب سے بھاری بارش کے لیے چھتا بازار یا کیفے رکھیں۔ بارش ہلکی ہو تو نگوین ہوئے پیدل گلی دن کے آخر میں رہ سکتی ہے۔ گرجا، ڈاک خانہ اور پیدل گلی ایک ہی مرکزی علاقے میں ہیں۔ کھلنے کا وقت بدلتا ہے، جگہ پر جانچ لیں۔')]),
            'guide-note-day': page(
                'سائگون ایک دن میں، صرف مرکز',
                'سائگون کا ایک دن مرکز کے لیے کافی ہے: گرجا، ڈاک خانہ، کتابوں کی گلی، پیدل گلی اور بین تھانہ بازار، ساتھ ایک عجائب گھر یا محل۔ کھلنے کا وقت وہیں دیکھیں۔',
                'سائگون ایک دن میں',
                'ہو چی منہ میں ایک دن مرکز کے لیے کافی ہے۔ ایک دن ہر عجائب گھر اور ہر علاقے کے لیے کافی نہیں۔',
                [S('مرکز کا چکر', 'گرجا، مرکزی ڈاک خانہ، نگوین وان بنہ کتاب گلی اور نگوین ہوئے پیدل گلی ایک ہی مرکزی علاقے میں ہیں، اس لیے کئی لوگ ان کے درمیان پیدل چلتے ہیں۔ بین تھانہ بازار کھانے یا ٹھیلے دیکھنے کا عام پڑاؤ ہے۔ اسی دن محل یا ایک عجائب گھر شامل کریں، باقی ہر جگہ نہیں۔'),
                 S('جگہوں کے درمیان', ul=[
                    'مرکز میں ان میں سے کئی جگہیں پیدل جانے کے قابل قریب ہیں۔',
                    'شہر کی بسیں اور بین تھانہ علاقے سے چلنے والی میٹرو لمبی دوری کے لیے ہیں۔',
                    'ٹیکسی اور ایپ سے بلائی گاڑیاں بہت عام ہیں۔ میٹر لگوائیں، یا نکلنے سے پہلے ایپ میں سفر کی تصدیق کریں۔',
                    'موٹر بائیک آمد و رفت کا حصہ ہیں۔ پیدل چلنے والوں کی لے میں سڑک پار کریں، بیچ میں نہ رکیں۔']),
                 S('کسی اور دن کے لیے', 'چڑیا گھر، ایک پگوڈا، دوسرا عجائب گھر، یا شہر سے باہر کی جگہ جیسے کو چی سرنگیں، الگ دن مانگتی ہیں۔ مرکز والے دن میں ایک سٹریٹ میل اور ایک کافی کافی ہے۔ فو، بان می یا ٹوٹا چاول آسانی سے ملتے ہیں۔ کنڈینسڈ دودھ والی آئس کافی مقامی شکل میں سب سے عام ہے۔')]),
            'guide-note-group': page(
                'فیملی یا گروہ کے ساتھ سائگون',
                'بچوں یا گروہ کے ساتھ سائگون تب آسان ہے جب دن میں ایک کھلی جگہ اور ایک اندر کی جگہ ہو: چڑیا گھر، پانی کی کٹھ پتلی، ایک عجائب گھر اور ساتھ کا کھانا۔',
                'فیملی یا گروہ کے ساتھ سائگون',
                'ہو چی منہ فیملی اور گروہ دونوں کے لیے ٹھیک ہے، اگر دن ایک کھلی جگہ اور ایک چھتی جگہ میں بٹا ہو۔',
                [S('بچوں کے ساتھ', ul=[
                    'سائگون کا چڑیا گھر اور نباتاتی باغ شہر کا پرانا پارک ہے، سایہ دار راستوں کے ساتھ۔',
                    'پانی کی کٹھ پتلی ایک ہال میں دکھتی ہے اور بغیر بہت مکالمے کے سمجھ آتی ہے۔',
                    'چھتے بازار بھیڑ والے ہوتے ہیں۔ سڑک کے پاس اور ٹھیلوں کے درمیان بچوں کا ہاتھ پکڑیں۔',
                    'دوپہر اکثر گرم ہوتی ہے۔ صبح اور دیر دوپہر باہر کے لیے ٹھیک ہیں۔ دوپہر عجائب گھر، کیفے یا آرام کے لیے ٹھیک ہے۔',
                    'بوتل کا یا چھنا پانی پیئیں۔',
                    'پگوڈا اور گرجا میں سادا کپڑا مناسب ہے۔ پگوڈا میں عموماً جوتے اتارتے ہیں۔']),
                 S('گروہ کے ساتھ', 'گروہ ٹھیلے پر کئی چھوٹی پلیٹیں منگوا سکتا ہے، یا فو یا ٹوٹے چاول کی دکان پر کچھ حصے۔ نگوین ہوئے پیدل گلی اور اوپیرا کے سامنے کی جگہ شام کو ملنے کے آسان نقطے ہیں۔ ساتھ رہنے کے لیے ایک عجائب گھر یا محل چنیں، اور ہر جگہ کو ایک دن میں ٹھونسنے کے بجائے بغیر وقت کے خانے کا وقت چھوڑیں۔'),
                 S('سب کے لیے نوٹ', ul=[
                    'موٹر بائیک کی آمد و رفت گھنی ہے۔ دوسروں کے ساتھ، یکساں رفتار سے سڑک پار کریں۔',
                    'چھوٹے ٹھیلے عموماً نقد لیتے ہیں۔ کچھ پر منتقلی کے لیے کیو آر کوڈ بھی ہوتا ہے۔',
                    'مئی سے نومبر تک اندر کی جگہوں کی فہرست پاس رکھیں۔'])]),
            'guide-note-food': page(
                'سائگون کا سڑک کا کھانا',
                'سائگون کا سڑک کا کھانا ناشتے سے رات تک چلتا ہے: فو، بان می، ٹوٹا چاول، بان سیو اور دودھ والی کافی۔ وہ ٹھیلہ چنیں جہاں آپ کے سامنے پکایا جائے۔',
                'سائگون میں سڑک کا کھانا',
                'فٹ پاتھ پر پکانا ہو چی منہ میں ناشتے سے دیر رات تک کھانے کا عام طریقہ ہے۔',
                [S('جو پکوان اکثر ملتے ہیں', ul=[
                    'فو: چاول کی نوڈل کا سوپ، اکثر گائے یا مرغی کے ساتھ۔',
                    'بان می: بیگٹ، گوشت، اچار، جڑی بوٹی اور مرچ کے ساتھ۔',
                    'ٹوٹا چاول: گرل کی پسلی، انڈا اور ساتھ کے پکوانوں کے ساتھ۔',
                    'ہو تیئو اور دوسرے صاف شوربے والے نوڈل سوپ۔',
                    'بان سیو: کرکری نمکین پین کیک، جڑی بوٹی کے ساتھ۔',
                    'گوئی کوون: جڑی بوٹی والے تازہ رول۔',
                    'چے: میٹھے سوپ جیسے میٹھے۔',
                    'کا فے سوائے دا کنڈینسڈ دودھ والی آئس کافی ہے۔ بک سیو میں دودھ زیادہ ہوتا ہے۔']),
                 S('ٹھیلے پر', 'ٹھیلہ فٹ پاتھ پر نیچی سٹول رکھتا ہے۔ بھیڑ والا ٹھیلہ، جہاں پلیٹیں جلدی آئیں، عام انتخاب ہے۔ دیکھیں کہ کھانا آپ کے سامنے پک رہا ہے۔ کم مرچ چاہیے تو آرڈر کرتے وقت کہیں۔ سبزی خور کھانے پر اکثر chay لکھا ہوتا ہے۔'),
                 S('کام آنے والی عادتیں', ul=[
                    'ناشتہ سڑک کے کھانے کا بڑا وقت ہے، خاص طور پر فو اور بان می۔ شام کو گرل اور گھونگھے بڑھتے ہیں۔',
                    'بین تھانہ بازار اور کئی محلے کی گلیوں پر بیٹھنے اور لے جانے دونوں ہیں۔',
                    'چھوٹے ٹھیلے اکثر نقد چاہتے ہیں۔ کچھ پر منتقلی کے لیے کیو آر کوڈ ہوتا ہے۔',
                    'وہ کھانا چنیں جو سامنے پکے اور گرم پیش کیا جائے۔ بوتل کا یا چھنا پانی پیئیں۔',
                    'کسی مشہور نام کے پیچھے بھاگنا ضروری نہیں۔ سادہ بھیڑ والا ٹھیلہ اس شہر کا طریقہ ہے۔'])]),
        },
    )

def ar(DATA, page, S, L):
    g, tg = 'دليل السفر في سايغون', 'دليل الأماكن لمن يقيم في المدينة'
    home = 'يُعرَض المنزل في <a href="{L}">الصفحة الرئيسية</a>.'
    DATA['ar'] = dict(
        btn='الحجز والتواصل',
        book='إذا أردتم الإقامة في هو تشي منه، فصفحة الحجز والتواصل توضح كيف يُحجز المنزل.',
        more_h2='صفحات أخرى في هذا الموقع',
        hub_h2='أربعة مواضيع ليوم في سايغون',
        hub_p='أربع صفحات عن المطر، ويوم واحد في الوسط، وخروج مع العائلة أو المجموعة، وطعام الشارع.',
        cards=[
            ['سايغون في يوم ماطر', 'guide-note-rain', 'متاحف وسوق مسقوف ومقاهٍ حين تمطر.'],
            ['سايغون في يوم واحد', 'guide-note-day', 'جولة في الوسط، من دون محاولة رؤية كل مكان.'],
            ['سايغون مع العائلة أو المجموعة', 'guide-note-group', 'حديقة الحيوان ودمى الماء ووجبة مشتركة.'],
            ['طعام الشارع في سايغون', 'guide-note-food', 'فو وبان مي وأرز مكسور وكيفية اختيار عربة.'],
        ],
        links={
            'rain': L('لإكمال يوم ماطر، افتحوا ', g, ' و', tg, home),
            'day': L('لترتيب اليوم بهدوء أكبر، افتحوا ', g, ' و', tg, home),
            'group': L('مع العائلة أو المجموعة، افتحوا ', g, ' و', tg, home),
            'food': L('إذا أردتم أماكن أكثر للأكل والمشي، افتحوا ', g, ' و', tg, home),
        },
        pages={
            'guide-note-rain': page(
                'سايغون تحت المطر: في الداخل',
                'في هو تشي منه تكون الزخات الغزيرة معتادة من مايو إلى نوفمبر. المتاحف والقصر والبريد والسوق المسقوف والمقاهي تتيح متابعة اليوم في مكان جاف. الساعات تتغير.',
                'سايغون في يوم ماطر',
                'المطر لا يلغي بالضرورة يوماً في هو تشي منه. المتاحف والسوق المسقوف والمقاهي هي الخطة المعتادة في الداخل.',
                [S('أشهر المطر', 'مناخ هو تشي منه مداري. الزخات القوية معتادة تقريباً من مايو إلى نوفمبر، والجو الأجف أكثر شيوعاً من ديسمبر إلى أبريل. بعد مطر غزير قد يبقى الماء قليلاً في المواضع المنخفضة ثم ينصرف. في الأشهر الرطبة يحسن أن تضم الخطة وقفة تحت سقف.'),
                 S('أماكن في الداخل أو تحت سقف', ul=[
                    'متحف شواهد الحرب، ومتحف الفنون الجميلة، ومتحف التاريخ.',
                    'قصر الاستقلال، بقاعات استقبال ومعارض داخلية.',
                    'مكتب البريد المركزي والكاتدرائية في المنطقة الوسطى نفسها.',
                    'سوق بن ثانه سوق مسقوف، فيه طعام وسلع صغيرة.',
                    'باغودا إمبراطور اليشم: تُخلع الأحذية ويُرتدى لباس محتشم، كما في كثير من الباغودا.',
                    'عروض الدمى المائية تُقدَّم في قاعة.',
                    'المقاهي والمتاجر المكيفة تنفع حين تبدأ زخة.']),
                 S('كيف يُرتَّب اليوم', 'اختاروا متحفاً واحداً أو القصر. اتركوا السوق المسقوف أو مقهى لأشد المطر. يمكن ترك شارع نغوين هوي للمشاة إلى آخر اليوم إذا خف المطر. الكاتدرائية والبريد وشارع المشاة في المنطقة الوسطى نفسها. ساعات الفتح تتغير، فتأكدوا منها في المكان.')]),
            'guide-note-day': page(
                'سايغون في يوم: الوسط فقط',
                'يوم في سايغون يكفي للوسط: الكاتدرائية والبريد وشارع الكتب وشارع المشاة وسوق بن ثانه، مع متحف واحد أو القصر. يوم واحد لا يغطي كل مكان، فراجعوا ساعات الفتح.',
                'سايغون في يوم واحد',
                'يوم في هو تشي منه يكفي للوسط. يوم واحد لا يكفي لكل متحف ولكل ناحية.',
                [S('جولة في الوسط', 'الكاتدرائية ومكتب البريد المركزي وشارع الكتب نغوين فان بينه وشارع المشاة نغوين هوي في المنطقة الوسطى نفسها، لذلك يمشي كثير من الناس بينها. سوق بن ثانه محطة معتادة للأكل أو النظر إلى العربات. أضيفوا القصر أو متحفاً واحداً، لا كل النقاط الأخرى في اليوم نفسه.'),
                 S('بين الأماكن', ul=[
                    'في الوسط تقترب عدة من هذه النقاط بما يكفي للمشي.',
                    'حافلات المدينة والمترو المنطلق من جهة بن ثانه تغطي المسافات الأبعد.',
                    'سيارات الأجرة والسيارات المطلوبة عبر تطبيق شائعة جداً. اطلبوا تشغيل العداد، أو أكدوا الرحلة في التطبيق قبل الانطلاق.',
                    'الدراجات النارية جزء من الحركة. اعبروا بإيقاع المشاة ولا تتوقفوا في الوسط.']),
                 S('ما يُترك ليوم آخر', 'حديقة الحيوان، وباغودا، ومتحف ثانٍ، أو مكان خارج المدينة مثل أنفاق كو تشي، تحتاج يوماً خاصاً. في يوم الوسط تكفي وجبة شارع وقهوة. فو أو بان مي أو الأرز المكسور يسهل إيجادها. القهوة المثلجة بحليب مكثف هي الصيغة المحلية الأكثر شيوعاً.')]),
            'guide-note-group': page(
                'سايغون مع العائلة أو مجموعة',
                'سايغون مع الأطفال أو مجموعة أسهل حين يجمع اليوم مكاناً في الهواء ومكاناً في الداخل: حديقة الحيوان ودمى الماء ومتحفاً ووجبة مشتركة. منتصف النهار غالباً حار.',
                'سايغون مع العائلة أو المجموعة',
                'يناسب هو تشي منه العائلات والمجموعات إذا انقسم اليوم بين مكان مكشوف ومكان مسقوف.',
                [S('مع الأطفال', ul=[
                    'حديقة الحيوان والحديقة النباتية في سايغون حديقة قديمة في المدينة، بممرات ظليلة.',
                    'تُشاهد الدمى المائية في قاعة ويمكن متابعتها من دون حوار كثير.',
                    'الأسواق المسقوفة مزدحمة. أمسكوا أيدي الأطفال قرب الطريق وبين العربات.',
                    'منتصف النهار غالباً حار. الصباح وآخر العصر يناسبان الخارج. منتصف النهار يناسب متحفاً أو مقهى أو استراحة.',
                    'اشربوا ماءً معبأة أو مفلترة.',
                    'في الباغودا والكنائس يُستحسن لباس محتشم. في الباغودا تُخلع الأحذية عادة.']),
                 S('مع مجموعة', 'يمكن للمجموعة أن تطلب عدة أطباق صغيرة عند عربة، أو حصصاً في محل فو أو أرز مكسور. شارع نغوين هوي للمشاة والفسحة أمام دار الأوبرا نقطتا لقاء سهلتان مساءً. اختاروا متحفاً واحداً أو القصر لتبقوا معاً، واتركوا وقتاً بلا جدول بدل حشر كل نقطة في اليوم نفسه.'),
                 S('ملاحظات للجميع', ul=[
                    'حركة الدراجات النارية كثيفة. اعبروا مع الآخرين بخطوة منتظمة.',
                    'العربات الصغيرة تقبل عادةً النقد. بعضها يعرض رمز QR لتحويل.',
                    'من مايو إلى نوفمبر تقريباً، أبقوا قائمة بأماكن داخلية في المتناول.'])]),
            'guide-note-food': page(
                'طعام الشارع في سايغون',
                'يمتد طعام الشارع في سايغون من الفطور إلى المساء: فو وبان مي وأرز مكسور وبان سيو وقهوة بالحليب. اختاروا عربة يُطهى الطعام أمامكم، والمزدحمة أنسب.',
                'طعام الشارع في سايغون',
                'الطبخ على الرصيف طريقة عادية للأكل في هو تشي منه، من الفطور إلى وقت متأخر من الليل.',
                [S('أطباق تُرى كثيراً', ul=[
                    'فو: حساء نودلز الأرز، غالباً بلحم البقر أو الدجاج.',
                    'بان مي: باغيت مع لحم ومخللات وأعشاب وفلفل حار.',
                    'أرز مكسور: مع ضلع مشوي وبيضة وإضافات.',
                    'هو تيو وحساءات نودلز أخرى بمرق صافٍ.',
                    'بان سيو: فطيرة مالحة مقرمشة مع أعشاب.',
                    'غوي كوون: لفائف طازجة بالأعشاب.',
                    'تشي: حلويات على شكل حساء حلو.',
                    'كا في سوا دا قهوة مثلجة بحليب مكثف. باك سيو أكثر حليباً.']),
                 S('عند العربة', 'تضع العربة مقاعد منخفضة على الرصيف. العربة المزدحمة التي تخرج أطباقها بسرعة هي الاختيار المعتاد. انظروا إلى الطعام وهو يُطهى أمامكم. إذا أردتم فلفلاً أقل فقولوا ذلك عند الطلب. الطعام النباتي يُعلَّم غالباً بكلمة chay.'),
                 S('عادات مفيدة', ul=[
                    'الفطور وقت مهم لطعام الشارع، خصوصاً فو وبان مي. في المساء تكثر المشاوي والقواقع.',
                    'سوق بن ثانه وكثير من شوارع الأحياء فيها جلوس وطعام يُحمل.',
                    'العربات الصغيرة تفضّل غالباً النقد. بعضها يعرض رمز QR لتحويل.',
                    'اختاروا طعاماً يُطهى أمامكم ويُقدَّم ساخناً. اشربوا ماءً معبأة أو مفلترة.',
                    'لا حاجة لملاحقة اسم مشهور. عربة عادية ومزدحمة هي نمط المدينة.'])]),
        },
    )

def zhtw(DATA, page, S, L):
    g, tg = '西貢旅遊指南', '住客可用的本地地點指南'
    home = '房子的介紹在<a href="{L}">首頁</a>。'
    DATA['zh-tw'] = dict(
        btn='預訂與聯絡',
        book='如果想住在胡志明市，預訂與聯絡頁說明如何預訂這棟房子。',
        more_h2='本站上的其他閱讀',
        hub_h2='西貢一天可以怎麼過',
        hub_p='下面四篇分別寫雨天、市中心一天、與家人或朋友同行，以及街頭飲食。',
        cards=[
            ['西貢雨天', 'guide-note-rain', '博物館、有頂市場和咖啡館，用來躲開陣雨。'],
            ['西貢一天', 'guide-note-day', '只走市中心，不把每個景點排進同一天。'],
            ['西貢同行', 'guide-note-group', '動物園、水上木偶和一頓大家一起吃的飯。'],
            ['西貢街頭吃', 'guide-note-food', '河粉、法國麵包、碎米飯，以及怎麼挑路邊攤。'],
        ],
        links={
            'rain': L('雨天之外的行程，可以接著看', g, '和', tg, home),
            'day': L('想把這一天和其他安排接上，可以看', g, '和', tg, home),
            'group': L('和家人或朋友一起走，可以再看', g, '和', tg, home),
            'food': L('如果還想找地方吃、找地方走，可以看', g, '和', tg, home),
        },
        pages={
            'guide-note-rain': page(
                '西貢雨天：室內怎麼安排',
                '胡志明市約五月至十一月常有大陣雨，十二月至四月較乾。雨天可去戰爭遺跡博物館、美術館、獨立宮、中央郵局、濱城市場或咖啡館，水上木偶也在室內演出。',
                '西貢雨天，安排在室內',
                '下雨不必取消胡志明市的一天。博物館、有頂的市場和咖啡館是常見的室內安排。',
                [S('哪幾個月更常下雨', '胡志明市是熱帶氣候。大約五月到十一月常有大陣雨。大約十二月到四月更常是乾季。大雨之後，低窪處可能短時間積水，然後退去。濕季裡，一天的安排裡應該有一個室內落點。'),
                 S('室內或有頂的地方', ul=[
                    '戰爭遺跡博物館、美術館和歷史博物館。',
                    '獨立宮，接待廳和展覽都在室內。',
                    '中央郵局和聖母教堂在同一片市中心。',
                    '濱城市場是有頂的市場，有吃的，也有小商品。',
                    '玉皇殿：和許多寺廟一樣，進門脫鞋，穿著樸素。',
                    '水上木偶在室內演出。',
                    '陣雨開始時，咖啡館和有冷氣的店舖可以先避一避。']),
                 S('怎樣排這一天', '選一座博物館或獨立宮。把有頂的市場或一家咖啡館留給出雨最大的時候。雨勢緩和的話，阮惠步行街可以放在一天的後面。教堂、郵局和步行街在同一片市中心。開放時間會變，出發前在當地確認。')]),
            'guide-note-day': page(
                '西貢一天：只走市中心',
                '西貢的一天適合走市中心：聖母教堂、中央郵局、書店街、阮惠步行街和濱城市場，再加一座博物館或獨立宮。其餘景點和市外地點留到另一天。出發前請在當地確認開放時間。',
                '西貢的一天',
                '在胡志明市過一天，可以把市中心走清楚。一天涵蓋不了每座博物館和每片街區。',
                [S('市中心這一圈', '聖母教堂、中央郵局、阮文平書店街和阮惠步行街在同一片市中心，很多人在這些點之間步行。濱城市場是吃飯或看攤位的常見一站。同一天裡加上獨立宮或一座博物館即可，不必再把其餘景點都排進去。'),
                 S('點與點之間', ul=[
                    '市中心這幾處彼此靠近，可以步行銜接。',
                    '公共汽車，以及從濱城市場一帶出發的地鐵，用來走更遠的距離。',
                    '計程車和在應用裡叫的車很常見。可以請司機打表，或在出發前在應用裡確認行程。',
                    '摩托車是路面交通的一部分。過馬路時跟著行人的節奏，不要停在車流中間。']),
                 S('留給另一天', '動物園、一座寺廟、第二座博物館，以及市外的地點如古芝地道，都更適合單獨的一天。市中心這一天，一頓街頭餐和一杯咖啡就夠。河粉、法國麵包或碎米飯都容易找到。煉乳冰咖啡是本地常見的喝法。')]),
            'guide-note-group': page(
                '西貢與家人或朋友同行',
                '和家人或朋友在西貢，宜把一天分成戶外和室內：動物園與植物園、室內水上木偶、一座博物館，再加一頓一起吃的飯。中午通常很熱，早晨和傍晚更適合走在戶外。',
                '和家人或朋友在西貢',
                '胡志明市適合家庭，也適合朋友同行，只要這一天分成一處戶外和一處室內。',
                [S('和孩子一起', ul=[
                    '西貢動物園和植物園是城裡歷史很長的公園，園路有樹蔭。',
                    '水上木偶在室內演出，對白不多也看得懂。',
                    '有頂的市場很熱鬧。在馬路邊和攤位之間拉著孩子的手。',
                    '中午通常很熱。早晨和傍晚適合戶外。中午適合博物館、咖啡館或休息。',
                    '飲用瓶裝水或過濾水。',
                    '寺廟和教堂宜穿著樸素。寺廟裡通常要脫鞋。']),
                 S('和朋友一起', '可以在路邊攤點幾樣小菜，或在河粉店、碎米飯店點幾盤一起吃。阮惠步行街和歌劇院前的空地是晚上容易找到的會合點。選一座博物館或獨立宮，讓大家待在一起，並留出沒有排滿的時間，而不是把每個景點都塞進同一天。'),
                 S('大家都用得上的備註', ul=[
                    '摩托車很多。過馬路時與其他人保持平穩的步速。',
                    '小攤通常收現金。有的地方也放二維碼，用於銀行轉帳。',
                    '大約五月到十一月，手邊留一份室內地點名單。'])]),
            'guide-note-food': page(
                '西貢街頭飲食怎麼吃',
                '西貢街頭從早餐吃到夜裡：河粉、法國麵包、碎米飯、粿條、煎餅和煉乳冰咖啡。看攤主是否當面烹煮，忙的小攤是本地常見選擇，小攤多收現金。不必追一個有名的招牌。',
                '西貢的街頭飲食',
                '在人行道上做飯，是胡志明市從早餐到深夜都常見的吃法。',
                [S('常會遇見的吃食', ul=[
                    '河粉：米粉湯，常見牛肉或雞肉。',
                    '法國麵包：麵包夾肉、醃菜、香草和辣椒。',
                    '碎米飯：配烤排骨、肉鬆、蛋和煎蛋餅一類的小菜。',
                    '粿條，以及其他清湯粉麵。',
                    '煎餅：脆皮鹹餅，配大量香草。',
                    '鮮春捲：米紙捲香草。',
                    '甜湯：各式甜品。',
                    '煉乳冰咖啡是常見喝法。白咖啡更淡，奶更多。']),
                 S('在路邊攤', '攤主把矮凳放在人行道上。客人多、上菜快的攤是通常的選擇。看食物在你面前做出來。想少放辣椒，點餐時說一聲。素食常常標著 chay。'),
                 S('有用的習慣', ul=[
                    '早餐是街頭飲食的重要時段，尤其是河粉和法國麵包。晚上多了燒烤和炒螺。',
                    '濱城市場和許多街巷都有坐下來吃的攤，也有帶走的。',
                    '小攤通常收現金。有的地方有二維碼，用於銀行轉帳。',
                    '選當面做熟、熱著端上來的食物。飲用瓶裝水或過濾水。',
                    '不必追一個很有名的招牌。普通而忙碌的攤，就是這座城市的吃法。'])]),
        },
    )
