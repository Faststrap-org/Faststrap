# Tag

`Tag` renders an interactive chip or label for filtering, categorization, and selection. Unlike `Badge`, which is purely informational, `Tag` is designed to be interactive — it can be removed by the user and supports HTMX attributes for server-side removal.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Badges](https://getbootstrap.com/docs/5.3/components/badges/)

---

## Quick Start

```python
from faststrap import Tag

# Basic tag
Tag("Python")

# Removable tag
Tag("JavaScript", removable=True)

# Tag with icon
Tag("React", icon="react", variant="primary")
```

---

## Visual Examples & Use Cases

### 1. Basic Tags

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2">
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-secondary px-2 py-1 user-select-none">Python</span>
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-primary px-2 py-1 user-select-none">JavaScript</span>
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-success px-2 py-1 user-select-none">Rust</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Tag("Python", variant="secondary")
Tag("JavaScript", variant="primary")
Tag("Rust", variant="success")
```
  </div>
</div>

### 2. Removable Tags

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2">
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-secondary px-2 py-1 user-select-none">
        Python
        <button type="button" class="btn-close btn-close-white ms-1" aria-label="Remove" style="font-size: 0.65em; filter: brightness(0) invert(1);"></button>
      </span>
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-primary px-2 py-1 user-select-none">
        JavaScript
        <button type="button" class="btn-close btn-close-white ms-1" aria-label="Remove" style="font-size: 0.65em; filter: brightness(0) invert(1);"></button>
      </span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Tag("Python", removable=True)
Tag("JavaScript", removable=True)
```
  </div>
</div>

### 3. Tags with Icons

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2">
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-primary px-2 py-1 user-select-none">
        <i class="bi bi-react" style="font-size: 0.85em;"></i>
        React
      </span>
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-warning px-2 py-1 user-select-none">
        <i class="bi bi-currency-bitcoin" style="font-size: 0.85em;"></i>
        Crypto
      </span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Tag("React", icon="react", variant="primary")
Tag("Crypto", icon="currency-bitcoin", variant="warning")
```
  </div>
</div>

### 4. Filter Tags with HTMX

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2">
      <span class="badge d-inline-flex align-items-center gap-1 text-bg-primary px-2 py-1 user-select-none">
        Python
        <button type="button" class="btn-close btn-close-white ms-1" aria-label="Remove"></button>
      </span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Tag(
    "Python",
    removable=True,
    on_remove="hx-delete='/filters/python' hx-target='#filter-list'",
)
```
  </div>
</div>

---

## Practical Functionality

### 1. Filter Bar

```python
from faststrap import Tag, Form

def filter_bar(active_filters):
    tags = []
    for filter_name in active_filters:
        tags.append(
            Tag(
                filter_name,
                removable=True,
                on_remove=f"hx-delete='/filters/{filter_name}' hx-target='#results'",
            )
        )
    return Form(*tags, cls="d-flex flex-wrap gap-2")
```

### 2. Removable Tags with Animation

Tags include a `data-fs-tag="true"` attribute that the Faststrap initializer uses to add a fade-out animation when the remove button is clicked. The animation is handled automatically by `faststrap-init.js`.

```python
Tag(
    "Draft",
    variant="warning",
    removable=True,
    on_remove="hx-delete='/tags/1' hx-swap='outerHTML'",
)
```

---

## Tag vs Badge

| Feature | Tag | Badge |
|---------|-----|-------|
| Interactive | Yes (removable) | No |
| Use case | Filters, labels, selections | Status indicators, counts |
| Remove button | Optional | No |
| Animation | Fade-out on remove | No |

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `children` | `str \| tuple` | required | Tag text content. |
| `variant` | `VariantType` | `"secondary"` | Bootstrap color variant. |
| `size` | `"sm" \| "md"` | `"md"` | Tag size. |
| `removable` | `bool` | `False` | Show a close/remove button. |
| `icon` | `str \| None` | `None` | Optional leading Bootstrap icon name. |
| `on_remove` | `str \| None` | `None` | HTMX attributes for removal (e.g. `hx-delete="/tags/1"`). |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes (cls, id, hx-*, data-*, etc.). |

---

## API Reference

::: faststrap.components.display.tag.Tag
    options:
        show_source: true
        heading_level: 4
