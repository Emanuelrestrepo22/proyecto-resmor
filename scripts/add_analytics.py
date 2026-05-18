"""
Inserta el script de analytics.js antes de los demás scripts en todas las páginas.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    "index.html",
    "nosotros.html",
    "servicios.html",
    "tarifas.html",
    "galeria.html",
    "contactanos.html",
    "404.html",
    "airport-transfer-buenos-aires.html",
    "transfer-aeroporto-buenos-aires.html",
]

ANALYTICS_TAG = '<script src="./js/analytics.js"></script>'

for page in PAGES:
    p = ROOT / page
    if not p.exists():
        print(f"  {page} no existe, skip")
        continue
    txt = p.read_text(encoding="utf-8")

    if "analytics.js" in txt:
        print(f"   {page} ya tiene analytics.js")
        continue

    # Insertar analytics.js justo después del bootstrap bundle
    new_txt = re.sub(
        r'(<script src="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.1\.2/dist/js/bootstrap\.bundle\.min\.js"[^>]*></script>)',
        r'\1\n' + ANALYTICS_TAG,
        txt,
        count=1
    )

    if new_txt != txt:
        p.write_text(new_txt, encoding="utf-8")
        print(f"OK {page} analytics.js agregado")
    else:
        print(f"   {page} no se pudo insertar (patrón no encontrado)")
