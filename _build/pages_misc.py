# -*- coding: utf-8 -*-
"""Overige pagina's van de stads-site: /contact/, /over-ons/, /algemene-voorwaarden/ en /privacy/ (ontwerp 1-op-1 als de bestaande stadssites).
Content: CONTACT, ABOUT, TERMS, PRIVACY in content/misc.py."""
import common as C
from common import esc, linkify, section, hero_dark, prose_sections, related_section, cta, icon

FIELD = "w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 shadow-sm placeholder:text-gray-400 focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-500/20"
LEGAL_LINK = "font-semibold text-brand-600 underline"


def legal_linkify(s):
    """Links in de juridische teksten krijgen, zoals op de bestaande stadssites, een onderstreping in plaats van de hover-kleur."""
    import re
    return re.sub(r'<a href="([^"]+)">', lambda m: '<a href="%s" class="%s"%s>' % (m.group(1), LEGAL_LINK, ' target="_blank" rel="noopener"' if m.group(1).startswith("http") else ""), s)


def contact_card(href, ico, dark, title, sub, bg="bg-white", shadow=True):
    tag = "a" if href else "div"
    attrs = (' href="%s"' % href) if href else ""
    if href and href.startswith("http"):
        attrs += ' target="_blank" rel="noopener"'
    cls = "flex items-center gap-4 rounded-2xl border border-gray-100 %s p-5%s" % (bg, " shadow-card transition hover:-translate-y-1" if shadow else "")
    return ('<%s%s class="%s">\n<span class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl %s text-white">%s</span>\n'
            '<span>\n<span class="block font-bold text-gray-900">%s</span>\n<span class="block text-sm text-gray-500">%s</span>\n</span>\n</%s>\n'
            % (tag, attrs, cls, "bg-whatsapp-600" if dark == "wa" else "bg-gray-900", ico, esc(title), sub, tag))


def contact_page(site):
    P = site.get("CONTACT")
    path = "/contact/"
    intro = '<section class="%s" data-intro="site">\n<div class="mx-auto max-w-4xl">\n%s</div>\n</section>\n' % (
        C.SEC, "".join('<p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % linkify(t) for t in P["intro"]))
    cards = (contact_card(C.wa_link(), icon("wa", 22), "wa", "WhatsApp: %s" % C.WA_DISPLAY, esc(P["wa_sub"]))
             + contact_card("mailto:" + C.EMAIL, icon("mail", 20), "dark", "E-mail", esc(C.EMAIL))
             + contact_card(None, icon("clock", 20), "dark", P["hours_label"], esc(P["hours_text"]), bg="bg-surface-50", shadow=False)
             + contact_card(None, icon("pin", 20), "dark", "Bezorggebied", esc(C.AREA_LINE) + " &amp; wijken", bg="bg-surface-50", shadow=False))
    options = "".join("<option>%s</option>\n" % esc(o) for o in P["form_options"])
    form = ('<div class="rounded-2xl border border-gray-100 bg-surface-50 p-6 shadow-card sm:p-8">\n'
            '<h2 class="mb-1 font-heading text-2xl font-bold">%s</h2>\n<p class="mb-6 text-sm text-gray-500">%s</p>\n'
            '<form action="mailto:%s?subject=%s" method="post" enctype="text/plain" class="space-y-5">\n'
            '<div class="grid gap-5 sm:grid-cols-2">\n<div>\n'
            '<label for="f-naam" class="mb-1.5 block text-sm font-medium text-gray-900">Naam <span class="text-cta-600">*</span></label>\n'
            '<input type="text" id="f-naam" name="naam" required autocomplete="name" class="%s" placeholder="Je naam"/>\n</div>\n<div>\n'
            '<label for="f-telefoon" class="mb-1.5 block text-sm font-medium text-gray-900">Telefoon / WhatsApp</label>\n'
            '<input type="tel" id="f-telefoon" name="telefoon" autocomplete="tel" class="%s" placeholder="06 12 34 56 78"/>\n</div>\n</div>\n<div>\n'
            '<label for="f-email" class="mb-1.5 block text-sm font-medium text-gray-900">E-mailadres <span class="text-cta-600">*</span></label>\n'
            '<input type="email" id="f-email" name="email" required autocomplete="email" class="%s" placeholder="naam@voorbeeld.nl"/>\n</div>\n<div>\n'
            '<label for="f-onderwerp" class="mb-1.5 block text-sm font-medium text-gray-900">Waarmee kunnen we helpen?</label>\n'
            '<select id="f-onderwerp" name="onderwerp" class="w-full rounded-xl border border-gray-200 bg-white px-4 py-3 text-gray-900 shadow-sm focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-500/20">\n%s</select>\n</div>\n<div>\n'
            '<label for="f-regio" class="mb-1.5 block text-sm font-medium text-gray-900">Wijk / plaats</label>\n'
            '<input type="text" id="f-regio" name="regio" class="%s" placeholder="%s"/>\n</div>\n<div>\n'
            '<label for="f-bericht" class="mb-1.5 block text-sm font-medium text-gray-900">Bericht <span class="text-cta-600">*</span></label>\n'
            '<textarea id="f-bericht" name="bericht" required rows="4" class="%s" placeholder="Vertel ons wat je nodig hebt..."></textarea>\n</div>\n'
            '<button type="submit" class="w-full rounded-xl bg-brand-600 px-6 py-4 text-base font-bold text-white shadow-lg transition hover:bg-brand-700 hover:shadow-xl active:scale-[0.99]">Verstuur bericht</button>\n'
            '<p class="text-center text-xs text-gray-500">%s</p>\n</form>\n</div>\n'
            % (esc(P["form_h2"]), esc(P["form_text"]), C.EMAIL, C.quote("Bericht via %s" % C.CNAME), FIELD, FIELD, FIELD, options, FIELD, esc(P["form_place_placeholder"]), FIELD,
               P["form_consent"].replace('<a href="/privacy/">', '<a href="/privacy/" class="underline">')))
    grid = ('<section class="%s">\n<div class="mx-auto grid max-w-6xl gap-10 lg:grid-cols-5">\n<div class="lg:col-span-2">\n'
            '<h2 class="mb-6 font-heading text-2xl font-bold">%s</h2>\n<div class="space-y-4">\n%s</div>\n</div>\n<div class="lg:col-span-3">\n%s</div>\n</div>\n</section>\n'
            % (C.SEC, esc(P["cards_h2"]), cards, form))
    body = hero_dark([("Home", "/"), ("Contact", None)], "Contact", P["h1"], P["lead"]) + intro + grid
    schema = C.webpage_schema(P["title"], P["description"], path, typ="ContactPage")
    schema["mainEntity"] = {"@id": C.SITE + "/#business"}
    site.add(path=path, title=P["title"], description=P["description"], body=body, priority="0.7",
             schemas=[C.crumbs_schema([("Home", "/"), ("Contact", path)]), schema])


def about_page(site):
    P = site.get("ABOUT")
    path = "/over-ons/"
    rel = site.related_links(P["related"])
    body = (hero_dark([("Home", "/"), (P["h1"], None)], "Over ons", P["h1"], P["lead"])
            + section(prose_sections(P["sections"], P.get("note"), P.get("updated")), width="max-w-3xl")
            + related_section(rel, badge="Meer over ons", alt=True)
            + cta())
    schema = C.webpage_schema(P["title"], P["description"], path, typ="AboutPage")
    schema["mainEntity"] = {"@id": C.SITE + "/#business"}
    site.add(path=path, title=P["title"], description=P["description"], body=body, priority="0.6",
             schemas=[C.crumbs_schema([("Home", "/"), (P["h1"], path)]), schema])


def legal_body(P):
    """Juridische tekst: korte koppen (text-xl) met ruim gespatieerde alinea's, exact zoals de voorwaarden- en privacypagina's van de stadssites."""
    out = ['<p class="mb-8 text-sm text-gray-500">Laatst bijgewerkt: %s</p>' % esc(P.get("updated") or C.MONTH_NL)]
    arts = P["articles"]
    for i, a in enumerate(arts):
        last_art = i == len(arts) - 1
        out.append('<h2 class="mb-3 font-heading text-xl font-bold">%s</h2>' % esc(a["h2"]))
        paras, bl, after = a.get("paragraphs", []), a.get("bullets", []), a.get("after", [])
        for j, t in enumerate(paras):
            final = last_art and not bl and not after and j == len(paras) - 1
            out.append('<p class="%s">%s</p>' % ("text-gray-600 leading-relaxed" if final else ("mb-4 text-gray-600 leading-relaxed" if bl else "mb-8 text-gray-600 leading-relaxed"), legal_linkify(t)))
        if bl:
            out.append('<ul class="mb-8 space-y-2 text-gray-600">\n%s</ul>' % "".join('<li class="flex gap-3"><span class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-brand-600"></span><span>%s</span></li>\n' % legal_linkify(b) for b in bl))
        for j, t in enumerate(after):
            final = last_art and j == len(after) - 1
            out.append('<p class="%s">%s</p>' % ("text-gray-600 leading-relaxed" if final else "mb-8 text-gray-600 leading-relaxed", legal_linkify(t)))
    return "".join(out) + "\n"


def legal_page(site, key, path, crumb, h1_badge="Juridisch"):
    P = site.get(key)
    body = (hero_dark([("Home", "/"), (crumb, None)], h1_badge, P["h1"], P["lead"])
            + section(legal_body(P), width="max-w-3xl")
            + cta(P["cta_h2"], P["cta_text"]))
    site.add(path=path, title=P["title"], description=P["description"], body=body, priority="0.3",
             schemas=[C.crumbs_schema([("Home", "/"), (crumb, path)]), C.webpage_schema(P["title"], P["description"], path)])


def build(site):
    if not site.get("CONTACT"):
        return
    contact_page(site)
    about_page(site)
    legal_page(site, "TERMS", "/algemene-voorwaarden/", "Algemene voorwaarden")
    legal_page(site, "PRIVACY", "/privacy/", "Privacy")
