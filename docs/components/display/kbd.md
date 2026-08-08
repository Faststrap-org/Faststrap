# Kbd

`Kbd` renders a styled keyboard key indicator. It wraps content in a semantic `<kbd>` element with Bootstrap-compatible styling, making it easy to document keyboard shortcuts and hotkeys in your UI.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Typography — Keyboard Inputs](https://getbootstrap.com/docs/5.3/content/typography/)

---

## Quick Start

```python
from faststrap import Kbd

Kbd("Ctrl")
Kbd("S", variant="dark")
Kbd("Ctrl", "S")
```

---

## Visual Examples & Use Cases

### 1. Single Keys

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2 align-items-center">
      <kbd class="kbd bg-light text-dark border border-secondary-subtle">Ctrl</kbd>
      <kbd class="kbd bg-dark text-light">S</kbd>
      <kbd class="kbd bg-light text-dark border border-secondary-subtle">Enter</kbd>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Kbd("Ctrl")
Kbd("S", variant="dark")
Kbd("Enter")
```
  </div>
</div>

### 2. Key Combinations

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2 align-items-center">
      <span class="d-flex gap-1">
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">Ctrl</kbd>
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">C</kbd>
      </span>
      <span class="d-flex gap-1">
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">⌘</kbd>
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">K</kbd>
      </span>
      <span class="d-flex gap-1">
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">Ctrl</kbd>
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">Shift</kbd>
        <kbd class="kbd bg-light text-dark border border-secondary-subtle">P</kbd>
      </span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Pass multiple children to render a key combo
Kbd("Ctrl", "C")
Kbd("⌘", "K")
Kbd("Ctrl", "Shift", "P")
```
  </div>
</div>

### 3. Size Variants

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex flex-wrap gap-2 align-items-center">
      <kbd class="kbd kbd-sm bg-light text-dark border border-secondary-subtle">Small</kbd>
      <kbd class="kbd bg-light text-dark border border-secondary-subtle">Medium</kbd>
      <kbd class="kbd kbd-lg bg-light text-dark border border-secondary-subtle">Large</kbd>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Kbd("Small", size="sm")
Kbd("Medium", size="md")
Kbd("Large", size="lg")
```
  </div>
</div>

---

## Practical Functionality

### 1. Inside a Button Tooltip

```python
from faststrap import Button, Tooltip

Button(
    "Save",
    variant="primary",
    data_bs_toggle="tooltip",
    data_bs_title="Save document",
    data_bs_placement="bottom",
)

# In your template:
# <kbd>Ctrl</kbd> + <kbd>S</kbd> to save
```

### 2. Inside an Alert

```python
Alert(
    "Press ",
    Kbd("Ctrl", "K"),
    " to open the command palette.",
    variant="info",
)
```

### 3. In Documentation

```python
from faststrap import Stack

Stack(
    "Keyboard Shortcuts",
    Kbd("Ctrl", "C") + " — Copy",
    Kbd("Ctrl", "V") + " — Paste",
    Kbd("Ctrl", "Z") + " — Undo",
    gap=1,
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Key label content (e.g. `"Ctrl"`, `"⌘"`, `"F1"`). |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Font size variant. |
| `variant` | `"light" \| "dark"` | `"light"` | Color variant: `light` for light backgrounds, `dark` for dark backgrounds. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes (cls, id, etc.). |

---

## Accessibility

- Renders a semantic `<kbd>` element.
- Screen readers will announce the content as keyboard input.

---

## API Reference

::: faststrap.components.display.kbd.Kbd
    options:
        show_source: true
        heading_level: 4
