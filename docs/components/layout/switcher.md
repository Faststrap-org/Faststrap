# Switcher

**Planned** · `@experimental`

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
- Equal or custom column ratio
- Configurable gap between panels
- Works with any FastHTML/Faststrap content
- Pure CSS — no JavaScript required

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | required | Two or more panel contents |
| `breakpoint` | `"sm" \| "md" \| "lg"` | `"md"` | Breakpoint to switch from row to column |
| `ratio` | `str \| None` | `None` | CSS `grid-template-columns` (e.g. `"1fr 2fr"`) |
| `gap` | `int \| str` | `3` | Bootstrap gap utility value |
| `min_item_width` | `str \| None` | `None` | Minimum width before wrapping |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Pure CSS layout using Bootstrap grid utilities.
- Different from `SplitPane` — `Switcher` is not resizable and is designed for content that should reflow, not be split.
- Marked `@experimental`.
