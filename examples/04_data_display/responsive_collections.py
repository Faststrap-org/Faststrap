"""Progressive examples for Faststrap's responsive collection components.

Run from the repository root:
    python examples/04_data_display/responsive_collections.py

Open http://localhost:5041. The page moves from basic composition to
record-rendered views and a filterable, paginated HTMX file browser.
"""

from math import ceil
from urllib.parse import urlencode

from fasthtml.common import (
    H1,
    H2,
    H3,
    A,
    Div,
    FastHTML,
    Form,
    Input,
    Label,
    Main,
    P,
    Span,
    Titled,
    serve,
)
from fasthtml.common import (
    Select as HtmlSelect,
)

from faststrap import (
    Avatar,
    Button,
    Card,
    CollectionView,
    Container,
    EmptyState,
    GridList,
    Icon,
    ListItem,
    ListView,
    Navbar,
    Pagination,
    StatusBadge,
    ViewToggle,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")

FILES = [
    {
        "id": "f-001",
        "name": "Year 10 lesson plan.pdf",
        "folder": "Science / Physics",
        "kind": "PDF",
        "size": "1.2 MB",
        "updated": "10 min ago",
        "status": "ready",
    },
    {
        "id": "f-002",
        "name": "Term 2 results.csv",
        "folder": "Assessments / 2026",
        "kind": "CSV",
        "size": "84 KB",
        "updated": "Yesterday",
        "status": "ready",
    },
    {
        "id": "f-003",
        "name": "Lab safety guide.md",
        "folder": "Science / Shared",
        "kind": "Markdown",
        "size": "18 KB",
        "updated": "2 days ago",
        "status": "review",
    },
    {
        "id": "f-004",
        "name": "Cell structure diagram.png",
        "folder": "Science / Biology",
        "kind": "Image",
        "size": "640 KB",
        "updated": "3 days ago",
        "status": "ready",
    },
    {
        "id": "f-005",
        "name": "Attendance export.csv",
        "folder": "Administration",
        "kind": "CSV",
        "size": "52 KB",
        "updated": "4 days ago",
        "status": "ready",
    },
    {
        "id": "f-006",
        "name": "Electricity practical.pdf",
        "folder": "Science / Physics",
        "kind": "PDF",
        "size": "920 KB",
        "updated": "Last week",
        "status": "review",
    },
    {
        "id": "f-007",
        "name": "Student directory.json",
        "folder": "Administration",
        "kind": "JSON",
        "size": "210 KB",
        "updated": "Last week",
        "status": "ready",
    },
    {
        "id": "f-008",
        "name": "Plant growth observations.csv",
        "folder": "Science / Biology",
        "kind": "CSV",
        "size": "33 KB",
        "updated": "2 weeks ago",
        "status": "review",
    },
    {
        "id": "f-009",
        "name": "School crest.png",
        "folder": "Brand / Images",
        "kind": "Image",
        "size": "310 KB",
        "updated": "2 weeks ago",
        "status": "ready",
    },
    {
        "id": "f-010",
        "name": "Chemistry equations.md",
        "folder": "Science / Chemistry",
        "kind": "Markdown",
        "size": "27 KB",
        "updated": "3 weeks ago",
        "status": "ready",
    },
]


def page_shell(*content, cls=None):
    """Wrap a route in the shared app chrome."""
    return Titled(
        "Responsive collections",
        Navbar(brand="Faststrap examples", brand_href="/", expand="lg"),
        Main(
            Container(Div(*content, cls=cls) if cls else content, cls="py-5"),
            cls="bg-body-tertiary min-vh-100",
        ),
    )


def file_row(file):
    """Render one file as a three-line, keyboard-operable list row."""
    status = StatusBadge(
        "Ready" if file["status"] == "ready" else "Needs review",
        status="success" if file["status"] == "ready" else "warning",
    )
    return ListItem(
        leading=Icon("file-earmark", cls="fs-4 text-primary"),
        title=file["name"],
        subtitle=file["folder"],
        meta=Span(file["size"], status, cls="d-flex align-items-center gap-2"),
        href=f"/files/{file['id']}",
        lines=3,
        density="comfortable",
    )


def file_card(file):
    """Render one file as a card with a type icon, metadata, and actions."""
    icon_name = {
        "Image": "file-earmark-image",
        "PDF": "file-earmark-pdf",
        "CSV": "filetype-csv",
        "JSON": "filetype-json",
        "Markdown": "filetype-md",
    }.get(file["kind"], "file-earmark")
    preview = Div(
        Icon(icon_name, cls="display-4 text-primary"),
        cls="d-flex align-items-center justify-content-center bg-body-tertiary rounded",
        style={"height": "150px"},
    )
    status = StatusBadge(
        "Ready" if file["status"] == "ready" else "Needs review",
        status="success" if file["status"] == "ready" else "warning",
    )
    return Card(
        preview,
        P(file["folder"], cls="small text-muted mb-1"),
        P(file["size"], cls="small mb-0"),
        header=Div(file["name"], cls="fw-semibold"),
        footer=Div(
            status,
            Button("Open", href=f"/files/{file['id']}", size="sm", cls="ms-auto"),
            cls="d-flex align-items-center gap-2",
        ),
        cls="h-100",
    )


def matching_files(q: str, kind: str):
    """Filter the in-memory demo data; replace this with a database query."""
    query = q.strip().casefold()
    return [
        file
        for file in FILES
        if (not query or query in file["name"].casefold() or query in file["folder"].casefold())
        and (not kind or file["kind"].casefold() == kind.casefold())
    ]


def explorer_panel(q: str, kind: str, view: str, page: int):
    """Render the entire HTMX-swappable file-browser fragment."""
    view = view if view in {"list", "grid"} else "list"
    matches = matching_files(q, kind)
    per_page = 4
    total_pages = max(1, ceil(len(matches) / per_page))
    page = min(max(page, 1), total_pages)
    visible_files = matches[(page - 1) * per_page : page * per_page]
    query_params = {"q": q or None, "kind": kind or None, "view": view}
    endpoint = "/files?" + urlencode({key: value for key, value in query_params.items() if value})

    return Div(
        Div(
            Form(
                Div(
                    Label("Search files", fr="file-query", cls="form-label"),
                    Input(
                        name="q",
                        id="file-query",
                        value=q,
                        placeholder="Try 'physics' or 'results'",
                    ),
                    cls="col-md-6",
                ),
                Div(
                    Label("File type", fr="file-kind", cls="form-label"),
                    HtmlSelect(
                        "kind",
                        ("", "All types", not kind),
                        ("PDF", "PDF", kind == "PDF"),
                        ("CSV", "CSV", kind == "CSV"),
                        ("Markdown", "Markdown", kind == "Markdown"),
                        ("Image", "Image", kind == "Image"),
                        id="file-kind",
                    ),
                    cls="col-md-3",
                ),
                Div(
                    Button("Apply filters", type="submit", cls="w-100"),
                    cls="col-md-3 d-flex align-items-end",
                ),
                method="get",
                action="/files",
                hx_get="/files",
                hx_target="#file-browser",
                hx_swap="outerHTML",
                hx_push_url="true",
                cls="row g-3 align-items-end",
            ),
            ViewToggle(
                value=view,
                endpoint=endpoint,
                options=("list", "grid"),
                labels={"list": "Rows", "grid": "Cards"},
                hx_target="#file-browser",
                hx_swap="outerHTML",
                push_url=True,
            ),
            cls="d-flex flex-column flex-lg-row justify-content-between gap-3 mb-4",
        ),
        H3(f"{len(matches)} files", cls="h5 mb-3"),
        CollectionView(
            records=visible_files,
            mode=view,
            list_renderer=file_row,
            card_renderer=file_card,
            list_density="comfortable",
            grid_min_width="15rem",
            gap=3,
            label="Filtered files",
            empty=EmptyState(
                Icon("folder-x"),
                title="No files match these filters",
                description="Clear the search or choose another file type.",
            ),
        ),
        Pagination(
            current_page=page,
            total_pages=total_pages,
            base_url="/files",
            query_params=query_params,
            htmx=True,
            hx_target="#file-browser",
            hx_swap="outerHTML",
            hx_push_url=True,
            align="center",
            cls="mt-4",
        ),
        P(
            f"Showing {len(visible_files)} of {len(matches)} matching files. "
            "Search, filters, view mode, and page are preserved in the URL.",
            cls="small text-muted text-center mt-3",
        ),
        id="file-browser",
        cls="p-3 p-lg-4 bg-body rounded-4 border shadow-sm",
    )


@app.get("/")
def home():
    """Beginner and moderate examples, with a link to the interactive browser."""
    basic_profiles = ListView(
        ListItem(
            leading=Avatar(name="Ada Lovelace"),
            title="Ada Lovelace",
            subtitle="Mathematics department",
            meta="Active now",
            trailing=StatusBadge("Instructor", status="info"),
            href="/people/ada",
        ),
        ListItem(
            leading=Avatar(name="Grace Hopper"),
            title="Grace Hopper",
            subtitle="Computer science department",
            meta="Last active yesterday",
            trailing=StatusBadge("Administrator", status="success"),
            selected=True,
        ),
        label="Team members",
        density="comfortable",
        divided=True,
    )

    loading_and_empty = Div(
        ListView(loading=True, loading_content="Loading recent activity..."),
        ListView(
            empty=EmptyState(title="Nothing here yet", description="New items will appear here.")
        ),
        cls="d-grid gap-3",
    )

    moderate = CollectionView(
        records=FILES[:4],
        mode="grid",
        list_renderer=file_row,
        card_renderer=file_card,
        grid_min_width="15rem",
        gap=3,
        label="Recent files as cards",
        empty="No recent files.",
    )

    return page_shell(
        H1("Responsive collections", cls="display-5 fw-bold"),
        P(
            "Compose record views from Faststrap primitives. Start with a row, "
            "move to record renderers, then explore a working filterable browser.",
            cls="lead text-muted mb-5",
        ),
        Div(
            Card(
                H2("1. Simple: build rows from slots", cls="h4"),
                P(
                    "Use leading/content/trailing slots, native links, selected states, "
                    "and density. Children remain ordinary FastHTML components.",
                    cls="text-muted",
                ),
                basic_profiles,
                cls="h-100",
            ),
            Card(
                H2("2. Simple: auto-fit a grid", cls="h4"),
                P(
                    "GridList is responsive by default when columns is omitted. "
                    "Set min_width and gap instead of scattering layout CSS.",
                    cls="text-muted",
                ),
                GridList(
                    Card("3,420 rows", header="Physics results", cls="h-100"),
                    Card("18 datasets", header="Biology practicals", cls="h-100"),
                    min_width="12rem",
                    gap=3,
                    label="Science data collections",
                ),
                cls="h-100",
            ),
            cls="row g-4 mb-4",
        ),
        Div(
            Card(
                H2("3. States: empty and loading", cls="h4"),
                loading_and_empty,
                cls="h-100",
            ),
            Card(
                H2("4. Moderate: render records", cls="h4"),
                P(
                    "CollectionView separates the record shape from list/card markup. "
                    "The selected mode chooses the renderer.",
                    cls="text-muted",
                ),
                moderate,
                cls="h-100",
            ),
            cls="row g-4 mb-5",
        ),
        Card(
            H2("5. Complex: a working file browser", cls="h4"),
            P(
                "The next route combines CollectionView renderers, ViewToggle, "
                "query-preserving pagination, filtering, empty states, "
                "and HTMX fragment swaps.",
                cls="text-muted",
            ),
            Button("Open the interactive file browser", href="/files", variant="primary"),
            cls="p-4",
        ),
        cls="vstack gap-3",
    )


@app.get("/files")
def files_page(request, q: str = "", kind: str = "", view: str = "list", page: int = 1):
    """Serve the full page or just the HTMX-swapped browser fragment."""
    panel = explorer_panel(q, kind, view, page)
    if request.headers.get("HX-Request") == "true":
        return panel
    return page_shell(
        A("Back to examples", href="/", cls="text-decoration-none"),
        H1("File browser", cls="mt-3"),
        P(
            "Try search, filter by file type, switch rows/cards, and page through "
            "the same query-preserving server-rendered collection.",
            cls="text-muted mb-4",
        ),
        panel,
    )


@app.get("/files/{file_id}")
def file_detail(file_id: str):
    """Small detail target used by the example's ordinary file links."""
    file = next((item for item in FILES if item["id"] == file_id), None)
    if file is None:
        return EmptyState(title="File not found", description="This is an in-memory demo record.")
    return Card(
        H2(file["name"], cls="h5"),
        P(f"Folder: {file['folder']}"),
        P(f"Type: {file['kind']} / Size: {file['size']}"),
        Button("Back to browser", href="/files", variant="outline-secondary", size="sm"),
        cls="p-3",
    )


if __name__ == "__main__":
    serve(port=5041)
