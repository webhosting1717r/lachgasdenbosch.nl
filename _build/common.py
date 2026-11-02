# -*- coding: utf-8 -*-
"""Gedeelde bouwstenen voor de stads-sites (familie "stad", zoals lachgasbreda.nl): instellingen, chrome (header, mobiel menu, footer),
componenten in dezelfde Tailwind-markup als de bestaande stadssites, schema's en de paginarenderer.
Site-specifieke instellingen komen uit content/_site.py (zie configure())."""
import html as _html
import json
import os
import re
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SITE = "https://lachgasdenbosch.nl"
CNAME = "lachgasdenbosch.nl"
BRAND = "Lachgas Den Bosch"
BRAND_EM = "Den Bosch"
CITY = "'s-Hertogenbosch"
CITY_SHORT = "Den Bosch"
REGION = "Noord-Brabant"
REGION_SLUG = "noordoost-brabant"
REGION_NAME = "Noordoost-Brabant"
AREA_LINE = "Den Bosch, Rosmalen, Vught, Oss & de Bommelerwaard"
STATUS_LINE = "In Den Bosch meestal binnen 15 tot 25 minuten"
FOOTER_BLURB = ""
BUSINESS_DESC = ""
WA_NUMBER = "31684626182"
WA_DISPLAY = "+31 6 84626182"
WA_TEXT = "hey, ik wil graag bestellen."
EMAIL = "info@lachgasdenbosch.nl"
OG_IMAGE = "/assets/img/og-lachgas-den-bosch.jpg"
OG_ALT = ""
HERO_IMAGE = "/assets/img/hero-lachgas-den-bosch.webp"
TANK_IMAGE = "/assets/img/lachgastank-2kg-den-bosch.webp"
THEME = "#b91c1c"
GEO = (51.6978, 5.3037)
GEO_REGION = "NL-NB"
TODAY = "2026-11-02"
MONTH_NL = "november 2026"
INDEXNOW_KEY = ""
MANIFEST_DESC = ""
LLMS_BLURB = ""
PALETTE = []
CSS = ""


def configure(cfg):
    g = globals()
    for k, v in cfg.items():
        if k.isupper():
            g[k] = v
    g["CSS"] = _build_css()


def _build_css():
    """Inline stylesheet: @font-face + tailwind.css (met het palet van deze site) + site.css. Schrijft css/tailwind.css ook terug in de repo."""
    tw = open(os.path.join(ROOT, "css", "tailwind.css"), encoding="utf-8").read().strip()
    for old, new in PALETTE:
        tw = tw.replace(old, new)
    with open(os.path.join(ROOT, "css", "tailwind.css"), "w", encoding="utf-8") as f:
        f.write(tw + "\n")
    sc = open(os.path.join(ROOT, "css", "site.css"), encoding="utf-8").read().strip()
    sc = re.sub(r"/\*master\*/.*?/\*master-end\*/\n?", "", sc, flags=re.S).rstrip()
    sc = sc.replace("Lachgas Breda", BRAND)
    fonts = open(os.path.join(HERE, "fonts.css"), encoding="utf-8").read().strip()
    return fonts + tw + "\n" + sc


def esc(s):
    return _html.escape(s, quote=False).replace('"', "&quot;")


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def wa_link(text=None):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(text or WA_TEXT))


LINK_CLS = "font-semibold text-brand-600 hover:text-brand-700"


def linkify(s):
    """Zet op inline links in contentteksten de Tailwind-klassen van de stadssites (alleen op <a> zonder class)."""
    return re.sub(r'<a href="([^"]+)">', lambda m: '<a href="%s" class="%s"%s>' % (m.group(1), LINK_CLS, ' target="_blank" rel="noopener"' if m.group(1).startswith("http") else ""), s)


# --- iconen ---------------------------------------------------------------------
WA_PATH_FULL = "M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.42 1.26 4.86L2 22l5.35-1.31c1.4.75 2.98 1.17 4.69 1.17 5.5 0 9.96-4.46 9.96-9.96S17.54 2 12.04 2zm5.79 14.24c-.24.68-1.19 1.24-1.95 1.4-.52.11-1.2.2-3.49-.75-2.92-1.21-4.8-4.17-4.95-4.37-.14-.2-1.18-1.57-1.18-3 0-1.43.75-2.13 1.02-2.42.27-.29.58-.36.78-.36.19 0 .39 0 .56.01.18.01.42-.07.66.5.24.58.83 2 .9 2.15.07.15.12.32.02.52-.1.2-.15.32-.3.49-.14.17-.31.38-.44.51-.14.14-.29.29-.13.58.17.29.75 1.23 1.61 1.99 1.11.98 2.04 1.29 2.33 1.43.29.15.46.12.63-.07.17-.2.72-.84.92-1.13.19-.29.39-.24.65-.15.27.1 1.68.79 1.97.93.29.15.48.22.55.34.07.13.07.72-.17 1.4z"
WA_PATH_SHORT = "M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.42 1.26 4.86L2 22l5.35-1.31c1.4.75 2.98 1.17 4.69 1.17 5.5 0 9.96-4.46 9.96-9.96S17.54 2 12.04 2z"
STROKE = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'


def svg(path, size=20, fill=False, cls=""):
    return '<svg%s width="%d" height="%d" viewBox="0 0 24 24" %s>%s</svg>' % ((' class="%s"' % cls) if cls else "", size, size, 'fill="currentColor"' if fill else STROKE, path)


ICON = {
    "wa": lambda size=16: svg('<path d="%s"/>' % WA_PATH_SHORT, size, fill=True),
    "wa_full": lambda size=16: svg('<path d="%s"/>' % WA_PATH_FULL, size, fill=True),
    "tank": '<rect x="7" y="6" width="10" height="16" rx="3"/><path d="M10 6V3h4v3"/><path d="M7 11h10"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "chev": '<path d="m9 18 6-6-6-6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "seal": '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "close": '<path d="M18 6 6 18M6 6l12 12"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    "id": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M15 8h3M15 12h3M6 16h12"/>',
    "star": '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
    "truck": '<path d="M10 17h4V5H2v12h3"/><path d="M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "moon": '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "map": '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3V6z"/><path d="M9 3v15M15 6v15"/>',
    "heart": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4M12 17h.01"/>',
    "scale": '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10M12 3v18M3 7h18"/>',
    "box": '<path d="m21 8-9-5-9 5v8l9 5 9-5V8z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
}


def icon(name, size=20, cls=""):
    v = ICON[name]
    return v(size) if callable(v) else svg(v, size, cls=cls)


# --- schema's -------------------------------------------------------------------
def business_schema():
    return {"@context": "https://schema.org", "@type": "LocalBusiness", "@id": SITE + "/#business", "name": BRAND, "url": SITE + "/",
            "image": SITE + OG_IMAGE, "logo": SITE + "/icon-512.png", "email": EMAIL, "telephone": "+" + WA_NUMBER, "description": BUSINESS_DESC,
            "priceRange": "€€", "currenciesAccepted": "EUR", "paymentAccepted": "Contant, Tikkie",
            "areaServed": [{"@type": "City", "name": CITY}, {"@type": "AdministrativeArea", "name": REGION_NAME}],
            "address": {"@type": "PostalAddress", "addressLocality": CITY, "addressRegion": REGION, "addressCountry": "NL"},
            "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}],
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "telephone": "+" + WA_NUMBER, "email": EMAIL, "availableLanguage": "nl"},
            "sameAs": ["https://wa.me/" + WA_NUMBER]}


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND, "inLanguage": "nl-NL", "publisher": {"@id": SITE + "/#business"}}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h} for i, (n, h) in enumerate(items) if h]}


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in items]}


def service_schema(name, desc, path, area=None, area_type="City", geo=None):
    served = {"@type": area_type, "name": area or CITY}
    if geo:
        served["geo"] = {"@type": "GeoCoordinates", "latitude": geo[0], "longitude": geo[1]}
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": SITE + path, "serviceType": "Lachgas bezorgservice",
            "provider": {"@id": SITE + "/#business"}, "areaServed": served, "availableChannel": {"@type": "ServiceChannel", "serviceUrl": "https://wa.me/" + WA_NUMBER, "name": "WhatsApp"}}


def article_schema(title, desc, path):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "inLanguage": "nl-NL", "mainEntityOfPage": SITE + path,
            "datePublished": TODAY, "dateModified": TODAY, "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"}, "publisher": {"@id": SITE + "/#business"}}


def webpage_schema(title, desc, path, typ="WebPage"):
    return {"@context": "https://schema.org", "@type": typ, "name": title, "description": desc, "url": SITE + path, "inLanguage": "nl-NL", "isPartOf": {"@id": SITE + "/#website"}}


def itemlist_schema(name, items):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name, "itemListOrder": "https://schema.org/ItemListUnordered",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": SITE + h} for i, (n, h) in enumerate(items)]}


def product_schema(name, desc, path, image=None):
    return {"@context": "https://schema.org", "@type": "Product", "name": name, "description": desc, "url": SITE + path, "brand": {"@type": "Brand", "name": BRAND},
            **({"image": SITE + image} if image else {})}


# --- chrome ---------------------------------------------------------------------
NAV = [("/assortiment/", "Assortiment"), ("/bezorggebied/", "Bezorggebied"), ("/lachgas-informatie/", "Lachgas Info"), ("/over-ons/", "Over ons"), ("/contact/", "Contact")]
PRODUCTS = [("/product/lachgas-tank-2kg/", "Lachgastank 2KG"), ("/product/lachgas-tank-4kg/", "Lachgastank 4KG"), ("/product/lachgas-tank-10kg/", "Lachgastank 10KG"),
            ("/product/lachgas-cracker/", "Lachgas crackers"), ("/product/slagroompatronen/", "Slagroompatronen")]


def mm_groups():
    return [("Bestellen", [PRODUCTS[0], PRODUCTS[1], PRODUCTS[2], ("/werkwijze/", "Zo werkt bestellen"), ("/betalen-bij-levering/", "Betalen bij levering"), ("/zakelijk-bestellen/", "Zakelijk bestellen")]),
            ("Bezorgen", [("/bezorgtijden-den-bosch/", "Bezorgtijden"), ("/bezorggebied/%s/" % REGION_SLUG, REGION_NAME), ("/lachgas-nachtbezorging/", "Nachtbezorging"), ("/lachgas-spoedbezorging/", "Spoedbezorging")]),
            ("Informatie", [("/lachgas-informatie/veiligheid-en-gezondheid/", "Veiligheid en gezondheid"), ("/lachgas-informatie/regels-en-wetgeving/", "Regels en wetgeving"),
                            ("/lachgas-informatie/eerste-keer-lachgas-bestellen/", "Voor het eerst bestellen"), ("/lachgas-informatie/veilig-gebruik/", "Verantwoord omgaan met lachgas")]),
            ("Service", [("/bezorgvoorwaarden/", "Bezorgvoorwaarden"), ("/bestelling-wijzigen-of-annuleren/", "Wijzigen of annuleren"), ("/veilig-bestellen-oplichting-herkennen/", "Veilig bestellen"), ("/over-ons/", "Over ons"), ("/contact/", "Contact")])]


def header(path):
    cur = lambda h: ' aria-current="page"' if h == path else ""
    links = "".join('<a href="%s" class="rounded-lg px-4 py-2 text-sm font-medium text-gray-600 transition hover:bg-gray-50 hover:text-gray-900"%s>%s</a>\n' % (h, cur(h), t) for h, t in NAV)
    tiles = [("/assortiment/", "Assortiment", "tank"), ("/bezorggebied/", "Bezorggebied", "pin"), ("/lachgas-informatie/", "Informatie", "book"), ("/veelgestelde-vragen/", "Veelgestelde vragen", "chat")]
    tile_html = ""
    for i, (h, t, ic) in enumerate(tiles):
        dark = i == 0
        tile_html += '<a href="%s" class="mm-tile %s"%s><span class="%s"><svg viewBox="0 0 24 24" %s>%s</svg></span>%s</a>' % (
            h, "bg-gray-900 text-white" if dark else "bg-surface-50 text-gray-900", cur(h), "text-white" if dark else "text-brand-600", STROKE, ICON[ic], t)
    groups = ""
    for g, items in mm_groups():
        groups += '<div class="mm-group"><p class="mm-h text-gray-500">%s</p>%s</div>' % (g, "".join(
            '<a href="%s" class="mm-link text-gray-700"%s><span>%s</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">%s</svg></a>' % (h, cur(h), esc(t), ICON["chev"]) for h, t in items))
    return ('<a class="skip" href="#inhoud">Direct naar inhoud</a><header><nav id="site-nav" class="fixed top-0 left-0 right-0 z-50 transition-all duration-300 bg-white/95 backdrop-blur-sm" aria-label="Hoofdmenu">\n'
            '<div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3.5 sm:px-6 lg:px-8">\n'
            '<a href="/" class="flex items-center gap-2.5" aria-label="%s – naar de homepage">\n'
            '<span class="flex h-9 w-9 items-center justify-center rounded-lg bg-brand-600 font-heading text-lg font-extrabold text-white">L</span>\n'
            '<span class="font-heading text-lg font-extrabold tracking-tight">Lachgas <span class="text-brand-600">%s</span></span>\n</a>\n'
            '<div class="hidden items-center gap-1 lg:flex">\n%s</div>\n'
            '<div class="flex items-center gap-2">\n'
            '<a href="%s" target="_blank" rel="noopener" class="hidden items-center gap-2 rounded-xl bg-whatsapp-600 px-5 py-2.5 text-sm font-bold text-white shadow-sm transition hover:bg-whatsapp-700 sm:flex">\n%s\nWhatsApp ons\n</a>\n'
            '<button id="mobile-menu-btn" class="flex h-10 w-10 items-center justify-center rounded-lg border border-gray-200 lg:hidden" aria-label="Menu openen" aria-expanded="false" aria-controls="mobile-panel">\n%s\n</button>\n'
            '</div>\n</div>\n</nav></header>\n'
            '<div id="mobile-overlay" class="hidden fixed inset-0 z-[60] bg-gray-900/50 backdrop-blur-sm lg:hidden"></div>\n'
            '<div id="mobile-panel" class="mm-panel hidden fixed right-0 top-0 z-[70] flex h-full w-80 max-w-[85vw] flex-col bg-white p-6 shadow-2xl animate-slide-in-right lg:hidden" role="dialog" aria-modal="true" aria-label="Menu">'
            '<div class="mb-4 flex items-center justify-between"><span class="font-heading text-lg font-extrabold">Menu</span><button id="mobile-menu-close" class="flex h-9 w-9 items-center justify-center rounded-lg border border-gray-200" aria-label="Menu sluiten">\n%s\n</button></div>'
            '<div class="mm-status bg-surface-50 text-gray-600"><span class="mm-dot"></span><span><strong class="text-gray-900">24/7 bereikbaar via WhatsApp</strong><br/>%s</span></div>'
            '<nav aria-label="Mobiel menu"><div class="mm-tiles">%s</div>'
            '<a href="/product/lachgas-tank-2kg/" class="mm-prod border border-gray-100 bg-white"><img src="/img/lachgastank-2kg-160.webp" width="56" height="56" alt="" loading="lazy" decoding="async"/><span><strong class="block text-gray-900">Lachgastank 2KG</strong><span class="text-sm text-gray-500">Verzegeld geleverd &middot; bekijk de tank</span></span></a>'
            '%s</nav><div class="mm-foot"><a href="%s" target="_blank" rel="noopener" class="flex items-center justify-center gap-2 rounded-xl bg-whatsapp-600 px-5 py-3.5 text-sm font-bold text-white hover:bg-whatsapp-700">%s WhatsApp ons nu</a>'
            '<p class="mm-trust text-gray-500"><span>18+ met legitimatie</span><span>Verzegeld</span><span>Betalen aan de deur</span></p></div></div>\n'
            % (esc(BRAND), esc(BRAND_EM), links, wa_link(), icon("wa_full", 16), icon("menu", 20), icon("close", 18), esc(STATUS_LINE), tile_html, groups, wa_link(), icon("wa", 16)))


def footer():
    def li(h, t):
        return '<li><a href="%s" class="hover:text-white">%s</a></li>\n' % (h, t)
    info = [("/lachgas-informatie/", "Lachgas informatie"), ("/lachgas-informatie/is-lachgas-legaal-in-nederland/", "Is lachgas legaal in Nederland?"), ("/lachgas-informatie/veilig-gebruik/", "Veilig gebruik"),
            ("/bezorggebied/", "Bezorggebied"), ("/veelgestelde-vragen/", "Veelgestelde vragen"), ("/lachgas-nachtbezorging/", "Lachgas &rsquo;s avonds en &rsquo;s nachts"), ("/lachgas-feest-evenement/", "Feest &amp; evenement"),
            ("/zakelijk-bestellen/", "Zakelijk bestellen"), ("/bezorgvoorwaarden/", "Bezorgvoorwaarden"), ("/bestelling-wijzigen-of-annuleren/", "Bestelling wijzigen of annuleren"), ("/veilig-bestellen-oplichting-herkennen/", "Veilig bestellen"), ("/over-ons/", "Over ons")]
    chk = '<p class="flex items-center gap-2"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M20 6 9 17l-5-5"/></svg> %s</p>\n'
    box = '<span class="flex h-10 w-10 items-center justify-center rounded-lg bg-white/5 border border-white/10">%s</span>'
    return ('<footer class="bg-gray-900 text-gray-400">\n<div class="mx-auto grid max-w-7xl gap-12 px-4 py-16 sm:grid-cols-2 sm:px-6 lg:grid-cols-4 lg:px-8">\n<div>\n'
            '<a href="/" class="mb-4 flex items-center gap-2.5">\n<span class="flex h-9 w-9 items-center justify-center rounded-lg bg-white/10"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="M12 15v6"/><path d="M9 21h6"/></svg></span>\n'
            '<span class="font-heading text-lg font-extrabold text-white">%s</span>\n</a>\n<p class="mb-4 text-sm">%s</p>\n<div class="space-y-1.5 text-sm">\n%s%s%s</div>\n</div>\n'
            '<div>\n<h3 class="mb-4 font-heading text-sm font-bold text-white uppercase tracking-wide">Assortiment</h3>\n<ul class="space-y-2.5 text-sm">\n%s</ul>\n</div>\n'
            '<div>\n<h3 class="mb-4 font-heading text-sm font-bold text-white uppercase tracking-wide">Info &amp; bezorging</h3>\n<ul class="space-y-2.5 text-sm">\n%s</ul>\n</div>\n'
            '<div>\n<h3 class="mb-4 font-heading text-sm font-bold text-white uppercase tracking-wide">Contact</h3>\n<ul class="space-y-3 text-sm">\n'
            '<li>\n<a href="%s" target="_blank" rel="noopener" class="flex items-center gap-3 hover:text-white">\n%s\nWhatsApp: %s\n</a>\n</li>\n'
            '<li>\n<a href="mailto:%s" class="flex items-center gap-3 hover:text-white">\n%s\n%s\n</a>\n</li>\n'
            '<li class="flex items-center gap-3">\n%s\n%s\n</li>\n</ul>\n</div>\n</div>\n'
            '<div class="border-t border-white/10 px-4 py-6 sm:px-6 lg:px-8">\n<div class="mx-auto flex max-w-7xl flex-col items-center justify-between gap-3 text-xs sm:flex-row">\n'
            '<p>&copy; <span id="year">2026</span> %s. Alle rechten voorbehouden. Verkoop uitsluitend aan personen van 18 jaar en ouder.</p>\n'
            '<div class="flex gap-4">\n<a href="/algemene-voorwaarden/" class="hover:text-white">Algemene voorwaarden</a>\n<a href="/privacy/" class="hover:text-white">Privacy</a>\n<a href="/sitemap/" class="hover:text-white">Sitemap</a>\n</div>\n</div>\n</div>\n</footer>\n'
            '<div id="image-lightbox" class="hidden fixed inset-0 z-[90] items-center justify-center bg-gray-900/95 backdrop-blur-sm p-4 sm:p-8" role="dialog" aria-modal="true" aria-label="Afbeelding vergroot">\n'
            '<button id="image-lightbox-close" type="button" class="absolute top-4 right-4 flex h-11 w-11 items-center justify-center rounded-full bg-white/10 text-white transition hover:bg-white/20 sm:top-6 sm:right-6" aria-label="Sluiten">\n%s\n</button>\n'
            '<img loading="lazy" decoding="async" id="image-lightbox-img" src="" alt="" width="1200" height="800" class="max-h-[92vh] max-w-[95vw] rounded-2xl object-contain shadow-2xl">\n</div>\n'
            '<a href="%s" target="_blank" rel="noopener" class="fixed bottom-6 right-6 z-40 flex h-14 w-14 items-center justify-center rounded-full bg-whatsapp-600 text-white shadow-2xl transition hover:bg-whatsapp-700 hover:scale-105 animate-pulse-ring" aria-label="WhatsApp ons">\n%s\n</a>\n'
            '<script src="/js/site.js" defer></script>\n<script>document.getElementById("year").textContent = new Date().getFullYear();</script>\n'
            % (esc(BRAND), esc(FOOTER_BLURB), chk % "Snel &amp; discreet bezorgd", chk % "Verzegelde kwaliteit", chk % "Alleen verkoop aan 18+",
               "".join(li(h, t) for h, t in PRODUCTS), "".join(li(h, t) for h, t in info),
               wa_link(), box % icon("wa", 16), WA_DISPLAY, EMAIL, box % icon("mail", 16), EMAIL, box % icon("pin", 16), esc(AREA_LINE), esc(BRAND),
               svg(ICON["close"], 20).replace(' stroke-linejoin="round"', ""), wa_link(), icon("wa_full", 28)))


# --- componenten ----------------------------------------------------------------
SEC = 'px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24'
BADGE_DARK = '<span class="mb-4 inline-block rounded-full bg-gray-900 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">%s</span>'
BADGE_LIGHT = '<span class="mb-4 inline-block rounded-full bg-white/10 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">%s</span>'
CHIP = '<a href="%s" class="rounded-full border border-gray-200 bg-white px-5 py-2.5 text-sm font-semibold text-gray-700 transition hover:border-brand-300 hover:bg-brand-50 hover:text-brand-700">%s</a>\n'


def crumbs(items, light=True):
    out = []
    for n, h in items:
        if h:
            out.append('<a href="%s" class="hover:text-white/70">%s</a>\n<span aria-hidden="true">/</span>\n' % (h, esc(n)))
        else:
            out.append('<span class="text-white/70" aria-current="page">%s</span>\n' % esc(n))
    return '<nav aria-label="Kruimelpad" class="mb-6 flex flex-wrap items-center justify-center gap-1.5 text-xs text-white/40">\n%s</nav>\n' % "".join(out)


def hero_dark(crumb_items, badge, h1, lead, extra=""):
    """Donkere paginakop zoals op de plaats-, service- en artikelpagina's van de stadssites."""
    return ('<section class="relative overflow-hidden bg-gray-900 pt-28 pb-16 lg:pt-36 lg:pb-20">\n'
            '<div class="absolute -top-10 -right-10 h-72 w-72 rounded-full bg-brand-600/20 blur-[100px]"></div>\n'
            '<div class="relative mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">\n%s%s\n'
            '<h1 class="mb-4 font-heading text-4xl font-extrabold text-white sm:text-5xl">%s</h1>\n'
            '<p class="mx-auto max-w-2xl text-white/60">%s</p>\n%s</div>\n</section>\n'
            % (crumbs(crumb_items), BADGE_LIGHT % esc(badge), esc(h1), linkify(lead), extra))


def stats(items=None, data_extra="area"):
    items = items or [("Levertijd", "Meestal 15 tot 25 min"), ("Bestellen", "24/7 via WhatsApp"), ("Betalen", "Contant of Tikkie bij levering"), ("Leeftijd", "Alleen 18+, met legitimatie")]
    return ('<section class="relative -mt-8 z-10 px-4 sm:px-6 lg:px-8" data-extra="%s">\n<div class="mx-auto grid max-w-6xl grid-cols-2 gap-4 sm:grid-cols-4">\n%s</div>\n</section>\n'
            % (data_extra, "".join('<div class="rounded-2xl border border-gray-100 bg-white p-5 text-center shadow-card">\n<p class="text-xs text-gray-500">%s</p>\n<p class="font-heading text-sm font-bold text-gray-900">%s</p>\n</div>\n' % (esc(k), esc(v)) for k, v in items)))


def section(inner, alt=False, width="max-w-4xl", center=False, attrs=""):
    return '<section class="%s%s"%s>\n<div class="mx-auto %s%s">\n%s</div>\n</section>\n' % ("bg-surface-50 " if alt else "", SEC, (" " + attrs) if attrs else "", width, " text-center" if center else "", inner)


def sec_head(badge, h2, text=None, narrow=True, mb="mb-12"):
    return ('<div class="mx-auto %s max-w-2xl text-center">\n%s\n<h2 class="%sfont-heading text-3xl font-bold sm:text-4xl">%s</h2>\n%s</div>\n'
            % (mb, BADGE_DARK % esc(badge), "mb-4 " if text else "", esc(h2), ('<p class="text-gray-500">%s</p>\n' % linkify(text)) if text else ""))


def p(text, last=False):
    return '<p class="text-gray-600 leading-relaxed%s">%s</p>\n' % ("" if last else " mb-4", linkify(text))


def h2(text, first=False):
    return '<h2 class="mb-4%s font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n' % ("" if first else " mt-10", esc(text))


def h3(text):
    return '<h3 class="mb-3 mt-8 font-heading text-xl font-bold">%s</h3>\n' % esc(text)


def bullets(items):
    return '<ul class="mb-6 space-y-2 text-gray-600">\n%s</ul>\n' % "".join('<li class="flex gap-3"><span class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-brand-600"></span><span>%s</span></li>\n' % linkify(b) for b in items)


def notice(text, label="Let op:"):
    return ('<div class="mt-10 rounded-2xl border border-gray-100 bg-surface-50 p-6">\n<p class="text-sm text-gray-500 leading-relaxed"><strong class="text-gray-900">%s</strong> %s</p>\n</div>\n' % (esc(label), linkify(text)))


def updated(month=None):
    return '<p class="mb-8 text-sm text-gray-500">Laatst bijgewerkt: %s</p>\n' % esc(month or MONTH_NL)


def prose_sections(sections, note=None, month=None):
    """Artikelachtige inhoud: datum, h2-blokken met alinea's en opsommingen, optioneel 'Let op'-kader."""
    out = [updated(month)]
    for i, s in enumerate(sections):
        out.append(h2(s["h2"], first=(i == 0)))
        paras = s.get("paragraphs", [])
        for j, t in enumerate(paras):
            out.append(p(t))
        if s.get("bullets"):
            out.append(bullets(s["bullets"]))
        for sub in s.get("subsections", []):
            out.append(h3(sub["h3"]))
            for t in sub.get("paragraphs", []):
                out.append(p(t))
            if sub.get("bullets"):
                out.append(bullets(sub["bullets"]))
    if note:
        out.append(notice(note))
    return "".join(out)


def faq(items, open_first=True):
    out = []
    for i, (q, a) in enumerate(items):
        out.append('<details class="group rounded-xl border border-gray-100 bg-white overflow-hidden transition-shadow hover:shadow-sm"%s>\n'
                   '<summary class="flex w-full cursor-pointer items-center justify-between px-6 py-5 text-left">\n'
                   '<span class="pr-4 text-base font-semibold text-gray-900">%s</span>\n'
                   '<svg class="shrink-0 text-gray-400 transition-transform group-open:rotate-180" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>\n'
                   '</summary>\n<div class="px-6 pb-5 text-sm text-gray-500 leading-relaxed">%s</div>\n</details>\n' % (" open" if (i == 0 and open_first) else "", esc(q), linkify(a)))
    return '<div class="space-y-3">\n%s</div>\n' % "".join(out)


def faq_section(items, h2_text="Veelgestelde vragen", alt=True, badge="FAQ"):
    inner = '<div class="mb-10 text-center">\n%s\n<h2 class="font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n</div>\n%s' % (BADGE_DARK % esc(badge), esc(h2_text), faq(items))
    return section(inner, alt=alt, width="max-w-3xl")


def chips(items):
    return '<div class="flex flex-wrap justify-center gap-3">\n%s</div>\n' % "".join(CHIP % (h, esc(t)) for h, t in items)


def chips_section(badge, h2_text, items, text=None, alt=False):
    inner = '%s\n<h2 class="%s font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n%s%s' % (
        BADGE_DARK % esc(badge), "mb-4" if text else "mb-6", esc(h2_text), ('<p class="mb-8 text-gray-500">%s</p>\n' % linkify(text)) if text else "", chips(items))
    return section(inner, alt=alt, center=True)


def related_section(items, badge="Meer weten", h2_text="Verder lezen", alt=False):
    return chips_section(badge, h2_text, items, alt=alt)


def card(href, title, text, icon_name, dark_icon=True, more=None):
    ico = '<div class="mb-4 flex h-12 w-12 items-center justify-center rounded-xl %s">%s</div>\n' % ("bg-gray-900 text-white" if dark_icon else "bg-brand-50 text-brand-600", icon(icon_name, 20))
    inner = '%s<h3 class="mb-1 font-bold">%s</h3>\n<p class="text-sm text-gray-500">%s</p>\n' % (ico, esc(title), linkify(text))
    if href:
        return '<a href="%s" class="group block rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:-translate-y-1">\n%s%s</a>\n' % (
            href, inner, ('<span class="mt-3 inline-flex items-center gap-1 text-sm font-semibold text-brand-600 group-hover:text-brand-700">%s %s</span>\n' % (esc(more), svg(ICON["chev"], 14))) if more else "")
    return '<div class="rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:-translate-y-1">\n%s</div>\n' % inner


def cards_grid(items, cols=4):
    cls = {2: "grid gap-4 sm:grid-cols-2", 3: "grid gap-4 sm:grid-cols-2 lg:grid-cols-3", 4: "grid gap-4 sm:grid-cols-2 lg:grid-cols-4"}[cols]
    return '<div class="%s">\n%s</div>\n' % (cls, "".join(items))


def why_section(place=None, alt=True):
    where = place or CITY_SHORT
    items = [card(None, "Bestellen in één bericht", "Geen account of webshop: je appt je bestelling en je adres en wij nemen het van je over.", "wa"),
             card(None, "Verzegeld geleverd", "Tanks komen verzegeld aan, zodat je bij de deur ziet dat de inhoud onaangeroerd is.", "seal"),
             card(None, "Alleen voor volwassenen", "We leveren uitsluitend aan 18-plussers en vragen bij twijfel om een identiteitsbewijs.", "shield"),
             card(None, "Snelle levering", "In %s meestal binnen 15 tot 25 minuten." % where, "clock")]
    return section(sec_head("Waarom wij", "Waarom %s" % BRAND) + cards_grid(items, 4), alt=alt, width="max-w-6xl")


def products_section(place=None, alt=False):
    where = place or CITY_SHORT
    inner = ('%s\n<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">Lachgastanks in drie formaten</h2>\n'
             '<p class="mb-8 text-gray-500">Ook crackers en slagroompatronen leverbaar in %s. Prijs op aanvraag via WhatsApp.</p>\n%s'
             % (BADGE_DARK % "Assortiment", esc(where), chips(PRODUCTS[:3])))
    return section(inner, alt=alt, center=True)


def cta(h2_text="Bestellen of eerst iets vragen?", text="Stuur een WhatsApp-bericht met je adres en wat je nodig hebt; je krijgt direct een prijs en een verwachte tijd terug.", wa_text=None):
    return ('<section class="relative overflow-hidden bg-whatsapp-600 px-4 py-16 sm:px-6 lg:px-8">\n<div class="absolute -top-16 -right-16 h-72 w-72 rounded-full bg-white/10 blur-3xl"></div>\n'
            '<div class="relative mx-auto max-w-3xl text-center">\n<h2 class="mb-4 font-heading text-3xl font-bold text-white sm:text-4xl">%s</h2>\n<p class="mb-8 text-white/80">%s</p>\n'
            '<div class="flex flex-col items-center justify-center gap-3 sm:flex-row">\n'
            '<a href="%s" target="_blank" rel="noopener" class="inline-flex items-center gap-2 rounded-xl bg-white px-7 py-4 text-base font-bold text-whatsapp-700 shadow-lg transition hover:shadow-xl active:scale-[0.98]">\n%s\nWhatsApp ons nu\n</a>\n'
            '<a href="/contact/" class="inline-flex items-center gap-2 rounded-xl border-2 border-white/30 px-7 py-4 text-base font-bold text-white transition hover:bg-white/10">Of vul het contactformulier in</a>\n'
            '</div>\n</div>\n</section>\n' % (esc(h2_text), linkify(text), wa_link(wa_text), icon("wa", 18)))


def wa_button(text="WhatsApp ons nu", wa_text=None, cls="inline-flex items-center gap-2 rounded-xl bg-whatsapp-600 px-6 py-3.5 text-sm font-bold text-white shadow-sm transition hover:bg-whatsapp-700"):
    return '<a href="%s" target="_blank" rel="noopener" class="%s">%s %s</a>' % (wa_link(wa_text), cls, icon("wa", 16), esc(text))


# --- renderer -------------------------------------------------------------------
def render(page, ctx=None):
    path = page["path"]
    url = SITE + path
    title, desc = page["title"], page["description"]
    schemas = page.get("schemas", [])
    if path == "/":
        schemas = [business_schema(), website_schema()] + schemas
    ld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") for s in schemas)
    robots = page.get("robots", "index, follow, max-image-preview:large")
    preload = ('<link rel="preload" as="image" href="%s" type="image/webp" fetchpriority="high" media="(min-width: 1024px)">' % HERO_IMAGE) if path == "/" else ""
    head = ('<!DOCTYPE html>\n<html lang="nl">\n<head>\n<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>%s</title><meta name="description" content="%s"><meta name="robots" content="%s">'
            '<link rel="canonical" href="%s"><link rel="alternate" hreflang="nl" href="%s"><link rel="alternate" hreflang="x-default" href="%s">'
            '<meta property="og:type" content="%s"><meta property="og:site_name" content="%s"><meta property="og:locale" content="nl_NL"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s">'
            '<meta property="og:image" content="%s"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="%s">'
            '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s"><meta name="twitter:image" content="%s">'
            '<meta name="theme-color" content="%s"><meta name="geo.region" content="%s"><meta name="geo.placename" content="%s">'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="32x32 48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/manifest.webmanifest">%s'
            '<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/plusjakartasans.woff2" as="font" type="font/woff2" crossorigin>'
            '<style>%s</style>%s\n</head>\n'
            % (esc(title), esc(desc), robots, url, url, url, page.get("og_type", "website"), esc(BRAND), esc(title), esc(desc), url, SITE + OG_IMAGE, esc(OG_ALT), esc(title), esc(desc), SITE + OG_IMAGE,
               THEME, GEO_REGION, esc(CITY), preload, CSS, ld))
    body = '<body class="font-sans antialiased bg-white text-gray-900">\n%s<main id="inhoud">\n%s</main>\n%s</body>\n</html>\n' % (header(path), page["body"], footer())
    return head + body


def page_text(page):
    b = re.sub(r"<(script|style|svg)\b.*?</\1>", "", page["body"], flags=re.S)
    b = re.sub(r"</(p|li|h1|h2|h3|dd|dt|tr|div|section|summary)>", "\n", b)
    t = _html.unescape(strip_tags(b))
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()
