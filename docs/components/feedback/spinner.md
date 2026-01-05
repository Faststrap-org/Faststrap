# Spinner

The `Spinner` component creates animated loading indicators that show users something is happening. Essential for async operations, page loads, and any process that takes time.

!!! success "Goal"
    Master creating loading spinners, understand Bootstrap animation classes, and build smooth loading experiences that keep users informed.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Spinners Documentation](https://getbootstrap.com/docs/5.3/components/spinners/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="spinner-border text-primary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Spinner

Spinner(variant="primary")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Spinner Types - Border vs Grow

Bootstrap provides two animation styles: **border** (spinning circle) and **grow** (pulsing dot).

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-4 align-items-center justify-content-center">
      <div>
        <div class="spinner-border text-primary mb-2" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
        <div class="text-center small text-muted">Border (default)</div>
      </div>
      <div>
        <div class="spinner-grow text-success mb-2" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
        <div class="text-center small text-muted">Grow</div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Border spinner (default) - spinning circle
Spinner(variant="primary", spinner_type="border")

# Grow spinner - pulsing dot
Spinner(variant="success", spinner_type="grow")
```
  </div>
</div>

**When to use each:**

| Type | Animation | Best For |
|------|-----------|----------|
| `border` | Spinning circle | Buttons, inline loading, most cases |
| `grow` | Pulsing dot | Subtle indicators, background processes |

---

### 2. Color Variants - Match Your Context

Use semantic colors to indicate what's loading.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-3 justify-content-center">
      <div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-success" role="status"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-danger" role="status"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-warning" role="status"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-info" role="status"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-light" role="status" style="border-color: #dee2e6 transparent transparent transparent;"><span class="visually-hidden">Loading...</span></div>
      <div class="spinner-border text-dark" role="status"><span class="visually-hidden">Loading...</span></div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Spinner(variant="primary")   # Default actions
Spinner(variant="success")   # Successful operations
Spinner(variant="danger")    # Deletions, critical operations
Spinner(variant="warning")   # Caution operations
Spinner(variant="info")      # Information loading
Spinner(variant="light")     # Dark backgrounds
Spinner(variant="dark")      # Light backgrounds
```
  </div>
</div>

---

### 3. Sizes - Small for Buttons, Large for Pages

Adjust spinner size to match context.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-4 align-items-center justify-content-center">
      <div class="spinner-border spinner-border-sm text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Small - for buttons
Spinner(variant="primary", size="sm")

# Default - standard loading
Spinner(variant="primary")

# Custom large - for full-page loading
Spinner(variant="primary", style={"width": "3rem", "height": "3rem"})
```
  </div>
</div>

---

## Practical Functionality

### In Buttons - Loading States

Show users their action is processing.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-2">
      <button class="btn btn-primary" disabled>
        <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
        Saving...
      </button>
      <button class="btn btn-success" disabled>
        <span class="spinner-grow spinner-grow-sm me-2" role="status" aria-hidden="true"></span>
        Processing...
      </button>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Button, Spinner

# Border spinner in button
Button(
    Spinner(size="sm", variant="light", cls="me-2"),
    "Saving...",
    variant="primary",
    disabled=True
)

# Grow spinner in button
Button(
    Spinner(size="sm", variant="light", spinner_type="grow", cls="me-2"),
    "Processing...",
    variant="success",
    disabled=True
)

# Or use Button's built-in loading state
Button("Save", variant="primary", loading=True, loading_text="Saving...")
```
  </div>
</div>

---

### Full-Page Loading Overlay

Show a loading screen while content loads.

```python
from faststrap import Spinner, Fx
from fasthtml.common import Div, H4

def LoadingOverlay(message: str = "Loading..."):
    return Div(
        Div(
            Spinner(variant="primary", style={"width": "3rem", "height": "3rem"}),
            H4(message, cls="mt-3 text-muted"),
            cls=f"text-center {Fx.fade_in}"
        ),
        cls="position-fixed top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center bg-white bg-opacity-75",
        style={"z-index": "9999"},
        id="loading-overlay"
    )

# Use with HTMX
@app.get("/")
def home():
    return Div(
        LoadingOverlay("Loading your dashboard..."),
        Div(id="content"),
        hx_get="/load-content",
        hx_target="#content",
        hx_swap="innerHTML",
        hx_trigger="load"
    )

@app.get("/load-content")
def load_content():
    # Your content loading logic
    return Div("Content loaded!", cls="container")
```

---

### Inline Loading - Text Replacement

Replace text with spinner during async operations.

```python
from faststrap import Spinner

@app.get("/")
def home():
    return Div(
        Button(
            "Load Data",
            hx_get="/fetch-data",
            hx_target="#data-status",
            hx_swap="innerHTML"
        ),
        Div(id="data-status", cls="mt-3")
    )

@app.get("/fetch-data")
def fetch_data():
    # Show spinner immediately
    return Div(
        Spinner(size="sm", variant="primary", cls="me-2"),
        "Fetching data...",
        hx_get="/data-result",
        hx_trigger="load delay:2s",  # Simulate 2s load
        hx_swap="outerHTML"
    )

@app.get("/data-result")
def data_result():
    return Div("Data loaded successfully!", cls="text-success")
```

---

## Bootstrap CSS Classes Explained

### Core Spinner Classes

| Class | Purpose | Effect |
|-------|---------|--------|
| `.spinner-border` | **Border animation** - Spinning circle | Default spinner style |
| `.spinner-grow` | **Grow animation** - Pulsing dot | Alternative animation |
| `.spinner-border-sm` | **Small border** - Reduced size | For buttons, inline use |
| `.spinner-grow-sm` | **Small grow** - Reduced size | For buttons, inline use |
| `.text-{variant}` | **Color** - Applies variant color | primary, success, danger, etc. |

### Utility Classes for Spinners

| Class | Purpose | Use Case |
|-------|---------|----------|
| `.visually-hidden` | **Screen reader only** - Hides text visually | Accessibility label |
| `.me-2`, `.ms-2` | **Margin** - Spacing around spinner | Inline with text |
| `.d-inline-block` | **Display** - Inline positioning | Inline spinners |
| `.position-absolute` | **Positioning** - Absolute placement | Overlay spinners |

### Custom Sizing

```python
# Custom size via style
Spinner(
    variant="primary",
    style={"width": "5rem", "height": "5rem"}
)

# Or via CSS classes
Spinner(
    variant="success",
    cls="spinner-border-lg"  # If you define this in your CSS
)
```

---

## Responsive Loading Patterns

### Mobile-Friendly Loading

```python
from faststrap import Spinner, Card

# Larger spinners for better visibility on mobile
Card(
    Div(
        Spinner(
            variant="primary",
            style={"width": "3rem", "height": "3rem"},
            cls="mb-3"
        ),
        H5("Loading your content...", cls="text-muted"),
        cls="text-center py-5"
    )
)
```

### Skeleton Loading (Alternative Pattern)

While not a spinner, skeleton screens are modern loading patterns:

```python
from fasthtml.common import Div

def SkeletonCard():
    return Div(
        Div(cls="placeholder-glow"),
        Div(cls="placeholder col-12 mb-2"),
        Div(cls="placeholder col-8"),
        cls="card-body"
    )
```

---

## Core Faststrap Features

### Global Defaults with `set_component_defaults`

Set consistent spinner styling across your app.

```python
from faststrap import set_component_defaults, Spinner

# All spinners use success variant and grow animation
set_component_defaults("Spinner", variant="success", spinner_type="grow")

# Now all spinners inherit these defaults
Spinner()  # ← Automatically success + grow

# Override when needed
Spinner(variant="danger", spinner_type="border")
```

**Common Default Patterns:**

```python
# Loading-heavy apps - consistent primary spinners
set_component_defaults("Spinner", variant="primary")

# Dark theme apps - light spinners
set_component_defaults("Spinner", variant="light")

# Subtle loading - grow animations
set_component_defaults("Spinner", spinner_type="grow")
```

---

## Common Recipes

### The "Loading Button" Pattern

Disable button and show spinner during async operations.

```python
from faststrap import Button, Spinner

@app.get("/")
def home():
    return Button(
        "Submit Form",
        id="submit-btn",
        variant="primary",
        hx_post="/submit",
        hx_target="#result",
        hx_indicator="#submit-btn"  # Show loading on this button
    )

# HTMX automatically adds .htmx-request class during requests
# Style it in CSS:
"""
.htmx-request .htmx-indicator {
    display: inline-block !important;
}
.htmx-indicator {
    display: none;
}
"""

# Or manually control with JavaScript/HTMX events
```

### The "Infinite Scroll" Spinner

Show spinner at bottom while loading more content.

```python
@app.get("/")
def home():
    return Div(
        Div(id="items", *[item_card(i) for i in range(20)]),
        Div(
            Spinner(variant="primary"),
            id="load-more",
            hx_get="/load-more?page=2",
            hx_trigger="revealed",  # Triggers when scrolled into view
            hx_swap="outerHTML"
        ),
        cls="container"
    )

@app.get("/load-more")
def load_more(page: int):
    items = [item_card(i) for i in range(page*20, (page+1)*20)]
    next_spinner = Div(
        Spinner(variant="primary"),
        id="load-more",
        hx_get=f"/load-more?page={page+1}",
        hx_trigger="revealed",
        hx_swap="outerHTML"
    )
    return Div(*items, next_spinner)
```

---

## Accessibility Best Practices

Faststrap automatically handles accessibility:

✅ **Automatic Features:**
- `role="status"` for screen readers
- `.visually-hidden` text for context
- Proper ARIA attributes

**Manual Enhancements:**

```python
Spinner(
    variant="primary",
    label="Loading user data",  # Custom screen reader text
    aria_live="polite",         # Announce when appears
    aria_busy="true"            # Indicate busy state
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | `VariantType \| None` | `"primary"` | Color variant |
| `size` | `"sm" \| None` | `None` | Spinner size (default is medium) |
| `spinner_type` | `"border" \| "grow"` | `"border"` | Animation type |
| `label` | `str \| None` | `"Loading..."` | Screen reader label |
| `**kwargs` | `Any` | - | Additional HTML attributes (cls, style, id) |

::: faststrap.components.feedback.spinner.Spinner
    options:
        show_source: true
        heading_level: 4
