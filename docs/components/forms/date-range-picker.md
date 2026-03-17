# DateRangePicker

Lightweight date range input with HTMX-friendly hooks.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="d-flex flex-wrap gap-3 align-items-end">
      <div class="mb-3">
        <label class="form-label">Start date</label>
        <input type="date" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">End date</label>
        <input type="date" class="form-control">
      </div>
      <button class="btn btn-primary">Apply</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import DateRangePicker

DateRangePicker(
    start_name="start",
    end_name="end",
    auto=True,
)
```
  </div>
</div>

---

## Presets

```python
DateRangePicker(
    presets=[
        ("Last 7 days", "2026-03-10", "2026-03-17"),
        ("Last 30 days", "2026-02-16", "2026-03-17"),
    ],
)
```

---

## HTMX Integration

```python
DateRangePicker(
    endpoint="/reports",
    method="get",
    auto=True,
    hx_target="#results",
    push_url=True,
)
```

---

## Limits and Defaults

Use `min_date`, `max_date`, `start_value`, and `end_value` to control allowed ranges.

For `method="post"`, ensure CSRF protection is enabled.

---

## API Reference

::: faststrap.components.forms.date_range_picker.DateRangePicker
    options:
        show_source: true
        heading_level: 4
