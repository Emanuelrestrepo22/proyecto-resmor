/* ═══════════════════════════════════════════════════════════════
   Resmor — Analytics
   ───────────────────────────────────────────────────────────────
   GA4 via gtag.js + custom event tracking.

   IMPORTANTE: reemplazar G-XXXXXXXXXX por el Measurement ID real
   cuando se cree la propiedad de Google Analytics 4.

   Eventos custom emitidos:
   - lang_change       { from, to }
   - cta_click         { service, channel: 'whatsapp'|'phone'|'form', source }
   - form_submit       { service, language }
   ─────────────────────────────────────────────────────────────── */

(function () {
    'use strict';

    const GA_ID = window.RESMOR_GA_ID || 'G-XXXXXXXXXX';
    const IS_PLACEHOLDER = GA_ID === 'G-XXXXXXXXXX';

    // ────────────── Cargar gtag.js si hay ID real ──────────────
    if (!IS_PLACEHOLDER) {
        const s = document.createElement('script');
        s.async = true;
        s.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
        document.head.appendChild(s);

        window.dataLayer = window.dataLayer || [];
        window.gtag = function () { dataLayer.push(arguments); };
        gtag('js', new Date());
        gtag('config', GA_ID, {
            anonymize_ip: true,
            send_page_view: true
        });
    } else {
        // Stub de gtag para no romper el código si no hay GA real configurado todavía
        window.dataLayer = window.dataLayer || [];
        window.gtag = function () {
            dataLayer.push(arguments);
            if (window.RESMOR_GA_DEBUG) {
                console.log('[analytics:stub]', ...arguments);
            }
        };
    }

    const track = (eventName, params = {}) => {
        try {
            window.gtag('event', eventName, params);
        } catch (e) {
            console.warn('[analytics] track failed', e);
        }
    };

    // ────────────── Helpers ──────────────
    const getCurrentLang = () => {
        if (window.ResmorI18n && typeof ResmorI18n.getLang === 'function') {
            return ResmorI18n.getLang() || 'es';
        }
        return document.documentElement.getAttribute('lang') || 'es';
    };

    const getServiceFromWaKey = (el) => {
        return el.getAttribute('data-i18n-wa') || 'unknown';
    };

    // ────────────── Listener: cambio de idioma ──────────────
    let lastLang = getCurrentLang();
    document.addEventListener('resmor:langchange', (e) => {
        const newLang = e.detail && e.detail.lang ? e.detail.lang : 'es';
        if (newLang !== lastLang) {
            track('lang_change', { from: lastLang, to: newLang });
            lastLang = newLang;
        }
    });

    // ────────────── Listener: clicks en WhatsApp (CTAs) ──────────────
    document.addEventListener('click', (e) => {
        const anchor = e.target.closest('a[href*="wa.me/"]');
        if (anchor) {
            const service = anchor.getAttribute('data-i18n-wa') || 'general';
            const isFloat = anchor.classList.contains('whatsapp-float');
            track('cta_click', {
                channel: 'whatsapp',
                service: service,
                source: isFloat ? 'whatsapp_float' : (anchor.classList.contains('servicio-card__cta') ? 'service_card' : 'inline'),
                language: getCurrentLang(),
                page_location: window.location.pathname
            });
            return;
        }

        const telAnchor = e.target.closest('a[href^="tel:"]');
        if (telAnchor) {
            track('cta_click', {
                channel: 'phone',
                source: 'tel_link',
                language: getCurrentLang(),
                page_location: window.location.pathname
            });
        }
    }, { capture: true });

    // ────────────── Listener: form submit ──────────────
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', () => {
            const fd = new FormData(contactForm);
            track('form_submit', {
                service: String(fd.get('servicio') || 'unknown'),
                language: getCurrentLang(),
                page_location: window.location.pathname
            });
        }, { capture: true });
    }

    // Exponer API mínima para testing manual
    window.ResmorAnalytics = { track, getCurrentLang };
})();
