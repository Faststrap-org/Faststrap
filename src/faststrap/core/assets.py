"""
FastStrap - Production Bootstrap Asset Manager
Safe for multi-worker servers, thread-safe, with graceful fallbacks.
"""

from __future__ import annotations

import inspect
import os
import warnings
from importlib import metadata as importlib_metadata
from os import environ
from pathlib import Path
from typing import Any
from urllib.parse import quote

from fasthtml.common import Link, Meta, Script, Style
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
    "css/faststrap-visual.css",
    "css/faststrap-toast.css",
]
FASTSTRAP_INIT_JS_FILE = "js/faststrap-init.js"
FASTSTRAP_MODERN_TOAST_JS_FILE = "js/modern-toast.js"
# HTMX cross-version bridge: resolved synchronously in <head> so body-inline
# component scripts and the deferred init/modern-toast runtimes can rely on it.
FASTSTRAP_HTMX_BRIDGE_JS_FILE = "js/faststrap-htmx.js"
# htmx 4 official 2.x-compat extension (load AFTER the htmx core script when a
# page enables `htmx4=True`; restores old event names for user code).
HTMX4_COMPAT_JS_URL = "https://cdn.jsdelivr.net/npm/htmx.org@4.0.0/dist/ext/htmx-2-compat.min.js"

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
        Link(rel="stylesheet", href=f"{base}/css/faststrap-visual.css"),
        Link(rel="stylesheet", href=f"{base}/css/faststrap-toast.css"),
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


def _faststrap_static_cdn_base(version: str) -> str:
    """Return the jsDelivr base URL for version-pinned Faststrap static assets."""
    if version == "main":
        ref = "main"
    elif version.startswith("v"):
        ref = version
    else:
        ref = f"v{version}"
    return f"https://cdn.jsdelivr.net/gh/Faststrap-org/Faststrap@{ref}/src/faststrap/static"


def _build_cdn_assets(
    version: str,
    include_favicon: bool,
    *,
    include_js: bool = True,
) -> list[Any]:
    """Build complete CDN assets list for use_cdn mode."""
    static_base = _faststrap_static_cdn_base(version)
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

.fs-theme-toggle {
  gap: 0.5rem;
  margin-bottom: 0;
}

.fs-theme-toggle .fs-theme-toggle-icon {
  flex-shrink: 0;
}

.fs-theme-toggle .form-check-input {
  margin-left: 0;
  cursor: pointer;
}

.fs-theme-toggle .form-check-label {
  margin-bottom: 0;
}

/* Simple Toast animations (no JavaScript required) */
@keyframes toastFadeOut {
  0% { opacity: 1; transform: translateX(0); pointer-events: auto; }
  99% { opacity: 0; transform: translateX(100%); pointer-events: none; }
  100% { opacity: 0; transform: translateX(100%); pointer-events: none; visibility: hidden; }
}

.toast-fade-out {
  animation: toastFadeOut 0.5s ease-in-out forwards;
}
"""

CUSTOM_STYLES = Style(CUSTOM_STYLES_CSS)

# The initialization script is loaded from static/js/faststrap-init.js
# This keeps the Python source clean and allows browsers to cache the JS.
# The file is served via the static files mount in local mode, or via CDN
# in CDN mode.
INIT_SCRIPT_JS = ""
INIT_SCRIPT = Script(src="/static/js/faststrap-init.js", defer=True)


def _faststrap_init_script(static_base: str) -> Any:
    """Return the Faststrap browser initializer for the given static base URL."""
    base = static_base.rstrip("/")
    return Script(src=f"{base}/{FASTSTRAP_INIT_JS_FILE}", defer=True)


def _faststrap_htmx_bridge_script(static_base: str) -> Any:
    """Return the HTMX cross-version bridge script.

    Loaded synchronously (not deferred) so inline component scripts in the
    body can rely on ``window.FaststrapHtmx`` during page parse.
    """
    base = static_base.rstrip("/")
    return Script(src=f"{base}/{FASTSTRAP_HTMX_BRIDGE_JS_FILE}")


def _faststrap_modern_toast_script(static_base: str) -> Any:
    """Return the ModernToast runtime script for the given static base URL."""
    base = static_base.rstrip("/")
    return Script(src=f"{base}/{FASTSTRAP_MODERN_TOAST_JS_FILE}", defer=True)


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
    include_modern_toast: bool = False,
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
        include_modern_toast: Include ModernToast runtime script

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
        if use_cdn:
            cdn_base = _faststrap_static_cdn_base(_get_faststrap_cdn_version())
            elements.append(_faststrap_htmx_bridge_script(cdn_base))
            elements.append(_faststrap_init_script(cdn_base))
            if include_modern_toast:
                elements.append(_faststrap_modern_toast_script(cdn_base))
        else:
            elements.append(_faststrap_htmx_bridge_script(actual_static_url))
            elements.append(_faststrap_init_script(actual_static_url))
            if include_modern_toast:
                elements.append(_faststrap_modern_toast_script(actual_static_url))

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


def _any_uses_modern_toast(components: list[Any]) -> bool:
    """Check whether any provided component is ModernToast or ModernToastStack."""
    for comp in components:
        name = getattr(comp, "__name__", None)
        if name in {"ModernToast", "ModernToastStack"}:
            return True
        meta = getattr(comp, "__faststrap_metadata__", None)
        if meta and meta.get("name") in {"ModernToast", "ModernToastStack"}:
            return True
    return False


def _detect_htmx4(app: Any) -> bool:
    """Return True when the app's headers already serve htmx 4 (FastHTML(htmx4=True))."""
    for h in getattr(app, "hdrs", []):
        attrs = getattr(h, "attrs", None)
        src = attrs.get("src", "") if isinstance(attrs, dict) else ""
        if isinstance(src, str) and "htmx.org@4" in src:
            return True
    return False


def _set_htmx_config(app: Any, *, extensions: list[str]) -> None:
    """Merge the `extensions` allow-list into the htmx-config meta element.

    htmx 4 reads only the *first* ``meta[name=\"htmx-config\"]`` in the page, so
    FastHTML's own ``metaCharacter`` shim must be patched in place rather than
    shadowed by a second meta (which htmx would ignore).
    """
    import json as _json

    hdrs = getattr(app, "hdrs", [])
    for h in hdrs:
        attrs = getattr(h, "attrs", None)
        if isinstance(attrs, dict) and attrs.get("name") == "htmx-config":
            try:
                cfg = _json.loads(attrs.get("content") or "{}")
            except ValueError:
                cfg = {}
            cfg["extensions"] = extensions
            attrs["content"] = _json.dumps(cfg)
            return
    # No htmx-config meta present yet (e.g. custom app without def_hdrs).
    hdrs.append(Meta(name="htmx-config", content=_json.dumps({"extensions": extensions})))


def _htmx4_compat_script() -> Any:
    """Official htmx 4 -> htmx 2 compat extension (restores old event names)."""
    return Script(src=HTMX4_COMPAT_JS_URL, defer=True)


def _apply_htmx4_options(
    app: Any, *, htmx4: bool | None, htmx_compat: bool, allow_extensions: list[str] | None
) -> None:
    """Apply Faststrap-level htmx 4 integrations onto the app's own headers.

    Detect the runtime from the app (``FastHTML(htmx4=True)``) unless an
    explicit override is given. When the runtime is htmx 4:
    - ``allow_extensions`` merges an extension allow-list into the page's
      htmx-config meta (htmx 4 security model).
    - ``htmx_compat`` appends the official 2.x-compat extension script AFTER
      the htmx core script so downstream user code keeps working.
    """
    is_htmx4 = _detect_htmx4(app) if htmx4 is None else bool(htmx4)
    if not is_htmx4:
        return
    if allow_extensions:
        _set_htmx_config(app, extensions=allow_extensions)
    if htmx_compat:
        getattr(app, "hdrs", []).append(_htmx4_compat_script())


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
    include_modern_toast: bool | None = None,
    htmx4: bool | None = None,
    htmx_compat: bool = False,
    allow_extensions: list[str] | None = None,
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
        include_modern_toast: Explicitly include the ModernToast runtime script.
            When None (default), the script is included only if `components`
            contains ModernToast or ModernToastStack.
        htmx4: Whether the app runs htmx 4 (FastHTML(htmx4=True)). When None
            (default), Faststrap auto-detects from the app's headers. This
            gates the htmx 4 compatibility and allow-list integrations below.
        htmx_compat: When running htmx 4, load the official htmx-2-compat
            extension so downstream code using legacy event names keeps working.
        allow_extensions: When running htmx 4, restrict which HTMX extensions
            may register by merging an allow-list into the page's htmx-config
            meta element (htmx 4 security model).

    Returns:
        Modified app instance

    Examples:
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
        warnings.warn(
            "add_bootstrap() has already been called on this app. " "Subsequent calls are ignored.",
            RuntimeWarning,
            stacklevel=2,
        )
        return
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"
    include_js = True if components is None else _any_requires_js(components)
    if include_modern_toast is None:
        include_modern_toast = False if components is None else _any_uses_modern_toast(components)

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
        include_modern_toast=include_modern_toast,
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
                    include_modern_toast=include_modern_toast,
                )
                fallback_fs_hdrs = list(fallback_favicon_links) + list(fallback_bootstrap_assets)
                app.hdrs = fallback_fs_hdrs + filtered_hdrs
                app._faststrap_hdrs = fallback_fs_hdrs

    app._faststrap_bootstrap_added = True
    # htmx 4 integrations (compat extension + extension allow-list) must be applied
    # after both the normal and the CDN-fallback header assembly above.
    _apply_htmx4_options(
        app,
        htmx4=htmx4,
        htmx_compat=htmx_compat,
        allow_extensions=allow_extensions,
    )
    return app


def mount_assets(
    app: Any,
    directory: str,
    url_path: str = "/assets",
    name: str | None = None,
    priority: bool = True,
    allow_override: bool = False,
    base_dir: str | os.PathLike[str] | None = None,
) -> None:
    """Mount a static files directory to your FastHTML app.

    This is a convenience wrapper around Starlette's Mount and StaticFiles
    that handles path resolution and mounting order automatically.

    Args:
        app: FastHTML application instance
        directory: Path to directory containing static files.
                  Can be absolute, relative to `base_dir`, relative to the
                  calling file (when available), or relative to the current
                  working directory as a final fallback.
        url_path: URL path to mount at (default: "/assets").
                 Must start with "/".
        name: Mount name for Starlette routing.
             If None, auto-generated from url_path.
        priority: If True, insert at start of routes to take precedence
                 over catch-all routes (default: True).
        allow_override: If True, allow overriding Faststrap's static mount.
                       NOT recommended as it will break Bootstrap CSS/JS loading.
                       (default: False)
        base_dir: Optional explicit base directory for resolving relative
                  `directory` paths. When omitted, Faststrap attempts to
                  resolve relative to the calling file and falls back to the
                  current working directory.

    Raises:
        ValueError: If url_path doesn't start with "/" or conflicts with Faststrap
        FileNotFoundError: If directory doesn't exist

    Warning:
        Do not use the same url_path as Faststrap's static files (usually "/static").
        This will cause Bootstrap CSS/JS to fail loading. Use "/assets" or another path.

    Examples:
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
        assets_path = _resolve_relative_assets_path(directory, base_dir=base_dir)

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


def _resolve_relative_assets_path(
    directory: str,
    *,
    base_dir: str | os.PathLike[str] | None = None,
) -> Path:
    """Resolve a relative assets path without relying on CPython-only frame APIs."""
    if base_dir is not None:
        return Path(base_dir) / directory

    module_file = Path(__file__).resolve()
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back if current_frame is not None else None
    try:
        while caller_frame is not None:
            caller_file = caller_frame.f_globals.get("__file__")
            if caller_file:
                resolved_caller = Path(caller_file).resolve()
                if resolved_caller != module_file:
                    return resolved_caller.parent / directory
            caller_frame = caller_frame.f_back
    finally:
        del current_frame
        del caller_frame

    return Path.cwd() / directory
