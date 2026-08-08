# Layout Primitives

`Stack`, `Cluster`, and `Center` are zero-JS flexbox layout primitives that cover the most common layout patterns in web applications. They use Bootstrap utility classes under the hood, so they are lightweight, responsive, and familiar.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Flexbox](https://getbootstrap.com/docs/5.3/utilities/flex/)

---

## Quick Start

```python
from faststrap import Stack, Cluster, Center, Button

# Vertical stack with gap
Stack(
    "Profile",
    "Billing",
    "Security",
    gap=3,
)

# Horizontal action row
Cluster(
    Button("Save", variant="primary"),
    Button("Cancel", variant="secondary", outline=True),
    justify="end",
)

# Centered content
Center(
    "Nothing selected yet",
    min_height="40vh",
    max_width="32rem",
)
```

---

## Visual Examples & Use Cases

### 1. Stack (Vertical Layout)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column gap-3">
      <div class="p-2 border rounded">Profile</div>
      <div class="p-2 border rounded">Billing</div>
      <div class="p-2 border rounded">Security</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Stack(
    "Profile",
    "Billing",
    "Security",
    gap=3,
)
```
  </div>
</div>

### 2. Cluster (Horizontal Layout)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2 justify-content-end">
      <button class="btn btn-primary">Save</button>
      <button class="btn btn-secondary">Cancel</button>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Cluster(
    Button("Save", variant="primary"),
    Button("Cancel", variant="secondary", outline=True),
    justify="end",
)
```
  </div>
</div>

### 3. Center (Centered Content)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex justify-content-center" style="min-height: 40vh; max-width: 32rem;">
      <div class="text-center">
        <p class="mb-0">Nothing selected yet</p>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Center(
    "Nothing selected yet",
    min_height="40vh",
    max_width="32rem",
)
```
  </div>
</div>

### 4. Nested Layouts

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column gap-3">
      <div class="d-flex flex-wrap gap-2 justify-content-end">
        <button class="btn btn-primary btn-sm">New</button>
        <button class="btn btn-secondary btn-sm">Refresh</button>
      </div>
      <div class="p-3 border rounded">
        <div class="d-flex flex-column gap-2">
          <div class="p-2 border rounded">Item 1</div>
          <div class="p-2 border rounded">Item 2</div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Stack(
    Cluster(
        Button("New", variant="primary", size="sm"),
        Button("Refresh", variant="secondary", outline=True, size="sm"),
        justify="end",
    ),
    Card(
        Card.Body(
            Stack(
                "Item 1",
                "Item 2",
                gap=2,
            )
        ),
    ),
    gap=3,
)
```
  </div>
</div>

---

## Practical Functionality

### 1. Sidebar Navigation

```python
Stack(
    NavbarItem("Dashboard", href="/", icon="speedometer2"),
    NavbarItem("Users", href="/users", icon="people"),
    NavbarItem("Settings", href="/settings", icon="gear"),
    gap=1,
)
```

### 2. Action Bar with HTMX

```python
Cluster(
    Button("Save", variant="primary", hx_post="/save", hx_target="#form", hx_swap="outerHTML"),
    Button("Cancel", variant="secondary", hx_get="/cancel", hx_target="#form"),
    justify="between",
)
```

### 3. Empty State

```python
Center(
    EmptyState(
        "No data yet",
        description="Create your first item to get started.",
        icon="inbox",
    ),
    min_height="60vh",
)
```

---

## Parameter Reference

### `Stack`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Stacked content. |
| `gap` | `int` | `2` | Bootstrap gap utility suffix (0–5). |
| `align` | `str \| None` | `None` | Bootstrap `align-items-*` class. |
| `justify` | `str \| None` | `None` | Bootstrap `justify-content-*` class. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

### `Cluster`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Clustered content. |
| `gap` | `int` | `2` | Bootstrap gap utility suffix (0–5). |
| `align` | `str \| None` | `None` | Bootstrap `align-items-*` class. |
| `justify` | `str \| None` | `None` | Bootstrap `justify-content-*` class. |
| `wrap` | `bool` | `True` | Allow children to wrap. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

### `Center`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Centered content. |
| `min_height` | `str` | `"100vh"` | Minimum container height. |
| `max_width` | `str` | `"100%"` | Maximum content width. |
| `text_center` | `bool` | `True` | Apply `text-center` class. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

---

## API Reference

::: faststrap.components.layout.primitives.Stack
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.layout.primitives.Cluster
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.layout.primitives.Center
    options:
        show_source: true
        heading_level: 4
