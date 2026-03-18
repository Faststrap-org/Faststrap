"""Bootstrap EmptyState component."""

from typing import Any

from fasthtml.common import H4, Div, P

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="display")
@stable
def EmptyState(
    icon: Any | None = None,
    title: str = "No data available",
    description: str | None = None,
    action: Any | None = None,
    centered: bool = True,
    icon_cls: str = "display-4 text-muted mb-3",
    title_cls: str = "mb-2",
    description_cls: str = "text-muted mb-4",
    **kwargs: Any,
) -> Div:
    """Bootstrap Empty State component.

    Placeholder for empty data states.

    Args:
        icon: Icon component or img to display
        title: Main heading
        description: Subtitle/explanation
        action: Button or link to perform an action
        centered: Center align content (default: True)
        icon_cls: Classes for the icon wrapper
        title_cls: Classes for title
        description_cls: Classes for description
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element

    Example:
        >>> EmptyState(
        ...     Icon("inbox", cls="display-1"),
        ...     title="No messages",
        ...     description="Your inbox is empty.",
        ...     action=Button("Refresh")
        ... )
    """
    user_cls = kwargs.pop("cls", "")

    classes = ["py-5"]
    if centered:
        classes.append("text-center")

    wrapper_cls = merge_classes(" ".join(classes), user_cls)

    attrs: dict[str, Any] = {"cls": wrapper_cls}
    attrs.update(convert_attrs(kwargs))

    content = []

    if icon:
        content.append(Div(icon, cls=icon_cls))

    content.append(H4(title, cls=title_cls))

    if description:
        content.append(P(description, cls=description_cls))

    if action:
        content.append(Div(action))

    return Div(*content, **attrs)
