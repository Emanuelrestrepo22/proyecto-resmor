# Sistema de Agentes — Resmor Transportes Web

> **Orquestador principal:** `CLAUDE.md` (root) — cargado automáticamente por Claude Code en cada sesión.
> **Sub-agentes:** esta carpeta `agents/` — activados bajo demanda según el dominio de la tarea.

---

## Registro de agentes

| ID     | Archivo                          | Rol                 | Dominio                                  | Estado    |
| ------ | -------------------------------- | ------------------- | ---------------------------------------- | --------- |
| AGT-00 | `../CLAUDE.md`                   | Orquestador         | Coordinación global                      | Activo    |
| AGT-01 | `CLAUDE_MARKETING.md`            | Marketing & Brand   | Estrategia, copy, narrativa, ES/PT       | Activo    |
| AGT-02 | `CLAUDE_UX_FRONTEND.md`          | UX / Frontend       | HTML, Bootstrap 5, SCSS, responsive      | Activo    |
| AGT-03 | `CLAUDE_DOCUMENTATION.md`        | Documentación       | Docs técnicas y funcionales              | Activo    |
| AGT-04 | `CLAUDE_FUNCTIONAL_QA.md`        | QA Funcional        | Auditoría, criterios, pruebas pre-deploy | Activo    |

---

## Diagrama de flujo entre agentes

```
Usuario / Negocio
        │
        ▼
┌──────────────────┐
│   ORQUESTADOR    │  CLAUDE.md (root)
│   AGT-00         │  Recibe la tarea, identifica el dominio
│                  │  y delega al agente correcto
└────────┬─────────┘
         │
    ┌────┴────────────────────────────────┐
    │                                     │
    ▼                                     ▼
AGT-01 MARKETING               AGT-02 UX / FRONTEND
Mensajes por servicio          HTML + Bootstrap + SCSS
Copy ES/PT, CTAs               Responsive, accesibilidad
    │                                     │
    └──────────────┬──────────────────────┘
                   │
                   ▼
          AGT-03 DOCUMENTATION
          Documenta decisiones,
          guías de mantenimiento
                   │
                   ▼
          AGT-04 FUNCTIONAL QA
          Audita pre-deploy,
          criterios y bugs
```

---

## Cuándo activar cada agente

### AGT-01 — Marketing
Activar cuando la tarea involucre:
- definición de tono de voz
- propuesta de valor por servicio (minifletes, mudanzas, aeropuerto, etc.)
- redacción de copy para la web (ES y PT)
- definición de CTA (WhatsApp / llamada / formulario)
- diferenciadores reales frente a competencia local
- prueba social, testimonios, años de experiencia

**Instrucción:** `Usa el agente CLAUDE_MARKETING.md para esta tarea.`

---

### AGT-02 — UX / Frontend
Activar cuando la tarea involucre:
- estructura HTML semántica de páginas
- componentes Bootstrap 5 (carousel, navbar, cards, forms, accordion, modal)
- customización SCSS (variables, parciales, responsive)
- accesibilidad base
- optimización de imágenes
- SEO técnico (meta tags, OG, favicon, sitemap)
- WhatsApp flotante / sticky CTA

**Instrucción:** `Usa el agente CLAUDE_UX_FRONTEND.md para esta tarea.`

---

### AGT-03 — Documentation
Activar cuando la tarea involucre:
- documentar decisiones de diseño o desarrollo
- crear guías para mantener una página
- documentar cómo agregar un servicio nuevo, una foto o una tarifa
- generar CHANGELOG o release notes
- mantener `README.md` y `DEPLOY.md`

**Instrucción:** `Usa el agente CLAUDE_DOCUMENTATION.md para esta tarea.`

---

### AGT-04 — Functional QA
Activar cuando la tarea involucre:
- auditar una página antes del deploy
- generar criterios de aceptación por página
- crear checklist de pruebas
- identificar bugs en CTAs, formularios, enlaces
- validar responsive (mobile / tablet / desktop)
- validar consistencia entre páginas (navbar/header/footer)

**Instrucción:** `Usa el agente CLAUDE_FUNCTIONAL_QA.md para esta tarea.`

---

## Protocolo de handoff entre agentes

Cuando un agente completa su trabajo y necesita pasar el output a otro:

```
AGT-01 → AGT-02   Marketing define mensajes y CTA → UX/Frontend los implementa en HTML
AGT-01 → AGT-03   Marketing define copy → Docs lo registra como Brand Notes
AGT-02 → AGT-03   UX/Frontend implementa → Docs documenta estructura y SCSS
AGT-02 → AGT-04   UX/Frontend implementa → QA audita pre-deploy
AGT-03 → AGT-04   Docs registra criterios → QA valida cumplimiento
```

---

## Fuentes de verdad del proyecto

En orden de prioridad:

1. `image/*` — fotos reales del negocio
2. `docs/PROJECT_BRIEF.md` — brief del proyecto
3. `docs/BRAND_RULES.md` — reglas de marca, paleta y tono
4. `scss/_variables.scss` — variables de diseño activas
5. Outputs de AGT-01 (Marketing)
6. Outputs de AGT-02 (UX/Frontend)
7. Páginas HTML actuales
8. `wireframe.pdf`

---

## Reglas globales del sistema

- Ningún agente puede programar sin que los mensajes y CTAs estén definidos (AGT-01 primero)
- Ningún agente puede generar copy sin alinearlo con `docs/BRAND_RULES.md`
- Todo cambio significativo debe quedar documentado (AGT-03)
- Toda página o cambio relevante debe pasar por auditoría QA (AGT-04) antes del merge a master
- Los supuestos siempre deben marcarse explícitamente
- No introducir frameworks JS sin aprobación del dueño del repo

---

## Stack del proyecto

| Categoría     | Tecnología                                            |
| ------------- | ----------------------------------------------------- |
| Markup        | HTML5 semántico                                       |
| CSS framework | Bootstrap 5.1.2 (vía CDN)                             |
| Iconos        | Bootstrap Icons 1.5.0 (vía CDN)                       |
| Estilos       | SCSS modular en `/scss` → `/css/estilo.css`           |
| JS            | Vanilla (`main.js`) + Bootstrap JS (CDN)              |
| Build         | `npm run build-css` / `npm run watch-css` (node-sass) |
| Deploy        | GitHub Pages                                          |
| Repo          | github.com/Emanuelrestrepo22/proyecto-resmor          |
