"""Landing page layout component."""

from typing import Any

from fasthtml.common import Div, Main

from ..components.layout.grid import Container
from ..core._stability import beta


@beta
def LandingLayout(
    *content: Any,
    navbar: Any | None = None,
    footer: Any | None = None,
    fluid: bool = False,
    **kwargs: Any,
) -> Div:
    """A clean full-width layout optimized for landing pages and marketing sites.

    Args:
        *content: Main content sections (Hero, Features, etc.)
        navbar: Top navigation component
        footer: Bottom footer component
        fluid: Use fluid container for main content
        **kwargs: Additional attributes
    """
    return Div(
        navbar or "",
        Main(Container(*content, fluid=fluid) if content else "", cls="flex-shrink-0"),
        footer or "",
        cls="d-flex flex-column min-vh-100 landing-layout",
        **kwargs,
    )
