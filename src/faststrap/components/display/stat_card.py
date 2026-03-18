"""Bootstrap StatCard component."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal, cast

from fasthtml.common import H3, Div, P, Span

from ...core._stability import beta, stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from .card import Card


@register(category="display")
@stable
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


def _trend_badge(
    delta: str | int | float | None,
    *,
    delta_type: Literal["up", "down", "neutral"],
) -> Span | None:
    if delta is None:
        return None

    delta_cls = "text-muted"
    if delta_type == "up":
        delta_cls = "text-success"
    elif delta_type == "down":
        delta_cls = "text-danger"

    arrow = {"up": "^", "down": "v", "neutral": ""}.get(delta_type, "")
    label = f"{arrow} {delta}" if arrow else str(delta)
    return Span(label, cls=f"{delta_cls} small fw-semibold")


@register(category="display")
@beta
def MetricCard(
    title: str,
    value: str | int | float,
    delta: str | int | float | None = None,
    delta_type: Literal["up", "down", "neutral"] = "neutral",
    icon: Any | None = None,
    variant: VariantType | None = None,
    inverse: bool = False,
    icon_bg: str | None = None,
    **kwargs: Any,
) -> Div:
    """Metric card with value and delta indicator."""
    user_cls = kwargs.pop("cls", "")
    kwargs["cls"] = merge_classes("faststrap-metric-card", user_cls)

    cfg = resolve_defaults(
        "MetricCard",
        delta_type=delta_type,
        variant=variant,
        inverse=inverse,
        icon_bg=icon_bg,
    )
    c_delta_type = cfg.get("delta_type", delta_type)
    c_variant = cfg.get("variant", variant)
    c_inverse = cfg.get("inverse", inverse)
    c_icon_bg = cfg.get("icon_bg", icon_bg)

    delta_el = _trend_badge(delta, delta_type=c_delta_type)
    value_el = H3(value, cls="mb-0 fw-bold")
    title_cls = "text-muted small text-uppercase fw-semibold"
    if c_inverse:
        title_cls = "text-white-50 small text-uppercase fw-semibold"

    title_el = P(title, cls=title_cls)

    icon_el = None
    if icon:
        icon_wrapper_cls = "d-flex align-items-center justify-content-center rounded p-3"
        if c_icon_bg:
            icon_wrapper_cls = f"{icon_wrapper_cls} {c_icon_bg}"
        else:
            icon_wrapper_cls = f"{icon_wrapper_cls} bg-body-tertiary"
        icon_el = Div(icon, cls=icon_wrapper_cls)

    if icon_el:
        body_content = Div(
            Div(title_el, value_el, delta_el, cls="flex-grow-1"),
            icon_el,
            cls="d-flex align-items-center justify-content-between gap-3",
        )
    else:
        body_content = Div(title_el, value_el, delta_el)

    return Card(body_content, variant=c_variant, inverse=c_inverse, **kwargs)


@register(category="display")
@beta
def TrendCard(
    title: str,
    value: str | int | float,
    sparkline: Any | None = None,
    sparkline_safe: bool = False,
    delta: str | int | float | None = None,
    delta_type: Literal["up", "down", "neutral"] = "neutral",
    variant: VariantType | None = None,
    inverse: bool = False,
    **kwargs: Any,
) -> Div:
    """Metric card with a sparkline slot for trends."""
    user_cls = kwargs.pop("cls", "")
    kwargs["cls"] = merge_classes("faststrap-trend-card", user_cls)

    cfg = resolve_defaults(
        "TrendCard",
        delta_type=delta_type,
        variant=variant,
        inverse=inverse,
    )
    c_delta_type = cfg.get("delta_type", delta_type)
    c_variant = cfg.get("variant", variant)
    c_inverse = cfg.get("inverse", inverse)

    delta_el = _trend_badge(delta, delta_type=c_delta_type)
    value_el = H3(value, cls="mb-0 fw-bold")
    title_cls = "text-muted small text-uppercase fw-semibold"
    if c_inverse:
        title_cls = "text-white-50 small text-uppercase fw-semibold"

    title_el = P(title, cls=title_cls)

    sparkline_el = None
    if sparkline is not None:
        if isinstance(sparkline, str):
            if not sparkline_safe:
                msg = "sparkline_safe=True is required to embed raw HTML/SVG sparklines."
                raise ValueError(msg)
            from fasthtml.common import NotStr

            sparkline_el = Div(NotStr(sparkline), cls="text-end")
        else:
            sparkline_el = Div(sparkline, cls="text-end")

    body_content = Div(
        Div(title_el, value_el, delta_el, cls="flex-grow-1"),
        sparkline_el,
        cls="d-flex align-items-center justify-content-between gap-3",
    )

    return Card(body_content, variant=c_variant, inverse=c_inverse, **kwargs)


@register(category="display")
@beta
def KPICard(
    title: str,
    metrics: Sequence[Sequence[Any]],
    columns: int = 2,
    variant: VariantType | None = None,
    inverse: bool = False,
    **kwargs: Any,
) -> Div:
    """Card that displays multiple KPIs in a compact grid."""
    user_cls = kwargs.pop("cls", "")
    kwargs["cls"] = merge_classes("faststrap-kpi-card", user_cls)

    cfg = resolve_defaults(
        "KPICard",
        columns=columns,
        variant=variant,
        inverse=inverse,
    )
    c_columns = cfg.get("columns", columns)
    c_variant = cfg.get("variant", variant)
    c_inverse = cfg.get("inverse", inverse)

    if c_columns < 1:
        msg = f"columns must be >= 1, got {c_columns}"
        raise ValueError(msg)

    title_cls = "text-muted small text-uppercase fw-semibold"
    if c_inverse:
        title_cls = "text-white-50 small text-uppercase fw-semibold"

    title_el = P(title, cls=title_cls)

    metric_cells: list[Any] = []
    col_class = f"col-{12 // min(c_columns, 12)}"
    for metric in metrics:
        if len(metric) < 2:
            msg = "Each metric must include at least (label, value)."
            raise ValueError(msg)
        label = metric[0]
        value = metric[1]
        delta = metric[2] if len(metric) > 2 else None
        delta_type_raw = metric[3] if len(metric) > 3 else "neutral"
        if delta_type_raw not in {"up", "down", "neutral"}:
            delta_type_raw = "neutral"
        delta_type = cast(Literal["up", "down", "neutral"], delta_type_raw)
        delta_el = _trend_badge(delta, delta_type=delta_type)

        metric_cells.append(
            Div(
                P(label, cls="mb-1 text-muted small"),
                H3(value, cls="mb-0 fw-bold"),
                delta_el,
                cls=col_class,
            )
        )

    body_content = Div(
        title_el,
        Div(*metric_cells, cls="row g-3"),
    )

    return Card(body_content, variant=c_variant, inverse=c_inverse, **kwargs)
