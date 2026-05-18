/* ═══════════════════════════════════════════════════════════════
   Resmor — Lógica UI + formulario a WhatsApp
   ═══════════════════════════════════════════════════════════════ */

(function () {
    'use strict';

    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    const navbar = document.getElementById('menu__nav');
    if (navbar) {
        const onScroll = () => {
            navbar.classList.toggle('is-scrolled', window.scrollY > 8);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    const navLinks = document.querySelectorAll('.navbar-resmor .nav-link');
    const navCollapse = document.getElementById('navbarMain');
    if (navCollapse && window.bootstrap) {
        const bsCollapse = bootstrap.Collapse.getInstance(navCollapse) || new bootstrap.Collapse(navCollapse, { toggle: false });
        navLinks.forEach((link) => {
            link.addEventListener('click', () => {
                if (navCollapse.classList.contains('show')) {
                    bsCollapse.hide();
                }
            });
        });
    }

    const contactForm = document.getElementById('contactForm');
    const formStatus = document.getElementById('formStatus');

    if (contactForm) {
        const setStatus = (message, state = 'info') => {
            if (!formStatus) return;
            formStatus.textContent = message;
            formStatus.dataset.state = state;
        };

        // Lee la etiqueta del servicio desde el <option> seleccionado (ya está traducido por i18n.js)
        const serviceLabelFromOption = (form, value) => {
            const opt = form.querySelector(`option[value="${value}"]`);
            return opt ? opt.textContent.trim() : value;
        };

        // Wrapper i18n con fallback al español
        const t = (key, fallback) => {
            if (window.ResmorI18n && typeof ResmorI18n.t === 'function') {
                const value = ResmorI18n.t(`wa.${key}`);
                if (typeof value === 'string') return value;
            }
            return fallback;
        };

        contactForm.addEventListener('submit', (event) => {
            event.preventDefault();

            if (!contactForm.checkValidity()) {
                contactForm.reportValidity();
                setStatus(t('formErrorIncomplete', 'Completá los campos obligatorios antes de seguir.'), 'error');
                return;
            }

            const data = new FormData(contactForm);
            const whatsapp = contactForm.dataset.whatsapp || '5491123048846';

            const servicio = String(data.get('servicio') || '').trim();
            const serviceLabel = servicio
                ? serviceLabelFromOption(contactForm, servicio)
                : t('formServiceNone', 'No indicado');

            const lines = [
                t('formIntro', 'Hola Resmor, quiero pedir una cotización.'),
                '',
                `${t('formName', 'Nombre')}: ${String(data.get('nombre') || '').trim()}`,
                `${t('formService', 'Servicio')}: ${serviceLabel}`,
                `${t('formPhone', 'Teléfono')}: ${String(data.get('telefono') || '').trim()}`
            ];

            const email = String(data.get('email') || '').trim();
            if (email) lines.push(`${t('formEmail', 'Email')}: ${email}`);

            lines.push('', `${t('formDetail', 'Detalle')}:`, String(data.get('mensaje') || '').trim());

            const url = `https://wa.me/${whatsapp}?text=${encodeURIComponent(lines.join('\n'))}`;
            setStatus(t('formOpening', 'Abriendo WhatsApp con mensaje listo para enviar…'), 'success');
            window.open(url, '_blank', 'noopener');
        });
    }
})();
