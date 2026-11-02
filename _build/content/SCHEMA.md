# Contentschema's voor de stads-generator (_build) van lachgasdenbosch.nl
Alle contentmodules zijn Python-bestanden in _build/content/ met hoofdletter-variabelen. build.py laadt alle *.py (behalve _*.py) en verzamelt per naam.
Teksten zijn gewone strings; inline links schrijf je als `<a href="/pad/">tekst</a>` (de renderer zet daar zelf de Tailwind-klassen op). Geen andere HTML in teksten behalve <a>, <strong>, <em>.

## AREAS (lijst van dicts, één per plaats; bestand areas_*.py)
slug, name, kind ("wijk" | "dorp" | "stad"), group (groep-slug uit BRIEF), gemeente,
title (40-60 tekens, "Lachgas <Naam> | Lachgas Den Bosch" of "Lachgas bestellen <Naam> | Bezorgd via WhatsApp"),
description (110-160 tekens, bevat "meestal binnen 15 tot 25 minuten", eindigt op "18+."),
h1 ("Lachgas <Naam>" zoals Breda, bijv. "Lachgas Rosmalen" / "Lachgas Binnenstad Den Bosch"),
lead (1 zin, bijv. "Snel en discreet bezorgd in Rosmalen, besteld via WhatsApp."),
intro (lijst van precies 3 alinea's van 80-140 woorden: 1 = ligging, buurten/straten, hoe de bezorger er komt; 2 = voor welke gelegenheden, bestellen via WhatsApp met adres, geen afhaalpunt; 3 = "Je kiest uit een Lachgastank 2KG, 4KG of op aanvraag 10KG, aangevuld met lachgas crackers en slagroompatronen", verzegeld, 18+, contant of Tikkie, met één interne link naar /lachgas-informatie/welke-lachgastank-heb-ik-nodig/ of een andere toegestane pagina),
plekken (kommagescheiden string met echte buurten, straten en plekken; wordt getoond als "Buurten en plekken in <Naam>: ..."),
levertijd (exact "meestal binnen 15 tot 25 minuten"),
faq (precies 3 [vraag, antwoord]-paren; antwoorden 40-90 woorden, minstens één met interne link; lokale onderwerpen),
nearby (3 slugs uit de BRIEF, niet zichzelf), lat, lon (3 decimalen).

## SERVICE_PAGES (lijst van dicts; bestanden services*.py)
slug (zonder slashes, pagina komt op /<slug>/), label (badge, bijv. "Spoed"), title (40-60), description (110-160),
h1, lead (1-2 zinnen), updated (bijv. "november 2026"),
sections (lijst van 3-5 dicts: h2, paragraphs (lijst van 1-3 alinea's van 60-120 woorden), optioneel bullets (lijst van 3-6 korte zinnen)),
note (optioneel, 1-2 zinnen voor het "Let op"-kader),
faq (precies 3 [vraag, antwoord]-paren, 40-90 woorden),
related (lijst van 2-3 toegestane interne paden, bijv. ["/lachgas-nachtbezorging/", "/lachgas-informatie/lachgas-bijwerkingen-en-eerste-hulp/"]; de renderer voegt zelf "Alle informatie" toe).

## ARTICLES (lijst van dicts; bestanden articles_*.py) en TOPIC_HUBS
ARTICLES: slug, label (badge: Basis | Regels | Gezondheid | Veiligheid | Praktisch | Producten | Achtergrond | Hulp), title (40-60), description (110-160),
h1, lead (1-2 zinnen), updated, sections (4-7 dicts: h2, paragraphs (2-4 alinea's van 70-130 woorden), optioneel bullets),
note (optioneel), related (lijst van 3-4 artikel-slugs of interne paden).
TOPIC_HUBS: slug, label, title, description, h1, lead, intro (2-3 alinea's), groups (lijst van dicts: h2, text, slugs (artikel-slugs)), faq (4-5 paren).

## Overige modules (schema bepaalt de bouwer zelf, zie pages_*.py): HOME, AREA_INDEX, AREA_GROUPS, REGIO, INFO_INDEX, ASSORTIMENT, PRODUCTS, FAQ_TOPICS, FAQ_INDEX, CONTACT, ABOUT, TERMS, PRIVACY.
