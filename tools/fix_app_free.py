import json,re
R={'en':[
("Our ASCON Guide App, password-protected for guests, helps","Our free ASCON Guide App helps"),
("After booking you receive the password for the ASCON Guide App, our guest guide for Ho Chi Minh City. It includes","Our free ASCON Guide App is a guide to Ho Chi Minh City. It includes"),
("ASCON Guide App (password after booking)","Free ASCON Guide App"),
(", plus the password for the ASCON Guide App, our guest guide to Ho Chi Minh City with places to eat, things to do and practical tips.",". Our free ASCON Guide App for Ho Chi Minh City has places to eat, things to do and practical tips."),
("When do I get the check-in instructions and the app password?","When do I get the check-in instructions?"),
("You receive the password for our guest guide app after booking.","Open it in your phone's browser; it is free and needs no password."),
("the password-protected ASCON Guide App for guests,","the free ASCON Guide App,"),
("The ASCON Guide App: exclusive for guests","The free ASCON Guide App"),
("It is password-protected and made exclusively for ASCON LIVING guests: you receive the password after booking. It opens","It is free, needs no password and opens"),
("Exclusive for ASCON LIVING guests: you receive the password after booking.","Free to use, no password needed."),
("How do I get the password for the ASCON Guide App?","Do I need a password for the ASCON Guide App?"),
("You receive the password after booking. The app is exclusive to ASCON LIVING guests.","No. The app is free and opens straight in your phone's browser."),
("Book your stay and get the ASCON Guide App password with your booking.","Book your stay and plan your days with the free ASCON Guide App."),
("Our password-protected guest app for Ho Chi Minh City: places near the house, travel times, routes, a map and practical tips. Password after booking.","Our free guide app for Ho Chi Minh City: places near the house, routes, a map and practical tips. No password, nothing to install."),
("Exclusive for ASCON LIVING guests; the password comes with your booking.","It is free and needs no password."),
("You receive the password after booking, so you can start planning before you even land.","It is free, so you can start planning before you even land."),
("the ASCON Guide App (password after booking)","the free ASCON Guide App")],
'de':[
("Unsere passwortgeschützte ASCON Guide App hilft","Unsere kostenlose ASCON Guide App hilft"),
("Nach der Buchung bekommt ihr das Passwort für die ASCON Guide App, unseren Gäste-Guide für Ho-Chi-Minh-Stadt. Darin","Unsere kostenlose ASCON Guide App ist ein Guide für Ho-Chi-Minh-Stadt. Darin"),
("ASCON Guide App (Passwort nach der Buchung)","Kostenlose ASCON Guide App"),
(", außerdem das Passwort für die ASCON Guide App, unseren Gäste-Guide für Ho-Chi-Minh-Stadt mit Restaurants, Aktivitäten und praktischen Tipps.",". Unsere kostenlose ASCON Guide App für Ho-Chi-Minh-Stadt zeigt Restaurants, Aktivitäten und praktische Tipps."),
("Wann bekomme ich die Check-in-Anleitung und das App-Passwort?","Wann bekomme ich die Check-in-Anleitung?"),
("Das Passwort für unsere Gäste-App bekommt ihr nach der Buchung.","Öffnet sie im Browser eures Handys; sie ist kostenlos und braucht kein Passwort."),
("die passwortgeschützte ASCON Guide App für Gäste,","die kostenlose ASCON Guide App,"),
("Die ASCON Guide App: exklusiv für Gäste","Die kostenlose ASCON Guide App"),
("Sie ist passwortgeschützt und exklusiv für ASCON LIVING Gäste: Das Passwort bekommt ihr nach der Buchung. Sie öffnet","Sie ist kostenlos, braucht kein Passwort und öffnet"),
("Exklusiv für ASCON LIVING Gäste: Das Passwort bekommt ihr nach der Buchung.","Kostenlos, ohne Passwort."),
("Wie bekomme ich das Passwort für die ASCON Guide App?","Brauche ich ein Passwort für die ASCON Guide App?"),
("Das Passwort bekommt ihr nach der Buchung. Die App ist exklusiv für ASCON LIVING Gäste.","Nein. Die App ist kostenlos und öffnet sich direkt im Browser eures Handys."),
("Bucht euren Aufenthalt und erhaltet das Passwort für die ASCON Guide App nach der Buchung.","Bucht euren Aufenthalt und plant eure Tage mit der kostenlosen ASCON Guide App."),
("Unsere passwortgeschützte Gäste-App für Ho-Chi-Minh-Stadt: Orte nahe dem Haus, Fahrzeiten, Routen, Karte und praktische Tipps. Passwort nach Buchung.","Unsere kostenlose Guide-App für Ho-Chi-Minh-Stadt: Orte nahe dem Haus, Routen, Karte und praktische Tipps. Ohne Passwort, ohne Installation."),
("Exklusiv für ASCON LIVING Gäste; das Passwort bekommt ihr nach der Buchung.","Sie ist kostenlos und braucht kein Passwort."),
("Das Passwort bekommt ihr nach der Buchung, so könnt ihr schon vor der Landung mit der Planung beginnen.","Sie ist kostenlos, so könnt ihr schon vor der Landung mit der Planung beginnen."),
("die ASCON Guide App (Passwort nach der Buchung)","die kostenlose ASCON Guide App")],
'vi':[("Dành riêng cho khách của ASCON LIVING – bạn sẽ nhận mật khẩu sau khi đặt phòng.","Miễn phí, không cần mật khẩu.")],
'hi':[("केवल ASCON LIVING के मेहमानों के लिए – पासवर्ड बुकिंग के बाद मिलता है।","मुफ़्त, किसी पासवर्ड की ज़रूरत नहीं।")],
'ur':[("صرف ASCON LIVING کے مہمانوں کے لیے – پاس ورڈ بکنگ کے بعد ملتا ہے۔","مفت، کسی پاس ورڈ کی ضرورت نہیں۔")],
'pa':[("ਸਿਰਫ਼ ASCON LIVING ਦੇ ਮਹਿਮਾਨਾਂ ਲਈ – ਪਾਸਵਰਡ ਬੁਕਿੰਗ ਤੋਂ ਬਾਅਦ ਮਿਲਦਾ ਹੈ।","ਮੁਫ਼ਤ, ਕਿਸੇ ਪਾਸਵਰਡ ਦੀ ਲੋੜ ਨਹੀਂ।")]}
for l,rs in R.items():
    rs=sorted(rs,key=lambda x:-len(x[0])) if l in('en','de') else rs
    f=f'content/{l}.json'; s=open(f).read()
    for a,b in rs:
        n=s.count(a); assert n>=1,(l,a); s=s.replace(a,b)
    open(f,'w').write(s); json.loads(s)
print('ok')
