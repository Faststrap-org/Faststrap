# HTMX Integration Guide

HTMX is the primary way Faststrap handles dynamic behavior without custom JavaScript. This guide covers the most common HTMX patterns with Faststrap components.

---

## What is HTMX?

HTMX is a JavaScript library that lets you access AJAX, CSS Transitions, WebSockets, and Server Sent Events directly in HTML. Instead of writing JavaScript, you use `hx-*` attributes in your markup.

Faststrap is designed around HTMX. Every component accepts `hx_*`, `data_*`, and `aria_*` kwargs and converts them to proper HTML attributes.

---

## Setting Up HTMX

Faststrap includes HTMX via CDN by default when you call `add_bootstrap(app)`:

```python
from faststrap import add_bootstrap

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)
```

HTMX is loaded automatically from jsDelivr CDN. If you need a specific version, pass `hx_version`:

```python
add_bootstrap(app, hx_version="1.9.10")
```

---

## Common HTMX Patterns

### 1. Search with Debounce

```python
from faststrap import Input, Debounce

Input(
    type="search",
    placeholder="Search...",
    name="q",
    hx_get="/api/search",
    hx_target="#results",
    hx_trigger=Debounce(300),
    cls="form-control",
)
```

### 2. Form Submission with Target

```python
from faststrap import Form, FormGroup, Input, Button

Form(
    FormGroup("Email", Input(name="email", type="email")),
    FormGroup("Password", Input(name="password", type="password")),
    Button("Login", type="submit", variant="primary"),
    method="post",
    hx_post="/login",
    hx_target="#content",
    hx_swap="innerHTML",
)
```

### 3. Button with Loading State

```python
from faststrap import Button

Button(
    "Save",
    variant="primary",
    hx_post="/save",
    hx_target="#form",
    hx_swap="outerHTML",
    hx_include="#form",
    hx_indicator="#saving",
)
Span("Saving...", id="saving", cls="d-none")
```

### 4. Infinite Scroll

```python
from faststrap import InfiniteScroll

InfiniteScroll(
    "/api/items",
    target="#item-list",
    page_param="page",
    item_template=lambda item: P(item["name"]),
)
```

### 5. Live Polling

```python
from faststrap import AutoRefresh

AutoRefresh(
    "/api/status",
    target="#status",
    interval=5000,
)
```

### 6. Click to Edit

```python
from faststrap import InlineEditor

InlineEditor(
    Span("Click to edit", id="name-display"),
    Input(name="name", value="Click to edit", id="name-input"),
    hx_patch="/profile/name",
    hx_target="#name-display",
)
```

### 7. Optimistic Update

```python
from faststrap import OptimisticAction

OptimisticAction(
    Button("Like", variant="secondary", outline=True),
    endpoint="/api/like",
    method="post",
    target="#like-count",
    swap="innerHTML",
    success_selector="#like-count",
)
```

---

## HTMX Attributes Reference

Faststrap converts Python kwargs to HTML attributes automatically:

| Python kwarg | HTML attribute | Description |
| --- | --- | --- |
| `hx_get` | `hx-get` | GET request URL |
| `hx_post` | `hx-post` | POST request URL |
| `hx_put` | `hx-put` | PUT request URL |
| `hx_delete` | `hx-delete` | DELETE request URL |
| `hx_patch` | `hx-patch` | PATCH request URL |
| `hx_target` | `hx-target` | CSS selector for target element |
| `hx_swap` | `hx-swap` | Swap strategy (`innerHTML`, `outerHTML`, `beforeend`, etc.) |
| `hx_trigger` | `hx-trigger` | Event trigger string |
| `hx_indicator` | `hx-indicator` | Loading indicator selector |
| `hx_include` | `hx-include` | Additional elements to include in request |
| `hx_boost` | `hx-boost` | Boost links |
| `hx_push_url` | `hx-push-url` | Push URL to browser history |
| `hx_history` | `hx-history` | History handling |
| `hx_select` | `hx-select` | CSS selector for response content |
| `hx_swap_oob` | `hx-swap-oob` | Out-of-band swap |
| `hx_sync` | `hx-sync` | Synchronize with other requests |
| `hx_vals` | `hx-vals` | Additional values to send |
| `hx_headers` | `hx-headers` | Additional headers |

---

## Debugging HTMX

### 1. Enable HTMX Debug Logging

```python
add_bootstrap(app, hx_debug=True)
```

### 2. Common Issues

| Problem | Solution |
| --- | --- |
| Request not firing | Check `hx-trigger` value in browser dev tools |
| Wrong content swapping | Verify `hx-target` selector matches element |
| CSRF errors | Ensure CSRF middleware is configured if using sessions |
| 404 on POST | Verify route accepts POST method |

### 3. Inspect Requests

Use browser dev tools Network tab to inspect HTMX requests. Look for:
- Request URL
- Request method
- Form data / query params
- Response content

---

## HTMX Presets

Faststrap provides presets for common HTMX patterns. See [Presets](../presets/index.md) for:

- `ActiveSearch` — search-as-you-type with debounce
- `InfiniteScroll` — pagination on scroll
- `AutoRefresh` — periodic polling
- `LazyLoad` — deferred loading
- `LoadingButton` — button loading state
- `OptimisticAction` — instant UI updates
- `PollUntil` — repeat until condition met

---

## Best Practices

1. **Keep endpoints RESTful** — Use GET for reads, POST/PUT/DELETE for mutations
2. **Return fragments, not full pages** — HTMX swaps only the target element
3. **Use `hx-swap-oob`** for side effects like toasts and notifications
4. **Debounce inputs** — Always use `Debounce` with search inputs
5. **Show loading states** — Use `hx-indicator` with Spinner or Loader components
6. **Handle errors** — Return error fragments from your routes

---

## See Also

- [Validation Guide](../guides/validation.md)
- [Error Handling Guide](../guides/error-handling.md)
- [Preset Reference](../presets/index.md)
