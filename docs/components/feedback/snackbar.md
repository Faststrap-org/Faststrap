# Snackbar

`Snackbar` is an anchored, action-oriented feedback surface. Use it near the content that changed; use `Toast` for Bootstrap's global notification container and `ModernToast` for a global polished notification stack.

```python
from faststrap import Button, Snackbar

Snackbar(
    "Your draft is saved.",
    title="Saved",
    action=Button("Undo", variant="link"),
    placement="bottom",
    duration=4000,
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | required | Message content. |
| `variant` | `str` | `"dark"` | Bootstrap feedback variant. |
| `title` | `str \| None` | `None` | Optional title above the message. |
| `action` | `Any \| None` | `None` | Action control such as `Button("Undo")`. |
| `icon` | `str \| None` | `None` | Bootstrap icon name. |
| `dismissible` | `bool` | `True` | Include a Bootstrap alert dismiss control. |
| `placement` | `str` | `"inline"` | `inline`, `top`, or `bottom` anchoring class. |
| `duration` | `int \| "infinite"` | `"infinite"` | Metadata for an application auto-dismiss runtime; core does not require JavaScript. |

The component exposes `aria-live`, `aria-atomic`, and a semantic `role`. Duration is intentionally progressive: applications can add their own runtime or use HTMX response timing without requiring a new client-side framework.

::: faststrap.components.feedback.snackbar.Snackbar
    options:
        show_source: true
