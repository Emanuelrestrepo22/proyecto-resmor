---
tipo: plantilla
dominio: qa
proyecto: Resmor Transportes
versión: 1.0
---

# Plantilla — Auditoría QA Funcional

## Página auditada
`[Nombre y ruta: /servicios.html]`

## Fecha
`[YYYY-MM-DD]`

## Agente responsable
AGT-04 — Functional QA

## Auditor / sesión
`[Claude / Emanuel / sesión #N]`

---

## 1. Información general

- **Página:**
- **Objetivo de conversión:** [WhatsApp / llamada / formulario]
- **Buyer persona objetivo:**
- **CTA principal:**
- **CTA secundarios:**
- **Dependencias:** WhatsApp / mailto / tel / formulario

---

## 2. Criterios de aceptación

| #     | Criterio                                                     | Estado     | Notas                          |
| ----- | ------------------------------------------------------------ | ---------- | ------------------------------ |
| CA-01 | Navbar idéntico al resto de páginas                          | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-02 | CTA WhatsApp abre wa.me con mensaje pre-cargado              | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-03 | Imágenes con `alt` descriptivo                               | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-04 | Responsive 375px sin scroll horizontal                       | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-05 | Formulario valida campos y muestra errores claros            | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-06 | `<title>` y `<meta description>` únicos                      | ✅ / ❌ / ⚠️ | `[observación]`                |
| CA-07 | Footer idéntico al resto de páginas                          | ✅ / ❌ / ⚠️ | `[observación]`                |

---

## 3. Checklist de pruebas

### 3.1 Funcionalidad

- [ ] Todos los CTAs llevan al destino correcto
- [ ] WhatsApp flotante abre `wa.me/5491123048846` en nueva pestaña
- [ ] `tel:` clickeable en mobile y abre dialer
- [ ] Formulario valida campos requeridos
- [ ] Mensajes de error son claros y visibles
- [ ] Carousel auto-play y controles funcionan
- [ ] Enlaces internos de navbar funcionan desde ESTA página

### 3.2 Consistencia entre páginas

- [ ] Navbar tiene exactamente las mismas opciones y enlaces
- [ ] Header (banda superior con contacto) idéntico
- [ ] Footer idéntico
- [ ] Tono de voz coherente con el resto del sitio
- [ ] Variables SCSS aplicadas (colores desde `_variables.scss`)

### 3.3 Responsive

- [ ] Mobile (375px) — sin desbordamientos ni scroll horizontal
- [ ] Mobile (575px) — layout adaptado
- [ ] Tablet (768px) — layout correcto, navbar colapsable
- [ ] Desktop (1200px+) — proporciones correctas, espaciados

### 3.4 Accesibilidad

- [ ] Imágenes tienen `alt` descriptivo (no `alt=""` salvo decorativas)
- [ ] Contraste de colores ≥ AA (4.5:1 para texto normal)
- [ ] Navegación por teclado funcional (Tab no se pierde)
- [ ] Foco visible en CTAs e inputs
- [ ] `aria-label` en botones sin texto (ej: WhatsApp flotante)
- [ ] Estructura de encabezados sin saltos (H1 → H2 → H3)

### 3.5 SEO técnico

- [ ] `<title>` único y descriptivo
- [ ] `<meta name="description">` único, 140-160 caracteres
- [ ] `<html lang="es">`
- [ ] Open Graph: `og:title`, `og:description`, `og:image` (si aplica)
- [ ] Favicon cargando correctamente
- [ ] Sin errores 404 en consola

### 3.6 Performance

- [ ] Imágenes optimizadas (peso razonable, <200KB en home)
- [ ] `loading="lazy"` en imágenes below-the-fold
- [ ] Bootstrap CSS y JS desde CDN (sin duplicar local)
- [ ] Sin JS bloqueante en el head

---

## 4. Bugs encontrados

| ID     | Descripción                                | Severidad         | Sección  | Estado    |
| ------ | ------------------------------------------ | ----------------- | -------- | --------- |
| BUG-01 | `[descripción concreta]`                   | Alta / Media / Baja | SEC-XX | Abierto   |

---

## 5. Recomendaciones

- Recomendación funcional: `[...]`
- Recomendación UX: `[...]`
- Recomendación QA: `[...]`

---

## 6. Resultado

**Estado general:** ✅ Aprobado / ❌ Requiere cambios / ⚠️ Aprobado con observaciones

**Justificación:** `[breve resumen del veredicto]`

<!-- TODO: Completar con hallazgos reales de la auditoría -->
