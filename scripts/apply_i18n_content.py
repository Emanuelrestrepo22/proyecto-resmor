"""
Aplica data-i18n a los heroes y bloques de contenido específicos de cada página.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Helper: hace replace literal sólo si el texto está presente
def replace_literal(txt, old, new):
    if old in txt:
        return txt.replace(old, new), True
    return txt, False


def process(page, replacements):
    p = ROOT / page
    txt = p.read_text(encoding="utf-8")
    orig = txt
    hits = 0
    for old, new in replacements:
        txt, ok = replace_literal(txt, old, new)
        if ok:
            hits += 1
    if txt != orig:
        p.write_text(txt, encoding="utf-8")
    print(f"{page}: {hits}/{len(replacements)} replacements applied")


# ─── INDEX ────────────────────────────────────────────────────────
INDEX = [
    (
        '<span class="hero__eyebrow">Buenos Aires · Desde 2018</span>',
        '<span class="hero__eyebrow" data-i18n="hero.indexEyebrow">Buenos Aires - Desde 2018</span>'
    ),
    (
        '<h1 class="hero__title">Transporte ejecutivo &amp; minifletes en Buenos Aires.</h1>',
        '<h1 class="hero__title" data-i18n="hero.indexTitle">Transporte ejecutivo &amp; minifletes en Buenos Aires.</h1>'
    ),
    (
        'Llegás a tiempo. Movemos lo que necesitás. Atendemos por WhatsApp y respondemos rápido — handyman incluido en mudanzas.',
        '<span data-i18n="hero.indexSubtitle">Llegas a tiempo. Movemos lo que necesitas. Atendemos por WhatsApp y respondemos rapido - handyman incluido en mudanzas.</span>'
    ),
    (
        '<span class="hero__subtitle-pt">Atendimento em português</span>',
        '<span class="hero__subtitle-pt" data-i18n="hero.indexSubtitlePt">Atendimento em portugues - English-speaking team</span>'
    ),
    (
        '<i class="bi bi-whatsapp"></i> Cotizar por WhatsApp\n                </a>\n                <a class="btn-cta-outline btn-cta-outline--on-dark" href="servicios.html">\n                    Ver servicios',
        '<i class="bi bi-whatsapp"></i> <span data-i18n="hero.ctaPrimary">Cotizar por WhatsApp</span>\n                </a>\n                <a class="btn-cta-outline btn-cta-outline--on-dark" href="servicios.html" data-i18n="hero.ctaSecondary">\n                    Ver servicios'
    ),
    # WhatsApp principal del hero → data-i18n-wa
    (
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener">\n                    <i class="bi bi-whatsapp"></i> <span data-i18n="hero.ctaPrimary">Cotizar por WhatsApp</span>',
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener" data-i18n-wa="general">\n                    <i class="bi bi-whatsapp"></i> <span data-i18n="hero.ctaPrimary">Cotizar por WhatsApp</span>'
    ),
    # Por qué Resmor
    (
        '<span class="eyebrow">Por qué Resmor</span>\n            <h2>Confianza con la rapidez de un WhatsApp.</h2>\n            <p>Combinamos la seriedad del transporte ejecutivo con la cercanía y disponibilidad de un servicio local. Más de seis años moviendo Buenos Aires.</p>',
        '<span class="eyebrow" data-i18n="porQue.eyebrow">Por que Resmor</span>\n            <h2 data-i18n="porQue.title">Confianza con la rapidez de un WhatsApp.</h2>\n            <p data-i18n="porQue.intro">Combinamos la seriedad del transporte ejecutivo con la cercania y disponibilidad de un servicio local. Mas de seis anos moviendo Buenos Aires.</p>'
    ),
    (
        '<h3>Transporte ejecutivo</h3>\n                <p>Conductor profesional, vehículo en orden, puntualidad asegurada.</p>',
        '<h3 data-i18n="porQue.item1Title">Transporte ejecutivo</h3>\n                <p data-i18n="porQue.item1Desc">Conductor profesional, vehiculo en orden, puntualidad asegurada.</p>'
    ),
    (
        '<h3>Handyman incluido</h3>\n                <p>En mudanzas: armado, desarmado y mano de obra. Todo coordinado.</p>',
        '<h3 data-i18n="porQue.item2Title">Handyman incluido</h3>\n                <p data-i18n="porQue.item2Desc">En mudanzas: armado, desarmado y mano de obra. Todo coordinado.</p>'
    ),
    (
        '<h3>Bilingüe ES / PT</h3>\n                <p>Atendemos en español y portugués. Atendimento em português.</p>',
        '<h3 data-i18n="porQue.item3Title">Multilenguaje ES / PT / EN</h3>\n                <p data-i18n="porQue.item3Desc">Atendemos en espanol, portugues e ingles. Pensado para expats y turistas.</p>'
    ),
    # Servicios destacados (home)
    (
        '<div class="servicios__intro">\n            <span class="eyebrow">Servicios</span>\n            <h2>Un servicio para cada necesidad.</h2>\n            <p>Desde un paquete chico hasta una mudanza completa con handyman, pasando por traslados al aeropuerto y logística para PyMEs.</p>',
        '<div class="servicios__intro">\n            <span class="eyebrow" data-i18n="servicesSection.eyebrow">Servicios</span>\n            <h2 data-i18n="servicesSection.title">Un servicio para cada necesidad.</h2>\n            <p data-i18n="servicesSection.intro">Desde un paquete chico hasta una mudanza completa con handyman, pasando por traslados al aeropuerto y logistica para PyMEs.</p>'
    ),
    (
        '<h3 class="servicio-card__title">Transporte ejecutivo</h3>\n                <p class="servicio-card__desc">Remis ejecutivo, transfer corporativo y viajes urbanos con conductor profesional.</p>\n                <a class="servicio-card__cta" href="servicios.html#ejecutivo">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.executiveTitle">Transporte ejecutivo</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.executiveDesc">Remis ejecutivo, transfer corporativo y viajes urbanos con conductor profesional.</p>\n                <a class="servicio-card__cta" href="servicios.html#ejecutivo"><span data-i18n="servicesSection.executiveCta">Conocer mas</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Traslado al aeropuerto</h3>\n                <p class="servicio-card__desc">Ezeiza y Aeroparque. Puntualidad asegurada, equipaje cuidado, atención bilingüe.</p>\n                <a class="servicio-card__cta" href="servicios.html#aeropuerto">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.airportTitle">Traslado al aeropuerto</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.airportDesc">Ezeiza y Aeroparque. Puntualidad asegurada, equipaje cuidado.</p>\n                <a class="servicio-card__cta" href="servicios.html#aeropuerto"><span data-i18n="servicesSection.airportCta">Conocer mas</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Minifletes</h3>\n                <p class="servicio-card__desc">Paquetería, muebles chicos y entregas puerta a puerta en CABA y AMBA.</p>\n                <a class="servicio-card__cta" href="servicios.html#minifletes">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.minifletesTitle">Minifletes</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.minifletesDesc">Paqueteria, muebles chicos y entregas puerta a puerta en CABA y AMBA.</p>\n                <a class="servicio-card__cta" href="servicios.html#minifletes"><span data-i18n="servicesSection.minifletesCta">Conocer mas</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Mudanzas con handyman</h3>\n                <p class="servicio-card__desc">Camión + mano de obra. Armado y desarmado de muebles incluido en la cotización.</p>\n                <a class="servicio-card__cta" href="servicios.html#mudanzas">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.mudanzasTitle">Mudanzas con handyman</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.mudanzasDesc">Camion + mano de obra. Armado y desarmado de muebles incluido en la cotizacion.</p>\n                <a class="servicio-card__cta" href="servicios.html#mudanzas"><span data-i18n="servicesSection.mudanzasCta">Conocer mas</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Logística para PyMEs</h3>\n                <p class="servicio-card__desc">Entregas recurrentes en CABA y AMBA con horario cumplido y costos previsibles.</p>\n                <a class="servicio-card__cta" href="servicios.html#logistica">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.logisticaTitle">Logistica para PyMEs</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.logisticaDesc">Entregas recurrentes en CABA y AMBA con horario cumplido y costos previsibles.</p>\n                <a class="servicio-card__cta" href="servicios.html#logistica"><span data-i18n="servicesSection.logisticaCta">Conocer mas</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Turismo & city tour</h3>\n                <p class="servicio-card__desc">Recorré Buenos Aires con guía local en español o portugués.</p>\n                <a class="servicio-card__cta" href="servicios.html#turismo">Conocer más</a>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.turismoTitle">Turismo &amp; city tour</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.turismoDesc">Recorre Buenos Aires con guia local en espanol, portugues o ingles.</p>\n                <a class="servicio-card__cta" href="servicios.html#turismo"><span data-i18n="servicesSection.turismoCta">Conocer mas</span></a>'
    ),
    # Pasos
    (
        '<span class="eyebrow">Cómo trabajamos</span>\n            <h2>Tres pasos. Sin vueltas.</h2>',
        '<span class="eyebrow" data-i18n="pasos.eyebrow">Como trabajamos</span>\n            <h2 data-i18n="pasos.title">Tres pasos. Sin vueltas.</h2>'
    ),
    (
        '<h3>Nos escribís por WhatsApp</h3>\n                <p>Contanos qué necesitás mover, desde dónde y hasta dónde.</p>',
        '<h3 data-i18n="pasos.step1Title">Nos escribis por WhatsApp</h3>\n                <p data-i18n="pasos.step1Desc">Contanos que necesitas mover, desde donde y hasta donde.</p>'
    ),
    (
        '<h3>Cotizamos en minutos</h3>\n                <p>Te respondemos con el presupuesto y la disponibilidad.</p>',
        '<h3 data-i18n="pasos.step2Title">Cotizamos en minutos</h3>\n                <p data-i18n="pasos.step2Desc">Te respondemos con el presupuesto y la disponibilidad.</p>'
    ),
    (
        '<h3>Coordinamos día y hora</h3>\n                <p>Llegamos a tiempo, hacemos el servicio y listo.</p>',
        '<h3 data-i18n="pasos.step3Title">Coordinamos dia y hora</h3>\n                <p data-i18n="pasos.step3Desc">Llegamos a tiempo, hacemos el servicio y listo.</p>'
    ),
    # CTA cierre
    (
        '<span class="eyebrow" style="color: var(--gold-light, #D4CB9B);">¿Listo?</span>\n        <h2 style="color: #fff; max-width: 22ch; margin-inline: auto;">Reservá tu próximo viaje o mudanza por WhatsApp.</h2>',
        '<span class="eyebrow" data-i18n="ctaClose.eyebrow" style="color: var(--gold-light, #D4CB9B);">Listo?</span>\n        <h2 style="color: #fff; max-width: 22ch; margin-inline: auto;" data-i18n="ctaClose.title">Reserva tu proximo viaje o mudanza por WhatsApp.</h2>'
    ),
    (
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener">\n                <i class="bi bi-whatsapp"></i> Cotizar ahora',
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener" data-i18n-wa="general">\n                <i class="bi bi-whatsapp"></i> <span data-i18n="ctaClose.primary">Cotizar ahora</span>'
    ),
    (
        '<a class="btn-cta-outline btn-cta-outline--on-dark" href="tel:+5491123048846">\n                <i class="bi bi-telephone-fill"></i> Llamar',
        '<a class="btn-cta-outline btn-cta-outline--on-dark" href="tel:+5491123048846">\n                <i class="bi bi-telephone-fill"></i> <span data-i18n="ctaClose.secondary">Llamar</span>'
    ),
]
process("index.html", INDEX)


# ─── NOSOTROS ──────────────────────────────────────────────────────
NOSOTROS = [
    (
        '<span class="hero__eyebrow">Sobre Resmor</span>\n            <h1 class="hero__title">Movemos Buenos Aires con la confianza de un servicio ejecutivo.</h1>',
        '<span class="hero__eyebrow" data-i18n="hero.aboutEyebrow">Sobre Resmor</span>\n            <h1 class="hero__title" data-i18n="hero.aboutTitle">Movemos Buenos Aires con la confianza de un servicio ejecutivo.</h1>'
    ),
    (
        '<span class="eyebrow">Quiénes somos</span>\n                <h2>Una empresa porteña con flota propia.</h2>',
        '<span class="eyebrow" data-i18n="about.introEyebrow">Quienes somos</span>\n                <h2 data-i18n="about.introTitle">Una empresa portena con flota propia.</h2>'
    ),
    (
        '<p>Desde 2018 Resmor presta servicios de <strong>transporte ejecutivo, minifletes y mudanzas con handyman</strong> en CABA y AMBA. Nuestra base está en Balvanera y nuestros vehículos identificados recorren la ciudad todos los días.</p>',
        '<p data-i18n-html="about.introP1">Desde 2018 Resmor presta servicios de <strong>transporte ejecutivo, minifletes y mudanzas con handyman</strong> en CABA y AMBA. Nuestra base esta en Balvanera y nuestros vehiculos identificados recorren la ciudad todos los dias.</p>'
    ),
    (
        '<p>Trabajamos con una premisa simple: que mover cosas — o personas — deje de ser un problema. Coordinamos por WhatsApp, llegamos a horario y cuidamos lo que llevamos. Atendemos en español y portugués para clientes brasileños que llegan o se mueven por Buenos Aires.</p>',
        '<p data-i18n="about.introP2">Trabajamos con una premisa simple: que mover cosas - o personas - deje de ser un problema. Coordinamos por WhatsApp, llegamos a horario y cuidamos lo que llevamos. Atendemos en espanol, portugues e ingles.</p>'
    ),
    (
        '<i class="bi bi-whatsapp"></i> Hablemos por WhatsApp',
        '<i class="bi bi-whatsapp"></i> <span data-i18n="about.introCta">Hablemos por WhatsApp</span>'
    ),
    (
        '<span class="eyebrow">Valores</span>\n            <h2>Atributos que nos definen.</h2>\n            <p>Los colores y la tipografía de nuestra marca traducen lo que somos.</p>',
        '<span class="eyebrow" data-i18n="about.valuesEyebrow">Valores</span>\n            <h2 data-i18n="about.valuesTitle">Atributos que nos definen.</h2>\n            <p data-i18n="about.valuesIntro">Los colores y la tipografia de nuestra marca traducen lo que somos.</p>'
    ),
    (
        '<h3>Confianza</h3>\n                <p>Amabilidad, simpatía y seguridad. Hacemos lo que decimos y cuidamos lo que movemos.</p>',
        '<h3 data-i18n="about.value1Title">Confianza</h3>\n                <p data-i18n="about.value1Desc">Amabilidad, simpatia y seguridad. Hacemos lo que decimos y cuidamos lo que movemos.</p>'
    ),
    (
        '<h3>Distinción</h3>\n                <p>Servicio ejecutivo con detalle: vehículo en orden, conductor profesional, atención cuidada.</p>',
        '<h3 data-i18n="about.value2Title">Distincion</h3>\n                <p data-i18n="about.value2Desc">Servicio ejecutivo con detalle: vehiculo en orden, conductor profesional, atencion cuidada.</p>'
    ),
    (
        '<h3>Modernidad</h3>\n                <p>Coordinamos por WhatsApp y respondemos rápido. Sin trámites innecesarios.</p>',
        '<h3 data-i18n="about.value3Title">Modernidad</h3>\n                <p data-i18n="about.value3Desc">Coordinamos por WhatsApp y respondemos rapido. Sin tramites innecesarios.</p>'
    ),
    (
        '<h3>Cercanía</h3>\n                <p>Empresa local, atención directa, sin intermediarios. Bilingüe ES/PT.</p>',
        '<h3 data-i18n="about.value4Title">Multilenguaje</h3>\n                <p data-i18n="about.value4Desc">Empresa local, atencion directa, sin intermediarios. ES / PT / EN.</p>'
    ),
    (
        '<span class="eyebrow">Flota</span>\n                <h2>Vehículos identificados, mantenidos y disponibles.</h2>',
        '<span class="eyebrow" data-i18n="about.fleetEyebrow">Flota</span>\n                <h2 data-i18n="about.fleetTitle">Vehiculos identificados, mantenidos y disponibles.</h2>'
    ),
    (
        '<p><strong>Renault Kangoo blanca</strong> — para minifletes, paquetería y mudanzas chicas. Capacidad para muebles medianos, electrodomésticos y cargas puerta a puerta.</p>',
        '<p data-i18n-html="about.fleetP1"><strong>Renault Kangoo blanca</strong> - para minifletes, paqueteria y mudanzas chicas. Capacidad para muebles medianos, electrodomesticos y cargas puerta a puerta.</p>'
    ),
    (
        '<p><strong>Mercedes Vito</strong> — para transporte ejecutivo, traslados al aeropuerto, grupos y equipaje. Confort, espacio y aire acondicionado.</p>',
        '<p data-i18n-html="about.fleetP2"><strong>Mercedes Vito</strong> - para transporte ejecutivo, traslados al aeropuerto, grupos y equipaje. Confort, espacio y aire acondicionado.</p>'
    ),
    (
        '<p>Todos nuestros vehículos llevan el logo de Resmor a la vista. Vas a saber siempre quién te está retirando o recibiendo.</p>',
        '<p data-i18n="about.fleetP3">Todos nuestros vehiculos llevan el logo de Resmor a la vista. Vas a saber siempre quien te esta retirando o recibiendo.</p>'
    ),
    (
        '<span class="eyebrow">Dónde estamos</span>\n                <h2>Base operativa en Balvanera, CABA.</h2>\n                <p>Nuestra oficina está en pleno centro de Buenos Aires. Cubrimos toda la Ciudad Autónoma de Buenos Aires y el conurbano bonaerense.</p>',
        '<span class="eyebrow" data-i18n="about.locationEyebrow">Donde estamos</span>\n                <h2 data-i18n="about.locationTitle">Base operativa en Balvanera, CABA.</h2>\n                <p data-i18n="about.locationDesc">Nuestra oficina esta en pleno centro de Buenos Aires. Cubrimos toda la Ciudad Autonoma de Buenos Aires y el conurbano bonaerense.</p>'
    ),
]
process("nosotros.html", NOSOTROS)


# ─── SERVICIOS ──────────────────────────────────────────────────────
SERVICIOS = [
    (
        '<span class="hero__eyebrow">Servicios</span>\n            <h1 class="hero__title">Un servicio para cada necesidad.</h1>\n            <p class="hero__subtitle">Desde un paquete chico hasta tu mudanza completa con handyman. Atendemos por WhatsApp.</p>',
        '<span class="hero__eyebrow" data-i18n="hero.servicesEyebrow">Servicios</span>\n            <h1 class="hero__title" data-i18n="hero.servicesTitle">Un servicio para cada necesidad.</h1>\n            <p class="hero__subtitle" data-i18n="hero.servicesSubtitle">Desde un paquete chico hasta tu mudanza completa con handyman. Atendemos por WhatsApp.</p>'
    ),
    # Cada card de servicio
    (
        '<h3 class="servicio-card__title">Transporte ejecutivo</h3>\n                <p class="servicio-card__desc">Remis ejecutivo, transfer corporativo y viajes urbanos con conductor profesional y vehículo en orden.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.executiveTitle">Transporte ejecutivo</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.executiveDesc">Remis ejecutivo, transfer corporativo y viajes urbanos con conductor profesional y vehiculo en orden.</p>'
    ),
    (
        '<li>Conductor profesional</li>\n                    <li>Vehículo identificado y mantenido</li>\n                    <li>Puntualidad asegurada</li>\n                    <li>Pago en efectivo o transferencia</li>',
        '<li data-i18n="servicesSection.executiveFeat1">Conductor profesional</li>\n                    <li data-i18n="servicesSection.executiveFeat2">Vehiculo identificado y mantenido</li>\n                    <li data-i18n="servicesSection.executiveFeat3">Puntualidad asegurada</li>\n                    <li data-i18n="servicesSection.executiveFeat4">Pago en efectivo o transferencia</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20transporte%20ejecutivo" target="_blank" rel="noopener">Reservar</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20transporte%20ejecutivo" target="_blank" rel="noopener" data-i18n-wa="executive"><span data-i18n="servicesSection.executiveCta">Reservar</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Traslado al aeropuerto</h3>\n                <p class="servicio-card__desc">Ezeiza y Aeroparque. Puntualidad asegurada, equipaje cuidado y atención bilingüe ES/PT.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.airportTitle">Traslado al aeropuerto</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.airportDesc">Ezeiza y Aeroparque. Puntualidad asegurada, equipaje cuidado y atencion multilingue.</p>'
    ),
    (
        '<li>Ezeiza · Aeroparque</li>\n                    <li>Atendimento em português</li>\n                    <li>Espera incluida</li>\n                    <li>Tarifa cerrada por viaje</li>',
        '<li data-i18n="servicesSection.airportFeat1">Ezeiza - Aeroparque</li>\n                    <li data-i18n="servicesSection.airportFeat2">Atencion en ES / PT / EN</li>\n                    <li data-i18n="servicesSection.airportFeat3">Espera incluida</li>\n                    <li data-i18n="servicesSection.airportFeat4">Tarifa cerrada por viaje</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20traslado%20al%20aeropuerto" target="_blank" rel="noopener">Reservar traslado</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20traslado%20al%20aeropuerto" target="_blank" rel="noopener" data-i18n-wa="airport"><span data-i18n="servicesSection.airportCta">Reservar traslado</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Minifletes</h3>\n                <p class="servicio-card__desc">Paquetería, muebles chicos, entregas puerta a puerta en CABA y AMBA. Levantamos hoy, entregamos hoy.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.minifletesTitle">Minifletes</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.minifletesDesc">Paqueteria, muebles chicos, entregas puerta a puerta en CABA y AMBA. Levantamos hoy, entregamos hoy.</p>'
    ),
    (
        '<li>CABA &amp; AMBA</li>\n                    <li>Puerta a puerta</li>\n                    <li>Ayuda para cargar y descargar</li>\n                    <li>Cotización rápida por WhatsApp</li>',
        '<li data-i18n="servicesSection.minifletesFeat1">CABA &amp; AMBA</li>\n                    <li data-i18n="servicesSection.minifletesFeat2">Puerta a puerta</li>\n                    <li data-i18n="servicesSection.minifletesFeat3">Ayuda para cargar y descargar</li>\n                    <li data-i18n="servicesSection.minifletesFeat4">Cotizacion rapida por WhatsApp</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20un%20mini-flete" target="_blank" rel="noopener">Cotizar flete</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20un%20mini-flete" target="_blank" rel="noopener" data-i18n-wa="minifletes"><span data-i18n="servicesSection.minifletesCta">Cotizar flete</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Mudanzas con handyman</h3>\n                <p class="servicio-card__desc">Camión + mano de obra. Armado y desarmado de muebles incluido en la cotización.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.mudanzasTitle">Mudanzas con handyman</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.mudanzasDesc">Camion + mano de obra. Armado y desarmado de muebles incluido en la cotizacion.</p>'
    ),
    (
        '<li>Camión adecuado al volumen</li>\n                    <li>Handyman incluido (armado/desarmado)</li>\n                    <li>Embalaje básico</li>\n                    <li>CABA &amp; AMBA</li>',
        '<li data-i18n="servicesSection.mudanzasFeat1">Camion adecuado al volumen</li>\n                    <li data-i18n="servicesSection.mudanzasFeat2">Handyman incluido</li>\n                    <li data-i18n="servicesSection.mudanzasFeat3">Embalaje basico</li>\n                    <li data-i18n="servicesSection.mudanzasFeat4">CABA &amp; AMBA</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20cotizar%20una%20mudanza" target="_blank" rel="noopener">Cotizar mudanza</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20cotizar%20una%20mudanza" target="_blank" rel="noopener" data-i18n-wa="mudanzas"><span data-i18n="servicesSection.mudanzasCta">Cotizar mudanza</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Logística para PyMEs</h3>\n                <p class="servicio-card__desc">Entregas recurrentes en CABA y AMBA con horario cumplido y costos previsibles.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.logisticaTitle">Logistica para PyMEs</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.logisticaDesc">Entregas recurrentes en CABA y AMBA con horario cumplido y costos previsibles.</p>'
    ),
    (
        '<li>Rutas diarias o semanales</li>\n                    <li>Costo previsible</li>\n                    <li>Reportes simples por WhatsApp</li>\n                    <li>Facturación A o B</li>',
        '<li data-i18n="servicesSection.logisticaFeat1">Rutas diarias o semanales</li>\n                    <li data-i18n="servicesSection.logisticaFeat2">Costo previsible</li>\n                    <li data-i18n="servicesSection.logisticaFeat3">Reportes simples por WhatsApp</li>\n                    <li data-i18n="servicesSection.logisticaFeat4">Facturacion A o B</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20log%C3%ADstica%20recurrente%20para%20mi%20negocio" target="_blank" rel="noopener">Pedir propuesta</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Necesito%20log%C3%ADstica%20recurrente%20para%20mi%20negocio" target="_blank" rel="noopener" data-i18n-wa="logistica"><span data-i18n="servicesSection.logisticaCta">Pedir propuesta</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Turismo &amp; city tour</h3>\n                <p class="servicio-card__desc">Recorré Buenos Aires con guía local en español o portugués. Itinerarios personalizados.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.turismoTitle">Turismo &amp; city tour</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.turismoDesc">Recorre Buenos Aires con guia local en espanol, portugues o ingles. Itinerarios personalizados.</p>'
    ),
    (
        '<li>Atendimento em português</li>\n                    <li>Itinerario personalizable</li>\n                    <li>Hasta 4 pasajeros + equipaje</li>\n                    <li>Pickup desde hotel</li>',
        '<li data-i18n="servicesSection.turismoFeat1">Atencion multilingue ES / PT / EN</li>\n                    <li data-i18n="servicesSection.turismoFeat2">Itinerario personalizable</li>\n                    <li data-i18n="servicesSection.turismoFeat3">Hasta 4 pasajeros + equipaje</li>\n                    <li data-i18n="servicesSection.turismoFeat4">Pickup desde hotel</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20info%20de%20city%20tour" target="_blank" rel="noopener">Consultar tour</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20info%20de%20city%20tour" target="_blank" rel="noopener" data-i18n-wa="turismo"><span data-i18n="servicesSection.turismoCta">Consultar tour</span></a>'
    ),
    (
        '<h3 class="servicio-card__title">Transporte pet-friendly</h3>\n                <p class="servicio-card__desc">Tu mascota viaja segura y cómoda. Ideal para mudanzas, veterinario o viajes largos.</p>',
        '<h3 class="servicio-card__title" data-i18n="servicesSection.petTitle">Transporte pet-friendly</h3>\n                <p class="servicio-card__desc" data-i18n="servicesSection.petDesc">Tu mascota viaja segura y comoda. Ideal para mudanzas, veterinario o viajes largos.</p>'
    ),
    (
        '<li>Vehículo adecuado para mascotas</li>\n                    <li>Recorrido tranquilo</li>\n                    <li>Coordinación con veterinario si aplica</li>',
        '<li data-i18n="servicesSection.petFeat1">Vehiculo adecuado para mascotas</li>\n                    <li data-i18n="servicesSection.petFeat2">Recorrido tranquilo</li>\n                    <li data-i18n="servicesSection.petFeat3">Coordinacion con veterinario si aplica</li>'
    ),
    (
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20transportar%20a%20mi%20mascota" target="_blank" rel="noopener">Consultar</a>',
        '<a class="servicio-card__cta" href="https://wa.me/5491123048846?text=Quiero%20transportar%20a%20mi%20mascota" target="_blank" rel="noopener" data-i18n-wa="pet"><span data-i18n="servicesSection.petCta">Consultar</span></a>'
    ),
]
process("servicios.html", SERVICIOS)


# ─── TARIFAS ──────────────────────────────────────────────────────
TARIFAS = [
    (
        '<span class="hero__eyebrow">Tarifas</span>\n            <h1 class="hero__title">Cotización personalizada por WhatsApp.</h1>\n            <p class="hero__subtitle">Cada viaje y mudanza es distinto. Te respondemos en minutos con el presupuesto.</p>',
        '<span class="hero__eyebrow" data-i18n="hero.pricingEyebrow">Tarifas</span>\n            <h1 class="hero__title" data-i18n="hero.pricingTitle">Cotizacion personalizada por WhatsApp.</h1>\n            <p class="hero__subtitle" data-i18n="hero.pricingSubtitle">Cada viaje y mudanza es distinto. Te respondemos en minutos con el presupuesto.</p>'
    ),
    (
        '<span class="eyebrow">Cómo cotizamos</span>\n            <h2>Qué define el precio.</h2>\n            <p>No publicamos precios cerrados porque cada servicio depende de variables concretas. Sí podemos cotizarte en pocos minutos.</p>',
        '<span class="eyebrow" data-i18n="pricing.factorsEyebrow">Como cotizamos</span>\n            <h2 data-i18n="pricing.factorsTitle">Que define el precio.</h2>\n            <p data-i18n="pricing.factorsIntro">No publicamos precios cerrados porque cada servicio depende de variables concretas. Si podemos cotizarte en pocos minutos.</p>'
    ),
    (
        '<h3>Distancia</h3>\n                <p>Punto de origen y destino. CABA, AMBA, conurbano o ruta provincial.</p>',
        '<h3 data-i18n="pricing.factor1Title">Distancia</h3>\n                <p data-i18n="pricing.factor1Desc">Punto de origen y destino. CABA, AMBA, conurbano o ruta provincial.</p>'
    ),
    (
        '<h3>Tipo de carga</h3>\n                <p>Volumen, peso, fragilidad, cantidad de pasajeros y equipaje.</p>',
        '<h3 data-i18n="pricing.factor2Title">Tipo de carga</h3>\n                <p data-i18n="pricing.factor2Desc">Volumen, peso, fragilidad, cantidad de pasajeros y equipaje.</p>'
    ),
    (
        '<h3>Handyman</h3>\n                <p>Si la mudanza requiere armado/desarmado o ayuda extra de mano de obra.</p>',
        '<h3 data-i18n="pricing.factor3Title">Handyman</h3>\n                <p data-i18n="pricing.factor3Desc">Si la mudanza requiere armado/desarmado o ayuda extra de mano de obra.</p>'
    ),
    (
        '<h3>Horario y día</h3>\n                <p>Días hábiles, fines de semana o feriados. Horario diurno o nocturno.</p>',
        '<h3 data-i18n="pricing.factor4Title">Horario y dia</h3>\n                <p data-i18n="pricing.factor4Desc">Dias habiles, fines de semana o feriados. Horario diurno o nocturno.</p>'
    ),
    (
        '<span class="eyebrow">Pedir cotización</span>\n            <h2>Tres pasos. Respuesta en minutos.</h2>',
        '<span class="eyebrow" data-i18n="pricing.stepsEyebrow">Pedir cotizacion</span>\n            <h2 data-i18n="pricing.stepsTitle">Tres pasos. Respuesta en minutos.</h2>'
    ),
    (
        '<h3>Nos escribís</h3>\n                <p>WhatsApp o formulario de contacto. Contanos qué necesitás mover y desde dónde.</p>',
        '<h3 data-i18n="pricing.stepsStep1Title">Nos escribis</h3>\n                <p data-i18n="pricing.stepsStep1Desc">WhatsApp o formulario de contacto. Contanos que necesitas mover y desde donde.</p>'
    ),
    (
        '<h3>Cotizamos</h3>\n                <p>Te respondemos con el presupuesto y la disponibilidad — en general el mismo día.</p>',
        '<h3 data-i18n="pricing.stepsStep2Title">Cotizamos</h3>\n                <p data-i18n="pricing.stepsStep2Desc">Te respondemos con el presupuesto y la disponibilidad - en general el mismo dia.</p>'
    ),
    (
        '<h3>Coordinamos</h3>\n                <p>Si te sirve, agendamos día y hora. Llegamos a tiempo.</p>',
        '<h3 data-i18n="pricing.stepsStep3Title">Coordinamos</h3>\n                <p data-i18n="pricing.stepsStep3Desc">Si te sirve, agendamos dia y hora. Llegamos a tiempo.</p>'
    ),
    (
        '<span class="eyebrow">Pago</span>\n                <h2>Métodos de pago aceptados.</h2>',
        '<span class="eyebrow" data-i18n="pricing.paymentEyebrow">Pago</span>\n                <h2 data-i18n="pricing.paymentTitle">Metodos de pago aceptados.</h2>'
    ),
    (
        '<li>Efectivo (ARS)</li>\n                    <li>Transferencia bancaria</li>\n                    <li>Mercado Pago</li>\n                    <li>Facturación A o B para PyMEs (logística recurrente)</li>',
        '<li data-i18n="pricing.paymentFeat1">Efectivo (ARS)</li>\n                    <li data-i18n="pricing.paymentFeat2">Transferencia bancaria</li>\n                    <li data-i18n="pricing.paymentFeat3">Mercado Pago</li>\n                    <li data-i18n="pricing.paymentFeat4">Facturacion A o B para PyMEs (logistica recurrente)</li>'
    ),
    (
        '<i class="bi bi-whatsapp"></i> Pedir mi cotización',
        '<i class="bi bi-whatsapp"></i> <span data-i18n="pricing.paymentCta">Pedir mi cotizacion</span>'
    ),
]
process("tarifas.html", TARIFAS)


# ─── GALERIA ──────────────────────────────────────────────────────
GALERIA = [
    (
        '<span class="hero__eyebrow">Galería</span>\n            <h1 class="hero__title">Mirá nuestro trabajo.</h1>\n            <p class="hero__subtitle">Algunos de los servicios que hicimos en Buenos Aires.</p>',
        '<span class="hero__eyebrow" data-i18n="hero.galleryEyebrow">Galeria</span>\n            <h1 class="hero__title" data-i18n="hero.galleryTitle">Mira nuestro trabajo.</h1>\n            <p class="hero__subtitle" data-i18n="hero.gallerySubtitle">Algunos de los servicios que hicimos en Buenos Aires.</p>'
    ),
    (
        '<span class="eyebrow" style="color: #D4CB9B;">¿Querés ser parte?</span>\n        <h2 style="color:#fff; max-width: 22ch; margin-inline: auto;">Cotizá tu próxima mudanza o flete.</h2>',
        '<span class="eyebrow" data-i18n="gallery.ctaEyebrow" style="color: #D4CB9B;">Queres ser parte?</span>\n        <h2 style="color:#fff; max-width: 22ch; margin-inline: auto;" data-i18n="gallery.ctaTitle">Cotiza tu proxima mudanza o flete.</h2>'
    ),
    (
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener">\n                <i class="bi bi-whatsapp"></i> Cotizar por WhatsApp',
        '<a class="btn-cta-whatsapp" href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener" data-i18n-wa="general">\n                <i class="bi bi-whatsapp"></i> <span data-i18n="gallery.ctaPrimary">Cotizar por WhatsApp</span>'
    ),
    (
        '<a class="btn-cta-outline btn-cta-outline--on-dark" href="servicios.html">\n                Ver servicios',
        '<a class="btn-cta-outline btn-cta-outline--on-dark" href="servicios.html">\n                <span data-i18n="gallery.ctaSecondary">Ver servicios</span>'
    ),
]
process("galeria.html", GALERIA)


# ─── CONTACTANOS ─────────────────────────────────────────────────
CONTACTANOS = [
    (
        '<span class="hero__eyebrow">Contacto</span>\n            <h1 class="hero__title">Escribinos. Te respondemos rápido.</h1>',
        '<span class="hero__eyebrow" data-i18n="hero.contactEyebrow">Contacto</span>\n            <h1 class="hero__title" data-i18n="hero.contactTitle">Escribinos. Te respondemos rapido.</h1>'
    ),
    (
        '<p class="hero__subtitle">\n                Atendemos por WhatsApp, teléfono o este formulario.',
        '<p class="hero__subtitle" data-i18n-html="hero.contactSubtitle">\n                Atendemos por WhatsApp, telefono o este formulario.'
    ),
    (
        '<span class="eyebrow">Cómo llegarnos</span>\n                <h2>Tres formas de contactarnos.</h2>',
        '<span class="eyebrow" data-i18n="contact.infoEyebrow">Como llegarnos</span>\n                <h2 data-i18n="contact.infoTitle">Tres formas de contactarnos.</h2>'
    ),
    (
        '<p>El canal más rápido es WhatsApp — solemos responder en minutos durante horario laboral. Si preferís, dejá tu consulta en el formulario y te contactamos a vuelta.</p>',
        '<p data-i18n="contact.infoDesc">El canal mas rapido es WhatsApp - solemos responder en minutos. Si preferis, deja tu consulta en el formulario y abrimos WhatsApp con el mensaje listo.</p>'
    ),
    (
        '<span class="channel-label">WhatsApp · El más rápido</span>',
        '<span class="channel-label" data-i18n="contact.channelWhatsappLabel">WhatsApp - El mas rapido</span>'
    ),
    (
        '<span class="channel-label">Teléfono</span>\n                            <a href="tel:+5491123048846">(+54) 11 2304-8846</a>',
        '<span class="channel-label" data-i18n="contact.channelPhoneLabel">Telefono</span>\n                            <a href="tel:+5491123048846">(+54) 11 2304-8846</a>'
    ),
    (
        '<span class="channel-label">Dirección</span>\n                            <span class="contacto__meta">Viamonte 2450, Balvanera, CABA</span>',
        '<span class="channel-label" data-i18n="contact.channelAddressLabel">Direccion</span>\n                            <span class="contacto__meta" data-i18n="footer.contactAddressValue">Viamonte 2450, Balvanera, CABA</span>'
    ),
    (
        '<span class="channel-label">Horario</span>\n                            <span class="contacto__meta">Atención 24 hs · todos los días</span>',
        '<span class="channel-label" data-i18n="contact.channelHoursLabel">Horario</span>\n                            <span class="contacto__meta" data-i18n="contact.channelHoursValue">Atencion 24 hs - todos los dias</span>'
    ),
    (
        '<h2 class="form-resmor__title">Pedí tu cotización</h2>\n                <p class="form-resmor__subtitle">Completá datos básicos y abrimos WhatsApp con mensaje listo para enviar.</p>',
        '<h2 class="form-resmor__title" data-i18n="contact.formTitle">Pedi tu cotizacion</h2>\n                <p class="form-resmor__subtitle" data-i18n="contact.formSubtitle">Completa datos basicos y abrimos WhatsApp con mensaje listo para enviar.</p>'
    ),
    (
        '<label for="nombre">Nombre y apellido</label>\n                    <input type="text" id="nombre" name="nombre" class="form-control" placeholder="Tu nombre" required>',
        '<label for="nombre" data-i18n="contact.formNameLabel">Nombre y apellido</label>\n                    <input type="text" id="nombre" name="nombre" class="form-control" placeholder="Tu nombre" data-i18n-attr="placeholder:contact.formNamePlaceholder" required>'
    ),
    (
        '<label for="email">Email (opcional)</label>\n                    <input type="email" id="email" name="email" class="form-control" placeholder="tu@email.com">',
        '<label for="email" data-i18n="contact.formEmailLabel">Email (opcional)</label>\n                    <input type="email" id="email" name="email" class="form-control" placeholder="tu@email.com" data-i18n-attr="placeholder:contact.formEmailPlaceholder">'
    ),
    (
        '<label for="telefono">Teléfono / WhatsApp</label>\n                    <input type="tel" id="telefono" name="telefono" class="form-control" placeholder="+54 9 11 ..." required>',
        '<label for="telefono" data-i18n="contact.formPhoneLabel">Telefono / WhatsApp</label>\n                    <input type="tel" id="telefono" name="telefono" class="form-control" placeholder="+54 9 11 ..." data-i18n-attr="placeholder:contact.formPhonePlaceholder" required>'
    ),
    (
        '<label for="servicio">Servicio que necesitás</label>',
        '<label for="servicio" data-i18n="contact.formServiceLabel">Servicio que necesitas</label>'
    ),
    (
        '<option value="" disabled selected>Elegí un servicio</option>',
        '<option value="" disabled selected data-i18n="contact.formServicePlaceholder">Elegi un servicio</option>'
    ),
    (
        '<option value="transporte-ejecutivo">Transporte ejecutivo</option>',
        '<option value="transporte-ejecutivo" data-i18n="contact.formServiceExecutive">Transporte ejecutivo</option>'
    ),
    (
        '<option value="aeropuerto">Traslado al aeropuerto</option>',
        '<option value="aeropuerto" data-i18n="contact.formServiceAirport">Traslado al aeropuerto</option>'
    ),
    (
        '<option value="minifletes">Minifletes</option>',
        '<option value="minifletes" data-i18n="contact.formServiceMinifletes">Minifletes</option>'
    ),
    (
        '<option value="mudanzas">Mudanzas con handyman</option>',
        '<option value="mudanzas" data-i18n="contact.formServiceMudanzas">Mudanzas con handyman</option>'
    ),
    (
        '<option value="logistica">Logística para PyMEs</option>',
        '<option value="logistica" data-i18n="contact.formServiceLogistica">Logistica para PyMEs</option>'
    ),
    (
        '<option value="turismo">Turismo / city tour</option>',
        '<option value="turismo" data-i18n="contact.formServiceTurismo">Turismo / city tour</option>'
    ),
    (
        '<option value="pet">Transporte pet-friendly</option>',
        '<option value="pet" data-i18n="contact.formServicePet">Transporte pet-friendly</option>'
    ),
    (
        '<option value="otro">Otro</option>',
        '<option value="otro" data-i18n="contact.formServiceOther">Otro</option>'
    ),
    (
        '<label for="mensaje">Contanos qué necesitás</label>\n                    <textarea id="mensaje" name="mensaje" class="form-control" rows="4" placeholder="Origen, destino, fecha aproximada, observaciones..." required></textarea>',
        '<label for="mensaje" data-i18n="contact.formMessageLabel">Contanos que necesitas</label>\n                    <textarea id="mensaje" name="mensaje" class="form-control" rows="4" placeholder="Origen, destino, fecha aproximada, observaciones..." data-i18n-attr="placeholder:contact.formMessagePlaceholder" required></textarea>'
    ),
    (
        '<i class="bi bi-send"></i> Enviar mensaje',
        '<i class="bi bi-send"></i> <span data-i18n="contact.formSubmit">Enviar mensaje</span>'
    ),
    (
        '<p class="form-note">O escribinos directamente por <a href="https://wa.me/5491123048846?text=Hola%20Resmor%2C%20quiero%20cotizar" target="_blank" rel="noopener">WhatsApp</a> — el canal más rápido.</p>',
        '<p class="form-note" data-i18n-html="contact.formNote">O escribinos directamente por <a href="https://wa.me/5491123048846" target="_blank" rel="noopener">WhatsApp</a> - el canal mas rapido.</p>'
    ),
]
process("contactanos.html", CONTACTANOS)

print("\nAll pages processed.")
