# PROJECT_BRIEF — Resmor Transportes

**Última actualización:** 2026-05-17
**Mantenido por:** AGT-03 Documentation
**Estado:** Borrador inicial — algunos puntos marcados como **supuesto** deben validarse con el dueño del negocio.

---

## 1. Empresa

**Nombre:** Resmor Transportes
**Rubro:** Transporte, mudanzas, logística local
**Ubicación operativa:** Buenos Aires, Argentina — CABA y AMBA <!-- supuesto: confirmar radio exacto de cobertura -->
**Tamaño:** PyME local <!-- supuesto: confirmar cantidad de empleados/vehículos -->
**Idiomas operativos:** Español (principal) + Portugués (clientes brasileños)

---

## 2. Servicios

| Servicio                       | Descripción                                                                | Diferenciador clave                            |
| ------------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------- |
| Minifletes / Fletes            | Entrega puerta a puerta de paquetes, muebles chicos, compras de Marketplace | Disponibilidad rápida en CABA/AMBA             |
| Mudanzas con handyman          | Camión + mano de obra para armado/desarmado de muebles                     | **Handyman incluido** — no solo transporte    |
| Traslado al aeropuerto         | Transfer a Ezeiza y Aeroparque                                             | Puntualidad, equipaje, atención bilingüe       |
| Remis / transfer ejecutivo     | Servicio de remis para empresa, viajes urbanos                             | Conductor profesional, vehículo en buen estado |
| Logística de entregas          | Entregas recurrentes para PyMEs locales                                    | Confiabilidad y costos previsibles             |
| Turismo / city tour            | Recorridos turísticos por Buenos Aires                                     | Atención en portugués para brasileños          |
| Transporte pet-friendly        | Traslado de mascotas                                                       | Pocos competidores ofrecen este servicio       |

> **Nota:** todos los servicios deben confirmarse con el dueño del negocio antes de comunicarse como oferta activa.

---

## 3. Audiencias

| Persona                       | Servicio principal       | Canal de descubrimiento típico       | Trigger de contacto                  |
| ----------------------------- | ------------------------ | ------------------------------------ | ------------------------------------ |
| Familia mudándose             | Mudanza con handyman     | Google, recomendación, redes sociales | Mudanza programada                  |
| Particular con flete chico    | Mini-flete               | Google, Marketplace                  | Compra/venta de mueble, mudanza chica |
| Ejecutivo / viajero           | Aeropuerto               | Google, hotel, recomendación          | Vuelo en agenda                      |
| Turista brasileño             | Aeropuerto + city tour   | Google PT, agencia de viajes         | Llegada a Buenos Aires               |
| PyME local                    | Logística recurrente     | Boca a boca, networking              | Necesidad operativa                  |
| Dueño de mascota              | Pet-friendly             | Google, comunidad de mascotas        | Mudanza o viaje al veterinario       |

---

## 4. Objetivos del sitio web

1. **Generar leads por WhatsApp** — canal principal del negocio.
2. **Comunicar los diferenciadores reales** (handyman incluido, bilingüe ES/PT, cobertura puerta a puerta).
3. **Generar confianza** mediante fotos reales, prueba social y claridad de servicios.
4. **Ser accesible en móvil** — el tráfico real probable viene de búsquedas locales en móvil.
5. **Permitir contacto rápido** — WhatsApp / llamada / formulario, en orden de prioridad.

---

## 5. Métricas de éxito (sugeridas)

| Métrica                                       | Cómo medirla                                  | Objetivo inicial         |
| --------------------------------------------- | --------------------------------------------- | ------------------------ |
| Clicks en WhatsApp flotante                   | Evento Google Analytics o Tag Manager          | Aumento mes a mes        |
| Mensajes recibidos por WhatsApp via web       | Conteo manual o automation                    | Linea base + 20%         |
| Formularios completados                       | Backend del formulario (cuando exista)        | Linea base + 20%         |
| Tasa de rebote en mobile                      | Google Analytics                              | < 60%                    |
| Velocidad de carga LCP en mobile              | PageSpeed Insights                            | < 2.5s                   |

> **Nota:** instrumentar Google Analytics / Tag Manager es una tarea pendiente.

---

## 6. Stack técnico

| Categoría     | Tecnología                                            |
| ------------- | ----------------------------------------------------- |
| Markup        | HTML5 semántico                                       |
| CSS framework | Bootstrap 5.1.2 (vía CDN)                             |
| Iconos        | Bootstrap Icons 1.5.0 (vía CDN)                       |
| Estilos       | SCSS modular en `/scss` compilado a `/css/estilo.css` |
| Build         | `npm run build-css` / `npm run watch-css` (node-sass) |
| JS            | Vanilla (`main.js`) + Bootstrap bundle JS (CDN)       |
| Deploy        | GitHub Pages                                          |
| Repo          | github.com/Emanuelrestrepo22/proyecto-resmor          |

---

## 7. Páginas del sitio

| Página                | Propósito                                          | Estado actual           |
| --------------------- | -------------------------------------------------- | ----------------------- |
| `index.html`          | Home — hero + servicios destacados + CTA           | Existente               |
| `nosotros.html`       | Quiénes somos + valores + equipo                   | Existente               |
| `servicios.html`      | Detalle por servicio                               | Existente               |
| `tarifas.html`        | Tarifas (cuando se confirmen)                      | Existente — sin datos validados |
| `galeria.html`        | Fotos reales de trabajos                           | Existente               |
| `contactanos.html`    | Formulario + WhatsApp + tel + ubicación            | Existente               |

---

## 8. Contacto

- **WhatsApp:** [wa.me/5491123048846](https://wa.me/5491123048846) — `(+54) 9 11 2304-8846`
- **Email:** <!-- supuesto: confirmar email oficial -->
- **Dirección física:** <!-- supuesto: confirmar dirección -->
- **Horarios de atención:** 24 hs · todos los días

---

## 9. Supuestos abiertos (a validar con el dueño del negocio)

- [ ] Radio exacto de cobertura (CABA, AMBA, GBA Norte/Sur/Oeste)
- [ ] Lista oficial de servicios activos (¿pet-friendly y turismo siguen vigentes?)
- [ ] Tarifas mínimas o referencias por servicio
- [ ] Tiempo de respuesta promedio en WhatsApp
- [ ] Años de experiencia / cantidad de mudanzas hechas (para usar como prueba social)
- [ ] Si hay equipo o es operación uniperonal
- [ ] Si tiene testimonios reales utilizables
- [ ] Email oficial de contacto
- [ ] Dirección física (si tiene depósito visible)
- [ ] Necesidad real de copy en portugués (¿qué % del cliente es brasileño?)

---

## 10. Roadmap (sugerido)

| Fase | Objetivo                                                                     | Estado    |
| ---- | ---------------------------------------------------------------------------- | --------- |
| 1    | Validar y completar este brief con el dueño del negocio                      | Pendiente |
| 2    | Definir `BRAND_RULES.md` con paleta, tipografía y CTAs aprobados             | Pendiente |
| 3    | Reescribir copy de cada página con AGT-01 (Marketing)                        | Pendiente |
| 4    | Auditar y mejorar UI con AGT-02 (UX/Frontend) — consistencia + responsive    | Pendiente |
| 5    | QA pre-deploy con AGT-04 (Functional QA)                                     | Pendiente |
| 6    | Instrumentar analytics y trackear clicks en WhatsApp                         | Pendiente |
| 7    | (Opcional) Sumar copy en portugués en páginas clave                          | Pendiente |
