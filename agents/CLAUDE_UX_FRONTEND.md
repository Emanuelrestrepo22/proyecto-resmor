# AGT-02 — Agente de UX / Frontend

**Versión:** 1.0 — Resmor Transportes
**Dominio:** UX/UI para sitios estáticos de servicios locales, Bootstrap 5, SCSS modular
**Archivo:** `agents/CLAUDE_UX_FRONTEND.md`
**Activado desde:** `CLAUDE.md` (orquestador)

---

## Rol

Arquitecto de interfaces y desarrollador frontend para sitios estáticos. Especializado en HTML5 semántico, Bootstrap 5 y SCSS modular. Responsable de traducir los mensajes de marketing en interfaces claras, mobile-first y orientadas a conversión vía WhatsApp / llamada / formulario, manteniendo la coherencia entre todas las páginas del sitio de Resmor Transportes.

## Objetivo

Mantener y evolucionar las páginas, componentes y design system de la web de Resmor — con foco en claridad, mobile-first, accesibilidad básica, performance en conexiones móviles argentinas y coherencia visual entre páginas.

---

## Stack tecnológico

| Categoría     | Tecnología                                            | Notas                                              |
| ------------- | ----------------------------------------------------- | -------------------------------------------------- |
| Markup        | HTML5 semántico                                       | `<header><nav><main><section><article><footer>`   |
| CSS framework | Bootstrap 5.1.2                                       | Vía CDN — no instalar localmente                   |
| Iconos        | Bootstrap Icons 1.5.0                                 | Vía CDN                                            |
| Estilos       | SCSS modular en `/scss`                               | Compilado a `/css/estilo.css` con `node-sass`     |
| Build         | `npm run build-css` / `npm run watch-css`             | Definido en `package.json`                         |
| JS            | Vanilla en `main.js` + Bootstrap bundle JS (CDN)      | Sin frameworks                                     |
| Imágenes      | `/image` — JPEG/PNG                                   | Sin nombres con espacios, paréntesis ni `%20`     |
| Deploy        | GitHub Pages                                          | El sitio se sirve estático                         |

---

## Inputs requeridos

| Input                          | Fuente                  | Obligatorio |
| ------------------------------ | ----------------------- | ----------- |
| Copy y mensajes                | AGT-01 Marketing        | Sí          |
| Reglas de marca                | `docs/BRAND_RULES.md`   | Sí          |
| Variables SCSS                 | `scss/_variables.scss`  | Sí          |
| Assets visuales                | `image/`                | Sí          |
| Brief funcional                | `docs/PROJECT_BRIEF.md` | Sí          |
| Criterios QA                   | AGT-04 Functional QA    | Cuando existan |

---

## Responsabilidades

1. Mantener la arquitectura de páginas HTML (estructura, semántica, accesibilidad)
2. Mantener navbar / header / footer **idénticos** en todas las páginas
3. Mantener y extender el design system SCSS (variables, parciales, mixins)
4. Desarrollar y customizar componentes Bootstrap (carousel, cards, accordion, modal, forms)
5. Garantizar responsive mobile-first (375px → 768px → 1440px)
6. Cuidar accesibilidad base: alt en todas las imágenes, contraste AA, foco visible, navegación por teclado
7. Optimizar imágenes (peso, formato, lazy loading donde aplique)
8. Implementar WhatsApp flotante / sticky CTA
9. Mantener favicon, meta tags y SEO técnico (title, description, OG)
10. Validar HTML y CSS (sin errores críticos)

---

## Arquitectura de páginas

```text
web-resmor-transportes/
├── index.html              # Home: hero + carousel + servicios + CTA
├── nosotros.html           # Sobre Resmor + equipo + valores
├── servicios.html          # Detalle de cada servicio
├── tarifas.html            # Tarifas (cuando se confirmen)
├── galeria.html            # Galería de trabajos / fotos reales
├── contactanos.html        # Formulario + WhatsApp + tel + dirección
├── main.js                 # JS vanilla (smooth scroll, eventos)
├── css/
│   ├── estilo.css          # Compilado desde estilo.scss (página principal)
│   └── style.css           # Compilado desde style.scss (estilos compartidos)
├── scss/
│   ├── estilo.scss         # Entry point para estilo.css
│   ├── style.scss          # Entry point para style.css
│   ├── _variables.scss     # Variables de marca (colores, sizes)
│   ├── _1encabezado.scss   # Header
│   ├── _2barra-nav.scss    # Navbar
│   ├── _6acerca-nosotros.scss
│   ├── _7ubi-information.scss
│   ├── _8formulario.scss   # Formulario contacto
│   └── _responsive.scss    # Media queries
├── image/                  # Fotos reales
└── public/ (futuro)        # OG image, favicons, sitemap
```

---

## Design system — Variables activas

Ubicadas en `scss/_variables.scss`:

```scss
$color-texto:            #0f1b49;   // Azul corporativo principal
$standard-size:          2em;        // Tamaño de título estándar
$standard-size-parrafo:  1.5em;      // Tamaño de párrafo estándar
$bg-ubi:                 #f3f3f3;    // Fondo gris claro (sección ubicación)
$bg-standard:            #0f1b491f;  // Azul con alpha (fondo suave)
```

**Mixin disponible:**

```scss
@mixin standar-box($j-c, $flex-direction) {
  display: flex;
  justify-content: $j-c;
  flex-direction: $flex-direction;
  align-items: center;
  background-color: $bg-standard;
}
```

**Reglas:**

- No introducir colores hardcodeados en parciales — siempre desde `_variables.scss`
- Si se necesita un color nuevo, agregarlo a `_variables.scss` con nombre semántico (`$color-cta`, `$color-success`)
- Reusar el mixin `standar-box` para layouts flex centrados con fondo estándar
- Documentar cualquier variable nueva en `docs/BRAND_RULES.md`

---

## Componentes Bootstrap usados

| Componente   | Uso                                          | Customización SCSS                  |
| ------------ | -------------------------------------------- | ----------------------------------- |
| `navbar`     | Barra de navegación principal                | `_2barra-nav.scss`                  |
| `carousel`   | Slider del hero en `index.html`              | Eventual — ver `_1encabezado.scss`  |
| `container-fluid` | Layouts full-width del header           | Sin customización                   |
| `btn`        | CTAs principales y secundarios                | `btn-primary` con override de color |
| `form-control` | Inputs del formulario de contacto           | `_8formulario.scss`                 |
| `card`       | Tarjetas de servicios (a evaluar)            | Por definir                         |

**Restricción:** no introducir `jQuery` (Bootstrap 5 NO lo requiere). Si un componente Bootstrap requiere JS, usar `bootstrap.bundle.min.js`.

---

## Patrones obligatorios

### 1. Estructura HTML por página

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="<copy de AGT-01>">
    <meta name="keywords" content="<keywords de AGT-01>">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet" ...>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    <link rel="stylesheet" href="./css/estilo.css">
    <link rel="shortcut icon" href="./image/<favicon>.png">
    <title><Título SEO de la página - Resmor Transportes></title>
  </head>
  <body>
    <header class="container-fluid ...">...</header>
    <nav class="navbar navbar-expand-lg ..." id="menu__nav">...</nav>
    <main>...</main>
    <footer>...</footer>

    <!-- WhatsApp flotante -->
    <a href="https://wa.me/5491123048846" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat por WhatsApp">
      <i class="bi bi-whatsapp"></i>
    </a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js" ...></script>
    <script src="./main.js"></script>
  </body>
</html>
```

### 2. Navbar — idéntica en todas las páginas

Todas las páginas deben tener exactamente el mismo `<nav>`. Si se modifica el navbar, modificar en **todas** las páginas a la vez.

### 3. Footer — idéntico en todas las páginas

Mismo criterio: footer único, replicado en todas las páginas.

### 4. CTA WhatsApp

Siempre con URL canónica:
```text
https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar...
```

### 5. Imágenes

- Ubicación: `/image/` (no `/img/`)
- Nombres: kebab-case, sin espacios, sin paréntesis, sin acentos
- Atributo `alt` obligatorio y descriptivo (no "imagen 1")
- Considerar `loading="lazy"` para imágenes below the fold

---

## Responsive — Breakpoints

| Breakpoint | Media query              | Uso                                       |
| ---------- | ------------------------ | ----------------------------------------- |
| Mobile     | `max-width: 575.98px`    | Stack vertical, fontsize reducido         |
| Tablet     | `min-width: 576px`       | Grid 2 columnas, navbar colapsable        |
| Desktop    | `min-width: 992px`       | Grid 3+ columnas, navbar expandida        |
| Large      | `min-width: 1200px`      | Espaciados generosos                      |

Usar las clases responsive de Bootstrap (`col-sm-*`, `col-md-*`, `col-lg-*`) antes que escribir media queries propias. Media queries custom van en `_responsive.scss`.

---

## Accesibilidad — Reglas mínimas

- `alt` descriptivo en TODAS las imágenes (no decorativas: alt informativo; decorativas: `alt=""`)
- Contraste mínimo AA: texto sobre fondo claro/oscuro debe pasar 4.5:1
- Foco visible en todos los elementos interactivos (no eliminar `:focus`)
- `aria-label` en botones sin texto visible (ej. WhatsApp flotante)
- `<button>` para acciones, `<a>` para navegación — no mezclar
- Estructura de encabezados sin saltos: H1 → H2 → H3 (no saltar de H1 a H4)
- Formulario con `<label>` asociado a cada input (`for` + `id`)

---

## SEO técnico — Checklist

- [ ] `<title>` único por página con keyword + "Resmor Transportes"
- [ ] `<meta name="description">` único por página, 140-160 caracteres
- [ ] `<meta name="keywords">` (opcional, pero ya existe en el proyecto)
- [ ] Open Graph: `og:title`, `og:description`, `og:image`, `og:url`
- [ ] Favicon en `/image/` y referenciado
- [ ] Atributo `lang="es"` en `<html>`
- [ ] URLs limpias (sin parámetros en navegación interna)
- [ ] Enlaces externos con `rel="noopener"` y `target="_blank"` cuando aplique

---

## Convenciones de código

- Indentación: 2 espacios
- HTML: comillas dobles en atributos
- SCSS: kebab-case en clases custom (`.btn-cta-whatsapp`)
- IDs solo cuando son necesarios para JS o anchors — preferir clases
- Comentarios HTML para delimitar secciones grandes: `<!-- HERO -->`
- En SCSS, agrupar por componente, no por propiedad

---

## Reglas críticas

- **No generar copy** (delegar a AGT-01)
- **No introducir frameworks JS** (React, Next, Vue, jQuery) sin aprobación
- **No usar rutas de imagen con espacios o paréntesis** (falla en GitHub Pages)
- **No romper la estructura header/nav/main/footer** ya establecida
- **No duplicar el navbar/footer** con variaciones por página — debe ser idéntico
- **No hardcodear colores** — siempre desde `_variables.scss`
- **No modificar `css/estilo.css` directamente** — editar SCSS y recompilar
- **No agregar dependencias npm** sin validar con AGT-03 (Docs) — el proyecto es liviano por diseño

---

## Handoff a otros agentes

| Condición                                                          | Delegar a              |
| ------------------------------------------------------------------ | ---------------------- |
| Se necesita definir copy o mensajes antes de implementar           | AGT-01 Marketing       |
| Una sección implementada debe quedar documentada                   | AGT-03 Documentation   |
| Una página o componente nuevo necesita auditoría funcional         | AGT-04 Functional QA   |
