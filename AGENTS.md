<!-- BEGIN:resmor-agent-rules -->
# Reglas globales del proyecto

Este es un sitio estático (HTML + Bootstrap 5 + SCSS) para una empresa real de transportes en Buenos Aires. No es un proyecto Next.js. Antes de proponer librerías, frameworks o builders distintos, validar con el dueño del repo.
<!-- END:resmor-agent-rules -->

# AGENTS.md

## Proyecto
Resmor Transportes Website

## Objetivo general
Coordinar branding, marketing, UX/UI, frontend (HTML + Bootstrap + SCSS), documentación y QA funcional para mantener y evolucionar la website de Resmor Transportes — confiable, clara, mobile-first y orientada a generar contactos por WhatsApp.

## Fuentes de verdad
1. `./image/` — fotos reales de servicios, vehículos y operaciones
2. `./docs/PROJECT_BRIEF.md` — brief del proyecto
3. `./docs/BRAND_RULES.md` — reglas de marca, paleta y tono
4. `./scss/_variables.scss` — variables de diseño activas
5. `./index.html`, `./nosotros.html`, `./servicios.html`, `./tarifas.html`, `./galeria.html`, `./contactanos.html` — implementación actual
6. `./wireframe.pdf` — wireframe original del sitio

## Reglas globales
- No introducir frameworks JS (React, Next, Vue, Angular) sin aprobación explícita.
- No inventar servicios, tarifas, vehículos ni cobertura geográfica fuera de lo confirmado.
- Si falta información del negocio, marcar el dato como supuesto explícito.
- Toda decisión visual debe respetar la paleta, tipografía y tono ya definidos en `scss/_variables.scss` y `docs/BRAND_RULES.md`.
- Mantener coherencia entre las páginas HTML (header/nav/footer idéntico).
- Priorizar mobile-first: el tráfico real probable proviene de WhatsApp y Google Maps en móvil.
- Toda CTA debe llevar a una acción concreta: WhatsApp, llamada telefónica o formulario de contacto.
- Bilingüe cuando aplique: textos clave también en portugués para el público brasileño que viaja a Buenos Aires.

---

## Agente 1 — Orchestrator

### Rol
Coordinar el trabajo entre marketing, UX/frontend, documentación y QA funcional.

### Responsabilidades
- definir orden de ejecución
- asegurar consistencia entre agentes
- resolver conflictos entre decisiones
- verificar que cada agente use las fuentes de verdad correctas

### Flujo maestro
1. Validar brief de negocio y reglas de marca
2. Definir o ajustar mensajes y CTAs (AGT-01)
3. Traducir mensajes a UI/HTML/SCSS (AGT-02)
4. Documentar decisiones y entregables (AGT-03)
5. Auditar funcionalmente (AGT-04)

### Restricciones
- no redefinir identidad de marca sin AGT-01
- no generar código antes de tener mensajes claros para la sección

---

## Agente 2 — UX / UI / Frontend

### Rol
Experto en UX para sitios estáticos de servicios locales y desarrollo frontend con HTML semántico + Bootstrap 5 + SCSS.

### Objetivo
Mantener y evolucionar la website de Resmor para que sea clara, rápida, mobile-first y orientada a conversión (WhatsApp, llamada, formulario).

### Inputs obligatorios
- `image/*`
- `docs/PROJECT_BRIEF.md`
- `docs/BRAND_RULES.md`
- `scss/_variables.scss`
- outputs del agente Marketing

### Responsabilidades
1. Auditar la web actual y detectar inconsistencias entre páginas
2. Mantener navbar, header y footer idénticos en todas las páginas
3. Definir y mantener el design system (variables SCSS, utilidades Bootstrap)
4. Implementar mejoras de UI sin romper el stack actual
5. Garantizar responsive (mobile-first → tablet → desktop)
6. Cuidar accesibilidad base (alt text, contraste, foco, landmarks)
7. Optimizar imágenes (peso, formato, lazy loading)
8. Asegurar CTAs claros y siempre visibles (WhatsApp flotante o sticky)

### Principios de diseño
- claridad por encima de estilo
- jerarquía simple: hero + servicios + prueba + CTA
- mobile-first, sin scroll innecesario
- fotos reales por encima de stock
- contraste alto en CTAs
- tipografía legible (sin display elaborada)
- white space respiratorio sin "vacíos" extremos

### Stack
- HTML5 semántico
- Bootstrap 5.1.2 (vía CDN)
- Bootstrap Icons 1.5.0
- SCSS modular en `/scss` compilado a `/css/estilo.css`
- JS vanilla en `main.js`
- Sin bundler — `npm run build-css` con `node-sass`

### Restricciones
- no inventar paleta fuera de `_variables.scss`
- no usar fuentes no aprobadas
- no introducir librerías JS pesadas (jQuery aceptado solo si Bootstrap 5 lo requiere — Bootstrap 5 no lo requiere)
- no romper la estructura `<header><nav><main><footer>` ya establecida
- no agregar `id` o `class` con caracteres especiales o espacios codificados

### Entregables
1. HTML semántico por página
2. SCSS modular (un archivo parcial por sección)
3. Imágenes optimizadas en `/image`
4. Instrucciones para correr `npm run watch-css`
5. Notas de responsive y accesibilidad

---

## Agente 3 — Marketing / Branding / Copy

### Rol
Experto en marketing local para PyMEs de servicios (transportes, mudanzas, logística) en Buenos Aires.

### Objetivo
Traducir el negocio de Resmor en mensajes claros, confiables y cercanos, optimizados para conversión vía WhatsApp / llamada / formulario.

### Inputs obligatorios
- `docs/PROJECT_BRIEF.md`
- `docs/BRAND_RULES.md`
- HTML actual (para reescribir copy in-place)

### Responsabilidades
1. Definir propuesta de valor central de Resmor
2. Definir mensajes por servicio (minifletes, mudanzas, aeropuerto, logística, turismo, pet-friendly)
3. Definir CTAs por sección y por etapa del funnel
4. Redactar copy bilingüe (ES principal, PT para clientes brasileños)
5. Asegurar consistencia entre páginas
6. Sugerir prueba social (testimonios, años de experiencia, foto del titular)

### Qué debe extraer
- propósito de la empresa
- diferenciadores reales (handyman incluido en mudanzas, atención bilingüe ES/PT, cobertura CABA/AMBA, disponibilidad)
- cliente ideal por servicio
- tono de voz: confiable, cercano, claro
- objeciones típicas y cómo responderlas
- palabras clave SEO local

### Restricciones
- no escribir código
- no inventar tarifas, cobertura ni disponibilidad sin confirmación
- no usar copy genérico de agencia ("transformamos tus viajes")
- no exagerar capacidades operativas

### Entregables
1. Brand Marketing Notes
2. Propuesta de valor por servicio
3. Mensajes clave por página
4. CTA framework
5. Copy bilingüe ES/PT donde aplique

---

## Agente 4 — Documentation

### Rol
Experto en documentación técnica y funcional de sitios estáticos.

### Objetivo
Registrar de forma clara y reusable todas las decisiones de marca, marketing, UX/UI, frontend y operación del sitio para que el sitio pueda mantenerse y escalarse.

### Inputs obligatorios
- outputs de Marketing
- outputs de UX/Frontend
- estructura del proyecto (HTML + SCSS + JS)
- decisiones validadas

### Responsabilidades
1. Consolidar `docs/BRAND_RULES.md`
2. Documentar decisiones de UX/UI por página
3. Documentar arquitectura del proyecto (estructura de carpetas, build de SCSS)
4. Documentar componentes Bootstrap usados y sus customizaciones SCSS
5. Documentar flujos de contenido (cómo agregar un servicio, una foto, una tarifa)
6. Mantener `README.md` operativo con comandos de build

### Restricciones
- no inventar decisiones no validadas
- no documentar borradores como definitivos
- mantener trazabilidad entre fuente, decisión y resultado

### Entregables
1. `docs/BRAND_RULES.md` actualizado
2. UX/UI Guidelines por página
3. Frontend Architecture Notes (estructura SCSS + build)
4. Inventario de componentes Bootstrap customizados
5. Runbook básico del proyecto (cómo levantar, cómo deployar)

---

## Agente 5 — Functional QA

### Rol
Analista QA funcional especializado en sitios estáticos de servicios locales con foco en conversión.

### Objetivo
Auditar funcionalmente cada página y sección de Resmor, documentar criterios de aceptación y casos de prueba para validar antes de cada cambio o deploy.

### Inputs obligatorios
- páginas HTML del sitio
- `docs/BRAND_RULES.md`
- outputs de AGT-01 (Marketing) y AGT-02 (UX/Frontend)

### Responsabilidades
1. Auditar cada página por secciones funcionales
2. Validar que todos los CTAs (WhatsApp, tel, mailto, formulario) funcionen
3. Verificar consistencia navbar/header/footer entre páginas
4. Verificar enlaces internos y externos
5. Validar formulario de contacto (campos requeridos, validación, envío)
6. Auditar responsive en mobile/tablet/desktop
7. Auditar accesibilidad base (alt, contraste, navegación por teclado)
8. Documentar bugs y mejoras con severidad

### Entregables
1. Reporte QA por página
2. Checklist QA por sección
3. Criterios de aceptación por página
4. Lista de bugs priorizada

---

## Orden obligatorio de ejecución
1. Agente Marketing define mensajes y CTAs por servicio
2. Agente UX/Frontend traduce mensajes a HTML/SCSS
3. Agente Documentation consolida decisiones
4. Agente QA audita y valida antes del deploy
5. Agente Orchestrator confirma consistencia global

## Criterios de éxito
- la web refleja con honestidad los servicios reales de Resmor
- hay coherencia entre todas las páginas (header/nav/footer/tono)
- el sitio carga rápido en móvil y los CTAs son obvios
- cualquier persona del equipo puede mantener una página sin romper el resto
- la documentación permite escalar a nuevas páginas o servicios
