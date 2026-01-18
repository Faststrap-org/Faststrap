"""Core PWA functionality for Faststrap."""

from pathlib import Path
from typing import Any

from fasthtml.common import Link, Meta, Script, Title
from starlette.responses import FileResponse, JSONResponse

from ..components.display.empty_state import EmptyState

# SW Registration Script (Extracted for formatting)
_SW_REGISTER_SCRIPT = """
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(reg => console.log('SW registered!', reg))
            .catch(err => console.log('SW failed', err));
    });
}
"""


def PwaMeta(
    name: str | None = None,
    short_name: str | None = None,
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",
    description: str | None = None,
    icon_path: str = "/static/icon.png",  # Default path
) -> tuple[Any, ...]:
    """
    Generate PWA meta tags and link elements.

    These tags are essential for:
    - Installing the app on mobile home screens
    - Setting the theme color of the browser bar
    - Defining icons for different platforms (iOS/Android)

    Args:
        name: Full name of the application
        short_name: Short name for home screen (12 chars max recommended)
        theme_color: Color of the browser toolbar
        background_color: Background color for splash screen
        description: Description of the app
        icon_path: Path to the main icon (should be square, ideally 512x512)

    Returns:
        Tuple of FastHTML Meta and Link elements
    """
    tags = [
        # Basic Mobile Meta
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0",
        ),
        Meta(name="theme-color", content=theme_color),
        Meta(name="mobile-web-app-capable", content="yes"),
        # iOS Specific
        Meta(name="apple-mobile-web-app-capable", content="yes"),
        Meta(name="apple-mobile-web-app-status-bar-style", content="black-translucent"),
        Meta(name="apple-mobile-web-app-title", content=short_name or name or "App"),
        Link(rel="apple-touch-icon", href=icon_path),
        # Windows
        Meta(name="msapplication-TileColor", content=theme_color),
        Meta(name="msapplication-TileImage", content=icon_path),
        # Manifest
        Link(rel="manifest", href="/manifest.json"),
    ]

    if description:
        tags.append(Meta(name="description", content=description))

    return tuple(tags)


def add_pwa(
    app: Any,
    name: str = "Faststrap App",
    short_name: str = "Faststrap",
    description: str = "A Progressive Web App built with Faststrap",
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",
    icon_path: str = "/assets/icon.png",
    display: str = "standalone",
    start_url: str = "/",
    scope: str = "/",
    service_worker: bool = True,
    offline_page: bool = True,
) -> None:
    """
    Enable PWA capabilities for the FastHTML app.

    This helper:
    1. Injects PWA meta tags into app headers
    2. Serves a generated `manifest.json`
    3. Serves a standard `sw.js` Service Worker (if enabled)
    4. serves an `/offline` route (if enabled)

    Args:
        app: FastHTML application instance
        name: App name
        short_name: App short name
        description: App description
        theme_color: Theme color
        background_color: Splash screen background color
        icon_path: Path to icon file
        display: Display mode (standalone, fullscreen, minimal-ui, browser)
        start_url: URL to open on launch
        scope: Scope of the PWA
        service_worker: Enable automatic Service Worker
        offline_page: Enable automatic /offline route
    """

    # 1. Inject Headers
    pwa_headers = PwaMeta(
        name=name,
        short_name=short_name,
        theme_color=theme_color,
        background_color=background_color,
        description=description,
        icon_path=icon_path,
    )

    # Append to existing headers (similar logic to add_bootstrap)
    current_hdrs = list(getattr(app, "hdrs", []))
    app.hdrs = current_hdrs + list(pwa_headers)

    # 2. Serve Manifest
    manifest_data = {
        "name": name,
        "short_name": short_name,
        "description": description,
        "theme_color": theme_color,
        "background_color": background_color,
        "display": display,
        "start_url": start_url,
        "scope": scope,
        "icons": [
            {
                "src": icon_path,
                "sizes": "192x192",
                "type": "image/png",
            },
            {
                "src": icon_path,
                "sizes": "512x512",
                "type": "image/png",
            },
        ],
    }

    @app.get("/manifest.json")
    def manifest() -> JSONResponse:
        return JSONResponse(manifest_data)

    # 3. Serve Service Worker
    if service_worker:
        # Load the template
        sw_path = Path(__file__).parent / "templates" / "sw.js"

        @app.get("/sw.js")
        def sw() -> FileResponse:
            return FileResponse(sw_path, media_type="application/javascript")

        # Register the SW in the app (inject script)
        reg_script = Script(_SW_REGISTER_SCRIPT)
        app.hdrs = list(app.hdrs) + [reg_script]

    # 4. Serve Offline Page
    if offline_page:

        @app.get("/offline")
        def offline() -> Any:
            return (
                Title("Offline - " + name),
                EmptyState(
                    title="No Internet Connection",
                    description="You are currently offline. Please check your connection and try again.",
                    icon="wifi-off",
                    action_text="Retry",
                    action_href=start_url,  # Try going home
                    cls="min-vh-100 d-flex align-items-center justify-content-center",
                ),
            )
