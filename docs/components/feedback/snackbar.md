# Snackbar

`Snackbar` is a short, action-oriented feedback surface. `placement="inline"` keeps it in normal document flow; `placement="top"` and `"bottom"` anchor it to the viewport with the shipped Faststrap layout stylesheet and respect device safe areas. Use `Toast` for Bootstrap's global notification container and `ModernToast` for a global polished notification stack.

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
| `placement` | `str` | `"inline"` | `inline` (normal flow), `top`, or `bottom` (viewport-fixed). Top/bottom placement can cover page content; choose it for brief feedback and keep essential controls clear. |
| `duration` | `int \| "infinite"` | `"infinite"` | Metadata for an application auto-dismiss runtime; core does not require JavaScript. |

The component exposes `aria-live`, `aria-atomic`, and a semantic `role`. `duration` is metadata only; it does not automatically dismiss the snackbar. The close button uses Bootstrap's alert dismissal behavior, so Bootstrap JavaScript must be present for that control to dismiss it.

::: faststrap.components.feedback.snackbar.Snackbar
    options:
        show_source: true
