---
tipo: plantilla
dominio: functional
proyecto: Resmor Transportes
versión: 1.0
---

# Plantilla — Especificación Funcional

## Página / Flujo
`[Nombre de la página o flujo, ej: index.html, formulario-contacto, flujo-whatsapp]`

## Objetivo funcional
> ¿Qué debe lograr el usuario en esta página? ¿A qué conversión apunta (WhatsApp / tel / formulario)?

## Buyer persona principal
`[Familia mudándose / Particular con flete / Ejecutivo aeropuerto / Turista brasileño / PyME local / Dueño de mascota]`

## Flujo principal

1. El usuario llega a `[ruta]`
2. Ve `[elemento principal: hero + CTA]`
3. Puede hacer `[acción: click en WhatsApp, scroll a servicios, completar form]`
4. El sistema responde `[comportamiento esperado: abre wa.me, navega a sección, valida y envía]`

## Estados de UI

| Estado    | Trigger              | Comportamiento                              |
| --------- | -------------------- | ------------------------------------------- |
| default   | —                    | `[descripción]`                             |
| hover     | mouse sobre CTA      | `[cambio de color/sombra]`                  |
| focus     | tab por teclado      | `[outline visible]`                         |
| loading   | `[acción]`           | `[descripción — si aplica, ej: form]`       |
| success   | envío exitoso        | `[mensaje de confirmación]`                 |
| error     | validación falla     | `[mensaje de error claro]`                  |

## Validaciones

| Campo / Elemento | Regla                          | Mensaje de error                       |
| ---------------- | ------------------------------ | -------------------------------------- |
| nombre           | requerido, min 2 caracteres    | "Ingresá tu nombre"                    |
| email            | requerido, formato email       | "Ingresá un email válido"              |
| teléfono         | requerido, 10+ dígitos         | "Ingresá un teléfono válido"           |
| mensaje          | requerido, min 10 caracteres   | "Contanos brevemente qué necesitás"    |

## Edge cases

- Usuario sin conexión a internet
- Texto del usuario muy largo en formulario
- Imagen del carousel no carga
- Click en WhatsApp desde escritorio sin WhatsApp instalado
- Pantalla 320px (mobile más chico)
- Teléfonos con `+54 9 11 ...` y variantes

## Notas para desarrollo

<!-- TODO: Completar con notas específicas del flujo (qué SCSS toca, qué imágenes usa, qué CTA implementar) -->
