# SegmentedControl

Accessible single-choice control for compact filters, view modes, and time ranges. It accepts existing `Button` or link elements, so HTMX and ordinary navigation remain available without custom JavaScript.

```python
from faststrap import Button, SegmentedControl

SegmentedControl(
    Button("Overview", variant="outline-primary"),
    Button("Metrics", variant="outline-primary"),
    name="view",
    values=["overview", "metrics"],
    active_index=1,
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*options` | `Any` | required | Buttons, links, or other option elements. |
| `name` | `str \| None` | `None` | Optional hidden-input name for form submission. |
| `values` | `list[str] \| None` | `None` | Values aligned with the options. |
| `active_index` | `int` | `0` | Server-rendered active option index. |
| `orientation` | `str` | `"horizontal"` | `horizontal` or `vertical`. |
| `active_cls` | `str` | `"active"` | Class added to the active option. |
| `hidden_input` | `bool` | `True` | Add the hidden input when `name` is provided. |

For HTMX-driven filters, put `hx_get`, `hx_target`, and `hx_push_url` on the option elements and render the selected state from the request parameters.

::: faststrap.components.forms.segmented_control.SegmentedControl
    options:
        show_source: true

The control is a server-rendered group, not a keyboard-managed ARIA radio group. Button options retain native button semantics and expose `aria-pressed`; link options remain links and use `aria-current` when active. The component does not claim radio-arrow-key behavior or add client-side selection JavaScript.

When `name` is provided, the optional hidden input contains the currently rendered selection. It is not automatically updated when a user clicks an ordinary button. For submissions, use HTMX/server rendering to return the updated selected state, or use native links/forms appropriate to the workflow.
