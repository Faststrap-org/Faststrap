# StickyActionBar

Bottom-sticky action surface for mobile forms, checkout flows, filters, and record detail pages.

```python
from faststrap import Button, StickyActionBar

StickyActionBar(
    Button("Cancel", variant="outline-secondary"),
    Button("Save", variant="primary", type="submit"),
    justify="end",
    stack_at="sm",
)
```

The default includes bottom safe-area padding. Set `safe_area=False` when the bar is already inside another safe-area wrapper. The component does not submit forms or manage state itself; use normal form and HTMX attributes on its child actions.

::: faststrap.components.layout.sticky_action_bar.StickyActionBar
    options:
        show_source: true
