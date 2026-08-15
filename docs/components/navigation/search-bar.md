# SearchBar

`@experimental`

Polished global search input with optional HTMX integration.

---

## Quick Start

```python
from faststrap import SearchBar

SearchBar("Search users...")
```

---

## Features

- Polished search input with optional icon prefix
- HTMX-powered live search with debouncing
- Works with any server-side search endpoint
- Accessible with proper ARIA attributes

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `placeholder` | `str` | `"Search..."` | Input placeholder text. |
| `endpoint` | `str \| None` | `None` | HTMX endpoint for search results. |
| `target` | `str \| None` | `None` | HTMX target selector for results. |
| `swap` | `str` | `"innerHTML"` | HTMX swap strategy. |
| `name` | `str` | `"q"` | Query parameter name. |
| `method` | `str` | `"get"` | HTTP method for search requests. |
| `autocomplete` | `str` | `"off"` | Input autocomplete attribute. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

---

## Usage Examples

### Basic Search Input

```python
SearchBar("Search users...")
```

### Live Search with HTMX

```python
SearchBar(
    "Search users...",
    endpoint="/api/users/search",
    target="#search-results",
)
```

### Custom Parameter Name

```python
SearchBar("Search...", name="query", endpoint="/api/search")
```

---

## Notes

- Pure HTML/CSS with optional HTMX enhancement.
- When `endpoint` is provided, the input submits automatically on input changes with 300ms debounce.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.navigation.search_bar.SearchBar
    options:
        show_source: true
        heading_level: 4
