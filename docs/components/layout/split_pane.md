# SplitPane

**Planned** · `@experimental`

Two-pane resizable layout for master/detail screens, documentation editors, code inspectors, and productivity apps.

---

## Quick Start

```python
from faststrap.components.layout import SplitPane
from faststrap import Card, ListGroup, ListGroupItem

SplitPane(
    left=Card(
        ListGroup(
            ListGroupItem("Item 1", active=True),
            ListGroupItem("Item 2"),
            ListGroupItem("Item 3"),
        ),
        header="Items",
    ),
    right=Card("Select an item to view details.", header="Detail"),
    initial_ratio="30/70",
)
```

---

## Features

- Resizable divider (drag to adjust pane ratio)
- Collapsible left pane with toggle button
- Responsive: stacks vertically on mobile
- Configurable initial ratio
- Works with any FastHTML/Faststrap content in either pane

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `left` | `Any` | required | Left/master pane content |
| `right` | `Any` | required | Right/detail pane content |
| `initial_ratio` | `str` | `"30/70"` | CSS `grid-template-columns` ratio |
| `collapsible` | `bool` | `False` | Show collapse toggle for left pane |
| `collapsed` | `bool` | `False` | Start with left pane collapsed |
| `divider_width` | `str` | `"4px"` | Width of the draggable divider |
| `min_left` | `str` | `"200px"` | Minimum left pane width |
| `max_left` | `str` | `"50%"` | Maximum left pane width |
| `stack_on` | `"sm" \| "md" \| "lg" \| None` | `"md"` | Breakpoint to stack vertically |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Requires minimal JavaScript for the drag-to-resize interaction (progressive enhancement).
- On mobile, panes stack vertically automatically.
- Marked `@experimental`.
