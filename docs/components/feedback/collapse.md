# Collapse

The `Collapse` component creates show/hide content areas that can be toggled. Perfect for FAQs, expandable sections, and progressive disclosure patterns.

!!! success "Goal"
    Master creating collapsible content, understand Bootstrap collapse classes, and build space-efficient interfaces with expandable sections.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Collapse Documentation](https://getbootstrap.com/docs/5.3/components/collapse/)

---

## Quick Start

```python
from faststrap import Collapse, Button

# Toggle button
Button(
    "Toggle Content",
    variant="primary",
    data_bs_toggle="collapse",
    data_bs_target="#collapseExample"
)

# Collapsible content
Collapse(
    Card("This content can be toggled!"),
    collapse_id="collapseExample"
)
```

---

## Visual Examples

### 1. Initially Visible

```python
Collapse(
    "This content is visible by default",
    collapse_id="demo",
    show=True  # ← Initially visible
)
```

---

### 2. Horizontal Collapse

```python
Button(
    "Toggle Width",
    data_bs_toggle="collapse",
    data_bs_target="#horizontalCollapse"
)

Collapse(
    Div("Content", style={"width": "300px"}),
    collapse_id="horizontalCollapse",
    horizontal=True
)
```

---

### 3. Multiple Targets

```python
# One button toggles multiple collapses
Button(
    "Toggle Both",
    data_bs_toggle="collapse",
    data_bs_target=".multi-collapse"
)

Collapse("First", collapse_id="first", cls="multi-collapse")
Collapse("Second", collapse_id="second", cls="multi-collapse")
```

---

## Common Recipes

### FAQ Section

```python
from faststrap import Collapse, Button, Card

Div(
    # Q1
    Button(
        "How do I get started?",
        variant="link",
        cls="text-start w-100",
        data_bs_toggle="collapse",
        data_bs_target="#faq1"
    ),
    Collapse(
        Card("Install with pip install faststrap", cls="mb-3"),
        collapse_id="faq1"
    ),
    
    # Q2
    Button(
        "Is it free?",
        variant="link",
        cls="text-start w-100",
        data_bs_toggle="collapse",
        data_bs_target="#faq2"
    ),
    Collapse(
        Card("Yes, completely free and open-source!"),
        collapse_id="faq2"
    )
)
```

---

## Bootstrap CSS Classes

| Class | Purpose |
|-------|---------|
| `.collapse` | Base collapse class |
| `.collapse.show` | Visible state |
| `.collapse-horizontal` | Horizontal collapse |

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | Required | Content to show/hide |
| `collapse_id` | `str` | Required | Unique ID for collapse |
| `show` | `bool` | `False` | Initially visible |
| `horizontal` | `bool` | `False` | Collapse horizontally |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.navigation.listgroup.Collapse
    options:
        show_source: true
        heading_level: 4
