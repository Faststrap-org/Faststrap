from fasthtml.common import (
    Div,
    FastHTML,
    H1,
    H5,
    Main,
    P,
    Title,
    serve,
)

from faststrap import (
    Badge,
    Button,
    Card,
    Col,
    Container,
    Icon,
    Navbar,
    Row,
    StatCard,
    TBody,
    TCell,
    THead,
    TRow,
    Table,
    add_bootstrap,
)


def dashboard_home():
    # Top Stats (4 columns on desktop, 1 on mobile)
    stats = Row(
        Col(
            StatCard(
                "Monthly Revenue",
                "$54,230",
                trend="+12.5%",
                trend_type="up",
                icon=Icon("currency-dollar"),
            ),
            md=3,
            cls="mb-4",
        ),
        Col(
            StatCard("Active Users", "12,840", trend="+3.2%", trend_type="up", icon=Icon("people")),
            md=3,
            cls="mb-4",
        ),
        Col(
            StatCard("Avg. Session", "4m 32s", trend="-15s", trend_type="down", icon=Icon("clock")),
            md=3,
            cls="mb-4",
        ),
        Col(StatCard("Server Load", "24%", trend="Stable", icon=Icon("cpu")), md=3, cls="mb-4"),
        cls="mb-4",
    )

    # Recent Orders Table
    orders_table = Table(
        THead(
            TRow(
                TCell("Order ID", header=True),
                TCell("Customer", header=True),
                TCell("Amount", header=True),
                TCell("Status", header=True),
                TCell("Action", header=True),
            )
        ),
        TBody(
            TRow(
                TCell("#12345"),
                TCell("Alice Smith"),
                TCell("$120.00"),
                TCell(Badge("Paid", variant="success")),
                TCell(Button("View", size="sm", variant="outline-primary")),
            ),
            TRow(
                TCell("#12346"),
                TCell("Bob Johnson"),
                TCell("$450.00"),
                TCell(Badge("Pending", variant="warning")),
                TCell(Button("View", size="sm", variant="outline-primary")),
            ),
            TRow(
                TCell("#12347"),
                TCell("Charlie Brown"),
                TCell("$30.00"),
                TCell(Badge("Cancelled", variant="danger")),
                TCell(Button("View", size="sm", variant="outline-primary")),
            ),
        ),
        striped=True,
        hover=True,
        cls="border border-light-subtle rounded shadow-sm",
    )

    # Main Layout (8:4 split on desktop)
    return Container(
        H1("Dashboard", cls="h2 mb-4"),
        stats,
        Row(
            Col(Card(orders_table, header=H5("Recent Transactions"), cls="mb-4 shadow-sm"), md=8),
            Col(
                Card(
                    Div(
                        P("All systems operational.", cls="text-success fw-bold"),
                        P("Database latency: 12ms", cls="small text-muted"),
                        P("Cache hit rate: 94%", cls="small text-muted"),
                        cls="p-2",
                    ),
                    header=H5("System Health"),
                    footer=Button("Refresh Stats", variant="link", cls="p-0"),
                    cls="shadow-sm",
                ),
                md=4,
            ),
        ),
        py="4",
    )


app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    nav = Navbar(brand="AdminPanel", expand="lg", variant="dark", bg="dark")
    return Title("Admin Dashboard"), Main(nav, dashboard_home())


if __name__ == "__main__":
    serve()
