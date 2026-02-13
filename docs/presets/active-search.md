# ActiveSearch

Live search input with debounced server requests. Replaces React search components, Vue debounce scripts, and Alpine live search hacks.

!!! success "Stability: Stable"
    This component is stable and ready for production use.

## Usage

```python
from faststrap.presets import ActiveSearch

ActiveSearch(
    endpoint="/api/search",
    target="#results",
    placeholder="Search users...",
    debounce=300,
)
```

## Generated HTML

```html
<input
  type="search"
  class="form-control"
  hx-get="/api/search"
  hx-target="#results"
  hx-trigger="keyup changed delay:300ms"
  placeholder="Search users..."
  name="q"
/>
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | **required** | Server endpoint for search requests |
| `target` | `str` | **required** | CSS selector for results container |
| `debounce` | `int` | `300` | Milliseconds to wait after typing |
| `placeholder` | `str` | `"Search..."` | Input placeholder text |
| `name` | `str` | `"q"` | Form field name for query |
| `**kwargs` | | | Additional HTML/HTMX attributes |

## Server Endpoint

Your search endpoint receives the query as a form parameter:

```python
@app.get("/api/search")
def search(q: str = ""):
    if len(q) < 2:
        return ""

    results = [u for u in USERS if q.lower() in u["name"].lower()]
    return Div(*[Card(u["name"]) for u in results])
```

## Advanced Options

Override HTMX behavior with kwargs:

```python
ActiveSearch(
    endpoint="/api/search",
    target="#results",
    hx_indicator="#spinner",    # Show spinner during request
    hx_swap="innerHTML",        # Custom swap strategy
    cls="form-control-lg",      # Custom classes
)
```
