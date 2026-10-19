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

## Mobile Card Presentation

The default `mobile_mode="scroll"` preserves the existing semantic table and
responsive horizontal-scrolling behavior. This is often best for analytics and
data-science work where comparing columns matters. For a narrow-screen record
browsing layout, choose `mobile_mode="cards"` or `mobile_mode="stack"`.

Faststrap renders the semantic table at and above the selected breakpoint and
the requested card/stack presentation below it. Both representations use the
same current filtered, sorted, paginated records and wrapper ID. Sort, search,
pagination, and polling continue targeting the same wrapper; no custom
JavaScript is required. The table representation remains in the response so
server-rendered state and responsive resizing stay synchronized.

In local mode (no `endpoint` or `base_url`), Faststrap filters/sorts and slices
the in-memory records before rendering both views. In endpoint mode, your route
must query and pass the current page's rows; `total_rows` supplies the global
count for pagination. Both responsive presentations then render that same
server-provided page.

```python
DataTable(
    files,
    columns=["name", "owner", "size", "updated_at", "internal_id"],
    header_map={
        "name": "File",
        "owner": "Owner",
        "size": "Size",
        "updated_at": "Updated",
    },
    searchable=True,
    pagination=True,
    endpoint="/files",
    mobile_mode="cards",
    mobile_breakpoint="lg",
    mobile_title="name",
    mobile_subtitle="owner",
    mobile_meta=["size", "updated_at"],
    mobile_hidden=["internal_id"],
    mobile_card_cls="shadow-sm",
)
```

### Modes And Field Selection

| `mobile_mode` | Small-screen output |
| --- | --- |
| `"scroll"` (default) | Only the semantic table, using the existing `responsive` behavior. |
| `None` | Only the semantic table; the `responsive` option still controls horizontal overflow. Use this to explicitly disable an alternate mobile presentation. |
| `"cards"` | A responsive grid of individually surfaced record cards. |
| `"stack"` | A vertical sequence of flatter record rows. |

`mobile_breakpoint` accepts Bootstrap breakpoints `sm`, `md`, `lg`, `xl`, and
`xxl`. The table appears at and above that breakpoint; mobile content appears
below it. `mobile_title` defaults to the first data column. `mobile_subtitle`
is optional. If `mobile_meta` is omitted, remaining columns become labeled
metadata; pass an explicit list to choose order, or `[]` to omit metadata.
`mobile_hidden` removes columns from generated mobile output only; the desktop
table is unaffected. Labels come from `header_map` when available, otherwise
the column key is shown.

Unknown names in `mobile_title`, `mobile_subtitle`, `mobile_meta`,
`mobile_hidden`, or `mobile_field_renderers` raise `ValueError` rather than
being silently ignored.

### Custom Field Rendering

Use `mobile_field_renderers` to format values or return composed FastHTML
elements while retaining Faststrap's generated title/metadata layout:

```python
from faststrap import DataTable, StatusBadge

DataTable(
    experiments,
    columns=["name", "status", "accuracy"],
    header_map={"accuracy": "Accuracy"},
    mobile_mode="cards",
    mobile_title="name",
    mobile_meta=["status", "accuracy"],
    mobile_field_renderers={
        "status": lambda value, row: StatusBadge(str(value).title(), status=value),
        "accuracy": lambda value, row: f"{value:.1%}",
    },
)
```

Each field renderer receives `(value, row)`, where `row` is the normalized row
dictionary. Return text or FastHTML content. Field renderers apply only to
metadata fields, not the title or subtitle slots.

### Custom Mobile Cards And Actions

For a different card structure or row-specific actions, provide
`mobile_card_renderer`. It receives one normalized row dictionary and returns
FastHTML content. The result is wrapped in Faststrap's record surface and
receives `mobile_card_cls` and `mobile_card_attrs`:

```python
from fasthtml.common import Div
from faststrap import Button, DataTable, StatusBadge

DataTable(
    jobs,
    columns=["id", "name", "status", "owner"],
    mobile_mode="cards",
    mobile_card_cls="p-3",
    mobile_card_attrs={"data-testid": "job-card"},
    mobile_card_renderer=lambda row: Div(
        Div(row["name"], cls="fw-semibold"),
        StatusBadge(str(row["status"]).title(), status=row["status"]),
        Div(row["owner"], cls="text-muted small"),
        Button(
            "Open job",
            size="sm",
            hx_get=f"/jobs/{row['id']}",
            hx_target="#job-detail",
        ),
        cls="d-grid gap-2",
    ),
)
```

The callable owns its internal markup and may return buttons, links, badges,
or HTMX actions. It does not change the table's filtering, sorting, or
pagination. Actions rendered only in mobile cards are not automatically added
to desktop table cells. `mobile_card_attrs` is copied to every record surface,
so `id` is rejected. If custom markup emits IDs, make them unique per row.

### Mobile Parameters

| Parameter | Type | Default | Meaning |
| --- | --- | --- | --- |
| `mobile_mode` | `"scroll" \| "cards" \| "stack" \| None` | `"scroll"` | Preserve the table, disable alternate presentation, render a card grid, or render stacked rows on small screens. |
| `mobile_breakpoint` | `"sm" \| "md" \| "lg" \| "xl" \| "xxl"` | `"md"` | Breakpoint at which the semantic table replaces the mobile view. |
| `mobile_title` | `str \| None` | `None` | Title column; defaults to the first normalized data column. |
| `mobile_subtitle` | `str \| None` | `None` | Optional subtitle column. |
| `mobile_meta` | `list[str] \| None` | `None` | Ordered metadata columns. Omitted means remaining columns; `[]` means none. |
| `mobile_hidden` | `list[str] \| None` | `None` | Exclude columns from generated mobile presentation only. |
| `mobile_card_cls` | `str \| None` | `None` | Extra class on each mobile record surface. |
| `mobile_card_attrs` | `dict[str, Any] \| None` | `None` | HTML/ARIA/`data_*`/`hx_*` attributes copied to each surface; `id` is rejected. |
| `mobile_field_renderers` | `dict[str, Callable[[Any, dict], Any]] \| None` | `None` | Per-column callable receiving `(value, row)` for generated metadata fields. |
| `mobile_card_renderer` | `Callable[[dict], Any] \| None` | `None` | Custom per-row mobile content; receives normalized row data and returns FastHTML content. |

Field renderers customize selected generated values; the card renderer
replaces the generated layout entirely. With a custom card renderer,
`mobile_title`, `mobile_subtitle`, `mobile_meta`, and
`mobile_field_renderers` do not affect output. `mobile_hidden` is validated
but cannot filter arbitrary custom markup: exclude sensitive fields before
passing records to the component and enforce authorization in the route.

The inactive representation is hidden with responsive CSS display utilities.
Avoid emitting the same hard-coded DOM IDs from both table cells and custom
cards. Use `CollectionView` when the desktop and mobile surfaces are distinct
(such as an Explorer-style browser); use `DataTable` when table operations and
its server-side contract remain central.

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
