"""Progressive DataTable examples for narrow-screen data workflows.

Run from the repository root:
    python examples/04_data_display/datatable_mobile_views.py

Open http://localhost:5042. Compare scroll, generated-card, and stacked-row
presentations, then use the interactive server-paginated experiment table.
"""

from math import ceil

from fasthtml.common import H1, H2, Div, FastHTML, Form, Label, Main, P, Titled, serve

from faststrap import (
    Badge,
    Button,
    Card,
    Container,
    DataTable,
    EmptyState,
    MetricCard,
    Navbar,
    Row,
    Select,
    StatusBadge,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")

EXPERIMENTS = [
    {
        "id": f"exp-{index:03d}",
        "name": name,
        "model": model,
        "status": status,
        "accuracy": accuracy,
        "owner": owner,
        "updated": updated,
    }
    for index, (name, model, status, accuracy, owner, updated) in enumerate(
        [
            ("baseline-logreg", "Logistic regression", "completed", 0.793, "Amina", "Today"),
            ("bert-finetune-lr3e5", "BERT", "completed", 0.914, "Chen", "Today"),
            ("distill-teacher-v2", "DistilBERT", "running", 0.871, "Lara", "5 min ago"),
            ("ensemble-blend", "Ensemble", "queued", None, "Tobi", "Queued"),
            ("vision-resnet-18", "ResNet-18", "completed", 0.946, "Nora", "Yesterday"),
            ("fraud-xgb-v5", "XGBoost", "failed", 0.821, "Sam", "Yesterday"),
            ("forecast-arima", "ARIMA", "completed", 0.882, "Amina", "2 days ago"),
            ("text-topic-v4", "Transformer", "running", 0.903, "Chen", "2 min ago"),
            ("tabular-catboost", "CatBoost", "completed", 0.927, "Lara", "3 days ago"),
            ("vision-vit-base", "ViT", "queued", None, "Nora", "Queued"),
            ("churn-lightgbm", "LightGBM", "completed", 0.901, "Tobi", "4 days ago"),
            ("speech-conformer", "Conformer", "failed", 0.756, "Sam", "Last week"),
        ],
        start=1,
    )
]

STATUS_LABELS = {
    "completed": ("Completed", "success"),
    "running": ("Running", "info"),
    "queued": ("Queued", "pending"),
    "failed": ("Failed", "error"),
}


def page_shell(*content, cls=None):
    return Titled(
        "DataTable mobile views",
        Navbar(brand="Faststrap examples", brand_href="/", expand="lg"),
        Main(
            Container(Div(*content, cls=cls) if cls else content, cls="py-5"),
            cls="bg-body-tertiary min-vh-100",
        ),
    )


def status_badge(value, row):
    """Format a status field as a semantic Faststrap badge."""
    label, status = STATUS_LABELS.get(str(value), (str(value).title(), "neutral"))
    return StatusBadge(label, status=status)


def accuracy_label(value, row):
    """Format an optional metric without losing a meaningful zero value."""
    return "Not available" if value is None else f"{value:.1%}"


@app.get("/")
def home():
    """Beginner and moderate recipes, then a link to the full server example."""
    records = EXPERIMENTS[:5]

    simple = DataTable(
        records,
        columns=["name", "model", "status", "accuracy"],
        header_map={"name": "Experiment", "status": "State", "accuracy": "Accuracy"},
        responsive=True,
        pagination=True,
        per_page=4,
        mobile_mode="cards",
        mobile_title="name",
        mobile_subtitle="model",
        mobile_meta=["status", "accuracy"],
        mobile_field_renderers={"status": status_badge, "accuracy": accuracy_label},
        mobile_breakpoint="md",
    )

    stacked = DataTable(
        records,
        columns=["id", "name", "owner", "status", "updated"],
        header_map={"id": "Run ID", "updated": "Last updated"},
        sortable=True,
        mobile_mode="stack",
        mobile_title="name",
        mobile_subtitle="owner",
        mobile_meta=["status", "updated"],
        mobile_field_renderers={"status": status_badge},
        mobile_hidden=["id"],
        mobile_card_cls="px-3",
    )

    return page_shell(
        H1("DataTable mobile presentations", cls="display-5 fw-bold"),
        P(
            "Keep a semantic table for wide screens and choose a focused record "
            "presentation for phones. The default remains the responsive table.",
            cls="lead text-muted mb-5",
        ),
        Div(
            Card(
                H2("1. Simple: generated mobile cards", cls="h4"),
                P(
                    "Select a title, subtitle, and ordered metadata. A field renderer "
                    "adds rich formatting without replacing the generated layout.",
                    cls="text-muted",
                ),
                simple,
                cls="h-100",
            ),
            Card(
                H2("2. Moderate: flatter stacked rows", cls="h4"),
                P(
                    "Use stack for dense mobile scanning. Hidden fields stay in the "
                    "desktop table; labels come from header_map.",
                    cls="text-muted",
                ),
                stacked,
                cls="h-100",
            ),
            cls="row g-4 mb-5",
        ),
        Card(
            H2("3. Complex: server-side workflow", cls="h4"),
            P(
                "The experiment route below handles search, sorting, pagination, "
                "preserved filters, a selectable mobile mode, and custom card actions. "
                "Its endpoint returns only the current server-selected page.",
                cls="text-muted",
            ),
            Button("Open experiment table", href="/experiments", variant="primary"),
            cls="p-4 mb-4",
        ),
        H2("Reference recipes", cls="h4"),
        Div(
            Card(
                H2("Keep the current table", cls="h5"),
                P("Use None to disable the alternate card/stack rendering."),
                DataTable(records, responsive=True, mobile_mode=None),
            ),
            Card(
                H2("Choose the existing scroll behavior", cls="h5"),
                P("This is the backward-compatible default."),
                DataTable(records, responsive=True, mobile_mode="scroll"),
            ),
            cls="row g-4",
        ),
    )


def experiment_table(
    *,
    q: str,
    sort: str | None,
    direction: str,
    page: int,
    per_page: int,
    mobile_mode: str | None,
):
    """Render the current server page and matching card/table representations."""
    allowed_columns = {"name", "model", "status", "accuracy", "owner", "updated"}
    filtered = [
        row
        for row in EXPERIMENTS
        if not q or q.casefold() in " ".join(str(value) for value in row.values()).casefold()
    ]
    if sort in allowed_columns:
        filtered.sort(
            key=lambda row: (row.get(sort) is None, row.get(sort)), reverse=direction == "desc"
        )

    total_rows = len(filtered)
    safe_per_page = min(max(per_page, 1), 10)
    total_pages = max(1, ceil(total_rows / safe_per_page))
    safe_page = min(max(page, 1), total_pages)
    start = (safe_page - 1) * safe_per_page
    page_rows = filtered[start : start + safe_per_page]

    return DataTable(
        page_rows,
        columns=["id", "name", "model", "status", "accuracy", "owner", "updated"],
        header_map={
            "id": "Run ID",
            "name": "Experiment",
            "accuracy": "Accuracy",
            "updated": "Last updated",
        },
        sortable=True,
        searchable=True,
        search=q,
        search_placeholder="Search run, model, status, or owner...",
        pagination=True,
        page=safe_page,
        per_page=safe_per_page,
        total_rows=total_rows,
        endpoint="/experiments/table",
        filters={"mobile_mode": mobile_mode or "none"},
        mobile_mode=mobile_mode,
        mobile_breakpoint="lg",
        mobile_title="name",
        mobile_subtitle="model",
        mobile_meta=["status", "accuracy", "owner", "updated"],
        mobile_hidden=["id"],
        mobile_field_renderers={"status": status_badge, "accuracy": accuracy_label},
        mobile_card_cls="p-3",
        mobile_card_attrs={"data-testid": "experiment-card"},
        mobile_card_renderer=lambda row: (
            Div(
                Div(row["name"], cls="fw-semibold fs-5"),
                Div(row["model"], cls="small text-muted"),
                Div(
                    status_badge(row["status"], row),
                    Badge(accuracy_label(row["accuracy"], row), variant="primary"),
                    cls="d-flex flex-wrap gap-2",
                ),
                Div(f"Owner: {row['owner']} / Updated: {row['updated']}", cls="small"),
                Button(
                    "Inspect run",
                    size="sm",
                    hx_get=f"/experiments/{row['id']}",
                    hx_target="#experiment-detail",
                    hx_swap="innerHTML",
                ),
                cls="d-grid gap-2",
            )
            if mobile_mode == "cards"
            else None
        ),
        hx_target="#experiment-table",
        hx_swap="outerHTML",
        push_url=True,
        table_id="experiment-table",
        empty_text="No experiment runs match this search.",
    )


@app.get("/experiments")
def experiments_page(mobile_mode: str = "cards"):
    """Full page with a normal GET selector for the table presentation."""
    mode = mobile_mode if mobile_mode in {"scroll", "cards", "stack", "none"} else "cards"
    data_mode = None if mode == "none" else mode
    return page_shell(
        H1("Experiment runs", cls="mb-2"),
        P(
            "This route simulates a database-backed list endpoint. Search and "
            "table links request the current page from the server.",
            cls="text-muted mb-4",
        ),
        Form(
            Div(
                Label("Small-screen presentation", fr="mobile-mode", cls="form-label"),
                Select(
                    "mobile_mode",
                    ("cards", "Cards", mode == "cards"),
                    ("stack", "Stacked rows", mode == "stack"),
                    ("scroll", "Responsive table", mode == "scroll"),
                    ("none", "Table only (None)", mode == "none"),
                    id="mobile-mode",
                ),
                cls="col-md-5",
            ),
            Button("Apply presentation", type="submit", cls="align-self-end"),
            method="get",
            action="/experiments",
            cls="d-flex flex-wrap align-items-end gap-3 mb-4",
        ),
        Card(
            experiment_table(
                q="",
                sort=None,
                direction="asc",
                page=1,
                per_page=5,
                mobile_mode=data_mode,
            ),
            cls="p-3 p-lg-4",
        ),
        Div(
            EmptyState(
                title="Select an experiment",
                description="Use an Inspect run action in the mobile card view.",
            ),
            id="experiment-detail",
            cls="mt-4",
        ),
        cls="vstack gap-2",
    )


@app.get("/experiments/table")
def experiments_table(
    q: str = "",
    sort: str | None = None,
    direction: str = "asc",
    page: int = 1,
    per_page: int = 5,
    mobile_mode: str = "cards",
):
    """HTMX endpoint: filter/sort/page in Python and return one DataTable."""
    mode = mobile_mode if mobile_mode in {"scroll", "cards", "stack", "none"} else "cards"
    return experiment_table(
        q=q,
        sort=sort,
        direction=direction if direction in {"asc", "desc"} else "asc",
        page=page,
        per_page=per_page,
        mobile_mode=None if mode == "none" else mode,
    )


@app.get("/experiments/{run_id}")
def experiment_detail(run_id: str):
    """HTMX card action target demonstrating detail inspection."""
    row = next((item for item in EXPERIMENTS if item["id"] == run_id), None)
    if row is None:
        return EmptyState(title="Run not found", description="The demo data is in memory.")
    accuracy = accuracy_label(row["accuracy"], row)
    label, status = STATUS_LABELS[row["status"]]
    return Card(
        H2(row["name"], cls="h5"),
        Row(
            MetricCard("Model", row["model"]),
            MetricCard("Accuracy", accuracy),
            MetricCard("Owner", row["owner"]),
            cls="g-3",
        ),
        StatusBadge(label, status=status),
        cls="p-4",
    )


if __name__ == "__main__":
    serve(port=5042)
