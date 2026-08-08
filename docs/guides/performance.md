# Performance Guide

This guide covers performance optimization strategies for FastHTML apps built with Faststrap.

---

## Static Assets

### CDN Mode (Default)

```python
from faststrap import add_bootstrap

add_bootstrap(app)
# Uses jsDelivr CDN for Bootstrap, Bootstrap Icons, and HTMX
```

CDN mode benefits:
- No build step required
- Assets cached across sites
- Smaller app bundle

### Local Mode

```python
from faststrap import add_bootstrap

add_bootstrap(app, mode="local")
```

Local mode benefits:
- Works offline
- No external dependencies
- Full control over asset versions

### Hybrid Mode

```python
from faststrap import add_bootstrap

add_bootstrap(
    app,
    mode="cdn",
    include_js=True,  # Include HTMX locally
)
```

---

## Component Rendering

### Use `include_js` Wisely

```python
from faststrap import add_bootstrap

# Only include JS when needed
add_bootstrap(app, include_js=False)  # No JS
add_bootstrap(app, include_js=True)   # Full JS bundle
```

### Lazy Load Components

```python
from faststrap import LazyLoad

LazyLoad(
    "/api/heavy-component",
    target="#heavy-area",
    placeholder=Spinner(size="sm"),
)
```

---

## Caching

### Static File Caching

```python
from faststrap import get_assets

assets = get_assets(app)
# Assets are cached with cache-control headers
```

### Response Caching

```python
from fasthtml.common import CacheControl

@app.get("/api/data")
def get_data():
    return JsonResponse(data, headers={"Cache-Control": "max-age=300"})
```

---

## Database Queries

### N+1 Prevention

```python
# Bad: N+1 queries
items = db.query(Item).all()
for item in items:
    print(item.user.name)  # Extra query per item

# Good: Eager loading
items = db.query(Item).options(selectinload(Item.user)).all()
```

---

## Service Worker (PWA)

```python
from faststrap import PwaMeta

PwaMeta(
    name="My App",
    short_name="App",
    theme_color="#5B6CFF",
    background_color="#FFFFFF",
    start_url="/",
    display="standalone",
)
```

Service workers cache static assets for offline use and faster loads.

---

## Monitoring

### Response Times

```python
import time

@app.before
def log_request_time(req, resp):
    start = time.time()
    yield
    elapsed = time.time() - start
    if elapsed > 0.5:
        print(f"Slow request: {req.url.path} took {elapsed:.2f}s")
```

### Memory Usage

```python
import tracemalloc

tracemalloc.start()

# ... app code ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
for stat in top_stats[:10]:
    print(stat)
```

---

## See Also

- [Static Files Guide](../STATIC_FILES.md)
- [PWA Guide](../PWA_GUIDE.md)
- [First App Tutorial](../getting-started/first-app.md)
