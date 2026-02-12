"""Feature Pattern Components."""

from typing import Any

from fasthtml.common import H3, Div, I, P

from ...core._stability import beta
from ..layout.grid import Col, Row


@beta
def Feature(
    title: str,
    description: str,
    icon: str | Any | None = None,
    icon_cls: str = "bg-primary text-white",
    **kwargs: Any,
) -> Div:
    """A single feature item with icon, title, and description.

    Args:
        title: Feature title
        description: Feature description
        icon: Bootstrap icon name or custom element
        icon_cls: CSS classes for icon container
        **kwargs: Additional attributes

    Returns:
        Div with feature content

    Note:
        Marked as @beta - API may change in future releases.
    """
    icon_el = None
    if isinstance(icon, str):
        icon_el = Div(I(cls=f"bi bi-{icon}"), cls=f"feature-icon {icon_cls}")
    elif icon:
        icon_el = Div(icon, cls=f"feature-icon {icon_cls}")

    return Div(
        icon_el,
        H3(title, cls="fs-4 fw-bold"),
        P(description, cls="text-muted"),
        cls="feature-item",
        **kwargs,
    )


@beta
def FeatureGrid(
    *features: Any,
    columns: int = 3,
    **kwargs: Any,
) -> Div:
    """Grid layout for multiple feature items.

    Args:
        *features: Feature components
        columns: Number of columns (default: 3)
        **kwargs: Additional attributes

    Returns:
        Div with responsive feature grid

    Note:
        Marked as @beta - API may change in future releases.
    """
    col_size = 12 // columns
    cols = [Col(feat, md=col_size, cls="mb-4") for feat in features]
    return Div(Row(*cols), cls="feature-grid", **kwargs)
