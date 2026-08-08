# Separator

`Separator` renders a semantic divider for visually grouping content. It supports horizontal and vertical orientations, optional centered labels, and configurable thickness and spacing.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Dividers](https://getbootstrap.com/docs/5.3/components/dividers/)

---

## Quick Start

```python
from faststrap import Separator

# Horizontal divider
Separator()

# Vertical divider
Separator(orientation="vertical")

# Labeled divider
Separator(label="Section")
```

---

## Visual Examples & Use Cases

### 1. Horizontal Separator

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <p>Content above</p>
    <div class="border-top" role="separator" aria-orientation="horizontal"></div>
    <p>Content below</p>
  </div>
  <div class="preview-code" markdown>
```python
Separator()
```
  </div>
</div>

### 2. Vertical Separator

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <span>Left</span>
    <span class="vr" role="separator" aria-orientation="vertical" style="display: inline-block; width: 1px;"></span>
    <span>Right</span>
  </div>
  <div class="preview-code" markdown>
```python
Separator(orientation="vertical")
```
  </div>
</div>

### 3. Labeled Separator

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex align-items-center" role="separator" aria-orientation="horizontal">
      <div class="flex-grow-1 border"></div>
      <span class="px-2 text-muted small">OR</span>
      <div class="flex-grow-1 border"></div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Separator(label="OR")
```
  </div>
</div>

### 4. Custom Thickness and Spacing

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <p>Above</p>
    <div class="border-top" role="separator" aria-orientation="horizontal" style="border-top-width: 3px; margin-block: 0.75rem;"></div>
    <p>Below</p>
  </div>
  <div class="preview-code" markdown>
```python
Separator(thickness=3, spacing=3)
```
  </div>
</div>

---

## Practical Functionality

### 1. Inside a Card

```python
Card(
    Card.Header("Settings"),
    Card.Body(
        Separator(label="General"),
        # ... general settings
        Separator(label="Security"),
        # ... security settings
    ),
)
```

### 2. Inside a Stack

```python
Stack(
    "First item",
    Separator(),
    "Second item",
    Separator(),
    "Third item",
    gap=2,
)
```

### 3. Vertical Separator in a Toolbar

```python
Cluster(
    Button("Save", variant="primary"),
    Separator(orientation="vertical"),
    Button("Cancel", variant="secondary"),
    Separator(orientation="vertical"),
    Button("Delete", variant="danger"),
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Divider orientation. |
| `thickness` | `int \| None` | `None` | Border width in pixels (default: 1). |
| `spacing` | `int \| None` | `None` | Margin in Bootstrap spacing units (0–5). |
| `label` | `str \| None` | `None` | Centered text label on the divider. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes (cls, id, etc.). |

---

## Accessibility

- Renders `role="separator"` on the wrapper element.
- Sets `aria-orientation` to match the `orientation` parameter.
- When `label` is provided, the text is wrapped in a `<span>` for screen readers.

---

## API Reference

::: faststrap.components.layout.separator.Separator
    options:
        show_source: true
        heading_level: 4
