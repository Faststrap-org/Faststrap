"""Modern toast surfaces for polished feedback."""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from typing import Any, Literal, TypedDict

from fasthtml.common import Button as FTButton
from fasthtml.common import Div, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.visual import RadiusToken, ShadowToken, radius_class, shadow_class
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

ToastStyle = Literal["solid", "soft", "glass", "minimal"]
ToastIntent = Literal["success", "error", "warning", "info", "loading"]
ToastVisualStyle = Literal["solid", "soft", "glass", "flat"]
ToastAnimation = Literal["slide", "fade", "zoom", "none"]
ToastCloseReason = Literal["auto", "manual", "escape", "swipe"]


class ToastAction(TypedDict, total=False):
    label: str
    onClick: Any
    style: Literal["primary", "secondary", "destructive", "outline"]
    loading: bool


@dataclass
class ToastPlacement:
    position: Literal[
        "top-left",
        "top-center",
        "top-right",
        "bottom-left",
        "bottom-center",
        "bottom-right",
        "top-start",
        "top-end",
        "bottom-start",
        "bottom-end",
        "middle-start",
        "middle-center",
        "middle-end",
    ] = "bottom-right"
    offset: int = 16
    gutter: int = 8


TOAST_ICONS: dict[str, str] = {
    "primary": "info-circle",
    "secondary": "circle",
    "success": "check-circle",
    "danger": "x-circle",
    "warning": "exclamation-triangle",
    "info": "info-circle",
    "light": "bell",
    "dark": "bell",
    "link": "bell",
    "error": "x-circle",
    "loading": "arrow-clockwise",
}

_VARIANT_TO_INTENT = {
    "primary": "info",
    "secondary": "info",
    "success": "success",
    "danger": "error",
    "warning": "warning",
    "info": "info",
    "light": "info",
    "dark": "info",
    "link": "info",
}

_POSITION_ALIASES = {
    "top-right": "top-end",
    "top-left": "top-start",
    "bottom-right": "bottom-end",
    "bottom-left": "bottom-start",
}


@register(category="feedback")
@beta
def ModernToast(
    title: str,
    message: str | None = None,
    *,
    intent: ToastIntent | str | None = UNSET,
    visual_style: ToastStyle = "glass",
    placement: ToastPlacement | None = None,
    duration: int | Literal["infinite"] | None = UNSET,
    icon: str | None = None,
    action: ToastAction | Any | None = None,
    cancel: ToastAction | Any | None = None,
    dismissible: bool = True,
    pause_on_hover: bool = True,
    animation: ToastAnimation = "slide",
    variant: str | None = UNSET,
    position: str | None = UNSET,
    style: str | None = UNSET,
    on_dismiss: Any | None = None,
    radius: RadiusToken | str | None = None,
    shadow: ShadowToken | str | None = None,
    title_cls: str = "",
    message_cls: str = "",
    close_button_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Render an opinionated modern toast surface.

    Args:
        title: Primary toast heading.
        message: Optional supporting body text.
        intent: Semantic intent driving color and live-region role.
        visual_style: Surface treatment (``solid``, ``soft``, ``glass``,
            ``minimal``).
        placement: Positioned placement (position/offset/gutter).
        duration: Auto-dismiss delay in ms, or ``"infinite"`` to disable.
        icon: Bootstrap icon name override.
        action: Optional action button spec or custom element.
        cancel: Optional cancel button spec or custom element.
        dismissible: Render a close button.
        pause_on_hover: Pause the auto-dismiss timer while hovered/focused.
        animation: Enter/exit animation style.
        radius: Radius token overriding the default ``rounded-4``
            (e.g. ``md`` for a calmer surface in dense dashboards).
        shadow: Shadow token overriding the default ``shadow-lg``.
        title_cls: Extra classes for the title line.
        message_cls: Extra classes for the message paragraph.
        close_button_cls: Extra classes for the dismiss button.
        **kwargs: Additional HTML attributes (``cls``, ``css_vars``, hx-*, ...).
    """
    resolved_intent = intent
    if variant is not UNSET and variant is not None:
        warnings.warn(
            "ModernToast(variant=...) is deprecated; use intent=... instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        resolved_intent = _VARIANT_TO_INTENT.get(variant, intent)

    resolved_position = "bottom-right"
    if placement is not None:
        resolved_position = placement.position
    elif position is not UNSET and position is not None:
        warnings.warn(
            "ModernToast(position=...) is deprecated; use placement=ToastPlacement(position=...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        resolved_position = _POSITION_ALIASES.get(position, position)

    resolved_style: str = visual_style
    if style is not UNSET and style is not None:
        warnings.warn(
            "ModernToast(style=...) is deprecated; use visual_style=... instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        resolved_style = style

    # Global defaults support (set_component_defaults("ModernToast", ...))
    cfg = resolve_defaults("ModernToast", intent=resolved_intent, duration=duration)
    resolved_intent = str(cfg.get("intent") or "info")
    resolved_duration = cfg.get("duration")
    if resolved_duration is None:
        resolved_duration = 4000

    duration_ms = 0 if resolved_duration == "infinite" else int(resolved_duration)

    user_cls = kwargs.pop("cls", "")
    resolved_icon = icon if icon is not None else TOAST_ICONS.get(resolved_intent)
    base_radius_cls = radius_class(radius) or "rounded-4"
    base_shadow_cls = shadow_class(shadow) or "shadow-lg"
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-modern-toast d-flex gap-3 border p-3",
            base_radius_cls,
            base_shadow_cls,
            f"faststrap-modern-toast-{resolved_style}",
            f"border-{resolved_intent}",
            user_cls,
        ),
        "role": "status" if resolved_intent not in {"danger", "warning", "error"} else "alert",
        "data_fs_modern_toast": "true",
        "data_fs_intent": resolved_intent,
        "data_fs_position": resolved_position,
        "data_fs_duration": str(duration_ms),
        "data_fs_animation": animation,
        "data_fs_pause_on_hover": "true" if pause_on_hover else "false",
    }
    if dismissible:
        attrs["data_fs_dismiss"] = "true"
    attrs.update(convert_attrs(kwargs))

    parts: list[Any] = []
    if resolved_icon:
        parts.append(
            Span(
                Icon(resolved_icon, cls=f"text-{resolved_intent}", aria_hidden="true"),
                cls="fs-5 lh-1 mt-1",
            )
        )

    body_parts: list[Any] = [
        Span(title, cls=merge_classes("fw-semibold d-block", title_cls))
    ]
    if message:
        body_parts.append(P(message, cls=merge_classes("small text-muted mb-0", message_cls)))
    if action:
        if isinstance(action, dict):
            action_label = action.get("label", "")
            action_cls = merge_classes(
                "btn", action.get("style", "link"), "disabled" if action.get("loading") else None
            )
            action_btn = FTButton(
                action_label,
                type="button",
                cls=action_cls,
                aria_label=action_label,
            )
            body_parts.append(Div(action_btn, cls="mt-2"))
        else:
            body_parts.append(Div(action, cls="mt-2"))
    if cancel:
        if isinstance(cancel, dict):
            cancel_label = cancel.get("label", "")
            cancel_cls = merge_classes(
                "btn", cancel.get("style", "link"), "disabled" if cancel.get("loading") else None
            )
            cancel_btn = FTButton(
                cancel_label,
                type="button",
                cls=cancel_cls,
                aria_label=cancel_label,
            )
            body_parts.append(Div(cancel_btn, cls="mt-2"))
        else:
            body_parts.append(Div(cancel, cls="mt-2"))
    parts.append(Div(*body_parts, cls="flex-grow-1 min-w-0"))

    if dismissible:
        parts.append(
            FTButton(
                type="button",
                cls=merge_classes("btn-close", close_button_cls),
                aria_label="Dismiss notification",
                data_fs_dismiss="true",
            )
        )

    return Div(*parts, **attrs)


@register(category="feedback")
@beta
def ModernToastStack(
    *toasts: Any,
    placement: ToastPlacement | None = None,
    gap: int = 2,
    max_visible: int = 5,
    position: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a positioned stack of ModernToast components."""
    if position is not UNSET and position is not None:
        warnings.warn(
            "ModernToastStack(position=...) is deprecated; use placement=ToastPlacement(position=...) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        normalized = _POSITION_ALIASES.get(position, position)
        placement = ToastPlacement(position=normalized)  # type: ignore[arg-type]

    resolved_placement = placement or ToastPlacement()
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
    offset_style = (
        f"margin: {resolved_placement.offset}px; gap: {resolved_placement.gutter * 0.25}rem;"
    )
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-modern-toast-stack position-fixed p-3 d-grid",
            f"gap-{gap}",
            position_classes.get(resolved_placement.position, position_classes["bottom-right"]),
            user_cls,
        ),
        "data_fs_modern_toast_stack": "true",
        "data_fs_position": resolved_placement.position,
        "data_fs_max_visible": str(max_visible),
        "data_fs_gutter": str(resolved_placement.gutter),
        "style": f"z-index: var(--fs-toast-z-index, 1080); {offset_style}",
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*toasts, **attrs)
