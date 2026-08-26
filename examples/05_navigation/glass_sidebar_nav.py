"""
05_navigation/glass_sidebar_nav.py
Demonstrates: GlassNavbar, GlassNavItem, SidebarNavbar, SidebarNavItem, Scrollspy

- GlassNavbar: Premium translucent glassmorphism navigation with blur
- SidebarNavbar: Vertical application sidebar with active indicators
- Scrollspy: Auto-updating table of contents tracking scroll position
"""

from fasthtml.common import FastHTML, H1, H2, H3, P, Div, A, Nav, serve
from faststrap import (
    add_bootstrap,
    Container,
    GlassNavbar,
    GlassNavItem,
    SidebarNavbar,
    SidebarNavItem,
    Scrollspy,
    Card,
    Row,
    Col,
    Button,
    Badge,
)

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="dark")


@app.get("/")
def home():
    return Div(
        # ── GlassNavbar Header ─────────────────────────────────────────────
        GlassNavbar(
            GlassNavItem("Dashboard", href="#", active=True),
            GlassNavItem("Analytics", href="#"),
            GlassNavItem("Reports", href="#"),
            GlassNavItem("Settings", href="#"),
            brand="GlassApp",
            brand_href="/",
            blur_strength="medium",
            transparency=0.25,
            sticky=True,
        ),

        Container(
            H1("Glass & Sidebar Navigation", cls="display-5 fw-bold mt-5 mb-2"),
            P("Glassmorphism top nav, vertical app sidebar, and Scrollspy page tracking.", cls="lead text-muted mb-5"),

            Row(
                # Sidebar column
                Col(
                    Card(
                        SidebarNavbar(
                            SidebarNavItem("Overview", href="#overview", icon="speedometer2", active=True),
                            SidebarNavItem("Customers", href="#customers", icon="people"),
                            SidebarNavItem("Orders", href="#orders", icon="cart"),
                            SidebarNavItem("Revenue", href="#revenue", icon="currency-dollar"),
                            brand="OpsPortal",
                            theme="dark",
                            width="100%",
                        ),
                        header="SidebarNavbar",
                        cls="h-100",
                    ),
                    span=12, md=4, lg=3, cls="mb-4",
                ),

                # Content with Scrollspy
                Col(
                    Card(
                        Nav(
                            A("Overview", href="#sec-overview", cls="nav-link"),
                            A("Customers", href="#sec-customers", cls="nav-link"),
                            A("Orders", href="#sec-orders", cls="nav-link"),
                            id="scrollspy-nav",
                            cls="nav nav-pills mb-4",
                        ),
                        Scrollspy(
                            Div(
                                Div(
                                    H3("Overview Section", cls="h5 fw-bold"),
                                    P("Primary system health and status metrics. Content updates as you scroll.", cls="text-muted"),
                                    id="sec-overview",
                                    cls="p-4 mb-4 bg-dark border rounded",
                                ),
                                Div(
                                    H3("Customer Operations", cls="h5 fw-bold"),
                                    P("Active user sessions, accounts, and retention tracking metrics.", cls="text-muted"),
                                    id="sec-customers",
                                    cls="p-4 mb-4 bg-dark border rounded",
                                ),
                                Div(
                                    H3("Order Fulfillment", cls="h5 fw-bold"),
                                    P("Recent transactions and pending processing queue statuses.", cls="text-muted"),
                                    id="sec-orders",
                                    cls="p-4 mb-4 bg-dark border rounded",
                                ),
                            ),
                            target="#scrollspy-nav",
                            smooth_scroll=True,
                        ),
                        header="Scrollspy Content Region",
                        cls="p-4",
                    ),
                    span=12, md=8, lg=9, cls="mb-4",
                ),
            ),
            cls="py-4",
        ),
    )


if __name__ == "__main__":
    serve()
