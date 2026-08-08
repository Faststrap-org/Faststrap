"""Section-level header component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H2, H3, Div, P, Span

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


def _render_heading(title: str, tag: str) -> Any:
    if tag == "h3":
        return H3(title)
    return H2(title)


@register(category="layout")
@stable
def SectionHeader(
    title: str,
    *,
    subtitle: str | None = None,
    eyebrow: str | None = None,
    badge: Any | None = None,
    actions: Any | list[Any] | tuple[Any, ...] | None = None,
    size: str = "md",
    **kwargs: Any,
) -> Div:
    """Render a section title area with optional subtitle and actions.

    Lighter-weight sibling of `PageHeader` for within-section headings.

    Args:
        title: Section title text.
        subtitle: Optional muted description below the title.
        eyebrow: Optional small uppercase label above the title.
        badge: Optional badge element to show beside the title.
        actions: Optional action buttons or components to show on the right.
        size: Heading size — `sm` renders an `h3`, `md` renders an `h2`.
        **kwargs: Additional HTML attributes (cls, id, etc.).

    Returns:
        FastHTML Div element with section header styling.
    """
    user_cls = kwargs.pop("cls", "")

    size_map = {
        "sm": "h3",
        "md": "h2",
    }
    heading_tag = size_map.get(size, "h2")
    heading_cls = "mb-1" if size == "sm" else "mb-2"

    title_children: list[Any] = []
    if eyebrow:
        title_children.append(Span(eyebrow, cls="text-uppercase text-muted small fw-semibold"))

    heading_children: list[Any] = [title]
    if badge is not None:
        heading_children.append(Span(badge, cls="ms-2 align-middle"))
    title_children.append(_render_heading(Span(*heading_children), heading_tag))
    title_children[-1].cls = heading_cls

    if subtitle:
        title_children.append(P(subtitle, cls="text-muted mb-0"))

    children: list[Any] = [Div(*title_children)]
    if actions is not None:
        if isinstance(actions, (list, tuple)):
            action_children = list(actions)
        else:
            action_children = [actions]
        children.append(Div(*action_children, cls="d-flex flex-wrap gap-2 align-items-center"))

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-2 mb-3",
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
