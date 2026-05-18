"""
Aplica i18n a las 6 páginas HTML:
- topbar: data-i18n + lang-switcher
- navbar: data-i18n en nav-links + brand-tagline + CTA + mobile switcher
- footer: data-i18n en todos los textos
- Script src="./js/i18n.js"
- data-page-title-key en <html>
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "index.html":       {"titleKey": "hero.indexTitle",    "active": "home"},
    "nosotros.html":    {"titleKey": "hero.aboutTitle",    "active": "about"},
    "servicios.html":   {"titleKey": "hero.servicesTitle", "active": "services"},
    "tarifas.html":     {"titleKey": "hero.pricingTitle",  "active": "pricing"},
    "galeria.html":     {"titleKey": "hero.galleryTitle",  "active": "gallery"},
    "contactanos.html": {"titleKey": "hero.contactTitle",  "active": "contact"},
}

NEW_TOPBAR = '''<div class="topbar">
    <div class="topbar__inner">
        <p class="topbar__contact">
            <a href="tel:+5491123048846" data-i18n-attr="aria-label:topbar.phoneAria"><i class="bi bi-telephone-fill"></i> (+54) 9 11 2304-8846</a>
            <a href="https://wa.me/5491123048846" target="_blank" rel="noopener"><i class="bi bi-whatsapp"></i> <span data-i18n="topbar.whatsapp">WhatsApp</span></a>
        </p>
        <span class="topbar__lang" data-i18n="topbar.support">Atencion 24 hs - Atendimento em portugues</span>
        <div class="lang-switcher lang-switcher--on-dark" data-lang-switcher role="group" aria-label="Idioma">
            <button class="lang-switcher__btn" data-set-lang="es" type="button" aria-pressed="false"><span class="flag">AR</span>ES</button>
            <button class="lang-switcher__btn" data-set-lang="pt" type="button" aria-pressed="false"><span class="flag">BR</span>PT</button>
            <button class="lang-switcher__btn" data-set-lang="en" type="button" aria-pressed="false"><span class="flag">US</span>EN</button>
        </div>
    </div>
</div>'''


def build_navbar(active):
    items = [
        ("home",     "index.html",       "nav.home",     "Inicio"),
        ("about",    "nosotros.html",    "nav.about",    "Nosotros"),
        ("services", "servicios.html",   "nav.services", "Servicios"),
        ("pricing",  "tarifas.html",     "nav.pricing",  "Tarifas"),
        ("gallery",  "galeria.html",     "nav.gallery",  "Galeria"),
        ("contact",  "contactanos.html", "nav.contact",  "Contacto"),
    ]
    lis = []
    for slug, href, key, label in items:
        cls = "nav-link active" if slug == active else "nav-link"
        aria = ' aria-current="page"' if slug == active else ""
        lis.append(f'                <li class="nav-item"><a class="{cls}"{aria} href="{href}" data-i18n="{key}">{label}</a></li>')
    li_block = "\n".join(lis)
    return f'''<nav class="navbar navbar-expand-lg navbar-resmor" id="menu__nav">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.html" aria-label="Resmor - Inicio">
            <span class="brand-text">RESMOR
                <span class="brand-tagline" data-i18n="nav.brandTagline">Minifletes &amp; Transporte Ejecutivo</span>
            </span>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Abrir menu">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarMain">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
{li_block}
            </ul>
            <a class="btn-cta-whatsapp navbar-cta" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener" data-i18n-wa="general">
                <i class="bi bi-whatsapp"></i> <span data-i18n="nav.ctaQuote">Cotizar</span>
            </a>
            <div class="lang-switcher d-lg-none" data-lang-switcher role="group" aria-label="Idioma">
                <button class="lang-switcher__btn" data-set-lang="es" type="button" aria-pressed="false"><span class="flag">AR</span>ES</button>
                <button class="lang-switcher__btn" data-set-lang="pt" type="button" aria-pressed="false"><span class="flag">BR</span>PT</button>
                <button class="lang-switcher__btn" data-set-lang="en" type="button" aria-pressed="false"><span class="flag">US</span>EN</button>
            </div>
        </div>
    </div>
</nav>'''


NEW_FOOTER = '''<footer class="footer-resmor">
    <div class="footer-resmor__inner">
        <div class="footer-resmor__brand">
            <img class="logo-monogram" src="./image/brand/logos/monogram-gold-on-navy.png" alt="Resmor - monograma">
            <p data-i18n="footer.tagline">Minifletes &amp; Transporte Ejecutivo en Buenos Aires. Atendemos en espanol y portugues.</p>
            <div class="footer-resmor__social">
                <a href="https://instagram.com/resmortransportes" target="_blank" rel="noopener" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
                <a href="https://www.facebook.com/Resmor-transportes-293920501123032/" target="_blank" rel="noopener" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
                <a href="https://wa.me/5491123048846" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="bi bi-whatsapp"></i></a>
            </div>
        </div>
        <div class="footer-resmor__col">
            <h4 data-i18n="footer.services">Servicios</h4>
            <ul>
                <li><a href="servicios.html#ejecutivo" data-i18n="servicesSection.executiveTitle">Transporte ejecutivo</a></li>
                <li><a href="servicios.html#aeropuerto" data-i18n="servicesSection.airportTitle">Aeropuerto</a></li>
                <li><a href="servicios.html#minifletes" data-i18n="servicesSection.minifletesTitle">Minifletes</a></li>
                <li><a href="servicios.html#mudanzas" data-i18n="servicesSection.mudanzasTitle">Mudanzas con handyman</a></li>
                <li><a href="servicios.html#logistica" data-i18n="servicesSection.logisticaTitle">Logistica PyMEs</a></li>
                <li><a href="servicios.html#turismo" data-i18n="servicesSection.turismoTitle">Turismo / city tour</a></li>
            </ul>
        </div>
        <div class="footer-resmor__col">
            <h4 data-i18n="footer.company">Empresa</h4>
            <ul>
                <li><a href="nosotros.html" data-i18n="footer.companyAbout">Sobre Resmor</a></li>
                <li><a href="tarifas.html" data-i18n="footer.companyPricing">Tarifas</a></li>
                <li><a href="galeria.html" data-i18n="footer.companyGallery">Galeria</a></li>
                <li><a href="contactanos.html" data-i18n="footer.companyContact">Contacto</a></li>
            </ul>
        </div>
        <div class="footer-resmor__col">
            <h4 data-i18n="footer.contact">Contacto</h4>
            <div class="contact-item"><i class="bi bi-whatsapp"></i><div><span class="channel-label" data-i18n="footer.contactWhatsapp">WhatsApp</span><a href="https://wa.me/5491123048846" target="_blank" rel="noopener">+54 9 11 2304-8846</a></div></div>
            <div class="contact-item"><i class="bi bi-telephone-fill"></i><div><span class="channel-label" data-i18n="footer.contactPhone">Telefono</span><a href="tel:+5491123048846">(+54) 11 2304-8846</a></div></div>
            <div class="contact-item"><i class="bi bi-pin-map"></i><div><span class="channel-label" data-i18n="footer.contactAddress">Direccion</span><span data-i18n="footer.contactAddressValue">Viamonte 2450, Balvanera, CABA</span></div></div>
        </div>
    </div>
    <div class="footer-resmor__bottom">
        <p>Resmor Transportes &copy; <span id="year">2026</span> - <span data-i18n="footer.rights">Todos los derechos reservados</span></p>
    </div>
</footer>'''


NEW_SCRIPTS_TAG = '<script src="./js/i18n.js"></script>'

# Patrones
TOPBAR_RE = re.compile(r'<div class="topbar">.*?</div>\s*</div>', re.DOTALL)
NAV_RE = re.compile(r'<nav class="navbar navbar-expand-lg navbar-resmor" id="menu__nav">.*?</nav>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer class="footer-resmor">.*?</footer>', re.DOTALL)

for page, conf in PAGES.items():
    p = ROOT / page
    if not p.exists():
        print(f"  {page} NO existe, skip")
        continue
    txt = p.read_text(encoding="utf-8")
    original = txt

    # 1) <html> con data-page-title-key
    txt = re.sub(
        r'<html\s+lang="[^"]+"(?:\s+data-page-title-key="[^"]*")?>',
        f'<html lang="es" data-page-title-key="{conf["titleKey"]}">',
        txt,
        count=1
    )

    # 2) Topbar
    if TOPBAR_RE.search(txt):
        txt = TOPBAR_RE.sub(NEW_TOPBAR, txt, count=1)

    # 3) Navbar
    if NAV_RE.search(txt):
        txt = NAV_RE.sub(build_navbar(conf["active"]), txt, count=1)

    # 4) Footer
    if FOOTER_RE.search(txt):
        txt = FOOTER_RE.sub(NEW_FOOTER, txt, count=1)

    # 5) WhatsApp flotante: agregar data-i18n-wa="general"
    txt = re.sub(
        r'<a class="whatsapp-float" href="https://wa\.me/5491123048846[^"]*"((?![^>]*data-i18n-wa)[^>]*)>',
        r'<a class="whatsapp-float" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" data-i18n-wa="general"\1>',
        txt
    )

    # 6) Insertar i18n.js si falta (después del bootstrap bundle)
    if "./js/i18n.js" not in txt:
        txt = txt.replace(
            'crossorigin="anonymous"></script>\n<script src="./main.js"></script>',
            'crossorigin="anonymous"></script>\n<script src="./js/i18n.js"></script>\n<script src="./main.js"></script>'
        )

    if txt != original:
        p.write_text(txt, encoding="utf-8")
        print(f"OK {page} updated")
    else:
        print(f"   {page} no changes")

print("Done.")
