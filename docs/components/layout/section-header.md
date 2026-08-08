# SectionHeader

`SectionHeader` renders a lightweight section-level heading with optional subtitle, eyebrow label, badge, and action buttons. It is the within-section sibling of `PageHeader`, which is designed for page-level titles.

Use `PageHeader` for top-of-page titles. Use `SectionHeader` for headings inside cards, dashboard panels, and admin screens.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Typography](https://getbootstrap.com/docs/5.3/content/typography/)

---

## Quick Start

```python
from faststrap import SectionHeader, Button, Badge

SectionHeader(
    "Users",
    subtitle="Manage team members and permissions.",
    eyebrow="Admin",
    badge=Badge("New", variant="success"),
    actions=[Button("Add User", variant="primary")],
)
```

---

## Visual Examples & Use Cases

### 1. Basic Section Header

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-2 mb-3">
      <div>
        <span class="h2">Users</span>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SectionHeader("Users")
```
  </div>
</div>

### 2. With Subtitle and Eyebrow

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-2 mb-3">
      <div>
        <span class="text-uppercase text-muted small fw-semibold">Admin</span>
        <h2 class="mb-2">Users</h2>
        <p class="text-muted mb-0">Manage team members and permissions.</p>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SectionHeader(
    "Users",
    eyebrow="Admin",
    subtitle="Manage team members and permissions.",
)
```
  </div>
</div>

### 3. With Badge and Actions

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-2 mb-3">
      <div>
        <h2 class="mb-2">
          Users
          <span class="ms-2 align-middle badge bg-success">New</span>
        </h2>
        <p class="text-muted mb-0">Manage team members.</p>
      </div>
      <div class="d-flex flex-wrap gap-2 align-items-center">
        <button class="btn btn-primary">Add User</button>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SectionHeader(
    "Users",
    subtitle="Manage team members.",
    badge=Badge("New", variant="success"),
    actions=[Button("Add User", variant="primary")],
)
```
  </div>
</div>

### 4. Small Size (h3)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-2 mb-3">
      <div>
        <h3 class="mb-1">Settings</h3>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
SectionHeader("Settings", size="sm")
```
  </div>
</div>

---

## Practical Functionality

### 1. Inside a Card

```python
Card(
    SectionHeader(
        "Recent Activity",
        eyebrow="Logs",
        actions=[Button("Refresh", variant="secondary", outline=True)],
    ),
    Card.Body(
        # ... activity list
    ),
)
```

### 2. Inside a Dashboard Grid

```python
DashboardGrid(
    SectionHeader("Overview", subtitle="Key metrics for this week."),
    StatCard("Revenue", "$12K", "+5%"),
    StatCard("Users", "1.2K", "+12%"),
    cols=3,
)
```

### 3. With HTMX Actions

```python
SectionHeader(
    "Items",
    actions=[
        Button("Add", variant="primary", hx_get="/items/new", hx_target="#modal"),
    ],
)
```

---

## When to Use SectionHeader vs PageHeader

| Component | Use Case | Heading Level |
|-----------|----------|---------------|
| `PageHeader` | Page-level title, first thing on the page | `h1`/`h2` |
| `SectionHeader` | Within-section heading, inside cards/panels | `h2`/`h3` |

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | `str` | required | Section title text. |
| `subtitle` | `str \| None` | `None` | Muted supporting copy below the title. |
| `eyebrow` | `str \| None` | `None` | Small uppercase label above the title. |
| `badge` | `Any \| None` | `None` | Inline badge or status element beside the title. |
| `actions` | `Any \| list[Any] \| tuple[Any, ...] \| None` | `None` | Right-aligned action content. |
| `size` | `str` | `"md"` | Heading size: `"sm"` renders an `h3`, `"md"` renders an `h2`. |
| `**kwargs` | `Any` | `{}` | Additional HTML/HTMX/data/ARIA attributes. |

---

## API Reference

::: faststrap.components.layout.section_header.SectionHeader
    options:
        show_source: true
        heading_level: 4
