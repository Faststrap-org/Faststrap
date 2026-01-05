# Drawer (Offcanvas)

The `Drawer` component creates sliding side panels for navigation menus, settings, and additional content. Perfect for mobile-friendly navigation and contextual information displays.

!!! success "Goal"
    Master creating drawer panels, understand Bootstrap offcanvas classes, and build responsive navigation that works beautifully on all screen sizes.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Offcanvas Documentation](https://getbootstrap.com/docs/5.3/components/offcanvas/)

---

## Quick Start

```python
from faststrap import Drawer, Button

# Button to trigger drawer
Button(
    "Open Menu",
    variant="primary",
    data_bs_toggle="offcanvas",
    data_bs_target="#myDrawer"
)

# Drawer component
Drawer(
    ListGroup(
        ListGroupItem("Home", href="/"),
        ListGroupItem("About", href="/about"),
        ListGroupItem("Contact", href="/contact")
    ),
    drawer_id="myDrawer",
    title="Navigation",
    placement="start"  # Left side
)
```

---

## Visual Examples & Use Cases

### 1. Placements - Four Directions

```python
# Left drawer (default)
Drawer(content, drawer_id="left", title="Left Menu", placement="start")

# Right drawer
Drawer(content, drawer_id="right", title="Right Menu", placement="end")

# Top drawer
Drawer(content, drawer_id="top", title="Top Panel", placement="top")

# Bottom drawer
Drawer(content, drawer_id="bottom", title="Bottom Panel", placement="bottom")
```

---

### 2. Mobile Navigation Menu

```python
from faststrap import Drawer, ListGroup, ListGroupItem, Icon, Button

# Trigger button
Button(
    Icon("list"),
    variant="outline-primary",
    data_bs_toggle="offcanvas",
    data_bs_target="#mobileNav"
)

# Drawer
Drawer(
    ListGroup(
        ListGroupItem(Icon("house"), " Home", href="/", action=True),
        ListGroupItem(Icon("grid"), " Products", href="/products", action=True),
        ListGroupItem(Icon("info-circle"), " About", href="/about", action=True),
        ListGroupItem(Icon("envelope"), " Contact", href="/contact", action=True),
        flush=True
    ),
    drawer_id="mobileNav",
    title="Menu",
    placement="start"
)
```

---

### 3. Settings Panel

```python
Drawer(
    H5("Preferences"),
    Switch("dark_mode", label="Dark Mode"),
    Switch("notifications", label="Notifications"),
    Select(
        "language",
        ("en", "English"),
        ("es", "Spanish"),
        label="Language"
    ),
    Button("Save", variant="primary", cls="w-100 mt-3"),
    drawer_id="settings",
    title="Settings",
    placement="end"
)
```

---

## Bootstrap CSS Classes Explained

| Class | Purpose |
|-------|---------|
| `.offcanvas` | Base drawer container |
| `.offcanvas-start` | Left placement |
| `.offcanvas-end` | Right placement |
| `.offcanvas-top` | Top placement |
| `.offcanvas-bottom` | Bottom placement |
| `.offcanvas-header` | Drawer header |
| `.offcanvas-body` | Drawer content |
| `.offcanvas-title` | Title text |

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Drawer body content |
| `drawer_id` | `str \| None` | Auto-generated | Unique ID for drawer |
| `title` | `str \| None` | `None` | Drawer header title |
| `placement` | `"start" \| "end" \| "top" \| "bottom"` | `"start"` | Drawer position |
| `backdrop` | `bool \| None` | `True` | Show backdrop overlay |
| `scroll` | `bool \| None` | `False` | Allow body scroll when open |
| `dark` | `bool \| None` | `False` | Dark variant |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.navigation.drawer.Drawer
    options:
        show_source: true
        heading_level: 4
