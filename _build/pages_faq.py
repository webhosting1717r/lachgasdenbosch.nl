# -*- coding: utf-8 -*-
"""Veelgestelde vragen: de index (/veelgestelde-vragen/) met themakaarten en vier vragenblokken, en de themapagina's
(/veelgestelde-vragen/<thema>/), in dezelfde markup als de bestaande stadssites. Content: FAQ_INDEX en FAQ_TOPICS in content/faq_pages.py."""
import common as C
from common import esc, linkify, section, p, hero_dark, faq_section, chips_section, cta

ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
BOOK = C.svg(C.ICON["book"], 22)


def strongify(s):
    return linkify(s).replace("<strong>", '<strong class="text-gray-900">')


def topic_card(t):
    return ('<a href="/veelgestelde-vragen/%s/" class="group flex flex-col rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:border-gray-200 hover:-translate-y-1">\n'
            '<div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-gray-900 text-white transition-colors group-hover:bg-brand-600">%s</div>\n'
            '<h2 class="mb-2 text-lg font-bold group-hover:text-brand-600">%s</h2>\n'
            '<p class="mb-4 flex-1 text-sm text-gray-500">%s</p>\n'
            '<div class="flex items-center gap-1 text-sm font-semibold group-hover:text-brand-600">Bekijk de vragen %s</div>\n</a>\n'
            % (t["slug"], BOOK, esc(t["h1"]), esc(t.get("card") or t["description"]), ARROW))


def index_page(site, F):
    topics = site.faq_topics
    intro = "".join('<p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % strongify(t) for t in F["intro"])
    cards = "".join(topic_card(t) for t in topics)
    body = hero_dark([("Home", "/"), ("Veelgestelde vragen", None)], "FAQ", F["h1"], F["lead"])
    body += ('<section class="%s">\n<div class="mx-auto max-w-4xl">\n%s</div>\n<div class="mx-auto mt-6 max-w-5xl">\n<div class="grid gap-4 sm:grid-cols-2">\n%s</div>\n</div>\n</section>\n'
             % (C.SEC, intro, cards))
    shown = []
    for i, b in enumerate(F["blocks"]):
        body += faq_section(b["items"], b["h2"], alt=(i % 2 == 0))
        shown += b["items"]
    body += cta()
    site.add(path="/veelgestelde-vragen/", title=F["title"], description=F["description"], body=body, priority="0.8",
             schemas=[C.crumbs_schema([("Home", "/"), ("Veelgestelde vragen", "/veelgestelde-vragen/")]), C.faq_schema(shown),
                      C.itemlist_schema("Veelgestelde vragen per thema", [("/veelgestelde-vragen/%s/" % t["slug"], t["h1"]) for t in topics])])


def topic_page(site, t):
    path = "/veelgestelde-vragen/%s/" % t["slug"]
    crumb = [("Home", "/"), ("Veelgestelde vragen", "/veelgestelde-vragen/"), (t["h1"], None)]
    intro = "".join(p(x) for x in t["intro"])
    others = [("/veelgestelde-vragen/%s/" % x["slug"], x["h1"]) for x in site.faq_topics if x["slug"] != t["slug"]]
    rel = [l for l in site.related_links(t.get("related", [])) if l not in others]
    body = (hero_dark(crumb, "FAQ", t["h1"], t["lead"])
            + section(intro, width="max-w-3xl")
            + faq_section(t["items"], t["h1"], alt=True)
            + chips_section("Meer vragen", "Andere onderwerpen", others + rel + [("/veelgestelde-vragen/", "Alle veelgestelde vragen")])
            + cta())
    site.add(path=path, title=t["title"], description=t["description"], body=body, priority="0.7",
             schemas=[C.crumbs_schema([("Home", "/"), ("Veelgestelde vragen", "/veelgestelde-vragen/"), (t["h1"], path)]), C.faq_schema(t["items"])])


def build(site):
    F = site.get("FAQ_INDEX")
    if not F:
        return
    index_page(site, F)
    for t in site.faq_topics:
        topic_page(site, t)
