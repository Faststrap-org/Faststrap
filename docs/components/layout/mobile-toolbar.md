# MobileToolbar

Compact mobile app bar with title, optional subtitle, back link, leading slot, and action slot.

```python
from faststrap import Button, MobileToolbar

MobileToolbar(
    "Experiment 42",
    subtitle="Training run",
    back_href="/experiments",
    actions=Button("Stop", variant="danger", size="sm"),
    sticky=True,
)
```

Use `leading` when the back action is not a link, for example an HTMX button or a custom menu trigger. The toolbar is mobile-only when placed in `MobileAppShell(mobile_toolbar=...)`.

::: faststrap.components.layout.mobile_toolbar.MobileToolbar
    options:
        show_source: true
