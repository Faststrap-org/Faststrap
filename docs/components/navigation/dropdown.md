# Dropdown

The `Dropdown` component creates elegant contextual menus that appear on click. Perfect for navigation, actions, settings, and any interface where you need to reveal options without cluttering the UI.

!!! success "Goal"
    Master creating dropdown menus, understand Bootstrap's dropdown classes, and build dynamic, accessible navigation—all with zero custom JavaScript.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Dropdown Documentation](https://getbootstrap.com/docs/5.3/components/dropdowns/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="dropdown">
      <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Actions
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Edit</a></li>
        <li><a class="dropdown-item" href="#">Delete</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#">Archive</a></li>
      </ul>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Dropdown

Dropdown(
    "Edit",
    "Delete",
    "---",  # Divider
    "Archive",
    label="Actions",
    variant="primary"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Button Variants - Match Your Design

Dropdowns inherit all button variants for consistent theming.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2">
      <div class="dropdown">
        <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Primary
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropdown">
        <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Success
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropdown">
        <button class="btn btn-outline-danger dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Danger Outline
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Delete</a></li>
          <li><a class="dropdown-item" href="#">Remove</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Solid variants
Dropdown("Action", "Another action", label="Primary", variant="primary")
Dropdown("Action", "Another action", label="Success", variant="success")

# Outline variants (add outline=True to button via toggle_cls)
Dropdown("Delete", "Remove", label="Danger Outline", variant="danger",
         toggle_cls="btn-outline-danger")
```
  </div>
</div>

---

### 2. Dropdown Directions - Control Where Menus Appear

Control menu placement with the `direction` parameter. Essential for dropdowns near screen edges.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-3 justify-content-center">
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Dropdown (Down)
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropup">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Dropup (Up)
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropend">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Dropend (Right)
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropstart">
        <button class="btn btn-secondary dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown">
        </button>
        <button class="btn btn-secondary" type="button">
          Dropstart (Left)
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Down (default) - menu appears below button
Dropdown("Action", "Another action", label="Dropdown", direction="down")

# Up - menu appears above button (useful for bottom toolbars)
Dropdown("Action", "Another action", label="Dropup", direction="up")

# End (Right) - menu appears to the right
Dropdown("Action", "Another action", label="Dropend", direction="end")

# Start (Left) - menu appears to the left
Dropdown("Action", "Another action", label="Dropstart", direction="start")
```
  </div>
</div>

**When to use each direction:**

| Direction | Bootstrap Class | Use Case |
|-----------|----------------|----------|
| `down` | `.dropdown` | Default - most dropdowns |
| `up` | `.dropup` | Bottom navigation bars, footer actions |
| `end` | `.dropend` | Sidebar menus, nested navigation |
| `start` | `.dropstart` | Right-aligned sidebars, RTL layouts |

---

### 3. Split Button Dropdowns - Action + Options

Combine a primary action with additional options. The left button performs the default action, the right reveals more choices.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="btn-group">
      <button type="button" class="btn btn-primary">Save</button>
      <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
        <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Save and Close</a></li>
        <li><a class="dropdown-item" href="#">Save as Draft</a></li>
        <li><a class="dropdown-item" href="#">Save as Template</a></li>
      </ul>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Split button - left button is clickable action
Dropdown(
    "Save and Close",
    "Save as Draft",
    "Save as Template",
    label="Save",
    variant="primary",
    split=True  # ← Creates split button
)
```
  </div>
</div>

**Perfect for:**
- Save operations with variations
- Export with format options
- Send with delivery methods
- Delete with confirmation levels

---

### 4. Menu Alignment & Styling

Customize menu appearance with Bootstrap utility classes.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-2">
      <div class="dropdown">
        <button class="btn btn-info dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Dark Menu
        </button>
        <ul class="dropdown-menu dropdown-menu-dark">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item active" href="#">Active</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
          Right Aligned
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Dark menu theme
Dropdown(
    "Action", "Active", "Another action",
    label="Dark Menu",
    variant="info",
    menu_cls="dropdown-menu-dark"
)

# Right-aligned menu
Dropdown(
    "Action", "Another action",
    label="Right Aligned",
    variant="secondary",
    menu_cls="dropdown-menu-end"
)
```
  </div>
</div>

---

## Practical Functionality

### HTMX Integration - Dynamic Actions

Trigger server actions when dropdown items are clicked.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card shadow-sm">
      <div class="card-body">
        <div class="d-flex justify-content-between align-items-center">
          <h5 class="mb-0">Document.pdf</h5>
          <div class="dropdown">
            <button class="btn btn-sm btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
              Actions
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#"><i class="bi bi-download me-2"></i>Download</a></li>
              <li><a class="dropdown-item" href="#"><i class="bi bi-share me-2"></i>Share</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item text-danger" href="#"><i class="bi bi-trash me-2"></i>Delete</a></li>
            </ul>
          </div>
        </div>
        <div id="status" class="mt-2"></div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Dropdown, DropdownItem, Card, Icon
from fasthtml.common import Div, H5, A

@app.get("/")
def home():
    return Card(
        Div(
            H5("Document.pdf", cls="mb-0"),
            Dropdown(
                DropdownItem(
                    Icon("download"), " Download",
                    hx_post="/download/123",
                    hx_target="#status"
                ),
                DropdownItem(
                    Icon("share"), " Share",
                    hx_post="/share/123",
                    hx_target="#status"
                ),
                "---",
                DropdownItem(
                    Icon("trash"), " Delete",
                    hx_post="/delete/123",
                    hx_confirm="Are you sure?",
                    hx_target="#status",
                    cls="text-danger"
                ),
                label="Actions",
                variant="outline-secondary",
                size="sm"
            ),
            cls="d-flex justify-content-between align-items-center"
        ),
        Div(id="status", cls="mt-2")
    )

@app.post("/download/{file_id}")
def download_file(file_id: str):
    return Alert("Download started!", variant="success")

@app.post("/delete/{file_id}")
def delete_file(file_id: str):
    return Alert("File deleted!", variant="danger")
```
  </div>
</div>

---

### User Profile Dropdown

A common pattern for user menus with profile info, settings, and logout.

```python
from faststrap import Dropdown, DropdownItem, Icon, Badge
from fasthtml.common import Div, Img, Strong, Small

def UserDropdown(user_name: str, user_email: str, avatar_url: str):
    return Dropdown(
        # Custom header with user info
        Div(
            Img(src=avatar_url, cls="rounded-circle me-2", 
                style={"width": "32px", "height": "32px"}),
            Div(
                Strong(user_name),
                Small(user_email, cls="text-muted d-block"),
                cls="d-inline-block"
            ),
            cls="dropdown-header d-flex align-items-center"
        ),
        "---",
        DropdownItem(Icon("person"), " Profile", href="/profile"),
        DropdownItem(Icon("gear"), " Settings", href="/settings"),
        DropdownItem(
            Icon("bell"), " Notifications ",
            Badge("3", variant="danger", cls="ms-auto"),
            href="/notifications"
        ),
        "---",
        DropdownItem(Icon("box-arrow-right"), " Logout", 
                    href="/logout", cls="text-danger"),
        label=Img(src=avatar_url, cls="rounded-circle", 
                 style={"width": "40px", "height": "40px"}),
        variant="link",
        toggle_cls="border-0 p-0"
    )
```

---

## Bootstrap CSS Classes Explained

Understanding dropdown classes helps you customize menus and troubleshoot issues.

### Container Classes

| Class | Purpose | When to Use |
|-------|---------|-------------|
| `.dropdown` | **Base container** - Creates dropdown context | Default direction (down) |
| `.dropup` | **Upward direction** - Menu appears above button | Bottom toolbars, footer actions |
| `.dropend` | **Right direction** - Menu appears to the right | Sidebar menus, nested navigation |
| `.dropstart` | **Left direction** - Menu appears to the left | Right-aligned sidebars |
| `.btn-group` | **Button group** - Required for split buttons | When using `split=True` |

### Button Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.dropdown-toggle` | **Toggle indicator** - Adds caret icon | Shows menu can be opened |
| `.dropdown-toggle-split` | **Split button style** - Smaller toggle area | Used with split buttons |
| `.btn-{variant}` | **Button color** - Inherited from Button component | primary, success, danger, etc. |
| `.btn-{size}` | **Button size** - sm, lg | Matches button sizing |

### Menu Classes

| Class | Purpose | When to Use |
|-------|---------|-------------|
| `.dropdown-menu` | **Base menu** - Styles the menu container | Always present on menu |
| `.dropdown-menu-dark` | **Dark theme** - Dark background, light text | Dark mode interfaces |
| `.dropdown-menu-end` | **Right align** - Aligns menu to right edge | Right-side buttons, RTL layouts |
| `.dropdown-menu-lg-end` | **Responsive align** - Right align on large screens | Responsive navigation |

### Item Classes

| Class | Purpose | Visual Effect |
|-------|---------|---------------|
| `.dropdown-item` | **Menu item** - Styles clickable items | Hover effect, proper spacing |
| `.dropdown-item.active` | **Active state** - Highlights current selection | Blue background |
| `.dropdown-item.disabled` | **Disabled state** - Non-clickable item | Grayed out, no hover |
| `.dropdown-divider` | **Separator** - Visual divider between groups | Horizontal line |
| `.dropdown-header` | **Section header** - Non-clickable label | Muted text, smaller font |

---

## Responsive Dropdown Patterns

Make dropdowns work beautifully on mobile and desktop.

### Mobile-Friendly Sizes

```python
from faststrap import Dropdown

# Large buttons for touch targets on mobile
Dropdown(
    "Edit Profile",
    "Change Password",
    "Privacy Settings",
    "---",
    "Logout",
    label="Account",
    variant="primary",
    size="lg",  # ← Better for mobile
    cls="w-100"  # ← Full width on mobile
)
```

### Responsive Menu Alignment

```python
# Right-aligned on large screens, left-aligned on small
Dropdown(
    "Action 1",
    "Action 2",
    label="Options",
    menu_cls="dropdown-menu-lg-end"  # ← Responsive alignment
)
```

### Navbar Dropdowns

```python
from faststrap import Navbar, Dropdown

Navbar(
    brand="MyApp",
    items=[
        Dropdown(
            "Dashboard",
            "Analytics",
            "Reports",
            label="Menu",
            variant="link",  # ← Link style for navbar
            toggle_cls="nav-link"  # ← Navbar link styling
        )
    ]
)
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

Set consistent dropdown styling across your entire application.

```python
from faststrap import set_component_defaults, Dropdown

# All dropdowns use secondary variant and small size
set_component_defaults("Dropdown", variant="secondary", size="sm")

# Now all dropdowns inherit these defaults
Dropdown("Edit", "Delete", label="Actions")
# ↑ Automatically has variant="secondary" and size="sm"

# Override when needed
Dropdown("Important Action", "Critical Action", 
         label="Admin", variant="danger", size="lg")
# ↑ Explicitly override defaults
```

**Common Default Patterns:**

```python
# Admin panels - prominent dropdowns
set_component_defaults("Dropdown", variant="primary", size="lg")

# Data tables - compact action menus
set_component_defaults("Dropdown", variant="outline-secondary", size="sm")

# Dark theme apps - dark menus
set_component_defaults("Dropdown", menu_cls="dropdown-menu-dark")
```

---

## Advanced Customization

### Custom Menu Items with Icons and Badges

```python
from faststrap import Dropdown, DropdownItem, Icon, Badge

Dropdown(
    DropdownItem(
        Icon("inbox-fill", cls="text-primary me-2"),
        "Inbox ",
        Badge("12", variant="primary"),
        href="/inbox"
    ),
    DropdownItem(
        Icon("star-fill", cls="text-warning me-2"),
        "Favorites ",
        Badge("5", variant="warning"),
        href="/favorites"
    ),
    "---",
    DropdownItem(
        Icon("archive", cls="text-muted me-2"),
        "Archive",
        href="/archive"
    ),
    label="Messages",
    variant="info"
)
```

### Nested Dropdowns (Submenus)

While Bootstrap doesn't natively support nested dropdowns, you can create them with custom CSS:

```python
# Note: Requires custom CSS for .dropdown-submenu
from fasthtml.common import Div, A, Ul, Li

Div(
    Button("Main Menu", cls="btn btn-primary dropdown-toggle",
           data_bs_toggle="dropdown"),
    Ul(
        Li(A("Action", cls="dropdown-item", href="#")),
        Li(
            A("Submenu", cls="dropdown-item dropdown-toggle", href="#"),
            Ul(
                Li(A("Subaction 1", cls="dropdown-item", href="#")),
                Li(A("Subaction 2", cls="dropdown-item", href="#")),
                cls="dropdown-menu dropdown-submenu"
            ),
            cls="dropdown-submenu"
        ),
        cls="dropdown-menu"
    ),
    cls="dropdown"
)
```

---

## Common Recipes

### The "More Actions" Pattern

A common pattern for row actions in tables.

```python
from faststrap import Table, Dropdown, DropdownItem, Icon

Table(
    THead(
        Tr(Th("Name"), Th("Status"), Th("Actions"))
    ),
    TBody(
        Tr(
            Td("John Doe"),
            Td(Badge("Active", variant="success")),
            Td(
                Dropdown(
                    DropdownItem(Icon("eye"), " View", href="/view/1"),
                    DropdownItem(Icon("pencil"), " Edit", href="/edit/1"),
                    "---",
                    DropdownItem(Icon("trash"), " Delete", 
                               href="/delete/1", cls="text-danger"),
                    label=Icon("three-dots-vertical"),
                    variant="link",
                    size="sm",
                    toggle_cls="text-dark"
                )
            )
        )
    )
)
```

### The "Bulk Actions" Pattern

Dropdown for performing actions on multiple selected items.

```python
Dropdown(
    DropdownItem("Export Selected", hx_post="/export", hx_include=".item-checkbox:checked"),
    DropdownItem("Archive Selected", hx_post="/archive", hx_include=".item-checkbox:checked"),
    "---",
    DropdownItem("Delete Selected", hx_post="/delete", hx_include=".item-checkbox:checked",
                cls="text-danger", hx_confirm="Delete selected items?"),
    label="Bulk Actions",
    variant="secondary",
    disabled=True,  # Enable via JavaScript when items selected
    id="bulk-actions-dropdown"
)
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility, but here's what's happening:

✅ **Automatic Features:**
- `aria-expanded` attribute toggles on open/close
- `role="menu"` on dropdown menu
- `role="menuitem"` on dropdown items
- Keyboard navigation (Arrow keys, Esc, Enter)
- Focus management

**Manual Enhancements:**

```python
Dropdown(
    "Edit",
    "Delete",
    "Archive",
    label="Actions",
    aria_label="Document actions menu",  # Screen reader description
    id="doc-actions"  # For programmatic control
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*items` | `Any` | Required | Menu items (strings, DropdownItem, or "---" for dividers) |
| `label` | `str \| None` | `"Dropdown"` | Button label text |
| `variant` | `VariantType \| None` | `"primary"` | Button color variant |
| `size` | `"sm" \| "lg" \| None` | `None` | Button size |
| `split` | `bool \| None` | `False` | Use split button style |
| `direction` | `"down" \| "up" \| "start" \| "end"` | `"down"` | Menu direction |
| `toggle_cls` | `str \| None` | `None` | Additional classes for toggle button |
| `menu_cls` | `str \| None` | `None` | Additional classes for dropdown menu |
| `item_cls` | `str \| None` | `None` | Additional classes for all items |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, id, hx-*, data-*) |

::: faststrap.components.navigation.dropdown.Dropdown
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.navigation.dropdown.DropdownItem
    options:
        show_source: true
        heading_level: 4
