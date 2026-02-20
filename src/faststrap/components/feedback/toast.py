"""Bootstrap Toast component for temporary notifications."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Div, Strong

from ...core.base import merge_classes
from ...core.theme import resolve_defaults
from ...core.types import ToastPositionType, VariantType
from ...utils.attrs import convert_attrs


def SimpleToast(
    *children: Any,
    title: str | None = None,
    variant: VariantType | None = None,
    duration: int | None = None,
    position: ToastPositionType | None = None,
    **kwargs: Any,
) -> Div:
    """Simple Toast component that works without JavaScript."""
    # Resolve API defaults
    cfg = resolve_defaults("SimpleToast", variant=variant, duration=duration, position=position)

    c_variant = cfg.get("variant", "info")
    c_duration = cfg.get("duration", 5)
    c_position = cfg.get("position", "top-right")

    # Build base classes
    classes = ["alert", f"alert-{c_variant}", "alert-dismissible", "fade", "show"]

    # Position classes for fixed overlay
    position_classes = {
        "top-right": "position-fixed top-0 end-0 m-3",
        "top-left": "position-fixed top-0 start-0 m-3",
        "bottom-right": "position-fixed bottom-0 end-0 m-3",
        "bottom-left": "position-fixed bottom-0 start-0 m-3",
        "top-center": "position-fixed top-0 start-50 translate-middle-x m-3",
        "bottom-center": "position-fixed bottom-0 start-50 translate-middle-x m-3",
    }

    classes.append(position_classes.get(c_position, position_classes["top-right"]))

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "role": "alert",
        "style": "z-index: 9999; max-width: 400px;",
    }

    # Add CSS for auto-hide
    if c_duration > 0:
        style = f"animation: toastFadeOut {c_duration}s ease-in-out {c_duration}s forwards;"
        existing_style = attrs.get("style", "")
        if existing_style:
            attrs["style"] = f"{existing_style}; {style}"
        else:
            attrs["style"] = style

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Build toast structure
    parts = []

    if title:
        header = Div(
            Strong(title, cls="me-auto"),
            Button(
                "×",
                type="button",
                cls="btn-close",
                aria_label="Close",
                **{k: v for k, v in attrs.items() if k not in ["cls", "role", "style"]},
            ),
            cls="alert-heading",
        )
        parts.append(header)

    body = Div(*children, cls="mb-0")
    parts.append(body)

    return Div(*parts, **attrs)


def Toast(
    *children: Any,
    title: str | None = None,
    variant: VariantType | None = None,
    autohide: bool | None = None,
    delay: int | None = None,
    animation: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Toast component for temporary notifications."""
    # Resolve API defaults
    cfg = resolve_defaults(
        "Toast", variant=variant, autohide=autohide, delay=delay, animation=animation
    )

    c_variant = cfg.get("variant")
    c_autohide = cfg.get("autohide", True)
    c_delay = cfg.get("delay", 5000)
    c_animation = cfg.get("animation", True)

    # Build base classes
    classes = ["toast"]
    if c_variant:
        classes.append(f"text-bg-{c_variant}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "role": "alert",
        "aria-live": "assertive",
        "aria-atomic": "true",
    }

    # Bootstrap toast data attributes
    if c_autohide:
        attrs["data-bs-autohide"] = "true"
        attrs["data-bs-delay"] = str(c_delay)
    else:
        attrs["data-bs-autohide"] = "false"

    if c_animation:
        attrs["data-bs-animation"] = "true"

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Build toast structure
    parts = []

    if title:
        header = Div(
            Strong(title, cls="me-auto"),
            Button(
                type="button",
                cls="btn-close",
                data_bs_dismiss="toast",
                aria_label="Close",
            ),
            cls="toast-header",
        )
        parts.append(header)

    body = Div(*children, cls="toast-body")
    parts.append(body)

    return Div(*parts, **attrs)


def ToastContainer(
    *toasts: Any,
    position: ToastPositionType | None = None,
    container_id: str = "toast-container",
    **kwargs: Any,
) -> Div:
    """Container for positioning toasts on the page."""
    # Resolve API defaults
    cfg = resolve_defaults("ToastContainer", position=position)
    c_position = cfg.get("position", "top-end")

    # Build position classes
    classes = ["toast-container", "position-fixed", "p-3"]

    position_map = {
        "top-start": "top-0 start-0",
        "top-center": "top-0 start-50 translate-middle-x",
        "top-end": "top-0 end-0",
        "middle-start": "top-50 start-0 translate-middle-y",
        "middle-center": "top-50 start-50 translate-middle",
        "middle-end": "top-50 end-0 translate-middle-y",
        "bottom-start": "bottom-0 start-0",
        "bottom-center": "bottom-0 start-50 translate-middle-x",
        "bottom-end": "bottom-0 end-0",
    }

    classes.append(position_map.get(c_position, position_map["top-end"]))

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    container_id = kwargs.pop("id", container_id)
    attrs: dict[str, Any] = {"cls": all_classes, "id": container_id}
    attrs.update(convert_attrs(kwargs))

    return Div(*toasts, **attrs)
