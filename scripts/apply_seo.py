"""
Inyecta SEO mejorado en las 6 páginas HTML:
- canonical
- hreflang alternates (ES, PT, EN, x-default)
- Twitter Card
- og:site_name
- JSON-LD LocalBusiness (en index)
- JSON-LD Service (en servicios)
- JSON-LD BreadcrumbList (en todas excepto index)
- JSON-LD WebSite con SearchAction
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://resmor.com.ar"

PAGES = {
    "index.html":       {"path": "/",                  "name": "Home"},
    "nosotros.html":    {"path": "/nosotros.html",     "name": "Nosotros"},
    "servicios.html":   {"path": "/servicios.html",    "name": "Servicios"},
    "tarifas.html":     {"path": "/tarifas.html",      "name": "Tarifas"},
    "galeria.html":     {"path": "/galeria.html",      "name": "Galeria"},
    "contactanos.html": {"path": "/contactanos.html",  "name": "Contacto"},
}

LOCAL_BUSINESS_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MovingCompany",
  "name": "Resmor Transportes",
  "alternateName": "Resmor",
  "description": "Empresa de transporte ejecutivo y minifletes en Buenos Aires. Mudanzas con handyman, traslados al aeropuerto, logistica para PyMEs. Atendemos en espanol, portugues e ingles.",
  "url": "https://resmor.com.ar/",
  "logo": "https://resmor.com.ar/image/brand/logos/logo-resmor-navy-on-light.png",
  "image": "https://resmor.com.ar/image/brand/marketing/portada-facebook.jpg",
  "telephone": "+54-9-11-2304-8846",
  "priceRange": "$$",
  "foundingDate": "2018",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Viamonte 2450",
    "addressLocality": "Balvanera",
    "addressRegion": "Ciudad Autonoma de Buenos Aires",
    "addressCountry": "AR",
    "postalCode": "C1056"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "-34.605",
    "longitude": "-58.402"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "areaServed": [
    { "@type": "City", "name": "Ciudad Autonoma de Buenos Aires" },
    { "@type": "AdministrativeArea", "name": "Area Metropolitana de Buenos Aires" }
  ],
  "availableLanguage": ["Spanish", "Portuguese", "English"],
  "sameAs": [
    "https://instagram.com/resmortransportes",
    "https://www.facebook.com/Resmor-transportes-293920501123032/"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+54-9-11-2304-8846",
    "contactType": "customer service",
    "areaServed": "AR",
    "availableLanguage": ["es", "pt", "en"]
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://resmor.com.ar/",
  "name": "Resmor Transportes",
  "inLanguage": ["es-AR", "pt-BR", "en-US"],
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://resmor.com.ar/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>'''

SERVICE_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Servicios Resmor",
  "itemListElement": [
    { "@type": "Service", "position": 1, "name": "Transporte ejecutivo", "areaServed": "Buenos Aires", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 2, "name": "Traslado al aeropuerto - Ezeiza / Aeroparque", "areaServed": "Buenos Aires", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 3, "name": "Minifletes - paqueteria y entregas puerta a puerta", "areaServed": "CABA y AMBA", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 4, "name": "Mudanzas con handyman incluido", "areaServed": "CABA y AMBA", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 5, "name": "Logistica para PyMEs - entregas recurrentes", "areaServed": "CABA y AMBA", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 6, "name": "Turismo y city tour", "areaServed": "Buenos Aires", "provider": { "@type": "Organization", "name": "Resmor Transportes" } },
    { "@type": "Service", "position": 7, "name": "Transporte pet-friendly", "areaServed": "CABA y AMBA", "provider": { "@type": "Organization", "name": "Resmor Transportes" } }
  ]
}
</script>'''


def breadcrumb_ld(page_path, page_name):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Inicio", "item": "{BASE_URL}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "{page_name}", "item": "{BASE_URL}{page_path}" }}
  ]
}}
</script>'''


def seo_block(page_path):
    return f'''<link rel="canonical" href="{BASE_URL}{page_path}">
    <link rel="alternate" hreflang="es" href="{BASE_URL}{page_path}">
    <link rel="alternate" hreflang="pt" href="{BASE_URL}{page_path}?lang=pt">
    <link rel="alternate" hreflang="en" href="{BASE_URL}{page_path}?lang=en">
    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{page_path}">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@resmortransportes">
    <meta name="twitter:title" content="Resmor Transportes - Minifletes &amp; Transporte Ejecutivo">
    <meta name="twitter:description" content="Transporte ejecutivo, minifletes y mudanzas con handyman en Buenos Aires. ES / PT / EN.">
    <meta name="twitter:image" content="{BASE_URL}/image/brand/marketing/portada-facebook.jpg">

    <meta property="og:site_name" content="Resmor Transportes">
    <meta property="og:url" content="{BASE_URL}{page_path}">'''


for page, conf in PAGES.items():
    p = ROOT / page
    if not p.exists():
        print(f"  {page} no existe, skip")
        continue
    txt = p.read_text(encoding="utf-8")
    orig = txt

    # 1) Insertar SEO meta antes del </head>
    if "rel=\"canonical\"" not in txt:
        block = seo_block(conf["path"])
        txt = txt.replace("</head>", f"    {block}\n</head>", 1)

    # 2) JSON-LD
    if page == "index.html" and "application/ld+json" not in txt:
        txt = txt.replace("</head>", f"    {LOCAL_BUSINESS_LD}\n</head>", 1)
    elif page == "servicios.html" and "ItemList" not in txt:
        txt = txt.replace("</head>", f"    {SERVICE_LD}\n</head>", 1)
    elif page != "index.html" and "BreadcrumbList" not in txt:
        txt = txt.replace("</head>", f"    {breadcrumb_ld(conf['path'], conf['name'])}\n</head>", 1)

    if txt != orig:
        p.write_text(txt, encoding="utf-8")
        print(f"OK {page} SEO injected")
    else:
        print(f"   {page} ya tenia SEO")

print("\nDone.")
