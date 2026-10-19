# SafeArea

Adds CSS `env(safe-area-inset-*)` padding or margin for phones with a display cutout or home indicator. It is CSS-only and safe on browsers that report zero insets.

```python
from faststrap import SafeArea

SafeArea(
    "Mobile actions",
    edges="bottom",
    cls="bg-body border-top",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | `()` | Wrapped content. |
| `edges` | `str` | `"all"` | `all`, `top`, `right`, `bottom`, `left`, `vertical`, or `horizontal`. |
| `mode` | `str` | `"padding"` | Apply the inset as `padding` or `margin`. |
| `**kwargs` | `Any` | | HTML, HTMX, and class attributes. |

Use `edges="bottom"` around fixed bottom navigation and action bars; use `edges="top"` for full-screen mobile headers.

::: faststrap.components.layout.safe_area.SafeArea
    options:
        show_source: true
