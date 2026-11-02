# -*- coding: utf-8 -*-
"""Paginabouwers voor de stads-site: zetten contentmodules om in pagina-dicts voor common.render().
De kernbouwers (plaats, service, sitemap, 404) staan hier; de overige paginatypen staan in pages_*.py en registreren zich via build(site)."""
import common as C
from common import esc, linkify, section, sec_head, hero_dark, stats, faq, faq_section, chips, chips_section, related_section, cta, p, h2, bullets, notice, prose_sections, why_section, products_section, BADGE_DARK

AREA_DIR = "/bezorggebied"


def area_href(slug):
    return "%s/%s/" % (AREA_DIR, slug)


class Site:
    def __init__(self, content):
        self.c = content
        self.places = content.get("AREAS", [])
        self.services = content.get("SERVICE_PAGES", [])
        self.articles = content.get("ARTICLES", [])
        self.topic_hubs = content.get("TOPIC_HUBS", [])
        self.products = content.get("PRODUCTS", [])
        self.faq_topics = content.get("FAQ_TOPICS", [])
        self.groups = content.get("AREA_GROUPS", [])
        self.place_by = {x["slug"]: x for x in self.places}
        self.svc_by = {x["slug"]: x for x in self.services}
        self.art_by = {x["slug"]: x for x in self.articles}
        self.out = []

    # -- helpers -----------------------------------------------------------------
    def get(self, key, default=None):
        return self.c.get(key, default)

    def place_link(self, slug):
        return (area_href(slug), self.place_by[slug]["name"])

    def title_for(self, path):
        """Linktekst (h1) voor een intern pad, voor 'Verder lezen'-chips."""
        parts = [x for x in path.strip("/").split("/") if x]
        if path == "/lachgas-informatie/":
            return "Alle informatie"
        if len(parts) == 2 and parts[0] == "lachgas-informatie":
            a = self.art_by.get(parts[1])
            if a: return a["h1"]
            for h in self.topic_hubs:
                if h["slug"] == parts[1]: return h["h1"]
        if len(parts) == 2 and parts[0] == "bezorggebied" and parts[1] in self.place_by:
            return self.place_by[parts[1]]["h1"]
        if len(parts) == 2 and parts[0] == "product":
            for pr in self.products:
                if pr["slug"] == parts[1]: return pr["h1"]
        if len(parts) == 2 and parts[0] == "veelgestelde-vragen":
            for t in self.faq_topics:
                if t["slug"] == parts[1]: return t["h1"]
        if len(parts) == 1 and parts[0] in self.svc_by:
            return self.svc_by[parts[0]]["h1"]
        fixed = {"/bezorggebied/": "Bezorggebied", "/assortiment/": "Assortiment", "/veelgestelde-vragen/": "Veelgestelde vragen", "/contact/": "Contact", "/over-ons/": "Over ons",
                 "/werkwijze/": "Zo werkt bestellen", "/bezorggebied/%s/" % C.REGION_SLUG: "Lachgas bezorgen in %s" % C.REGION_NAME}
        return fixed.get(path, path.strip("/").split("/")[-1].replace("-", " ").capitalize())

    def related_links(self, items):
        """items: interne paden of artikel-/service-slugs -> [(href, tekst)]."""
        out = []
        for it in items:
            if it.startswith("/"):
                out.append((it, self.title_for(it)))
            elif it in self.art_by:
                out.append(("/lachgas-informatie/%s/" % it, self.art_by[it]["h1"]))
            elif it in self.svc_by:
                out.append(("/%s/" % it, self.svc_by[it]["h1"]))
            elif it in self.place_by:
                out.append(self.place_link(it))
        return out

    def add(self, **page):
        self.out.append(page)

    # -- plaatspagina --------------------------------------------------------------
    def place_page(self, a):
        path = area_href(a["slug"])
        crumb = [("Home", "/"), ("Bezorggebied", "/bezorggebied/"), (a["name"], None)]
        intro = "".join(p(t) for t in a["intro"])
        intro += '<p class="text-gray-600 leading-relaxed"><strong class="text-gray-900">Buurten en plekken in %s:</strong> %s.</p>\n' % (esc(a["name"]), esc(a["plekken"].rstrip(".")))
        near = [self.place_link(s) for s in a["nearby"] if s in self.place_by] + [("/bezorggebied/", "Bekijk volledig bezorggebied")]
        body = (hero_dark(crumb, "Bezorggebied", a["h1"], a["lead"]) + stats()
                + section(intro)
                + why_section(a["name"])
                + faq_section(a["faq"], "Veelgestelde vragen over lachgas in %s" % a["name"], alt=False)
                + products_section(a["name"])
                + chips_section("Ook actief in de buurt", "Wij bezorgen ook hier", near, alt=True)
                + cta())
        self.add(path=path, title=a["title"], description=a["description"], body=body, priority="0.8", changefreq="weekly",
                 schemas=[C.crumbs_schema([("Home", "/"), ("Bezorggebied", "/bezorggebied/"), (a["name"], path)]),
                          C.service_schema("Lachgas bezorgen in %s" % a["name"], a["description"], path, a["name"], "City", (a["lat"], a["lon"]) if a.get("lat") else None),
                          C.faq_schema(a["faq"])])

    # -- servicepagina -------------------------------------------------------------
    def service_page(self, s):
        path = "/%s/" % s["slug"]
        crumb = [("Home", "/"), (s["h1"], None)]
        rel = self.related_links(s.get("related", [])) + [("/lachgas-informatie/", "Alle informatie")]
        body = (hero_dark(crumb, s["label"], s["h1"], s["lead"])
                + section(prose_sections(s["sections"], s.get("note"), s.get("updated")), width="max-w-3xl")
                + faq_section(s["faq"], "Veelgestelde vragen", alt=True)
                + related_section(rel)
                + cta())
        self.add(path=path, title=s["title"], description=s["description"], body=body, priority="0.7",
                 schemas=[C.crumbs_schema([("Home", "/"), (s["h1"], path)]), C.service_schema(s["h1"], s["description"], path), C.faq_schema(s["faq"])])

    # -- sitemap en 404 ------------------------------------------------------------
    def sitemap_page(self):
        groups = [("Hoofdpagina's", [("/", "Home"), ("/assortiment/", "Assortiment"), ("/bezorggebied/", "Bezorggebied"), ("/lachgas-informatie/", "Lachgas informatie"), ("/veelgestelde-vragen/", "Veelgestelde vragen"), ("/werkwijze/", "Zo werkt bestellen"), ("/over-ons/", "Over ons"), ("/contact/", "Contact")]),
                  ("Bezorggebied", [("/bezorggebied/%s/" % C.REGION_SLUG, C.REGION_NAME)] + [self.place_link(a["slug"]) for a in self.places]),
                  ("Assortiment", [("/product/%s/" % pr["slug"], pr["h1"]) for pr in self.products]),
                  ("Lachgas informatie", [("/lachgas-informatie/%s/" % h["slug"], h["h1"]) for h in self.topic_hubs] + [("/lachgas-informatie/%s/" % a["slug"], a["h1"]) for a in self.articles]),
                  ("Service en bezorging", [("/%s/" % s["slug"], s["h1"]) for s in self.services]),
                  ("Veelgestelde vragen", [("/veelgestelde-vragen/%s/" % t["slug"], t["h1"]) for t in self.faq_topics]),
                  ("Juridisch", [("/algemene-voorwaarden/", "Algemene voorwaarden"), ("/privacy/", "Privacyverklaring")])]
        inner = ""
        for h, items in groups:
            if not items: continue
            inner += '<h2 class="mb-4 mt-10 font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n<ul class="mb-6 grid gap-2 text-gray-600 sm:grid-cols-2">\n%s</ul>\n' % (
                esc(h), "".join('<li><a href="%s" class="%s">%s</a></li>\n' % (u, C.LINK_CLS, esc(n)) for u, n in items))
        body = (hero_dark([("Home", "/"), ("Sitemap", None)], "Overzicht", "Sitemap", "Alle pagina's van %s op een rij." % C.BRAND)
                + section(inner + '<p class="mt-8 text-sm text-gray-500"><a href="/sitemap.xml" class="%s">XML-sitemap voor zoekmachines</a></p>\n' % C.LINK_CLS) + cta())
        self.add(path="/sitemap/", title="Sitemap | %s" % C.BRAND, description="Overzicht van alle pagina's van %s: assortiment, bezorggebied per wijk en plaats, lachgas informatie, service en veelgestelde vragen." % C.BRAND,
                 body=body, priority="0.3", schemas=[C.crumbs_schema([("Home", "/"), ("Sitemap", "/sitemap/")])])

    def not_found(self):
        body = (hero_dark([("Home", "/"), ("Pagina niet gevonden", None)], "404", "Pagina niet gevonden", "Deze pagina bestaat niet (meer). Kies hieronder waar je heen wilt.")
                + section(chips([("/", "Home"), ("/assortiment/", "Assortiment"), ("/bezorggebied/", "Bezorggebied"), ("/lachgas-informatie/", "Lachgas informatie"), ("/veelgestelde-vragen/", "Veelgestelde vragen"), ("/contact/", "Contact")]), center=True) + cta())
        self.add(path="/404.html", title="Pagina niet gevonden | %s" % C.BRAND, description="De opgevraagde pagina bestaat niet. Ga terug naar de homepage van %s of kies een van de hoofdpagina's." % C.BRAND,
                 body=body, robots="noindex, follow", sitemap=False)

    # -- alles ----------------------------------------------------------------------
    def build_core(self):
        for a in self.places: self.place_page(a)
        for s in self.services: self.service_page(s)
        self.sitemap_page(); self.not_found()
        return self.out
