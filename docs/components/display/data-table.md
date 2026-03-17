# DataTable

`DataTable` is a higher-level table with sorting, search, and pagination built in. It accepts `list[dict]` and pandas or polars DataFrames.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <table class="table table-striped table-hover w-100">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Ada Lovelace</td>
          <td>ada@example.com</td>
          <td>Active</td>
        </tr>
        <tr>
          <td>Alan Turing</td>
          <td>alan@example.com</td>
          <td>Invited</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import DataTable

DataTable(
    data,
    sortable=True,
    searchable=True,
    pagination=True,
    per_page=25,
)
```
  </div>
</div>

---

## Data Sources

`DataTable` accepts:

- `list[dict]`
- pandas `DataFrame`
- polars `DataFrame`

```python
DataTable(
    records,
    columns=["name", "email", "status"],
    header_map={"name": "User", "email": "Email"},
    include_index=False,
)
```

---

## Sorting and Search

Enable sorting and search with flags:

```python
DataTable(
    data,
    sortable=True,
    searchable=True,
    search_placeholder="Search users...",
    search_param="q",
    search_debounce=300,
)
```

Restrict sortable columns with a list:

```python
DataTable(data, sortable=["name", "email"])
```

If you want to control the current state (server-side mode), pass `sort`, `direction`, and `search`.

---

## Pagination

Client-side pagination works for small sets. For server-side pagination, pass `total_rows`.

```python
DataTable(
    data,
    pagination=True,
    page=2,
    per_page=50,
    total_rows=1200,
)
```

---

## Server-Side Contract

When you pass an `endpoint`, DataTable emits these query params:

- `sort`
- `direction`
- `page`
- `per_page`
- `q` (or your `search_param`)
- any `filters` you provide

```python
DataTable(
    data,
    endpoint="/users",
    sortable=True,
    searchable=True,
    pagination=True,
    hx_target="#table",
    hx_swap="outerHTML",
    push_url=True,
)
```

---

## Filters and Base URL

Use `filters` to preserve extra query params in pagination and sort links. Use `base_url` if you are not using HTMX.

```python
DataTable(
    data,
    filters={"team": "ops"},
    base_url="/users",
)
```

---

## Export Integration

Use the helper to reuse the table query state for exports:

```python
from faststrap import DataTable, ExportButton

params = DataTable.export_params(
    sort="name",
    direction="asc",
    search="alice",
    filters={"team": "ops"},
)

ExportButton("Export CSV", endpoint="/export", export_format="csv", extra_params=params)
```

---

## Theming and Layout

`DataTable` respects Bootstrap table styles:

- `striped=True`
- `hover=True`
- `bordered=True`
- `responsive=True` or `responsive="md"`

You can also pass `table_cls` and `table_attrs` to control the inner table element.

---

## Accessibility

`DataTable` renders semantic table markup (`<table>`, `<thead>`, `<tbody>`). Use short, descriptive column names for screen readers.

---

## Security Notes

- Validate `sort` and `direction` server-side to avoid unsafe column injection.
- Enforce `per_page` limits to prevent excessive responses.
- Sanitize search strings before using them in SQL or ORM queries.

---

## API Reference

::: faststrap.components.display.data_table.DataTable
    options:
        show_source: true
        heading_level: 4
