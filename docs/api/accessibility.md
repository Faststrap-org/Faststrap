# Accessibility API

These helpers provide small, composable accessibility primitives. They do not replace semantic HTML, keyboard testing, or application-specific focus management; they make common patterns explicit in a FastHTML tree.

## Choosing A Helper

| Helper | Use it for |
| --- | --- |
| `SkipLink` | A keyboard-first jump to the main content landmark. |
| `LiveRegion` | Announcing dynamic status or result changes to assistive technology. |
| `VisuallyHidden` | Screen-reader text that should not occupy visible layout space. |
| `FocusTrap` | Keeping keyboard focus inside a modal-like region while it is active. |

## Example

```python
from faststrap import FocusTrap, LiveRegion, SkipLink, VisuallyHidden

def accessible_layout(*content):
    return (
        SkipLink(target="#main-content"),
        LiveRegion(id="status", politeness="polite"),
        VisuallyHidden("Application navigation"),
        FocusTrap(*content, autofocus_selector="#main-content"),
    )
```

Use a real `<main id="main-content">` landmark in the page and update a live region only for meaningful state changes. `FocusTrap` adds the focus-management hooks; the dialog's open/close lifecycle remains the application's responsibility.

## API Reference

::: faststrap.accessibility.SkipLink
    options:
        show_source: true
        heading_level: 2

::: faststrap.accessibility.LiveRegion
    options:
        show_source: true
        heading_level: 2

::: faststrap.accessibility.VisuallyHidden
    options:
        show_source: true
        heading_level: 2

::: faststrap.accessibility.FocusTrap
    options:
        show_source: true
        heading_level: 2
