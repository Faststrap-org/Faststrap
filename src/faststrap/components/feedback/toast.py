"""Bootstrap Toast component for temporary notifications."""

from __future__ import annotations

import warnings
from typing import Any

from fasthtml.common import Button, Div, Strong

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.types import ToastPositionType, VariantType
from ...core.visual import radius_class
from ...utils.attrs import convert_attrs


@register(category="feedback")
def SimpleToast(
    *children: Any,
    title: str | None = None,
    variant: VariantType | None = UNSET,
    duration: int | None = UNSET,
    position: ToastPositionType | None = UNSET,
    radius: str | None = None,
    body_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Simple Toast component that works without JavaScript.

    Args:
        *children: Toast body content.
        title: Optional heading rendered above the body.
        variant: Bootstrap alert variant color.
        duration: Auto-fade delay in milliseconds.
        position: Fixed screen position.
        radius: Radius token (``sm``, ``md``, ``lg``, ``none``); ``None``
            keeps the default alert rounding.
        body_cls: Extra classes for the toast body.
        **kwargs: Additional HTML attributes.
    """
    # Resolve API defaults
    cfg = resolve_defaults("SimpleToast", variant=variant, duration=duration, position=position)

    c_variant = cfg.get("variant", "info")
    c_duration = cfg.get("duration", 5000)
    c_position = cfg.get("position", "top-right")

    # Build base classes (no alert-dismissible — close button removed for no-JS variant)
    classes = ["alert", "fade", "show"]
    if c_variant:
        classes.append(f"alert-{c_variant}")
    radius_cls = radius_class(radius)
    if radius_cls:
        classes.append(radius_cls)

    # Position classes for fixed overlay
    position_classes = {
        "top-right": "position-fixed top-0 end-0 m-3",
        "top-left": "position-fixed top-0 start-0 m-3",
        "bottom-right": "position-fixed bottom-0 end-0 m-3",
        "bottom-left": "position-fixed bottom-0 start-0 m-3",
        "top-center": "position-fixed top-0 start-50 translate-middle-x m-3",
        "bottom-center": "position-fixed bottom-0 start-50 translate-middle-x m-3",
        "top-start": "position-fixed top-0 start-0 m-3",
        "top-end": "position-fixed top-0 end-0 m-3",
        "bottom-start": "position-fixed bottom-0 start-0 m-3",
        "bottom-end": "position-fixed bottom-0 end-0 m-3",
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
    if c_duration and c_duration > 0:
        duration_ms = int(c_duration)
        # Backward compatibility: historical API used seconds.
        if duration_ms <= 50:
            warnings.warn(
                "SimpleToast(duration=...) now expects milliseconds; "
                "values <= 50 are treated as seconds for compatibility.",
                DeprecationWarning,
                stacklevel=2,
            )
            duration_ms *= 1000
        duration_seconds = duration_ms / 1000
        style = f"animation: toastFadeOut 0.5s ease-in-out " f"{duration_seconds}s forwards;"
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
            cls="alert-heading",
        )
        parts.append(header)

    body = Div(*children, cls=merge_classes("mb-0", body_cls) if body_cls else "mb-0")
    parts.append(body)

    return Div(*parts, **attrs)


@register(category="feedback", requires_js=True)
def Toast(
    *children: Any,
    title: str | None = None,
    variant: VariantType | None = UNSET,
    autohide: bool | None = UNSET,
    delay: int | None = UNSET,
    animation: bool | None = UNSET,
    radius: str | None = None,
    header_cls: str = "",
    body_cls: str = "",
    close_button_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap Toast component for temporary notifications.

    Args:
        *children: Toast body content.
        title: Optional header text; renders the ``toast-header`` row with a
            dismiss button.
        variant: Bootstrap color variant applied as ``text-bg-{variant}``.
        autohide: Whether Bootstrap auto-hides the toast.
        delay: Auto-hide delay in milliseconds.
        animation: Whether Bootstrap animates show/hide.
        radius: Radius token (``sm``, ``md``, ``lg``, ``none``); ``None``
            keeps the default Bootstrap toast rounding.
        header_cls: Extra classes for the header row.
        body_cls: Extra classes for the body row.
        close_button_cls: Extra classes for the close button.
        **kwargs: Additional HTML attributes.
    """
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
    radius_cls = radius_class(radius)
    if radius_cls:
        classes.append(radius_cls)

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
        # Bootstrap's default close glyph is black; use the white variant on
        # dark `text-bg-*` fills so it stays visible.
        dark_variants = {"primary", "secondary", "success", "danger", "dark"}
        close_cls = "btn-close"
        if c_variant in dark_variants:
            close_cls = merge_classes(close_cls, "btn-close-white")
        header = Div(
            Strong(title, cls="me-auto"),
            Button(
                type="button",
                cls=merge_classes(close_cls, close_button_cls),
                data_bs_dismiss="toast",
                aria_label="Close",
            ),
            cls=merge_classes("toast-header", header_cls),
        )
        parts.append(header)

    body = Div(*children, cls=merge_classes("toast-body", body_cls))
    parts.append(body)

    return Div(*parts, **attrs)


@register(category="feedback")
def ToastContainer(
    *toasts: Any,
    position: ToastPositionType | None = UNSET,
    container_id: str | None = "toast-container",
    **kwargs: Any,
) -> Div:
    """Container for positioning toasts on the page.

    Args:
        *toasts: Toast components to place inside the container.
        position: Fixed screen position of the container.
        container_id: DOM id for HTMX targeting; pass ``None`` to auto-generate
            a unique id when multiple containers are needed.
        **kwargs: Additional HTML attributes.
    """
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
    all_classes = merge_classes(classes, user_cls)

    # Build attributes
    explicit_id = kwargs.pop("id", None)
    if explicit_id is not None and container_id is not None and explicit_id != container_id:
        raise ValueError(
            "ToastContainer received both container_id and id with different values; "
            "use container_id only."
        )
    resolved_id = explicit_id or container_id
    if resolved_id is None:
        # Auto-generate a unique id so multiple containers can coexist.
        import uuid

        resolved_id = f"toast-container-{uuid.uuid4().hex[:8]}"
    attrs: dict[str, Any] = {"cls": all_classes, "id": resolved_id}
    attrs.update(convert_attrs(kwargs))

    return Div(*toasts, **attrs)
