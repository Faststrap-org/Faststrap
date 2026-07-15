"""Modern toast surfaces for polished feedback."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Button as FTButton
from fasthtml.common import Div, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import ToastPositionType, VariantType
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

ToastStyle = Literal["solid", "soft", "glass"]

TOAST_ICONS: dict[VariantType, str] = {
    "primary": "info-circle",
    "secondary": "circle",
    "success": "check-circle",
    "danger": "x-circle",
    "warning": "exclamation-triangle",
    "info": "info-circle",
    "light": "bell",
    "dark": "bell",
    "link": "bell",
}


@register(category="feedback")
@beta
def ModernToast(
    title: str,
    message: str | None = None,
    *,
    variant: VariantType = "info",
    position: ToastPositionType = "top-end",
    duration: int = 4000,
    style: ToastStyle = "glass",
    icon: str | None = None,
    action: Any | None = None,
    dismissible: bool = True,
    **kwargs: Any,
) -> Div:
    """Render an opinionated modern toast surface."""
    user_cls = kwargs.pop("cls", "")
    resolved_icon = icon if icon is not None else TOAST_ICONS.get(variant)
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-modern-toast d-flex gap-3 rounded-4 border shadow-lg p-3",
            f"faststrap-modern-toast-{style}",
            f"border-{variant}",
            user_cls,
        ),
        "role": "status" if variant not in {"danger", "warning"} else "alert",
        "data_fs_modern_toast": "true",
        "data_variant": variant,
        "data_position": position,
        "data_duration": str(duration),
    }
    attrs.update(convert_attrs(kwargs))

    parts: list[Any] = []
    if resolved_icon:
        parts.append(
            Span(
                Icon(resolved_icon, cls=f"text-{variant}", aria_hidden="true"),
                cls="fs-5 lh-1 mt-1",
            )
        )

    body_parts: list[Any] = [Span(title, cls="fw-semibold d-block")]
    if message:
        body_parts.append(P(message, cls="small text-muted mb-0"))
    if action:
        body_parts.append(Div(action, cls="mt-2"))
    parts.append(Div(*body_parts, cls="flex-grow-1 min-w-0"))

    if dismissible:
        parts.append(
            FTButton(
                "",
                type="button",
                cls="btn-close",
                aria_label="Dismiss notification",
                onclick="this.closest('[data-fs-modern-toast]').remove()",
            )
        )

    return Div(*parts, **attrs)


@register(category="feedback")
@beta
def ModernToastStack(
    *toasts: Any,
    position: ToastPositionType = "top-end",
    gap: int = 2,
    **kwargs: Any,
) -> Div:
    """Render a positioned stack of ModernToast components."""
    user_cls = kwargs.pop("cls", "")
    position_classes = {
        "top-start": "top-0 start-0",
        "top-center": "top-0 start-50 translate-middle-x",
        "top-end": "top-0 end-0",
        "top-left": "top-0 start-0",
        "top-right": "top-0 end-0",
        "bottom-start": "bottom-0 start-0",
        "bottom-center": "bottom-0 start-50 translate-middle-x",
        "bottom-end": "bottom-0 end-0",
        "bottom-left": "bottom-0 start-0",
        "bottom-right": "bottom-0 end-0",
        "middle-start": "top-50 start-0 translate-middle-y",
        "middle-center": "top-50 start-50 translate-middle",
        "middle-end": "top-50 end-0 translate-middle-y",
    }
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-modern-toast-stack position-fixed p-3 d-grid",
            f"gap-{gap}",
            position_classes.get(position, position_classes["top-end"]),
            user_cls,
        ),
        "data_fs_modern_toast_stack": "true",
        "data_position": position,
        "style": "z-index: var(--fs-toast-z-index, 1080);",
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*toasts, **attrs)
