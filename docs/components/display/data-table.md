# DataTable

`DataTable` is a higher-level table with sorting, search, and pagination built in. It accepts `list[dict]` and pandas or polars DataFrames.

!!! warning "Beta API"
    `DataTable` is currently marked `@beta`. It is stable enough for real apps, but query contracts and helper ergonomics may still evolve in minor releases.

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
    endpoint="/users",
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

Enable sorting and search with flags. For interactive controls, provide `endpoint` or `base_url` so header links and search submits have a stable request target:

```python
DataTable(
    data,
    sortable=True,
    searchable=True,
    search_placeholder="Search users...",
    search_param="q",
    search_debounce=300,
    endpoint="/users",
)
```

Restrict sortable columns with a list:

```python
DataTable(data, sortable=["name", "email"])
```

If you want to control the current state (server-side mode), pass `sort`, `direction`, and `search`.

---

## Pagination

Client-side pagination works for small sets when you render the full dataset locally. For server-side pagination, pass `total_rows` with `endpoint` or `base_url`.

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

## Server-Side Pagination Cookbook

When your dataset exceeds a few hundred rows, you should paginate server-side. This section shows the complete round-trip pattern.

### Server Route

Your FastHTML route reads the query params emitted by `DataTable`, validates them, queries your database, and returns the rendered table:

```python
from fasthtml.common import FastHTML, Titled
from faststrap import DataTable

app = FastHTML()

ALLOWED_SORT = {"name", "email", "created_at", "status"}

@app.get("/users")
def users_page(sort: str = "name", direction: str = "asc",
                page: int = 1, per_page: int = 25, q: str = ""):
    # Validate sort column
    if sort not in ALLOWED_SORT:
        sort = "name"
    if direction not in ("asc", "desc"):
        direction = "asc"
    per_page = min(max(per_page, 1), 100)  # clamp

    # Query your database here (example uses in-memory data)
    data = query_users(sort=sort, direction=direction,
                       search=q, page=page, per_page=per_page)
    total = count_users(search=q)

    return Titled(
        "Users",
        DataTable(
            data,
            sortable=True,
            searchable=True,
            pagination=True,
            page=page,
            per_page=per_page,
            total_rows=total,
            sort=sort,
            direction=direction,
            search=q,
            endpoint="/users",
            hx_target="#users-table",
            hx_swap="outerHTML",
            push_url=True,
            id="users-table",
        ),
    )
```

### Client-Side Rendering

On the initial page load, render the table with `endpoint` pointing to your server route:

```python
from faststrap import DataTable

DataTable(
    initial_data,
    sortable=True,
    searchable=True,
    pagination=True,
    per_page=25,
    total_rows=total_count,
    endpoint="/users",
    hx_target="#users-table",
    hx_swap="outerHTML",
    push_url=True,
    id="users-table",
)
```

### What Happens

1. User clicks a column header → `DataTable` emits HTMX GET to `/users?sort=name&direction=desc&page=1`
2. Server validates `sort`/`direction`, queries the database, returns the re-rendered table
3. HTMX swaps the table body via `hx_swap="outerHTML"`
4. `push_url=True` updates the browser URL so the current state is shareable

### Helper Functions

Use the helper functions to reuse the current query state for export buttons, links, and related actions:

```python
from faststrap import datatable_query_params, datatable_page_url, datatable_export_params

# Build a link to page 3 with current sort/search preserved
url = datatable_page_url("/users", page=3, sort="email", direction="asc", search="alice")

# Build export params matching the current table state
params = datatable_export_params(sort="name", direction="desc", search="bob", filters={"team": "ops"})

# Build query params for custom links
qp = datatable_query_params(sort="created_at", direction="desc", page=2, per_page=50)
```

These helpers are available both as top-level imports and as convenience attributes on `DataTable`:

```python
DataTable.query_params(sort="name", direction="asc")
DataTable.export_params(sort="name", filters={"active": True})
DataTable.page_url("/users", page=5, per_page=25)
```
---

## Filters and Base URL

Use `filters` to preserve extra query params in pagination and sort links. Use `base_url` if you are not using HTMX. When you pass `sort` or `search`, DataTable applies that state to the rendered rows so the UI stays consistent with the current request.

```python
DataTable(
    data,
    filters={"team": "ops"},
    base_url="/users",
)
```

---

## Export Integration

Use the helpers to reuse the table query state for exports, links, and handlers. They are available both as top-level helpers and as convenience attributes on `DataTable`:

```python
from faststrap import datatable_export_params, ExportButton

params = datatable_export_params(
    sort="name",
    direction="asc",
    search="alice",
    filters={"team": "ops"},
)

ExportButton("Export CSV", endpoint="/export", export_format="csv", extra_params=params)
```

Build the same query contract for non-export actions:

```python
from faststrap import datatable_query_params

params = datatable_query_params(
    sort="name",
    direction="asc",
    search="alice",
    filters={"team": "ops"},
    page=2,
    per_page=25,
)
```

Build one page URL while preserving table state:

```python
from faststrap import datatable_page_url

url = datatable_page_url(
    "/users?view=active",
    page=3,
    per_page=25,
    sort="name",
    search="alice",
    filters={"team": "ops"},
)
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

::: faststrap.components.display.data_table.datatable_export_params
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.display.data_table.datatable_query_params
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.display.data_table.datatable_page_url
    options:
        show_source: true
        heading_level: 4
