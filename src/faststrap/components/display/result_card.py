"""ResultCard component for post-action feedback."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import H5, Div, P

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

ResultStatus = Literal["success", "error", "warning", "info", "neutral"]

RESULT_VARIANTS = {
    "success": "success",
    "error": "danger",
    "warning": "warning",
    "info": "info",
    "neutral": "secondary",
}

RESULT_ICONS = {
    "success": "check-circle",
    "error": "x-circle",
    "warning": "exclamation-triangle",
    "info": "info-circle",
    "neutral": "circle",
}


@register(category="display")
@beta
def ResultCard(
    title: str,
    message: str | None = None,
    *,
    status: ResultStatus = "success",
    icon: str | None = None,
    action: Any | None = None,
    compact: bool = False,
    icon_cls: str | None = None,
    title_cls: str | None = None,
    message_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a focused result surface for completed actions.

    Args:
        title: Result heading.
        message: Optional supporting text.
        status: Semantic outcome driving color and live-region role.
        icon: Bootstrap icon name override.
        action: Optional action element rendered below the text.
        compact: Reduce vertical padding for dense layouts.
        icon_cls: Extra classes merged onto the icon (e.g. ``fs-2`` to
            reduce the icon's visual weight).
        title_cls: Extra classes merged onto the title heading.
        message_cls: Extra classes merged onto the message paragraph.
        **kwargs: Additional HTML attributes.
    """
    variant = RESULT_VARIANTS.get(status, "secondary")
    resolved_icon = icon if icon is not None else RESULT_ICONS.get(status)
    user_cls = kwargs.pop("cls", "")

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-result-card card border-0 shadow-sm",
            f"border-start border-4 border-{variant}",
            user_cls,
        ),
        "role": "status" if status in {"success", "info", "neutral"} else "alert",
    }
    attrs.update(convert_attrs(kwargs))

    body_cls = "card-body"
    if compact:
        body_cls = merge_classes(body_cls, "py-3")

    content = []
    if resolved_icon:
        content.append(
            Div(
                Icon(
                    resolved_icon,
                    cls=merge_classes(f"text-{variant} fs-4", icon_cls),
                    aria_hidden="true",
                ),
                cls="flex-shrink-0",
            )
        )

    text_parts: list[Any] = [H5(title, cls=merge_classes("card-title mb-1", title_cls))]
    if message:
        text_parts.append(P(message, cls=merge_classes("card-text text-muted mb-0", message_cls)))
    if action:
        text_parts.append(Div(action, cls="mt-3"))

    content.append(Div(*text_parts, cls="min-w-0"))

    return Div(Div(Div(*content, cls="d-flex gap-3 align-items-start"), cls=body_cls), **attrs)
