"""
Faststrap v0.9.0 Layout Demo

Demonstrates responsive layout components:
- Switcher: row-to-column responsive layout (pure CSS)
- SplitPane: resizable two-pane layout with drag support
"""

from fasthtml.common import FastHTML, H1, H2, H5, P, Ul, Li, A, serve
from faststrap import add_bootstrap, Container, Card, Row, Col, Switcher, SplitPane

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.9.0 — Layout", cls="display-5 fw-bold mb-2"),
        P(
            "Responsive layout primitives: Switcher and SplitPane.",
            cls="lead text-muted mb-4",
        ),
        H2("Switcher", cls="h4 mb-3"),
        P("Side-by-side on desktop, stacked on mobile. Pure CSS — no JavaScript required.", cls="text-muted mb-3"),
        Row(
            Col(
                Card(
                    H5("Left Panel", cls="card-title"),
                    P("This panel sits beside the right panel on desktop."),
                ),
                span=12,
                md=6,
            ),
            Col(
                Card(
                    H5("Right Panel", cls="card-title"),
                    P("On mobile, both panels stack vertically."),
                ),
                span=12,
                md=6,
            ),
            g=3,
        ),
        H2("Switcher with Ratio", cls="h4 mb-3 mt-4"),
        P("Use ratio for custom column widths (e.g., 1fr 2fr).", cls="text-muted mb-3"),
        Switcher(
            Card(H5("Sidebar (1fr)"), P("Narrower panel.")),
            Card(H5("Content (2fr)"), P("Wider panel with more room.")),
            ratio="1fr 2fr",
            gap=3,
        ),
        H2("SplitPane", cls="h4 mb-3 mt-4"),
        P("Resizable master/detail layout. Drag the divider to resize.", cls="text-muted mb-3"),
        SplitPane(
            Card(
                H5("Navigation"),
                Ul(
                    Li(A("Dashboard", href="#")),
                    Li(A("Projects", href="#")),
                    Li(A("Settings", href="#")),
                ),
                header="Master",
            ),
            Card(
                H5("Content"),
                P("Drag the divider between the panels to resize. On mobile, the panes stack."),
                header="Detail",
            ),
            initial_ratio="30/70",
            collapsible=True,
            stack_on="md",
        ),
        cls="my-5",
    )


if __name__ == "__main__":
    serve()
