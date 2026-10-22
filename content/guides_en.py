"""English city guides and the whole-house audience page."""
from guide_lib import page, ui

UI = ui(
    "On this page",
    "Tell us your dates on the booking page and we will confirm the house for your stay.",
    "Booking and contact",
    "More to read",
)
HUB = "All Saigon guides"
ALSO = {
    "guide-app": ["guide-sights", "guide-practical", "home"],
    "guide-family": ["guide-sights", "guide-weather", "home"],
    "guide-airport": ["guide-arrival", "guide-traffic", "home"],
}

def cards():
    return [
        ["ASCON LIVING Guide App", "guide-app", "Places near the house, routes and practical tips in the browser."],
        ["Ho Chi Minh City with kids", "guide-family", "Ideas and practical notes for a family trip."],
        ["Airport transfer", "guide-airport", "From Tan Son Nhat toward the house, with a transfer on request."],
        ["Saigon sights", "guide-sights", "Historic streets, museums, temples and the river, at an easy pace."],
        ["Saigon markets", "guide-markets", "Ben Thanh, neighbourhood markets and what to carry home to the kitchen."],
        ["Saigon coffee", "guide-coffee", "Phin coffee, condensed milk and the rhythm of a coffee day."],
        ["Saigon river", "guide-river", "The working river, a boat trip and the view from the bank."],
        ["Evenings in Saigon", "guide-evenings", "Walking streets, river air and a night back at the house."],
        ["Mekong and Cu Chi", "guide-daytrips", "A full day on the delta or at the Cu Chi tunnels."],
        ["Saigon weather", "guide-weather", "Heat, rain and how to choose the weeks you travel."],
        ["From the airport", "guide-arrival", "Tan Son Nhat, a transfer on request, and arrival at the house."],
        ["Money, SIM and apps", "guide-practical", "Cash, a local SIM and the apps that make the days easier."],
        ["Traffic and safety", "guide-traffic", "Crossing streets, rides and ordinary care in a busy city."],
        ["Whole house", "audience", "Why one private house suits families, friends and longer stays."],
    ]

PAGES = {}

PAGES["guide-sights"] = page(
    "Saigon sights to see | ASCON LIVING",
    "A practical Saigon sights guide: historic streets, museums, temples and the river, paced so a stay can include them slowly, and mostly on foot.",
    "Saigon sights worth a slow look",
    "Saigon rewards people who pick a few places and leave room between them. The centre is compact enough to walk, the museums ask for attention, and the river gives the skyline a reason to exist.",
    [
        ("The historic centre on foot", [
            "Begin around the cathedral, the central post office and the opera house. These buildings sit close together, so the pleasure is the walk between them as much as any one doorway. The post office still feels like a working hall, with a high roof and maps on the walls, and the square outside is a natural pause when the heat builds. Street trees, school groups and postcard stalls share the same pavements.",
            "The city hall stands nearby, best enjoyed from the pavement rather than as a checklist item. If you only have one unhurried loop, this cluster is the one: architecture, shade, and enough cafes that nobody has to march. Save the deeper museums for another part of the day, when you are ready to be indoors.",
        ]),
        ("Museums and the palace", [
            "The Independence Palace, also called the Reunification Palace, is a time capsule of state rooms, war rooms and the grounds around them. Go when you can read a few rooms properly instead of photographing every staircase. The War Remnants Museum is heavier. It is a place for adults who want context, and it is worth deciding in advance whether children in your group should see the hardest galleries.",
            "The Fine Arts Museum, in a colonial building a little further out, is quieter. Ceramics, lacquer and modern painting sit in rooms that are easy to leave and return to. None of these need a full day by themselves. Two of them, with a long lunch between, make a complete morning-to-afternoon shape.",
        ]),
        ("Temples and quieter streets", [
            "The Jade Emperor Temple is smoky, crowded with statues and much smaller than its reputation. Incense, turtles in the pond and the press of visitors make it a short visit that stays with you. Dress with shoulders and knees covered, step aside for people who are praying, and do not treat the courtyards as a stage.",
            "Other temples and temples are scattered through ordinary streets, often beside houses and workshops. That mix is the sight: a roof of dragons next to a motorbike repair shop, a school gate, a fruit seller. If a gate is open and a sign welcomes visitors, a quiet look is enough. If a ceremony is underway, stay at the edge.",
        ]),
        ("The river as part of the view", [
            "The Saigon River is not a backdrop you tick off from one bridge. Walk a section of the bank, watch the barges, and notice how the towers sit on the far side. A boat trip is its own subject, covered in the river guide. From land, the point is orientation: once you have seen which way the water runs, the rest of the map makes more sense.",
            "Sunset is the kind hour for this, because the heat drops and the sky does the work. You do not need a ticketed viewpoint. A public stretch of pavement, a cold drink and an unhurried look are the whole activity.",
        ]),
        ("How to shape the days", [
            "Pair an outdoor loop with an indoor one. The centre in the cooler part of the day, a museum when the sun is high, a temple or the river later. Leave one day with almost nothing booked, because Saigon is full of streets that are better than the plan you made at breakfast.",
            "Wear shoes you can walk in, carry water, and keep the museum bag light. The house is the reset: air conditioning in the bedrooms and the living room, a kitchen if you want fruit and coffee before you go out again, and a rooftop when the city has been enough.",
        ]),
        ("What this guide leaves out", [
            "There is no ranking here and no promise that a sight will be empty. Schedules change, and so do temporary closures. Check the day before, especially around public holidays, and treat a closed door as a reason to walk the neighbourhood instead.",
            "If you want markets, coffee or a day beyond the city, those have their own pages. The sights above are enough for a first stay, and they are better the second time, when you already know which street you liked.",
        ]),
    ],
    ["guide-markets", "guide-coffee", "guide-river", "home"],
)

PAGES["guide-markets"] = page(
    "Saigon markets for visitors | ASCON LIVING",
    "How Saigon markets work for visitors: Ben Thanh, neighbourhood halls, what people actually buy, and how to shop without turning the morning into a chore.",
    "Saigon markets, from the famous hall to the local one",
    "Markets in Saigon are not one thing. Some are built for visitors, some feed the street outside, and the useful ones do a bit of both. Go with a small list and an appetite, not a plan to see every aisle.",
    [
        ("Ben Thanh and the visitor halls", [
            "Ben Thanh is the market people mean when they say they went to the market. The main hall is a grid of stalls: coffee, dried fruit, lacquer, clothes, and a food section that smells louder than it looks. Vendors will call you over. A smile and a head shake is a complete answer if you are only looking.",
            "At stalls aimed at visitors, buying is a short conversation. Decide what you want before you start, and walk away if the conversation stops being pleasant. The building itself is the landmark: a clock tower, a low roof, and streets around it that stay busy long after you have finished inside.",
        ]),
        ("Neighbourhood markets", [
            "Every part of the city has a wet market that opens for people who live there. Produce is piled on tables, fish sits on ice, and the cooked-food edge serves breakfast to people on the way to work. These are not performances. Step carefully, buy something small if you are taking up space, and keep your bag in front of you.",
            "Binh Tay, in the Chinese-founded quarter of Cho Lon, is the large-scale version: a courtyard, wholesale aisles and a roof you can see from a distance. It is calmer if you treat it as architecture and people-watching, and more interesting if you notice what is being sold in bulk. You will not need a guide. You will need patience with the crowds near the gates.",
        ]),
        ("What is worth carrying home", [
            "Coffee is the easy souvenir: beans or ground coffee packed for travel, from a stall that will let you smell the bag. Look for a roast date or at least a shop that turns stock over, and buy a small amount first. Dried fruit, chilli and sweets travel well if the packet is sealed. Fabric and simple clothes are fun if you can try them or if the size is obvious.",
            "Skip anything that needs refrigeration on a long travel day, and skip lacquer or ceramics unless you have a way to pack them. The house kitchen is the better destination for fruit, herbs and breakfast things. A market tomato eaten the same day beats a suitcase of snacks you will not finish.",
        ]),
        ("How to behave, and what to watch", [
            "Ask before you photograph a person, especially someone working. Do not touch produce you are not buying. If you are offered a seat at a food stall, sitting down means you are a customer. Cash in small notes keeps the exchange simple, and the money guide covers how to carry it.",
            "Bags and phones are the practical risk, not the food. Wear your bag across your body, and do not leave a phone on the edge of a table. Heat and wet floors matter as much as crowds. Shoes with a grip, and a willingness to step aside, will do more than any list of rules.",
        ]),
        ("Morning or later", [
            "Produce is at its best earlier, when the stalls are still being filled and the cooked-food edge is serving people who have somewhere to be. Later in the day the visitor halls are busier and the local markets thinner. Neither is wrong. Match the hour to the errand: food shopping early, a look around Ben Thanh when you are already in the centre.",
            "Do not try to combine a serious market morning with a museum and a temple. The market is the outing. Go back to the house, wash the fruit, and make coffee. That sequence is more Saigon than a schedule that never sits down.",
        ]),
        ("A short list is enough", [
            "One visitor market and one neighbourhood market will teach you the difference. After that, you will notice markets you were not looking for: a lane of flower sellers, a row of fabric shops, a woman with a basket who is the market for her street.",
            "If the day is wet, the covered halls are the comfortable version. If you want the river or the sights instead, leave the market for another morning. They will still be there.",
        ]),
    ],
    ["guide-sights", "guide-coffee", "guide-practical", "home"],
)

PAGES["guide-coffee"] = page(
    "Saigon coffee culture | ASCON LIVING",
    "Saigon coffee culture without the jargon: phin filters, condensed milk, iced coffee and how to build a day around cups rather than a checklist.",
    "How Saigon drinks its coffee",
    "Coffee in Saigon is a pace, not a trend. People sit on low stools, in shop-houses and in quiet rooms with air conditioning. The drink is usually strong, often sweet, and almost always worth ordering again.",
    [
        ("The phin and the cup", [
            "The local brewer is a small metal phin set over a glass. Hot water drips through ground robusta, slowly enough that the table is part of the order. You can drink it black, or with a spoon of condensed milk that you stir in yourself. Iced coffee, ca phe sua da, is the default once the day is hot: the same drip, poured over ice.",
            "Bac xiu is the milder, milkier cousin. Coconut coffee and salted coffee show up on many menus now, and they are worth one cup if you like a drink that tastes like a recipe. Egg coffee is more associated with the north, though you will find it here. Start with the iced milk coffee. It is the one the city actually runs on.",
        ]),
        ("Where people sit", [
            "The sidewalk version is a few stools, a kettle and a view of the traffic. It is social and a little dusty, and it is perfect when you want twenty quiet sips between errands. Order, sit, and do not expect a long menu. If the stools are full, the next place is rarely far.",
            "Indoor cafes are the other half of the culture: rooms for laptops, conversations and the hottest part of the day. Some are calm and dim, some are bright and sweet. Choose by the chair, not by the sign. A cafe with space to talk will serve the same family of drinks as the sidewalk, usually with more ice and more time.",
        ]),
        ("How to order without a performance", [
            "Pointing at a neighbour's glass works. So does the short list: den da for iced black, sua da for iced with milk, nong if you want it hot. Sugar is often already in the condensed milk, so taste before you add anything. If you take less sweetness, say so at the start.",
            "Pay when the cup arrives or when you leave, depending on the place. Small notes help. You do not need to speak much Vietnamese to be a good customer. You do need to return the glass to the tray and not move a stool into the road.",
        ]),
        ("A day built on cups", [
            "One cup after breakfast, one when the centre has worn you out, one at the end of the afternoon. That is a full coffee day, and it leaves room for a market or a museum. Chasing a dozen shops turns the drink into a task. The better plan is to notice one place you would come back to, and then actually come back.",
            "Coffee also makes a useful pause with children or with friends who do not want another sight. The sidewalk is quick. The indoor room is where you decide what happens next. Either way, the caffeine is real. Robusta here is not a timid roast.",
        ]),
        ("Beans to take with you", [
            "If you want coffee for later, buy a small sealed bag from a place that will let you smell it, and use it within a few weeks of going home. Ground coffee is convenient for a phin. Beans make sense if you have a grinder. The markets guide covers the stall version of the same idea.",
            "The house has a coffee machine, so the first cup of the morning does not depend on finding a stool. Use that when you want a slow start, and go out for the glass of sua da when you want the city in the cup. Both belong in the same stay.",
        ]),
        ("What not to worry about", [
            "You will not ruin the experience by ordering the wrong size or the wrong ice. Saigon coffee is forgiving as long as you sit down for it. There is no score to chase and no shop you must visit to say you understood the city.",
            "If you want the evening version of this rhythm, the evenings guide picks up where the last cup leaves off. If you want the river at the end of the walk, that page is the next one to open.",
        ]),
    ],
    ["guide-markets", "guide-sights", "guide-evenings", "home"],
)

PAGES["guide-river"] = page(
    "Saigon river and boat tour | ASCON LIVING",
    "The Saigon River explained for visitors: what a boat trip shows, how to choose a calm outing, and how the water orients the rest of the city.",
    "The Saigon River and a boat on it",
    "The river is why the city is here. Barges still move goods, ferries still cross, and the bank is where the heat of the streets finally opens out. A boat trip is optional. Looking at the water is not.",
    [
        ("What the river is for", [
            "From the bank you see a working waterway, not a scenic canal that exists for photographs. Cargo boats, tourist decks and the odd fishing skiff share the same channel. The far bank has been building upward for years, so the skyline is part of the view, and it changes with the light more than with any single tower.",
            "Walking a stretch of pavement is the simplest version. You get the breeze, the scale and a clear sense of which way is downstream. Do that before you book a boat. The trip makes more sense once you already know the water from land.",
        ]),
        ("What a boat trip shows", [
            "Most visitor boats leave from piers in the centre and loop along the main channel. You pass port cranes, house-boats, bridges and the contrast between older warehouses and new towers. A daytime trip is about the work of the river. A later trip is about the light on the water and the city turning its lights on.",
            "Commentary varies. Some boats tell the history of the port, some play music, some simply serve a cold drink and let you stand at the rail. Choose the quieter option if you want to look, and the livelier one if your group wants a shared evening. Either way, the point is the banks sliding past, not a performance on deck.",
        ]),
        ("How to choose without a hard sell", [
            "Book with a company that tells you the pier, the kind of boat and what is included before you pay. A short loop on a small boat feels different from a large deck with a set menu. If you do not want a meal, say so. If you want to sit rather than dance, pick the boat that looks like sitting.",
            "Go on a day when you are not already exhausted. The pier approach can be busy, and boarding takes patience. Carry a light layer if you burn easily, even when the city itself feels hot, because the breeze on the water is stronger than it looks from the road. Keep bags zipped while you are moving between the pier and the deck.",
        ]),
        ("Weather, light and comfort", [
            "A clear late afternoon is the easy choice. In the rainy months a shower can arrive and leave again, and many boats simply wait it out or shorten the loop. That is not a failed trip. The river under cloud is still the river, and the city looks different without hard sun.",
            "If the forecast is a washout, take the bank on foot another day and give the boat a miss. There is no prize for going out in a storm. The weather guide explains the two seasons in more detail, without pretending that a single week is predictable.",
        ]),
        ("After you step off", [
            "The centre is right there when you land. A coffee, a short walk along the water, or a direct ride back to the house are all reasonable endings. Do not stack a museum on the same evening. Let the trip be the event.",
            "The house rooftop looks over the river and the skyline, which is a different angle from the deck: still, private, and available on the nights you do not want to go out at all. A boat one day and the terrace another is a complete river stay.",
        ]),
        ("The delta is a different water", [
            "The Mekong Delta is not a longer version of this loop. It is a day out of the city, with orchards, smaller channels and villages. If that is what you want, use the day-trip guide and keep the Saigon River as the city's own water.",
            "You can enjoy both in one stay. They should not be the same day. The city river is an evening or an easy afternoon. The delta asks for the whole day and a quieter morning after.",
        ]),
    ],
    ["guide-sights", "guide-daytrips", "guide-evenings", "home"],
)

PAGES["guide-evenings"] = page(
    "Saigon evenings and going out | ASCON LIVING",
    "Evenings in Saigon for a whole-house stay: walking streets, river air, music, and a clear plan for getting back to the house without packing the night.",
    "Evenings and going out in Saigon",
    "Saigon changes when the light drops. The pavements fill, the river breeze starts to matter, and the day you spent in museums becomes a reason to sit down. You do not need a nightlife itinerary. You need one plan and a way home.",
    [
        ("What the city does after dark", [
            "The walking streets in the centre, especially around Nguyen Hue, are the simple version of going out. Families, couples and groups share the same open space. It is lit, it is public, and it is enough if all you want is to be outside. Add a drink or a snack from a stall at the edge and you have an evening.",
            "The riverbank is the quieter alternative. The same water you might see from a boat is there for a walk, with fewer decisions. If the day was hot, this is when the city becomes pleasant again. Go while you still have energy to stroll, not as a forced last stop.",
        ]),
        ("Sitting down, not touring", [
            "A good evening here is usually one neighbourhood and one or two stops. A cafe that becomes a bar as the menu flips. A small room with live music. A late bowl of something you have already learned to order. The point is the table, the people you are with, and the fact that nobody is rushing you to a third venue.",
            "Busy streets aimed at visitors exist, and they are loud on purpose. Walk through if you are curious, and leave when you have seen enough. You will not miss a secret by skipping the loudest block. The better rooms are the ones where you can hear the person next to you.",
        ]),
        ("Music and a private room", [
            "Live music shows up in small venues across the centre: a singer, a guitar, a room that holds a few dozen people. Check the night before if you care about a style, and arrive with the idea that you might simply listen and leave. That is a complete outing.",
            "If your group would rather sing than watch, Saigon has private singing rooms as well as the karaoke set up in the house. The house version means you already have the room, the equipment and the rooftop if you want air between songs. Use the city when you want to go out. Use the house when the outing is the people you came with.",
        ]),
        ("Eating without making it the theme", [
            "Evenings are when many people want a proper table: a place with a menu, a fan or air conditioning, and enough chairs. Choose it in the afternoon, not while you are standing on a corner. The markets and coffee pages cover the daytime version of eating and drinking. At night, comfort matters more than novelty.",
            "If someone in the group is tired, split the plan. Part of the group can go out. The house has a kitchen, a large fridge and a living room with a big screen, so staying in is a real option rather than a compromise. A rooftop barbecue is the middle path when you want the evening air without a ride.",
        ]),
        ("Getting back", [
            "Agree the ride before you need it. A car booked in a ride-hailing app, or a taxi from a rank you already trust, is easier than negotiating on a loud pavement. The traffic and safety page goes into the habits that matter. For the evening itself, the rule is simple: decide the way home while you are still glad you went out.",
            "The house uses a keypad for self check-in, and the outer gate uses a key. Keep that key in a pocket you will still know about later, and do not leave it on a cafe table. Arrival after a night out should be dull. Dull is the goal.",
        ]),
        ("A week of evenings", [
            "You do not need a different spectacle every night. Repeat the walking street. Repeat the rooftop. Go to the river once from the water and once from the bank. The stay gets better when the evenings feel familiar.",
            "If you are here for a long stretch, the same logic scales: two nights out, the rest at home, and coffee the next morning. The weather will cancel some plans. Let it. Saigon will still be outside tomorrow.",
        ]),
    ],
    ["guide-river", "guide-coffee", "guide-traffic", "home"],
)

PAGES["guide-daytrips"] = page(
    "Mekong Delta and Cu Chi tunnels | ASCON LIVING",
    "A practical look at two classic days out of Saigon: the Mekong Delta's water and orchards, and the Cu Chi tunnels, and how to choose between them.",
    "Day trips: the Mekong Delta and the Cu Chi tunnels",
    "These are the two outings people mean when they ask what to do beyond Saigon. They are different days. One is water, fruit and villages. The other is history underground. Pick one, give it the whole day, and leave the city sights for the days around it.",
    [
        ("Two trips, two moods", [
            "The Mekong Delta is a landscape. You travel out of the city to smaller channels, orchards, workshops and houses that face the water. The pleasure is being away from traffic and seeing how the river system feeds the south. It is gentle if you choose a calm operator, and tiring if the day is packed with too many stops.",
            "Cu Chi is a historical site. The tunnels are a remnant of the wars of the twentieth century, preserved and, in places, enlarged so visitors can crawl a short section. It is sobering more than scenic. Go because you want the history, not because you want a pretty afternoon.",
        ]),
        ("The delta, without the script", [
            "A typical delta day includes a boat on a narrow channel, a walk through fruit trees, and a look at a small workshop: coconut candy, rice paper, or something similar. You will be offered fruit. You will be offered a seat. Take the parts you want and treat the rest as optional.",
            "The scenery is the point, so choose an operator that spends time on the water rather than in a gift shop. A smaller group feels more like a visit and less like a convoy. Wear clothes you can sit on a wooden boat in, and bring a hat. The sun on the water is stronger than the sun between buildings.",
        ]),
        ("Cu Chi, and how to take it", [
            "Above ground you see entrances, traps explained as history, and a landscape of eucalyptus and scrub that hides the scale of what was dug below. Below ground, the sections open to visitors are short, low and warm. You can skip the crawl and still understand the place from the displays and the cleared trenches.",
            "Wear shoes with a grip and clothes you do not mind getting dusty. If anyone in the group is uncomfortable in tight spaces, say so before they are at the entrance. The site is a memorial as well as a museum. Loud jokes wear thin quickly. Read a little the night before so the ground makes sense when you arrive.",
        ]),
        ("Choosing and combining", [
            "If you have one day, choose by the people you are with. Gardens and boats suit a mixed group that wants an easy shared day. Cu Chi suits people who have asked about the war and are ready for a serious answer. Neither is a reward for getting through the other.",
            "Doing both on the same day makes both of them worse. They lie in different directions and they ask for different kinds of attention. If your stay is long enough, put a quiet city day between them. If it is not, pick one and leave the other for a return visit.",
        ]),
        ("The shape of the day", [
            "Treat it as a full day out. Have breakfast at the house, where the kitchen and the coffee machine make an early start simple, and come back in time for a slow evening. Do not book a river cruise or a late music show on the same date. The outing is the day.",
            "Carry water, a light layer against the sun, and a little cash for fruit or a drink along the way. Agree the pickup point the day before. Self check-in at the house means you are not racing a front desk when you return, which is the right way to end a long outing.",
        ]),
        ("Booking it properly", [
            "Use a named operator that confirms the meeting point and what the day includes before you pay. Ask whether the boat time is a real stretch on the water or a short transfer between shops. Ask whether the tunnel visit includes the crawl or only the grounds. Clear answers are the sign you want.",
            "The city has more to do than these two trips, and you should not feel that a stay is incomplete without them. They are good days. They are not obligatory. The sights, markets and river inside Saigon can fill a week on their own.",
        ]),
    ],
    ["guide-river", "guide-sights", "guide-weather", "home"],
)

PAGES["guide-weather"] = page(
    "Saigon weather and when to visit | ASCON LIVING",
    "Saigon weather in plain language: the drier months, the rainy months, heat that never really leaves, and how to pack for a stay in a whole house.",
    "Saigon weather and when to come",
    "Saigon is warm in every month that has your name on it. The useful question is not whether it will be hot. It is whether you would rather have dry pavements or dramatic skies, and how you will spend the middle of the day.",
    [
        ("Two seasons, one climate", [
            "The drier months usually run from about December to April. Skies are clearer, rain is less common, and walking the centre is easier. It is still hot, especially from late morning into the afternoon. The difference is that you can plan an outdoor morning with more confidence.",
            "The rainy months usually run from about May to November. Rain often arrives as a heavy shower rather than a full day of drizzle, though some days simply stay grey. Streets can flood in low spots for a short time and then clear. You plan with a backup, not with a cancelled week.",
        ]),
        ("The drier months", [
            "December through February is the stretch many visitors find easiest. The heat is real but less punishing, and evenings are pleasant for the river and the walking streets. March and April grow hotter before the rains return. If you fade in high heat, aim for the earlier part of the dry season and keep midday indoors.",
            "These months are also when more people travel. Book the house for the dates you want instead of assuming a week will be open. The city is not more interesting because it is busier. It is simply fuller, and Tet, the lunar new year, can rearrange transport and meals for several days around the holiday itself.",
        ]),
        ("The rainy months", [
            "A rainy-season stay is not a mistake. Mornings are often clear enough for the centre or a market, and the shower becomes the signal to be in a museum, a cafe or back at the house. The air can feel heavy. The pay-off is greener streets and fewer assumptions that every hour must be outdoors.",
            "Pack a light rain jacket rather than an umbrella you will fight on a windy corner, and shoes that can get wet and dry again. A day trip to the delta or Cu Chi is still possible. Look at the morning sky and the operator's note, and be willing to move the outing by a day. The tunnels and the orchards do not expire.",
        ]),
        ("Heat, and the middle of the day", [
            "Whatever the month, build the day around the heat. Outdoor walking early, a long lunch or a rest when the sun is high, and the river or a neighbourhood stroll later. This is not laziness. It is how people who live here arrange an ordinary Tuesday.",
            "The house is part of that plan. Air conditioning runs in every bedroom and in the living room. A dark, quiet room in the middle of the day is a feature of the stay, not a failure of the itinerary. Drink water before you feel dramatic about it. The sun here is stronger than a cloudy morning suggests.",
        ]),
        ("What to pack", [
            "Light clothes you can wash, a hat, sunscreen, and one layer for aggressive air conditioning indoors. Modest clothes for temples: covered shoulders and knees. Shoes you can walk in on uneven wet tiles. A small bag you can wear across your body.",
            "The house has a washing machine and an iron, so a week of clothes does not require a large suitcase. A laundry service can be arranged as well if you would rather hand the bag over. Pack for the first few days either way, and let the machine cover the rest.",
        ]),
        ("Choosing your weeks", [
            "Come in the drier months if walking outside is the heart of the trip. Come in the rainy months if you are happy to mix cafes, museums and the house with the showers. Come outside the Tet rush if you want more choice of dates. None of these is a wrong city.",
            "The sights, markets and day trips all work in both seasons. They simply change shape. Read the traffic page as well if you are new to the streets, because wet roads and dry roads ask for the same habits, with a little more patience when it has just rained.",
        ]),
    ],
    ["guide-sights", "guide-daytrips", "guide-traffic", "home"],
)

PAGES["guide-arrival"] = page(
    "From the airport to Saigon | ASCON LIVING",
    "Arriving at Tan Son Nhat and reaching the house: a private transfer on request, ride-hailing, official taxis, and self check-in when you get to the door.",
    "Getting here from the airport",
    "Ho Chi Minh City's main airport is Tan Son Nhat, code SGN. It sits inside the urban area, with separate zones for international and domestic flights. The useful question on landing is not which sight to see first. It is how you will cover the last part of the journey, and what happens at the door.",
    [
        ("Before you land", [
            "Have the address written in Vietnamese: 389A Duong Tran Xuan Soan, Tan Hung, Ho Chi Minh City. A screenshot is enough if your data has not started yet. Add our phone number in your contacts before you fly, so a driver or a border form is not the moment you go looking for it.",
            "Pack the key information in your cabin bag: passport, the address, and any note we have sent about arrival. Checked luggage can take a while to appear. There is no need to start a city plan until you are actually outside the terminal with your bags.",
        ]),
        ("A transfer on request", [
            "A private airport transfer can be arranged on request. It is not added to a stay unless you ask. Message us with your flight number and landing time when you book, or as soon as the flight is fixed, and we will confirm whether we can meet that arrival.",
            "On request means you should not assume a driver is waiting if you have not heard back. If the flight moves, tell us. If you would rather make your own way, that is a normal choice and does not need an apology. The house is the same either way.",
        ]),
        ("Ride-hailing and official taxis", [
            "Ride-hailing apps work from designated pickup zones outside the terminals. Connect to airport data or a local SIM first, request the car in the app, and match the plate before you get in. The app is the receipt and the route. You do not need to negotiate a fare at the curb.",
            "Official taxis queue at marked ranks. Use those cars, confirm that the meter will run, and ignore offers from people who approach you inside the arrivals hall. If a conversation feels like a hustle, walk back to the rank. The traffic page covers the same habits for the rest of the stay.",
        ]),
        ("The drive itself", [
            "You will cross a busy city. Traffic changes with the time of day, with rain, and with whatever the streets are doing that afternoon. Build a margin if someone is meeting you or if you have plans the same evening. There is no single duration worth memorising, because the city does not owe you one.",
            "Sit back, keep the address visible, and let the driver drive. A translation app helps if you need to confirm a turn. You are not expected to navigate. If the route looks odd, the app's map is the calm way to check, not a debate at a junction.",
        ]),
        ("At the house", [
            "Check-in is from 14:00, and the window runs until 23:00. Checkout is at 12:00. Self check-in uses a keypad. The outer gate uses a separate key. We send the details for your stay before you arrive, so you are not waiting on the pavement for a person with a clipboard.",
            "If your flight lands outside that window, tell us before the day itself. Outdoor cameras cover the entrance, which is a fact of the house, not a promise about the street. Once you are in, the kitchen, the air conditioning and a shower matter more than any further plan.",
        ]),
        ("The first evening", [
            "Keep the first night small. A walk if you have energy, or food near the house and an early stop if you do not. The money, SIM and apps page is the one to read on the plane if you want data and cash sorted quickly. The sights can wait until morning.",
            "The whole house is yours from the moment you check in. That is the point of arriving somewhere that is not a lobby. Lock the gate, learn the keypad once, and let the rest of the city be tomorrow's problem.",
        ]),
    ],
    ["guide-practical", "guide-traffic", "guide-weather", "home"],
)

PAGES["guide-practical"] = page(
    "Money, SIM and apps in Saigon | ASCON LIVING",
    "Practical money, SIM and app notes for Saigon: dong and cards, a local SIM or eSIM, and the maps and ride apps that make ordinary days easier.",
    "Money, a SIM and the apps that help",
    "Saigon is easy once your phone has data and your pocket has small notes. Everything else is a variation on those two facts. Set them up early and the rest of the guides become simpler.",
    [
        ("Dong, cash and cards", [
            "The currency is the dong, and the numbers are long. Count zeros before you hand a note over, and count them again when you get change. Cards work in many hotels, larger restaurants and shops. Markets, sidewalk coffee and small bowls of food still expect cash. Carry both, and do not rely on a card for the stall you actually wanted.",
            "ATMs are widespread in the centre and around malls. Use machines attached to a bank when you can, and cover the keypad. Tell your bank you are travelling so the card is not frozen on day one. There is no need to exchange a large sum at the airport if a smaller amount will get you to the house and through the first meals.",
        ]),
        ("Small notes and everyday payments", [
            "Break large notes early, at a cafe or a shop that can do it without a speech. Drivers and market stalls do not always have change for the biggest bills. Keep a separate pocket for the money you are willing to spend that day, and a deeper pocket for the rest.",
            "Ask what you will owe before you sit down at a place with no menu, and glance at the total before you pay. This is ordinary care, not suspicion. The traffic and safety page covers the ride version of the same idea. For meals and coffee, a clear number spoken at the start prevents the only argument worth avoiding.",
        ]),
        ("SIM and eSIM", [
            "A local SIM or an eSIM is the difference between a confident day and a day spent searching for wifi. You can set up an eSIM before you fly if your phone allows it, or buy a tourist SIM at the airport or in town. Bring your passport. Staff do this all day and will usually have a short menu of data bundles.",
            "Test the data before you leave the counter. Load a map, send yourself a message, and save the house address offline. Wifi at the house is fast, fibre up to 1 Gbit/s with mesh on every floor, so you are not dependent on mobile data once you are home. You still want data for the ride back.",
        ]),
        ("Maps, translation and rides", [
            "Download an offline map of the city before you need it. Pin the house, the airport and any place you have already decided to visit. A translation app with the camera function helps with menus and signs. Download the language pack so it works in a stairwell with no signal.",
            "A ride-hailing app is the simplest way to move with luggage or in the rain. Set it up on the airport wifi if you did not do it at home, and pay in the app when you can. The car that matches the plate on your screen is the car you want. The same app is useful at the end of an evening, which is why the evenings guide sends you here.",
        ]),
        ("Contacts and copies", [
            "Save our phone number, and keep a photo of your passport in a place you can reach if the passport is in the safe of your bag. Share the house pin with the people you are travelling with, so nobody is dependent on one phone. The address in Vietnamese is on the airport page.",
            "Messaging apps you already use are enough to reach us. You do not need a new account for the sake of it. If a form or a driver needs a local number, the SIM you just bought is that number. Write it down. You will not remember it.",
        ]),
        ("What this does not cover", [
            "This page is not a list of shops, banks or plans, and it will not quote a rate that would be wrong next month. Money and data are tools. Once they work, go to the sights, the markets or the coffee page and use them.",
            "If something fails, a second ATM, a second cafe with wifi, or a message to us will fix more problems than a long troubleshooting guide. The house is the fallback: power, water, a kitchen and a connection that does not depend on the stall outside.",
        ]),
    ],
    ["guide-arrival", "guide-traffic", "guide-markets", "home"],
)

PAGES["guide-traffic"] = page(
    "Saigon traffic and safety | ASCON LIVING",
    "Saigon traffic and everyday safety: how the streets move, how to cross, how to take a ride, and the ordinary habits that keep a stay calm and simple.",
    "Traffic and everyday safety in Saigon",
    "The streets look chaotic and mostly are not. Motorbikes flow, cars push through the gaps, and people cross because the flow has a logic. Learn the logic once and the city stops feeling like a dare.",
    [
        ("How the streets move", [
            "Motorbikes are the main event. They move in streams, they filter to the front of queues, and they expect pedestrians to be predictable. Cars and buses are fewer and less nimble. Horns are a signal of presence more than a rebuke. The noise is information.",
            "Pavements are shared with parked bikes, cooking and the occasional stool. You will step into the road. That is normal. It is not a reason to freeze or to sprint. The crossing section below is the whole skill.",
        ]),
        ("Crossing", [
            "Pick a point where others are already crossing, wait for a gap in the nearest stream, and walk at a steady pace. Keep your path straight. Riders will adjust to you if you do not surprise them. Eye contact helps. A sudden step back is more dangerous than a calm walk forward.",
            "Do this with children by holding hands and moving as one person, not as a chain that hesitates in the middle. At night, cross where there is light. If you are tired or carrying bags, use a ride for the long pieces and cross only the last short bit. Pride is not a transport plan.",
        ]),
        ("Rides", [
            "For anything with luggage, rain, or a destination you do not know, take a car through a ride-hailing app or an official taxi. Match the plate. Wear a seatbelt if there is one. A motorbike taxi is a local habit that visitors can skip without missing anything important, especially with bags or after dark.",
            "Watch your route on your own phone if you like, and speak up early if it diverges, using a translation app rather than volume. Pay the way you agreed at the start. The money page covers cash and cards. The airport page covers the rank outside the terminal, which is the same idea in a busier place.",
        ]),
        ("Bags, phones and drinks", [
            "Wear your bag across your body and keep the opening against you in crowds and on the sidewalk. Phones leave hands quickly when they are held at the edge of a table or used in the road. Step to the side of a pavement before you look at a map.",
            "Do not leave a drink or a phone with a stranger while you step away. Do not accept a ride from someone who will not use the meter or the app. These are boring rules because they work. The city is not a puzzle designed to catch you. It is a busy place where unattended things move.",
        ]),
        ("Health and documents", [
            "Drink water, use sunscreen, and treat the midday heat as real. Stomach upsets are usually about pace and ice and new food, not about a single dangerous dish. Eat where the food is moving and where other people are eating. Wash your hands. The house kitchen is there when you want a simple meal you made yourself.",
            "Carry a copy of your passport and keep the original secure. Note the number of a clinic your insurer recommends before you need it. For emergencies, 113 reaches the police and 115 reaches an ambulance. Save them. You will probably never use them, which is the correct outcome.",
        ]),
        ("The house as the calm end", [
            "Outdoor cameras watch the entrance. Self check-in is a keypad, and the outer gate uses a key. That is the security setup we actually have. Use it: lock the gate, do not share the keypad code in a group chat with people who are not in your party, and tell us if something at the door looks wrong.",
            "None of this should shrink the trip. Cross the street, take the river, sit on the small stool. The habits above are what make those ordinary pleasures stay ordinary. Read the evenings guide when you want the night version, and the airport guide when you are still on the plane.",
        ]),
    ],
    ["guide-arrival", "guide-evenings", "guide-practical", "home"],
)

PAGES["audience"] = page(
    "Whole house for families and groups | ASCON LIVING",
    "Why a whole private house in Ho Chi Minh City suits families, groups of friends and longer stays: three floors, a kitchen, and no shared lobby.",
    "A whole house for families, friends and longer stays",
    "Some trips are easier when the whole place is yours. Families need bedrooms that are not a corridor apart. Friends need a kitchen and a roof. A longer stay needs a washing machine and a proper fridge. This house is built as one private house for one party.",
    [
        ("One party, the whole house", [
            "You rent the entire house, not a room in it. There are three floors plus a rooftop terrace, and more than 250 square metres. No other guests share the kitchen, the living room or the stairs. The entrance has outdoor cameras. Self check-in is by keypad, and the outer gate uses a key, so arrival does not depend on meeting someone in a lobby.",
            "Check-in is from 14:00 until 23:00. Checkout is at 12:00. Host languages are German, English, Hindi, Punjabi, Urdu and Vietnamese. Those are the practical edges of the stay. The reason to choose the house is what you can do inside it once the gate is shut.",
        ]),
        ("For families", [
            "There are three bedrooms, each with its own bathroom, plus a guest WC. Parents and children, or three generations, can spread across floors and still meet in the kitchen. Air conditioning covers every bedroom and the living room, four units in all, which matters in every month Saigon offers.",
            "The kitchen is private: a fridge of about 540 litres, a dishwasher, an oven, a microwave and a coffee machine. Breakfast can happen at the table you are not sharing. The living room is about 40 square metres, with a 75-inch 4K television. A 4K projector sets up a film night without leaving the house. The master bedroom is about 55 square metres, so one room can actually hold a family pile of bags.",
        ]),
        ("For a group of friends", [
            "Friends often want the evening more than the schedule. The rooftop terrace is about 56 square metres, with a river and skyline view, a barbecue and a smoker. Karaoke is in the house, so the singing does not require a booking across town. A games console is there for the hour when nobody wants to go out.",
            "Three floors mean one person can sleep, one can cook, and one can be on the roof. Fibre internet runs up to 1 Gbit/s, with mesh wifi on all floors, so a call home does not depend on who is streaming. The guest WC keeps the morning queue shorter. None of this is a programme. It is space.",
        ]),
        ("For a longer stay", [
            "A longer stay is a series of ordinary days. The washing machine and the iron make that possible, and a laundry service is available at 30 EUR per load when you want to hand the clothes over. The large fridge and the oven mean you are not eating every meal out. The coffee machine covers the early hour before the city is worth entering.",
            "Wifi on every floor and air conditioning in the rooms you actually sit in are what make a second week feel like living rather than camping. Self check-in means a late return from the airport, or from a day on the delta, does not need a reception desk. You come back to your own gate.",
        ]),
        ("What is actually here", [
            "The confirmed list is specific. Entire private use. Three floors and a rooftop. Three en-suite bedrooms and a guest WC. Air conditioning in the bedrooms and the living room. Fibre internet and mesh wifi. A full kitchen with the appliances named above. A 75-inch 4K television, further 4K screens, a projector, karaoke, and a games console. A rooftop with a river and skyline view, a barbecue and a smoker. Keypad check-in, a key for the gate, cameras at the entrance.",
            "If you need a detail that is not on that list, ask us on the booking page before you assume it. The house is the one in the photographs. The city guides on this site cover sights, markets, coffee, the river, evenings, day trips, weather, the airport, money and the streets, for the hours you are not at home.",
        ]),
        ("How to decide", [
            "Choose the house if your group wants one front door. A family that likes to reset at midday, friends who want a roof and a kitchen, or a longer stay that needs laundry and wifi, are the stays it fits. The booking page is where dates get confirmed.",
            "Read the airport guide before you fly, and the weather guide before you pack. Then stop reading and come. The city is the reason for the trip. The house is why the trip can stay calm.",
        ]),
    ],
    ["guide-sights", "guide-weather", "guide-coffee", "home"],
)

