# Icon

The `Icon` component provides easy access to Bootstrap Icons, the official icon library with 2,000+ high-quality SVG icons. Perfect for enhancing buttons, navigation, and UI elements.

!!! success "Goal"
    Master using Bootstrap Icons in your Faststrap applications with simple, Pythonic syntax.

!!! tip "Bootstrap Icons"
    [Browse all 2,000+ icons](https://icons.getbootstrap.com/)

---

## Quick Start

```python
from faststrap import Icon

# Basic icon
Icon("heart")

# Icon with color
Icon("heart-fill", cls="text-danger")

# Icon in button
Button(Icon("download"), " Download", variant="primary")
```

---

## Common Use Cases

### 1. In Buttons

```python
from faststrap import Button, Icon

Button(Icon("plus"), " Add New", variant="success")
Button(Icon("trash"), " Delete", variant="danger")
Button(Icon("pencil"), " Edit", variant="primary")
```

---

### 2. In Navigation

```python
from faststrap import ListGroup, ListGroupItem, Icon

ListGroup(
    ListGroupItem(Icon("house"), " Home", href="/"),
    ListGroupItem(Icon("gear"), " Settings", href="/settings"),
    ListGroupItem(Icon("person"), " Profile", href="/profile")
)
```

---

### 3. Status Indicators

```python
# Success
Icon("check-circle-fill", cls="text-success")

# Error
Icon("x-circle-fill", cls="text-danger")

# Warning
Icon("exclamation-triangle-fill", cls="text-warning")

# Info
Icon("info-circle-fill", cls="text-info")
```

---

### 4. Sizes

```python
# Small
Icon("star", cls="fs-6")

# Medium (default)
Icon("star")

# Large
Icon("star", cls="fs-3")

# Extra Large
Icon("star", cls="fs-1")
```

---

## Popular Icons

| Icon Name | Use Case |
|-----------|----------|
| `house`, `house-fill` | Home navigation |
| `gear`, `gear-fill` | Settings |
| `person`, `person-fill` | User profile |
| `envelope`, `envelope-fill` | Email/messages |
| `heart`, `heart-fill` | Favorites/likes |
| `star`, `star-fill` | Ratings |
| `cart`, `cart-fill` | Shopping cart |
| `search` | Search functionality |
| `plus`, `plus-circle` | Add/create |
| `trash`, `trash-fill` | Delete |
| `pencil`, `pencil-fill` | Edit |
| `download` | Download |
| `upload` | Upload |
| `check`, `check-circle` | Success/complete |
| `x`, `x-circle` | Close/error |
| `arrow-left`, `arrow-right` | Navigation |
| `list` | Menu |
| `three-dots-vertical` | More options |

---

## Parameter Reference

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Icon name from Bootstrap Icons (e.g., 'heart', 'star-fill') |
| `**kwargs` | `Any` | Additional attributes (cls, style, etc.) |

**Note**: Icon names use the Bootstrap Icons naming convention. Visit [icons.getbootstrap.com](https://icons.getbootstrap.com/) to browse all available icons.

::: faststrap.utils.icons.Icon
    options:
        show_source: true
        heading_level: 4
