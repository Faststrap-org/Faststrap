# Switcher

`@experimental`

Responsive adaptive panel layout. Displays side-by-side on desktop and switches to stacked single-column on mobile. Ideal for summary cards, settings pages, and split-content layouts.

---

## Quick Start

```python
from faststrap.components.layout import Switcher
from faststrap import Card

Switcher(
    Card("Chart goes here", header="Revenue"),
    Card("Stats go here", header="Summary"),
    breakpoint="md",
    gap=3,
)
```

---

## Features

- Automatic side-by-side to stacked transition at a configurable breakpoint
- Equal or custom column ratio via CSS Grid
- Configurable gap between panels
- Works with any FastHTML/Faststrap content
- Pure CSS — no JavaScript required

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | required | Two or more panel contents |
| `breakpoint` | `"sm" \| "md" \| "lg" \| "xl" \| "xxl"` | `"md"` | Breakpoint to switch from column to row |
| `ratio` | `str \| None` | `None` | CSS `grid-template-columns` (e.g. `"1fr 2fr"`) |
| `gap` | `int \| str` | `3` | Bootstrap gap utility value or custom CSS gap string |
| `min_item_width` | `str \| None` | `None` | Minimum width before items wrap when using `ratio` |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Usage Examples

### Basic Side-by-Side

```python
from faststrap import Card, Switcher

Switcher(
    Card("Left panel"),
    Card("Right panel"),
    breakpoint="md",
    gap=4,
)
```

### Custom Column Ratio

```python
Switcher(
    Card("Sidebar", header="Navigation"),
    Card("Main content", header="Dashboard"),
    ratio="1fr 3fr",
    breakpoint="lg",
)
```

### Minimum Item Width

```python
Switcher(
    Card("A"),
    Card("B"),
    Card("C"),
    ratio="repeat(auto-fit, minmax(250px, 1fr))",
    min_item_width="250px",
)
```

---

## Notes

- Pure CSS layout using Bootstrap flex utilities or CSS Grid.
- Different from `SplitPane` — `Switcher` is not resizable and is designed for content that should reflow, not be split.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.layout.switcher.Switcher
    options:
        show_source: true
        heading_level: 4
