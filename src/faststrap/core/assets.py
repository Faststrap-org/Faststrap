"""
FastStrap - Production Bootstrap Asset Manager
Safe for multi-worker servers, thread-safe, with graceful fallbacks.
"""

from __future__ import annotations

import warnings
from os import environ
from typing import Any

from fasthtml.common import Link, Script, Style
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


# CDN assets with SRI hashes
CDN_ASSETS = (
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css",
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
        crossorigin="anonymous",
    ),
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/bootstrap-icons.min.css",
    ),
    Script(
        src=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js",
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz",
        crossorigin="anonymous",
        defer=True,
    ),
)


def local_assets(static_url: str) -> tuple[Any, ...]:
    """Generate local asset links for the given static URL."""
    base = static_url.rstrip("/")
    return (
        Link(rel="stylesheet", href=f"{base}/css/bootstrap.min.css"),
        Link(rel="stylesheet", href=f"{base}/css/bootstrap-icons.min.css"),
        Link(rel="stylesheet", href=f"{base}/css/faststrap-fx.css"),
        Link(rel="stylesheet", href=f"{base}/css/faststrap-layouts.css"),
        Script(src=f"{base}/js/bootstrap.bundle.min.js"),
    )


# Custom FastStrap enhancements
CUSTOM_STYLES = Style(
    """
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
)

# Automatic initialization for Tooltips and Popovers (supports HTMX)
INIT_SCRIPT = Script(
    """
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

        initBS(document);

        // HTMX support: Re-initialize on content swap
        document.body.addEventListener('htmx:afterSwap', (evt) => {
            initBS(evt.detail.elt);
        });
    });
    """
)


def get_assets(
    use_cdn: bool | None = None,
    include_custom: bool = True,
    static_url: str | None = None,
    theme: str | Theme | None = None,
    mode: ModeType = "light",
    font_family: str | None = None,
    font_weights: list[int] | None = None,
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

    Returns:
        Tuple of FastHTML elements for app.hdrs
    """
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"

    if use_cdn:
        assets = CDN_ASSETS
    else:
        actual_static_url = static_url if static_url is not None else "/static"
        assets = local_assets(actual_static_url)

    elements = list(assets)

    # Add Google Fonts link if specified (BEFORE other styles for proper loading)
    if font_family:
        weights = font_weights or [400, 500, 700]
        weights_str = ";".join(str(w) for w in weights)
        font_url = f"https://fonts.googleapis.com/css2?family={font_family.replace(' ', '+')}:wght@{weights_str}&display=swap"
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
) -> Any:
    """
    Enhance FastHTML app with Bootstrap (production-safe).

    Args:
        app: FastHTML application instance
        theme: Color theme - either a built-in name (e.g., "green-nature", "purple-magic"),
               a Theme instance created via create_theme(), or a community theme
        mode: Color mode for light/dark backgrounds:
              - "light": Light background, dark text (default)
              - "dark": Dark background, light text
              - "auto": Follows user's system preference (prefers-color-scheme)
        use_cdn: Use CDN instead of local assets
        mount_static: Auto-mount static directory
        static_url: Preferred URL prefix for static files
        force_static_url: Force use of this URL even if already mounted
        include_favicon: Include default FastStrap favicon
        favicon_url: Custom favicon URL (overrides default)
        font_family: Google Font name (e.g., "Inter", "Roboto", "Poppins")
        font_weights: Font weights to load (default: [400, 500, 700])

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
    # Clean up any previous FastStrap state on this app
    if hasattr(app, "_faststrap_static_url"):
        # We don't delete it anymore if it's already there to avoid re-mounting
        pass

    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"

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
        default_favicon = get_default_favicon_url(use_cdn, actual_static_url)
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
            from starlette.routing import Mount

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

                # Re-call with CDN=True
                return add_bootstrap(
                    app,
                    theme=theme,
                    mode=mode,
                    use_cdn=True,
                    mount_static=False,
                    include_favicon=include_favicon,
                    favicon_url=favicon_url,
                )

    return app


def mount_assets(
    app: Any,
    directory: str,
    url_path: str = "/assets",
    name: str | None = None,
    priority: bool = True,
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

    Raises:
        ValueError: If url_path doesn't start with "/"
        FileNotFoundError: If directory doesn't exist

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
    """
    import os
    import sys
    from pathlib import Path

    from starlette.routing import Mount

    # Validate url_path
    if not url_path.startswith("/"):
        raise ValueError(f"url_path must start with '/'. Got: {url_path}")

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
