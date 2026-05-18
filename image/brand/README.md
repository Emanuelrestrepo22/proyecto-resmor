# `image/brand/` — Assets oficiales de marca Resmor

> **Fuente:** Manual de marca oficial **PRESENTACION_RESMOR.pdf** (24 páginas, 2018) + paquete de imagenes oficial de Resmor.
> **Última sincronización:** 2026-05-17
> **Mirror público:** `public/brand/` + favicons en `public/`

---

## Estructura

```text
image/brand/
├── PRESENTACION_RESMOR.pdf      # Manual de marca oficial (24 pp)
├── README.md                     # Este archivo
├── logos/                        # Logos oficiales en variantes
├── marketing/                    # Piezas de marketing oficiales (flyer, portada, TP)
└── photos/                       # Set de fotos branded oficiales
```

---

## Logos oficiales (`logos/`)

Archivos PNG transparentes 2250×2250 (alta resolución, listos para imprimir o adaptar).

| Archivo                              | Descripción                                            | Uso recomendado                              |
| ------------------------------------ | ------------------------------------------------------ | -------------------------------------------- |
| `logo-resmor-navy-on-light.png`      | Wordmark navy + alas dorado, sub "Servicios Remís & Minifletes" | Navbar (scroll), papelería, flota          |
| `logo-resmor-gold-wordmark.png`      | Wordmark dorado + alas navy                            | Variante alternativa                         |
| `monogram-navy-on-gold.png`          | Monograma R navy sobre fondo dorado                    | Avatar redes (premium)                       |
| `monogram-gold-on-navy.png`          | Monograma R dorado sobre fondo navy                    | **Avatar oficial / favicon**                 |
| `logo-variant-05.png`                | Variante adicional del manual                          | A confirmar con cliente                      |
| `logo-variant-06.png`                | Variante adicional del manual                          | A confirmar con cliente                      |

### Pendientes (entregables para el dueño)

- [ ] Versión SVG de cada logo
- [ ] Versión PNG **blanca pura** (solo alpha) para overlays sobre fotos oscuras
- [x] Favicons exportados en sizes 16, 32, 48, 64, 96, 180, 192, 512 + `.ico` (a partir del monograma)
- [ ] OG image 1200×630

---

## Marketing (`marketing/`)

Piezas oficiales de marketing producidas en 2018 (Adobe Photoshop CC 2019).

| Archivo                  | Tamaño        | Uso original              | Reutilizable como                              |
| ------------------------ | ------------- | ------------------------- | ---------------------------------------------- |
| `flyer-imprimir.jpg`     | 1122×1594     | Flyer impresión           | Referencia de paleta + composición             |
| `portada-facebook.jpg`   | 851×315       | Cover de Facebook         | Hero banner o referencia para OG image         |
| `tp-resmor-02.jpg`       | 1004×651      | Tarjeta personal / pieza  | Referencia de jerarquía visual                 |

---

## Fotos (`photos/`)

Set oficial de fotos con logo aplicado y tratamiento cinematográfico (overlay azul + logo wings blanco al pie).

### Set 1 — `Fedd-Resmor-1.jpg` a `Fedd-Resmor-9.jpg`
Fotos individuales con logo wings aplicado. Estilo cinematográfico, contraste alto.

### Set 2 — `Fedd-Resmor1.jpg` a `Fedd-Resmor4.jpg`
Set alternativo (numeración sin guion).

### Posts y stories
| Archivo                       | Uso original                |
| ----------------------------- | --------------------------- |
| `Resmor-Post-Grupos.jpg`      | Post Facebook Grupos        |
| `Resmor-Stories-FB-IG.jpg`    | Story Facebook + Instagram  |

### Mapeo sugerido para el sitio web

| Página / sección                    | Foto recomendada                              |
| ----------------------------------- | --------------------------------------------- |
| Home hero                            | `Fedd-Resmor-3.jpg` o `Fedd-Resmor1.jpg`     |
| Sección "Transporte ejecutivo"      | `Fedd-Resmor-1.jpg` (ejecutivo con periódico) |
| Sección "Aeropuerto"                | `Fedd-Resmor-4.jpg` o foto con maletas        |
| Sección "Minifletes"                | `Fedd-Resmor-6.jpg` (van + handyman)          |
| Sección "Nosotros / equipo"         | `Fedd-Resmor-5.jpg` (handyman polo blanco)    |
| Galería                             | Mezcla de todas + photo1-6 del set anterior   |

> **Nota legal:** confirmar con el cliente si las fotos son de su propiedad o si fueron tomadas de catálogos. En caso de duda, usar las **fotos reales del cliente** (`branding-resmor/photos/photo1-6`) como prioridad.

---

## Paleta oficial (resumen)

| Color                  | Pantone     | Hex (sRGB)  | Atributos verbales (manual)                    |
| ---------------------- | ----------- | ----------- | ---------------------------------------------- |
| Azul corporativo       | 2768 C      | `#0F1B49`   | Amabilidad, simpatía, seguridad, confianza    |
| Dorado corporativo     | 4525 C      | `#B0A56A`   | Glamour, éxito, fidelidad, riqueza, belleza   |

---

## Tipografía oficial (resumen)

**AVERTA** — moderna, elegante, alegre.

- AVERTA DEMO REGULAR — cuerpo
- AVERTA DEMO EXTRABOLD ITALIC — títulos / hero

**Sustituto web (sin licencia):** Inter (Google Fonts).

---

## Tagline oficial

> **MINIFLETES & TRANSPORTE EJECUTIVO**

Variante corta (en logos): "Servicios Remís & Minifletes"
Categoría corporativa: **TRANSPORTE EJECUTIVO**

---

## Mirror en `public/`

Se mantiene copia lista para deploy estático en `public/brand/`.

```text
public/
├── brand/
│   ├── logos/
│   ├── marketing/
│   ├── photos/
│   ├── PRESENTACION_RESMOR.pdf
│   └── README.md
├── favicon.ico
├── favicon-16.png
├── favicon-32.png
├── favicon-180.png
├── favicon-192.png
└── favicon-512.png
```

## Cómo citar estos assets en el código

```html
<!-- Navbar -->
<img src="./image/brand/logos/logo-resmor-navy-on-light.png" alt="Resmor — Transporte Ejecutivo">

<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="./image/favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="./image/favicon-180.png">

<!-- Hero del home -->
<section class="hero" style="background-image: url('./image/brand/photos/Fedd-Resmor-3.jpg');">
```

---

## Cambios pendientes

- [ ] Solicitar al cliente la versión SVG editable de los logos
- [ ] Confirmar derechos de uso de las fotos `Fedd-Resmor-*`
- [ ] Producir versión blanca pura del wordmark para hero sobre fotos oscuras
- [ ] Producir set de favicons
