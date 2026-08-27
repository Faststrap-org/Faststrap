# CalendarDatePicker

`CalendarDatePicker` is a single-date picker built around the native HTML `date` input. It is intentionally lightweight and works without custom JavaScript.

Use `DateRangePicker` when users need a start and end date. Use `CalendarDatePicker` when users choose one date, such as a publish date, appointment date, or filter date.

## Import

```python
from faststrap import CalendarDatePicker
```

## Basic Usage

```python
CalendarDatePicker(
    "publish_date",
    label="Publish date",
    value="2026-05-07",
)
```

## Date Limits

```python
CalendarDatePicker(
    "appointment_date",
    label="Appointment date",
    min_date="2026-05-01",
    max_date="2026-05-31",
)
```

## HTMX Filtering

```python
CalendarDatePicker(
    "day",
    label="Activity day",
    endpoint="/activity",
    hx_target="#activity-feed",
    auto=True,
    push_url=True,
)
```

When `auto=True`, the picker submits after the selected date changes.

## With Clear Button

```python
CalendarDatePicker(
    "due_date",
    label="Due date",
    clear_label="Clear",
)
```

## Parameters

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `"date"` | Input name. |
| `label` | `str` | `"Date"` | Label shown above the date input. |
| `value` | `str \| None` | `None` | Initial date in `YYYY-MM-DD` format. |
| `min_date` | `str \| None` | `None` | Earliest selectable date. |
| `max_date` | `str \| None` | `None` | Latest selectable date. |
| `endpoint` | `str \| None` | `None` | Optional form/HTMX endpoint. |
| `method` | `get \| post` | `"get"` | Submission method. |
| `auto` | `bool` | `False` | Submit on date change when an endpoint is present. |
| `apply_label` | `str \| None` | `"Apply"` | Submit button label. Set to `None` to hide. |
| `clear_label` | `str \| None` | `None` | Optional reset button label. |
| `apply_cls` / `clear_cls` | `str \| None` | `None` | Extra classes for the Apply/Clear buttons (e.g. `btn-sm`). |
| `hx_target` | `str \| None` | `None` | HTMX target for responses. |
| `hx_swap` | `str \| None` | `"outerHTML"` | HTMX swap style. |
| `push_url` | `bool` | `False` | Whether HTMX should push the URL. |
| `input_cls` / `form_cls` | `str \| None` | `None` | Styling hooks. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

The input control and the action buttons share one horizontal baseline; GET forms submit via the query string.

::: faststrap.components.forms.calendar_date_picker.CalendarDatePicker
    options:
        show_source: true
        heading_level: 3
