# SplitPane

`@experimental`

Two-pane resizable layout for master/detail screens, documentation editors, code inspectors, productivity apps, and exam question banks.

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
- Minimal JavaScript for drag-to-resize (progressive enhancement)

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `left` | `Any` | required | Left/master pane content |
| `right` | `Any` | required | Right/detail pane content |
| `initial_ratio` | `str` | `"30/70"` | Pane width ratio, e.g. `"30/70"` or `"40/60"` |
| `collapsible` | `bool` | `False` | Show collapse toggle for left pane |
| `collapsed` | `bool` | `False` | Start with left pane collapsed |
| `divider_width` | `str` | `"4px"` | Width of the draggable divider |
| `min_left` | `str` | `"200px"` | Minimum left pane width |
| `max_left` | `str` | `"50%"` | Maximum left pane width |
| `stack_on` | `"sm" \| "md" \| "lg" \| "xl" \| "xxl" \| None` | `"md"` | Breakpoint to stack vertically |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Usage Examples

### Exam Editor

```python
from faststrap import SplitPane, Card, DataTable, Form

SplitPane(
    left=Card(
        DataTable(questions_df, page_size=20),
        header="Question Bank",
    ),
    right=Card(
        Form(
            FormGroup("Question", Input(name="question")),
            FormGroup("Answer", Input(name="answer")),
        ),
        header="Editor",
    ),
    initial_ratio="40/60",
    collapsible=True,
)
```

### Documentation Editor

```python
from faststrap import Markdown, SplitPane

SplitPane(
    left=Markdown(doc_text),
    right=Card("Inspector"),
    initial_ratio="2/1",
    stack_on="lg",
)
```

---

## Notes

- Requires minimal JavaScript for the drag-to-resize interaction (progressive enhancement).
- On mobile, panes stack vertically automatically.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.layout.split_pane.SplitPane
    options:
        show_source: true
        heading_level: 4
