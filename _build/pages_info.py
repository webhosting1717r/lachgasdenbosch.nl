# -*- coding: utf-8 -*-
"""Informatiepagina's van de stads-site: artikelen (/lachgas-informatie/<slug>/), thema-hubs en de informatie-index.
Markup 1-op-1 overgenomen van de bestaande stadssites (lachgasbreda.nl)."""
import re

import common as C
from common import esc, linkify, section, hero_dark, faq_section, related_section, cta, p, bullets, notice, h3, BADGE_DARK, SEC

INFO = "/lachgas-informatie/"
ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
ARROW2 = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SVG22 = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>'

# iconen per kaart op de index (zoals op de bestaande stadssites); alles zonder eigen icoon krijgt het tank/cracker-icoon
ICON_BOOK = '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'
ICON_DEFAULT = '<rect x="4" y="9" width="16" height="8" rx="3"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/>'
CARD_ICONS = {
    "wat-is-lachgas": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "is-lachgas-legaal-in-nederland": '<path d="m12 3-8 4v5c0 5 3.5 8 8 9 4.5-1 8-4 8-9V7l-8-4Z"/>',
    "veilig-gebruik": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>',
    "lachgas-in-het-verkeer": '<rect x="3" y="11" width="18" height="7" rx="2"/><path d="M5 11 7 6h10l2 5"/><circle cx="7.5" cy="18.5" r="1.5"/><circle cx="16.5" cy="18.5" r="1.5"/>',
}


def slug_id(t):
    s = C.strip_tags(t).lower()
    for a, b in (("ë", "e"), ("é", "e"), ("è", "e"), ("ï", "i"), ("ö", "o"), ("ü", "u"), ("'", "-"), ("’", "-")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70]


def info_card(href, title, text, icon_path=ICON_BOOK, more="Lees meer", arrow=ARROW, span2=False, extra_attr=""):
    return ('<a%s href="%s" class="group flex flex-col rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:border-gray-200 hover:-translate-y-1%s">\n'
            '<div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-gray-900 text-white transition-colors group-hover:bg-brand-600">%s</div>\n'
            '<h2 class="mb-2 text-lg font-bold group-hover:text-brand-600">%s</h2>\n'
            '<p class="mb-4 flex-1 text-sm text-gray-500">%s</p>\n'
            '<div class="flex items-center gap-1 text-sm font-semibold group-hover:text-brand-600">%s %s</div>\n</a>\n'
            % ((" " + extra_attr) if extra_attr else "", href, " sm:col-span-2" if span2 else "", SVG22 % icon_path, esc(title), esc(text), esc(more), arrow))


def article_body(a, month):
    secs = a["sections"]
    heads = [(slug_id(s["h2"]), s["h2"]) for s in secs]
    words = sum(len(C.strip_tags(x).split()) for s in secs for x in s.get("paragraphs", []) + s.get("bullets", []) + [y for sub in s.get("subsections", []) for y in sub.get("paragraphs", []) + sub.get("bullets", [])])
    mins = max(1, round(words / 220))
    out = ['<p class="mb-8 text-sm text-gray-500" data-extra="article">Laatst bijgewerkt: %s &middot; Leestijd ongeveer %d %s &middot; Geschreven en gecontroleerd door het team van %s</p>\n'
           % (esc(month), mins, "minuut" if mins == 1 else "minuten", esc(C.BRAND))]
    if len(secs) >= 4:
        out.append('<nav aria-label="Inhoud" class="mb-10 rounded-2xl border border-gray-100 bg-surface-50 p-6" data-extra="article">\n<p class="mb-3 text-xs font-bold uppercase tracking-wide text-gray-500">Op deze pagina</p>\n<ol class="space-y-2 text-sm">\n%s</ol>\n</nav>\n'
                   % "".join('<li><a href="#%s" class="%s">%d. %s</a></li>\n' % (hid, C.LINK_CLS, i + 1, esc(t)) for i, (hid, t) in enumerate(heads)))
    for i, ((hid, _), s) in enumerate(zip(heads, secs)):
        out.append('<h2 class="mb-4%s font-heading text-2xl font-bold sm:text-3xl" id="%s">%s</h2>\n' % ("" if i == 0 else " mt-10", hid, esc(s["h2"])))
        for t in s.get("paragraphs", []):
            out.append(p(t))
        if s.get("bullets"):
            out.append(bullets(s["bullets"]))
        for sub in s.get("subsections", []):
            out.append(h3(sub["h3"]))
            for t in sub.get("paragraphs", []):
                out.append(p(t))
            if sub.get("bullets"):
                out.append(bullets(sub["bullets"]))
    if a.get("note"):
        out.append(notice(a["note"]))
    out.append('<div class="mt-10 rounded-2xl border border-gray-100 bg-white p-6">\n<p class="mb-3 text-xs font-bold uppercase tracking-wide text-gray-500">Over deze informatie</p>\n'
               '<p class="text-sm text-gray-500 leading-relaxed">Deze pagina is geschreven en nagekeken door het team van %s en wordt bijgewerkt als regels of inzichten veranderen. Wij leveren uitsluitend aan volwassenen van 18 jaar en ouder en geven bewust geen gebruiksinstructies. Vraag of fout gezien? <a href="/contact/" class="%s">Neem contact met ons op</a>.</p>\n</div>\n'
               % (esc(C.BRAND), C.LINK_CLS))
    return "".join(out)


def article_page(site, a):
    path = INFO + a["slug"] + "/"
    crumb = [("Home", "/"), ("Lachgas Informatie", INFO), (a["h1"], None)]
    rel = site.related_links(a.get("related", [])) + [(INFO, "Alle informatie")]
    body = (hero_dark(crumb, a["label"], a["h1"], a["lead"])
            + section(article_body(a, a.get("updated") or C.MONTH_NL), width="max-w-3xl")
            + related_section(rel, alt=True)
            + cta())
    site.add(path=path, title=a["title"], description=a["description"], body=body, og_type="article", priority="0.7",
             schemas=[C.crumbs_schema([("Home", "/"), ("Lachgas Informatie", INFO), (a["h1"], path)]), C.article_schema(a["title"], a["description"], path)])


def topic_page(site, h):
    path = INFO + h["slug"] + "/"
    crumb = [("Home", "/"), ("Lachgas Informatie", INFO), (h["h1"], None)]
    body = hero_dark(crumb, h.get("label", "Thema"), h["h1"], h["lead"])
    body += section("".join(p(t) for t in h["intro"]))
    listed = []
    for i, g in enumerate(h["groups"]):
        arts = [site.art_by[s] for s in g["slugs"] if s in site.art_by]
        if not arts:
            continue
        listed += [a["slug"] for a in arts]
        head = ('<div class="mx-auto mb-12 max-w-2xl text-center">\n%s\n<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n%s</div>\n'
                % (BADGE_DARK % "Thema", esc(g["h2"]), ('<p class="text-gray-500">%s</p>\n' % linkify(g["text"])) if g.get("text") else ""))
        grid = '<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s</div>\n' % "".join(info_card(INFO + a["slug"] + "/", a["h1"], a["description"]) for a in arts)
        body += section(head + grid, alt=(i % 2 == 0), width="max-w-6xl")
    body += faq_section(h["faq"], "Veelgestelde vragen", alt=False)
    body += cta()
    site.add(path=path, title=h["title"], description=h["description"], body=body, priority="0.8",
             schemas=[C.crumbs_schema([("Home", "/"), ("Lachgas Informatie", INFO), (h["h1"], path)]), C.faq_schema(h["faq"]),
                      C.webpage_schema(h["title"], h["description"], path, "CollectionPage"),
                      C.itemlist_schema(h["h1"], [(INFO + s + "/", site.art_by[s]["h1"]) for s in listed])])


def info_index(site, I):
    hubs = site.topic_hubs
    order = []
    for g in I.get("groups", []):
        order += [s for s in g["slugs"] if s in site.art_by and s not in order]
    order += [a["slug"] for a in site.articles if a["slug"] not in order]
    featured = [s for s in I.get("featured", []) if s in site.art_by][:6]
    rest = [s for s in order if s not in featured]
    cards = ""
    for i, h in enumerate(hubs):
        cards += info_card(INFO + h["slug"] + "/", h["h1"], h["description"], ICON_BOOK, "Bekijk het thema", ARROW, extra_attr='data-extra="hubs"' if i == 0 else "")
    for s in featured:
        a = site.art_by[s]
        cards += info_card(INFO + s + "/", a["h1"], a["description"], CARD_ICONS.get(s, ICON_DEFAULT), "Lees meer", ARROW2)
    for s in rest:
        a = site.art_by[s]
        cards += info_card(INFO + s + "/", a["h1"], a["description"], CARD_ICONS.get(s, ICON_DEFAULT), "Lees meer", ARROW2, span2=True)
    body = (hero_dark([("Home", "/"), ("Lachgas Informatie", None)], "Lachgas Informatie", I["h1"], I["lead"])
            + section("".join(p(t) for t in I["intro"]), attrs='data-intro="site"')
            + section('<div class="grid gap-4 sm:grid-cols-2">\n%s</div>\n' % cards, width="max-w-5xl")
            + cta("Nog een vraag?", "Stuur ons een bericht op WhatsApp, wij helpen je graag verder."))
    items = [(INFO + h["slug"] + "/", h["h1"]) for h in hubs] + [(INFO + s + "/", site.art_by[s]["h1"]) for s in featured + rest]
    site.add(path=INFO, title=I["title"], description=I["description"], body=body, priority="0.9",
             schemas=[C.crumbs_schema([("Home", "/"), ("Lachgas Informatie", INFO)]), C.itemlist_schema("Lachgas informatie", items)])


def build(site):
    for a in site.articles:
        article_page(site, a)
    for h in site.get("TOPIC_HUBS", []):
        topic_page(site, h)
    I = site.get("INFO_INDEX")
    if not I:
        return
    info_index(site, I)
