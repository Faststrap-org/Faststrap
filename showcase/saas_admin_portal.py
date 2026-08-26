"""Flagship showcase — SaaS Admin Portal.

Production-grade SaaS admin dashboard for Faststrap:

- create_theme() with modern SaaS palette (slate/indigo)
- Custom CSS for premium admin aesthetic
- SplitPane for resizable master/detail layout
- SearchBar for global search
- ProfileDropdown for user menu
- DataCard for account metadata
- DashboardGrid, DataTable, Chart, Card, Button, Form
- FilterBar, DateRangePicker, ExportButton
- AutoRefresh for live metrics
- Fx animations throughout
- Port 5022
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    A,
    Button,
    Div,
    FastHTML,
    H1,
    H2,
    H3,
    H4,
    Input,
    Link,
    P,
    Script,
    Small,
    Span,
    Style,
    Table,
    Tbody,
    Td,
    Tfoot,
    Th,
    Thead,
    Tr,
    serve,
)

from faststrap import (
    Card,
    Chart,
    Col,
    Container,
    DashboardGrid,
    DataCard,
    DataTable,
    DateRangePicker,
    ExportButton,
    FilterBar,
    MetricCard,
    Navbar,
    ProfileDropdown,
    Row,
    SearchBar,
    Select,
    SplitPane,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import AutoRefresh, hx_refresh

THEME_KEY = "admin_theme"

ADMIN_THEME = create_theme(
    primary="#4f46e5",
    secondary="#64748b",
    success="#22c55e",
    danger="#ef4444",
    warning="#f59e0b",
    info="#3b82f6",
)

app = FastHTML()
add_bootstrap(app, theme=ADMIN_THEME, font_family="Inter")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
  --admin-indigo: #4f46e5;
  --admin-slate: #64748b;
}

.admin-shell {
  min-height: 100vh;
  background: #f1f5f9;
  color: #0f172a;
}

.admin-shell[data-bs-theme="dark"] {
  background: #0b1220;
  color: #e2e8f0;
}

.admin-nav {
  background: #fff !important;
  border-bottom: 1px solid #e2e8f0;
}

.admin-shell[data-bs-theme="dark"] .admin-nav {
  background: rgba(15,23,42,0.95) !important;
  border-bottom: 1px solid rgba(148,163,184,0.12);
}

.admin-sidebar {
  background: #fff;
  border-right: 1px solid #e2e8f0;
  min-height: calc(100vh - 56px);
}

.admin-shell[data-bs-theme="dark"] .admin-sidebar {
  background: rgba(15,23,42,0.95);
  border-right: 1px solid rgba(148,163,184,0.12);
}

.admin-card {
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  background: #fff;
  transition: box-shadow 0.2s, transform 0.2s;
}

.admin-shell[data-bs-theme="dark"] .admin-card {
  background: rgba(30,41,59,0.6);
  border-color: rgba(148,163,184,0.10);
}

.admin-card:hover {
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  transform: translateY(-1px);
}

.admin-footer {
  background: #fff;
  border-top: 1px solid #e2e8f0;
  padding: 1.5rem 0;
}

.admin-shell[data-bs-theme="dark"] .admin-footer {
  background: rgba(15,23,42,0.95);
  border-top: 1px solid rgba(148,163,184,0.10);
}
"""

ACCOUNTS = [
    {"id": "ACC-001", "name": "Acme Corp", "plan": "Enterprise", "mrr": "$2,400", "health": "Healthy", "region": "North America"},
    {"id": "ACC-002", "name": "Globex Inc", "plan": "Business", "mrr": "$850", "health": "At Risk", "region": "Europe"},
    {"id": "ACC-003", "name": "Initech", "plan": "Starter", "mrr": "$120", "health": "Watch", "region": "Asia Pacific"},
    {"id": "ACC-004", "name": "Umbrella Co", "plan": "Enterprise", "mrr": "$3,100", "health": "Healthy", "region": "North America"},
]


def account_row(acc: dict) -> Any:
    return Tr(
        Td(acc["id"]),
        Td(acc["name"]),
        Td(acc["plan"]),
        Td(acc["mrr"]),
        Td(acc["health"]),
        Td(acc["region"]),
    )


@app.get("/")
def home(req) -> Any:
    theme = req.session.get(THEME_KEY, "light")
    return Div(
        Style(CSS),
         Navbar(
            SearchBar(
                placeholder="Search accounts, metrics, settings...",
                endpoint="/search",
                target="#search-results",
                cls="me-3",
            ),
            ThemeToggle(current_theme=theme, endpoint="/theme/toggle"),
            ProfileDropdown(
                "Alex Johnson",
                subtitle="Admin",
                items=[
                    ("Profile", "/profile"),
                    ("Settings", "/settings"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="AdminHub",
            brand_href="/",
            items=[
                {"text": "Dashboard", "href": "/"},
                {"text": "Accounts", "href": "/accounts"},
                {"text": "Settings", "href": "/settings"},
            ],
            variant="light",
            bg="light",
            expand="lg",
            sticky="top",
            cls="admin-nav",
        ),
        Container(
            Row(
                Col(
                    MetricCard(
                        "MRR",
                        "$48.2k",
                        delta="+3.1%",
                        delta_type="up",
                        variant="success",
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    MetricCard(
                        "Active Accounts",
                        "1,247",
                        delta="+18",
                        delta_type="up",
                        variant="primary",
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    MetricCard(
                        "Churn Rate",
                        "1.8%",
                        delta="-0.2%",
                        delta_type="up",
                        variant="success",
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    MetricCard(
                        "NPS",
                        "72",
                        delta="+5",
                        delta_type="up",
                        variant="info",
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                g=3,
                cls="mb-4 mt-4",
            ),
            Row(
                Col(
                    FilterBar(
                        DateRangePicker(
                            start_name="start",
                            end_name="end",
                            start_label="From",
                            end_label="To",
                            apply_label="Apply",
                        ),
                        Select(
                            "plan",
                            ("all", "All Plans"),
                            ("enterprise", "Enterprise"),
                            ("business", "Business"),
                            ("starter", "Starter"),
                            label="Plan",
                        ),
                        ExportButton(
                            "Export CSV",
                            endpoint="/export/accounts",
                            export_format="csv",
                            filename="accounts.csv",
                        ),
                    ),
                    cols=12,
                ),
            ),
            H2("Accounts", cls="h4 mb-3"),
            DataTable(
                data=[
                    {
                        "id": a["id"],
                        "name": a["name"],
                        "plan": a["plan"],
                        "mrr": a["mrr"],
                        "health": a["health"],
                        "region": a["region"],
                    }
                    for a in ACCOUNTS
                ],
                columns=["id", "name", "plan", "mrr", "health", "region"],
                sortable=True,
                pagination=True,
                per_page=10,
            ),
            cls="my-5",
        ),
        Div(
            Container(
                P("© 2026 AdminHub. Built with Faststrap.", cls="mb-0"),
            ),
            cls="admin-footer mt-5",
        ),
        cls="admin-shell",
        data_bs_theme=theme,
    )


@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Type to search accounts...", cls="text-muted")
    filtered = [a for a in ACCOUNTS if q.lower() in a["name"].lower() or q.lower() in a["plan"].lower()]
    if not filtered:
        return P(f"No results for '{q}'", cls="text-muted")
    return Table(
        Thead(Tr(Th("ID"), Th("Name"), Th("Plan"), Th("MRR"), Th("Health"), Th("Region"))),
        Tbody(*[account_row(a) for a in filtered]),
        striped=True,
        hover=True,
        cls="mt-3",
    )


@app.get("/export/accounts")
def export_accounts():
    from starlette.responses import Response
    output = "ID,Name,Plan,MRR,Health,Region\n"
    for a in ACCOUNTS:
        output += f"{a['id']},{a['name']},{a['plan']},{a['mrr']},{a['health']},{a['region']}\n"
    return Response(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="accounts.csv"'},
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "dark" if req.session.get(THEME_KEY, "light") == "light" else "dark"
    return hx_refresh()


if __name__ == "__main__":
    serve(port=5022)
