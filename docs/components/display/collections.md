# Responsive Collections

Faststrap's collection components compose lists, grids, and record cards from
ordinary FastHTML elements. They work for files, users, products, lessons,
datasets, experiment runs, and other browsable records. The components are
data-agnostic: your application owns fetching, authorization, and persistence.

Use a collection when people browse items as individual records. Use
[`DataTable`](data-table.md) when comparing columns, sorting, filtering,
pagination, or export is central to the task.

## Choose A Composition

| Need | Use | What it provides |
| --- | --- | --- |
| A single flexible record row | `ListItem` | Leading/content/trailing slots and interaction states. |
| A vertical sequence of rows | `ListView` | Shared density, dividers, empty, and loading presentation. |
| An auto-fitting CSS grid | `GridList` | Responsive card placement without JavaScript. |
| One server-selected list or grid | `CollectionView` | Composes rendered items or records through renderers. |
| A bookmarkable list/grid selector | `ViewToggle` | Query-parameter links, optionally upgraded with HTMX. |
| A table that changes presentation on small screens | `DataTable(mobile_mode=...)` | Retains table behavior and offers mobile cards or stacked rows. |

These are presentation primitives, not a client-side collection framework.
They do not fetch records, manage selection state, or implement client-side
sorting. Let FastHTML routes and HTMX own those behaviors.

## Quick Start

```python
from faststrap import Avatar, CollectionView, ListItem

people = CollectionView(
    ListItem(
        title="Ada Lovelace",
        subtitle="Mathematics department",
        meta="Active now",
        leading=Avatar(name="Ada Lovelace"),
        trailing="Administrator",
        href="/people/ada",
    ),
    ListItem(
        title="Grace Hopper",
        subtitle="Computer science department",
        meta="Last active yesterday",
        leading=Avatar(name="Grace Hopper"),
        trailing="Instructor",
        href="/people/grace",
    ),
    mode="list",
    label="People",
)
```

## ListItem

`ListItem` lays out a record summary with optional leading, central, and
trailing content. Its slots accept FastHTML elements, so compose `Avatar`,
`Icon`, `Badge`, `Button`, checkboxes, and other components rather than
embedding framework-specific behavior in the row.

```python
from faststrap import Badge, Button, Icon, ListItem

ListItem(
    leading=Icon("file-earmark-pdf", cls="fs-4 text-danger"),
    title="Q3 report.pdf",
    subtitle="Finance team",
    meta="2.4 MB - Updated 10 minutes ago",
    trailing=Badge("PDF", variant="danger"),
    href="/files/q3-report",
    density="comfortable",
)
```

For an action on the row itself, use `href` or pass supported `hx_*` attributes
to the component. Keep nested actions such as the example button intentional:
interactive controls nested inside a link are invalid HTML; prefer a non-link
`ListItem` with a trailing action button when the row also has an action.

```python
ListItem(
    title="Deployment #1842",
    subtitle="Production / us-east",
    meta=Badge("Healthy", variant="success"),
    leading=Icon("rocket-takeoff"),
    trailing=Button("Open", href="/deployments/1842", size="sm"),
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | `()` | Content; the first child becomes the title when `title` is omitted. Remaining children are appended to the text area. |
| `title` | `Any \| None` | `None` | Primary line. |
| `subtitle` | `Any \| None` | `None` | Secondary line. |
| `meta` | `Any \| None` | `None` | Tertiary or supporting line; may be a badge or other element. |
| `leading` / `trailing` | `Any \| None` | `None` | Start/end slots for avatars, icons, selection controls, badges, or actions. |
| `href` | `str \| None` | `None` | Render the row as a link. A disabled or loading row suppresses navigation. |
| `selected` | `bool` | `False` | Adds selected styling and `aria-current="true"`. This is presentation only; your route owns the state. |
| `active` | `bool` | `False` | Adds active styling and `aria-current="page"` for link rows. |
| `disabled` | `bool` | `False` | Adds disabled styling and `aria-disabled`; prevents row navigation. |
| `loading` | `bool` | `False` | Shows a Bootstrap spinner, announces loading, and prevents link navigation. |
| `density` | `"compact" \| "comfortable" \| "spacious"` | `"comfortable"` | Controls row padding. |
| `lines` | `1 \| 2 \| 3 \| None` | `None` | Hides lower text lines when set to one or two; three preserves all lines. |
| `cls`, `style`, `css_vars` | Standard Faststrap styling | — | Add custom classes, inline styles, or CSS variables. Other HTML, ARIA, `data_*`, and `hx_*` attributes are accepted. |

`selected`, `active`, `disabled`, and `loading` describe different states.
`selected` and `active` do not create a selection model; set them from your
server-rendered application state. Disabled/loading link rows render as
non-navigable content.

## ListView

`ListView` provides a vertical list surface. Children already carrying
`role="listitem"` (including `ListItem`) remain direct children; other content
is wrapped in a semantic list-item container. These are presentation semantics,
not stateful selection controls. Use it for settings, files, activity feeds,
or compact mobile summaries.

```python
from faststrap import ListItem, ListView

ListView(
    ListItem(title="Notifications", meta="On"),
    ListItem(title="Privacy", meta="Standard"),
    ListItem(title="Appearance", meta="System default"),
    density="compact",
    divided=True,
    label="Account settings",
    empty="No settings are available.",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | FastHTML content | `()` | Child rows or other content. |
| `density` | `"compact" \| "comfortable" \| "spacious"` | `"comfortable"` | Default row-density class for the list surface. Set a row's own density when it needs to differ. |
| `divided` | `bool` | `True` | Show separators between direct child rows. |
| `flush` | `bool` | `False` | Remove outer radius and side borders for edge-to-edge use inside another surface. |
| `label` | `str \| None` | `None` | Accessible name emitted as `aria-label`; provide one for a meaningful list. |
| `empty` | `Any \| None` | `None` | Content shown when there are no child items. No empty message is rendered unless supplied. |
| `loading` | `bool` | `False` | Replace children with `loading_content` and expose it as a status. |
| `loading_content` | `Any` | `"Loading..."` | Text or FastHTML content shown in the loading state. |
| `cls`, `style`, `css_vars` | Standard Faststrap styling | — | Customize the wrapper; standard HTML, ARIA, `data_*`, and `hx_*` attributes are also accepted. |

Loading takes precedence over the items and empty state. The component does not
manage focus or selection: links and buttons in its children retain their
native keyboard behavior. Use explicit `ListItem` link/action semantics rather
than making an entire static list behave like an undocumented widget.

## GridList

`GridList` is a CSS grid for cards, files, products, datasets, or custom
FastHTML content. Children already carrying `role="listitem"` remain direct;
other content is wrapped in a semantic list-item container. With
`columns=None`, CSS uses an auto-fitting responsive
layout based on `min_width`. Setting `columns` fixes the requested track count;
choose a suitable value for the narrowest viewport where that grid is shown.

```python
from faststrap import Card, GridList

GridList(
    Card("Dataset A", header="Sales"),
    Card("Dataset B", header="Retention"),
    Card("Dataset C", header="Forecast"),
    min_width="15rem",
    gap=3,
    label="Available datasets",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | FastHTML content | `()` | Grid children; each is wrapped in a list-item container. |
| `min_width` | `str` | `"16rem"` | Minimum track width in auto-fit mode; accepts a CSS length. |
| `columns` | `int \| None` | `None` | Optional explicit number of tracks; must be at least one. |
| `gap` | `int \| str` | `3` | Integer uses Bootstrap spacing scale (`3` becomes `0.75rem`); a string is emitted as a CSS gap value. |
| `label` | `str \| None` | `None` | Accessible list name. |
| `empty`, `loading`, `loading_content` | `Any`, `bool`, `Any` | `None`, `False`, `"Loading..."` | Optional empty and loading content; loading takes precedence. |
| `cls`, `style`, `css_vars` | Standard Faststrap styling | — | Customize the grid wrapper; standard HTML, ARIA, `data_*`, and `hx_*` attributes are accepted. |

## CollectionView

`CollectionView` chooses list, compact-list, grid, or card-grid presentation.
It supports both already-rendered children and a record-oriented mode. In
record mode, the selected renderer receives one record and returns a FastHTML
element. This keeps persistence and record shape in your application while
making the presentation mapping explicit.

```python
from faststrap import Badge, Card, CollectionView, ListItem

files = [
    {"name": "lesson-plan.pdf", "kind": "PDF", "size": "1.2 MB"},
    {"name": "results.csv", "kind": "CSV", "size": "84 KB"},
]

def file_row(file):
    return ListItem(
        title=file["name"],
        subtitle=file["kind"],
        meta=file["size"],
        href=f"/files/{file['name']}",
    )

def file_card(file):
    return Card(
        file["size"],
        header=file["name"],
        footer=Badge(file["kind"], variant="secondary"),
    )

CollectionView(
    records=files,
    mode="grid",
    list_renderer=file_row,
    card_renderer=file_card,
    grid_min_width="14rem",
    label="Files",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | FastHTML content | `()` | Already-rendered children. Use these when your route has already selected the representation. |
| `mode` | `"list" \| "compact" \| "grid" \| "cards"` | `"list"` | `list` and `compact` use `ListView`; `grid` and `cards` use `GridList`. |
| `records` | `Iterable[Any] \| None` | `None` | Optional raw records. Cannot be combined with positional rendered items. |
| `list_renderer` | `Callable[[Any], Any] \| None` | `None` | Required with `records` in `list` or `compact` mode. Called once per record. |
| `card_renderer` | `Callable[[Any], Any] \| None` | `None` | Required with `records` in `grid` or `cards` mode. Called once per record. |
| `list_density` | `ListDensity` | `"comfortable"` | Density forwarded to list modes. `compact` mode always uses compact density. |
| `grid_min_width` | `str` | `"16rem"` | Minimum auto-fit grid track width. |
| `grid_columns` | `int \| None` | `None` | Optional fixed grid track count. |
| `gap` | `int \| str` | `3` | Grid spacing, following `GridList` rules. |
| `label` | `str \| None` | `None` | Accessible collection name. |
| `empty`, `loading`, `loading_content` | `Any`, `bool`, `Any` | `None`, `False`, `"Loading..."` | Forwarded to the selected list/grid wrapper. Loading content takes precedence and record renderers are not invoked while loading. |
| `cls`, `style`, `css_vars` | Standard Faststrap styling | — | Customize the selected wrapper; standard HTML, ARIA, `data_*`, and `hx_*` attributes are accepted. |

Only the renderer for the current mode is required. A list view does not need a
card renderer until the user selects a grid mode, and vice versa. Do not put
authorization or data fetching inside a renderer; perform those in the route
before rendering.

### Server-Selected View

Keep the selected mode in a query parameter so links are bookmarkable and work
without client-side state:

```python
from fasthtml.common import Div, FastHTML
from faststrap import Button, CollectionView, ListItem, ViewToggle

app = FastHTML()
files = [{"name": "lesson-plan.pdf", "size": "1.2 MB"}]

def render_file_row(file):
    return ListItem(title=file["name"], meta=file["size"])

def render_file_card(file):
    return Button(file["name"], variant="light", cls="w-100")

@app.get("/files")
def files_page(request):
    view = request.query_params.get("view", "list")
    if view not in {"list", "grid"}:
        view = "list"
    return Div(
        ViewToggle(value=view, endpoint="/files", aria_label="Choose file layout"),
        CollectionView(
            records=files,
            mode=view,
            list_renderer=render_file_row,
            card_renderer=render_file_card,
            label="Files",
        ),
    )
```

For a partial update, target the collection wrapper or a parent that includes
both the toggle and results. With `hx_target`, `ViewToggle` emits `hx-get` links;
`hx_swap` defaults to `outerHTML`. Set `push_url=True` if the HTMX navigation
should update the browser URL. Your route must return the fragment expected by
that target.

## ViewToggle

`ViewToggle` renders accessible list/grid/cards controls. With an `endpoint`,
each option is an ordinary link with the selected `param` query value. It
preserves other query parameters and URL fragments, replacing any previous
value for that parameter.

```python
ViewToggle(
    value="grid",
    endpoint="/files?folder=reports&view=list#results",
    param="view",
    options=("list", "grid"),
    labels={"list": "Rows", "grid": "Tiles"},
    hx_target="#file-results",
    hx_swap="outerHTML",
    push_url=True,
    aria_label="Choose file layout",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `"list" \| "grid" \| "cards"` | `"list"` | Currently selected option; it must occur in `options`. |
| `endpoint` | `str \| None` | `None` | When set, render ordinary links to this URL with the selected query parameter. Without it, render buttons with `data-fs-view` for application-owned enhancement. |
| `param` | `str` | `"view"` | Query parameter to replace/add in endpoint mode. Must not be blank. |
| `options` | tuple of allowed modes | `("list", "grid")` | Options to render; must be non-empty and use supported values. |
| `labels` | `dict[str, str] \| None` | `None` | Accessible/display names; defaults to List, Grid, and Cards. |
| `aria_label` | `str` | `"Choose view"` | Accessible name for the control group. |
| `hx_target` | `str \| None` | `None` | Add `hx-get` and target attributes to endpoint links. |
| `hx_swap` | `str` | `"outerHTML"` | HTMX swap strategy used with `hx_target`. |
| `push_url` | `bool` | `False` | Add `hx-push-url="true"` in HTMX endpoint mode. |
| `cls` and standard attrs | — | — | Customize the group; standard HTML, ARIA, and `data_*` attributes are accepted. |

Without an endpoint, `data-fs-view` is only a hook. Faststrap does not ship a
global script that changes `CollectionView` in place; use endpoint mode for
server-rendered interaction or implement your own JavaScript enhancement.

## File Explorer Pattern

The collection primitives intentionally do not impose a file schema or a
`FileCollection` component. Pair them with `FilePreview`, icons, badges, and
actions to build the file-specific surface your application needs. This route
uses the record renderer API and returns the selected view on each request.
The example assumes records contain `id`, `name`, `folder`, `size`, and
`kind`; add a `preview_url` when a card should include an inline preview.

```python
from fasthtml.common import Div
from faststrap import (
    Badge,
    Button,
    Card,
    CollectionView,
    FilePreview,
    Icon,
    ListItem,
    ViewToggle,
)

def render_file_row(file):
    return ListItem(
        leading=Icon("file-earmark"),
        title=file["name"],
        subtitle=file["folder"],
        meta=file["size"],
        trailing=Badge(file["kind"], variant="secondary"),
        href=f"/files/{file['id']}",
    )

def render_file_card(file):
    return Card(
        FilePreview(file["preview_url"], title=file["name"], height=150)
        if file.get("preview_url")
        else Icon("file-earmark", cls="display-4 text-secondary"),
        file["size"],
        header=file["name"],
        footer=Div(
            Badge(file["kind"], variant="secondary"),
            Button("Open", href=f"/files/{file['id']}", size="sm", cls="ms-auto"),
            cls="d-flex align-items-center justify-content-between",
        ),
    )

def file_browser(files, view):
    if view not in {"list", "grid"}:
        view = "list"
    return Div(
        ViewToggle(value=view, endpoint="/files", options=("list", "grid")),
        CollectionView(
            records=files,
            mode=view,
            list_renderer=render_file_row,
            card_renderer=render_file_card,
            grid_min_width="13rem",
            label="Files",
            empty=Div("No files found.", cls="text-muted py-4"),
        ),
    )
```

## Responsive DataTable Presentation

Use `DataTable` when the same records need semantic columns and table
operations, but a phone-sized screen benefits from a more vertical
presentation. Its default remains the existing responsive table. Set
`mobile_mode="cards"` for separate record cards or `mobile_mode="stack"` for
flatter stacked record rows below the breakpoint.

For a custom action area, pass `mobile_card_renderer`; the callable receives
the normalized row dictionary and returns FastHTML content. Use
`mobile_field_renderers` when only selected field values need rich rendering
(for example a `StatusBadge` or formatted metric) while the generated layout
should remain in control.

The custom card callable can include buttons and `hx_*` attributes. Those
actions exist only in the mobile representation; render equivalent actions in
the desktop table's cells if users need them at every viewport size.

See [DataTable: Mobile Card Presentation](data-table.md#mobile-card-presentation)
for field selection, server-side state, accessibility, and a full example.

## Accessibility And Styling

- Give meaningful lists and grids a descriptive `label`.
- Use `href` for navigation rows and native buttons/links for actions.
- Do not place interactive controls inside a link row; use a non-link `ListItem` with a trailing action instead.
- Provide text alternatives for icon-only leading/trailing content.
- Keep important actions visible rather than relying on hover-only controls.
- Selected, active, loading, and disabled styles are states, not selection or focus-management systems.
- Use `cls`, `style`, and `css_vars` for application styling. Core CSS uses Bootstrap utilities and Faststrap surface tokens.
- The components do not implement roving focus or arrow-key navigation. Their children retain native browser keyboard behavior.

## API Reference

::: faststrap.components.display.collections.ListItem
    options:
        show_source: true

::: faststrap.components.display.collections.ListView
    options:
        show_source: true

::: faststrap.components.display.collections.GridList
    options:
        show_source: true

::: faststrap.components.display.collections.CollectionView
    options:
        show_source: true

::: faststrap.components.display.collections.ViewToggle
    options:
        show_source: true
