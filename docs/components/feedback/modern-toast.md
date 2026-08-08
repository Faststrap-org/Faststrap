# ModernToast

`ModernToast` is an opinionated alternative to the core Bootstrap `Toast`. It is for polished app-style notifications with configurable position, timing, style, and queue behavior.

Use core `Toast` when you want Bootstrap's native toast structure. Use `ModernToast` when you want a more modern product UI surface.

## Import

```python
from faststrap import ModernToast, ModernToastStack
```

## Basic Usage

```python
ModernToast(
    "Saved",
    "Your changes were applied.",
    intent="success",
)
```

## With Placement, Duration, And Style

```python
ModernToast(
    "Invite sent",
    "We emailed the new team member.",
    intent="success",
    placement=ToastPlacement(position="top-end"),
    duration=4000,
    visual_style="glass",
)
```

## Toast Stack

```python
ModernToastStack(
    ModernToast("Saved", intent="success"),
    ModernToast("Sync delayed", "Trying again soon.", intent="warning"),
    placement=ToastPlacement(position="bottom-end"),
)
```

## With Action

```python
ModernToast(
    "Project archived",
    "You can restore it from settings.",
    intent="warning",
    action={"label": "Undo", "style": "btn-link"},
)
```

## Parameters

### `ModernToast`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `str` | required | Main toast title. |
| `message` | `str \| None` | `None` | Optional message. |
| `intent` | `ToastIntent` | `info` | Semantic intent: `success`, `error`, `warning`, `info`, `loading`. |
| `visual_style` | `ToastStyle` | `glass` | Visual style: `solid`, `soft`, `glass`, `minimal`. |
| `placement` | `ToastPlacement \| None` | `bottom-right` | Position + offset + gutter. |
| `duration` | `int \| "infinite"` | `4000` | Auto-dismiss duration in milliseconds, or `"infinite"` to persist. |
| `icon` | `str \| None` | `None` | Bootstrap icon override. |
| `action` | `ToastAction \| Any \| None` | `None` | Optional action button or component. |
| `cancel` | `ToastAction \| Any \| None` | `None` | Optional cancel button or component. |
| `dismissible` | `bool` | `True` | Shows the close button. |
| `pause_on_hover` | `bool` | `True` | Pause auto-dismiss timer on hover/focus. |
| `animation` | `ToastAnimation` | `slide` | Enter/exit animation: `slide`, `fade`, `zoom`, `none`. |
| `**kwargs` | `Any` | | Extra attributes. |

### `ModernToastStack`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*toasts` | `Any` | | Toast children. |
| `placement` | `ToastPlacement \| None` | `bottom-right` | Stack position + offset + gutter. |
| `gap` | `int` | `2` | Bootstrap grid gap utility suffix. |
| `max_visible` | `int` | `5` | Maximum visible toasts before queueing. |
| `**kwargs` | `Any` | | Extra attributes. |

## Behavior Notes

- `ModernToast` uses a dedicated JS runtime (`modern-toast.js`) for auto-dismiss, keyboard dismiss, pause-on-hover, and swipe-to-dismiss.
- The runtime is loaded automatically when `ModernToast` or `ModernToastStack` is used with `add_bootstrap(app, components=[ModernToast, ...])`.
- `variant`, `position`, and `style` parameters are deprecated but still accepted with `DeprecationWarning`. Use `intent`, `placement`, and `visual_style` instead.

::: faststrap.components.feedback.modern_toast.ModernToast
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.feedback.modern_toast.ModernToastStack
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.feedback.modern_toast.ModernToastStack
    options:
        show_source: true
        heading_level: 3
