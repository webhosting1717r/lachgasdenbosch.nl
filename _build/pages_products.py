# -*- coding: utf-8 -*-
"""Productpagina's (/product/<slug>/) en de assortimentspagina (/assortiment/) van de stads-site, in de markup van de bestaande stadssites.
Content: PRODUCTS (lijst) en ASSORTIMENT (dict) in content/products.py."""
import common as C
from common import esc, linkify, section, sec_head, hero_dark, faq_section, chips_section, cta, prose_sections, p, BADGE_DARK

# pictogrammen van de productkaarten op de assortimentspagina (per slug), zoals op de bestaande stadssites
CARD_ICON = {
    "lachgas-tank-2kg": '<rect x="7" y="2" width="10" height="20" rx="4"/><path d="M9 8h6"/>',
    "lachgas-tank-4kg": '<rect x="6" y="2" width="12" height="20" rx="4"/><path d="M9 8h6"/>',
    "lachgas-tank-10kg": '<rect x="5" y="2" width="14" height="20" rx="4"/><path d="M8 8h8"/>',
    "lachgas-cracker": '<rect x="4" y="9" width="16" height="8" rx="3"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/>',
    "slagroompatronen": '<rect x="9" y="3" width="6" height="18" rx="3"/>',
}
ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def product_href(slug):
    return "/product/%s/" % slug


def spec_rows(specs):
    return '<div class="rounded-2xl border border-gray-100 bg-white p-6">\n%s</div>' % "".join(
        '<div class="flex justify-between gap-4 border-b border-gray-100 py-3 text-sm"><span class="text-gray-500">%s</span><span class="font-semibold text-gray-900">%s</span></div>\n' % (esc(k), esc(v)) for k, v in specs)


def specs_section(pr):
    """Specificatiekader 'X in het kort'; de 2KG krijgt de productfoto ernaast (pf-spec), de andere producten alleen het kader."""
    head = ('<div class="mb-8 text-center">%s\n<h2 class="font-heading text-3xl font-bold sm:text-4xl">%s in het kort</h2></div>\n' % (BADGE_DARK % "Specificaties", esc(pr["h1"])))
    if pr.get("image"):
        img = ('<div class="pf-img"><img src="/img/lachgastank-2kg.webp" srcset="/img/lachgastank-2kg-300.webp 300w, /img/lachgastank-2kg.webp 480w" sizes="(min-width: 768px) 300px, 70vw" width="480" height="640" alt="Verzegelde %s van %s" loading="lazy" decoding="async"/></div>'
               % (esc(pr["h1"].lower()), esc(C.BRAND)))
        inner = head + '<div class="pf-spec">%s%s</div>\n' % (img, spec_rows(pr["specs"]))
        return '<section class="bg-surface-50 %s">\n<div class="mx-auto pf-wide">\n%s</div>\n</section>\n' % (C.SEC, inner)
    return section(head + spec_rows(pr["specs"]) + "\n", alt=True, width="max-w-3xl")


def product_page(site, pr, all_products):
    path = product_href(pr["slug"])
    crumb = [("Home", "/"), ("Assortiment", "/assortiment/"), (pr["h1"], None)]
    others = [(product_href(x["slug"]), x["h1"]) for x in all_products if x["slug"] != pr["slug"]] + [("/assortiment/", "Volledig assortiment")]
    body = (hero_dark(crumb, "Assortiment", pr["h1"], pr["lead"])
            + section(prose_sections(pr["sections"], pr.get("note"), pr.get("updated")), width="max-w-3xl")
            + specs_section(pr)
            + faq_section(pr["faq"], "Veelgestelde vragen over de %s" % pr["h1"].lower(), alt=False)
            + chips_section("Ook leverbaar", "Andere producten", others, alt=True)
            + cta())
    site.add(path=path, title=pr["title"], description=pr["description"], body=body, priority="0.8",
             schemas=[C.crumbs_schema([("Home", "/"), ("Assortiment", "/assortiment/"), (pr["h1"], path)]),
                      C.product_schema(pr["h1"], pr["description"], path, "/img/lachgastank-2kg.webp" if pr.get("image") else None),
                      C.faq_schema(pr["faq"])])


def product_card(pr):
    return ('<a href="%s" class="group flex flex-col rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:border-gray-200 hover:-translate-y-1">\n'
            '<div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-gray-900 text-white transition-colors group-hover:bg-brand-600"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>\n'
            '<h3 class="mb-2 text-lg font-bold group-hover:text-brand-600">%s</h3>\n'
            '<p class="mb-4 flex-1 text-sm text-gray-500">%s</p>\n'
            '<div class="flex items-center gap-1 text-sm font-semibold group-hover:text-brand-600">Bekijk product %s</div>\n</a>\n'
            % (product_href(pr["slug"]), CARD_ICON.get(pr["slug"], C.ICON["tank"]), esc(pr.get("card_title") or pr["h1"]), esc(pr["lead"]), ARROW))


def wa_card():
    return ('<a href="%s" target="_blank" rel="noopener" class="group flex flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-200 bg-surface-50 p-6 text-center transition-all duration-300 hover:border-whatsapp-400 hover:bg-whatsapp-50">\n'
            '<div class="mb-3 flex h-14 w-14 items-center justify-center rounded-2xl bg-whatsapp-600 text-white shadow-sm">%s</div>\n'
            '<p class="font-bold text-gray-900">Niet zeker welk formaat?</p>\n<p class="text-sm text-gray-500">WhatsApp ons, wij denken mee</p>\n</a>\n' % (C.wa_link(), C.icon("wa", 22)))


def assortiment_page(site, A, products):
    intro = "".join(p(t, last=(i == len(A["intro"]) - 1)) for i, t in enumerate(A["intro"]))
    grid = '<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s%s</div>\n' % ("".join(product_card(pr) for pr in products), wa_card())
    body = (hero_dark([("Home", "/"), ("Assortiment", None)], "Assortiment", A["h1"], A["lead"])
            + section(intro)
            + section(sec_head("Alle producten", A["grid_h2"], A["grid_text"]) + grid, width="max-w-6xl")
            + section(prose_sections(A["sections"], A.get("note"), A.get("updated")), alt=True, width="max-w-3xl")
            + faq_section(A["faq"], A.get("faq_h2", "Vragen over ons assortiment"), alt=False)
            + cta())
    site.add(path="/assortiment/", title=A["title"], description=A["description"], body=body, priority="0.9", changefreq="weekly",
             schemas=[C.crumbs_schema([("Home", "/"), ("Assortiment", "/assortiment/")]),
                      C.itemlist_schema("Assortiment %s" % C.BRAND, [(product_href(pr["slug"]), pr["h1"]) for pr in products]),
                      C.faq_schema(A["faq"])])


def build(site):
    A = site.get("ASSORTIMENT")
    if not A or not site.products:
        return
    for pr in site.products:
        product_page(site, pr, site.products)
    assortiment_page(site, A, site.products)
