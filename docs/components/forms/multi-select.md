# MultiSelect

Bootstrap multi-select built for FastHTML.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Teams</label>
      <select class="form-select" multiple>
        <option>Platform</option>
        <option>Ops</option>
        <option selected>Data</option>
      </select>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import MultiSelect

MultiSelect(
    "team",
    ("platform", "Platform"),
    ("ops", "Ops"),
    ("data", "Data"),
    selected=["data"],
    label="Teams",
)
```
  </div>
</div>

---

## Sizes and States

```python
MultiSelect(
    "team",
    ("a", "A"),
    ("b", "B"),
    size="sm",
    required=True,
)
```

---

## Help Text

```python
MultiSelect(
    "team",
    ("a", "A"),
    ("b", "B"),
    help_text="Choose one or more teams.",
)
```

---

## Server Handling

Multi-select inputs submit multiple values. On the server, use the framework's list access for query params or form data.

---

## API Reference

::: faststrap.components.forms.multi_select.MultiSelect
    options:
        show_source: true
        heading_level: 4
