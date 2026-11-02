# -*- coding: utf-8 -*-
"""Homepage van de stads-site, in dezelfde opbouw als de homepage van lachgasbreda.nl:
hero met afbeelding, feitenstrook, assortiment (uitgelichte 2KG + 5 producten), waarom wij + cijfers, bezorggebied, 3 stappen, kennisbank,
donkere servicesectie, FAQ en CTA. Inhoud komt uit content/core_home.py (HOME)."""
import common as C
from common import esc, linkify, faq, cta, BADGE_DARK, CHIP, LINK_CLS, STROKE

ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW2 = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
CHECK_SM = '<span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-gray-900 text-white"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>'
BOOK22 = '<svg width="22" height="22" viewBox="0 0 24 24" %s>%s</svg>' % (STROKE, C.ICON["book"])
ZOOM = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/><path d="M11 8v6M8 11h6"/></svg>'
# producticonen zoals op de Breda-homepage (per formaat een iets bredere tank)
PROD_ICON = {
    "lachgas-tank-2kg": '<rect x="7" y="2" width="10" height="20" rx="4"/><path d="M9 8h6"/>',
    "lachgas-tank-4kg": '<rect x="6" y="2" width="12" height="20" rx="4"/><path d="M9 8h6"/>',
    "lachgas-tank-10kg": '<rect x="5" y="2" width="14" height="20" rx="4"/><path d="M8 8h8"/>',
    "lachgas-cracker": '<rect x="4" y="9" width="16" height="8" rx="3"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/>',
    "slagroompatronen": '<rect x="9" y="3" width="6" height="18" rx="3"/>',
}
DARK_PILL = '<a href="%s" class="rounded-full bg-gray-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-gray-800">%s</a>\n'
CARD_LINK = ('<a href="%s" class="group flex flex-col rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:border-gray-200 hover:-translate-y-1">\n'
             '<div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-gray-900 text-white transition-colors group-hover:bg-brand-600">%s</div>\n'
             '<%s class="mb-2 text-lg font-bold group-hover:text-brand-600">%s</%s>\n'
             '<p class="mb-4 flex-1 text-sm text-gray-500">%s</p>\n'
             '<div class="flex items-center gap-1 text-sm font-semibold group-hover:text-brand-600">%s %s</div>\n</a>\n')
SEC_HEAD = '<div class="mx-auto %s max-w-2xl text-center">\n%s\n<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl%s">%s</h2>\n<p class="%s">%s</p>\n</div>\n'


def card_link(href, title, text, ico, more="Lees meer", tag="h2", arrow=ARROW2):
    return CARD_LINK % (href, ico, tag, esc(title), tag, linkify(text), more, arrow)


def hero(H):
    checks = "".join('<div class="flex items-center gap-3">\n%s\n<span class="text-sm text-gray-700">%s</span>\n</div>\n' % (CHECK_SM, esc(c)) for c in H["checks"])
    alt = esc(H["hero_alt"])
    img = ('<img fetchpriority="high" src="%s" width="1536" height="1024" alt="%s" class="w-full h-auto rounded-2xl cursor-zoom-in" decoding="async" data-lightbox-src="%s" data-lightbox-alt="%s"/>'
           % (C.HERO_IMAGE, alt, C.HERO_IMAGE, alt))
    c1, c2 = H["hero_cards"]
    return ('<section class="relative min-h-[88vh] flex items-center overflow-hidden bg-gradient-to-b from-brand-50 to-white pt-24">\n'
            '<div class="absolute -top-20 -left-20 h-96 w-96 rounded-full bg-brand-200/30 blur-[100px]"></div>\n'
            '<div class="absolute bottom-0 right-0 h-96 w-96 rounded-full bg-whatsapp-500/10 blur-[100px]"></div>\n'
            '<div class="relative mx-auto grid max-w-7xl gap-16 px-4 py-16 sm:px-6 lg:grid-cols-2 lg:items-center lg:px-8">\n<div>\n'
            '<div class="mb-6 inline-flex items-center gap-2 rounded-full bg-white px-4 py-1.5 text-xs font-semibold text-gray-600 shadow-sm border border-gray-100">\n'
            '<span class="relative flex h-2 w-2">\n<span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-whatsapp-500 opacity-75"></span>\n<span class="relative inline-flex h-2 w-2 rounded-full bg-whatsapp-600"></span>\n</span>\n%s\n</div>\n'
            '<h1 class="mb-6 font-heading text-4xl font-extrabold leading-[1.1] tracking-tight sm:text-5xl lg:text-6xl">\n%s<span class="text-brand-600">%s</span>%s\n</h1>\n'
            '<p class="mb-8 max-w-xl text-lg text-gray-500">\n%s\n</p>\n'
            '<div class="mb-8 space-y-3">\n%s</div>\n'
            '<div class="flex flex-col gap-3 sm:flex-row">\n'
            '<a href="%s" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2 rounded-xl bg-whatsapp-600 px-7 py-4 text-base font-bold text-white shadow-lg transition hover:bg-whatsapp-700 hover:shadow-xl active:scale-[0.98]">\n%s\nWhatsApp ons nu\n</a>\n'
            '<a href="/assortiment/" class="inline-flex items-center justify-center gap-2 rounded-xl border-2 border-gray-900 px-7 py-4 text-base font-bold text-gray-900 transition hover:bg-gray-900 hover:text-white">\nBekijk assortiment\n</a>\n'
            '</div>\n</div>\n'
            '<div class="relative hidden lg:block">\n<div class="relative overflow-hidden rounded-3xl bg-gray-900 p-3 shadow-2xl">\n%s\n'
            '<button type="button" class="absolute bottom-5 right-5 flex h-11 w-11 items-center justify-center rounded-full bg-white/90 text-gray-900 shadow-lg backdrop-blur-sm transition hover:bg-white hover:scale-105" data-lightbox-src="%s" data-lightbox-alt="%s" aria-label="Vergroot afbeelding">\n%s\n</button>\n</div>\n'
            '<div class="absolute -top-5 -right-5 rounded-2xl bg-white p-4 shadow-card border border-gray-100">\n<p class="text-xs font-semibold text-gray-500">%s</p>\n<p class="font-heading text-sm font-extrabold text-gray-900">%s</p>\n</div>\n'
            '<div class="absolute -bottom-5 -left-5 rounded-2xl bg-white p-4 shadow-card border border-gray-100">\n<p class="text-xs font-semibold text-gray-500">%s</p>\n<p class="font-heading text-sm font-extrabold text-whatsapp-600">%s</p>\n</div>\n'
            '</div>\n</div>\n</section>\n'
            % (esc(H["badge"]), esc(H["h1_pre"]), esc(H["h1_em"]), esc(H["h1_post"]), linkify(H["lead"]), checks, C.wa_link(), C.icon("wa", 18), img, C.HERO_IMAGE, alt, ZOOM,
               esc(c1[0]), esc(c1[1]), esc(c2[0]), esc(c2[1])))


def stats_strip(H):
    cells = "".join('<div class="rounded-2xl border border-gray-100 bg-white p-5 text-center shadow-card">\n'
                    '<div class="mx-auto mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-gray-900 text-white">%s</div>\n'
                    '<p class="font-heading text-sm font-bold text-gray-900">%s</p>\n<p class="text-xs text-gray-500">%s</p>\n</div>\n' % (C.icon(ic, 20), esc(t), esc(s)) for ic, t, s in H["stats"])
    return '<section class="relative -mt-8 z-10 px-4 sm:px-6 lg:px-8">\n<div class="mx-auto grid max-w-6xl grid-cols-2 gap-4 sm:grid-cols-4">\n%s</div>\n</section>\n' % cells


def assortiment(H):
    A = H["assortiment"]
    pf = A["pf"]
    facts = "".join('<div><dt class="text-gray-500">%s</dt><dd class="text-gray-900">%s</dd></div>' % (esc(k), esc(v)) for k, v in pf["facts"])
    feature = ('<div class="pf border border-gray-100 bg-white shadow-card" data-extra="pf"><div class="pf-img"><img src="/img/lachgastank-2kg.webp" srcset="/img/lachgastank-2kg-300.webp 300w, /img/lachgastank-2kg.webp 480w" sizes="(min-width: 768px) 300px, 70vw" width="480" height="640" alt="Verzegelde lachgastank 2KG van %s" loading="lazy" decoding="async"/></div>'
               '<div><span class="pf-badge mb-4 inline-block rounded-full px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-brand-700">%s</span><h3 class="mb-3 font-heading text-2xl font-bold sm:text-3xl">%s</h3><p class="text-gray-600 leading-relaxed">%s</p>'
               '<dl class="pf-facts">%s</dl><div class="flex flex-wrap gap-3"><a href="/product/lachgas-tank-2kg/" class="rounded-full bg-gray-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-gray-800">Bekijk de 2KG</a>'
               '<a href="%s" target="_blank" rel="noopener" class="inline-flex items-center gap-2 rounded-full bg-whatsapp-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-whatsapp-700">%s Bestel via WhatsApp</a></div>'
               '<p class="pf-note text-xs text-gray-500">%s</p></div></div>\n'
               % (esc(C.BRAND), esc(pf["badge"]), esc(pf["h3"]), linkify(pf["text"]), facts, C.wa_link(), C.icon("wa", 16), esc(pf["note"])))
    cards = ""
    for slug, title, text in A["products"]:
        ico = '<svg width="22" height="22" viewBox="0 0 24 24" %s>%s</svg>' % (STROKE, PROD_ICON[slug])
        cards += card_link("/product/%s/" % slug, title, text, ico, more="Bekijk product", tag="h3", arrow=ARROW)
    cards += ('<a href="/assortiment/" class="group flex flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-200 bg-surface-50 p-6 text-center transition-all duration-300 hover:border-brand-300 hover:bg-brand-50">\n'
              '<div class="mb-3 flex h-14 w-14 items-center justify-center rounded-2xl bg-white text-gray-900 shadow-sm"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>\n'
              '<p class="font-bold text-gray-900">%s</p>\n<p class="text-sm text-gray-500">%s</p>\n</a>\n' % (esc(A["more"][0]), esc(A["more"][1])))
    return ('<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s%s<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s</div>\n</div>\n</section>\n'
            % (SEC_HEAD % ("mb-12", BADGE_DARK % "Assortiment", "", esc(A["h2"]), "text-gray-500", linkify(A["text"])), feature, cards))


def why(H):
    W = H["why"]
    cards = "".join('<div class="rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:-translate-y-1">\n'
                    '<div class="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-gray-900 text-white">%s</div>\n<h3 class="mb-1 font-bold">%s</h3>\n<p class="text-sm text-gray-500">%s</p>\n</div>\n'
                    % (C.icon(ic, 20), esc(t), linkify(x)) for ic, t, x in W["cards"])
    nums = "".join('<div>\n<p class="font-heading text-3xl font-extrabold text-white sm:text-4xl">%s</p>\n<p class="text-sm text-gray-400">%s</p>\n</div>\n' % (esc(b), esc(s)) for b, s in W["numbers"])
    return ('<section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s'
            '<div class="mb-12 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">\n%s</div>\n'
            '<div class="grid grid-cols-2 gap-6 rounded-3xl bg-gray-900 p-8 text-center sm:grid-cols-4 sm:p-12">\n%s</div>\n</div>\n</section>\n'
            % (SEC_HEAD % ("mb-12", BADGE_DARK % "Waarom wij", "", esc(W["h2"]), "text-gray-500", linkify(W["text"])), cards, nums))


def area(site, H):
    A = H["area"]
    def name(slug, fallback):
        return site.place_by[slug]["name"] if slug in site.place_by else fallback
    prim = "".join(DARK_PILL % ("/bezorggebied/%s/" % s, esc(name(s, n))) for s, n in A["primary"])
    sec = "".join(CHIP % ("/bezorggebied/%s/" % s, esc(name(s, n))) for s, n in A["secondary"])
    return ('<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s'
            '<div class="mx-auto mb-4 flex max-w-4xl flex-wrap justify-center gap-3">\n%s</div>\n'
            '<div class="mx-auto mb-8 flex max-w-4xl flex-wrap justify-center gap-3">\n%s</div>\n'
            '<div class="text-center">\n<a href="/bezorggebied/" class="inline-flex items-center gap-1 text-sm font-bold text-brand-600 hover:text-brand-700">Bekijk het volledige bezorggebied %s</a>\n</div>\n</div>\n</section>\n'
            % (SEC_HEAD % ("mb-10", BADGE_DARK % "Bezorggebied", "", esc(A["h2"]), "text-gray-500", linkify(A["text"])), prim, sec, ARROW))


def steps(H):
    S = H["steps"]
    items = "".join('<div class="rounded-2xl border border-gray-100 bg-white p-6 text-center shadow-card">\n'
                    '<div class="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-gray-900 font-heading text-lg font-extrabold text-white">%d</div>\n'
                    '<h3 class="mb-2 font-bold">%s</h3>\n<p class="text-sm text-gray-500">%s</p>\n</div>\n' % (i + 1, esc(t), linkify(x)) for i, (t, x) in enumerate(S["steps"]))
    text = S["text"].replace('<a href="/werkwijze/">', '<a href="/werkwijze/" class="font-semibold text-brand-600 underline">').replace('<a href="/veelgestelde-vragen/">', '<a href="/veelgestelde-vragen/" class="font-semibold text-brand-600 underline">')
    return ('<section data-extra="home" class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s'
            '<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s</div>\n</div>\n</section>\n'
            % (SEC_HEAD % ("mb-12", BADGE_DARK % "Werkwijze", "", esc(S["h2"]), "text-gray-500", linkify(text)), items))


def info(site, H):
    I = H["info"]
    hubs = {h["slug"]: h for h in site.topic_hubs}
    cards = ""
    for slug, title, text in I["cards"]:
        src = hubs.get(slug) or site.art_by.get(slug)
        if src:
            title, text = src["h1"], src["description"]
        cards += card_link("/lachgas-informatie/%s/" % slug, title, text, BOOK22)
    return ('<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s'
            '<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s</div>\n'
            '<div class="mt-10 text-center">\n<a href="/lachgas-informatie/" class="rounded-full bg-gray-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-gray-800">Alle informatie</a>\n</div>\n</div>\n</section>\n'
            % (SEC_HEAD % ("mb-12", BADGE_DARK % "Kennisbank", "", esc(I["h2"]), "text-gray-500", linkify(I["text"])), cards))


def service(site, H):
    S = H["service"]
    cards = ""
    for slug, title, text in S["cards"]:
        src = site.svc_by.get(slug)
        if src:
            title, text = src["h1"], src["description"]
        cards += card_link("/%s/" % slug, title, text, BOOK22)
    head = ('<div class="mx-auto mb-12 max-w-2xl text-center">\n<span class="mb-4 inline-block rounded-full bg-white/10 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">Service</span>\n'
            '<h2 class="mb-4 font-heading text-3xl font-bold text-white sm:text-4xl">%s</h2>\n<p class="text-white/60">%s</p>\n</div>\n' % (esc(S["h2"]), linkify(S["text"])))
    return '<section class="bg-gray-900 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-6xl">\n%s<div class="grid gap-4 sm:grid-cols-2">\n%s</div>\n</div>\n</section>\n' % (head, cards)


def faq_block(H):
    return ('<section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n<div class="mx-auto max-w-3xl">\n'
            '<div class="mx-auto mb-10 max-w-2xl text-center">\n%s\n<h2 class="font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n</div>\n%s</div>\n</section>\n'
            % (BADGE_DARK % "Veelgestelde vragen", esc(H["faq_h2"]), faq(H["faq"])))


def build(site):
    H = site.get("HOME")
    if not H:
        return
    body = hero(H) + stats_strip(H) + assortiment(H) + why(H) + area(site, H) + steps(H) + info(site, H) + service(site, H) + faq_block(H) + cta()
    site.add(path="/", title=H["title"], description=H["description"], body=body, priority="1.0", changefreq="weekly",
             schemas=[C.faq_schema(H["faq"]), C.itemlist_schema("Assortiment %s" % C.BRAND, [("/product/%s/" % s, t) for s, t, _ in H["assortiment"]["products"]])])
