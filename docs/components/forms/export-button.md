# Export Button

The `ExportButton` component generates export buttons for CSV, Excel, JSON, and PDF downloads.

## Quick Start

```python
ExportButton("Export", endpoint="/api/export", export_format="csv")
```

## Usage Scenarios

### Excel Export

```python
ExportButton("Download Excel", endpoint="/api/export", export_format="xlsx", filename="report.xlsx")
```

### JSON with Extra Params

```python
ExportButton("Export JSON", endpoint="/api/export", export_format="json", extra_params={"include_archived": True})
```

### HTMX Download

```python
ExportButton("Export", endpoint="/api/export", export_format="csv", use_hx=True, hx_target="#result", variant="success")
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `label` | `str` | `"Export"` | Button label text |
| `endpoint` | `str \| None` | `None` | Export endpoint URL |
| `export_format` | `"csv" \| "xlsx" \| "json" \| "pdf"` | `"csv"` | Export file format |
| `filename` | `str \| None` | `None` | Suggested filename for download |
| `method` | `"get" \| "post"` | `"get"` | HTTP method |
| `use_hx` | `bool` | `False` | Use HTMX for the request |
| `hx_target` | `str \| None` | `None` | HTMX target selector |
| `hx_swap` | `str \| None` | `"none"` | HTMX swap style |
| `push_url` | `bool` | `False` | Push URL for HTMX GET flows |
| `variant` | `str \| None` | UNSET | Bootstrap variant |
| `outline` | `bool` | `True` | Use outline style |
| `icon` | `str \| None` | `"download"` | Bootstrap icon name |
| `extra_params` | `dict \| None` | `None` | Extra query/body parameters |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Button uses semantic `<button>` or `<a>` tag based on method.
- Icons use `aria-hidden="true"`.
- Download attribute is set when `filename` is provided.

## API Reference

::: faststrap.components.forms.export_button.ExportButton
    options:
        show_source: true
        heading_level: 4
