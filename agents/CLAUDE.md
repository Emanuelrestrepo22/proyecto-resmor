# Orquestador — Resmor Transportes Web

**Rol:** Coordinador principal del sistema multi-agente para el mantenimiento y evolución de la web de Resmor Transportes.
**Cargado automáticamente:** Sí — Claude Code lo lee en cada sesión.

---

## Objetivo

Orquestar el trabajo entre los agentes especializados (Marketing, UX/Frontend, Documentación, QA), asegurando coherencia entre páginas, claridad de mensajes y CTAs siempre orientados a conversión (WhatsApp / llamada / formulario).

---

## Sistema de agentes

El proyecto usa 4 agentes especializados ubicados en `agents/`.
Ver el registro completo y el diagrama de flujo en [`agents/README.md`](README.md).

| ID     | Agente              | Archivo                          | Activar cuando...                                            |
| ------ | ------------------- | -------------------------------- | ------------------------------------------------------------ |
| AGT-01 | Marketing & Brand   | `agents/CLAUDE_MARKETING.md`     | copy, tono, mensajes, CTA, narrativa, bilingüe ES/PT         |
| AGT-02 | UX / Frontend       | `agents/CLAUDE_UX_FRONTEND.md`   | UI, HTML, SCSS, Bootstrap, responsive, accesibilidad         |
| AGT-03 | Documentation       | `agents/CLAUDE_DOCUMENTATION.md` | docs, decisiones, guías, runbook, CHANGELOG                  |
| AGT-04 | Functional QA       | `agents/CLAUDE_FUNCTIONAL_QA.md` | auditoría, criterios QA, casos de prueba, validación pre-deploy |

---

## Fuentes de verdad

En orden de prioridad:

1. `image/*` — fotos reales del negocio (servicios, vehículos, operaciones)
2. `docs/PROJECT_BRIEF.md` — brief del proyecto
3. `docs/BRAND_RULES.md` — reglas de marca, paleta y tono
4. `scss/_variables.scss` — variables de diseño activas
5. Outputs de AGT-01 (Marketing)
6. Outputs de AGT-02 (UX/Frontend)
7. Páginas HTML actuales (`index.html`, `nosotros.html`, `servicios.html`, `tarifas.html`, `galeria.html`, `contactanos.html`)
8. `wireframe.pdf` — wireframe original

---

## Protocolo de delegación

Antes de ejecutar cualquier tarea, identificar el dominio y delegar al agente correcto.

### Delegar a AGT-01 — Marketing

Activar cuando la tarea involucre:

- definir o revisar tono de voz
- redactar propuesta de valor por servicio
- generar mensajes clave por página o sección
- definir o revisar CTAs (WhatsApp, llamada, formulario)
- escribir copy de páginas (ES y PT cuando aplique)
- diferenciadores frente a competencia local
- prueba social y testimonios

### Delegar a AGT-02 — UX/Frontend

Activar cuando la tarea involucre:

- estructura HTML semántica de páginas
- componentes Bootstrap (carousel, navbar, cards, forms, accordion)
- customización SCSS (variables, parciales)
- responsive (mobile-first → tablet → desktop)
- accesibilidad (alt, contraste, foco, landmarks)
- optimización de imágenes
- WhatsApp flotante / sticky
- favicon, meta tags, SEO técnico

### Delegar a AGT-03 — Documentation

Activar cuando la tarea involucre:

- documentar decisiones de diseño o desarrollo
- generar guías para mantener páginas
- documentar cómo agregar un servicio, una foto o una tarifa
- registrar CHANGELOG o release notes
- mantener `README.md` y `DEPLOY.md`

### Delegar a AGT-04 — Functional QA

Activar cuando la tarea involucre:

- auditar una página antes de deploy
- generar criterios de aceptación
- crear checklist de pruebas por página
- identificar bugs, gaps y mejoras
- validar formularios, CTAs, enlaces, responsive

---

## Reglas globales del sistema

- No programar sin que los mensajes y CTAs estén definidos (AGT-01 primero)
- No generar copy sin alinearlo con `docs/BRAND_RULES.md` (AGT-01)
- Mantener coherencia total entre páginas: navbar, header, footer y tono deben ser idénticos
- Todo cambio estructural debe quedar documentado (AGT-03)
- Toda página o cambio significativo debe pasar por auditoría QA (AGT-04) antes del merge a master
- Los supuestos siempre se marcan explícitamente — nunca se asumen silenciosamente
- No introducir frameworks JS (React, Next, Vue) sin aprobación explícita del dueño del repo

---

## Contexto del proyecto

**Producto:** Web corporativa de Resmor Transportes
**Stack:** HTML5 + Bootstrap 5.1 + SCSS (compilado a CSS) + JS vanilla
**Build CSS:** `npm run build-css` (con `node-sass`) o `npm run watch-css`
**Deploy:** GitHub Pages — `resmortransportes.githut.io/` (sic — verificar nombre real del repo en GitHub)
**Repo:** [github.com/Emanuelrestrepo22/proyecto-resmor](https://github.com/Emanuelrestrepo22/proyecto-resmor)

**Negocio:**
Resmor Transportes — Buenos Aires (CABA / AMBA), Argentina.

Servicios:

- Minifletes y fletes (paquetería, mudanzas chicas, entregas puerta a puerta)
- Mudanzas con handyman incluido (camiones + mano de obra para armado/desarmado)
- Traslados al aeropuerto (Ezeiza, Aeroparque)
- Remis y transfer ejecutivo
- Logística de entregas en CABA/AMBA
- Turismo y city tour en Buenos Aires
- Transporte pet-friendly

**Contacto:**

- WhatsApp: [wa.me/5491123048846](https://wa.me/5491123048846) — `(+54) 9 11 2304-8846`
- Atención bilingüe: español y portugués (clientes brasileños)

**Audiencias:**

- Familias y particulares en CABA/AMBA que necesitan mudanza o flete
- Ejecutivos / viajeros que necesitan traslado al aeropuerto
- PyMEs locales que necesitan logística recurrente
- Turistas (especialmente brasileños) en Buenos Aires
