"""Faststrap DashboardLayout Demo.

Showcasing a responsive admin panel layout with collapsible sidebar.
"""

from fasthtml.common import H2, A, Div, FastHTML, P, serve

from faststrap import Badge, Button, Card, Col, DashboardLayout, Icon, Row, add_bootstrap

app = FastHTML()
add_bootstrap(app, theme="green-nature", font_family="Outfit")


@app.route("/")
def home():
    # Sidebar items
    items = [
        A(Div(Icon("house", cls="me-2"), "Overview"), href="#", cls="nav-link active"),
        A(Div(Icon("bar-chart", cls="me-2"), "Analytics"), href="#", cls="nav-link text-reset"),
        A(Div(Icon("people", cls="me-2"), "Customers"), href="#", cls="nav-link text-reset"),
        A(Div(Icon("gear", cls="me-2"), "Settings"), href="#", cls="nav-link text-reset"),
    ]

    # Quick stats
    stats = Div(
        Row(
            Col(
                Card(
                    Div(
                        P("Total Sales", cls="text-muted small"),
                        H2("$12,450"),
                        Badge("+15%", variant="success"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
            Col(
                Card(
                    Div(
                        P("Active Users", cls="text-muted small"),
                        H2("1,280"),
                        Badge("+5%", variant="success"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
            Col(
                Card(
                    Div(
                        P("Conversion", cls="text-muted small"),
                        H2("3.2%"),
                        Badge("-2%", variant="danger"),
                    ),
                    cls="border-0 shadow-sm",
                )
            ),
        ),
        cls="mb-4",
    )

    main_card = Card(
        "Welcome to the DashboardLayout. This sidebar is responsive: it stays visible on desktop and uses a standard Bootstrap offcanvas/toggle on mobile.",
        header="System Status",
        footer=Button("Refresh Data", cls="btn-sm btn-primary"),
        cls="border-0 shadow-sm",
    )

    user_dropdown = Div("Admin User", cls="badge bg-light text-dark p-2 rounded-pill shadow-sm")

    return DashboardLayout(
        stats,
        main_card,
        title="Admin Panel",
        sidebar_items=items,
        user=user_dropdown,
        footer="© 2026 Faststrap Admin Panel",
    )


if __name__ == "__main__":
    serve(port=5018)
