"""
Migra todos los parciales SCSS de @import → @use "variables" as *;
y reescribe estilo.scss con @use en lugar de @import.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "scss"

# Parciales que usan variables/mixins de _variables.scss
PARTIALS_USING_VARS = [
    "_1encabezado.scss",
    "_2barra-nav.scss",
    "_3hero.scss",
    "_4servicios.scss",
    "_5galeria.scss",
    "_6acerca-nosotros.scss",
    "_7ubi-information.scss",
    "_8formulario.scss",
    "_9footer.scss",
    "_10whatsapp-float.scss",
    "_11lang-switcher.scss",
    "_base.scss",
    "_typography.scss",
    "_bootstrap-overrides.scss",
    "_responsive.scss",
]

USE_LINE = '@use "variables" as *;\n\n'

for name in PARTIALS_USING_VARS:
    p = ROOT / name
    if not p.exists():
        print(f"  {name} no existe, skip")
        continue
    txt = p.read_text(encoding="utf-8")

    if "@use \"variables\"" in txt or "@use 'variables'" in txt:
        print(f"   {name} ya tiene @use")
        continue

    # Remover @import "variables" si existe
    txt = re.sub(r'@import\s+["\']variables["\'];\s*\n?', '', txt)

    # Insertar @use al principio del archivo, después del comment block inicial si lo hay
    # Si empieza con // o /* ... */, insertar después del bloque de comentarios iniciales
    lines = txt.split("\n")
    insert_idx = 0
    in_block_comment = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("//"):
            continue
        if stripped.startswith("/*"):
            in_block_comment = True
            if "*/" in stripped:
                in_block_comment = False
            continue
        if in_block_comment:
            if "*/" in stripped:
                in_block_comment = False
            continue
        insert_idx = i
        break

    new_lines = lines[:insert_idx] + [USE_LINE.rstrip()] + [""] + lines[insert_idx:]
    new_txt = "\n".join(new_lines)
    p.write_text(new_txt, encoding="utf-8")
    print(f"OK {name} agregado @use")

# Reescribir estilo.scss con @use en lugar de @import
ESTILO = ROOT / "estilo.scss"
new_estilo = '''// ═══════════════════════════════════════════════════════════════
// RESMOR — ENTRY SCSS
// Fuente: PRESENTACION_RESMOR.pdf (manual oficial, 2018)
// Stack: HTML5 + Bootstrap 5.1 (CDN) + Sass (Dart, @use moderna)
// ═══════════════════════════════════════════════════════════════

// 1. Tokens (cargado primero, una sola vez)
@use "variables";

// 2. Base + tipografía
@use "base";
@use "typography";

// 3. Overrides de Bootstrap
@use "bootstrap-overrides";

// 4. Componentes globales
@use "1encabezado";
@use "2barra-nav";
@use "3hero";
@use "4servicios";
@use "5galeria";
@use "6acerca-nosotros";
@use "7ubi-information";
@use "8formulario";
@use "9footer";
@use "10whatsapp-float";
@use "11lang-switcher";

// 5. Responsive overrides al final
@use "responsive";
'''
ESTILO.write_text(new_estilo, encoding="utf-8")
print("OK estilo.scss reescrito con @use")
print("\nMigración completa.")
