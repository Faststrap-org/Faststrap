"""Dashboard layout component."""

from typing import Any

from fasthtml.common import A, Button, Div, Footer, Nav, Span

from ..components.layout.grid import Container
from ..core._stability import beta


@beta
def DashboardLayout(
    *content: Any,
    title: str = "Dashboard",
    sidebar_items: list[Any] | None = None,
    user: Any | None = None,
    breadcrumbs: list[tuple[str, str | None]] | None = None,
    footer: str | Any | None = None,
    sidebar_width: str = "250px",
    theme: str = "light",
    **kwargs: Any,
) -> Div:
    """Production-ready admin panel layout with responsive sidebar.

    Args:
        *content: Main content area components
        title: Page title (shown in top navbar or title bar)
        sidebar_items: List of navigation items for the sidebar
        user: User dropdown or profile component
        breadcrumbs: List of (label, url) tuples for navigation
        footer: Footer content
        sidebar_width: Width of the sidebar on desktop
        theme: Layout theme (light or dark)
        **kwargs: Additional attributes
    """
    sidebar_id = "sidebar-wrapper"

    # 1. Sidebar Component
    sidebar = Div(
        Div(
            A(
                Span(title, cls="fs-4 fw-bold"),
                href="/",
                cls="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-decoration-none text-reset",
            ),
            Div(cls="hr mb-3"),
            Nav(*(sidebar_items or []), cls="nav nav-pills flex-column mb-auto"),
            cls="sidebar-sticky p-3",
        ),
        id=sidebar_id,
        cls=f"bg-{theme} border-end sidebar",
        style=f"width: {sidebar_width};",
    )

    # 2. Top Navbar
    top_nav = Nav(
        Div(
            Button(
                Span(cls="navbar-toggler-icon"),
                cls="btn p-0 border-0 me-3 d-lg-none",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{sidebar_id}",
            ),
            Div(
                # Breadcrumbs could go here
                cls="d-flex align-items-center"
            ),
            Div(user or "", cls="ms-auto"),
            cls="container-fluid",
        ),
        cls=f"navbar navbar-expand-lg navbar-{theme} bg-{theme} sticky-top border-bottom py-2",
    )

    # 3. Main Content
    main_content = Div(
        top_nav,
        Container(Div(*content, cls="py-4"), fluid=True),
        (
            Footer(
                Container(Div(footer, cls="text-muted small py-3") if footer else "", fluid=True),
                cls=f"mt-auto border-top bg-{theme}",
            )
            if footer
            else ""
        ),
        cls="main-content-wrapper d-flex flex-column flex-grow-1",
    )

    return Div(sidebar, main_content, cls="d-flex dashboard-layout", style="min-height: 100vh;")
