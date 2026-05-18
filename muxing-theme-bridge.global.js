(() => {
  const THEMES = new Set(["light","dark","nature","stellar"]);
  const STORAGE_KEY = "muxing-theme";
  const BRIDGE_VERSION = 1;
  const html = document.documentElement;

  const normalize = (value) => {
    if (!value || value === 'light') return '';
    return THEMES.has(value) ? value : '';
  };

  const persist = () => {
    const activeTheme = html.getAttribute('data-theme') || 'light';
    localStorage.setItem(STORAGE_KEY, activeTheme);
  };

  const apply = (value) => {
    const normalized = normalize(value);
    if (normalized) {
      html.setAttribute('data-theme', normalized);
    } else {
      html.removeAttribute('data-theme');
    }
    persist();
  };

  const isSupportedVersion = (version) => version == null || version === BRIDGE_VERSION;

  const params = new URLSearchParams(window.location.search);
  const queryTheme = params.get('muxing-theme') || params.get('theme');
  const storedTheme = localStorage.getItem(STORAGE_KEY);
  apply(THEMES.has(queryTheme) ? queryTheme : storedTheme);

  new MutationObserver(persist).observe(html, {
    attributes: true,
    attributeFilter: ['data-theme'],
  });

  window.addEventListener('message', (event) => {
    const data = event.data;
    if (
      !data ||
      data.source !== 'muxing-workbench' ||
      data.type !== 'muxing:set-theme' ||
      !isSupportedVersion(data.version)
    ) {
      return;
    }
    apply(data.theme);
  });
})();
