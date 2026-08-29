"""
ML Experiment Tracker - Data Science / Machine Learning Example App

A realistic experiment-tracking page for ML teams, the kind you would use to
manage model training runs from a Python notebook or a FastHTML backend:

- KPI header with MetricCard statistics (runs, best accuracy, GPU hours)
- Runs table with click-to-inspect rows (HTMX, zero custom JS)
- Hyperparameter inspection via JsonViewer
- Training event history via Timeline
- Live epoch progress for a running experiment (AutoRefresh polling)
- Status filtering of runs via FilterBar

Run: python app.py  (opens on http://localhost:5030)
"""

from typing import Any

from fasthtml.common import Div, FastHTML, H2, Main, serve

from faststrap import (
    Badge,
    Button,
    Card,
    Col,
    Container,
    DataTable,
    EmptyState,
    FilterBar,
    Input,
    JsonViewer,
    MetricCard,
    Navbar,
    PageHeader,
    Progress,
    Row,
    Select,
    StatusBadge,
    Timeline,
    TimelineItem,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import AutoRefresh

# ----------------------------------------------------------------------------
# App setup
# ----------------------------------------------------------------------------

app = FastHTML()

ml_theme = create_theme(
    primary="#4F46E5",  # indigo
    secondary="#64748B",
    success="#10B981",
    danger="#EF4444",
    warning="#F59E0B",
    info="#3B82F6",
)
add_bootstrap(app, theme=ml_theme, mode="light")

# ----------------------------------------------------------------------------
# Fake experiment store (replace with your DB / tracker API in production)
# ----------------------------------------------------------------------------

EXPERIMENTS = [
    {
        "id": "exp-042",
        "name": "bert-finetune-lr3e5",
        "model": "bert-base",
        "status": "completed",
        "accuracy": 0.914,
        "loss": 0.212,
        "epochs": 4,
        "gpu_hours": 3.2,
        "lr": "3e-5",
        "batch_size": 32,
    },
    {
        "id": "exp-043",
        "name": "bert-finetune-lr5e5",
        "model": "bert-base",
        "status": "completed",
        "accuracy": 0.902,
        "loss": 0.241,
        "epochs": 4,
        "gpu_hours": 3.1,
        "lr": "5e-5",
        "batch_size": 32,
    },
    {
        "id": "exp-044",
        "name": "distill-teacher-v2",
        "model": "distilbert",
        "status": "running",
        "accuracy": 0.871,
        "loss": 0.318,
        "epochs": 6,
        "gpu_hours": 1.8,
        "lr": "2e-5",
        "batch_size": 64,
    },
    {
        "id": "exp-041",
        "name": "baseline-logreg",
        "model": "logreg",
        "status": "failed",
        "accuracy": 0.793,
        "loss": None,
        "epochs": 1,
        "gpu_hours": 0.1,
        "lr": "-",
        "batch_size": 256,
    },
    {
        "id": "exp-045",
        "name": "ensemble-blend",
        "model": "ensemble",
        "status": "queued",
        "accuracy": None,
        "loss": None,
        "epochs": 0,
        "gpu_hours": 0.0,
        "lr": "-",
        "batch_size": "-",
    },
]

STATUS_MAP = {
    "completed": "success",
    "running": "info",
    "failed": "danger",
    "queued": "warning",
}


# ----------------------------------------------------------------------------
# Render helpers
# ----------------------------------------------------------------------------


def kpi_row() -> Div:
    completed = [e for e in EXPERIMENTS if e["status"] == "completed"]
    best = max((e["accuracy"] or 0) for e in EXPERIMENTS)
    gpu_total = sum(e["gpu_hours"] for e in EXPERIMENTS)
    running = [e for e in EXPERIMENTS if e["status"] == "running"]
    return Row(
        Col(
            MetricCard(
                "Completed runs",
                len(completed),
                delta="+2 this week",
                delta_type="up",
                icon="bi-clipboard-check",
            )
        ),
        Col(
            MetricCard(
                "Best accuracy",
                f"{best:.1%}",
                delta="+1.2 pts",
                delta_type="up",
                icon="bi-bullseye",
            )
        ),
        Col(
            MetricCard(
                "GPU hours",
                f"{gpu_total:.1f}h",
                delta="+3.1h",
                delta_type="neutral",
                icon="bi-gpu-card",
            )
        ),
        Col(
            MetricCard(
                "Running now",
                len(running),
                delta="exp-044",
                delta_type="neutral",
                icon="bi-activity",
            )
        ),
        cls="g-3 mb-4",
    )


def runs_table(runs: list[dict[str, Any]] | None = None) -> Div:
    """Runs list where each row loads its detail via HTMX."""
    runs = runs if runs is not None else EXPERIMENTS
    if not runs:
        return EmptyState(
            icon="bi-funnel",
            title="No matching experiments",
            description="Try clearing the status filter.",
        )
    rows = []
    for e in runs:
        acc = f"{e['accuracy']:.1%}" if e["accuracy"] is not None else "-"
        rows.append(
            Div(
                Div(f"#{e['id']}", cls="text-muted small"),
                e["name"],
                Badge(e["model"], variant="secondary"),
                StatusBadge(
                    e["status"].title(), status=STATUS_MAP[e["status"]], show_dot=True
                ),
                acc,
                cls=(
                    "d-flex align-items-center justify-content-between "
                    "border-bottom py-2 px-2 run-row"
                ),
                **{
                    "hx_get": f"/runs/{e['id']}",
                    "hx_target": "#run-detail",
                    "hx_swap": "innerHTML",
                    "role": "button",
                },
            )
        )
    return Card(
        Div(*rows),
        title="Experiments",
        subtitle="Click a row to inspect configuration and training history.",
    )


def run_detail(e: dict[str, Any]) -> Div:
    epochs_done = min(e["epochs"], 4) if e["status"] == "running" else e["epochs"]
    pct = int(100 * epochs_done / e["epochs"]) if e["epochs"] else 0
    events = Timeline(
        TimelineItem(
            "Experiment queued",
            description=f"Model {e['model']} registered with default config.",
            time="09:00",
            icon="bi-inbox",
            variant="secondary",
        ),
        TimelineItem(
            "Training started",
            description=f"lr={e['lr']}, batch_size={e['batch_size']}",
            time="09:02",
            icon="bi-play-fill",
            variant="primary",
            active=e["status"] in ("running", "completed"),
        ),
        TimelineItem(
            f"Checkpoint saved (epoch {epochs_done})",
            description=f"accuracy={e['accuracy'] or '-'}",
            time="10:15",
            icon="bi-save",
            variant="info",
            active=e["status"] == "completed",
        ),
        TimelineItem(
            "Run finished",
            description=(
                "Best model registered to the model registry."
                if e["status"] == "completed"
                else "Waiting for epochs to complete."
            ),
            time="11:30",
            icon="bi-flag-fill",
            variant="success" if e["status"] == "completed" else "secondary",
            active=e["status"] == "completed",
        ),
    )
    return Div(
        Card(
            Progress(
                pct,
                label=(
                    f"Epoch {epochs_done}/{e['epochs'] or '-'} ({pct}%)"
                    if e["epochs"]
                    else "Not started"
                ),
                striped=e["status"] == "running",
                animated=e["status"] == "running",
            ),
            title=f"{e['name']} - training progress",
            footer=Badge(f"status: {e['status']}", variant=STATUS_MAP[e["status"]]),
            cls="mb-4",
        ),
        Row(
            Col(
                Card(
                    JsonViewer(
                        {
                            "id": e["id"],
                            "model": e["model"],
                            "lr": e["lr"],
                            "batch_size": e["batch_size"],
                            "epochs": e["epochs"],
                            "gpu_hours": e["gpu_hours"],
                        },
                        title="Hyperparameters",
                    )
                ),
                md=6,
            ),
            Col(Card(events, title="Training timeline"), md=6),
            cls="g-3",
        ),
        Card(
            DataTable(
                [
                    {"epoch": 1, "train_loss": 0.512, "val_loss": 0.433, "val_acc": 0.842},
                    {"epoch": 2, "train_loss": 0.341, "val_loss": 0.312, "val_acc": 0.877},
                    {"epoch": 3, "train_loss": 0.262, "val_loss": 0.268, "val_acc": 0.895},
                    {"epoch": 4, "train_loss": 0.224, "val_loss": 0.241, "val_acc": 0.902},
                ],
                header_map={"val_acc": "Val Accuracy", "val_loss": "Val Loss"},
                max_rows=4,
            ),
            title="Per-epoch metrics",
            cls="mt-4",
        ),
    )


# ----------------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------------


@app.get("/")
def home() -> Any:
    running = next(e for e in EXPERIMENTS if e["status"] == "running")
    return Container(
        Navbar(
            brand="Experiment Tracker",
            items=[
                ("Runs", "/"),
                ("Datasets", "/"),
                ("Models", "/"),
                ("Reports", "/"),
            ],
        ),
        Main(
            PageHeader(
                "ML Experiments",
                subtitle="Track, compare, and monitor model training runs.",
                eyebrow="MLOps",
                badge=Badge("staging", variant="info"),
                actions=Button("New experiment", variant="primary", icon="bi-plus-lg"),
            ),
            kpi_row(),
            Row(
                Col(
                    Div(
                        FilterBar(
                            Select(
                                "status",
                                options=["all", "completed", "running", "failed", "queued"],
                                label="Status",
                                value="all",
                            ),
                            Input("q", label="Search", placeholder="Filter by name..."),
                            endpoint="/runs/filter",
                            hx_target="#runs-table",
                            apply_label="Apply",
                            reset_label="Reset",
                        ),
                        Div(runs_table(), id="runs-table"),
                    ),
                    lg=5,
                ),
                Col(
                    Div(
                        Card(
                            # AutoRefresh polls the running experiment's progress
                            # every 3 seconds and swaps only the progress fragment.
                            Div(
                                run_detail(running),
                                id=f"progress-{running['id']}",
                            ),
                            AutoRefresh(
                                endpoint=f"/api/progress/{running['id']}",
                                target=f"#progress-{running['id']}",
                                interval=3000,
                            ),
                        ),
                        id="run-detail",
                    ),
                    lg=7,
                ),
                cls="g-4",
            ),
            cls="py-4",
        ),
    )


@app.get("/runs/{run_id}")
def run(run_id: str) -> Any:
    e = next((x for x in EXPERIMENTS if x["id"] == run_id), None)
    if e is None:
        return EmptyState(
            icon="bi-question-circle",
            title="Experiment not found",
            description=f"No experiment with id {run_id!r}.",
        )
    return run_detail(e)


@app.get("/api/progress/{run_id}")
def progress(run_id: str) -> Any:
    """Polled by AutoRefresh; returns just the run detail fragment."""
    e = next((x for x in EXPERIMENTS if x["id"] == run_id), None)
    if e is None:
        return H2("Unknown experiment")
    return run_detail(e)


@app.get("/runs/filter")
def filter_runs(status: str = "all", q: str = "") -> Any:
    """FilterBar endpoint - returns a fresh runs list."""
    runs = EXPERIMENTS
    if status != "all":
        runs = [e for e in runs if e["status"] == status]
    if q:
        runs = [e for e in runs if q.lower() in e["name"].lower()]
    return runs_table(runs)


if __name__ == "__main__":
    serve(port=5030)
