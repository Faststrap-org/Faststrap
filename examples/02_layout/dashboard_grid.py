"""
02_layout/dashboard_grid.py
Demonstrates: DashboardGrid

DashboardGrid is an auto-fill CSS grid for dashboard metric cards.
It automatically wraps columns when the viewport narrows.
Key params:
  cols=N          — fixed number of columns (optional; omit for auto-fit)
  gap=1.5         — gutter (rem)
  min_card_width= — minimum card width before wrapping (px or string)
  dense=True      — fill gaps in the grid (grid-auto-flow: dense)
"""

from fasthtml.common import FastHTML, H1, H2, H3, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    DashboardGrid,
    StatCard,
    KPICard,
    TrendCard,
    MetricCard,
    Card,
    Badge,
)

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="dark")


@app.get("/")
def home():
    return Container(
        H1("DashboardGrid", cls="display-5 fw-bold mb-2"),
        P(
            "Auto-fill responsive grid for metric and KPI cards. "
            "Wraps automatically — no breakpoint classes needed.",
            cls="lead text-muted mb-5",
        ),

        # ── Auto-fit (no cols= specified) ──────────────────────────────────
        H2("Auto-fit (default)", cls="h4 fw-semibold mb-1"),
        P("Fills as many columns as fit. Cards wrap at min_card_width=240px.", cls="text-muted mb-3"),
        DashboardGrid(
            StatCard("Total Revenue", "$48,290", icon="currency-dollar", trend="+12% vs last month", trend_up=True),
            StatCard("Active Users", "3,847", icon="people-fill", trend="+5% vs last week", trend_up=True),
            StatCard("New Orders", "284", icon="bag-check-fill", trend="-3% vs yesterday", trend_up=False),
            StatCard("Churn Rate", "2.1%", icon="arrow-down-circle", trend="-0.4% vs last month", trend_up=True),
            cls="mb-5",
        ),

        # ── Fixed 3 columns ────────────────────────────────────────────────
        H2("Fixed cols=3", cls="h4 fw-semibold mb-1"),
        P("Force exactly 3 columns regardless of card content width.", cls="text-muted mb-3"),
        DashboardGrid(
            KPICard("SaaS Growth", [("MRR", "$12,400"), ("ARR", "$148,800"), ("ARPU", "$89"), ("LTV", "$2,400")], columns=2),
            KPICard("Customer Health", [("NPS Score", "72"), ("Retention", "94%"), ("Active Users", "3,847"), ("Churn", "2.1%")], columns=2),
            KPICard("Support Metrics", [("Open Tickets", "18"), ("Avg Resolution", "2.4h"), ("CSAT", "98%"), ("First Response", "12m")], columns=2),
            cols=3,
            gap=2,
            cls="mb-5",
        ),

        # ── Wide cards with dense packing ──────────────────────────────────
        H2("Dense packing with mixed widths", cls="h4 fw-semibold mb-1"),
        P("dense=True fills empty grid gaps when cards have different heights.", cls="text-muted mb-3"),
        DashboardGrid(
            TrendCard("Sessions", "14,320", sparkline=[120, 180, 150, 200, 175, 220, 195], delta="+8%", delta_type="up"),
            TrendCard("Bounce Rate", "38%", sparkline=[45, 42, 40, 38, 36, 37, 38], delta="-2%", delta_type="down"),
            TrendCard("Avg Duration", "3m 42s", sparkline=[200, 215, 225, 230, 218, 240, 222], delta="+15s", delta_type="up"),
            MetricCard("Conversion Rate", "4.7%", delta="+0.5%", delta_type="up"),
            MetricCard("Avg Order Value", "$169", delta="-$4", delta_type="down"),
            min_card_width=200,
            gap=2,
            dense=True,
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
