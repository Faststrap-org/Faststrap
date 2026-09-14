"""Core PWA functionality for Faststrap."""

import json
from collections.abc import Sequence
from typing import Any

from fasthtml.common import Link, Meta, Script, Title
from starlette.responses import JSONResponse, Response

from ..components.display.empty_state import EmptyState
from ..core.assets import (
    BOOTSTRAP_CSS_URL,
    BOOTSTRAP_ICONS_URL,
    BOOTSTRAP_JS_URL,
    FASTSTRAP_CDN_CSS_FILES,
    _get_faststrap_cdn_version,
)

_DEFAULT_ICON_PATH = "/assets/icon.png"


def _join_scope_path(scope: str, path: str) -> str:
    """Join a deployment scope and absolute path into a scoped absolute URL."""
    # Normalize route paths for scoped deployments (for example: /myapp/).
    normalized_scope = _normalize_scope(scope)
    relative_path = path.lstrip("/")
    return f"{normalized_scope}{relative_path}" if normalized_scope != "/" else f"/{relative_path}"


def _normalize_scope(scope: str) -> str:
    """Normalize scope to '/prefix/' format."""
    normalized_scope = (scope or "/").strip()
    if not normalized_scope.startswith("/"):
        normalized_scope = f"/{normalized_scope}"
    if not normalized_scope.endswith("/"):
        normalized_scope = f"{normalized_scope}/"
    return normalized_scope


def _build_sw_register_script(
    sw_path: str,
    scope: str,
    *,
    enable_background_sync: bool = False,
    background_sync_tag: str = "faststrap-background-sync",
) -> str:
    """Build service worker registration script for the configured scope."""
    sync_registration = ""
    if enable_background_sync:
        sync_tag = json.dumps(background_sync_tag)
        sync_registration = f"""
                if ('sync' in reg) {{
                    reg.sync.register({sync_tag}).catch(err => console.log('Sync register failed', err));
                }}
"""
    sw_path_js = json.dumps(sw_path)
    scope_js = json.dumps(scope)
    return f"""
if ('serviceWorker' in navigator) {{
    window.addEventListener('load', () => {{
        navigator.serviceWorker.register({sw_path_js}, {{ scope: {scope_js} }})
            .then(reg => {{
                console.log('SW registered!', reg);
                {sync_registration}
            }})
            .catch(err => console.log('SW failed', err));
    }});
}}
"""


_DEFAULT_LOCAL_PRECACHE_URLS = (
    BOOTSTRAP_CSS_URL,
    BOOTSTRAP_JS_URL,
    BOOTSTRAP_ICONS_URL,
    "/static/css/faststrap-fx.css",
    "/static/css/faststrap-layouts.css",
    "/static/css/faststrap-visual.css",
)


def _default_precache_urls(*, use_cdn: bool) -> tuple[str, ...]:
    """Return the default service-worker precache list for the asset mode."""
    if not use_cdn:
        return _DEFAULT_LOCAL_PRECACHE_URLS

    version = _get_faststrap_cdn_version()
    ref = "main" if version == "main" else version if version.startswith("v") else f"v{version}"
    static_base = f"https://cdn.jsdelivr.net/gh/Faststrap-org/Faststrap@{ref}/src/faststrap/static"
    faststrap_css = tuple(f"{static_base}/{css_path}" for css_path in FASTSTRAP_CDN_CSS_FILES)
    return (
        BOOTSTRAP_CSS_URL,
        BOOTSTRAP_JS_URL,
        BOOTSTRAP_ICONS_URL,
        *faststrap_css,
    )


def _app_uses_cdn_assets(app: Any) -> bool:
    """Best-effort detection of CDN asset usage from injected app headers."""
    for header in getattr(app, "hdrs", []):
        attrs = getattr(header, "attrs", {})
        for key in ("href", "src"):
            value = attrs.get(key)
            if isinstance(value, str) and "cdn.jsdelivr.net" in value:
                return True
    return False


def _render_sw_script(
    *,
    cache_name: str,
    cache_version: str,
    pre_cache_urls: Sequence[str],
    offline_fallback_path: str,
    enable_background_sync: bool,
    background_sync_tag: str,
    route_cache_policies: dict[str, str] | None,
    enable_push: bool,
    default_push_title: str,
) -> str:
    """Render a robust network-first + runtime-caching service worker."""
    escaped_urls = ",\n  ".join(json.dumps(url) for url in pre_cache_urls)
    full_cache_name = f"{cache_name}-{cache_version}"
    serialized_route_policies = json.dumps(route_cache_policies or {})
    cache_name_js = json.dumps(full_cache_name)
    offline_fallback_js = json.dumps(offline_fallback_path)
    background_sync_tag_js = json.dumps(background_sync_tag)
    default_push_title_js = json.dumps(default_push_title)

    return f"""const CACHE_NAME = {cache_name_js};
const OFFLINE_FALLBACK = {offline_fallback_js};
const PRECACHE_URLS = [
  {escaped_urls}
];

const STATIC_DESTINATIONS = new Set(["style", "script", "image", "font"]);
const ENABLE_BACKGROUND_SYNC = {"true" if enable_background_sync else "false"};
const BACKGROUND_SYNC_TAG = {background_sync_tag_js};
const ROUTE_CACHE_POLICIES = {serialized_route_policies};
const ENABLE_PUSH = {"true" if enable_push else "false"};
const DEFAULT_PUSH_TITLE = {default_push_title_js};

function isHttpRequest(request) {{
  return request.url.startsWith("http://") || request.url.startsWith("https://");
}}

function isStaticRequest(request) {{
  if (STATIC_DESTINATIONS.has(request.destination)) return true;
  const url = new URL(request.url);
  return url.pathname.startsWith("/static/") || url.pathname.endsWith(".css") || url.pathname.endsWith(".js");
}}

async function safePrecache() {{
  const cache = await caches.open(CACHE_NAME);
  await Promise.allSettled(PRECACHE_URLS.map((url) => cache.add(url)));
}}

async function cleanupOldCaches() {{
  const names = await caches.keys();
  await Promise.all(names.filter((name) => name !== CACHE_NAME).map((name) => caches.delete(name)));
}}

async function networkFirst(request) {{
  try {{
    const response = await fetch(request);
    if (response && response.ok) {{
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }}
    return response;
  }} catch (_error) {{
    const cached = await caches.match(request);
    if (cached) return cached;
    if (request.mode === "navigate") {{
      const offline = await caches.match(OFFLINE_FALLBACK);
      if (offline) return offline;
    }}
    return new Response("Offline", {{ status: 503, statusText: "Service Unavailable" }});
  }}
}}

async function staleWhileRevalidate(request) {{
  const cached = await caches.match(request);
  const networkPromise = fetch(request)
    .then(async (response) => {{
      if (response && response.ok) {{
        const cache = await caches.open(CACHE_NAME);
        cache.put(request, response.clone());
      }}
      return response;
    }})
    .catch(() => null);

  if (cached) {{
    networkPromise.catch(() => null);
    return cached;
  }}

  const networkResponse = await networkPromise;
  if (networkResponse) return networkResponse;
  return new Response("", {{ status: 504, statusText: "Gateway Timeout" }});
}}

async function cacheFirst(request) {{
  const cached = await caches.match(request);
  if (cached) return cached;
  try {{
    const response = await fetch(request);
    if (response && response.ok) {{
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }}
    return response;
  }} catch (_error) {{
    return new Response("", {{ status: 504, statusText: "Gateway Timeout" }});
  }}
}}

async function processBackgroundSync() {{
  // Foundation hook: queue persistence/replay strategy plugs in here.
  // Current behavior is intentionally no-op to keep this layer opt-in and safe.
  return Promise.resolve();
}}

function resolveRouteStrategy(request) {{
  const url = new URL(request.url);
  for (const [prefix, strategy] of Object.entries(ROUTE_CACHE_POLICIES)) {{
    if (url.pathname.startsWith(prefix) || url.href.startsWith(prefix) || url.origin === prefix) return strategy;
  }}
  return null;
}}

self.addEventListener("install", (event) => {{
  event.waitUntil(safePrecache());
  self.skipWaiting();
}});

self.addEventListener("activate", (event) => {{
  event.waitUntil(cleanupOldCaches());
  self.clients.claim();
}});

self.addEventListener("fetch", (event) => {{
  if (event.request.method !== "GET" || !isHttpRequest(event.request)) return;
  const routeStrategy = resolveRouteStrategy(event.request);

  if (routeStrategy === "cache-first") {{
    event.respondWith(cacheFirst(event.request));
    return;
  }}

  if (routeStrategy === "stale-while-revalidate") {{
    event.respondWith(staleWhileRevalidate(event.request));
    return;
  }}

  if (routeStrategy === "network-first") {{
    event.respondWith(networkFirst(event.request));
    return;
  }}

  if (event.request.mode === "navigate") {{
    event.respondWith(networkFirst(event.request));
    return;
  }}

  if (isStaticRequest(event.request)) {{
    event.respondWith(staleWhileRevalidate(event.request));
    return;
  }}

  event.respondWith(networkFirst(event.request));
}});

self.addEventListener("sync", (event) => {{
  if (!ENABLE_BACKGROUND_SYNC) return;
  if (event.tag !== BACKGROUND_SYNC_TAG) return;
  event.waitUntil(processBackgroundSync());
}});

self.addEventListener("push", (event) => {{
  if (!ENABLE_PUSH) return;
  const payload = event.data ? event.data.json() : {{}};
  const title = payload.title || DEFAULT_PUSH_TITLE;
  const options = {{
    body: payload.body || "",
    icon: payload.icon || "/static/icon.png",
    badge: payload.badge || "/static/icon.png",
    data: payload.data || {{}},
  }};
  event.waitUntil(self.registration.showNotification(title, options));
}});

self.addEventListener("notificationclick", (event) => {{
  event.notification.close();
  const targetUrl = (event.notification.data && event.notification.data.url) || "/";
  event.waitUntil(clients.openWindow(targetUrl));
}});
"""


def PwaMeta(
    name: str | None = None,
    short_name: str | None = None,
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",
    description: str | None = None,
    icon_path: str = _DEFAULT_ICON_PATH,
    icon_192: str | None = None,
    icon_512: str | None = None,
    manifest_path: str = "/manifest.json",
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
        icon_192: Optional dedicated 192x192 icon path
        icon_512: Optional dedicated 512x512 icon path
        manifest_path: URL path to the manifest file

    Returns:
        Tuple of FastHTML Meta and Link elements
    """
    primary_icon = icon_192 or icon_path
    tile_icon = icon_512 or icon_path
    tags = [
        # Basic Mobile Meta
        Meta(
            name="viewport",
            content="width=device-width, initial-scale=1",
        ),
        Meta(name="theme-color", content=theme_color),
        Meta(name="mobile-web-app-capable", content="yes"),
        # iOS Specific
        Meta(name="apple-mobile-web-app-capable", content="yes"),
        Meta(name="apple-mobile-web-app-status-bar-style", content="black-translucent"),
        Meta(name="apple-mobile-web-app-title", content=short_name or name or "App"),
        Link(rel="apple-touch-icon", href=primary_icon),
        # Windows
        Meta(name="msapplication-TileColor", content=theme_color),
        Meta(name="msapplication-TileImage", content=tile_icon),
        # Manifest
        Link(rel="manifest", href=manifest_path),
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
    icon_path: str = _DEFAULT_ICON_PATH,
    icon_192: str | None = None,
    icon_512: str | None = None,
    display: str = "standalone",
    start_url: str = "/",
    scope: str = "/",
    service_worker: bool = True,
    offline_page: bool = True,
    cache_name: str = "faststrap-app",
    cache_version: str = "v1",
    pre_cache_urls: Sequence[str] | None = None,
    use_cdn: bool | None = None,
    enable_background_sync: bool = False,
    background_sync_tag: str = "faststrap-background-sync",
    route_cache_policies: dict[str, str] | None = None,
    enable_push: bool = False,
    default_push_title: str = "Faststrap Notification",
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
        icon_192: Optional dedicated 192x192 icon path for the manifest and touch icon
        icon_512: Optional dedicated 512x512 icon path for the manifest/tile icon
        display: Display mode (standalone, fullscreen, minimal-ui, browser)
        start_url: URL to open on launch
        scope: Scope of the PWA
        service_worker: Enable automatic Service Worker
        offline_page: Enable automatic /offline route
        cache_name: Service worker cache name prefix
        cache_version: Cache version suffix used for cache invalidation
        pre_cache_urls: Optional extra URLs to precache (in addition to defaults)
        use_cdn: Force CDN-aware precache defaults; when omitted this is auto-detected
        enable_background_sync: Enable Background Sync foundation hooks
        background_sync_tag: Tag used for Background Sync registrations
        route_cache_policies: Optional route prefix -> strategy mapping
                              values: "network-first", "stale-while-revalidate", "cache-first"
        enable_push: Enable push notification service worker handlers
        default_push_title: Fallback push notification title
    """

    normalized_scope = _normalize_scope(scope)
    manifest_path = _join_scope_path(normalized_scope, "/manifest.json")
    sw_path = _join_scope_path(normalized_scope, "/sw.js")
    offline_path = _join_scope_path(normalized_scope, "/offline")

    # 1. Inject Headers
    pwa_headers = PwaMeta(
        name=name,
        short_name=short_name,
        theme_color=theme_color,
        background_color=background_color,
        description=description,
        icon_path=icon_path,
        icon_192=icon_192,
        icon_512=icon_512,
        manifest_path=manifest_path,
    )

    # Append to existing headers (similar logic to add_bootstrap)
    current_hdrs = list(getattr(app, "hdrs", []))
    app.hdrs = current_hdrs + list(pwa_headers)

    # 2. Serve Manifest
    icon_192_src = icon_192 or icon_path
    icon_512_src = icon_512 or icon_path
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
                "src": icon_192_src,
                "sizes": "192x192",
                "type": "image/png",
            },
            {
                "src": icon_512_src,
                "sizes": "512x512",
                "type": "image/png",
            },
        ],
    }

    @app.get(manifest_path)
    def manifest() -> Any:
        return JSONResponse(manifest_data)

    # 3. Serve Service Worker
    if service_worker:
        # Build robust service worker script with safe defaults and optional extension points.
        resolved_use_cdn = _app_uses_cdn_assets(app) if use_cdn is None else use_cdn
        deduped_precache = list(
            dict.fromkeys(
                [
                    *_default_precache_urls(use_cdn=resolved_use_cdn),
                    *(pre_cache_urls or []),
                    offline_path,
                ]
            )
        )
        sw_script = _render_sw_script(
            cache_name=cache_name,
            cache_version=cache_version,
            pre_cache_urls=deduped_precache,
            offline_fallback_path=offline_path,
            enable_background_sync=enable_background_sync,
            background_sync_tag=background_sync_tag,
            route_cache_policies=route_cache_policies,
            enable_push=enable_push,
            default_push_title=default_push_title,
        )

        @app.get(sw_path)
        def sw() -> Any:
            return Response(sw_script, media_type="application/javascript")

        # Register the SW in the app (inject script)
        reg_script = Script(
            _build_sw_register_script(
                sw_path=sw_path,
                scope=normalized_scope,
                enable_background_sync=enable_background_sync,
                background_sync_tag=background_sync_tag,
            )
        )
        app.hdrs = list(app.hdrs) + [reg_script]

    # 4. Serve Offline Page
    if offline_page:

        @app.get(offline_path)
        def offline() -> Any:
            return (
                Title("Offline - " + name),
                EmptyState(
                    title="No Internet Connection",
                    description="You are currently offline. Please check your connection and try again.",
                    icon="wifi-slash",
                    action_text="Retry",
                    action_href=start_url,  # Try going home
                    cls="min-vh-100 d-flex align-items-center justify-content-center",
                ),
            )
