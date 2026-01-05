# DashboardLayout

The `DashboardLayout` component provides a production-ready admin panel layout with responsive sidebar, top navigation, and content area. Perfect for building admin dashboards, control panels, and internal tools.

!!! success "Goal"
    Quickly build professional admin interfaces with a responsive sidebar, navigation, and content structure.

---

## Quick Start

```python
from faststrap import DashboardLayout, ListGroupItem

DashboardLayout(
    # Main content
    H1("Dashboard"),
    Card("Your content here"),
    
    # Configuration
    title="My Admin",
    sidebar_items=[
        ListGroupItem("Dashboard", href="/", active=True),
        ListGroupItem("Users", href="/users"),
        ListGroupItem("Settings", href="/settings")
    ]
)
```

---

## Features

- **Responsive sidebar** - Collapses on mobile
- **Top navigation bar** - With user menu support
- **Breadcrumbs support** - Show navigation path
- **Footer support** - Optional footer content
- **Theme support** - Light or dark mode
- **Customizable width** - Adjust sidebar width

---

## Complete Example

```python
from faststrap import DashboardLayout, ListGroupItem, Dropdown, DropdownItem, StatCard, Row, Col

@app.get("/")
def dashboard():
    return DashboardLayout(
        # Main content
        Row(
            Col(StatCard("Users", "1,234", variant="primary"), md=3),
            Col(StatCard("Revenue", "$12,345", variant="success"), md=3),
            Col(StatCard("Orders", "567", variant="info"), md=3),
            Col(StatCard("Visitors", "8,901", variant="warning"), md=3)
        ),
        Card(
            Table(...),  # Your data table
            header="Recent Orders"
        ),
        
        # Sidebar navigation
        sidebar_items=[
            ListGroupItem(Icon("house"), " Dashboard", href="/", active=True),
            ListGroupItem(Icon("people"), " Users", href="/users"),
            ListGroupItem(Icon("box"), " Products", href="/products"),
            ListGroupItem(Icon("graph-up"), " Analytics", href="/analytics"),
            ListGroupItem(Icon("gear"), " Settings", href="/settings")
        ],
        
        # User menu
        user=Dropdown(
            DropdownItem("Profile", href="/profile"),
            DropdownItem("Settings", href="/settings"),
            "---",
            DropdownItem("Logout", href="/logout"),
            label="Admin User",
            variant="link"
        ),
        
        # Page title
        title="Admin Panel",
        
        # Footer
        footer="© 2026 My Company. All rights reserved."
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*content` | `Any` | Required | Main content area components |
| `title` | `str` | `"Dashboard"` | Page title |
| `sidebar_items` | `list[Any] \| None` | `None` | Sidebar navigation items |
| `user` | `Any \| None` | `None` | User dropdown/profile component |
| `breadcrumbs` | `list[tuple] \| None` | `None` | Breadcrumb navigation |
| `footer` | `str \| Any \| None` | `None` | Footer content |
| `sidebar_width` | `str` | `"250px"` | Sidebar width on desktop |
| `theme` | `str` | `"light"` | Layout theme (light/dark) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.layouts.dashboard.DashboardLayout
    options:
        show_source: true
        heading_level: 4
