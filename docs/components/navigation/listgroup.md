# ListGroup

The `ListGroup` component creates flexible, versatile lists for displaying content, navigation, and custom interfaces. Perfect for sidebars, settings panels, and any structured content display.

!!! success "Goal"
    Master creating list groups with various styles, understand Bootstrap list-group classes, and build organized content displays that enhance user navigation.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 List Group Documentation](https://getbootstrap.com/docs/5.3/components/list-group/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <ul class="list-group">
      <li class="list-group-item">First item</li>
      <li class="list-group-item">Second item</li>
      <li class="list-group-item">Third item</li>
    </ul>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import ListGroup, ListGroupItem

ListGroup(
    ListGroupItem("First item"),
    ListGroupItem("Second item"),
    ListGroupItem("Third item")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Active and Disabled Items

```python
ListGroup(
    ListGroupItem("Active item", active=True),
    ListGroupItem("Normal item"),
    ListGroupItem("Disabled item", disabled=True)
)
```

---

### 2. With Links - Interactive Lists

```python
ListGroup(
    ListGroupItem("Dashboard", href="/dashboard", action=True),
    ListGroupItem("Settings", href="/settings", action=True),
    ListGroupItem("Profile", href="/profile", action=True, active=True)
)
```

---

### 3. Color Variants

```python
ListGroup(
    ListGroupItem("Success", variant="success"),
    ListGroupItem("Danger", variant="danger"),
    ListGroupItem("Warning", variant="warning"),
    ListGroupItem("Info", variant="info")
)
```

---

### 4. With Badges

```python
from faststrap import ListGroup, ListGroupItem, Badge

ListGroup(
    ListGroupItem(
        "Inbox",
        badge=Badge("12", variant="primary"),
        href="/inbox",
        action=True
    ),
    ListGroupItem(
        "Drafts",
        badge=Badge("3", variant="secondary"),
        href="/drafts",
        action=True
    )
)
```

---

### 5. Flush Style - Edge-to-Edge

```python
ListGroup(
    ListGroupItem("Item 1"),
    ListGroupItem("Item 2"),
    ListGroupItem("Item 3"),
    flush=True  # ← Removes borders
)
```

---

### 6. Horizontal Lists

```python
# Horizontal on all screens
ListGroup(
    ListGroupItem("Left"),
    ListGroupItem("Center"),
    ListGroupItem("Right"),
    horizontal=True
)

# Horizontal on medium screens and up
ListGroup(
    ListGroupItem("Item 1"),
    ListGroupItem("Item 2"),
    horizontal="md"
)
```

---

## Bootstrap CSS Classes Explained

| Class | Purpose |
|-------|---------|
| `.list-group` | Container for list items |
| `.list-group-item` | Individual list item |
| `.list-group-item-action` | Hover/focus styles for interactive items |
| `.list-group-item-{variant}` | Color variants (success, danger, etc.) |
| `.list-group-flush` | Removes borders for edge-to-edge |
| `.list-group-horizontal` | Horizontal layout |
| `.active` | Active/selected state |
| `.disabled` | Disabled state |

---

## Common Recipes

### Settings Menu

```python
from faststrap import ListGroup, ListGroupItem, Icon

ListGroup(
    ListGroupItem(
        Icon("person"), " Profile",
        href="/settings/profile",
        action=True,
        active=True
    ),
    ListGroupItem(
        Icon("bell"), " Notifications",
        href="/settings/notifications",
        action=True
    ),
    ListGroupItem(
        Icon("shield-lock"), " Privacy",
        href="/settings/privacy",
        action=True
    ),
    flush=True
)
```

---

## Parameter Reference

### ListGroup

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | ListGroupItem components |
| `flush` | `bool` | `False` | Remove borders |
| `horizontal` | `bool \| str` | `False` | Horizontal layout (True or breakpoint) |
| `numbered` | `bool` | `False` | Numbered list |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### ListGroupItem

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Item content |
| `variant` | `VariantType \| None` | `None` | Color variant |
| `active` | `bool` | `False` | Active state |
| `disabled` | `bool` | `False` | Disabled state |
| `action` | `bool` | `False` | Enable hover/focus styles |
| `href` | `str \| None` | `None` | Make item a link |
| `badge` | `Any` | `None` | Badge to display |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.navigation.listgroup.ListGroup
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.navigation.listgroup.ListGroupItem
    options:
        show_source: true
        heading_level: 4
