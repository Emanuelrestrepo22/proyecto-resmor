---
tipo: plantilla
dominio: ux
proyecto: Resmor Transportes
versión: 1.0
---

# Plantilla — Decisión de UX / Componente

## Componente / Sección
`[Nombre del componente o sección: navbar, hero-carousel, card-servicio, form-contacto, whatsapp-float]`

## Agente responsable
AGT-02 — UX / Frontend

---

## Descripción

> ¿Qué hace este componente y por qué existe? ¿A qué objetivo de conversión apunta?

## Variantes

| Variante       | Descripción                              | Cuándo usar                                 |
| -------------- | ---------------------------------------- | ------------------------------------------- |
| `default`      | `[descripción]`                          | `[contexto]`                                |
| `[variante]`   | `[descripción]`                          | `[contexto]`                                |

## Clases / Estructura HTML

```html
<!-- Ejemplo de estructura propuesta -->
<section class="seccion-servicios container py-5">
  <div class="row">
    <article class="col-12 col-md-6 col-lg-4 servicio-card">
      <!-- contenido -->
    </article>
  </div>
</section>
```

## Componentes Bootstrap usados

| Componente Bootstrap | Versión | Override SCSS         |
| -------------------- | ------- | --------------------- |
| `card`               | 5.1     | `_servicios.scss`     |
| `btn`                | 5.1     | `btn-cta-whatsapp`    |

## Variables SCSS usadas

| Variable                  | Valor       | Uso en este componente            |
| ------------------------- | ----------- | --------------------------------- |
| `$color-texto`            | `#0f1b49`   | Color de texto principal          |
| `$standard-size`          | `2em`       | Tamaño de título                  |
| `$standard-size-parrafo`  | `1.5em`     | Tamaño de párrafo                 |
| `$bg-standard`            | `#0f1b491f` | Fondo suave                       |

> Si se necesita un valor nuevo, agregarlo a `scss/_variables.scss` antes de usarlo.

## Decisiones tomadas

| Decisión                              | Alternativa descartada            | Razón                                                |
| ------------------------------------- | --------------------------------- | ---------------------------------------------------- |
| Usar Bootstrap `card`                 | Componente custom desde cero      | Bootstrap ya disponible, mantenible, responsive auto |
| WhatsApp float fijo en mobile         | Solo CTAs in-page                 | Maximiza conversión en móvil (canal principal)       |

## Responsive

| Breakpoint    | Comportamiento                                     |
| ------------- | -------------------------------------------------- |
| Mobile 375px  | `[1 columna, padding reducido]`                    |
| Tablet 768px  | `[2 columnas, padding medio]`                      |
| Desktop 1200px| `[3 columnas, padding generoso]`                   |

## Notas de accesibilidad

- `[Alt descriptivo en imágenes]`
- `[Contraste ≥ AA en texto sobre imagen — overlay si es necesario]`
- `[aria-label en botones icon-only como WhatsApp flotante]`
- `[Foco visible — no remover outline sin reemplazo]`

## Páginas que usan este componente

- [ ] `index.html`
- [ ] `nosotros.html`
- [ ] `servicios.html`
- [ ] `tarifas.html`
- [ ] `galeria.html`
- [ ] `contactanos.html`

> Si se modifica el componente, actualizar en TODAS las páginas marcadas.

<!-- TODO: Completar con decisiones reales del componente -->
