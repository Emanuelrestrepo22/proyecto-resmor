# Brand Implementation Notes — Resmor

**Agente:** AGT-02 UX / Frontend
**Versión:** v3 — alineada con manual oficial `PRESENTACION_RESMOR.pdf`
**Fecha:** 2026-05-17
**Fuente:** `BRAND_MARKETING_NOTES.md` (AGT-01) + `BRAND_RULES.md` (AGT-03) + extracción de hex desde el PDF.

> Tokens, SCSS y patrones listos para implementar. Compatibles con el stack actual (HTML5 + Bootstrap 5.1 + SCSS).

---

## 1. Tokens SCSS oficiales

Reemplazar el contenido de `scss/_variables.scss` por:

```scss
// ═══════════════════════════════════════════════════════════════
// RESMOR — DESIGN TOKENS
// Fuente: manual oficial PRESENTACION_RESMOR.pdf (2018)
// Pantone 2768 C (azul) + Pantone 4525 C (dorado)
// ═══════════════════════════════════════════════════════════════

// ───────────────────────────────────────────────
// COLOR — Marca oficial
// ───────────────────────────────────────────────
$color-brand-azul:           #0F1B49;   // Pantone 2768 C — confianza, simpatía, seguridad
$color-brand-azul-deep:      #0A1238;   // Hover/active sobre azul
$color-brand-azul-soft:      #1B2A66;   // Acento secundario sobre claro
$color-brand-dorado:         #B0A56A;   // Pantone 4525 C — glamour, éxito, fidelidad
$color-brand-dorado-light:   #D4CB9B;   // Hover, divisores, badges
$color-brand-dorado-dark:    #8C8350;   // Dorado oscuro (contraste sobre blanco)

// ───────────────────────────────────────────────
// COLOR — Neutros
// ───────────────────────────────────────────────
$color-bg-base:              #FFFFFF;
$color-bg-soft:              #F4F2EC;   // Fondo cálido (compañero del dorado)
$color-bg-cool:              #F3F3F3;   // Fondo neutro frío
$color-bg-overlay:           rgba(15, 27, 73, 0.12);   // Navy con alpha
$color-bg-photo-overlay:     rgba(15, 27, 73, 0.55);   // Overlay hero
$color-bg-photo-gradient:    linear-gradient(135deg, rgba(15, 27, 73, 0.55) 0%, rgba(10, 18, 56, 0.75) 100%);

$color-text-primary:         #0F1B49;   // = brand-azul
$color-text-secondary:       #4A5170;
$color-text-muted:           #8A8FA3;
$color-text-on-dark:         #F4F2EC;
$color-text-on-gold:         #0F1B49;   // Texto azul sobre fondo dorado

$color-border:               #E5E7ED;
$color-divider:              #D8DBE5;

// ───────────────────────────────────────────────
// COLOR — Funcionales
// ───────────────────────────────────────────────
$color-whatsapp:             #25D366;
$color-whatsapp-hover:       #1EBD5B;
$color-success:              #2EA44F;
$color-warning:              #D4A017;
$color-error:                #CF222E;

// ───────────────────────────────────────────────
// LEGACY (mantener compatibilidad con SCSS actual)
// ───────────────────────────────────────────────
$color-texto:                $color-brand-azul;
$bg-ubi:                     $color-bg-cool;
$bg-standard:                $color-bg-overlay;
$standard-size:              2em;
$standard-size-parrafo:      1.5em;

// ───────────────────────────────────────────────
// TIPOGRAFÍA — Inter como sustituto de Averta
// ───────────────────────────────────────────────
$font-display:               'Inter', 'Averta Demo', system-ui, -apple-system, 'Segoe UI', sans-serif;
$font-body:                  'Inter', 'Averta', system-ui, -apple-system, 'Segoe UI', sans-serif;

// Escala fluida (clamp)
$fs-display:                 clamp(2.5rem, 5vw, 4rem);
$fs-h1:                      clamp(2rem, 3.5vw, 2.75rem);
$fs-h2:                      clamp(1.5rem, 2.5vw, 2rem);
$fs-h3:                      clamp(1.25rem, 1.8vw, 1.5rem);
$fs-h4:                      1.125rem;
$fs-body:                    1rem;
$fs-body-lg:                 1.125rem;
$fs-small:                   0.875rem;
$fs-caption:                 0.75rem;

$lh-display:                 1.05;
$lh-heading:                 1.2;
$lh-body:                    1.6;

$ls-display:                 -0.02em;
$ls-heading:                 -0.01em;
$ls-overline:                0.12em;
$ls-uppercase:               0.08em;

// ───────────────────────────────────────────────
// ESPACIADO — Base 4/8
// ───────────────────────────────────────────────
$space-xxs:                  0.25rem;
$space-xs:                   0.5rem;
$space-sm:                   0.75rem;
$space-md:                   1rem;
$space-lg:                   1.5rem;
$space-xl:                   2rem;
$space-2xl:                  3rem;
$space-3xl:                  4rem;
$space-4xl:                  6rem;

$section-padding-y:          clamp(3rem, 6vw, 6rem);
$container-padding-x:        clamp(1rem, 3vw, 2rem);

// ───────────────────────────────────────────────
// RADIOS Y SOMBRAS
// ───────────────────────────────────────────────
$radius-sm:                  4px;
$radius-md:                  8px;
$radius-lg:                  16px;
$radius-pill:                999px;

$shadow-sm:                  0 2px 6px rgba(15, 27, 73, 0.06);
$shadow-md:                  0 8px 24px rgba(15, 27, 73, 0.08);
$shadow-lg:                  0 16px 40px rgba(15, 27, 73, 0.12);
$shadow-float:               0 4px 16px rgba(0, 0, 0, 0.2);

// ───────────────────────────────────────────────
// MIXINS (mantener el existente + sumar nuevos)
// ───────────────────────────────────────────────
@mixin standar-box($j-c, $flex-direction) {
  display: flex;
  justify-content: $j-c;
  flex-direction: $flex-direction;
  align-items: center;
  background-color: $bg-standard;
}

@mixin section-padding {
  padding-top: $section-padding-y;
  padding-bottom: $section-padding-y;
}

@mixin hero-overlay {
  position: relative;
  isolation: isolate;
  &::before {
    content: '';
    position: absolute;
    inset: 0;
    background: $color-bg-photo-gradient;
    z-index: -1;
  }
}
```

---

## 2. Override de Bootstrap

Crear `scss/_bootstrap-overrides.scss` y cargarlo **antes** de cualquier import de Bootstrap (si en algún momento se compila Bootstrap local). Si Bootstrap sigue cargándose por CDN, estas variables Sass actúan como referencia para reescribir clases custom:

```scss
@import 'variables';

// Bootstrap variables (si se compila local)
$primary:                    $color-brand-azul;
$secondary:                  $color-text-secondary;
$success:                    $color-whatsapp;
$danger:                     $color-error;
$warning:                    $color-warning;
$light:                      $color-bg-soft;
$dark:                       $color-brand-azul-deep;
$body-color:                 $color-text-primary;
$body-bg:                    $color-bg-base;
$link-color:                 $color-brand-azul;
$link-hover-color:           $color-brand-azul-deep;
$font-family-base:           $font-body;
$headings-font-family:       $font-display;
$headings-font-weight:       700;
$border-radius:              $radius-md;

// Si Bootstrap se carga por CDN, sobreescribir manualmente las clases:
.btn-primary {
  background-color: $color-brand-azul !important;
  border-color: $color-brand-azul !important;
  &:hover, &:focus {
    background-color: $color-brand-azul-deep !important;
    border-color: $color-brand-azul-deep !important;
  }
}

.bg-primary { background-color: $color-brand-azul !important; }
.text-primary { color: $color-brand-azul !important; }
.border-primary { border-color: $color-brand-azul !important; }
```

---

## 3. Componentes — Código listo para usar

### Hero con foto + overlay azul

```scss
// _3hero.scss
.hero {
  @include hero-overlay;
  background-size: cover;
  background-position: center;
  min-height: clamp(420px, 70vh, 640px);
  display: flex;
  align-items: center;
  color: $color-text-on-dark;
  padding: $space-4xl $container-padding-x;

  &__title {
    font-family: $font-display;
    font-weight: 800;
    font-style: italic;            // Averta Extrabold Italic equivalent
    font-size: $fs-display;
    line-height: $lh-display;
    letter-spacing: $ls-display;
    margin-bottom: $space-lg;
    max-width: 18ch;
  }

  &__subtitle {
    font-family: $font-body;
    font-weight: 300;
    font-size: $fs-body-lg;
    line-height: $lh-body;
    max-width: 56ch;
    margin-bottom: $space-2xl;
    color: $color-text-on-dark;
  }

  &__subtitle-pt {
    display: inline-block;
    margin-top: $space-sm;
    font-family: $font-body;
    font-size: $fs-small;
    text-transform: uppercase;
    letter-spacing: $ls-overline;
    color: $color-brand-dorado-light;
  }

  &__cta-group {
    display: flex;
    flex-wrap: wrap;
    gap: $space-md;
  }
}
```

### Botones

```scss
// _components-btn.scss

// CTA primario azul (Bootstrap btn-primary override)
.btn {
  font-family: $font-body;
  font-weight: 500;
  padding: $space-sm $space-xl;
  border-radius: $radius-sm;
  transition: all 0.2s ease;
  letter-spacing: $ls-uppercase;
  text-transform: uppercase;
  font-size: $fs-small;
}

.btn-primary-resmor {
  background: $color-brand-azul;
  color: $color-text-on-dark;
  border: 2px solid $color-brand-azul;
  &:hover {
    background: $color-brand-azul-deep;
    border-color: $color-brand-azul-deep;
    color: $color-text-on-dark;
  }
}

.btn-outline-resmor {
  background: transparent;
  color: $color-brand-azul;
  border: 2px solid $color-brand-azul;
  &:hover {
    background: $color-brand-azul;
    color: $color-text-on-dark;
  }
  // Variante sobre fondo oscuro (hero)
  &--on-dark {
    color: $color-text-on-dark;
    border-color: $color-text-on-dark;
    &:hover {
      background: $color-text-on-dark;
      color: $color-brand-azul;
    }
  }
}

// CTA WhatsApp
.btn-whatsapp {
  background: $color-whatsapp;
  color: $color-text-on-dark;
  border: 2px solid $color-whatsapp;
  display: inline-flex;
  align-items: center;
  gap: $space-xs;
  font-weight: 700;
  &:hover {
    background: $color-whatsapp-hover;
    border-color: $color-whatsapp-hover;
    color: $color-text-on-dark;
  }
  .bi-whatsapp { font-size: 1.25em; }
}

// CTA dorado premium (reservar transporte ejecutivo)
// Uso: máximo 1 por página. Texto azul oscuro para asegurar contraste.
.btn-gold-resmor {
  background: $color-brand-dorado;
  color: $color-brand-azul;
  border: 2px solid $color-brand-dorado;
  font-weight: 700;
  &:hover {
    background: $color-brand-dorado-dark;
    border-color: $color-brand-dorado-dark;
    color: $color-text-on-dark;
  }
}
```

### WhatsApp flotante

```scss
// _10whatsapp-float.scss
.whatsapp-float {
  position: fixed;
  bottom: $space-lg;
  right: $space-lg;
  z-index: 999;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: $color-whatsapp;
  color: $color-text-on-dark;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  text-decoration: none;
  box-shadow: $shadow-float;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;

  &:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.25);
    background: $color-whatsapp-hover;
    color: $color-text-on-dark;
  }

  @media (max-width: 768px) {
    bottom: $space-md;
    right: $space-md;
    width: 52px;
    height: 52px;
    font-size: 1.75rem;
  }
}
```

### Card de servicio

```scss
// _4servicios.scss
.servicio-card {
  background: $color-bg-base;
  border: 1px solid $color-border;
  border-radius: $radius-md;
  padding: $space-xl;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: $shadow-md;
    border-color: $color-brand-dorado;
  }

  &__icon {
    color: $color-brand-dorado;
    font-size: 2.5rem;
    margin-bottom: $space-md;
  }

  &__title {
    font-family: $font-display;
    font-weight: 700;
    font-size: $fs-h3;
    color: $color-brand-azul;
    margin-bottom: $space-sm;
  }

  &__desc {
    color: $color-text-secondary;
    font-size: $fs-body;
    line-height: $lh-body;
    flex: 1;
    margin-bottom: $space-md;
  }

  &__cta {
    display: inline-flex;
    align-items: center;
    gap: $space-xs;
    color: $color-brand-azul;
    text-decoration: none;
    font-weight: 500;
    font-size: $fs-small;
    text-transform: uppercase;
    letter-spacing: $ls-uppercase;

    &::after {
      content: '→';
      transition: transform 0.2s ease;
    }
    &:hover::after { transform: translateX(4px); }
  }
}
```

### Navbar

```scss
// _2barra-nav.scss
.navbar-resmor {
  background: $color-bg-base;
  border-bottom: 1px solid $color-border;
  padding-block: $space-md;
  transition: background 0.2s ease, box-shadow 0.2s ease;

  &.is-scrolled {
    box-shadow: $shadow-sm;
  }

  .navbar-brand img {
    height: 40px;
    width: auto;
  }

  .nav-link {
    color: $color-brand-azul;
    font-family: $font-body;
    font-weight: 500;
    font-size: $fs-small;
    text-transform: uppercase;
    letter-spacing: $ls-uppercase;
    padding-inline: $space-md;

    &:hover,
    &.active {
      color: $color-brand-dorado-dark;
    }
  }

  .navbar-cta {
    margin-left: $space-md;
  }
}
```

---

## 4. Estructura HTML — Hero del home

```html
<section class="hero" style="background-image: url('./image/brand/photos/Fedd-Resmor-3.jpg');">
  <div class="container">
    <h1 class="hero__title">Transporte ejecutivo &amp; minifletes en Buenos Aires.</h1>
    <p class="hero__subtitle">
      Llegás a tiempo. Movemos lo que necesitás.
      Atendemos por WhatsApp y respondemos rápido.
      <span class="hero__subtitle-pt">Atendimento em português</span>
    </p>
    <div class="hero__cta-group">
      <a href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar"
         target="_blank" rel="noopener"
         class="btn btn-whatsapp">
        <i class="bi bi-whatsapp"></i> Cotizar por WhatsApp
      </a>
      <a href="servicios.html" class="btn btn-outline-resmor btn-outline-resmor--on-dark">
        Ver servicios
      </a>
    </div>
  </div>
</section>
```

---

## 5. Logos — Mapeo a páginas y contextos

Los logos copiados están en `image/brand/logos/`. Mapeo recomendado:

| Contexto                                    | Archivo                              | Notas                                          |
| ------------------------------------------- | ------------------------------------ | ---------------------------------------------- |
| Navbar (fondo blanco)                       | `logo-resmor-navy-on-light.png`      | Crop alrededor del wordmark (2250×2250)       |
| Hero / sobre foto oscura                    | (generar variante blanca o usar negativa con CSS `filter: brightness(0) invert(1)`) |  |
| Footer (fondo azul)                          | `monogram-gold-on-navy.png` o variante blanca | Mantener proporción 1:1               |
| Favicon                                      | `monogram-gold-on-navy.png` 64×64 →  | Exportar también 16, 32, 180, 192, 512        |
| Avatar redes sociales                        | `monogram-gold-on-navy.png`           | Recomendada como avatar oficial               |
| OG image (1200×630)                          | Compose `logo-resmor-navy-on-light` + foto | A producir                                |

### Patrón de crop para el wordmark

El archivo `logo-resmor-navy-on-light.png` es 2250×2250 con whitespace. El wordmark "RESMOR" ocupa ~75% del ancho y ~12% del alto.

```html
<a href="index.html" class="navbar-brand" aria-label="Resmor — Inicio">
  <div class="logo-wordmark">
    <img src="./image/brand/logos/logo-resmor-navy-on-light.png"
         alt="Resmor — Transporte Ejecutivo"
         width="2250" height="2250">
  </div>
</a>
```

```scss
.logo-wordmark {
  position: relative;
  width: clamp(160px, 18vw, 240px);
  height: 48px;
  overflow: hidden;

  img {
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 100%;
    height: auto;
    display: block;
  }
}
```

> **Tarea pendiente:** generar SVG limpios o PNGs recortados al bounding box del wordmark para evitar esta gimnasia CSS.

---

## 6. Carga de webfonts

En `<head>` de cada página HTML (antes del CSS de Bootstrap):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300..800;1,400..800&display=swap" rel="stylesheet">
```

En `body` del CSS final:

```scss
body {
  font-family: $font-body;
  color: $color-text-primary;
  background: $color-bg-base;
  line-height: $lh-body;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, .hero__title {
  font-family: $font-display;
  font-weight: 700;
  line-height: $lh-heading;
  letter-spacing: $ls-heading;
  color: $color-brand-azul;
}
```

---

## 7. Optimización de imágenes

### Recomendaciones por tipo

| Tipo                  | Formato                  | Peso objetivo  | Atributos HTML                              |
| --------------------- | ------------------------ | -------------- | ------------------------------------------- |
| Hero del home         | WebP + JPG fallback      | <180 KB        | `loading="eager" fetchpriority="high"`     |
| Fotos de servicios    | WebP + JPG fallback      | <140 KB        | `loading="lazy"`                            |
| Galería               | WebP + JPG fallback      | <300 KB        | `loading="lazy"`                            |
| Logos PNG             | PNG transparente         | <50 KB         | `loading="eager"`                           |
| Logo SVG (a producir) | SVG                      | <10 KB         | inline o `<img>`                            |
| Favicon               | ICO + PNG                | <8 KB c/u      | `<link rel="icon">`                         |

### Patrón `<picture>` para hero

```html
<picture>
  <source srcset="./image/hero-home.webp" type="image/webp">
  <img src="./image/hero-home.jpg"
       alt="Resmor Transportes — Transporte ejecutivo en Buenos Aires"
       class="hero-bg"
       loading="eager"
       fetchpriority="high"
       width="1920" height="1080">
</picture>
```

---

## 8. Iconografía — Bootstrap Icons

Set ya cargado por CDN. Mapeo de servicios:

| Servicio              | Clase Bootstrap         | Color                       |
| --------------------- | ----------------------- | --------------------------- |
| Transporte ejecutivo  | `bi-car-front-fill`     | `$color-brand-dorado`       |
| Aeropuerto            | `bi-airplane`           | `$color-brand-dorado`       |
| Minifletes            | `bi-box-seam`           | `$color-brand-dorado`       |
| Mudanzas              | `bi-truck`              | `$color-brand-dorado`       |
| Logística PyMEs       | `bi-clipboard-check`    | `$color-brand-dorado`       |
| Turismo               | `bi-geo-alt-fill`       | `$color-brand-dorado`       |
| Pet-friendly          | `bi-heart-fill`         | `$color-brand-dorado`       |
| WhatsApp              | `bi-whatsapp`           | `$color-whatsapp` o blanco  |
| Teléfono              | `bi-telephone-fill`     | `$color-brand-azul`         |
| Email                 | `bi-envelope`           | `$color-brand-azul`         |
| Dirección             | `bi-pin-map`            | `$color-brand-azul`         |

---

## 9. Estructura SCSS final recomendada

```text
scss/
├── _variables.scss              # tokens oficiales (ver sección 1)
├── _mixins.scss                 # standar-box, section-padding, hero-overlay
├── _base.scss                   # reset suave + body
├── _typography.scss             # H1-H6, .display, .label
├── _utilities.scss              # text-azul, bg-cream, divider-gold, etc.
├── _bootstrap-overrides.scss    # overrides de btn, navbar, bg-primary
├── _1encabezado.scss            # header con teléfono
├── _2barra-nav.scss             # navbar
├── _3hero.scss                  # hero con foto + overlay (nuevo)
├── _4servicios.scss             # cards de servicios (nuevo)
├── _5galeria.scss               # galería (nuevo)
├── _6acerca-nosotros.scss
├── _7ubi-information.scss
├── _8formulario.scss
├── _9footer.scss                # footer (nuevo)
├── _10whatsapp-float.scss       # WhatsApp flotante (nuevo)
├── _responsive.scss             # media queries
└── estilo.scss                  # entry: imports
```

Orden de imports en `estilo.scss`:

```scss
@import 'variables';
@import 'mixins';
@import 'base';
@import 'typography';
@import 'utilities';
@import 'bootstrap-overrides';

@import '1encabezado';
@import '2barra-nav';
@import '3hero';
@import '4servicios';
@import '5galeria';
@import '6acerca-nosotros';
@import '7ubi-information';
@import '8formulario';
@import '9footer';
@import '10whatsapp-float';

@import 'responsive';
```

---

## 10. Accesibilidad — Reglas implementables

- `alt` descriptivo en TODAS las imágenes.
- Contraste mínimo AA verificado (tabla en `BRAND_RULES.md` sección 11).
- **Dorado no se usa para texto pequeño sobre blanco** — solo iconos grandes, líneas, fondos de botón.
- **WhatsApp verde** + texto blanco bold ≥14px para asegurar contraste.
- Foco visible en todos los elementos interactivos:

```scss
:focus-visible {
  outline: 2px solid $color-brand-dorado;
  outline-offset: 2px;
}
```

- `aria-label` en botones icon-only (WhatsApp flotante, hamburger).
- Estructura H1 → H2 → H3 sin saltos.
- `<button>` para acciones, `<a>` para navegación.

---

## 11. Migración recomendada del proyecto

Estado actual del repo:

```text
scss/_variables.scss      # variables mínimas (4 colores)
node-sass                  # DEPRECADO desde 2020
```

**Plan de migración (orden):**

1. Sustituir `scss/_variables.scss` con los tokens de la sección 1 (manteniendo aliases legacy).
2. Migrar `node-sass` → `sass` (Dart Sass) en `package.json`:
   ```json
   "scripts": {
     "build-css": "sass scss/estilo.scss css/estilo.css --no-source-map",
     "watch-css": "sass --watch scss/estilo.scss css/estilo.css"
   },
   "devDependencies": {
     "sass": "^1.77.0"
   }
   ```
3. Cargar Inter desde Google Fonts en `<head>` de cada HTML.
4. Crear los nuevos parciales SCSS (3hero, 4servicios, 9footer, 10whatsapp-float).
5. Actualizar `index.html` con la nueva estructura del hero.
6. Replicar navbar + footer idénticos en todas las páginas.
7. Auditoría QA (AGT-04) antes del deploy.

---

## 12. Handoff a otros agentes

| Acción                                                          | Delegar a              |
| --------------------------------------------------------------- | ---------------------- |
| Documentar este SCSS final en `docs/architecture/`              | AGT-03 Documentation   |
| Auditar implementación contra estos tokens                      | AGT-04 Functional QA   |
| Validar copy nuevo en cada bloque renderizado                   | AGT-01 Marketing       |
