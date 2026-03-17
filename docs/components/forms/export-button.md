# ExportButton

Standardized export action for CSV, Excel, JSON, or PDF downloads.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <button class="btn btn-outline-secondary">
      <i class="bi bi-download me-1"></i>
      Export CSV
    </button>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import ExportButton

ExportButton("Export CSV", endpoint="/export", export_format="csv")
```
  </div>
</div>

---

## With DataTable State

```python
from faststrap import DataTable, ExportButton

params = DataTable.export_params(sort="name", direction="asc", search="alice")
ExportButton("Export", endpoint="/export", extra_params=params)
```

---

## GET vs POST

- `method="get"` creates a link or HTMX request
- `method="post"` creates a form submit

```python
ExportButton(
    "Export",
    endpoint="/export",
    method="post",
    export_format="xlsx",
)
```

---

## Custom Filename

```python
ExportButton(
    "Export",
    endpoint="/export",
    filename="report.xlsx",
)
```

---

## HTMX Exports

```python
ExportButton(
    "Export",
    endpoint="/export",
    use_hx=True,
    hx_target="#status",
    hx_swap="innerHTML",
)
```

---

## Security Notes

Validate export formats server-side and require auth. Avoid using untrusted filenames.

---

## API Reference

::: faststrap.components.forms.export_button.ExportButton
    options:
        show_source: true
        heading_level: 4
