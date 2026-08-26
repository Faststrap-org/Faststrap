# Searchable Select

The `SearchableSelect` component creates a server-side searchable dropdown using HTMX, replacing client-side libraries with pure server-side filtering.

## Quick Start

```python
SearchableSelect(endpoint="/api/users/search", name="user_id", placeholder="Search users...", csp_safe=True)
```

## Usage Scenarios

### User Selection

```python
SearchableSelect(
    endpoint="/api/users/search",
    name="assigned_to",
    select_id="assigned_to",
    placeholder="Search by name or email...",
    debounce=300,
    csp_safe=True
)
```

### Country/Location Selection

```python
SearchableSelect(
    endpoint="/api/countries/search",
    name="country",
    placeholder="Search countries...",
    initial_options=[
        ("us", "United States"),
        ("uk", "United Kingdom"),
        ("ca", "Canada"),
    ]
)
```

### Product Search

```python
SearchableSelect(
    endpoint="/api/products/search",
    name="product_id",
    placeholder="Search products...",
    min_chars=3,
    debounce=400
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `endpoint` | `str` | Required | Server endpoint for search (receives 'q' param) |
| `name` | `str` | Required | Form field name |
| `placeholder` | `str` | "Search..." | Search input placeholder |
| `initial_options` | `list[tuple]` | `None` | Initial options as (value, text) tuples |
| `debounce` | `int` | 300 | Milliseconds to wait after typing |
| `min_chars` | `int` | 2 | Minimum characters before triggering search |
| `select_id` | `str \| None` | Auto | Unique ID for the select element |
| `csp_safe` | `bool \| None` | `None` | Recommended production mode that avoids inline JavaScript |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Search input has proper `aria` attributes.
- Results are returned as semantic `<a>` elements with list-group styling.
- `csp_safe=True` avoids inline click handlers for strict Content Security Policy compliance.

## API Reference

::: faststrap.components.forms.searchable_select.SearchableSelect
    options:
        show_source: true
        heading_level: 4
