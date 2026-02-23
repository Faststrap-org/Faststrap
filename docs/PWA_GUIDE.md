# Building PWAs with Faststrap

Faststrap provides a production-safe PWA baseline through `add_pwa()`:

- Manifest generation (`/manifest.json`)
- Service worker route (`/sw.js`)
- Automatic service worker registration
- Offline fallback route (`/offline`)
- Runtime caching for better resilience

## Quick Start

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, add_pwa

app = FastHTML()
add_bootstrap(app)

add_pwa(
    app,
    name="My App",
    short_name="MyApp",
    theme_color="#0d6efd",
    icon_path="/static/icon.png",
)
```

## What `add_pwa()` Configures

1. Injects required PWA/mobile meta tags.
2. Serves a generated `manifest.json`.
3. Serves a robust service worker script at `/sw.js`.
4. Injects service worker registration code into app headers.
5. Serves `/offline` page (enabled by default).

## Default Offline/Caching Strategy

The built-in service worker uses:

- Install: tolerant pre-cache (`Promise.allSettled`) so one failed URL does not break install.
- Navigation requests: network-first with cache fallback, then `/offline`.
- Static assets (`css`, `js`, `images`, fonts): stale-while-revalidate.
- Other GET requests: network-first with runtime cache write-through.

This is a practical baseline for production apps that need reliable offline fallback behavior.

## Advanced Configuration

`add_pwa()` now supports cache controls:

```python
add_pwa(
    app,
    cache_name="myapp-cache",
    cache_version="v2026-02-23",
    pre_cache_urls=(
        "/health",
        "/assets/logo.png",
    ),
)
```

- `cache_name`: prefix for cache storage
- `cache_version`: version suffix for cache invalidation on deploy
- `pre_cache_urls`: additional URLs to pre-cache

Faststrap still pre-caches its core defaults and `/offline`.

## When to Use a Custom Service Worker

Use a custom `sw.js` when you need:

- fine-grained API caching rules
- background sync
- push notifications
- per-route cache policies

In that case:

1. pass `service_worker=False` to `add_pwa()`
2. mount your own `/sw.js` route

## Mobile Components

Faststrap also includes mobile-oriented UI components:

- `BottomNav`, `BottomNavItem`
- `Sheet`
- `InstallPrompt`
