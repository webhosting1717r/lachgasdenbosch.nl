# -*- coding: utf-8 -*-
"""Bezorggebied-index (/bezorggebied/) en regiopagina (/bezorggebied/<regio>/) van de stads-site, in de opbouw van de bestaande stadssites."""
import common as C
from common import esc, linkify, section, hero_dark, faq_section, chips, cta, why_section, p, CHIP, BADGE_DARK

DARK_CHIP = '<a href="%s" class="rounded-full bg-gray-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-gray-800">%s</a>\n'
ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
LABEL = '<p class="mb-3 text-center text-xs font-bold uppercase tracking-wide text-gray-400">%s</p>\n'
DEFAULT_STEPS = [
    ["Bestel via WhatsApp", "Je stuurt ons een bericht met wat je wilt bestellen en je adres in Den Bosch, Rosmalen, Vught, Oss, de Bommelerwaard of een van de andere plaatsen."],
    ["Wij bevestigen adres en tijd", "Wij bevestigen direct je bestelling en geven een indicatie van de bezorgtijd voor jouw adres, meestal binnen 15 tot 25 minuten."],
    ["Wij bezorgen discreet aan de deur", "Onopvallende aflevering op een woonadres, geen afhaalpunt nodig. Je betaalt bij ontvangst, contant of via Tikkie."],
]


def _chips(items, dark):
    tpl = DARK_CHIP if dark else CHIP
    return "".join(tpl % (h, esc(t)) for h, t in items)


def _group_links(site, slugs):
    return [site.place_link(s) for s in slugs if s in site.place_by]


def area_index(site, A, groups, regio):
    regio_href = "/bezorggebied/%s/" % C.REGION_SLUG
    regio_name = (regio or {}).get("name", C.REGION_NAME)
    intro = A["intro"]
    inner = '<div class="mx-auto max-w-4xl">\n<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n' % esc(A.get("intro_h2", "Eén levertijd, één werkgebied"))
    for i, t in enumerate(intro):
        inner += p(t, last=(i == len(intro) - 1))
    inner += "</div>\n"
    all_links = []
    for i, g in enumerate(groups):
        links = _group_links(site, g["slugs"])
        if not links:
            continue
        all_links += links
        inner += '<div class="mx-auto %s max-w-4xl">\n' % ("mt-10" if i == 0 else "mt-8")
        inner += LABEL % esc(g["title"])
        if g.get("text"):
            inner += '<p class="mb-4 text-center text-sm text-gray-500">%s</p>\n' % linkify(g["text"])
        inner += '<div class="flex flex-wrap justify-center gap-3">\n%s</div>\n' % _chips(links, dark=(i == 0))
        if i == 0 and regio:
            inner += ('<div class="mt-10 text-center">\n<a href="%s" class="inline-flex items-center gap-1 text-sm font-bold text-brand-600 hover:text-brand-700">Alles over bezorgen in %s %s</a>\n</div>\n'
                      % (regio_href, esc(regio_name), ARROW))
        inner += "</div>\n"
    body = hero_dark([("Home", "/"), ("Bezorggebied", None)], "Bezorggebied", A["h1"], A["lead"])
    body += '<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n%s</section>\n' % inner
    steps = A.get("steps") or DEFAULT_STEPS
    cards = "".join('<div class="rounded-2xl border border-gray-100 bg-white p-6 text-center shadow-card">\n'
                    '<div class="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-gray-900 font-heading text-lg font-extrabold text-white">%d</div>\n'
                    '<h3 class="mb-2 font-bold">%s</h3>\n<p class="text-sm text-gray-500">%s</p>\n</div>\n' % (i + 1, esc(t), linkify(d)) for i, (t, d) in enumerate(steps))
    body += ('<section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n'
             '<div class="mx-auto mb-12 max-w-2xl text-center">\n%s\n<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n</div>\n'
             '<div class="grid gap-6 sm:grid-cols-3">\n%s</div>\n</div>\n</section>\n' % (BADGE_DARK % "Hoe werkt bezorging", esc(A.get("steps_h2", "In drie stappen aan je deur")), cards))
    body += faq_section(A["faq"], A.get("faq_h2", "Vragen over ons bezorggebied"), alt=False, badge="Veelgestelde vragen")
    body += cta()
    site.add(path="/bezorggebied/", title=A["title"], description=A["description"], body=body, priority="0.9", changefreq="weekly",
             schemas=[C.crumbs_schema([("Home", "/"), ("Bezorggebied", "/bezorggebied/")]), C.faq_schema(A["faq"]),
                      C.itemlist_schema("Bezorggebied %s" % C.BRAND, ([(regio_href, regio_name)] if regio else []) + all_links)])


def regio_page(site, R):
    path = "/bezorggebied/%s/" % R["slug"]
    crumb = [("Home", "/"), ("Bezorggebied", "/bezorggebied/"), (R["name"], None)]
    body = hero_dark(crumb, "Regio", R["h1"], R["lead"])
    body += section("".join(p(t) for t in R["intro"]))
    blocks = ""
    listed = []
    secs = R["sections"]
    for i, s in enumerate(secs):
        links = _group_links(site, s["slugs"])
        listed += links
        blocks += ('<div class="%s">\n<h2 class="mb-2 font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n<p class="mb-6 text-gray-500">%s</p>\n'
                   '<div class="flex flex-wrap gap-3">\n%s</div>\n</div>\n' % ("mb-12" if i < len(secs) - 1 else "", esc(s["h2"]), linkify(s["text"]), _chips(links, dark=(i % 2 == 0))))
    body += '<section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-4xl">\n%s</div>\n</section>\n' % blocks
    body += why_section(alt=True)
    body += faq_section(R["faq"], R.get("faq_h2", "Veelgestelde vragen over bezorgen in de regio"), alt=False, badge="FAQ")
    body += cta()
    site.add(path=path, title=R["title"], description=R["description"], body=body, priority="0.8", changefreq="weekly",
             schemas=[C.crumbs_schema([("Home", "/"), ("Bezorggebied", "/bezorggebied/"), (R["name"], path)]),
                      C.service_schema("Lachgas bezorgen in %s" % R["name"], R["description"], path, R["name"], "AdministrativeArea"),
                      C.faq_schema(R["faq"]), C.itemlist_schema("Plaatsen in %s" % R["name"], listed)])


def build(site):
    A = site.get("AREA_INDEX")
    if not A:
        return
    groups = site.get("AREA_GROUPS") or []
    regio = site.get("REGIO")
    area_index(site, A, groups, regio)
    if regio:
        regio_page(site, regio)
