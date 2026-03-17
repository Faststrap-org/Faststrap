# FilterBar

Composable filter layout with HTMX integration and optional apply mode.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="d-flex flex-wrap gap-3 align-items-end">
      <div class="mb-3">
        <label class="form-label">Team</label>
        <select class="form-select" multiple>
          <option>Ops</option>
          <option>Data</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Score</label>
        <input type="range" class="form-range" min="0" max="100">
      </div>
      <button class="btn btn-primary">Apply</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import FilterBar, MultiSelect, RangeSlider

FilterBar(
    MultiSelect("team", ("ops", "Ops"), ("data", "Data")),
    RangeSlider("score", min_value=0, max_value=100),
    mode="apply",
)
```
  </div>
</div>

---

## Auto vs Apply Mode

- `mode="auto"` triggers HTMX on change and keyup
- `mode="apply"` renders an Apply button

```python
FilterBar(
    *filters,
    endpoint="/reports",
    mode="auto",
    debounce=400,
)
```

---

## Reset Button

```python
FilterBar(
    *filters,
    mode="apply",
    reset_label="Reset",
    reset_href="/reports",
)
```

---

## HTMX Integration

```python
FilterBar(
    *filters,
    endpoint="/reports",
    method="get",
    hx_target="#results",
    hx_swap="outerHTML",
    push_url=True,
)
```

---

## Layout Control

Use `filters_cls` and `actions_cls` to adjust spacing or alignment.

```python
FilterBar(
    *filters,
    filters_cls="gap-2",
    actions_cls="ms-auto",
)
```

---

## Security Notes

Validate filters server-side. If you use `method="post"`, enable CSRF protection.

---

## API Reference

::: faststrap.components.forms.filter_bar.FilterBar
    options:
        show_source: true
        heading_level: 4
