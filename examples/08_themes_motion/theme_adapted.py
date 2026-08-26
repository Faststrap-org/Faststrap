"""
v0.6.0 Theme-Aware Components Demo

Demonstrates:
- Theme overrides with create_theme()
- Component hook classes for custom styling
- NotificationCenter + ExportButton
"""

from fasthtml.common import (
    Div,
    FastHTML,
    H1,
    H5,
    Style,
    serve,
)

from faststrap import (
    Card,
    Col,
    Container,
    DataTable,
    ExportButton,
    FilterBar,
    KPICard,
    MetricCard,
    MultiSelect,
    NotificationCenter,
    RangeSlider,
    Row,
    TrendCard,
    add_bootstrap,
    create_theme,
)

app = FastHTML()

theme = create_theme(
    primary="#4c6fff",
    secondary="#6c757d",
    info="#0dcaf0",
    success="#2fbf71",
)
add_bootstrap(app, theme=theme, mode="light")

THEME_STYLE = Style("""
.faststrap-metric-card { border: 1px solid var(--bs-primary-border-subtle); }
.faststrap-trend-card { background: var(--bs-primary-bg-subtle); }
.faststrap-kpi-card { background: var(--bs-tertiary-bg); }
.faststrap-multi-select { border-color: var(--bs-primary); }
.faststrap-range-slider .form-range { accent-color: var(--bs-primary); }
.faststrap-notification-toggle { color: var(--bs-primary); }
.faststrap-export-button { min-width: 8rem; }
.faststrap-data-table .table { --bs-table-bg: var(--bs-body-bg); }
""".strip())

DATA = [
    {"name": "Ada", "team": "Platform", "score": 91},
    {"name": "Bola", "team": "Ops", "score": 84},
    {"name": "Chidi", "team": "Data", "score": 96},
]


@app.get("/")
def home():
    return Container(
        THEME_STYLE,
        Div(
            H1("Theme-Aware Components", cls="mb-4"),
            NotificationCenter(
                ("New report ready", "/reports/1"),
                ("Server maintenance scheduled", "/status"),
                count=2,
                center_id="notif-demo",
            ),
            Row(
                Col(MetricCard("Revenue", "$128k", delta="+12%", delta_type="up")),
                Col(
                    TrendCard("Active Users", "9,842", sparkline="<svg></svg>", sparkline_safe=True)
                ),
                Col(
                    KPICard(
                        "KPIs",
                        metrics=[
                            ("Retention", "84%", "+2%", "up"),
                            ("Churn", "3.1%", "-0.4%", "down"),
                        ],
                    )
                ),
                cls="g-4 my-4",
            ),
            Card(
                H5("Filters"),
                FilterBar(
                    MultiSelect(
                        "team",
                        ("platform", "Platform"),
                        ("ops", "Ops"),
                        ("data", "Data"),
                        selected=["data"],
                        label="Teams",
                    ),
                    RangeSlider("score", min_value=0, max_value=100, value=75, label="Score"),
                    mode="apply",
                ),
                cls="mb-4",
            ),
            Card(
                H5("DataTable"),
                DataTable(DATA, sortable=True, searchable=True, table_id="theme-table"),
                cls="mb-4",
            ),
            Div(
                ExportButton("Export CSV", endpoint="/export", export_format="csv"),
                cls="d-flex gap-2",
            ),
        ),
        cls="my-5",
    )


@app.get("/export")
def export():
    return "Export handled server-side"


if __name__ == '__main__':
    serve()
