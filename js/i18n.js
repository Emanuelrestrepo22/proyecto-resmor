/* ═══════════════════════════════════════════════════════════════
   Resmor i18n — ES / PT / EN
   ───────────────────────────────────────────────────────────────
   Convenciones:
   - Elementos con data-i18n="key.path" → reemplaza textContent
   - Elementos con data-i18n-html="key.path" → reemplaza innerHTML
   - Elementos con data-i18n-attr="attr:key.path[,attr2:key.path2]"
       → setea atributos (placeholder, aria-label, alt, title, content...)
   - Elementos con data-i18n-wa="key" → reemplaza href de WhatsApp
       insertando el texto del diccionario wa.[key] como mensaje pre-cargado
   - Botón switcher con data-set-lang="es|pt|en"
   ─────────────────────────────────────────────────────────────── */

(function () {
    'use strict';

    const SUPPORTED = ['es', 'pt', 'en'];
    const DEFAULT_LANG = 'es';
    const STORAGE_KEY = 'resmor.lang';
    const WA_NUMBER = '5491123048846';
    const DICT_BASE = './js/i18n';

    const dictCache = {};
    let currentLang = null;
    let currentDict = null;

    /* ────────────── Helpers ────────────── */

    function detectInitialLang() {
        // 1) URL param ?lang=
        const params = new URLSearchParams(window.location.search);
        const fromUrl = params.get('lang');
        if (fromUrl && SUPPORTED.includes(fromUrl)) return fromUrl;

        // 2) localStorage
        try {
            const stored = localStorage.getItem(STORAGE_KEY);
            if (stored && SUPPORTED.includes(stored)) return stored;
        } catch (e) { /* private mode */ }

        // 3) navigator.language (pt-BR → pt, en-US → en)
        const nav = (navigator.language || navigator.userLanguage || '').slice(0, 2).toLowerCase();
        if (SUPPORTED.includes(nav)) return nav;

        return DEFAULT_LANG;
    }

    function getByPath(obj, path) {
        return path.split('.').reduce((o, k) => (o && o[k] != null ? o[k] : undefined), obj);
    }

    async function loadDict(lang) {
        if (dictCache[lang]) return dictCache[lang];
        try {
            const res = await fetch(`${DICT_BASE}/${lang}.json`, { cache: 'force-cache' });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();
            dictCache[lang] = data;
            return data;
        } catch (err) {
            console.error(`[i18n] No se pudo cargar ${lang}.json`, err);
            if (lang !== DEFAULT_LANG) return loadDict(DEFAULT_LANG);
            return {};
        }
    }

    /* ────────────── Apply translations ────────────── */

    function applyText(dict) {
        document.querySelectorAll('[data-i18n]').forEach((el) => {
            const key = el.getAttribute('data-i18n');
            const value = getByPath(dict, key);
            if (typeof value === 'string') el.textContent = value;
        });
    }

    function applyHtml(dict) {
        document.querySelectorAll('[data-i18n-html]').forEach((el) => {
            const key = el.getAttribute('data-i18n-html');
            const value = getByPath(dict, key);
            if (typeof value === 'string') el.innerHTML = value;
        });
    }

    function applyAttrs(dict) {
        document.querySelectorAll('[data-i18n-attr]').forEach((el) => {
            const raw = el.getAttribute('data-i18n-attr');
            // Formato: "placeholder:key.path,aria-label:key.path"
            raw.split(',').forEach((pair) => {
                const [attr, key] = pair.split(':').map((s) => s.trim());
                const value = getByPath(dict, key);
                if (typeof value === 'string' && attr) el.setAttribute(attr, value);
            });
        });
    }

    function applyWaLinks(dict) {
        const wa = dict.wa || {};
        document.querySelectorAll('[data-i18n-wa]').forEach((el) => {
            const key = el.getAttribute('data-i18n-wa');
            const message = wa[key] || wa.general || 'Hola Resmor';
            const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
            el.setAttribute('href', url);
        });
    }

    function applyHtmlMeta(dict) {
        const meta = dict.html || {};
        if (meta.lang) document.documentElement.setAttribute('lang', meta.lang);

        const ogLocale = document.querySelector('meta[property="og:locale"]');
        if (ogLocale && meta.ogLocale) ogLocale.setAttribute('content', meta.ogLocale);

        // Title con sufijo si el diccionario lo aporta
        const titleKey = document.documentElement.getAttribute('data-page-title-key');
        if (titleKey) {
            const value = getByPath(dict, titleKey);
            if (value) document.title = value;
        }
    }

    function updateSwitcherUI(lang) {
        document.querySelectorAll('[data-lang-switcher]').forEach((el) => {
            el.querySelectorAll('[data-set-lang]').forEach((btn) => {
                btn.classList.toggle('is-active', btn.getAttribute('data-set-lang') === lang);
                btn.setAttribute('aria-pressed', btn.getAttribute('data-set-lang') === lang ? 'true' : 'false');
            });
        });
    }

    /* ────────────── Public API ────────────── */

    async function setLang(lang, options = {}) {
        if (!SUPPORTED.includes(lang)) lang = DEFAULT_LANG;
        if (lang === currentLang && !options.force) return;

        const dict = await loadDict(lang);
        currentLang = lang;
        currentDict = dict;

        applyText(dict);
        applyHtml(dict);
        applyAttrs(dict);
        applyWaLinks(dict);
        applyHtmlMeta(dict);
        updateSwitcherUI(lang);

        try {
            if (!options.skipStorage) localStorage.setItem(STORAGE_KEY, lang);
        } catch (e) { /* private mode */ }

        document.dispatchEvent(new CustomEvent('resmor:langchange', { detail: { lang, dict } }));
    }

    function getLang() { return currentLang; }
    function getDict() { return currentDict; }
    function t(key) { return currentDict ? getByPath(currentDict, key) : undefined; }

    /* ────────────── Init ────────────── */

    function attachSwitcher() {
        document.querySelectorAll('[data-set-lang]').forEach((btn) => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const lang = btn.getAttribute('data-set-lang');
                setLang(lang);
            });
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        attachSwitcher();
        setLang(detectInitialLang(), { skipStorage: false });
    });

    window.ResmorI18n = { setLang, getLang, getDict, t, supported: SUPPORTED };
})();
