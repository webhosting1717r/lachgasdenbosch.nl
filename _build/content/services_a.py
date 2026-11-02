# -*- coding: utf-8 -*-
# Servicepagina's (deel A) voor lachgasdenbosch.nl: wijzigen/annuleren, betalen, bezorgtijden, bezorgvoorwaarden, 18+, veilig bestellen, werkwijze, zakelijk.
# Schema: zie SCHEMA.md (SERVICE_PAGES). Pagina's komen op /<slug>/.

UPD = "november 2026"

SERVICE_PAGES = [
    {
        "slug": "bestelling-wijzigen-of-annuleren", "label": "Service",
        "title": "Bestelling wijzigen of annuleren | Lachgas Den Bosch",
        "description": "Adres, tijdstip of formaat aanpassen, of toch annuleren? Zo werkt dat bij Lachgas Den Bosch, tot wanneer het kan en wat er gebeurt als de bezorger al rijdt.",
        "h1": "Je bestelling wijzigen of annuleren",
        "lead": "Plannen veranderen, zeker op een feestavond. Zolang de bezorger niet is vertrokken, pas je je bestelling kosteloos aan in hetzelfde WhatsApp-gesprek; daarna kijken we wat nog kan.",
        "updated": UPD,
        "sections": [
            {"h2": "Tot wanneer wijzigen of annuleren kan", "paragraphs": [
                "Het ijkpunt is het moment waarop de bezorger vertrekt. Tot dat moment is je bestelling niet meer dan een afspraak in een gesprek: je kunt hem aanpassen of intrekken zonder uitleg en zonder kosten. We vragen alleen dat je het laat weten zodra je het zelf weet, zodat we geen tank voor niets klaarzetten en een ander adres in Den Bosch of Rosmalen niet onnodig op zijn beurt wacht. Een kort bericht volstaat; een reden hoef je er niet bij te geven.",
                "Is de bezorger eenmaal onderweg, dan ligt het anders. Hij rijdt dan met jouw tank naar jouw adres en heeft de rest van zijn ronde daarop ingepland. Annuleren of wijzigen gaat vanaf dat moment in overleg: we kijken wat praktisch nog haalbaar is en zeggen daar eerlijk iets over. Omdat je bij ons pas aan de deur betaalt, zit je nergens aan vast, maar we vragen wel om in het gesprek te blijven reageren tot er een nieuwe afspraak staat."]},
            {"h2": "Zo geef je een wijziging door", "paragraphs": [
                "Alles loopt via het WhatsApp-gesprek waarin je hebt besteld; dat gesprek blijft open tot de levering is afgerond. Begin geen nieuw gesprek en gebruik geen ander kanaal, want dan missen we de koppeling met je bestelling. Elke wijziging bevestigen we met een nieuw bericht met het aangepaste product, de aangepaste prijs en de verwachte tijd. Pas als je dat bericht hebt, is de wijziging definitief; een bericht van jouw kant alleen is dat nog niet. Schrijf daarom duidelijk op wat er verandert en wat hetzelfde blijft:"],
             "bullets": [
                "Adres wijzigen: stuur het volledige nieuwe adres met huisnummer, toevoeging en eventueel de verdieping. Ook op het nieuwe adres rekenen we meestal binnen 15 tot 25 minuten, gerekend vanaf het moment dat je de wijziging doorgeeft; meer daarover lees je bij <a href=\"/bezorgtijden-den-bosch/\">bezorgtijden in Den Bosch</a>.",
                "Tijdstip wijzigen: geef aan of je het eerder of later wilt. Later is bijna altijd mogelijk, eerder hangt af van de planning op dat moment.",
                "Formaat wijzigen: van 2KG naar 4KG of andersom kan tot vertrek zonder probleem, mits het formaat beschikbaar is. Een 10KG vraagt altijd apart overleg.",
                "Iets toevoegen of weglaten: slagroompatronen of een cracker erbij of eraf, zeg het en we bevestigen de bestelling opnieuw."]},
            {"h2": "Als de bezorger al onderweg is", "paragraphs": [
                "Een adreswijziging terwijl de bezorger rijdt, kan als het nieuwe adres op of vlak bij zijn route ligt; van de Maaspoort naar Den Bosch-Zuid is een andere kant van de stad en lukt niet altijd direct. Een ander formaat kan meestal niet meer, want de bezorger heeft alleen bij zich wat voor zijn ronde is ingepland. Een later tijdstip kan vaak wel, al betekent dat soms dat hij eerst een andere levering doet en daarna terugkomt. We zeggen in het gesprek eerlijk wat kan en wat niet.",
                "Annuleren terwijl de bezorger onderweg is, is vervelend voor beide kanten, maar het kan. De tank gaat mee terug en je betaalt niets, want betaling vindt alleen plaats bij overdracht. We vragen wel om het direct te melden en niet pas als er wordt aangebeld. Wie herhaaldelijk bestelt en bij aankomst niet thuis is of annuleert, kan daarna om een extra bevestiging vooraf worden gevraagd of niet meer worden bediend; dat beoordelen we per geval. Hoe de bezorger omgaat met niet thuis zijn, staat in de <a href=\"/bezorgvoorwaarden/\">bezorgvoorwaarden</a>."]},
            {"h2": "Als wij niet kunnen leveren", "paragraphs": [
                "Het komt voor dat wij een bevestigde bestelling toch niet kunnen uitvoeren: een carnavalsavond waarop de binnenstad van Oeteldonk nauwelijks bereikbaar is, een file op de A2 bij knooppunt Hintham die de hele planning laat schuiven, zware sneeuw of ijzel, of een formaat dat eerder op de avond uitverkocht raakt dan verwacht. In dat geval laten we het je zo snel mogelijk weten in het gesprek en bieden we een alternatief: een ander tijdstip, een ander formaat als dat voor jou werkt, of niets. Kies je voor niets, dan is de bestelling daarmee afgerond en betaal je niets; er zijn geen kosten voor een levering die niet heeft plaatsgevonden. Een vergoeding voor de vertraging bieden we niet, en een levertijd blijft bij ons altijd een indicatie met ‘meestal’."]},
        ],
        "note": "Wijzigen en annuleren is kosteloos zolang de bezorger niet is vertrokken. Daarna gaat het in overleg, maar je betaalt nooit voor een tank die niet is overhandigd.",
        "faq": [
            ["Ik heb besteld maar hoor niets meer. Is mijn bestelling nog actief?",
             "Een bestelling is pas een bestelling als je van ons een bevestiging hebt gekregen met wat je krijgt, wat het kost en wanneer we er ongeveer zijn. Heb je die niet, stuur dan een kort bericht in hetzelfde gesprek; zo staat alles op één plek. De stappen staan bij onze <a href=\"/werkwijze/\">werkwijze</a>."],
            ["Kan ik de bestelling laten bezorgen bij een vriend in plaats van bij mij?",
             "Ja, zolang je dat voor vertrek doorgeeft en de ontvanger daar 18 jaar of ouder is, zich kan legitimeren en betaalt. Het nieuwe adres moet een woonadres zijn, geen openbare plek; een bankje op de Parade of een parkeerplaats bij de Pettelaarse Schans telt dus niet."],
            ["Jullie konden niet leveren door het weer. Krijg ik korting op een volgende bestelling?",
             "Nee. We rekenen niets voor een levering die niet is doorgegaan en bieden ook geen compensatie; de levertijd is een indicatie en geen belofte. Een nieuwe bestelling plannen we graag opnieuw in hetzelfde gesprek, op een moment dat de wegen rond Den Bosch weer begaanbaar zijn."]],
        "related": ["/bezorgvoorwaarden/", "/werkwijze/"],
    },
    {
        "slug": "betalen-bij-levering", "label": "Betalen",
        "title": "Betalen bij levering: contant of Tikkie | Lachgas Den Bosch",
        "description": "Bij Lachgas Den Bosch betaal je pas aan de deur, contant of via Tikkie, tegen de prijs die vooraf in WhatsApp is bevestigd. Geen account, geen vooruitbetaling.",
        "h1": "Betalen bij levering",
        "lead": "Geen vooruitbetaling en geen account: je rekent pas af als de bestelling voor je staat, contant of via Tikkie, tegen het bedrag dat we vooraf in WhatsApp hebben bevestigd.",
        "updated": UPD,
        "sections": [
            {"h2": "Eerst bevestigen, dan pas betalen", "paragraphs": [
                "Zodra je bestelling binnenkomt, sturen we een bevestiging terug met het product, de prijs en de verwachte tijd. Dat bericht is je houvast: het bedrag dat daarin staat, is het bedrag dat je aan de deur betaalt. Komt er iets bij, bijvoorbeeld omdat je alsnog een doosje slagroompatronen wilt, dan bevestigen we dat opnieuw voordat de bezorger vertrekt. Zo weet je altijd vooraf waar je aan toe bent en hoeft er aan de deur niets meer besproken te worden behalve de overdracht zelf.",
                "Je hoeft nergens een account voor aan te maken, geen rekeningnummer te delen en niets vooruit over te maken. Dat geldt voor een enkele 2KG in een studentenhuis aan de Hinthamerstraat net zo goed als voor een grotere bestelling voor een tuinfeest in Rosmalen; ook dan wordt pas betaald als de tanks er daadwerkelijk zijn."]},
            {"h2": "Contant betalen", "paragraphs": [
                "Contant is de eenvoudigste manier. Leg het bedrag klaar dat in WhatsApp is bevestigd, liefst gepast, want de bezorger heeft beperkt wisselgeld bij zich. Grote biljetten kunnen we niet altijd wisselen; geef het vooraf aan als je daar alleen mee kunt betalen, dan houden we er rekening mee. De bezorger telt het bedrag na en daarmee is de overdracht afgerond. Een bedrag dat volledig uit kleingeld bestaat, is voor de bezorger lastig te tellen aan de deur; kies in dat geval liever voor Tikkie."]},
            {"h2": "Betalen via Tikkie", "paragraphs": [
                "Wil je liever geen contant geld gebruiken, dan stuurt de bezorger bij aankomst een Tikkie-betaalverzoek in het WhatsApp-gesprek dat je al met ons hebt. Je opent de link, betaalt via iDEAL met je eigen bankapp, en zodra de betaling bij ons zichtbaar is, krijg je de bestelling overhandigd. Dat duurt doorgaans minder dan een minuut. Je hebt er een Nederlandse bankrekening met iDEAL voor nodig en werkende mobiele data of wifi; valt dat weg, dan kun je altijd nog contant afrekenen."]},
            {"h2": "Wat niet kan", "paragraphs": [
                "Een paar dingen doen we bewust niet, omdat ze de overdracht aan de deur ingewikkelder of minder veilig maken. Krijg je vóór de levering een betaalverzoek dat niet uit ons eigen WhatsApp-gesprek komt, bijvoorbeeld via een ander nummer of een link in een sms, betaal dan niet en laat het ons weten. Wij vragen nooit om vooraf te betalen. Hoe de controle aan de deur gaat, staat bij <a href=\"/leeftijdscontrole-18-plus/\">leeftijdscontrole 18+</a>; hoe je nepaanbieders herkent, bij <a href=\"/veilig-bestellen-oplichting-herkennen/\">veilig bestellen</a>."],
             "bullets": [
                "Pinnen aan de deur: onze bezorgers hebben geen pinapparaat bij zich.",
                "Creditcard, PayPal of andere betaalapps: alleen contant of Tikkie.",
                "Op rekening of achteraf betalen: de bestelling wordt afgerekend op het moment van overhandigen.",
                "Vooruitbetalen of een aanbetaling: ook voor een 10KG of een grote bestelling niet.",
                "Betalen door een minderjarige: degene die afrekent en de bestelling aanneemt, is 18 jaar of ouder en kan dat aantonen."]},
        ],
        "note": "Wij vragen nooit om vooruitbetaling. Een betaalverzoek dat voor de levering binnenkomt en niet uit ons eigen gesprek komt, is niet van ons.",
        "faq": [
            ["Kan ik aan de deur pinnen?",
             "Nee, onze bezorgers hebben geen pinapparaat. Je betaalt contant of via een Tikkie-link die je in het WhatsApp-gesprek ontvangt en met iDEAL afrekent. Zorg dus dat je gepast geld in huis hebt of dat je bankapp werkt voordat de bezorger voor de deur staat."],
            ["Moet ik voor een grote bestelling of een 10KG tank een aanbetaling doen?",
             "Nee. Ook voor een <a href=\"/product/lachgas-tank-10kg/\">lachgastank 10KG</a> spreken we vooraf alles af in WhatsApp, maar het bedrag betaal je pas als de tank bij je staat. Vooruitbetaling of een borg vragen we nooit, ook niet voor een feest met meerdere tanks."],
            ["Krijg ik een bewijs van betaling?",
             "Bij Tikkie zie je de betaling direct in je bankapp en in de Tikkie-app. Betaal je contant, dan is het WhatsApp-gesprek met de bevestigde prijs je afspraak; vraag de bezorger of ons gerust om een korte bevestiging in datzelfde gesprek."]],
        "related": ["/lachgas-spoedbezorging/", "/werkwijze/"],
    },
    {
        "slug": "bezorgtijden-den-bosch", "label": "Bezorgtijden",
        "title": "Bezorgtijden lachgas in Den Bosch en omgeving",
        "description": "Hoe snel wordt lachgas bezorgd? In Den Bosch, Rosmalen en de hele regio meestal binnen 15 tot 25 minuten, met vooraf een tijdsindicatie via WhatsApp.",
        "h1": "Bezorgtijden in Den Bosch",
        "lead": "Eén indicatie voor het hele gebied: in Den Bosch, Rosmalen, de dorpen eromheen en de rest van de regio zijn we meestal binnen 15 tot 25 minuten bij je.",
        "updated": UPD,
        "sections": [
            {"h2": "Overal meestal binnen 15 tot 25 minuten", "paragraphs": [
                "Of je nu in de <a href=\"/bezorggebied/den-bosch-centrum/\">binnenstad</a> woont, in De Muntel, Hintham of de Maaspoort, in <a href=\"/bezorggebied/rosmalen/\">Rosmalen</a> of De Groote Wielen, in een dorp als Vught, Berlicum of Den Dungen, of verderop in Oss, Boxtel, Drunen of net over de Maas in Zaltbommel: we rekenen overal op meestal binnen 15 tot 25 minuten. We zorgen ervoor dat er doorgaans een bezorger in de buurt van je adres is, zodat je niet hoeft te puzzelen in welk deel van de regio je woont. Welke wijken en plaatsen we aandoen, zie je in het overzicht van ons <a href=\"/bezorggebied/\">bezorggebied</a>."]},
            {"h2": "Hoe je een tijdsindicatie krijgt", "paragraphs": [
                "Zodra je bericht binnen is, kijken we welke bezorger het dichtst bij je adres zit en hoe druk het op dat moment is. In ons antwoord staan de prijs en de verwachte aankomsttijd; pas als jij akkoord geeft, gaat de bezorger op weg. Die tijd is een realistische verwachting en geen exacte minuut. Komt er onderweg nog een update, dan zie je die gewoon in hetzelfde gesprek terug. Hoe de stappen van bericht tot voordeur precies lopen, lees je bij onze <a href=\"/werkwijze/\">werkwijze</a>."]},
            {"h2": "Wat de tijd kan beïnvloeden", "paragraphs": [
                "Meestal blijft het binnen 15 tot 25 minuten, maar soms duurt het iets langer. Op vrijdag- en zaterdagnacht tussen elf en drie, op feestdagen en tijdens carnaval in Oeteldonk, Koningsdag of het Bevrijdingsfestival op de Pettelaarse Schans komen er meer bestellingen binnen en zijn delen van de binnenstad afgesloten. Ook slecht weer, een file op de A2, de A59 of de A65 en wegwerkzaamheden op de Randweg kunnen een paar minuten kosten. In zulke gevallen melden we dat vooraf via WhatsApp met een nieuwe tijdsindicatie, zodat je zelf kunt kiezen of je wacht of een rustiger moment afspreekt. Vaste openingstijden hebben we niet: bestellen kan elke dag, ook laat, zoals beschreven bij <a href=\"/lachgas-nachtbezorging/\">bezorging ’s avonds en ’s nachts</a>."]},
            {"h2": "Zo gaat het zelf sneller", "paragraphs": [
                "Een compleet bericht scheelt de meeste tijd, want elke vraag die we nog terug moeten sturen, kost minuten. Een bezorger die meteen weet wat hij meeneemt en waar hij moet aanbellen, is eerder bij je dan een bezorger die onderweg nog moet wachten op een huisnummer of een verdieping. Dit helpt:"],
             "bullets": [
                "Noem het product en het formaat, bijvoorbeeld een lachgastank 2KG, een cracker of een doosje slagroompatronen.",
                "Zet het volledige afleveradres erbij, met huisnummer, toevoeging, verdieping en de naam op de bel.",
                "Geef aan of je nu thuis bent of op welk tijdstip het je beter uitkomt.",
                "Houd je telefoon bij de hand en zorg dat de bel werkt of dat iemand de portiekdeur kan openen.",
                "Houd een identiteitsbewijs klaar en betaal contant of via Tikkie, dan is de overdracht snel geregeld."]},
            {"h2": "Als het toch later wordt", "paragraphs": [
                "Merkt de bezorger onderweg dat hij later is dan verwacht, bijvoorbeeld door een afgesloten straat in de binnenstad of een ongeluk op de A2, dan krijg je een bericht met een nieuwe verwachting. Is de genoemde tijd voorbij en heb je niets gehoord, stuur dan een kort bericht in hetzelfde WhatsApp-gesprek; we kijken meteen waar de bezorger op dat moment is. Komt het je intussen niet meer uit, laat het ons dan zo snel mogelijk weten. Plan je een feest, dan kun je ook vooraf een tijdstip afspreken; ook dan blijft het een verwachting rond dat moment."]},
        ],
        "note": "Meestal binnen 15 tot 25 minuten is een indicatie voor een gewone dag. Op drukke momenten noemen we in WhatsApp een aangepaste verwachting voordat de bezorger vertrekt.",
        "faq": [
            ["Hebben jullie vaste openingstijden?",
             "Nee. We zijn elke dag van de week bereikbaar via WhatsApp en bezorgen ook ’s nachts. De verwachte tijd die je bij je bestelling krijgt, is afgestemd op het moment van de dag en op hoe druk het dan is in Den Bosch en de regio."],
            ["Wat als ik in een appartementencomplex woon?",
             "Zet de naam op de bel, het huisnummer en de verdieping in je bericht, en laat weten of de portiekdeur op slot zit. Bij een flat in de <a href=\"/bezorggebied/maaspoort/\">Maaspoort</a> of een appartement in het Paleiskwartier scheelt het minuten als je zelf even naar beneden komt of de deur opent zodra de bezorger belt."],
            ["Kan ik een vast tijdstip afspreken?",
             "Ja. Geef in je bericht de dag en de tijd door, dan plannen we de levering daarop in. Houd er rekening mee dat ook een afgesproken tijd een verwachting is; we komen zo dicht mogelijk bij dat moment en melden het in het gesprek als het verschuift."]],
        "related": ["/lachgas-spoedbezorging/", "/lachgas-nachtbezorging/", "/lachgas-feestdagen/"],
    },
    {
        "slug": "bezorgvoorwaarden", "label": "Service",
        "title": "Bezorgvoorwaarden van Lachgas Den Bosch",
        "description": "Waar we wel en niet bezorgen, wanneer de bezorger een levering weigert en wat er aan de deur gebeurt: de bezorgvoorwaarden van Lachgas Den Bosch op één pagina.",
        "h1": "Bezorgvoorwaarden en huisregels van de bezorging",
        "lead": "Een levering aan de deur verloopt het prettigst als beide kanten weten wat er wordt verwacht. Dit zijn de voorwaarden waaronder onze bezorgers in Den Bosch en omgeving rijden.",
        "updated": UPD,
        "sections": [
            {"h2": "Alleen op een huisadres", "paragraphs": [
                "We bezorgen uitsluitend op een woonadres of op een besloten adres dat vooraf in WhatsApp is afgesproken: een huis, een appartement, een studentenkamer, een gehuurde zaal met eigen ingang. De bezorger komt naar een voordeur waar hij kan aanbellen en waar de ontvanger naar buiten komt. Niet op de lijst staat de openbare ruimte in al haar vormen: een straathoek, een parkeerplaats bij de Pettelaarse Schans, een bankje in het Zuiderpark, een tankstation langs de A2, een perron op station ’s-Hertogenbosch of de stoep voor een supermarkt.",
                "Ook evenemententerreinen vallen buiten de bezorging. Een festivalweide, een carnavalsplein, een afgezet terrein tijdens Theaterfestival Boulevard of een camping zonder vast adres zijn geen afleverpunten, ook niet als je ons naar de ingang laat komen. Dat heeft een praktische reden, want zo’n overdracht is voor niemand veilig of controleerbaar, en een juridische: lachgas staat op lijst II van de Opiumwet en gemeenten kunnen in de APV gebieden aanwijzen waar extra regels gelden. Zie <a href=\"/lachgas-informatie/lachgas-regels-den-bosch/\">lachgasregels in Den Bosch</a> voor de achtergrond."]},
            {"h2": "Legitimatie en het recht om te weigeren", "paragraphs": [
                "Elke ontvanger is 18 jaar of ouder en kan dat aantonen met een geldig identiteitsbewijs; welke documenten we accepteren staat bij <a href=\"/leeftijdscontrole-18-plus/\">leeftijdscontrole 18+</a>. Daarnaast heeft de bezorger altijd het laatste woord. Hij beoordeelt de situatie aan de deur en mag de levering weigeren zonder dat daar discussie over mogelijk is. Een geweigerde tank gaat terug in de auto. We bespreken daarna in het gesprek of en wanneer een nieuwe poging zinvol is; bij een weigering wegens leeftijd of identiteit is dat niet het geval. Weigeren gebeurt in ieder geval in deze situaties:"],
             "bullets": [
                "De ontvanger is of lijkt minderjarig, of er zijn duidelijk minderjarigen aanwezig voor wie de bestelling bedoeld lijkt.",
                "Er is twijfel over de identiteit: het document hoort niet bij de persoon, is verlopen of wordt alleen als foto op een telefoon getoond.",
                "De situatie is onveilig voor de bezorger: agressie, een groep die zich rond de auto verzamelt, een onverlichte of onoverzichtelijke plek.",
                "De ontvanger is zichtbaar sterk onder invloed van alcohol of andere middelen.",
                "Het afleveradres blijkt toch een openbare plek of een evenemententerrein te zijn."]},
            {"h2": "Aan de deur: wachten, betalen en verzegeling", "paragraphs": [
                "De bezorger meldt zich in het WhatsApp-gesprek als hij er is en belt aan. Hij wacht een paar minuten, niet langer; wie niet opendoet en niet reageert in het gesprek, treft een bezorger die weer vertrokken is. De tank gaat dan mee terug en we plannen opnieuw, en bij herhaling behouden we ons het recht voor om een adres niet meer te bedienen. Zorg dus dat je telefoon aanstaat, dat de bel werkt en dat je bij een appartement de verdieping en de naam op de bel hebt doorgegeven.",
                "Betaling vindt plaats bij de overdracht, contant of via Tikkie, tegen de prijs die vooraf is bevestigd; de details staan bij <a href=\"/betalen-bij-levering/\">betalen bij levering</a>. Voordat je betaalt, controleer je samen met de bezorger dat de verzegeling van de tank intact is. Een tank waarvan de verzegeling beschadigd is, hoef je niet aan te nemen; de bezorger neemt hem dan mee terug en we lossen het op. Zodra het bedrag is ontvangen en de tank is overhandigd, is de levering afgerond."]},
            {"h2": "Na de levering: bewaren en de lege tank", "paragraphs": [
                "Vanaf de overdracht ben jij verantwoordelijk voor de tank. Bewaar hem staand, koel en buiten bereik van kinderen; de aandachtspunten staan bij <a href=\"/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/\">bewaren en vervoeren</a>. Een lege tank is een stalen drukhouder met restdruk en hoort niet bij het huisvuil, niet in de container van het complex en niet op straat. Vraag ons in het gesprek of we hem bij een volgende levering meenemen, of lees hoe je hem zelf kwijtraakt bij <a href=\"/lachgas-informatie/lege-lachgastank-inleveren-den-bosch/\">een lege tank inleveren in Den Bosch</a>. Voor een 10KG maken we daar altijd vooraf afspraken over."]},
        ],
        "note": "De bezorger beoordeelt de situatie aan de deur en mag altijd weigeren. Een geweigerde of niet aangenomen levering gaat mee terug; daarover gaan we niet in discussie op straat.",
        "faq": [
            ["Kan de bezorger de tank bij de buren of in de schuur achterlaten?",
             "Nee. De tank wordt alleen overhandigd aan de persoon die zich legitimeert en betaalt. Achterlaten zonder overdracht, bij buren, in een portiek of achter een poort, doen we nooit; ook niet als je dat vooraf in het gesprek vraagt of als het om een herhaalbestelling gaat."],
            ["Ik woon in een studentenhuis zonder werkende bel. Hoe gaat dat?",
             "Geef dat vooraf door in het gesprek. De bezorger stuurt een bericht zodra hij voor de deur staat; reageer je niet binnen een paar minuten, dan vertrekt hij weer. Meer hierover bij <a href=\"/lachgas-studenten-den-bosch/\">lachgas voor studentenhuizen in Den Bosch</a>."],
            ["Wat als de verzegeling bij aankomst beschadigd is?",
             "Neem de tank dan niet aan en wijs de bezorger erop. Hij neemt hem weer mee en we zoeken in het gesprek naar een oplossing, meestal een nieuwe tank zo snel als de planning toelaat. Je betaalt niets voor een tank die je niet hebt aangenomen."]],
        "related": ["/leeftijdscontrole-18-plus/", "/bestelling-wijzigen-of-annuleren/"],
    },
    {
        "slug": "leeftijdscontrole-18-plus", "label": "18+",
        "title": "Leeftijdscontrole 18+ bij Lachgas Den Bosch",
        "description": "Lachgas Den Bosch levert alleen aan volwassenen. Zo werkt de leeftijdscontrole aan de deur, deze documenten gelden en dit gebeurt zonder geldig document.",
        "h1": "Leeftijdscontrole: alleen voor 18 jaar en ouder",
        "lead": "Een bestelling wisselt pas van hand als duidelijk is dat de ontvanger volwassen is. Zo werkt de controle aan de deur, en zo zorg je dat die in een paar seconden klaar is.",
        "updated": UPD,
        "sections": [
            {"h2": "Waarom we bij 18 een harde grens trekken", "paragraphs": [
                "Lachgas is geen product voor jongeren. Instanties als het Trimbos-instituut wijzen erop dat jongeren extra kwetsbaar zijn voor de effecten van lachgas, onder meer voor het zenuwstelsel en door het effect op vitamine B12. Daarnaast is verkoop aan minderjarigen in Nederland verboden. Wij hebben daar zelf nog iets aan toegevoegd: we leveren niet aan minderjarigen, ook niet als een volwassene bestelt en een jongere de deur opent, en we laten een bestelling liever terugkomen dan dat we een inschatting maken op gevoel. Meer achtergrond vind je bij <a href=\"https://www.trimbos.nl\">trimbos.nl</a> en in ons artikel over <a href=\"/lachgas-informatie/lachgas-en-vitamine-b12/\">lachgas en vitamine B12</a>."]},
            {"h2": "Welke legitimatie geldt", "paragraphs": [
                "De bezorger kijkt naar een officieel document met pasfoto en geboortedatum. Niet voldoende zijn een schoolpas, een collegekaart van Avans of de HAS, een OV-chipkaart, een bankpas, een foto van een document op je telefoon of een identiteitsbewijs van iemand anders. Een kopie of een screenshot via WhatsApp telt ook niet: het document moet aan de deur getoond worden door de persoon die de bestelling aanneemt. Let ook op de geldigheidsdatum: een verlopen paspoort of identiteitskaart accepteren we niet. Dit accepteren we wel:"],
             "bullets": [
                "Een paspoort, Nederlands of buitenlands.",
                "Een Nederlandse identiteitskaart of een identiteitskaart uit een ander EU-land.",
                "Een rijbewijs.",
                "Een verblijfsdocument of vreemdelingendocument met foto en geboortedatum."]},
            {"h2": "Zo gaat de controle aan de deur", "paragraphs": [
                "De bezorger vraagt om legitimatie zodra er twijfel is over de leeftijd, en bij wie er jong uitziet is die twijfel er bijna altijd. Voel je dus niet aangesproken als de vraag komt; het is de standaardgang van zaken, in een studentenhuis in de binnenstad net zo goed als bij een gezinswoning in Rosmalen. De bezorger kijkt naar de foto en de geboortedatum, geeft het document terug en rondt de overdracht af. We maken geen kopie, geen foto en geen notitie van je documentnummer; wat we over je bewaren, staat in ons <a href=\"/privacy/\">privacybeleid</a>. Leg je legitimatie klaar naast je betaalmiddel, dan is het in één handeling gebeurd."]},
            {"h2": "Zonder geldig document geen levering", "paragraphs": [
                "Kan de ontvanger geen geldig identiteitsbewijs laten zien, dan neemt de bezorger de bestelling mee terug. Dat geldt ook als de bestelling al is bevestigd, als je zegt dat je het document binnen kunt ophalen maar het niet vindt, of als een volwassene telefonisch bevestigt dat het goed is. Is er een volwassen huisgenoot die zich wel kan legitimeren en de bestelling aanneemt en betaalt, dan kan de levering alsnog doorgaan. Ziet de bezorger aan de deur duidelijk dat er minderjarigen aanwezig zijn voor wie de bestelling bedoeld lijkt, dan kan hij ook dan besluiten niet te leveren. Bestel daarom alleen als je zeker weet dat er op het moment van levering iemand van 18 of ouder met legitimatie thuis is."]},
        ],
        "note": "Geen geldig identiteitsbewijs betekent geen levering, ook niet als de bestelling al onderweg is. Dat is geen wantrouwen, maar de enige manier om een leeftijdsgrens serieus te nemen.",
        "faq": [
            ["Ik ben 18, maar mijn identiteitsbewijs ligt ergens anders. Kan iemand anders zich legitimeren?",
             "Ja, als die persoon zelf 18 jaar of ouder is, de bestelling aanneemt en betaalt. De controle gaat over de ontvanger aan de deur, niet over degene die het bericht stuurde. Hoe dat verder gaat, staat in de <a href=\"/bezorgvoorwaarden/\">bezorgvoorwaarden</a>."],
            ["Accepteren jullie een buitenlands paspoort of een identiteitskaart uit een ander EU-land?",
             "Ja. Elk officieel document met pasfoto en geboortedatum is goed, ook uit een ander land; voor internationale studenten in Den Bosch is dat vaak het paspoort. Alleen kopieën, foto’s op een telefoon en passen zonder geboortedatum accepteren we niet."],
            ["Slaan jullie mijn gegevens op na de controle?",
             "Nee. De bezorger kijkt alleen naar de foto en de geboortedatum en geeft het document direct terug. Er wordt niets gekopieerd of genoteerd; wat we wel bewaren, lees je in ons <a href=\"/privacy/\">privacybeleid</a>."]],
        "related": ["/lachgas-studenten-den-bosch/", "/betalen-bij-levering/", "/lachgas-informatie/is-lachgas-legaal-in-nederland/"],
    },
    {
        "slug": "veilig-bestellen-oplichting-herkennen", "label": "Service",
        "title": "Veilig bestellen: oplichting herkennen | Lachgas Den Bosch",
        "description": "Nepaccounts en kopieën van sites vragen om vooruitbetaling en leveren niets. Zo herken je het echte nummer van Lachgas Den Bosch en dit doe je na oplichting.",
        "h1": "Veilig bestellen en oplichting herkennen",
        "lead": "Rond lachgasbezorging zijn nepaanbieders actief die alleen op je aanbetaling uit zijn. Wij vragen nooit om vooruit te betalen; dit is hoe je het echte Lachgas Den Bosch herkent.",
        "updated": UPD,
        "sections": [
            {"h2": "Eén nummer, en je vindt het alleen via deze site", "paragraphs": [
                "We hebben één WhatsApp-nummer en dat zit achter de WhatsApp-knop op deze website, lachgasdenbosch.nl. Dat is de enige plek waar we het publiceren. Een nummer dat je via een advertentie, een Snapchat- of Telegram-account, een Instagram-profiel of een doorgestuurd berichtje krijgt, is niet van ons, ook niet als onze naam, teksten of foto’s erbij staan. Twijfel je, open dan zelf de site via de adresbalk en gebruik de knop; klik niet op een link die iemand je stuurt.",
                "Let bij een site op het adres in de adresbalk. Kopieën gebruiken een net iets ander domein, een extra woord of een andere extensie, en zien er soms identiek uit omdat ze onze pagina’s hebben overgenomen. Een echte bestelling bij ons begint met een bericht van jouw kant in WhatsApp, gevolgd door een bevestiging met product, prijs en verwachte tijd; zie onze <a href=\"/werkwijze/\">werkwijze</a>."]},
            {"h2": "Nooit vooruitbetalen, nooit een betaallink vooraf", "paragraphs": [
                "De eenvoudigste regel om oplichting te herkennen: wie vooraf geld wil, is niet Lachgas Den Bosch. Wij vragen geen aanbetaling, geen borg, geen reserveringskosten en geen bedrag om ‘je bestelling vast te leggen’. Er komt vooraf geen Tikkie, geen iDEAL-link en geen vraag om iets over te maken naar een rekeningnummer. Betaald wordt pas aan de deur, als de verzegelde tank voor je staat en de legitimatie is bekeken; zie <a href=\"/betalen-bij-levering/\">betalen bij levering</a>. Vraagt iemand om cadeaukaarten of cryptovaluta, dan is de zaak daarmee beslist."]},
            {"h2": "Hoe nepaccounts en kopieën werken", "paragraphs": [
                "Het patroon is bijna altijd hetzelfde. Een account op sociale media of een advertentiesite adverteert met een snelle levering en een prijs die te mooi is om waar te zijn, vaak laat op de avond wanneer je weinig zin hebt om te vergelijken. Na je bericht volgt een vriendelijke bevestiging, en dan het verzoek om vooruit te betalen, met een reden die haast suggereert: de bezorger staat al klaar, het is de laatste tank. Na de betaling komt er niets, of een nieuw verzoek om nog een bedrag over te maken omdat er iets zou zijn misgegaan.",
                "Kopieën van websites werken daar aanvullend op. Ze nemen teksten, foto’s en soms een plaatsnaam in het domein over, zetten er een eigen nummer bij en vangen zo mensen die via een zoekmachine binnenkomen. Ook gemonteerde ‘bewijzen’ van leveringen in Den Bosch of Rosmalen komen voor. Het enige wat telt, is of er vooraf om geld wordt gevraagd en of het nummer van deze site komt."]},
            {"h2": "Toch opgelicht? Dit doe je", "paragraphs": [
                "Schaam je er niet voor: deze vorm van oplichting is gemaakt om in een haastig moment te werken, en treft studenten en feestgangers in Den Bosch net zo goed als ieder ander. Laat het ons ook weten via de echte WhatsApp-knop als iemand onze naam gebruikt, dan kunnen we anderen waarschuwen. Ben je toch geld kwijt, handel dan snel en in deze volgorde:"],
             "bullets": [
                "Neem direct contact op met je bank. Bij een iDEAL- of Tikkie-betaling is het geld meestal al overgeboekt, maar de bank kan soms een terugvordering proberen en de ontvangende rekening melden.",
                "Doe aangifte bij de politie, online of op een bureau, met screenshots van het gesprek, de advertentie, het nummer en het betaalbewijs.",
                "Meld de oplichting bij de Fraudehelpdesk, die meldingen bundelt en waarschuwt voor lopende vormen van fraude.",
                "Meld het account of de advertentie bij het platform waar je het aantrof, en waarschuw de mensen met wie je de link hebt gedeeld."]},
            {"h2": "Onze eigen waarborgen", "paragraphs": [
                "Wat wij doen om bestellen controleerbaar te houden, is bewust eenvoudig. Je ontvangt vóór vertrek een bevestiging van formaat, prijs en verwacht tijdstip in het gesprek dat je zelf hebt geopend. De tank komt verzegeld aan en je controleert dat samen met de bezorger voordat je betaalt, contant of via Tikkie; het betaalverzoek sturen we pas aan de deur in datzelfde gesprek. Je hoeft geen account aan te maken en we bewaren niet meer dan in ons <a href=\"/privacy/\">privacybeleid</a> staat. En we leveren alleen aan 18-plussers na <a href=\"/leeftijdscontrole-18-plus/\">leeftijdscontrole</a>; een aanbieder die daar niet naar vraagt, neemt het ook met de rest niet zo nauw."]},
        ],
        "note": "Wij vragen nooit om vooruitbetaling en publiceren ons WhatsApp-nummer uitsluitend op deze site. Elk ander nummer en elk betaalverzoek vooraf is niet van ons.",
        "faq": [
            ["Iemand met jullie naam vraagt om een aanbetaling via Tikkie. Is dat echt?",
             "Nee. Wij sturen nooit een betaalverzoek vóór de levering; een Tikkie krijg je alleen aan de deur, in het gesprek dat je zelf via de site hebt geopend. Betaal niet, blokkeer het nummer en laat het ons weten via de WhatsApp-knop op deze pagina."],
            ["Hoe weet ik zeker dat ik op de echte site zit?",
             "Controleer het adres in de adresbalk en typ lachgasdenbosch.nl bij twijfel zelf in. Gebruik de WhatsApp-knop op de pagina en geen nummer uit een advertentie, een story of een doorgestuurd bericht; hoe een echte bestelling verloopt, staat bij onze <a href=\"/werkwijze/\">werkwijze</a>."],
            ["Ik ben opgelicht door een onbekend nummer. Waar meld ik dat?",
             "Neem eerst contact op met je bank, doe aangifte bij de politie en meld het bij de Fraudehelpdesk. Bewaar screenshots van het gesprek, de advertentie en het betaalbewijs; daarmee kunnen bank en politie het meest. Heeft iemand onze naam gebruikt, laat het ons dan ook weten."]],
        "related": ["/betalen-bij-levering/", "/werkwijze/"],
    },
    {
        "slug": "werkwijze", "label": "Werkwijze",
        "title": "Werkwijze: lachgas bestellen in Den Bosch in 3 stappen",
        "description": "Zo bestel je bij Lachgas Den Bosch: één WhatsApp-bericht, een bevestiging met prijs en verwachte tijd, en een discrete levering aan de deur. Alleen voor 18+.",
        "h1": "Zo werkt bestellen bij Lachgas Den Bosch",
        "lead": "Drie stappen, geen account en geen webshop: je appt, wij bevestigen en de bezorger komt. Hieronder staat precies wat er in elke stap gebeurt en wat wij van jou nodig hebben.",
        "updated": UPD,
        "sections": [
            {"h2": "Stap 1: stuur een WhatsApp-bericht", "paragraphs": [
                "Alles begint met één bericht. Daarin zet je welk product je wilt en hoeveel, bijvoorbeeld een lachgastank 2KG of een cracker met een doosje patronen, het volledige afleveradres met huisnummer, toevoeging en de naam op de bel, en wanneer je het wilt hebben: nu, later op de dag of op een andere dag. Weet je nog niet welk formaat past, kijk dan eerst in ons <a href=\"/assortiment/\">assortiment</a> of stel de vraag gewoon in hetzelfde bericht; we denken mee zonder dat je iets hoeft vast te leggen. Bestellen kan elke dag, ook ’s avonds laat en in het weekend."]},
            {"h2": "Stap 2: bevestiging met prijs en verwachte tijd", "paragraphs": [
                "Wij antwoorden met een bevestiging waarin het product, de prijs en de verwachte levertijd staan. In Den Bosch, Rosmalen en de rest van de regio is dat meestal binnen 15 tot 25 minuten; wat die tijd kan beïnvloeden, staat bij <a href=\"/bezorgtijden-den-bosch/\">bezorgtijden</a>. Pas na jouw akkoord gaat de bestelling naar een bezorger. Is een product op dat moment niet beschikbaar, dan stellen we een alternatief voor in plaats van zonder overleg iets anders mee te geven. De prijs in dat bericht is het bedrag dat je aan de deur betaalt.",
                "Wil je op een later moment geleverd krijgen, zeg dat dan in dit stadium; we zetten de levering dan in de planning en sturen op de dag zelf een berichtje als de bezorger vertrekt. Dat werkt ook voor een feest in het weekend of een verjaardag waarvan je de datum al weet: hoe eerder we het weten, hoe makkelijker we een rustig moment voor je kunnen aanhouden."]},
            {"h2": "Stap 3: levering aan de deur", "paragraphs": [
                "De bezorger komt in een gewone auto en in gewone kleding naar je voordeur, niet naar een parkeerplaats of een straathoek. Hij vraagt bij twijfel over de leeftijd om een identiteitsbewijs, je controleert samen dat de verzegeling van de tank intact is, en je betaalt contant of via een Tikkie-link in het WhatsApp-gesprek. Daarna is de overdracht klaar. Woon je in een appartement in het Paleiskwartier of een studentenhuis in de binnenstad, geef dan de verdieping en de bel door, zodat de bezorger niet hoeft te zoeken. Wat er precies gebeurt bij die controle en bij het betalen, lees je bij <a href=\"/leeftijdscontrole-18-plus/\">leeftijdscontrole 18+</a> en <a href=\"/betalen-bij-levering/\">betalen bij levering</a>."]},
            {"h2": "Na de levering", "paragraphs": [
                "Bewaar de tank staand, koel en buiten bereik van kinderen, weg van warmtebronnen; de rest van de aandachtspunten staat bij <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a>. Is de tank leeg, zet hem dan niet bij het huisvuil; er zit restdruk in. Vraag ons via WhatsApp of we hem bij een volgende levering meenemen, of lees hoe je hem kwijtraakt bij <a href=\"/lachgas-informatie/lege-lachgastank-inleveren-den-bosch/\">een lege tank inleveren</a>. Heb je na de levering nog een vraag, dan stel je die gewoon in hetzelfde gesprek; dat blijft open. Een volgende bestelling gaat nog sneller: je adres staat al in het gesprek, dus een kort berichtje is genoeg."]},
        ],
        "note": "Wij bezorgen alleen op een woonadres of een vooraf afgesproken privéadres, uitsluitend aan 18-plussers en alleen tegen de prijs die in het gesprek is bevestigd.",
        "faq": [
            ["Moet ik een account aanmaken of een app installeren?",
             "Nee. Alles loopt via WhatsApp, dat je waarschijnlijk al hebt. Je hoeft geen profiel aan te maken, geen formulier in te vullen en geen betaalgegevens achter te laten; je betaalt pas aan de deur, zoals beschreven bij <a href=\"/betalen-bij-levering/\">betalen bij levering</a>."],
            ["Kan ik mijn bestelling nog aanpassen nadat ik heb besteld?",
             "Tot de bezorger vertrekt kun je alles wijzigen in hetzelfde gesprek; we bevestigen de aanpassing dan opnieuw. Is hij al onderweg, dan is een ander formaat niet altijd meer mogelijk, maar vraag het gerust. De regels staan bij <a href=\"/bestelling-wijzigen-of-annuleren/\">wijzigen of annuleren</a>."],
            ["Wat gebeurt er als er niemand thuis is als de bezorger aankomt?",
             "De bezorger stuurt een bericht en wacht kort. Komt er geen volwassene met legitimatie aan de deur, dan gaat de bestelling mee terug en spreken we een nieuw moment af. Zonder ontvanger laten we nooit iets achter, ook niet bij de buren of in een portiek."]],
        "related": ["/betalen-bij-levering/", "/leeftijdscontrole-18-plus/", "/bezorgtijden-den-bosch/"],
    },
    {
        "slug": "zakelijk-bestellen", "label": "Zakelijk",
        "title": "Zakelijk lachgas bestellen in Den Bosch: horeca en evenementen",
        "description": "Horeca, evenementenbureau of vereniging in Den Bosch? Zo bestel je zakelijk bij Lachgas Den Bosch: afstemming via WhatsApp, contactpersoon 18+, eigen adres.",
        "h1": "Zakelijk bestellen bij Lachgas Den Bosch",
        "lead": "Horeca, evenementenbureaus, verenigingen en andere organisaties in Den Bosch en omgeving bestellen bij ons met afspraken vooraf, een vaste contactpersoon en levering bij de zaak.",
        "updated": UPD,
        "sections": [
            {"h2": "Voor wie zakelijk bestellen bedoeld is", "paragraphs": [
                "Een café aan de Parade of in de Korte Putstraat dat slagroompatronen nodig heeft voor de keuken, een evenementenbureau dat een besloten bedrijfsfeest in een gehuurde loods op De Brand voorbereidt, een studentenvereniging bij Avans, de HAS of het Koning Willem I College met een eigen sociëteit, een carnavalsvereniging in Oeteldonk met een besloten avond, een cateraar in Vught of Rosmalen: de aanvragen die we zakelijk krijgen, lopen sterk uiteen. Wat ze gemeen hebben is dat een organisatie bestelt en niet een persoon, dat er meer afstemming nodig is dan bij een losse levering op een woonadres, en dat iemand van de zaak de bestelling op een vast adres aanneemt.",
                "Zakelijk bestellen is bij ons geen apart loket met andere regels. Dezelfde uitgangspunten gelden als voor elke andere bestelling: alleen aan volwassenen, verzegeld geleverd, betaling bij overdracht en een prijs die vooraf in WhatsApp is bevestigd. Het verschil zit in de voorbereiding: hoe eerder we weten wat je nodig hebt en waar, hoe beter we een tijdvenster kunnen aanhouden dat bij jouw planning past."]},
            {"h2": "Wat wij van je nodig hebben", "paragraphs": [
                "Vermeld in je eerste bericht om welke gelegenheid het gaat en welke producten je in gedachten hebt, van <a href=\"/product/slagroompatronen/\">slagroompatronen</a> tot een <a href=\"/product/lachgas-tank-4kg/\">lachgastank 4KG</a>. Dan kunnen we direct meedenken over wat zinvol is voor jouw situatie en wat niet. Om een zakelijke aanvraag te kunnen beoordelen, vragen we daarnaast om drie dingen:"],
             "bullets": [
                "Een contactpersoon van 18 jaar of ouder die de bestelling aanneemt, zich aan de deur kan legitimeren en bereikbaar blijft in het WhatsApp-gesprek tot de overdracht is afgerond.",
                "Een afleveradres van de zaak of de locatie, met een duidelijke ingang: de keukendeur, de artiesteningang, het clubgebouw. Een postbus, een festivalweide of een parkeerterrein kunnen we niet gebruiken.",
                "Een tijdvenster waarin die contactpersoon aanwezig is. Voor horeca is dat vaak buiten de piekuren; voor een evenement is dat tijdens de opbouw, niet tijdens het programma."]},
            {"h2": "Afstemmen vooraf via WhatsApp", "paragraphs": [
                "Alle zakelijke afspraken lopen via hetzelfde WhatsApp-gesprek dat ook particuliere klanten gebruiken; je vindt de knop op elke pagina van deze site. Dat gesprek is tegelijk je dossier: wat daar is bevestigd, geldt. We leggen daarin het product, de prijs, het adres, het tijdvenster en de naam van de contactpersoon vast. Voor een eenmalige levering is een paar uur vooruit vaak voldoende; voor een evenement met opbouw, meerdere locaties of een groter formaat rekenen we liever op een paar dagen.",
                "Grotere formaten, zoals de <a href=\"/product/lachgas-tank-10kg/\">lachgastank 10KG</a>, leveren we uitsluitend in overleg, met afspraken over de plek waar de tank komt te staan en over het ophalen van de lege tank. Vragen over facturatie, terugkerende leveringen of andere administratieve wensen bespreken we per geval; we beloven daar vooraf niets over, maar denken wel mee."]},
            {"h2": "Jouw verantwoordelijkheid als organisatie", "paragraphs": [
                "Wij leveren een product aan een volwassene op een afgesproken adres. Wat er daarna in jouw zaak of op jouw evenement gebeurt, valt onder jouw verantwoordelijkheid als ondernemer of bestuur. Lachgas staat sinds 1 januari 2023 op lijst II van de Opiumwet; handel voor recreatief gebruik is verboden, met uitzonderingen voor onder meer de voedingsindustrie. Hoe die uitzondering is afgebakend, lees je op <a href=\"https://www.rijksoverheid.nl\">rijksoverheid.nl</a>. Daarbovenop gelden gemeentelijke regels: de APV van ’s-Hertogenbosch kan gebieden aanwijzen en eisen stellen rond evenementen, en elke andere gemeente in de regio heeft een eigen verordening.",
                "Als zaak bepaal je zelf je huisregels en ben je het aanspreekpunt voor de gemeente, de handhaving en je gasten. Controleer daarom voor een evenement bij de gemeente wat je vergunning toestaat en wat niet, zeker in de aanloop naar carnaval, de kermis of een festival. Een overzicht van de verschillende lagen regels staat in ons artikel over <a href=\"/lachgas-informatie/lachgas-regels-den-bosch/\">lachgasregels in Den Bosch</a>."]},
            {"h2": "Culinair gebruik in de keuken", "paragraphs": [
                "Voor restaurants, lunchrooms, ijssalons en cateraars is de toepassing meestal culinair: slagroompatronen voor een slagroomspuit, of lachgas als drijfgas voor espuma’s en luchtige sauzen. Dat is de toepassing waarvoor het gas al lang in professionele keukens wordt gebruikt en waarvoor de wet een uitzondering kent. Welke verpakking bij jouw keuken past, hangt af van het volume en je apparatuur; de opties staan in ons <a href=\"/assortiment/\">assortiment</a>. Bewaar patronen en tanks koel, staand en buiten bereik van gasten."]},
        ],
        "note": "Zakelijk bestellen verandert niets aan onze basisregels: alleen aan 18-plussers met legitimatie, verzegeld, en betaald bij overdracht. Wat jouw zaak met de producten doet, blijft jouw verantwoordelijkheid.",
        "faq": [
            ["Kunnen jullie op een festivalterrein of een buitenevenement leveren?",
             "Nee. We leveren op het adres van de zaak of op een besloten, vooraf afgesproken locatie met een deur en een contactpersoon. Een festivalterrein, de Parade tijdens een evenement, een parkeerplaats of de openbare weg komt daar niet voor in aanmerking; lees de <a href=\"/bezorgvoorwaarden/\">bezorgvoorwaarden</a>."],
            ["Kan ik op rekening bestellen of een factuur krijgen?",
             "Dat bespreken we per geval in het WhatsApp-gesprek. Standaard betaal je bij overdracht, contant of via Tikkie; andere afspraken maken we alleen in overleg en bevestigen we vooraf in datzelfde gesprek, zodat beide kanten weten waar ze aan toe zijn."],
            ["Hoe lang van tevoren moet een evenementenbureau bestellen?",
             "Voor een enkele levering op een vast adres is een paar uur meestal genoeg. Gaat het om een evenement met opbouw, een groter formaat of meerdere adressen, dan plannen we liever een paar dagen vooruit, zodat tijdvenster en contactpersoon vastliggen."]],
        "related": ["/lachgas-feest-evenement/", "/lachgas-informatie/lachgas-regels-den-bosch/"],
    },
]
