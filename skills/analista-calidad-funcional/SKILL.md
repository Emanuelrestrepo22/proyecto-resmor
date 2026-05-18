---
name: analista-calidad-funcional
description: Skill especializada para auditar funcionalmente páginas del sitio Resmor Transportes (HTML + Bootstrap 5 + SCSS). Esta skill se debe usar cuando el usuario pida auditar una página antes de un deploy, validar consistencia entre páginas, generar criterios de aceptación, crear checklist QA o documentar bugs y mejoras. Orquesta al agente AGT-04 (Functional QA) con criterios específicos de Resmor: validación de CTAs WhatsApp/tel, consistencia navbar/footer entre páginas, formulario de contacto, responsive mobile-first y accesibilidad base.
metadata:
  type: skill
  versión: 1.0
  agente_base: AGT-04
---

# Skill — Analista de Calidad Funcional (Resmor Transportes)

## Propósito

Ejecutar auditorías funcionales completas sobre páginas o flujos del sitio Resmor Transportes Web.

Orquesta al agente AGT-04 con contexto enriquecido del negocio (servicios, audiencias, canal principal WhatsApp) y checklists específicos del stack HTML + Bootstrap 5 + SCSS.

---

## Cuándo usar este skill

- Al terminar de implementar o modificar una página
- Antes de hacer un merge a `master` o deploy a GitHub Pages
- Al detectar inconsistencias visibles entre páginas
- Para generar documentación de aceptación formal antes de entregar al cliente
- Para auditar el formulario de contacto o los CTAs de WhatsApp

---

## Cómo ejecutar

```
/skill analista-calidad-funcional [página o flujo a auditar]
```

**Ejemplos:**

```
/skill analista-calidad-funcional index.html
/skill analista-calidad-funcional contactanos.html
/skill analista-calidad-funcional flujo-whatsapp
/skill analista-calidad-funcional consistencia-navbar
```

---

## Inputs requeridos

| Input              | Descripción                                     | Obligatorio |
| ------------------ | ----------------------------------------------- | ----------- |
| `página`           | Nombre del HTML o flujo a auditar               | Sí          |
| `contexto`         | Cambios recientes relevantes                    | No          |
| `criterios_extra` | Criterios específicos adicionales              | No          |

---

## Outputs generados

1. Reporte QA en `docs/qa/QA_[PÁGINA]_v[n].md`
2. Lista de bugs con severidad (Alta / Media / Baja)
3. Criterios de aceptación documentados
4. Checklist QA específico para Resmor (ver criterios obligatorios abajo)
5. Estado final: **Aprobado** / **Requiere cambios** / **Aprobado con observaciones**

---

## Criterios QA obligatorios para Resmor

Toda auditoría debe verificar como mínimo:

1. **Consistencia entre páginas:** navbar, header y footer idénticos en TODAS las páginas (`index`, `nosotros`, `servicios`, `tarifas`, `galeria`, `contactanos`).
2. **CTA WhatsApp:** abre `https://wa.me/5491123048846` con mensaje pre-cargado.
3. **CTA tel:** `tel:+5491123048846` clickeable en mobile.
4. **Formulario de contacto:** valida campos requeridos, mensaje de error claro, destino real.
5. **Carousel:** auto-play funciona, controles funcionan, imágenes cargan.
6. **Imágenes:** todas con `alt` descriptivo, peso razonable.
7. **Enlaces internos:** la navbar lleva a las páginas correctas desde cualquier página.
8. **Responsive 375px:** sin scroll horizontal, jerarquía clara.
9. **Contraste:** texto sobre imágenes legible (AA mínimo).
10. **Foco visible:** navegación por teclado sin perder elemento activo.
11. **Meta tags:** `<title>` y `<meta description>` únicos por página.
12. **Sin errores en consola:** ni JS, ni 404 de assets.
13. **Bilingüe:** donde se haya decidido aplicar ES/PT, consistencia entre páginas.

---

## Referencias internas

- Plantilla base: [`../../templates/qa/TEMPLATE_QA.md`](../../templates/qa/TEMPLATE_QA.md)
- Brief del proyecto: [`../../docs/PROJECT_BRIEF.md`](../../docs/PROJECT_BRIEF.md)
- Reglas de marca: [`../../docs/BRAND_RULES.md`](../../docs/BRAND_RULES.md)
- Agente QA: [`../../agents/CLAUDE_FUNCTIONAL_QA.md`](../../agents/CLAUDE_FUNCTIONAL_QA.md)
- Agente UX/Frontend: [`../../agents/CLAUDE_UX_FRONTEND.md`](../../agents/CLAUDE_UX_FRONTEND.md)

<!-- TODO: Agregar criterios de aceptación globales una vez aprobados con el dueño del negocio -->
