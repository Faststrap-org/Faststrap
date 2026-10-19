# PWA API

Faststrap's PWA helpers provide a generated manifest, service-worker route, offline fallback, and registration script without making PWA behavior mandatory for ordinary FastHTML apps.

## `PwaMeta`

Use `PwaMeta(...)` when you need the generated manifest link and mobile metadata without registering routes or a service worker yourself.

```python
from faststrap import PwaMeta

head = PwaMeta(
    name="Operations Console",
    short_name="Ops",
    icon_path="/assets/icon.png",
)
```

## `add_pwa`

Use `add_pwa(app, ...)` for the complete integration. It registers the manifest and service-worker routes and injects the required metadata and registration script.

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, add_pwa

app = FastHTML()
add_bootstrap(app)
add_pwa(
    app,
    name="Operations Console",
    icon_path="/assets/icon.png",
    cache_name="ops-console",
    cache_version="v2",
    pre_cache_urls=("/health",),
)
```

Important boundaries:

- Use a square PNG for the default icon path when broad install compatibility matters.
- `enable_background_sync` and `enable_push` provide service-worker foundations; queue persistence, authentication, and push subscription storage remain application responsibilities.
- Set `service_worker=False` when the application owns its own service-worker route.
- Review `scope`, `start_url`, and cache policies when deploying below a subpath.

## API Reference

::: faststrap.pwa.core.PwaMeta
    options:
        show_source: true
        heading_level: 2

::: faststrap.pwa.core.add_pwa
    options:
        show_source: true
        heading_level: 2
