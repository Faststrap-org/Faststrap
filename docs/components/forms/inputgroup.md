# InputGroup

The `InputGroup` component extends form controls by adding text, buttons, or icons before or after inputs. Perfect for currency fields, search boxes, and any input that needs context or actions.

!!! success "Goal"
    Master creating input groups with addons, understand Bootstrap input-group classes, and build enhanced form controls that provide better user context and functionality.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Input Group Documentation](https://getbootstrap.com/docs/5.3/forms/input-group/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="input-group mb-3">
      <span class="input-group-text">@</span>
      <input type="text" class="form-control" placeholder="Username">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import InputGroup, InputGroupText, Input

InputGroup(
    InputGroupText("@"),
    Input("username", placeholder="Username")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Text Addons - Provide Context

Add text before or after inputs to clarify what users should enter.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="input-group mb-3">
      <span class="input-group-text">$</span>
      <input type="number" class="form-control" placeholder="0.00">
      <span class="input-group-text">.00</span>
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Your website">
      <span class="input-group-text">.com</span>
    </div>
    <div class="input-group">
      <span class="input-group-text">https://</span>
      <input type="text" class="form-control" placeholder="example.com">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Currency input
InputGroup(
    InputGroupText("$"),
    Input("amount", input_type="number", placeholder="0.00"),
    InputGroupText(".00")
)

# Domain input
InputGroup(
    Input("domain", placeholder="Your website"),
    InputGroupText(".com")
)

# URL input
InputGroup(
    InputGroupText("https://"),
    Input("url", placeholder="example.com")
)
```
  </div>
</div>

---

### 2. Button Addons - Add Actions

Combine inputs with buttons for immediate actions.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Search...">
      <button class="btn btn-primary" type="button">
        <i class="bi bi-search"></i> Search
      </button>
    </div>
    <div class="input-group mb-3">
      <button class="btn btn-outline-secondary" type="button">Copy</button>
      <input type="text" class="form-control" value="https://example.com/share/abc123" readonly>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import InputGroup, Input, Button, Icon

# Search box
InputGroup(
    Input("search", placeholder="Search..."),
    Button(Icon("search"), " Search", variant="primary")
)

# Copy link
InputGroup(
    Button("Copy", variant="outline-secondary", 
           onclick="navigator.clipboard.writeText(this.nextElementSibling.value)"),
    Input("share_link", value="https://example.com/share/abc123", readonly=True)
)
```
  </div>
</div>

---

### 3. Dropdown Addons - Multiple Options

Add dropdown menus to input groups for filtering or actions.

```python
from faststrap import InputGroup, Input, Dropdown, DropdownItem

InputGroup(
    Dropdown(
        DropdownItem("All Categories", href="#"),
        DropdownItem("Electronics", href="#"),
        DropdownItem("Clothing", href="#"),
        DropdownItem("Books", href="#"),
        label="Category",
        variant="outline-secondary"
    ),
    Input("search", placeholder="Search products...")
)
```

---

### 4. Icon Addons - Visual Indicators

Use icons to indicate input purpose.

```python
from faststrap import InputGroup, InputGroupText, Input, Icon

# Email input with icon
InputGroup(
    InputGroupText(Icon("envelope")),
    Input("email", input_type="email", placeholder="Email address")
)

# Password input with icon
InputGroup(
    InputGroupText(Icon("lock")),
    Input("password", input_type="password", placeholder="Password")
)

# Phone input with icon
InputGroup(
    InputGroupText(Icon("telephone")),
    Input("phone", input_type="tel", placeholder="Phone number")
)
```

---

### 5. Sizes - Match Your Design

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="input-group input-group-lg mb-3">
      <span class="input-group-text">@</span>
      <input type="text" class="form-control" placeholder="Large">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">@</span>
      <input type="text" class="form-control" placeholder="Default">
    </div>
    <div class="input-group input-group-sm">
      <span class="input-group-text">@</span>
      <input type="text" class="form-control" placeholder="Small">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Large
InputGroup(
    InputGroupText("@"),
    Input("username", placeholder="Large"),
    size="lg"
)

# Default
InputGroup(
    InputGroupText("@"),
    Input("username", placeholder="Default")
)

# Small
InputGroup(
    InputGroupText("@"),
    Input("username", placeholder="Small"),
    size="sm"
)
```
  </div>
</div>

---

## Practical Functionality

### Search Box with HTMX

```python
from faststrap import InputGroup, Input, Button, Icon

InputGroup(
    Input(
        "search",
        placeholder="Search products...",
        hx_get="/search",
        hx_trigger="keyup changed delay:500ms",
        hx_target="#search-results"
    ),
    Button(
        Icon("search"),
        variant="primary",
        hx_get="/search",
        hx_include="[name='search']",
        hx_target="#search-results"
    )
)
```

---

### Promo Code Input

```python
from faststrap import InputGroup, Input, Button

InputGroup(
    Input("promo_code", placeholder="Enter promo code"),
    Button(
        "Apply",
        variant="success",
        hx_post="/apply-promo",
        hx_include="[name='promo_code']",
        hx_target="#cart-total",
        hx_swap="outerHTML"
    ),
    cls="mb-3"
)
```

---

### File Upload with Button

```python
from faststrap import InputGroup, Button

InputGroup(
    Input("file", input_type="file", cls="form-control"),
    Button(
        Icon("upload"), " Upload",
        variant="primary",
        hx_post="/upload",
        hx_encoding="multipart/form-data",
        hx_include="[name='file']"
    )
)
```

---

## Bootstrap CSS Classes Explained

### Core InputGroup Classes

| Class | Purpose | Applied To |
|-------|---------|------------|
| `.input-group` | **Container** - Wraps input and addons | `<div>` wrapper |
| `.input-group-lg` | **Large size** - Bigger inputs and addons | `.input-group` |
| `.input-group-sm` | **Small size** - Compact inputs and addons | `.input-group` |
| `.input-group-text` | **Text addon** - Styles text/icon addons | `<span>` for text |
| `.form-control` | **Input styling** - Must be on input element | `<input>`, `<select>`, `<textarea>` |
| `.btn` | **Button addon** - Styles button addons | `<button>` elements |

### Layout Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.flex-nowrap` | **Prevent wrapping** - Keep on one line | Prevents wrapping on small screens |
| `.mb-3` | **Margin bottom** - Spacing between groups | Standard form spacing |

---

## Responsive InputGroup Patterns

### Mobile-Friendly Input Groups

```python
# Stack on mobile, inline on desktop
InputGroup(
    InputGroupText("$"),
    Input("amount", input_type="number"),
    Button("Submit", variant="primary"),
    cls="flex-wrap flex-md-nowrap"  # Wrap on mobile, nowrap on desktop
)
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

```python
from faststrap import set_component_defaults, InputGroup

# All input groups large by default
set_component_defaults("InputGroup", size="lg")

# Now all input groups inherit large size
InputGroup(
    InputGroupText("@"),
    Input("username")
)  # ← Automatically size="lg"
```

---

## Common Recipes

### The "Copy to Clipboard" Pattern

```python
from faststrap import InputGroup, Input, Button, Icon

def CopyableInput(value: str, label: str = "Copy"):
    return InputGroup(
        Input("copy_value", value=value, readonly=True),
        Button(
            Icon("clipboard"),
            label,
            variant="outline-secondary",
            onclick=f"navigator.clipboard.writeText('{value}'); this.textContent='Copied!'; setTimeout(()=>this.textContent='{label}',2000)"
        )
    )

# Usage
CopyableInput("https://example.com/share/abc123")
```

---

### The "Unit Selector" Pattern

```python
from faststrap import InputGroup, Input, Select

InputGroup(
    Input("value", input_type="number", placeholder="0"),
    Select(
        "unit",
        ("kg", "Kilograms"),
        ("lb", "Pounds"),
        ("oz", "Ounces"),
        cls="form-select"
    )
)
```

---

## Accessibility Best Practices

✅ **Automatic Features:**
- Proper form control structure
- Label associations (use with labels)
- Keyboard navigation

**Manual Enhancements:**

```python
InputGroup(
    InputGroupText("@", aria_label="Username prefix"),
    Input("username", placeholder="Username", aria_label="Username")
)
```

---

## Parameter Reference

### InputGroup

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Form controls and addons |
| `size` | `"sm" \| "lg" \| None` | `None` | Group size |
| `nowrap` | `bool` | `False` | Prevent wrapping |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### InputGroupText

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Text or icon content |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.forms.inputgroup.InputGroup
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.inputgroup.InputGroupText
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.inputgroup.FloatingLabel
    options:
        show_source: true
        heading_level: 4
