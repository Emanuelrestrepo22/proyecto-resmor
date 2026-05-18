# Analytics — Resmor Web

**Agente:** AGT-03 Documentation
**Estado:** Implementado · placeholder GA ID a reemplazar al deploy
**Stack:** Google Analytics 4 vía `gtag.js` (sin Tag Manager por ahora)

---

## 1. Visión general

`js/analytics.js` instrumenta el sitio con:

- **page_view** (automático por GA4)
- **lang_change** — dispara cuando el usuario cambia idioma vía el toggle
- **cta_click** — dispara en cualquier click sobre `wa.me` o `tel:` con metadata del servicio
- **form_submit** — dispara cuando se envía el formulario de contacto

Filosofía: **medir lo que decide negocio**. No tracking obsesivo. Pocas señales bien dirigidas.

---

## 2. Setup inicial (5 minutos)

### Paso 1 — Crear propiedad GA4

1. Ir a https://analytics.google.com
2. Admin → Crear propiedad → "Resmor Transportes"
3. Configurar stream de datos web → URL `https://resmor.com.ar`
4. Copiar el **Measurement ID** (formato `G-XXXXXXXXXX`)

### Paso 2 — Configurar el ID en el sitio

**Opción A — quick fix (1 archivo):**

Editar [js/analytics.js](../../js/analytics.js) línea 14:

```js
const GA_ID = window.RESMOR_GA_ID || 'G-XXXXXXXXXX';
```

Reemplazar `G-XXXXXXXXXX` por el ID real.

**Opción B — vía variable global (recomendado para staging vs prod):**

En cada HTML antes de cargar `analytics.js`:

```html
<script>window.RESMOR_GA_ID = 'G-ABC123XYZ';</script>
<script src="./js/analytics.js"></script>
```

Mientras `GA_ID` esté en placeholder, `gtag` opera en **modo stub**: registra eventos en consola si `window.RESMOR_GA_DEBUG = true`, pero no manda nada a GA. Esto evita ruido en métricas durante desarrollo.

### Paso 3 — Validar

1. Abrir el sitio con el ID real configurado.
2. GA4 → Reports → Realtime: deberías ver tu sesión.
3. DevTools → Network → filtrar `collect` → deberías ver los POST a Google Analytics.

---

## 3. Eventos custom — Schema

### `lang_change`

| Param | Tipo   | Ejemplo | Descripción                              |
| ----- | ------ | ------- | ---------------------------------------- |
| from  | string | `es`    | Idioma previo                            |
| to    | string | `en`    | Idioma nuevo seleccionado                |

**Trigger:** evento DOM `resmor:langchange` emitido por `js/i18n.js`.

**Pregunta que responde:** ¿qué porcentaje de visitas cambian de idioma? ¿hacia cuál? ¿desde qué páginas?

### `cta_click`

| Param         | Tipo   | Ejemplo                  | Descripción                                       |
| ------------- | ------ | ------------------------ | ------------------------------------------------- |
| channel       | string | `whatsapp` / `phone`     | Canal del CTA                                     |
| service       | string | `airport` / `mudanzas`   | Servicio (de `data-i18n-wa`)                      |
| source        | string | `whatsapp_float`         | Origen del click (`inline`, `service_card`, etc.) |
| language      | string | `en`                     | Idioma activo al momento del click                |
| page_location | string | `/servicios.html`        | Path de la página                                 |

**Trigger:** cualquier click sobre `a[href*="wa.me/"]` o `a[href^="tel:"]`. Captura en fase de captura para no perder clicks de elementos anidados.

**Pregunta que responde:** ¿qué servicios convierten más? ¿WhatsApp flotante vs CTAs in-page? ¿qué idioma genera más clicks?

### `form_submit`

| Param         | Tipo   | Ejemplo            | Descripción                                |
| ------------- | ------ | ------------------ | ------------------------------------------ |
| service       | string | `aeropuerto`       | Servicio elegido en el select del form     |
| language      | string | `pt`               | Idioma activo                              |
| page_location | string | `/contactanos.html`| Path                                       |

**Trigger:** submit del `<form id="contactForm">` (sólo si pasó la validación HTML5).

**Pregunta que responde:** ¿cuántas cotizaciones llegan por formulario? ¿en qué idioma?

---

## 4. Custom dimensions a configurar en GA4

Después del primer deploy con datos reales, registrar estas dimensiones para poder segmentar reports:

| Dimensión              | Scope  | Event Parameter |
| ---------------------- | ------ | --------------- |
| Idioma del cliente     | Event  | `language`      |
| Servicio del CTA       | Event  | `service`       |
| Canal del CTA          | Event  | `channel`       |
| Origen del CTA         | Event  | `source`        |
| Idioma anterior        | Event  | `from`          |
| Idioma nuevo           | Event  | `to`            |

Setup: Admin → Custom definitions → Create custom dimension.

---

## 5. Reports recomendados

### Report 1 — Distribución de tráfico por idioma

- **Métrica:** Active users
- **Dimensión:** Custom dimension "Idioma del cliente"
- **Filtro:** event_name = `cta_click` OR `page_view`

Output esperado: % visitas en ES vs PT vs EN. Si EN/PT < 5%, hay que reforzar SEO o adquisición pagada para esos segmentos.

### Report 2 — Top servicios por clicks WhatsApp

- **Métrica:** event_count
- **Dimensión:** Custom dimension "Servicio del CTA"
- **Filtro:** event_name = `cta_click` AND channel = `whatsapp`

Output esperado: ranking de demanda. Define qué servicio destacar en hero, qué keywords priorizar SEO.

### Report 3 — Conversión por idioma

- **Métrica:** Conversion rate
- **Dimensión:** "Idioma del cliente"
- **Conversion:** event `cta_click` OR `form_submit`

Output esperado: cuál idioma convierte mejor. Si EN convierte 3× sobre ES, vale más la pena traducir bien EN que ES.

### Report 4 — Eficacia del language toggle

- **Métrica:** event_count
- **Dimensión:** `from`, `to`
- **Filtro:** event_name = `lang_change`

Output esperado: ¿cuántas visitas cambian de idioma? ¿cuál es el flujo más común (auto-detect ES → cambio manual EN)? Si nadie cambia, podemos simplificar la UI.

---

## 6. Conversiones (objetivos clave)

Marcar como **Conversion** en GA4 → Admin → Events → Mark as conversion:

| Evento         | Por qué                                                 |
| -------------- | ------------------------------------------------------- |
| `form_submit`  | Lead capturado por formulario                           |
| `cta_click`    | Lead WhatsApp / llamada (no es submit, pero es intent)  |

Para `cta_click`, considerar crear un evento derivado `whatsapp_intent` filtrando `channel=whatsapp` y marcarlo como conversión.

---

## 7. Privacidad y consentimiento

- `analytics.js` configura `anonymize_ip: true` por default.
- **No incluye Consent Mode aún.** Si Resmor publica el sitio para clientes UE, hay que agregar banner de consentimiento + `gtag('consent', 'default', {...})`. Para mercado AR/BR/US el riesgo legal es menor pero no nulo.
- No se envían datos personales del formulario (nombre, email, teléfono) a GA. Sólo el nombre del servicio y el idioma.

### Cuando se haga release con Consent Mode

1. Agregar banner de cookies (proponer librería liviana como `klaro!` o implementación propia).
2. Configurar `gtag('consent', 'default', { analytics_storage: 'denied' })` antes de cargar gtag.js.
3. Al aceptar: `gtag('consent', 'update', { analytics_storage: 'granted' })`.

---

## 8. Eventos opcionales a sumar más adelante

| Evento              | Cuándo                                                   |
| ------------------- | -------------------------------------------------------- |
| `scroll_depth`      | Cuando se llega al 25/50/75/100% del hero o página       |
| `outbound_click`    | Click a Instagram/Facebook en el footer                  |
| `landing_seo_view`  | Page view de las landings dedicadas (PT/EN)              |
| `gallery_image_view`| Hover/click en una foto de la galería                    |
| `faq_open`          | Apertura de un `<details>` en las landings (FAQPage)     |

No implementar hasta que haya tráfico suficiente para justificarlos.

---

## 9. Tag Manager (futuro)

Si el día de mañana se quiere instrumentar Facebook Pixel, LinkedIn Insight, o Hotjar, conviene migrar a **Google Tag Manager** para no embarrar `analytics.js`. La estructura actual de eventos custom (`data-i18n-wa`, `id="contactForm"`, etc.) hace fácil el porteo.

---

## 10. Troubleshooting

| Síntoma                              | Posible causa                              | Solución                                   |
| ------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| GA4 no muestra Realtime              | `GA_ID` sigue en placeholder               | Reemplazar `G-XXXXXXXXXX` en `analytics.js`|
| Eventos no aparecen en DebugView     | DebugView requiere extensión GA4 Debugger  | Instalar GA4 Debugger Chrome extension     |
| `cta_click` no dispara               | Click sobre elemento sin `wa.me` o `tel:` | Verificar `href` del `<a>`                 |
| `lang_change` no dispara             | `i18n.js` no está cargando o no emite      | Verificar consola; activar `RESMOR_GA_DEBUG=true` |
| Eventos duplicados                   | El listener está en capture, no debería duplicar; revisar si hay re-render del DOM | Inspeccionar `document.querySelectorAll('a[href*="wa.me"]')` count |

---

## 11. Verificación local sin GA real

En consola del browser:

```js
window.RESMOR_GA_DEBUG = true;
// Ahora cada gtag('event', ...) imprime en consola
ResmorAnalytics.track('test_event', { foo: 'bar' });
// → [analytics:stub] event test_event { foo: 'bar' }
```

Útil para verificar que los listeners están bindeados antes del deploy.

---

## 12. Checklist pre-go-live

- [ ] Crear propiedad GA4 con dominio real `https://resmor.com.ar`
- [ ] Reemplazar `G-XXXXXXXXXX` en `js/analytics.js`
- [ ] Configurar las 6 custom dimensions en GA4
- [ ] Marcar `form_submit` y `cta_click` como conversions
- [ ] Validar con GA4 Debugger en staging antes de producción
- [ ] Decidir si se necesita Consent Mode (mercado objetivo)
- [ ] Documentar la propiedad en el inventario de cuentas de Resmor
