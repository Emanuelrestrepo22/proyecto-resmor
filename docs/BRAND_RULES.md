# BRAND_RULES — Resmor

**Última actualización:** 2026-05-17 (v3 — basada en manual oficial `PRESENTACION_RESMOR.pdf`)
**Mantenido por:** AGT-03 Documentation
**Estado:** Definitivo en colores, tipografía y tagline. Foto/copy/voz: pendiente de validación final.

> **Fuente de verdad:** `image/brand/PRESENTACION_RESMOR.pdf` (manual de marca oficial de Resmor, 24 páginas).
>
> Documentos hermanos:
> - [`docs/brand/BRAND_MARKETING_NOTES.md`](brand/BRAND_MARKETING_NOTES.md) — tono, copy y narrativa
> - [`docs/brand/BRAND_IMPLEMENTATION_NOTES.md`](brand/BRAND_IMPLEMENTATION_NOTES.md) — tokens SCSS y componentes
> - [`image/brand/README.md`](../image/brand/README.md) — inventario completo de assets

---

## 1. Identidad oficial

| Elemento                  | Valor oficial (del manual)                                |
| ------------------------- | --------------------------------------------------------- |
| Marca                     | **RESMOR**                                                |
| Categoría / claim         | **TRANSPORTE EJECUTIVO**                                  |
| Tagline operativo         | **Minifletes & Transporte Ejecutivo**                    |
| Símbolo                   | Wordmark RESMOR + alas / Monograma R con alas             |
| Año del manual            | 2018 (Photoshop CC 2019, archivos 2018-12-10)             |

**Implicación estratégica:** la marca se posiciona oficialmente como **Transporte Ejecutivo** — los minifletes son un servicio bundled, no la oferta central. Mudanzas con handyman, traslados al aeropuerto y logística son **extensiones** del rubro ejecutivo.

---

## 2. Esencia de marca (atributos del manual)

| Pilar             | Color asociado | Atributos verbales oficiales (manual pág. 6-9, 11)         |
| ----------------- | -------------- | ----------------------------------------------------------- |
| **Confianza**     | Azul           | Amabilidad, simpatía, seguridad, confianza                 |
| **Distinción**    | Dorado         | Glamour, éxito, fidelidad, riqueza, belleza                |
| **Modernidad**    | Tipografía     | Moderna, elegante, alegre                                  |

**Síntesis narrativa:**

> Resmor combina **la confianza de un transporte ejecutivo serio** con **la distinción de un servicio premium accesible** — todo en una marca moderna, elegante y siempre disponible.

---

## 3. Paleta oficial

### Colores corporativos primarios

| Token                    | Pantone     | Hex (sRGB)  | CMYK (PDF)                       | Significado                                    |
| ------------------------ | ----------- | ----------- | -------------------------------- | ---------------------------------------------- |
| `$color-brand-azul`      | 2768 C      | `#0F1B49`   | `(100, 91, 42, 43)` *aprox*      | Amabilidad, simpatía, seguridad, confianza    |
| `$color-brand-dorado`    | 4525 C      | `#B0A56A`   | `(25, 22, 53, 5)` *aprox*        | Glamour, éxito, fidelidad, riqueza, belleza   |

> Los hex sRGB son la conversión web-estándar de los Pantone declarados. El CMYK del PDF original es `(100, 90.7, 42.2, 43.3)` para el azul y `(24.8, 22.2, 53.4, 4.9)` para el dorado.

### Tonalidades operativas (derivadas, no oficiales — para web)

| Token                       | Hex         | Uso                                                |
| --------------------------- | ----------- | -------------------------------------------------- |
| `$color-brand-azul-deep`    | `#0A1238`   | Hover/active sobre azul                            |
| `$color-brand-azul-soft`    | `#1B2A66`   | Acentos secundarios sobre fondo claro              |
| `$color-brand-dorado-light` | `#D4CB9B`   | Hover suave, divisores, badges                     |
| `$color-brand-dorado-dark`  | `#8C8350`   | Acentos sobre fondo claro con contraste suficiente |

### Neutros

| Token                    | Hex         | Uso                                            |
| ------------------------ | ----------- | ---------------------------------------------- |
| `$color-bg-base`         | `#FFFFFF`   | Fondo principal                                |
| `$color-bg-soft`         | `#F4F2EC`   | Fondo cálido suave (compañero del dorado)     |
| `$color-bg-cool`         | `#F3F3F3`   | Fondo neutro frío (compañero del azul)        |
| `$color-text-primary`    | `#0F1B49`   | Texto principal (= brand-azul)                |
| `$color-text-secondary`  | `#4A5170`   | Texto secundario                               |
| `$color-text-muted`      | `#8A8FA3`   | Captions, metadata                             |
| `$color-text-on-dark`    | `#F4F2EC`   | Texto sobre fondo azul                         |
| `$color-border`          | `#E5E7ED`   | Bordes suaves                                  |

### Funcionales

| Token              | Hex         | Uso                                |
| ------------------ | ----------- | ---------------------------------- |
| `$color-whatsapp`  | `#25D366`   | Verde WhatsApp oficial             |
| `$color-success`   | `#2EA44F`   | Mensajes de éxito                  |
| `$color-warning`   | `#D4A017`   | Avisos                             |
| `$color-error`     | `#CF222E`   | Errores                            |

### Reglas de uso

- **Azul** es el color dominante: títulos, navbar, footer, texto de marca, fondos premium.
- **Dorado** es el acento de distinción: alas del logo, líneas separadoras, íconos premium, CTA puntual de "transporte ejecutivo". **Máximo 1 botón dorado por página.**
- **Blanco** sobre azul = combinación primaria del logo en piezas promocionales.
- **Dorado sobre azul oscuro** = combinación premium para el monograma.
- **Nunca usar el dorado para texto pequeño sobre blanco** (contraste insuficiente — ver sección 11).
- **Nunca introducir colores fuera de esta paleta** sin actualizar este documento.

---

## 4. Tipografía oficial

**Fuente corporativa:** **AVERTA** (manual pág. 10-13)
**Atributos:** moderna, elegante, alegre.
**Variantes oficiales:**

- AVERTA DEMO REGULAR — para cuerpo y elementos secundarios
- AVERTA DEMO EXTRABOLD ITALIC — para títulos, hero, acentos

### Estrategia web

Averta es una fuente comercial de Kostic Type Foundry (no está en Google Fonts). Opciones para web:

| Opción                                    | Pros                                                                  | Contras                                  |
| ----------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------- |
| **Adobe Fonts (Averta Std)**              | Familia oficial, mismo look                                           | Requiere cuenta Adobe + Web Project ID   |
| **Self-host Averta Demo**                 | Idéntica a la del manual                                              | Hay que comprar/licenciar las WOFF2      |
| **Inter (Google Fonts)** ⭐ recomendada   | Geometría muy similar a Averta, peso 100-900, free                   | No es exactamente Averta                 |
| **Manrope (Google Fonts)**                | Cercana a Averta, gratuita                                            | Más "rounded" que Averta                 |

**Decisión recomendada para web (a validar con el dueño):**

- **Hero y títulos:** Inter peso 800 italic (sustituto de Averta Demo Extrabold Italic)
- **Cuerpo:** Inter peso 400 (sustituto de Averta Demo Regular)
- **Tagline pequeño:** Inter peso 500 uppercase letterspacing 0.08em (similar al subtítulo del logo)

Si en algún momento se compra Averta o se suscribe a Adobe Fonts, sustituir Inter por Averta sin cambiar pesos.

### Tokens tipográficos

```scss
$font-display:  'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif; // sustituto Averta
$font-body:     'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;

// Si se compra Averta:
// $font-display: 'Averta Demo', 'Inter', system-ui, sans-serif;
// $font-body:    'Averta', 'Inter', system-ui, sans-serif;
```

### Carga vía Google Fonts (Inter)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
```

### Escala (mantener clamp fluido)

| Elemento              | Familia      | Peso       | Tamaño fluido                  | Estilo            |
| --------------------- | ------------ | ---------- | ------------------------------ | ----------------- |
| Display / Hero H1     | Inter        | 800 italic | `clamp(2.5rem, 5vw, 4rem)`    | uppercase opc.    |
| H1 sección            | Inter        | 700        | `clamp(2rem, 3.5vw, 2.75rem)` | tracking -0.02em  |
| H2                    | Inter        | 700        | `clamp(1.5rem, 2.5vw, 2rem)`  |                   |
| H3 card               | Inter        | 600        | `clamp(1.25rem, 1.8vw, 1.5rem)` |                 |
| Cuerpo                | Inter        | 400        | `1rem`                         | line-height 1.6   |
| Intro / hero párrafo  | Inter        | 300        | `1.125rem`                     |                   |
| Labels / overline     | Inter        | 500        | `0.875rem`                     | uppercase 0.08em  |
| Caption               | Inter        | 400        | `0.75rem`                      |                   |

---

## 5. Logo oficial — Variantes confirmadas

Los archivos están en `image/brand/logos/`. Variantes del manual:

| Archivo                                   | Variante                                            | Uso                                              |
| ----------------------------------------- | --------------------------------------------------- | ------------------------------------------------ |
| `logo-resmor-navy-on-light.png`           | Wordmark + alas — navy sobre claro                  | Navbar (scroll), papelería, flota                |
| `logo-resmor-gold-wordmark.png`           | Wordmark dorado + alas navy                          | Variante alternativa sobre claro                 |
| `monogram-navy-on-gold.png`               | Monograma R navy sobre fondo dorado                  | Avatar redes (premium)                           |
| `monogram-gold-on-navy.png`               | Monograma R dorado sobre fondo navy                  | Avatar redes (oficial recomendada), favicon      |
| `logo-variant-05.png`                     | (Variante adicional del manual)                     | A confirmar con cliente                          |
| `logo-variant-06.png`                     | (Variante adicional del manual)                     | A confirmar con cliente                          |

### Tagline oficial bajo el wordmark

> **SERVICIOS REMÍS & MINIFLETES**

Aparece bajo el wordmark en los archivos. La versión interna del manual lo extiende a:

> **MINIFLETES & TRANSPORTE EJECUTIVO**

**Decisión recomendada:**

- En el sitio web mantener **"Minifletes & Transporte Ejecutivo"** (alineado con el manual oficial pág. 15)
- En contextos cortos / redes sociales aceptar **"Servicios Remís & Minifletes"** (versión que está en los logos)

### Reglas de uso del logo

- **Espacio de respeto:** mínimo el alto de la "R" alrededor del logo en todos los lados.
- **No deformar.** Mantener proporciones originales.
- **No cambiar colores** fuera de las variantes oficiales.
- **No usar el logo sobre fondos de bajo contraste.**
  - Foto clara → variante navy
  - Foto oscura o fondo navy → variante dorada o blanca
- **No agregar efectos** (sombras, brillos, contornos, gradientes) que no estén en la variante oficial.

### Activos pendientes de generar (entregables para el dueño)

- [ ] Logo oficial en SVG (navy + blanco + dorado)
- [ ] Monograma en SVG
- [ ] Favicon (16x16, 32x32, 180x180, 192x192, 512x512)
- [ ] OG image (1200x630) — ya hay base en `image/brand/marketing/portada-facebook.jpg`

---

## 6. Tono de voz

Reescrito tras conocer la categoría oficial (**Transporte Ejecutivo**) y los atributos del manual.

### Principios

- **Confiable, no jactancioso** — "Llegamos a tiempo. Cuidamos lo que movemos." NO "Somos los mejores."
- **Elegante, no pomposo** — el lenguaje refleja el posicionamiento premium sin caer en frases corporativas vacías.
- **Cálido, no formal acartonado** — "amabilidad y simpatía" están en los atributos oficiales. No es un tono frío.
- **Moderno, no infantil** — "moderna, elegante, alegre" según el manual.
- **Directo** — frases cortas, verbos de acción.
- **Bilingüe donde aporta** — ES principal, PT en aeropuerto/turismo/transfer ejecutivo brasileño.

### Uso de pronombres

- **Vos** en CTAs y mensajes cortos (mercado porteño).
- **Usted** en cotizaciones empresariales y propuestas corporativas (B2B).
- **Tú** — no usar. No mezclar registros en la misma página.

### Ejemplos correctos

- "Transporte ejecutivo y minifletes en Buenos Aires."
- "Llegás a tiempo. Movemos lo que necesitás."
- "Tu mudanza, con handyman incluido."
- "Atendemos en español y portugués." / "Atendimento em português."

### Anti-ejemplos

- ❌ "Somos la mejor empresa de transportes del país"
- ❌ "Soluciones de movilidad integradas"
- ❌ "Transformamos tu experiencia de mudanza"
- ❌ "Líderes del mercado en logística porteña"

---

## 7. CTAs aprobados

Toda CTA del sitio debe ser una de estas (sin variaciones sin aprobación):

| CTA                                  | Destino                                                              | Cuándo usar                                |
| ------------------------------------ | -------------------------------------------------------------------- | ------------------------------------------ |
| **Cotizar por WhatsApp**             | `wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar`      | CTA principal global                       |
| **Reservar transporte ejecutivo**    | `wa.me/...?text=Necesito%20transporte%20ejecutivo`                   | Sección ejecutivo / aeropuerto             |
| **Pedí tu mudanza**                  | `wa.me/...?text=Quiero%20cotizar%20una%20mudanza`                   | Sección mudanzas                           |
| **Cotizar mi flete**                 | `wa.me/...?text=Necesito%20un%20mini-flete`                         | Sección minifletes                         |
| **Llamanos: (+54) 11 2304-8846**     | `tel:+5491123048846`                                                 | Header + contactanos                       |
| **Enviar mensaje**                   | Submit del formulario                                                | `contactanos.html`                         |
| **Ver servicios**                    | `servicios.html`                                                     | CTA secundario                             |
| **WhatsApp flotante** (ícono solo)   | `wa.me/5491123048846`                                                | Sticky en TODAS las páginas                |

### Reglas de implementación

- WhatsApp siempre con mensaje pre-cargado.
- WhatsApp siempre `target="_blank"` + `rel="noopener"`.
- `tel:` siempre con código país completo (`+54`).
- Botón principal: contraste alto, imperativo, verbo + complemento.
- WhatsApp flotante visible en TODAS las páginas, esquina inferior derecha.

---

## 8. Iconografía

- **Set:** Bootstrap Icons 1.5.0 (CDN, ya cargado).
- **Color sobre fondo claro:** `$color-brand-dorado` para acentos premium; `$color-brand-azul` para contacto/utility.
- **Color sobre fondo navy:** `$color-brand-dorado-light` o `$color-bg-soft`.
- **Tamaño consistente por sección.**

### Iconos por servicio

| Servicio              | Icono                   |
| --------------------- | ----------------------- |
| Transporte ejecutivo  | `bi-car-front-fill`     |
| Aeropuerto            | `bi-airplane`           |
| Minifletes            | `bi-box-seam`           |
| Mudanzas con handyman | `bi-truck`              |
| Logística PyMEs       | `bi-clipboard-check`    |
| Turismo / city tour   | `bi-geo-alt-fill`       |
| Pet-friendly          | `bi-heart-fill`         |
| WhatsApp              | `bi-whatsapp`           |
| Teléfono              | `bi-telephone-fill`     |
| Email                 | `bi-envelope`           |
| Dirección             | `bi-pin-map`            |

---

## 9. Bilingüe ES / PT

### Cuándo aplicar portugués

| Página / Sección                    | Aplicar PT |
| ----------------------------------- | ---------- |
| Hero del home                       | Sí (subtítulo corto) |
| Sección "transporte ejecutivo / aeropuerto" | Sí          |
| Sección "turismo / city tour"       | Sí          |
| Footer (info de contacto)           | Sí (frase corta) |
| Página `contactanos.html`           | Sí (línea de bienvenida) |
| Minifletes / mudanzas                | No (público local)         |

### Reglas

- No traducir todo el sitio — sólo donde el cliente brasileño aporta valor real.
- Frases PT cortas y claras.
- Marcar visualmente PT con color `$color-brand-dorado-light` (uppercase, letterspacing) o ícono de bandera.

### Frases sugeridas

| ES                                          | PT                                              |
| ------------------------------------------- | ----------------------------------------------- |
| "Atendemos en español y portugués."         | "Atendimento em português."                     |
| "Transporte ejecutivo"                      | "Transporte executivo"                          |
| "Traslado al aeropuerto"                    | "Transfer ao aeroporto"                         |
| "Llegás a tiempo, sin estrés."              | "Você chega na hora, sem estresse."             |

---

## 10. Componentes Bootstrap aprobados

| Componente        | Uso permitido                                | Customización SCSS                |
| ----------------- | -------------------------------------------- | --------------------------------- |
| `navbar`          | Menú principal — idéntico en todas las páginas | `_2barra-nav.scss`              |
| `carousel`        | Solo en hero del home                        | `_3hero.scss`                     |
| `card`            | Servicios y galería                          | `_4servicios.scss`                |
| `btn-primary`     | CTAs principales (override → azul)           | `_bootstrap-overrides.scss`       |
| `btn-whatsapp`    | CTAs WhatsApp (custom)                       | `_bootstrap-overrides.scss`       |
| `btn-gold`        | CTA premium puntual (ejecutivo)              | `_components.scss`                |
| `form-control`    | Inputs del formulario                         | `_8formulario.scss`               |
| `accordion`       | FAQs (futuro)                                | Por definir                       |
| `modal`           | Confirmación de envío del formulario         | Por definir                       |

**No usar sin aprobación:** `toast`, `offcanvas`, `tooltip`, `popover`.

---

## 11. Accesibilidad — Contrastes verificados

| Combinación                                    | Ratio          | WCAG AA texto normal (4.5:1) | WCAG AA texto grande (3:1) |
| ---------------------------------------------- | -------------- | ---------------------------- | -------------------------- |
| Azul `#0F1B49` sobre blanco                    | 14.5:1         | ✅                           | ✅                         |
| Blanco sobre azul `#0F1B49`                    | 14.5:1         | ✅                           | ✅                         |
| Dorado `#B0A56A` sobre azul `#0F1B49`          | 5.0:1          | ✅                           | ✅                         |
| Dorado `#B0A56A` sobre blanco                  | 2.6:1          | ❌                           | ⚠️ (solo iconos grandes)   |
| Azul `#0F1B49` sobre dorado `#B0A56A`          | 5.0:1          | ✅                           | ✅                         |
| WhatsApp `#25D366` sobre blanco                | 2.7:1          | ❌                           | ⚠️ (solo iconos grandes)   |
| Blanco sobre WhatsApp `#25D366`                | 2.7:1          | ⚠️                          | ✅ (solo bold ≥ 24px)      |

**Reglas:**

- **Dorado NO se usa para texto pequeño sobre blanco.** Solo para iconos grandes, líneas separadoras, fondos de botones (con texto azul encima) o sobre fondo azul.
- **Verde WhatsApp:** texto blanco bold sobre fondo verde. Para íconos grandes pasa, para texto chico no.
- Para CTAs WhatsApp, preferir **texto blanco bold + icon** sobre fondo verde para asegurar contraste.

---

## 12. Reglas de consistencia entre páginas

- **Navbar:** idéntico en `index`, `nosotros`, `servicios`, `tarifas`, `galeria`, `contactanos`. Si se modifica, actualizar en TODAS.
- **Header (banda superior con teléfono):** idéntico.
- **Footer:** idéntico.
- **WhatsApp flotante:** presente en TODAS las páginas, misma posición.
- **`<title>`:** distinto por página.
- **`<meta description>`:** distinto por página, 140-160 caracteres.

---

## 13. Datos del negocio confirmados

| Dato              | Valor                                              |
| ----------------- | -------------------------------------------------- |
| WhatsApp / tel    | `(+54) 9 11 2304-8846` — `wa.me/5491123048846`     |
| Dirección         | Viamonte 2450, Balvanera, CABA (de `mapa.jpg`) <!-- confirmar publicación --> |
| Flota visible     | Renault Kangoo blanca + Mercedes Vito ejecutiva   |
| Patente vista     | AC 017 TR                                          |
| Antigüedad marca  | Manual de 2018 — branding consolidado hace 8 años  |

---

## 14. Inventario de assets oficiales

Ubicados en `image/brand/`:

```text
image/brand/
├── PRESENTACION_RESMOR.pdf      # Manual oficial (24 pp)
├── logos/
│   ├── logo-resmor-navy-on-light.png       # Wordmark navy + alas dorado
│   ├── logo-resmor-gold-wordmark.png       # Wordmark dorado + alas navy
│   ├── monogram-navy-on-gold.png           # R navy sobre dorado
│   ├── monogram-gold-on-navy.png           # R dorado sobre navy (avatar recomendado)
│   ├── logo-variant-05.png                 # Variante adicional
│   └── logo-variant-06.png                 # Variante adicional
├── marketing/
│   ├── flyer-imprimir.jpg                  # Flyer oficial impreso
│   ├── portada-facebook.jpg                # Portada FB 851×315
│   └── tp-resmor-02.jpg                    # Tarjeta personal / pieza adicional
└── photos/
    ├── Fedd-Resmor-1.jpg → Fedd-Resmor-9.jpg     # Set oficial 1
    ├── Fedd-Resmor1.jpg → Fedd-Resmor4.jpg       # Set oficial 2
    ├── Resmor-Post-Grupos.jpg                    # Post redes
    └── Resmor-Stories-FB-IG.jpg                  # Story FB/IG
```

Ver detalles en [`image/brand/README.md`](../image/brand/README.md).

---

## 15. Decisiones pendientes (a validar)

- [ ] Compra/licencia de **Averta** o uso de **Inter** como sustituto definitivo
- [ ] Generación de logos en **SVG** (a partir de los PNG/PDF originales)
- [ ] Si Viamonte 2450 se publica en el sitio o queda reservada
- [ ] Año de fundación (para "Hace X años movemos Buenos Aires")
- [ ] Decisión final sobre el **tagline** principal del sitio: `Minifletes & Transporte Ejecutivo` (manual) vs `Servicios Remís & Minifletes` (en logo)
- [ ] Migrar `node-sass` → `sass` (Dart Sass) — el actual está deprecado
- [ ] Email oficial de contacto
- [ ] Horarios de atención
- [ ] Confirmar si las fotos `Fedd-Resmor-*` son del cliente o referenciales
