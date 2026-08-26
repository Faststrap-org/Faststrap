/**
 * FastStrap MkDocs Interactive Embed Bridge.
 * Synchronizes iframe auto-height and MkDocs/Bootstrap theme transitions.
 */
(function () {
  // Listen for iframe height adjustments to eliminate scrollbars
  window.addEventListener('message', function (e) {
    if (e.data && e.data.type === 'fs-iframe-height' && e.data.height) {
      document.querySelectorAll('iframe[data-faststrap-preview]').forEach(function (iframe) {
        if (iframe.contentWindow === e.source) {
          iframe.style.height = (e.data.height + 10) + 'px';
        }
      });
    }
  });

  // Sync theme changes to embedded FastStrap iframes
  function notifyIframesTheme(newTheme) {
    document.querySelectorAll('iframe[data-faststrap-preview]').forEach(function (iframe) {
      if (iframe.contentWindow) {
        iframe.contentWindow.postMessage({ type: 'fs-set-theme', theme: newTheme }, '*');
      }
    });
  }

  // Observe MkDocs Material theme palette switches (body[data-md-color-scheme])
  var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.type === 'attributes') {
        var bodyScheme = document.body.getAttribute('data-md-color-scheme');
        var bsTheme = document.documentElement.getAttribute('data-bs-theme');
        
        var theme = (bodyScheme === 'slate' || bsTheme === 'dark') ? 'dark' : 'light';
        notifyIframesTheme(theme);
      }
    });
  });

  if (document.body) {
    observer.observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
  }
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-bs-theme'] });
})();
