# LazyLoad

Lazy-loaded content block. Loads content from the server when scrolled into view. Replaces JavaScript image loaders and dynamic content scripts.

!!! success "Stability: Stable"
    This component is stable and ready for production use.

## Usage

```python
from faststrap.presets import LazyLoad

LazyLoad(endpoint="/api/heavy-widget")
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | **required** | Server endpoint to fetch content |
| `trigger` | `str` | `"revealed"` | HTMX trigger event |
| `placeholder` | `Any` | Loading text | Content to show before loading |
| `**kwargs` | | | Additional HTML/HTMX attrs |

## Custom Placeholder

```python
from faststrap import Spinner

LazyLoad(
    endpoint="/api/chart",
    placeholder=Spinner(),
)
```

## Load on Click

```python
LazyLoad(
    endpoint="/api/details",
    trigger="click",
    placeholder=Button("Load Details"),
)
```

!!! tip
    Perfect for below-the-fold content, charts, or heavy components that would slow initial page load.
