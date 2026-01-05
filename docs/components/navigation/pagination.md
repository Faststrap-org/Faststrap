# Pagination

The `Pagination` component creates page navigation controls for browsing through large datasets. Essential for tables, search results, and any content split across multiple pages.

!!! success "Goal"
    Master creating pagination controls, understand Bootstrap pagination classes, and build intuitive page navigation that helps users explore content efficiently.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Pagination Documentation](https://getbootstrap.com/docs/5.3/components/pagination/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#">Previous</a></li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active" aria-current="page"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">Next</a></li>
      </ul>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Pagination

Pagination(
    current_page=2,
    total_pages=10
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Sizes - Match Your Design

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="Large pagination" class="mb-3">
      <ul class="pagination pagination-lg">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
    <nav aria-label="Default pagination" class="mb-3">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
    <nav aria-label="Small pagination">
      <ul class="pagination pagination-sm">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
# Large - prominent pagination
Pagination(current_page=2, total_pages=10, size="lg")

# Default - standard use
Pagination(current_page=2, total_pages=10)

# Small - compact tables
Pagination(current_page=2, total_pages=10, size="sm")
```
  </div>
</div>

---

### 2. Alignment - Position Controls

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="Left aligned" class="mb-3">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
    <nav aria-label="Center aligned" class="mb-3">
      <ul class="pagination justify-content-center">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
    <nav aria-label="Right aligned">
      <ul class="pagination justify-content-end">
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
      </ul>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
# Left aligned (default)
Pagination(current_page=2, total_pages=10, align="start")

# Center aligned
Pagination(current_page=2, total_pages=10, align="center")

# Right aligned
Pagination(current_page=2, total_pages=10, align="end")
```
  </div>
</div>

---

### 3. First/Last Buttons - Quick Navigation

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="Pagination with first/last">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#">«</a></li>
        <li class="page-item"><a class="page-link" href="#">‹</a></li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item active"><span class="page-link">2</span></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">›</a></li>
        <li class="page-item"><a class="page-link" href="#">»</a></li>
      </ul>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
Pagination(
    current_page=2,
    total_pages=100,
    show_first_last=True,  # ← Adds « and » buttons
    show_prev_next=True    # ← Adds ‹ and › buttons (default)
)
```
  </div>
</div>

---

## Practical Functionality

### HTMX Integration - Dynamic Page Loading

Load pages dynamically without full page refresh.

```python
from faststrap import Pagination, Table, Card

@app.get("/")
def home():
    return Card(
        Div(id="data-table", hx_get="/page/1", hx_trigger="load"),
        Div(id="pagination-controls"),
        header="Product Catalog"
    )

@app.get("/page/{page}")
def load_page(page: int):
    # Get data for this page
    products = get_products(page=page, per_page=20)
    total_pages = get_total_pages(per_page=20)
    
    # Return table and pagination
    return Div(
        Table(
            THead(Tr(Th("Name"), Th("Price"), Th("Stock"))),
            TBody(*[
                Tr(Td(p.name), Td(f"${p.price}"), Td(p.stock))
                for p in products
            ]),
            id="data-table"
        ),
        Pagination(
            current_page=page,
            total_pages=total_pages,
            base_url="/page",
            align="center",
            hx_get=True,  # Use HTMX for page clicks
            hx_target="#data-table",
            hx_swap="outerHTML",
            id="pagination-controls"
        )
    )
```

---

### Search Results Pagination

```python
@app.get("/search")
def search(q: str, page: int = 1):
    results = search_database(q, page=page, per_page=10)
    total_pages = calculate_total_pages(q, per_page=10)
    
    return Div(
        H4(f"Search results for '{q}'"),
        Div(*[result_card(r) for r in results]),
        Pagination(
            current_page=page,
            total_pages=total_pages,
            base_url=f"/search?q={q}",
            align="center",
            max_pages=7  # Show max 7 page numbers
        ),
        cls="container my-4"
    )
```

---

### Infinite Scroll Alternative

Provide pagination as fallback for infinite scroll.

```python
@app.get("/feed")
def feed(page: int = 1):
    posts = get_posts(page=page, per_page=20)
    total_pages = get_total_pages(per_page=20)
    
    return Div(
        # Posts
        Div(
            *[post_card(p) for p in posts],
            id="posts-container"
        ),
        
        # Pagination (fallback if JS disabled)
        Pagination(
            current_page=page,
            total_pages=total_pages,
            base_url="/feed",
            align="center",
            cls="mt-4"
        ),
        
        # Infinite scroll trigger (if JS enabled)
        Div(
            id="load-more-trigger",
            hx_get=f"/feed?page={page+1}",
            hx_trigger="revealed",
            hx_swap="beforebegin",
            hx_target="#posts-container"
        ) if page < total_pages else None
    )
```

---

## Bootstrap CSS Classes Explained

### Core Pagination Classes

| Class | Purpose | Applied To |
|-------|---------|------------|
| `.pagination` | **Container** - Styles the list | `<ul>` element |
| `.pagination-lg` | **Large size** - Bigger buttons | `<ul>` element |
| `.pagination-sm` | **Small size** - Compact buttons | `<ul>` element |
| `.page-item` | **Item wrapper** - Wraps each link | `<li>` elements |
| `.page-link` | **Link styling** - Styles the clickable area | `<a>` or `<span>` |
| `.page-item.active` | **Active state** - Current page | `<li>` element |
| `.page-item.disabled` | **Disabled state** - Non-clickable | `<li>` element |

### Alignment Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.justify-content-start` | **Left align** - Default position | Aligns to left |
| `.justify-content-center` | **Center align** - Center position | Centers pagination |
| `.justify-content-end` | **Right align** - Right position | Aligns to right |

### State Classes

| Class | Purpose | Visual Effect |
|-------|---------|---------------|
| `.active` | Current page | Blue background, white text |
| `.disabled` | Non-clickable item | Grayed out, no hover |

---

## Responsive Pagination Patterns

### Mobile-Friendly Pagination

```python
from faststrap import Pagination

# Show fewer pages on mobile
def ResponsivePagination(current: int, total: int):
    return Div(
        # Desktop - show more pages
        Pagination(
            current_page=current,
            total_pages=total,
            max_pages=7,
            show_first_last=True,
            cls="d-none d-md-flex"
        ),
        # Mobile - show fewer pages
        Pagination(
            current_page=current,
            total_pages=total,
            max_pages=3,
            show_first_last=False,
            size="sm",
            cls="d-md-none"
        )
    )
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

```python
from faststrap import set_component_defaults, Pagination

# All pagination centered with first/last buttons
set_component_defaults("Pagination", 
                      align="center", 
                      show_first_last=True,
                      max_pages=7)

# Now all pagination inherits these defaults
Pagination(current_page=5, total_pages=20)
# ↑ Automatically centered with first/last buttons

# Override when needed
Pagination(current_page=1, total_pages=5, align="start", show_first_last=False)
```

**Common Default Patterns:**

```python
# Data tables - compact pagination
set_component_defaults("Pagination", size="sm", align="end")

# Search results - centered pagination
set_component_defaults("Pagination", align="center", max_pages=9)

# Admin panels - large, prominent pagination
set_component_defaults("Pagination", size="lg", show_first_last=True)
```

---

## Common Recipes

### The "Page Info" Pattern

Show current page info alongside pagination.

```python
def PaginationWithInfo(current: int, total: int, total_items: int):
    start = (current - 1) * 20 + 1
    end = min(current * 20, total_items)
    
    return Div(
        Div(
            f"Showing {start}-{end} of {total_items} items",
            cls="text-muted small mb-2"
        ),
        Pagination(
            current_page=current,
            total_pages=total,
            align="center"
        )
    )
```

---

### The "Per Page Selector" Pattern

Let users choose items per page.

```python
from faststrap import Select, Pagination

def PaginationWithPerPage(current: int, total_items: int, per_page: int = 20):
    total_pages = (total_items + per_page - 1) // per_page
    
    return Div(
        Div(
            Select(
                "per_page",
                ("10", "10 per page"),
                ("20", "20 per page", per_page == 20),
                ("50", "50 per page"),
                ("100", "100 per page"),
                hx_get="/update-pagination",
                hx_target="#pagination-container",
                cls="form-select-sm"
            ),
            Pagination(
                current_page=current,
                total_pages=total_pages,
                align="center"
            ),
            cls="d-flex justify-content-between align-items-center"
        ),
        id="pagination-container"
    )
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility:

✅ **Automatic Features:**
- `aria-label="Page navigation"` on `<nav>`
- `aria-current="page"` on active page
- `aria-label` on first/last/prev/next buttons
- Semantic `<nav>` structure

**Manual Enhancements:**

```python
Pagination(
    current_page=5,
    total_pages=20,
    aria_label="Product listing navigation"  # Custom context
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `current_page` | `int` | Required | Current active page (1-indexed) |
| `total_pages` | `int` | Required | Total number of pages |
| `size` | `"sm" \| "lg" \| None` | `None` | Pagination size |
| `align` | `"start" \| "center" \| "end"` | `"start"` | Alignment |
| `max_pages` | `int \| None` | `5` | Maximum page numbers to show |
| `base_url` | `str \| None` | `"#"` | Base URL for page links |
| `show_first_last` | `bool \| None` | `False` | Show first/last page buttons |
| `show_prev_next` | `bool \| None` | `True` | Show previous/next buttons |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, id, hx-*) |

::: faststrap.components.navigation.pagination.Pagination
    options:
        show_source: true
        heading_level: 4
