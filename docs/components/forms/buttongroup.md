# ButtonGroup

The `ButtonGroup` component groups related buttons together for toolbars, segmented controls, and action sets. Creates a seamless, professional appearance by merging adjacent buttons.

!!! success "Goal"
    Master creating button groups and toolbars, understand Bootstrap btn-group classes, and build cohesive action controls that improve UI organization.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Button Group Documentation](https://getbootstrap.com/docs/5.3/components/button-group/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="btn-group" role="group">
      <button type="button" class="btn btn-primary">Left</button>
      <button type="button" class="btn btn-primary">Middle</button>
      <button type="button" class="btn btn-primary">Right</button>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import ButtonGroup, Button

ButtonGroup(
    Button("Left", variant="primary"),
    Button("Middle", variant="primary"),
    Button("Right", variant="primary")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Sizes

```python
# Large
ButtonGroup(
    Button("One", variant="primary"),
    Button("Two", variant="primary"),
    Button("Three", variant="primary"),
    size="lg"
)

# Small
ButtonGroup(
    Button("One", variant="secondary"),
    Button("Two", variant="secondary"),
    size="sm"
)
```

---

### 2. Vertical Groups

```python
ButtonGroup(
    Button("Top", variant="outline-primary"),
    Button("Middle", variant="outline-primary"),
    Button("Bottom", variant="outline-primary"),
    vertical=True
)
```

---

### 3. Button Toolbar - Multiple Groups

```python
from faststrap import ButtonToolbar, ButtonGroup, Button

ButtonToolbar(
    ButtonGroup(
        Button("1"), Button("2"), Button("3"), Button("4")
    ),
    ButtonGroup(
        Button("5"), Button("6"), Button("7")
    ),
    ButtonGroup(
        Button("8")
    )
)
```

---

## Bootstrap CSS Classes Explained

| Class | Purpose |
|-------|---------|
| `.btn-group` | Horizontal button group |
| `.btn-group-vertical` | Vertical button group |
| `.btn-group-lg` | Large size |
| `.btn-group-sm` | Small size |
| `.btn-toolbar` | Groups multiple button groups |

---

## Common Recipes

### Text Editor Toolbar

```python
from faststrap import ButtonToolbar, ButtonGroup, Button, Icon

ButtonToolbar(
    ButtonGroup(
        Button(Icon("type-bold"), variant="outline-secondary"),
        Button(Icon("type-italic"), variant="outline-secondary"),
        Button(Icon("type-underline"), variant="outline-secondary"),
        size="sm"
    ),
    ButtonGroup(
        Button(Icon("list-ul"), variant="outline-secondary"),
        Button(Icon("list-ol"), variant="outline-secondary"),
        size="sm"
    ),
    ButtonGroup(
        Button(Icon("link"), variant="outline-secondary"),
        size="sm"
    )
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*buttons` | `Any` | Required | Button components |
| `size` | `"sm" \| "lg" \| None` | `None` | Group size |
| `vertical` | `bool` | `False` | Stack vertically |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.forms.buttongroup.ButtonGroup
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.buttongroup.ButtonToolbar
    options:
        show_source: true
        heading_level: 4
