# Action Buttons

`GradientButton` and `FloatingActionButton` are opinionated button wrappers for polished product interfaces. They compose the core `Button`, so they keep Faststrap's normal button behavior, HTMX attributes, accessible labels, and `type="button"` default.

## Quick Start

```python
from faststrap import FloatingActionButton, GradientButton

GradientButton("Launch", gradient="blue", href="/start")

FloatingActionButton(
    icon="plus",
    variant="success",
    position="bottom-right",
    label="Create item",
    hx_get="/items/new",
    hx_target="#modal",
)
```

## GradientButton

Use `GradientButton` when you want a stronger call-to-action than a default Bootstrap button.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | required | Button content. |
| `gradient` | `purple \| blue \| green \| orange \| pink \| str` | `purple` | Preset or custom CSS gradient. All presets keep ≥3:1 contrast (WCAG non-text/UI) against the default white label. |
| `size` | `sm \| lg \| None` | `None` | Bootstrap button size. |
| `text_color` | `str \| None` | `None` | Label color override for light gradients (via `--faststrap-gradient-button-text`). |
| `hover` | `default \| lift \| glow \| none` | `default` | Hover treatment. |

```python
GradientButton("Start trial", gradient="linear-gradient(135deg, #111827, #22c55e)")
GradientButton("Buy now", gradient="orange", hover="lift")
```

## FloatingActionButton

Use `FloatingActionButton` for a page-level primary action, especially in dashboard and mobile-first layouts.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | empty | Optional visible content. |
| `icon` | `str \| None` | `None` | Bootstrap icon name. |
| `variant` | Bootstrap variant | `primary` | Button color. |
| `position` | `bottom-right \| bottom-left \| top-right \| top-left` | `bottom-right` | Fixed viewport position. |
| `label` | `str \| None` | `Primary action` | Accessible label. |
| `size` | `sm \| md \| lg` | `lg` | Logical size via `--fs-fab-size` (44/48/56px). |
| `offset` | `int \| None` | `2rem` inset | Viewport inset in rem units via `--fs-fab-inset`; reduce on mobile. |
| `shape` | `circle \| pill` | `circle` | `pill` renders an extended icon+label FAB. |

```python
FloatingActionButton(icon="plus", label="Add expense", size="sm", offset=4)
FloatingActionButton("Edit draft", icon="edit", shape="pill")
```

## Notes

- `GradientButton` and `FloatingActionButton` accept normal `Button` kwargs such as `href`, `hx_get`, `hx_target`, `data_bs_toggle`, and `disabled`.
- `hover="none"` fully disables hover/focus treatment (no lift, glow, or brightness shift).
- `FloatingActionButton` validates `position`, `size`, and `shape` at render time and raises `ValueError` for unknown values.
- `faststrap-visual.css` is loaded automatically by `add_bootstrap()`.

## API Reference

::: faststrap.components.forms.action_buttons.GradientButton

::: faststrap.components.forms.action_buttons.FloatingActionButton
