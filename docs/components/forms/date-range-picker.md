# DateRangePicker

Lightweight date range input with optional preset shortcuts and HTMX integration.

## Quick Start

```python
DateRangePicker(start_name="start", end_name="end", auto=True)
```

## Usage Scenarios

### Presets

```python
DateRangePicker(
    start_name="start",
    end_name="end",
    presets=[
        ("Last 7 days", "2026-03-10", "2026-03-17"),
        ("Last 30 days", "2026-02-16", "2026-03-17"),
    ],
)
```

### HTMX Integration

```python
DateRangePicker(
    start_name="start",
    end_name="end",
    endpoint="/reports",
    method="get",
    auto=True,
    hx_target="#results",
    push_url=True,
)
```

### Limits and Defaults

```python
DateRangePicker(
    start_name="start",
    end_name="end",
    start_value="2026-01-01",
    end_value="2026-03-17",
    min_date="2026-01-01",
    max_date="2026-12-31",
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `start_name` | `str` | `"start_date"` | Start date field name. |
| `end_name` | `str` | `"end_date"` | End date field name. |
| `start_label` | `str` | `"Start date"` | Start date label. |
| `end_label` | `str` | `"End date"` | End date label. |
| `start_value` | `str \| None` | `None` | Initial start date in `YYYY-MM-DD` format. |
| `end_value` | `str \| None` | `None` | Initial end date in `YYYY-MM-DD` format. |
| `min_date` | `str \| None` | `None` | Earliest selectable date. |
| `max_date` | `str \| None` | `None` | Latest selectable date. |
| `presets` | `list[tuple[str, str, str]] \| None` | `None` | Preset buttons as `(label, start, end)`. |
| `endpoint` | `str \| None` | `None` | Form action and optional HTMX endpoint. |
| `method` | `"get" \| "post"` | `"get"` | Submit method. |
| `auto` | `bool` | `False` | Submit on change when an endpoint exists. |
| `apply_label` | `str \| None` | `"Apply"` | Submit button label. Set `None` to hide. |
| `hx_target` | `str \| None` | `None` | HTMX target selector. |
| `hx_swap` | `str \| None` | `"outerHTML"` | HTMX swap style. |
| `push_url` | `bool` | `False` | Push URL for HTMX GET flows. |
| `form_cls` / `presets_cls` / `inputs_cls` | `str \| None` | `None` | Styling hooks. |
| `**kwargs` | `Any` | | Extra form attributes. |

## Accessibility

- Labels are properly associated with date inputs.
- For `method="post"`, ensure CSRF protection is enabled.
- Preset shortcuts rely on the Faststrap runtime from `add_bootstrap(app)`.

## API Reference

::: faststrap.components.forms.date_range_picker.DateRangePicker
    options:
        show_source: true
        heading_level: 4
