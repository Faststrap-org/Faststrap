# LoadingButton

Button with automatic loading state during HTMX requests. Shows a spinner and disables during the request. Uses HTMX's built-in `hx-indicator` and `hx-disabled-elt` attributes — zero JavaScript.

!!! success "Stability: Stable"
    This component is stable and ready for production use.

## Usage

```python
from faststrap.presets import LoadingButton

LoadingButton(
    "Save Changes",
    endpoint="/api/save",
    target="#result",
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | | Button content (text, icons) |
| `endpoint` | `str` | **required** | Server endpoint for the request |
| `method` | `str` | `"post"` | HTTP method (get, post, put, delete) |
| `target` | `str` | `None` | CSS selector for response target |
| `variant` | `str` | `"primary"` | Bootstrap button variant |
| `**kwargs` | | | Additional HTML/HTMX attrs |

## Examples

### POST with Confirmation

```python
LoadingButton(
    "Delete Account",
    endpoint="/api/delete-account",
    method="delete",
    variant="danger",
    hx_confirm="Are you sure? This cannot be undone.",
)
```

### GET Request

```python
LoadingButton(
    "Load More",
    endpoint="/api/items?page=2",
    method="get",
    target="#items-list",
    variant="outline-primary",
)
```
