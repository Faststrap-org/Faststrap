# Breadcrumb

The `Breadcrumb` component creates navigation trails that show users their current location in your site hierarchy. Essential for deep navigation structures and improving user orientation.

!!! success "Goal"
    Master creating breadcrumb navigation, understand Bootstrap breadcrumb classes, and build intuitive navigation trails that help users never get lost.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Breadcrumb Documentation](https://getbootstrap.com/docs/5.3/components/breadcrumb/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="#">Home</a></li>
        <li class="breadcrumb-item"><a href="#">Products</a></li>
        <li class="breadcrumb-item active" aria-current="page">Laptops</li>
      </ol>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Breadcrumb

Breadcrumb(
    ("Home", "/"),
    ("Products", "/products"),
    ("Laptops", None)  # None = active/current page
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. With Icons - Enhanced Visual Hierarchy

Add icons to breadcrumb items for better visual recognition.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="#"><i class="bi bi-house-fill me-1"></i>Home</a>
        </li>
        <li class="breadcrumb-item">
          <a href="#"><i class="bi bi-folder me-1"></i>Documents</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
          <i class="bi bi-file-earmark me-1"></i>Report.pdf
        </li>
      </ol>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Breadcrumb, Icon

Breadcrumb(
    (Div(Icon("house-fill"), " Home"), "/"),
    (Div(Icon("folder"), " Documents"), "/documents"),
    (Div(Icon("file-earmark"), " Report.pdf"), None)
)
```
  </div>
</div>

---

### 2. Styled Breadcrumbs - Custom Appearance

Customize breadcrumb styling with Bootstrap utility classes.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <nav aria-label="breadcrumb" class="mb-3">
      <ol class="breadcrumb bg-light p-3 rounded">
        <li class="breadcrumb-item"><a href="#" class="text-decoration-none">Home</a></li>
        <li class="breadcrumb-item"><a href="#" class="text-decoration-none">Library</a></li>
        <li class="breadcrumb-item active" aria-current="page">Data</li>
      </ol>
    </nav>
    <nav aria-label="breadcrumb" class="mb-3">
      <ol class="breadcrumb bg-primary bg-opacity-10 p-3 rounded border border-primary">
        <li class="breadcrumb-item"><a href="#" class="text-primary fw-bold">Dashboard</a></li>
        <li class="breadcrumb-item"><a href="#" class="text-primary fw-bold">Analytics</a></li>
        <li class="breadcrumb-item active text-primary" aria-current="page">Reports</li>
      </ol>
    </nav>
  </div>
  <div class="preview-code" markdown>
```python
# Light background with padding
Breadcrumb(
    ("Home", "/"),
    ("Library", "/library"),
    ("Data", None),
    cls="bg-light p-3 rounded"
)

# Primary themed breadcrumb
Breadcrumb(
    ("Dashboard", "/dashboard"),
    ("Analytics", "/analytics"),
    ("Reports", None),
    cls="bg-primary bg-opacity-10 p-3 rounded border border-primary"
)
```
  </div>
</div>

---

### 3. Responsive Breadcrumbs - Mobile-Friendly

Show abbreviated breadcrumbs on mobile devices.

```python
from faststrap import Breadcrumb
from fasthtml.common import Div

def ResponsiveBreadcrumb(*items):
    # Full breadcrumb for desktop
    full_breadcrumb = Breadcrumb(*items, cls="d-none d-md-flex")
    
    # Abbreviated for mobile (only show last 2 items)
    mobile_items = items[-2:] if len(items) > 2 else items
    mobile_breadcrumb = Breadcrumb(*mobile_items, cls="d-md-none")
    
    return Div(full_breadcrumb, mobile_breadcrumb)

# Usage
ResponsiveBreadcrumb(
    ("Home", "/"),
    ("Products", "/products"),
    ("Electronics", "/products/electronics"),
    ("Laptops", "/products/electronics/laptops"),
    ("Gaming", None)
)
```

---

## Practical Functionality

### Dynamic Breadcrumbs from URL Path

Automatically generate breadcrumbs from the current URL.

```python
from faststrap import Breadcrumb
from fasthtml.common import Request

def auto_breadcrumb(request: Request):
    path = request.url.path
    parts = [p for p in path.split('/') if p]
    
    items = [("Home", "/")]
    current_path = ""
    
    for i, part in enumerate(parts):
        current_path += f"/{part}"
        label = part.replace('-', ' ').title()
        
        # Last item is active (no href)
        if i == len(parts) - 1:
            items.append((label, None))
        else:
            items.append((label, current_path))
    
    return Breadcrumb(*items)

# Usage in route
@app.get("/products/electronics/laptops")
def laptops_page(request: Request):
    return Div(
        auto_breadcrumb(request),  # Generates: Home > Products > Electronics > Laptops
        # Page content...
    )
```

---

### Breadcrumbs with Dropdowns

Add dropdown menus to breadcrumb items for quick navigation to siblings.

```python
from faststrap import Breadcrumb, Dropdown, DropdownItem
from fasthtml.common import Div, A

def BreadcrumbWithDropdown():
    return Div(
        Div(
            A("Home", href="/", cls="breadcrumb-item"),
            " / ",
            Dropdown(
                DropdownItem("Electronics", href="/products/electronics"),
                DropdownItem("Clothing", href="/products/clothing"),
                DropdownItem("Books", href="/products/books"),
                label="Products",
                variant="link",
                size="sm",
                toggle_cls="breadcrumb-item text-decoration-none p-0"
            ),
            " / ",
            Span("Laptops", cls="breadcrumb-item active"),
            cls="d-flex align-items-center"
        ),
        cls="breadcrumb"
    )
```

---

## Bootstrap CSS Classes Explained

### Core Breadcrumb Classes

| Class | Purpose | Applied To |
|-------|---------|------------|
| `.breadcrumb` | **Container** - Styles the ordered list | `<ol>` element |
| `.breadcrumb-item` | **Item** - Styles each breadcrumb link | `<li>` elements |
| `.breadcrumb-item.active` | **Active state** - Current page indicator | Last `<li>` element |

### Separator Customization

Bootstrap uses CSS `::before` pseudo-element for separators. Customize via CSS variables:

```css
/* Change separator */
.breadcrumb {
  --bs-breadcrumb-divider: '>';
}

/* Use icon as separator */
.breadcrumb {
  --bs-breadcrumb-divider: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cpath d='M2.5 0L1 1.5 3.5 4 1 6.5 2.5 8l4-4-4-4z' fill='currentColor'/%3E%3C/svg%3E");
}

/* Remove separator */
.breadcrumb {
  --bs-breadcrumb-divider: '';
}
```

### Styling Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.bg-light` | **Background** - Light gray background | Visual container |
| `.p-3` | **Padding** - Adds spacing | More prominent |
| `.rounded` | **Corners** - Rounded borders | Softer appearance |
| `.border` | **Border** - Adds border | Defined container |
| `.text-decoration-none` | **No underline** - Removes link underline | Cleaner look |

---

## Responsive Breadcrumb Patterns

### Collapsible Breadcrumbs

Show only essential items on mobile, expand on desktop.

```python
from faststrap import Breadcrumb, Dropdown

def CollapsibleBreadcrumb(*items):
    if len(items) <= 3:
        return Breadcrumb(*items)
    
    # On mobile: Home > ... > Current
    # On desktop: Full path
    first = items[0]
    last = items[-1]
    middle = items[1:-1]
    
    return Div(
        # Mobile version
        Breadcrumb(
            first,
            ("...", None),  # Ellipsis
            last,
            cls="d-md-none"
        ),
        # Desktop version
        Breadcrumb(*items, cls="d-none d-md-flex")
    )
```

---

## Core Faststrap Features

### Using with Layouts

Breadcrumbs work great in page headers and dashboard layouts.

```python
from faststrap import DashboardLayout, Breadcrumb, Card

@app.get("/dashboard/analytics/reports")
def reports_page():
    breadcrumb = Breadcrumb(
        ("Dashboard", "/dashboard"),
        ("Analytics", "/dashboard/analytics"),
        ("Reports", None)
    )
    
    return DashboardLayout(
        breadcrumb,
        Card("Report content here..."),
        title="Reports"
    )
```

---

## Common Recipes

### The "Back Button" Alternative

Use breadcrumbs instead of generic "Back" buttons for better context.

```python
# ❌ Generic back button - where does it go?
Button("← Back", variant="link")

# ✅ Breadcrumb - shows exact path
Breadcrumb(
    ("Products", "/products"),
    ("Laptops", "/products/laptops"),
    ("Dell XPS 15", None)
)
```

---

### E-commerce Product Navigation

```python
def ProductBreadcrumb(category: str, subcategory: str, product: str):
    return Breadcrumb(
        (Icon("house-fill"), "/"),
        (category, f"/category/{category.lower()}"),
        (subcategory, f"/category/{category.lower()}/{subcategory.lower()}"),
        (product, None),
        cls="mb-4"
    )

# Usage
ProductBreadcrumb("Electronics", "Laptops", "Dell XPS 15")
```

---

### Documentation Site Navigation

```python
def DocsBreadcrumb(section: str, page: str):
    return Breadcrumb(
        ("Docs", "/docs"),
        (section, f"/docs/{section.lower()}"),
        (page, None),
        cls="bg-light p-2 rounded mb-4"
    )

# Usage
DocsBreadcrumb("Components", "Button")
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility:

✅ **Automatic Features:**
- `aria-label="breadcrumb"` on `<nav>` element
- `aria-current="page"` on active item
- Semantic `<nav>` and `<ol>` structure
- Proper link hierarchy

**Manual Enhancements:**

```python
# Custom aria-label for context
Breadcrumb(
    ("Home", "/"),
    ("Products", "/products"),
    ("Laptops", None),
    aria_label="Product category navigation"
)
```

---

## Parameter Reference

| Parameter | Type | Description |
|-----------|------|-------------|
| `*items` | `tuple` | Breadcrumb items as `(label, href)` or `(label, href, active)` |
| `**kwargs` | `Any` | Additional HTML attributes (cls, id, aria-*, style) |

**Item Format:**
- `(label, href)` - Link item (href can be string or None for active)
- `(label, href, active)` - Explicitly set active state (True/False)
- Last item is automatically marked as active if not specified

::: faststrap.components.navigation.breadcrumb.Breadcrumb
    options:
        show_source: true
        heading_level: 4
