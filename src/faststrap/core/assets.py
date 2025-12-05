"""Bootstrap asset injection and theme management."""

from typing import Optional, Tuple, Any
from os import environ
from fasthtml.common import Link, Script, Style
from starlette.staticfiles import StaticFiles  # For explicit mounting (FastHTML/Starlette standard)

# Bootstrap versions
BOOTSTRAP_VERSION = "5.3.3"
BOOTSTRAP_ICONS_VERSION = "1.11.3"

# CDN assets with SRI hashes
CDN_ASSETS = (
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css",
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
        crossorigin="anonymous"
    ),
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/bootstrap-icons.min.css"
    ),
    Script(
        src=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js",
        integrity="sha384-YVPcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz",
        crossorigin="anonymous"
    ),
)

# Local assets
LOCAL_ASSETS = (
    Link(rel="stylesheet", href="/static/css/bootstrap.min.css"),
    Link(rel="stylesheet", href="/static/css/bootstrap-icons.min.css"),
    Script(src="/static/js/bootstrap.bundle.min.js"),
)

# Custom FastStrap enhancements — now properly placed in <head>
CUSTOM_STYLES = Style("""
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
""")

def get_assets(use_cdn: Optional[bool] = None, include_custom: bool = True) -> Tuple[Any, ...]:
    """Get Bootstrap assets for injection.
    
    Args:
        use_cdn: Use CDN (True) or local files (False). Defaults to FASTSTRAP_USE_CDN env var.
        include_custom: Include FastStrap custom styles.
    
    Returns:
        Tuple of FastHTML elements for app.hdrs
    """
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"
    
    assets = CDN_ASSETS if use_cdn else LOCAL_ASSETS
    
    if include_custom:
        return assets + (CUSTOM_STYLES,)
    return assets


def add_bootstrap(
    app: Any,
    theme: Optional[str] = None,
    use_cdn: Optional[bool] = None,
    mount_static: bool = True
) -> Any:
    """Enhance FastHTML app with Bootstrap.
    
    Args:
        app: FastHTML application instance
        theme: Bootstrap theme ('light', 'dark', or None for auto)
        use_cdn: Use CDN instead of local assets
        mount_static: Auto-mount /static directory
    
    Returns:
        Modified app instance
    
    Example:
        from fasthtml.common import FastHTML
        from faststrap import add_bootstrap
        
        app = FastHTML()
        add_bootstrap(app, theme="dark")
    """
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"
    
    # Inject assets — safe for FastHTML 0.12+ (handles list/tuple hdrs)
    new_assets = get_assets(use_cdn=use_cdn, include_custom=True)
    if isinstance(app.hdrs, tuple):
        app.hdrs = list(app.hdrs)  # Convert to list if needed
    app.hdrs[0:0] = new_assets  # Prepend without mutation issues
    
    # Apply theme safely using middleware (avoids ASGI breakage)
    if theme in {"light", "dark"}:
        @app.middleware("http")
        async def theme_middleware(request: Any, call_next: Any) -> Any:
            """Middleware to inject data-bs-theme into <html> tag."""
            response = await call_next(request)
            if "text/html" in response.headers.get("content-type", ""):
                try:
                    html = response.body.decode("utf-8")
                    if "<html" in html and f'data-bs-theme="{theme}"' not in html[:300]:
                        html = html.replace("<html", f'<html data-bs-theme="{theme}"', 1)
                        response.body = html.encode("utf-8")
                        if "content-length" in response.headers:
                            response.headers["content-length"] = str(len(response.body))
                except (UnicodeDecodeError, AttributeError):
                    pass  # Graceful fallback for non-HTML or binary responses
            return response
    
    # Mount static files (only when using local assets) — using Starlette's explicit mount
    if not use_cdn and mount_static:
        try:
            # Check if already mounted to avoid duplicates
            if not any(route.path == "/static" for route in app.routes):
                app.mount("/static", StaticFiles(directory="static"), name="static")
        except Exception:
            pass  # Already mounted or dir missing — safe to ignore

    return app