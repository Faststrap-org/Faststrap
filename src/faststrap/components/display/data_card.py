"""DataCard structured metadata display component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H5, Div, P, Span, Table, Tbody, Td, Tr

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="display")
@experimental
def DataCard(
    title: str,
    *,
    subtitle: str | None = None,
    status: str | None = None,
    metrics: dict[str, str] | None = None,
    fields: dict[str, str] | None = None,
    footer: Any | None = None,
    variant: str = "default",
    **kwargs: Any,
) -> Div:
    """Structured metadata card for models, datasets, experiments, and entities.

    Provides a consistent surface for displaying key-value metadata,
    status badges, and summary metrics.

    Args:
        title: Primary title or entity name.
        subtitle: Optional secondary description.
        status: Optional status string rendered as a badge.
        metrics: Optional dict of metric name -> value pairs.
        fields: Optional dict of field name -> value pairs rendered as
            a metadata table.
        footer: Optional footer content.
        variant: Visual variant. Currently only ``"default"`` is supported.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element styled as a data card.
    """
    user_cls = kwargs.pop("cls", "")

    header_children: list[Any] = [H5(title, cls="mb-1")]
    if subtitle:
        header_children.append(P(subtitle, cls="text-muted mb-0 small"))
    if status:
        header_children.append(Span(status, cls=f"badge bg-{_status_variant(status)} ms-2"))

    body_children: list[Any] = []
    if metrics:
        body_children.append(
            Div(
                *[
                    Div(
                        Span(key, cls="text-muted small"),
                        Span(value, cls="fw-semibold"),
                        cls="d-flex justify-content-between",
                    )
                    for key, value in metrics.items()
                ],
                cls="faststrap-data-card-metrics",
            )
        )
    if fields:
        body_children.append(
            Table(
                Tbody(
                    *[
                        Tr(
                            Td(key, cls="text-muted small"),
                            Td(value),
                        )
                        for key, value in fields.items()
                    ]
                ),
                cls="table table-sm mb-0",
            )
        )

    footer_children: list[Any] = []
    if footer is not None:
        footer_children.append(footer)

    children: list[Any] = [
        Div(*header_children, cls="card-header"),
        Div(*body_children, cls="card-body"),
    ]
    if footer_children:
        children.append(Div(*footer_children, cls="card-footer"))

    attrs: dict[str, Any] = {
        "cls": merge_classes("card faststrap-data-card", user_cls),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


def _status_variant(status: str) -> str:
    mapping = {
        "active": "success",
        "running": "success",
        "completed": "primary",
        "done": "primary",
        "pending": "warning",
        "queued": "secondary",
        "failed": "danger",
        "error": "danger",
        "stopped": "secondary",
    }
    return mapping.get(status.lower(), "secondary")
