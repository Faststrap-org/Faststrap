"""OTP (One-Time Password) input components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Input

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="forms")
@stable
def OTPInput(
    length: int = 6,
    *,
    name: str = "otp",
    variant: Literal["primary", "secondary", "success", "danger", "warning", "info"] = "primary",
    size: Literal["sm", "md", "lg"] = "md",
    placeholder: str = "•",
    **kwargs: Any,
) -> Div:
    """Render a CSS-only OTP/pin input with a single field.

    Truly zero-JS: uses a single <input> with maxlength, inputmode, and CSS
    letter-spacing for the visual split appearance.

    Args:
        length: Number of digits expected (default 6)
        name: Form field name for the concatenated value
        variant: Bootstrap color variant for focus styling
        size: Input size (sm, md, lg)
        placeholder: Character to show in each position (default "•")
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div wrapping a styled single-field OTP input
    """
    user_cls = kwargs.pop("cls", "")

    # Size classes
    size_map = {
        "sm": "form-control-sm",
        "md": "",
        "lg": "form-control-lg",
    }
    size_class = size_map.get(size, "")

    classes = ["form-control", "text-center", "letter-spaced-otp"]
    if size_class:
        classes.append(size_class)

    style = (
        f"letter-spacing: 0.5em; "
        f"font-family: monospace; "
        f"max-width: {length * 2.2}em; "
        f"text-align: center;"
    )

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
        "type": "text",
        "inputmode": "numeric",
        "pattern": f"\\d{{{length}}}",
        "maxlength": str(length),
        "autocomplete": "one-time-code",
        "placeholder": placeholder * length,
        "name": name,
        "style": style,
        "aria_label": f"Enter {length}-digit verification code",
    }
    attrs.update(convert_attrs(kwargs))

    return Div(Input(**attrs))


@register(category="forms", requires_js=True)
@stable
def OTPInputGroup(
    length: int = 6,
    *,
    name: str = "otp",
    variant: Literal["primary", "secondary", "success", "danger", "warning", "info"] = "primary",
    size: Literal["sm", "md", "lg"] = "md",
    gap: int = 2,
    autofocus: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a multi-field OTP input with auto-advance.

    Each digit gets its own input box. Uses a single line of JavaScript
    (via Faststrap INIT_SCRIPT) for auto-advancing focus between fields.

    Args:
        length: Number of digit boxes (default 6)
        name: Form field name for the concatenated value
        variant: Bootstrap color variant for focus styling
        size: Input size (sm, md, lg)
        gap: Gap between boxes in Bootstrap spacing units (0-5)
        autofocus: Auto-focus the first input on render
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div containing individual digit input boxes
    """
    user_cls = kwargs.pop("cls", "")

    # Size classes
    size_map = {
        "sm": "form-control-sm",
        "md": "",
        "lg": "form-control-lg",
    }
    size_class = size_map.get(size, "")

    # Gap classes
    gap_class = f"gap-{gap}" if gap > 0 else ""

    container_classes = ["d-flex", "align-items-center", "justify-content-center", gap_class]
    container_cls = merge_classes(" ".join(container_classes), user_cls)

    input_classes = [
        "form-control",
        "text-center",
        "otp-digit-input",
        f"border-{variant}",
    ]
    if size_class:
        input_classes.append(size_class)

    style = (
        "width: 2.5em; "
        "font-family: monospace; "
        "font-size: 1.25em; "
        "text-align: center; "
        "padding: 0.25em;"
    )

    inputs = []
    for i in range(length):
        input_attrs: dict[str, Any] = {
            "cls": merge_classes(" ".join(input_classes), ""),
            "type": "text",
            "inputmode": "numeric",
            "pattern": "\\d",
            "maxlength": "1",
            "autocomplete": "one-time-code",
            "name": f"{name}_{i}",
            "data_otp_index": str(i),
            "data_otp_length": str(length),
            "data_otp_name": name,
            "style": style,
            "aria_label": f"Digit {i + 1} of {length}",
        }
        if autofocus and i == 0:
            input_attrs["autofocus"] = "true"

        inputs.append(Input(**input_attrs))

    container_attrs: dict[str, Any] = {
        "cls": container_cls,
        "data_fs_otp_group": "true",
    }
    container_attrs.update(convert_attrs(kwargs))

    return Div(*inputs, **container_attrs)
