# InfiniteScroll

Infinite scroll trigger element. Loads more content when scrolled into view. Replaces IntersectionObserver JavaScript.

!!! success "Stability: Stable"
    This component is stable and ready for production use.

## Usage

```python
from faststrap.presets import InfiniteScroll

InfiniteScroll(
    endpoint="/api/feed?page=2",
    target="#feed",
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | **required** | Endpoint to fetch next page |
| `target` | `str` | **required** | CSS selector for results container |
| `trigger` | `str` | `"revealed"` | HTMX trigger event |
| `threshold` | `str` | `"0px"` | Intersection observer threshold |
| `content` | `Any` | Loading indicator | Custom loading content |
| `**kwargs` | | | Additional HTML/HTMX attrs |

## Server Endpoint

Return HTML content + a new trigger for the next page:

```python
@app.get("/api/feed")
def feed(page: int = 1):
    items = get_items(page=page, per_page=10)
    result = [Card(item.title) for item in items]

    if has_more_pages(page):
        result.append(
            InfiniteScroll(
                endpoint=f"/api/feed?page={page + 1}",
                target="#feed",
            )
        )

    return Div(*result)
```

## With Custom Threshold

Trigger loading 200px before the element is visible:

```python
InfiniteScroll(
    endpoint="/api/feed?page=2",
    target="#feed",
    threshold="200px",
)
```
