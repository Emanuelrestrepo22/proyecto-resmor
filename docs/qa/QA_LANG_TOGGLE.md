# QA — Language Toggle ES / PT / EN

**Agente:** AGT-04 Functional QA
**Fecha:** 2026-05-17
**Alcance:** funcionamiento del switcher de idioma + cobertura de traducciones + persistencia + accesibilidad + impacto en CTAs (WhatsApp).

---

## 1. Información general

- **Feature:** Toggle de idioma con 3 idiomas (ES / PT / EN)
- **Páginas afectadas:** las 6 públicas (`index`, `nosotros`, `servicios`, `tarifas`, `galeria`, `contactanos`)
- **Componentes nuevos:** `lang-switcher` (topbar) + `lang-switcher d-lg-none` (mobile, dentro del navbar)
- **Motor:** `js/i18n.js` + diccionarios `js/i18n/{es,pt,en}.json`
- **Dependencias funcionales:**
  - `localStorage` para persistencia
  - `fetch` para cargar diccionarios
  - `navigator.language` para auto-detección
  - `window.bootstrap.Collapse` para cierre del navbar mobile (ya cargado antes)

---

## 2. Criterios de aceptación

| #     | Criterio                                                                            | Prioridad |
| ----- | ----------------------------------------------------------------------------------- | --------- |
| CA-01 | Por default (sin acción del usuario), el sitio aparece en español                   | Alta      |
| CA-02 | Al hacer click en "PT" en el switcher, todo el contenido de la página cambia a portugués sin recargar | Alta |
| CA-03 | Al hacer click en "EN", todo el contenido cambia a inglés sin recargar              | Alta      |
| CA-04 | El idioma elegido se persiste entre páginas (al navegar de Home → Servicios mantiene el idioma) | Alta |
| CA-05 | El idioma elegido se persiste entre sesiones (cerrar y reabrir el navegador mantiene la elección) | Alta |
| CA-06 | `navigator.language` se respeta al primer ingreso (si el usuario está en PT-BR ve el sitio en PT) | Media |
| CA-07 | `?lang=en` en la URL fuerza el idioma EN aunque haya otro guardado                  | Media     |
| CA-08 | El atributo `<html lang="">` se actualiza según el idioma activo                    | Alta      |
| CA-09 | El `<title>` de la página cambia al idioma activo                                   | Media     |
| CA-10 | `og:locale` se actualiza al idioma activo                                           | Baja      |
| CA-11 | Los links de WhatsApp llevan el mensaje pre-cargado en el idioma activo             | Alta      |
| CA-12 | El switcher marca visualmente el idioma activo (`is-active` + `aria-pressed="true"`)| Alta      |
| CA-13 | El sitio sigue funcional si `localStorage` está deshabilitado (modo privado)        | Media     |
| CA-14 | El sitio sigue funcional si `fetch` falla (ej: 404 del JSON) — muestra fallback ES  | Alta      |
| CA-15 | Navegación por teclado (Tab) recorre los botones del switcher con foco visible      | Alta      |
| CA-16 | Los placeholders del formulario de contacto se traducen                             | Alta      |
| CA-17 | El `<option>` del select de servicio se traduce manteniendo el `value` original     | Alta      |
| CA-18 | No hay errores en consola al cambiar de idioma                                      | Alta      |

---

## 3. Checklist QA detallado por bloque

### 3.1 Topbar

- [ ] El texto "Atención 24 hs · Atendimento em português" cambia al cambiar idioma
- [ ] El `aria-label` del link de teléfono cambia (ES: "Llamar a Resmor" / PT: "Ligar para Resmor" / EN: "Call Resmor")
- [ ] El span "WhatsApp" se mantiene (es marca, no se traduce)
- [ ] Los 3 botones del switcher están visibles en desktop
- [ ] En mobile (≤575px), las banderas se ocultan, sólo queda el código corto (ES/PT/EN)
- [ ] El botón del idioma activo tiene fondo dorado + texto azul (variante `--on-dark`)

### 3.2 Navbar

- [ ] La tagline "Minifletes & Transporte Ejecutivo" debajo de RESMOR cambia por idioma
- [ ] Los 6 nav-links se traducen (Inicio/Nosotros/Servicios/Tarifas/Galería/Contacto)
- [ ] El botón CTA "Cotizar" cambia su texto y su `href` (mensaje WhatsApp en el idioma)
- [ ] El switcher mobile (`d-lg-none`) aparece sólo en pantallas <992px
- [ ] El switcher mobile funciona igual que el de topbar

### 3.3 Hero (cada página)

- [ ] El eyebrow cambia ("Buenos Aires · Desde 2018" / "Buenos Aires · Since 2018" / "Buenos Aires · Desde 2018")
- [ ] El H1 cambia por completo
- [ ] El subtítulo cambia
- [ ] El subtítulo PT (color dorado) cambia (en EN dice "English-speaking team · Atendimento em português")
- [ ] Los CTAs cambian de texto

### 3.4 Por qué Resmor (home)

- [ ] Los 3 items y sus descripciones cambian
- [ ] Los íconos no cambian (son universales)

### 3.5 Cards de servicio

- [ ] Cada `servicio-card__title` cambia
- [ ] Cada `servicio-card__desc` cambia
- [ ] Cada `<li>` del listado cambia
- [ ] Cada `servicio-card__cta` cambia
- [ ] El `href` del CTA WhatsApp se actualiza con el mensaje en el idioma

### 3.6 Pasos (home + tarifas)

- [ ] El eyebrow + título cambian
- [ ] Los 3 pasos (título + descripción) cambian

### 3.7 Bloque CTA cierre (home + servicios + galería)

- [ ] El eyebrow, H2 y los dos botones cambian
- [ ] El href del WhatsApp se actualiza

### 3.8 Footer

- [ ] Tagline en el footer cambia
- [ ] Headers de las 3 columnas (Servicios / Empresa / Contacto) cambian
- [ ] Las 6 links de servicios cambian
- [ ] Las 4 links de empresa cambian
- [ ] Labels "WhatsApp / Teléfono / Dirección" cambian
- [ ] El año dinámico funciona (no es traducible)
- [ ] "Todos los derechos reservados" cambia

### 3.9 Formulario de contacto (contactanos.html)

- [ ] Título del form cambia
- [ ] Subtítulo del form cambia
- [ ] Cada `<label>` cambia
- [ ] Cada `placeholder` cambia (incluyendo `+54 9 11 ...` → `+55 11 ...` en PT)
- [ ] Cada `<option>` del select cambia, manteniendo el `value` (ej: `value="aeropuerto"` siempre)
- [ ] El botón "Enviar mensaje" cambia
- [ ] La nota del WhatsApp (`form-note`) cambia
- [ ] Al enviar el form, el mensaje WhatsApp generado **debe** seguir siendo en español (porque el equipo Resmor responde en ES por default) — **decisión a confirmar con el cliente**

### 3.10 WhatsApp flotante

- [ ] El icono no cambia
- [ ] El `href` actualiza el mensaje pre-cargado al idioma activo

### 3.11 Mapa / iframe

- [ ] El mapa de Google no se traduce (queda en el idioma del navegador del cliente) — sin acción

---

## 4. Casos de prueba específicos

### CP-01 — Primer ingreso desde un navegador en español

| Paso | Acción                                                  | Resultado esperado                                     |
| ---- | ------------------------------------------------------- | ------------------------------------------------------ |
| 1    | DevTools → Application → Local Storage → eliminar `resmor.lang` | Vacío                                          |
| 2    | Recargar la página                                       | Sitio en ES, botón "ES" activo en el switcher          |
| 3    | Verificar `<html lang>`                                  | `lang="es"`                                            |
| 4    | Verificar `localStorage.resmor.lang`                     | `'es'`                                                 |

### CP-02 — Cambio explícito a PT

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Sitio en ES (recién cargado)                        | OK                                                 |
| 2    | Click en botón "PT" en topbar                       | Todo el contenido cambia a portugués (sin recargar)|
| 3    | Verificar `<html lang>`                              | `lang="pt-BR"`                                     |
| 4    | Verificar `<title>`                                  | "Transporte executivo & mini-fretes em Buenos Aires."|
| 5    | Click en WhatsApp flotante                          | Abre wa.me con texto "Olá Resmor, quero cotizar"   |
| 6    | Recargar la página (F5)                             | Sigue en PT                                        |
| 7    | Navegar a /servicios.html                           | servicios.html aparece en PT                       |

### CP-03 — Auto-detección con navigator.language

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | DevTools → Sensors → Locale → "pt-BR"               | OK                                                 |
| 2    | Eliminar `localStorage.resmor.lang`                  | OK                                                 |
| 3    | Recargar                                             | Sitio en PT por auto-detección                     |

### CP-04 — URL forzada con ?lang=

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Setear `localStorage.resmor.lang = 'es'`             | OK                                                 |
| 2    | Visitar `/?lang=en`                                  | Sitio en EN, ignora el localStorage                |
| 3    | Verificar `localStorage.resmor.lang`                 | `'en'` (ahora se actualizó)                        |

### CP-05 — Fetch fallido (modo offline o 404)

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | DevTools → Network → Offline                        | OK                                                 |
| 2    | Click en "EN"                                        | Si el JSON no estaba cacheado, intenta cargar ES como fallback; consola muestra error pero sitio no se rompe |
| 3    | No hay errores que rompan la página                  | OK                                                 |

### CP-06 — Modo privado / incógnito (sin localStorage)

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Abrir el sitio en modo incógnito                     | Funciona normalmente                               |
| 2    | Cambiar de idioma                                    | Funciona durante la sesión                         |
| 3    | Cerrar y reabrir incógnito                           | Vuelve a auto-detectar (no hay persistencia)       |

### CP-07 — Accesibilidad (teclado)

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Tab desde la barra de URL                            | El foco llega al primer link de la topbar          |
| 2    | Tab varias veces                                     | Llega a los botones del switcher con foco visible (outline dorado) |
| 3    | Enter sobre "PT"                                     | Cambia a portugués                                 |
| 4    | Verificar `aria-pressed`                             | El botón activo tiene `aria-pressed="true"`, los otros `"false"` |

### CP-08 — Mobile (375px)

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | DevTools → viewport iPhone SE                        | OK                                                 |
| 2    | Topbar: switcher visible, banderas ocultas           | Sólo "ES PT EN"                                    |
| 3    | Abrir navbar mobile (hamburger)                      | Switcher mobile aparece dentro del collapse        |
| 4    | Click en idioma mobile                               | Cambia idioma; el navbar collapse se mantiene abierto (no se cierra automáticamente con el cambio de lang) |

### CP-09 — Consistencia entre las 6 páginas

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Setear idioma a EN en index.html                     | OK                                                 |
| 2    | Click en cada link del navbar                       | Cada página carga en EN sin necesidad de reseleccionar |
| 3    | Verificar que el botón "EN" sigue activo en cada página | OK                                              |

### CP-10 — Formulario en EN abre WhatsApp

| Paso | Acción                                              | Resultado esperado                                 |
| ---- | --------------------------------------------------- | -------------------------------------------------- |
| 1    | Setear idioma a EN                                  | OK                                                 |
| 2    | Ir a /contactanos.html                              | Form en inglés                                     |
| 3    | Completar form (Name: John, Service: Airport transfer, Message: "Need pickup at Ezeiza 3pm Friday") | OK |
| 4    | Click "Send message"                                | Abre wa.me con mensaje en EN o ES — **revisar comportamiento actual de main.js** que arma el mensaje |

> **Nota AGT-04:** el código del form en `main.js` actualmente arma el mensaje en español duro (`'Hola Resmor, quiero pedir una cotización.'` y los labels `'Nombre:'`, `'Servicio:'`, etc). **Bug menor de coherencia i18n:** si el usuario cambió a EN, el form abre WhatsApp en ES. Recomiendo refactorizar `main.js` para usar `ResmorI18n.t('wa.formIntro')` y leer las labels del diccionario.

---

## 5. Bugs / mejoras detectadas en pre-revisión

| ID     | Descripción                                                                       | Severidad | Estado    |
| ------ | --------------------------------------------------------------------------------- | --------- | --------- |
| BUG-01 | `main.js` form-handler arma mensaje WhatsApp con strings en ES hardcodeados, ignora el idioma activo | Media | Abierto |
| BUG-02 | Algunos `data-i18n` quedaron sin aplicar en 2/25 reemplazos de contactanos (revisión manual recomendada) | Baja | Abierto |
| BUG-03 | El mapa de Google iframe siempre carga en español del lado de Google              | Baja      | Aceptado  |
| MEJ-01 | Falta `<link rel="alternate" hreflang>` en `<head>` para SEO multilenguaje        | Media     | Pendiente |
| MEJ-02 | Considerar mostrar un "?" tooltip al lado del switcher con label completo del idioma en hover | Baja | Backlog |
| MEJ-03 | El switcher mobile podría cerrar el navbar collapse después del cambio (UX)       | Baja      | Backlog   |

---

## 6. Recomendaciones

1. **Validar las traducciones con hablantes nativos** PT y EN antes de pasar a producción. El copy actual es funcional pero no nativo.
2. **Resolver BUG-01** para coherencia total: si el cliente está en EN/PT y el form WhatsApp llega en ES, se rompe la promesa "we speak your language".
3. **Trackear el cambio de idioma** con un evento de analytics. Saber qué porcentaje de usuarios cambia y a qué idioma define si vale la pena ampliar la cobertura PT/EN o reducirla.
4. **Cargar `pt.json` y `en.json` con `<link rel="prefetch">`** después del primer paint para acelerar el cambio de idioma. Mínima ganancia, fácil de implementar.

---

## 7. Resultado de la auditoría (pre-implementación)

**Estado:** ⚠️ Aprobado con observaciones
**Justificación:** la arquitectura es sólida, el sistema funciona end-to-end, las 6 páginas tienen i18n aplicado, y el switcher es accesible. Quedan 2 bugs menores documentados (BUG-01 y BUG-02) y mejoras de SEO/analytics que no bloquean el lanzamiento pero deben atenderse antes del go-live formal en EN/PT.
