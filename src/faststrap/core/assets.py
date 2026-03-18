"""
FastStrap - Production Bootstrap Asset Manager
Safe for multi-worker servers, thread-safe, with graceful fallbacks.
"""

from __future__ import annotations

import os
import sys
import warnings
from importlib import metadata as importlib_metadata
from os import environ
from pathlib import Path
from typing import Any
from urllib.parse import quote

from fasthtml.common import Link, Script, Style
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from ..utils.static_management import (
    create_favicon_links,
    get_default_favicon_url,
    get_static_path,
    resolve_static_url,
)
from .theme import ModeType, Theme, get_builtin_theme

# Bootstrap versions
BOOTSTRAP_VERSION = "5.3.3"
BOOTSTRAP_ICONS_VERSION = "1.11.3"

# Asset URLs (Extracted for formatting stability)
BOOTSTRAP_CSS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css"
)
BOOTSTRAP_ICONS_URL = f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/bootstrap-icons.min.css"
BOOTSTRAP_JS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js"
)

BOOTSTRAP_CSS_INTEGRITY = "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
BOOTSTRAP_JS_INTEGRITY = "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
# Bootstrap Icons docs currently do not publish an official SRI hash for this asset.
BOOTSTRAP_ICONS_INTEGRITY: str | None = None

# When new CSS files are added to src/faststrap/static/css/, add them here.
FASTSTRAP_CDN_CSS_FILES = [
    "css/faststrap-fx.css",
    "css/faststrap-layouts.css",
]

# CDN assets with SRI hashes
CDN_ASSETS = (
    Link(
        rel="stylesheet",
        href=BOOTSTRAP_CSS_URL,
        integrity=BOOTSTRAP_CSS_INTEGRITY,
        crossorigin="anonymous",
    ),
    Link(
        rel="stylesheet",
        href=BOOTSTRAP_ICONS_URL,
    ),
    Script(
        src=BOOTSTRAP_JS_URL,
        integrity=BOOTSTRAP_JS_INTEGRITY,
        crossorigin="anonymous",
        defer=True,
    ),
)


def local_assets(static_url: str, *, include_js: bool = True) -> tuple[Any, ...]:
    """Generate local asset links for the given static URL."""
    base = static_url.rstrip("/")
    assets: list[Any] = [
        Link(rel="stylesheet", href=f"{base}/css/bootstrap.min.css"),
        Link(rel="stylesheet", href=f"{base}/css/bootstrap-icons.min.css"),
        Link(rel="stylesheet", href=f"{base}/css/faststrap-fx.css"),
        Link(rel="stylesheet", href=f"{base}/css/faststrap-layouts.css"),
    ]
    if include_js:
        assets.append(Script(src=f"{base}/js/bootstrap.bundle.min.js"))
    return tuple(assets)


def _get_faststrap_cdn_version() -> str:
    """Read installed package version for CDN pinning, fallback to main in editable/dev."""
    try:
        return importlib_metadata.version("faststrap")
    except importlib_metadata.PackageNotFoundError:
        return "main"


def _build_cdn_assets(
    version: str,
    include_favicon: bool,
    *,
    include_js: bool = True,
) -> list[Any]:
    """Build complete CDN assets list for use_cdn mode."""
    if version == "main":
        ref = "main"
    elif version.startswith("v"):
        ref = version
    else:
        ref = f"v{version}"
    static_base = f"https://cdn.jsdelivr.net/gh/Faststrap-org/Faststrap@{ref}/src/faststrap/static"
    assets: list[Any] = [
        Link(
            rel="stylesheet",
            href=BOOTSTRAP_CSS_URL,
            integrity=BOOTSTRAP_CSS_INTEGRITY,
            crossorigin="anonymous",
        ),
    ]

    icons_link: dict[str, Any] = {"rel": "stylesheet", "href": BOOTSTRAP_ICONS_URL}
    if BOOTSTRAP_ICONS_INTEGRITY:
        icons_link["integrity"] = BOOTSTRAP_ICONS_INTEGRITY
        icons_link["crossorigin"] = "anonymous"
    assets.append(Link(**icons_link))

    for css_path in FASTSTRAP_CDN_CSS_FILES:
        assets.append(Link(rel="stylesheet", href=f"{static_base}/{css_path}"))

    if include_js:
        assets.append(
            Script(
                src=BOOTSTRAP_JS_URL,
                integrity=BOOTSTRAP_JS_INTEGRITY,
                crossorigin="anonymous",
                defer=True,
            )
        )

    if include_favicon:
        assets.append(Link(rel="icon", type="image/svg+xml", href=f"{static_base}/favicon.svg"))

    return assets


# Custom FastStrap enhancements
CUSTOM_STYLES_CSS = """
:root {
  --fs-shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --fs-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
  --fs-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --fs-transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.shadow-sm { box-shadow: var(--fs-shadow-sm) !important; }
.shadow { box-shadow: var(--fs-shadow) !important; }
.shadow-lg { box-shadow: var(--fs-shadow-lg) !important; }

.btn { transition: var(--fs-transition); }
.btn:hover:not(:disabled) { transform: translateY(-1px); box-shadow: var(--fs-shadow); }
.btn:active:not(:disabled) { transform: translateY(0); }

[data-bs-theme="dark"] { transition: background-color 0.3s, color 0.3s; }

/* Simple Toast animations (no JavaScript required) */
@keyframes toastFadeOut {
  0% { opacity: 1; transform: translateX(0); }
  100% { opacity: 0; transform: translateX(100%); }
}

.toast-fade-out {
  animation: toastFadeOut 0.5s ease-in-out forwards;
}
"""

CUSTOM_STYLES = Style(CUSTOM_STYLES_CSS)

# Automatic initialization for Tooltips and Popovers (supports HTMX)
INIT_SCRIPT_JS = """
    document.addEventListener('DOMContentLoaded', () => {
        const initBS = (scope) => {
            if (!window.bootstrap) return;
            // Tooltips
            scope.querySelectorAll('[data-bs-toggle="tooltip"]')
                 .forEach(el => new bootstrap.Tooltip(el));
            // Popovers
            scope.querySelectorAll('[data-bs-toggle="popover"]')
                 .forEach(el => new bootstrap.Popover(el));
        };

        const initToggleGroups = (scope) => {
            scope.querySelectorAll('[data-fs-toggle-group="true"]').forEach(group => {
                if (group.dataset.fsToggleInit === 'true') return;
                group.dataset.fsToggleInit = 'true';

                const activeClass = group.dataset.fsActiveClass || 'active';
                const inputId = group.dataset.fsInputId;
                const hiddenInput = inputId ? document.getElementById(inputId) : null;

                const setActive = (btn) => {
                    group.querySelectorAll('[data-fs-toggle-item="true"]').forEach(item => {
                        item.classList.remove(activeClass);
                        item.setAttribute('aria-pressed', 'false');
                        item.setAttribute('aria-current', 'false');
                    });
                    btn.classList.add(activeClass);
                    btn.setAttribute('aria-pressed', 'true');
                    btn.setAttribute('aria-current', 'true');
                    if (hiddenInput) hiddenInput.value = btn.dataset.fsValue || '';
                };

                group.querySelectorAll('[data-fs-toggle-item="true"]').forEach(btn => {
                    btn.addEventListener('click', () => setActive(btn));
                });
            });
        };

        const initTextClamp = (scope) => {
            scope.querySelectorAll('[data-fs-text-clamp="true"]').forEach(container => {
                if (container.dataset.fsTextClampInit === 'true') return;
                container.dataset.fsTextClampInit = 'true';

                const btn = container.querySelector('[data-fs-text-toggle="true"]');
                const preview = container.querySelector('[data-fs-preview="true"]');
                const full = container.querySelector('[data-fs-full="true"]');
                if (!btn || !preview || !full) return;

                const expandLabel = btn.dataset.fsExpandLabel || 'Show more';
                const collapseLabel = btn.dataset.fsCollapseLabel || 'Show less';
                let expanded = false;

                btn.addEventListener('click', () => {
                    expanded = !expanded;
                    preview.classList.toggle('d-none', expanded);
                    full.classList.toggle('d-none', !expanded);
                    btn.textContent = expanded ? collapseLabel : expandLabel;
                    btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
                });
            });
        };

        const initFocusTraps = (scope) => {
            const FOCUSABLE =
                'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';
            const focusTrapStates = window.__fsFocusTrapStates || new WeakMap();
            window.__fsFocusTrapStates = focusTrapStates;

            const isVisible = (node) => {
                if (!(node instanceof HTMLElement)) return false;
                const style = window.getComputedStyle(node);
                return style.display !== 'none'
                    && style.visibility !== 'hidden'
                    && node.getClientRects().length > 0;
            };

            const getFocusable = (container) => {
                return Array.from(container.querySelectorAll(FOCUSABLE))
                    .filter(node => isVisible(node));
            };

            const activateFocusTrap = (container) => {
                if (!isVisible(container)) return;

                const focusables = getFocusable(container);
                if (focusables.length === 0) return;

                const existing = focusTrapStates.get(container);
                if (existing && existing.active) return;

                const previous = document.activeElement instanceof HTMLElement
                    ? document.activeElement
                    : null;
                const first = focusables[0];
                const last = focusables[focusables.length - 1];

                const handler = (e) => {
                    if (e.key !== 'Tab') return;

                    const currentFocusables = getFocusable(container);
                    if (currentFocusables.length === 0) return;

                    const currentFirst = currentFocusables[0];
                    const currentLast = currentFocusables[currentFocusables.length - 1];

                    if (e.shiftKey && document.activeElement === currentFirst) {
                        e.preventDefault();
                        currentLast.focus();
                    } else if (!e.shiftKey && document.activeElement === currentLast) {
                        e.preventDefault();
                        currentFirst.focus();
                    }
                };

                container.addEventListener('keydown', handler);
                focusTrapStates.set(container, { active: true, handler, previous });

                const autofocusSelector = container.dataset.fsAutofocus;
                if (autofocusSelector) {
                    const target = container.querySelector(autofocusSelector);
                    if (isVisible(target)) {
                        target.focus();
                        return;
                    }
                }

                first.focus();
            };

            const deactivateFocusTrap = (container) => {
                const state = focusTrapStates.get(container);
                if (!state || !state.active) return;

                container.removeEventListener('keydown', state.handler);
                state.active = false;
                focusTrapStates.set(container, state);

                if (state.previous && document.body.contains(state.previous)) {
                    state.previous.focus();
                }
            };

            scope.querySelectorAll('[data-fs-focus-trap="true"]').forEach(container => {
                if (container.dataset.fsFocusTrapInit === 'true') return;
                container.dataset.fsFocusTrapInit = 'true';

                const owner = container.closest('.modal, .offcanvas') || container;
                const ownerIsModal = owner.classList.contains('modal');
                const ownerIsOffcanvas = owner.classList.contains('offcanvas');

                if (ownerIsModal) {
                    owner.addEventListener('shown.bs.modal', () => activateFocusTrap(container));
                    owner.addEventListener('hidden.bs.modal', () => deactivateFocusTrap(container));
                    if (owner.classList.contains('show')) {
                        activateFocusTrap(container);
                    }
                    return;
                }

                if (ownerIsOffcanvas) {
                    owner.addEventListener('shown.bs.offcanvas', () => activateFocusTrap(container));
                    owner.addEventListener('hidden.bs.offcanvas', () => deactivateFocusTrap(container));
                    if (owner.classList.contains('show')) {
                        activateFocusTrap(container);
                    }
                    return;
                }

                activateFocusTrap(container);
            });
        };

        const initSearchableSelect = (scope) => {
            scope.querySelectorAll('[data-fs-searchable-select="true"]').forEach(container => {
                if (container.dataset.fsSearchableInit === 'true') return;
                container.dataset.fsSearchableInit = 'true';

                container.addEventListener('click', (e) => {
                    const option = e.target.closest('[data-fs-searchable-option="true"]');
                    if (!option || !container.contains(option)) return;
                    e.preventDefault();

                    const selectId = option.dataset.fsSelectId;
                    const inputId = option.dataset.fsInputId;
                    const resultsId = option.dataset.fsResultsId;
                    if (!selectId) return;

                    const hiddenSelect = document.getElementById(selectId);
                    if (!hiddenSelect) return;

                    const value = option.dataset.fsValue || '';
                    const label = option.dataset.fsLabel || option.textContent || '';

                    hiddenSelect.innerHTML = '';
                    const selectedOption = document.createElement('option');
                    selectedOption.value = value;
                    selectedOption.text = label;
                    selectedOption.selected = true;
                    hiddenSelect.appendChild(selectedOption);

                    if (inputId) {
                        const input = document.getElementById(inputId);
                        if (input) input.value = label;
                    }
                    if (resultsId) {
                        const results = document.getElementById(resultsId);
                        if (results) results.innerHTML = '';
                    }
                });
            });
        };

        const initDateRangePresets = (scope) => {
            scope.querySelectorAll('[data-fs-date-range="true"]').forEach(form => {
                if (form.dataset.fsDateRangeInit === 'true') return;
                form.dataset.fsDateRangeInit = 'true';

                form.addEventListener('click', (e) => {
                    const button = e.target.closest('[data-fs-date-preset="true"]');
                    if (!button || !form.contains(button)) return;

                    e.preventDefault();

                    const startName = button.dataset.fsDateStartName;
                    const endName = button.dataset.fsDateEndName;
                    const startValue = button.dataset.fsDateStart || '';
                    const endValue = button.dataset.fsDateEnd || '';

                    const startInput = startName ? form.elements.namedItem(startName) : null;
                    const endInput = endName ? form.elements.namedItem(endName) : null;

                    if (startInput) startInput.value = startValue;
                    if (endInput) endInput.value = endValue;

                    if (button.dataset.fsDatePresetSubmit === 'true') {
                        if (typeof form.requestSubmit === 'function') {
                            form.requestSubmit();
                        } else {
                            form.submit();
                        }
                    }
                });
            });
        };

        const initInfiniteScroll = (scope) => {
            scope.querySelectorAll('[data-fs-infinite-scroll="true"]').forEach(el => {
                if (el.dataset.fsInfiniteInit === 'true') return;
                el.dataset.fsInfiniteInit = 'true';

                const margin = el.dataset.fsInfiniteMargin || '0px';
                if (!('IntersectionObserver' in window) || !window.htmx) {
                    return;
                }

                const observer = new IntersectionObserver((entries) => {
                    entries.forEach((entry) => {
                        if (!entry.isIntersecting) return;
                        window.htmx.trigger(el, 'faststrap:infinite-scroll');
                        observer.disconnect();
                    });
                }, {
                    root: null,
                    rootMargin: `0px 0px ${margin} 0px`,
                    threshold: 0,
                });

                observer.observe(el);

                const cleanup = new MutationObserver(() => {
                    if (!document.body.contains(el)) {
                        observer.disconnect();
                        cleanup.disconnect();
                    }
                });
                cleanup.observe(document.body, { childList: true, subtree: true });
            });
        };

        const initSseTargets = (scope) => {
            scope.querySelectorAll('[data-fs-sse="true"]').forEach(el => {
                if (el.dataset.fsSseInit === 'true') return;
                el.dataset.fsSseInit = 'true';

                if (!window.EventSource) return;

                const endpoint = el.dataset.fsSseEndpoint;
                if (!endpoint) return;

                const eventName = el.dataset.fsSseEvent || 'message';
                const swap = el.dataset.fsSseSwap || 'inner';
                const targetSelector = el.dataset.fsSseTarget;
                const withCredentials = el.dataset.fsSseCredentials === 'true';
                const reconnect = el.dataset.fsSseReconnect !== 'false';
                const retryRaw = el.dataset.fsSseRetry;
                const retry = retryRaw ? parseInt(retryRaw, 10) : null;

                let connectionRoot = el;
                let target = el;
                if (targetSelector) {
                    const candidate = document.querySelector(targetSelector);
                    if (candidate) target = candidate;
                }

                const toFragment = (html) => {
                    const template = document.createElement('template');
                    template.innerHTML = html;
                    return template.content;
                };

                const applySwap = (html) => {
                    if (targetSelector && !document.body.contains(target)) {
                        const candidate = document.querySelector(targetSelector);
                        if (candidate) target = candidate;
                    }

                    switch (swap) {
                        case 'outer':
                        case 'replace':
                            {
                                const parent = target.parentNode;
                                if (!parent) return;

                                const marker = document.createElement('span');
                                marker.hidden = true;
                                marker.setAttribute('data-fs-sse-marker', 'true');
                                parent.insertBefore(marker, target);
                                target.remove();
                                marker.insertAdjacentHTML('afterend', html);
                                const replacement = marker.nextElementSibling;
                                marker.remove();

                                if (!replacement) {
                                    if (source) source.close();
                                    if (observer) observer.disconnect();
                                    return;
                                }

                                const replacedConnectionRoot = target === connectionRoot;
                                target = replacement;
                                if (replacedConnectionRoot) {
                                    connectionRoot = replacement;
                                }
                            }
                            break;
                        case 'before':
                            target.insertAdjacentHTML('beforebegin', html);
                            break;
                        case 'after':
                            target.insertAdjacentHTML('afterend', html);
                            break;
                        case 'append':
                            target.insertAdjacentHTML('beforeend', html);
                            break;
                        case 'prepend':
                            target.insertAdjacentHTML('afterbegin', html);
                            break;
                        default:
                            target.innerHTML = html;
                    }
                };
                const handler = (evt) => {
                    const data = evt.data ?? '';
                    if (swap === 'text') {
                        target.textContent = data;
                        return;
                    }
                    applySwap(data);
                };

                let source = null;
                let reconnectTimer = null;
                let observer = null;

                const connect = () => {
                    if (!document.body.contains(connectionRoot)) return;
                    source = new EventSource(endpoint, { withCredentials });
                    source.addEventListener(eventName, handler);
                    source.onerror = () => {
                        if (!reconnect) {
                            source.close();
                            source = null;
                            return;
                        }

                        if (retry !== null && Number.isFinite(retry)) {
                            source.close();
                            source = null;
                            if (reconnectTimer) {
                                window.clearTimeout(reconnectTimer);
                            }
                            reconnectTimer = window.setTimeout(() => {
                                reconnectTimer = null;
                                connect();
                            }, retry);
                        }
                    };
                };

                connect();

                observer = new MutationObserver(() => {
                    if (!document.body.contains(connectionRoot)) {
                        if (source) {
                            source.close();
                            source = null;
                        }
                        if (reconnectTimer) {
                            window.clearTimeout(reconnectTimer);
                            reconnectTimer = null;
                        }
                        observer.disconnect();
                    }
                });
                observer.observe(document.body, { childList: true, subtree: true });
            });
        };

        const initMermaid = (scope) => {
            if (!window.mermaid) return;

            const nodes = Array.from(scope.querySelectorAll('[data-fs-mermaid="true"]'))
                .filter(el => el.dataset.fsMermaidInit !== 'true');
            if (nodes.length === 0) return;

            if (!window.__fsMermaidInit) {
                const first = nodes[0];
                const config = { startOnLoad: false };
                const theme = first.dataset.fsMermaidTheme;
                const security = first.dataset.fsMermaidSecurity;
                if (theme) config.theme = theme;
                if (security) config.securityLevel = security;
                try {
                    window.mermaid.initialize(config);
                } catch (e) {
                    return;
                }
                window.__fsMermaidInit = true;
            }

            try {
                if (window.mermaid.run) {
                    window.mermaid.run({ nodes });
                } else if (window.mermaid.init) {
                    window.mermaid.init(undefined, nodes);
                }
            } catch (e) {
                return;
            }

            nodes.forEach(el => {
                el.dataset.fsMermaidInit = 'true';
            });
        };

        initBS(document);
        initToggleGroups(document);
        initTextClamp(document);
        initFocusTraps(document);
        initSearchableSelect(document);
        initDateRangePresets(document);
        initInfiniteScroll(document);
        initSseTargets(document);
        initMermaid(document);

        // HTMX support: Re-initialize on content swap
        document.body.addEventListener('htmx:afterSwap', (evt) => {
            initBS(evt.detail.elt);
            initToggleGroups(evt.detail.elt);
            initTextClamp(evt.detail.elt);
            initFocusTraps(evt.detail.elt);
            initSearchableSelect(evt.detail.elt);
            initDateRangePresets(evt.detail.elt);
            initInfiniteScroll(evt.detail.elt);
            initSseTargets(evt.detail.elt);
            initMermaid(evt.detail.elt);
        });
    });
"""

INIT_SCRIPT = Script(INIT_SCRIPT_JS)


def get_assets(
    use_cdn: bool | None = None,
    include_custom: bool = True,
    static_url: str | None = None,
    theme: str | Theme | None = None,
    mode: ModeType = "light",
    font_family: str | None = None,
    font_weights: list[int] | None = None,
    include_js: bool = True,
    include_favicon: bool = False,
) -> tuple[Any, ...]:
    """
    Get Bootstrap assets for injection.

    Args:
        use_cdn: Use CDN (True) or local files (False)
        include_custom: Include FastStrap custom styles
        static_url: Custom static URL (if using local assets)
        theme: Theme name (str) or Theme instance
        mode: Color mode - "light", "dark", or "auto"
        font_family: Google Font name (e.g., "Inter", "Roboto", "Poppins")
        font_weights: Font weights to load (default: [400, 500, 700])
        include_js: Include Bootstrap JavaScript bundle
        include_favicon: Include default Faststrap favicon (CDN mode only)

    Returns:
        Tuple of FastHTML elements for app.hdrs
    """
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"

    if use_cdn:
        assets = tuple(
            _build_cdn_assets(
                _get_faststrap_cdn_version(),
                include_favicon=include_favicon,
                include_js=include_js,
            )
        )
    else:
        actual_static_url = static_url if static_url is not None else "/static"
        assets = local_assets(actual_static_url, include_js=include_js)

    elements = list(assets)

    # Add Google Fonts link if specified (BEFORE other styles for proper loading)
    if font_family:
        weights = font_weights or [400, 500, 700]
        weights_str = ";".join(str(w) for w in weights)
        # Properly encode font family name for URL (handles spaces and special characters)
        encoded_family = quote(font_family)
        font_url = f"https://fonts.googleapis.com/css2?family={encoded_family}:wght@{weights_str}&display=swap"
        # Add preconnect for performance
        elements.insert(0, Link(rel="preconnect", href="https://fonts.googleapis.com"))
        elements.insert(
            1, Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True)
        )
        elements.insert(2, Link(rel="stylesheet", href=font_url))

    if include_custom:
        elements.append(CUSTOM_STYLES)
        elements.append(INIT_SCRIPT)

    # Add theme styles
    if theme is not None:
        if isinstance(theme, str):
            theme_obj = get_builtin_theme(theme)
        elif isinstance(theme, Theme):
            theme_obj = theme
        else:
            raise ValueError("theme must be a string (theme name) or Theme instance")
        elements.append(theme_obj.to_style(mode=mode))

    # Add font-family CSS if font specified (AFTER theme so it can override)
    if font_family:
        font_css = Style(
            f":root {{ --bs-body-font-family: '{font_family}', sans-serif; }} "
            f"body {{ font-family: var(--bs-body-font-family); }}"
        )
        elements.append(font_css)

    return tuple(elements)


def _any_requires_js(components: list[Any]) -> bool:
    """Check component registry metadata for JS requirement."""
    for comp in components:
        meta = getattr(comp, "__faststrap_metadata__", None)
        if meta and meta.get("requires_js", False):
            return True
    return False


def add_bootstrap(
    app: Any,
    theme: str | Theme | None = None,
    mode: ModeType = "light",
    use_cdn: bool | None = None,
    mount_static: bool = True,
    static_url: str = "/static",
    force_static_url: bool = False,
    include_favicon: bool = True,
    favicon_url: str | None = None,
    font_family: str | None = None,
    font_weights: list[int] | None = None,
    components: list[Any] | None = None,
) -> Any:
    """Enhance FastHTML app with Bootstrap and FastStrap assets.

    Args:
        app: FastHTML application instance
        theme: Color theme - either a built-in name (e.g., "green-nature", "purple-magic"),
               a Theme instance created via create_theme(), or a community theme
        mode: Color mode for light/dark backgrounds:
              - "light": Light background, dark text (default)
              - "dark": Dark background, light text
              - "auto": Follows user's system preference (prefers-color-scheme)
        use_cdn: When True, ALL assets (Bootstrap CSS/JS, Bootstrap Icons,
                 Faststrap CSS files, favicon) are served from CDN. No local
                 StaticFiles are mounted. Required for serverless deployments
                 (Vercel, AWS Lambda, Google Cloud Run). Default: False.
        mount_static: Auto-mount static directory
        static_url: Preferred URL prefix for static files
        force_static_url: Force use of this URL even if already mounted
        include_favicon: Include default FastStrap favicon
        favicon_url: Custom favicon URL (overrides default)
        font_family: Google Font name (e.g., "Inter", "Roboto", "Poppins")
        font_weights: Font weights to load (default: [400, 500, 700])
        components: Optional list of Faststrap component functions used in the app.
            When provided, Bootstrap JS is only injected if at least one
            component has requires_js=True in its registry metadata.
            Components without @register() metadata are treated as
            requires_js=False. When None (default), JS is always injected.

    Returns:
        Modified app instance

    Example:
        # Basic setup with light mode
        add_bootstrap(app)

        # Dark mode with a color theme
        add_bootstrap(app, theme="purple-magic", mode="dark")

        # Auto mode (follows system preference)
        add_bootstrap(app, theme="green-nature", mode="auto")

        # Custom theme with dark mode
        from faststrap import create_theme
        my_theme = create_theme(primary="#7BA05B", secondary="#48C774")
        add_bootstrap(app, theme=my_theme, mode="dark")

        # Built-in theme with custom font
        add_bootstrap(app, theme="green-nature", font_family="Inter")

        # Custom theme with custom font
        my_theme = create_theme(primary="#7BA05B")
        add_bootstrap(app, theme=my_theme, font_family="Roboto", font_weights=[400, 600, 700])

        # Font only, no theme
        add_bootstrap(app, font_family="Poppins")

        # CDN mode for production
        add_bootstrap(app, theme="blue-ocean", mode="auto", use_cdn=True)
    """
    if getattr(app, "_faststrap_bootstrap_added", False):
        raise RuntimeError(
            "add_bootstrap() has already been called on this app. "
            "It should only be called once during app setup. "
            "If you are using fast_app(), call add_bootstrap() after "
            "fast_app() returns the app object."
        )
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"
    include_js = True if components is None else _any_requires_js(components)

    # 1. Determine where to mount static files
    actual_static_url = static_url
    if not use_cdn and mount_static:
        if force_static_url:
            actual_static_url = static_url
        else:
            # Only resolve and mount if not already done
            if hasattr(app, "_faststrap_static_url"):
                actual_static_url = app._faststrap_static_url
            else:
                actual_static_url = resolve_static_url(app, static_url)

    # 2. Collect favicon links FIRST (before Bootstrap assets)
    favicon_links: list[Any] = []
    if favicon_url:
        favicon_links = create_favicon_links(favicon_url)
    elif include_favicon:
        if not use_cdn:
            default_favicon = get_default_favicon_url(False, actual_static_url)
            favicon_links = create_favicon_links(default_favicon)

    # 3. Get Bootstrap assets with theme, mode, and font
    bootstrap_assets = get_assets(
        use_cdn=use_cdn,
        include_custom=True,
        static_url=actual_static_url if not use_cdn else None,
        theme=theme,
        mode=mode,
        font_family=font_family,
        font_weights=font_weights,
        include_js=include_js,
        include_favicon=use_cdn and include_favicon and favicon_url is None,
    )

    # 4. Idempotent Header Management
    # Remove any existing FastStrap headers to prevent accumulation
    new_fs_hdrs = list(favicon_links) + list(bootstrap_assets)
    old_fs_hdrs = getattr(app, "_faststrap_hdrs", [])

    current_hdrs = list(getattr(app, "hdrs", []))

    # Remove old items by identity if possible
    filtered_hdrs = [h for h in current_hdrs if h not in old_fs_hdrs]

    # Prepend new ones
    app.hdrs = new_fs_hdrs + filtered_hdrs
    app._faststrap_hdrs = new_fs_hdrs

    # 5. Apply data-bs-theme attribute for non-auto modes
    if mode in {"light", "dark"}:
        existing_htmlkw = getattr(app, "htmlkw", {}) or {}
        existing_htmlkw.update({"data-bs-theme": mode})
        app.htmlkw = existing_htmlkw

    # 6. Mount static files (once only)
    if not use_cdn and mount_static and not hasattr(app, "_faststrap_static_url"):
        try:
            static_path = get_static_path()
            # Use insert(0) to ensure static route takes precedence over catch-all routes (like fast_app's /{path})
            app.routes.insert(
                0,
                Mount(
                    actual_static_url,
                    StaticFiles(directory=str(static_path)),
                    name="faststrap_static",
                ),
            )
            app._faststrap_static_url = actual_static_url
        except Exception as e:
            # Check if this is a "already mounted" error (which is fine)
            error_msg = str(e).lower()
            if any(
                keyword in error_msg for keyword in ["already", "duplicate", "mounted", "exists"]
            ):
                # Static files already mounted by another call, just mark it
                app._faststrap_static_url = actual_static_url
            else:
                # Real error - fall back to CDN
                caution = f"""
            FastStrap: Could not mount local static files ({e}).
            Falling back to CDN mode. You can explicitly set use_cdn=True.
            """
                warnings.warn(caution, RuntimeWarning, stacklevel=2)
                use_cdn = True
                if favicon_url:
                    fallback_favicon_links = create_favicon_links(favicon_url)
                else:
                    fallback_favicon_links = []

                fallback_bootstrap_assets = get_assets(
                    use_cdn=True,
                    include_custom=True,
                    static_url=None,
                    theme=theme,
                    mode=mode,
                    font_family=font_family,
                    font_weights=font_weights,
                    include_js=include_js,
                    include_favicon=include_favicon and favicon_url is None,
                )
                fallback_fs_hdrs = list(fallback_favicon_links) + list(fallback_bootstrap_assets)
                app.hdrs = fallback_fs_hdrs + filtered_hdrs
                app._faststrap_hdrs = fallback_fs_hdrs

    app._faststrap_bootstrap_added = True
    return app


def mount_assets(
    app: Any,
    directory: str,
    url_path: str = "/assets",
    name: str | None = None,
    priority: bool = True,
    allow_override: bool = False,
) -> None:
    """Mount a static files directory to your FastHTML app.

    This is a convenience wrapper around Starlette's Mount and StaticFiles
    that handles path resolution and mounting order automatically.

    Args:
        app: FastHTML application instance
        directory: Path to directory containing static files.
                  Can be relative (to calling file) or absolute.
        url_path: URL path to mount at (default: "/assets").
                 Must start with "/".
        name: Mount name for Starlette routing.
             If None, auto-generated from url_path.
        priority: If True, insert at start of routes to take precedence
                 over catch-all routes (default: True).
        allow_override: If True, allow overriding Faststrap's static mount.
                       NOT recommended as it will break Bootstrap CSS/JS loading.
                       (default: False)

    Raises:
        ValueError: If url_path doesn't start with "/" or conflicts with Faststrap
        FileNotFoundError: If directory doesn't exist

    Warning:
        Do not use the same url_path as Faststrap's static files (usually "/static").
        This will cause Bootstrap CSS/JS to fail loading. Use "/assets" or another path.

    Example:
        Basic usage:
        >>> from fasthtml.common import FastHTML
        >>> from faststrap import add_bootstrap, mount_assets
        >>>
        >>> app = FastHTML()
        >>> add_bootstrap(app)
        >>> mount_assets(app, "assets")  # Mounts assets/ at /assets/

        Multiple directories:
        >>> mount_assets(app, "images", url_path="/img")
        >>> mount_assets(app, "uploads", url_path="/uploads")

        Absolute path:
        >>> mount_assets(app, "/var/www/static", url_path="/static-files")

        Custom static URL for Faststrap (to use /static for your files):
        >>> add_bootstrap(app, static_url="/faststrap-static")
        >>> mount_assets(app, "static", url_path="/static")  # Now safe!
    """
    # Validate url_path
    if not url_path.startswith("/"):
        raise ValueError(f"url_path must start with '/'. Got: {url_path}")

    # Check for conflicts with Faststrap's static mount
    faststrap_url = getattr(app, "_faststrap_static_url", None)
    if faststrap_url and url_path.rstrip("/") == faststrap_url.rstrip("/"):
        if not allow_override:
            raise ValueError(
                f"Cannot mount assets at '{url_path}' - this conflicts with Faststrap's static files.\n"
                f"Faststrap is using '{faststrap_url}' for Bootstrap CSS/JS.\n\n"
                f"Solutions:\n"
                f"1. Use a different url_path:\n"
                f"   mount_assets(app, '{directory}', url_path='/assets')\n\n"
                f"2. Configure Faststrap to use a different URL:\n"
                f"   add_bootstrap(app, static_url='/faststrap-static')\n"
                f"   mount_assets(app, '{directory}', url_path='/static')\n\n"
                f"3. Override Faststrap (NOT recommended, will break Bootstrap):\n"
                f"   mount_assets(app, '{directory}', url_path='{url_path}', allow_override=True)\n\n"
                f"Recommended: Use '/assets' for your files and '{faststrap_url}' for Faststrap."
            )
        else:
            warnings.warn(
                f"Overriding Faststrap's static mount at '{url_path}'. "
                f"Bootstrap CSS/JS may not load correctly.",
                RuntimeWarning,
                stacklevel=2,
            )

    # Resolve directory path
    if os.path.isabs(directory):
        # Absolute path - use as-is
        assets_path = Path(directory)
    else:
        # Relative path - resolve relative to calling file
        # Get the caller's file path from the stack
        frame = sys._getframe(1)
        caller_file = frame.f_globals.get("__file__")

        if caller_file:
            caller_dir = os.path.dirname(os.path.abspath(caller_file))
            assets_path = Path(caller_dir) / directory
        else:
            # Fallback to current working directory
            assets_path = Path.cwd() / directory

    # Check if directory exists
    if not assets_path.exists():
        raise FileNotFoundError(
            f"Static directory not found: {assets_path}\n"
            f"Make sure the directory exists before calling mount_assets()."
        )

    if not assets_path.is_dir():
        raise ValueError(
            f"Path is not a directory: {assets_path}\n"
            f"mount_assets() requires a directory, not a file."
        )

    # Auto-generate name if not provided
    if name is None:
        # Convert /assets to "assets", /my-files to "my_files"
        name = url_path.strip("/").replace("-", "_").replace("/", "_")
        if not name:
            name = "static"

    # Create the mount
    mount = Mount(url_path, StaticFiles(directory=str(assets_path)), name=name)

    # Add to routes
    if priority:
        # Insert at beginning to take precedence
        app.routes.insert(0, mount)
    else:
        # Append to end
        app.routes.append(mount)
