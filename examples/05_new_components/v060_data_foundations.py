"""
v0.6.0 Data Foundations Demo

Demonstrates:
- DataTable (sortable, searchable, paginated)
- Chart (inline SVG)
- MetricCard, TrendCard, KPICard
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)

DATA = [
    {"name": "Amina", "department": "Operations", "score": 92},
    {"name": "Tobi", "department": "Finance", "score": 88},
    {"name": "Chen", "department": "Engineering", "score": 96},
    {"name": "Lara", "department": "Growth", "score": 84},
    {"name": "Sam", "department": "Product", "score": 90},
    {"name": "Nora", "department": "Design", "score": 86},
]

SPARKLINE = (
    "<svg viewBox='0 0 120 32' width='120' height='32' aria-hidden='true'>"
    "<polyline fill='none' stroke='currentColor' stroke-width='2' "
    "points='0,24 20,18 40,20 60,12 80,14 100,8 120,10'/>"
    "</svg>"
)

CHART_SVG = (
    "<svg viewBox='0 0 320 180' width='100%' height='180' aria-hidden='true'>"
    "<rect width='320' height='180' fill='#f8f9fa'/>"
    "<polyline fill='none' stroke='#0d6efd' stroke-width='3' "
    "points='10,140 70,110 130,120 190,80 250,90 310,60'/>"
    "</svg>"
)


def _apply_query(data, q: str | None, sort: str | None, direction: str | None):
    filtered = data
    if q:
        q_lower = q.lower()
        filtered = [
            row
            for row in data
            if q_lower in row["name"].lower() or q_lower in row["department"].lower()
        ]

    if sort in {"name", "department", "score"}:
        reverse = direction == "desc"
        filtered = sorted(filtered, key=lambda row: row[sort], reverse=reverse)

    return filtered


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.6.0 Data Foundations", cls="mb-4"),
        Row(
            Col(MetricCard("Revenue", "$128k", delta="+12%", delta_type="up")),
            Col(TrendCard("Active Users", "9,842", sparkline=SPARKLINE, sparkline_safe=True)),
            Col(
                KPICard(
                    "KPIs",
                    metrics=[
                        ("Retention", "84%", "+2%", "up"),
                        ("Churn", "3.1%", "-0.4%", "down"),
                    ],
                )
            ),
            cls="g-4 mb-4",
        ),
        Card(
            H5("DataTable"),
            DataTable(
                DATA,
                sortable=True,
                searchable=True,
                pagination=True,
                page=1,
                per_page=3,
                total_rows=len(DATA),
                endpoint="/table",
                table_id="demo-table",
            ),
            cls="mb-4",
        ),
        Card(
            H5("Chart"),
            Chart(CHART_SVG, backend="svg", allow_unsafe_html=True, height=180),
        ),
        cls="my-5",
    )


@app.get("/table")
def table(
    q: str | None = None,
    sort: str | None = None,
    direction: str | None = None,
    page: int = 1,
    per_page: int = 3,
):
    filtered = _apply_query(DATA, q, sort, direction)
    return DataTable(
        filtered,
        sortable=True,
        searchable=True,
        search=q,
        sort=sort,
        direction=direction or "asc",
        pagination=True,
        page=page,
        per_page=per_page,
        total_rows=len(filtered),
        endpoint="/table",
        table_id="demo-table",
    )


serve()
