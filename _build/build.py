#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt de stads-site (familie "stad", zoals lachgasbreda.nl): alle pagina's, sitemap.xml, robots.txt, llms.txt, llms-full.txt, manifest, favicon, 404.
Gebruik (vanuit de repo-root): python3 _build/build.py
Paginatypen: kern (plaats, service, sitemap, 404) in pages.py; home, bezorggebied-index, regio, informatie, producten, FAQ en overige pagina's in pages_*.py
(elke module heeft een functie build(site))."""
import glob
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import common as C  # noqa
import pages as P  # noqa


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def load_content(cdir):
    mods = [load(os.path.join(cdir, f)) for f in sorted(os.listdir(cdir)) if f.endswith(".py") and not f.startswith("_")]
    content = {}
    for m in mods:
        for name in dir(m):
            if not name.isupper(): continue
            v = getattr(m, name)
            if isinstance(v, list):
                content.setdefault(name, []); content[name] += v
            else:
                if name in content: raise KeyError("%s dubbel gedefinieerd (in %s)" % (name, m.__name__))
                content[name] = v
    return content


def write(rel, data, binary=False):
    p = os.path.join(ROOT, rel.lstrip("/")); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb" if binary else "w", **({} if binary else {"encoding": "utf-8"})) as f: f.write(data)


def favicon():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="%s"/><path d="M21.8 16h8.3v25h14.1v7H21.8z" fill="#fff"/></svg>' % C.THEME


def main():
    cdir = os.path.join(HERE, "content")
    C.configure(load(os.path.join(cdir, "_site.py")).SITECFG)
    content = load_content(cdir)
    site = P.Site(content)
    # paginatypen uit pages_*.py (home eerst, daarna alfabetisch)
    mods = sorted(glob.glob(os.path.join(HERE, "pages_*.py")), key=lambda f: (0 if f.endswith("pages_home.py") else 1, f))
    for f in mods:
        load(f).build(site)
    out = site.build_core()
    seen = set()
    for pg in out:
        assert pg["path"] not in seen, "dubbel pad " + pg["path"]; seen.add(pg["path"])
    for pg in out:
        rel = pg["path"]
        if rel.endswith("/"): rel += "index.html"
        write(rel, C.render(pg))
    rows = ["  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>" % (C.SITE, pg["path"], C.TODAY, pg.get("changefreq", "monthly"), pg.get("priority", "0.6"))
            for pg in out if pg.get("sitemap", True) and "noindex" not in pg.get("robots", "")]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % C.SITE)
    write("CNAME", C.CNAME + "\n")
    write("favicon.svg", favicon())
    write("manifest.webmanifest", json.dumps({"name": C.BRAND, "short_name": C.BRAND, "description": C.MANIFEST_DESC, "id": "/", "start_url": "/", "scope": "/", "display": "standalone",
                                             "background_color": "#ffffff", "theme_color": C.THEME, "lang": "nl",
                                             "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2) + "\n")
    write(C.INDEXNOW_KEY + ".txt", C.INDEXNOW_KEY)
    idx = ["# %s" % C.BRAND, "", "> %s %s" % (C.BRAND, C.LLMS_BLURB), "", "Volledige tekst: %s/llms-full.txt" % C.SITE, "", "## Pagina's"]
    full = ["# %s - volledige inhoud" % C.BRAND, "", "WhatsApp: %s | E-mail: %s" % (C.WA_DISPLAY, C.EMAIL), ""]
    for pg in out:
        if not pg.get("sitemap", True) or "noindex" in pg.get("robots", ""): continue
        idx.append("- [%s](%s%s): %s" % (pg["title"], C.SITE, pg["path"], pg["description"]))
        full += ["---", "", "## " + pg["title"], "URL: " + C.SITE + pg["path"], "", C.page_text(pg), ""]
    idx += ["", "## Contact", "- WhatsApp: %s" % C.WA_DISPLAY, "- E-mail: %s" % C.EMAIL, "- Bereikbaar: 24/7", ""]
    write("llms.txt", "\n".join(idx)); write("llms-full.txt", "\n".join(full))
    sys.path.insert(0, os.path.join(HERE, "speed"))
    import apply_speed
    apply_speed.apply(ROOT, "template")
    sys.path.insert(0, os.path.join(HERE, "master"))
    import seo_master
    seo_master.apply_site(ROOT, C.SITE)
    print("%d pagina's gebouwd in %s" % (len(out), ROOT))


if __name__ == "__main__":
    main()
