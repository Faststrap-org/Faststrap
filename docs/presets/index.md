# HTMX Presets

**Replace 90% of frontend JavaScript** with server-side Python + HTMX patterns.

FastStrap ships ready-made HTMX interaction presets that eliminate the need for client-side JavaScript libraries. Each preset generates the correct `hx-*` attributes automatically.

## Why Presets?

Most SaaS frontends ship custom JavaScript for:

- Live search & filtering → **ActiveSearch**
- Infinite scroll pagination → **InfiniteScroll**
- Auto-refreshing dashboards → **AutoRefresh**
- Lazy loading content → **LazyLoad**
- Loading buttons → **LoadingButton**

FastStrap replaces all of these with **zero JavaScript**.

## Installation

Presets are included in FastStrap but imported separately:

```python
from faststrap.presets import ActiveSearch, InfiniteScroll, AutoRefresh, LazyLoad, LoadingButton
```

## Response Helpers

Server-side response utilities for common HTMX patterns:

```python
from faststrap.presets import hx_redirect, hx_refresh, toast_response, require_auth
```

| Helper | Purpose |
| --- | --- |
| `hx_redirect(url)` | Client-side redirect via HX-Redirect header |
| `hx_refresh()` | Full page refresh via HX-Refresh header |
| `toast_response(content, message)` | Return content + out-of-band toast notification |
| `@require_auth()` | Decorator to protect routes with session auth |

## Quick Example

```python
from fasthtml.common import *
from faststrap import *
from faststrap.presets import ActiveSearch, toast_response

app = FastHTML()
add_bootstrap(app)

@app.get("/")
def home():
    return Container(
        ActiveSearch(
            endpoint="/api/search",
            target="#results",
            placeholder="Search users...",
        ),
        Div(id="results"),
    )

@app.get("/api/search")
def search(q: str = ""):
    results = db.search(q)
    return Div(*[Card(r.name) for r in results])

@app.post("/save")
def save():
    return toast_response(
        content=Card("Saved!"),
        message="Changes saved successfully",
        variant="success",
    )
```
