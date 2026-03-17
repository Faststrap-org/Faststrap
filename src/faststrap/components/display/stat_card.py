"""Bootstrap StatCard component."""

from typing import Any, Literal

from fasthtml.common import H3, Div, P, Span

from ...core._stability import beta
from ...core.registry import register
from ...core.types import VariantType
from .card import Card


@register(category="display")
@beta
def StatCard(
    title: str,
    value: str | int | float,
    icon: Any | None = None,
    trend: str | None = None,
    trend_type: Literal["up", "down", "neutral"] = "neutral",
    variant: VariantType | None = None,
    inverse: bool = False,
    icon_bg: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Statistic Card component.

    Display a metric with optional icon and trend.

    Args:
        title: Label for the statistic
        value: The numeric or text value
        icon: Icon component to display
        trend: Trend text (e.g. "+5%")
        trend_type: "up" (green), "down" (red), or "neutral" (muted)
        variant: Card background variant
        inverse: Invert text colors (white text)
        icon_bg: Background color class for icon (e.g. "bg-primary-subtle")
        **kwargs: Additional HTML attributes

    Returns:
        Card component

    Example:
        >>> StatCard("Revenue", "$50k", trend="+12%", trend_type="up")
    """
    # Trend logic
    trend_cls = "text-muted"
    if trend_type == "up":
        trend_cls = "text-success"
    elif trend_type == "down":
        trend_cls = "text-danger"

    trend_el = Span(trend, cls=f"{trend_cls} small fw-bold ms-2") if trend else None

    # Value wrapper
    value_el = H3(value, trend_el, cls="mb-0 fw-bold")

    # Title
    title_cls = "text-muted small text-uppercase fw-semibold"
    if inverse:
        title_cls = "text-white-50 small text-uppercase fw-semibold"

    title_el = P(title, cls=title_cls)

    # Icon logic
    icon_el = None
    if icon:
        icon_wrapper_cls = "d-flex align-items-center justify-content-center rounded p-3"
        if icon_bg:
            icon_wrapper_cls = f"{icon_wrapper_cls} {icon_bg}"
        else:
            icon_wrapper_cls = f"{icon_wrapper_cls} bg-body-tertiary"

        icon_el = Div(icon, cls=icon_wrapper_cls)

    # Layout: Row with col for text, col-auto for icon
    if icon_el:
        body_content = Div(
            Div(title_el, value_el, cls="flex-grow-1"),
            icon_el,
            cls="d-flex align-items-center justify-content-between",
        )
    else:
        body_content = Div(title_el, value_el)

    return Card(body_content, variant=variant, inverse=inverse, **kwargs)
