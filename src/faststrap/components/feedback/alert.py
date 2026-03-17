"""Bootstrap Alert component for contextual feedback messages."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Div

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from ...utils.attrs import convert_attrs


@register(category="feedback", requires_js=True)
def Alert(
    *children: Any,
    variant: VariantType | None = None,
    dismissible: bool | None = None,
    heading: Any | None = None,
    heading_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Alert component for contextual feedback messages.

    Args:
        *children: Alert content
        variant: Bootstrap color variant
        dismissible: Add close button to dismiss alert
        heading: Optional heading text or element
        heading_cls: CSS class for heading
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with alert classes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Alert", variant=variant, dismissible=dismissible, heading_cls=heading_cls
    )

    c_variant = cfg.get("variant", "primary")
    c_dismissible = cfg.get("dismissible", False)
    c_heading_cls = cfg.get("heading_cls", "alert-heading h4")

    # Build base classes
    classes = ["alert", f"alert-{c_variant}"]

    # Add dismissible class if needed
    if c_dismissible:
        classes.append("alert-dismissible fade show")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes, "role": "alert"}

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Build content
    content = []

    # Add heading if provided
    if heading:
        if isinstance(heading, (str, bytes)):
            content.append(Div(heading, cls=c_heading_cls))
        else:
            content.append(heading)

    # Add main content
    content.extend(children)

    # Add close button if dismissible
    if c_dismissible:
        close_btn = Button(
            type="button",
            cls="btn-close",
            data_bs_dismiss="alert",
            aria_label="Close",
        )
        content.append(close_btn)

    return Div(*content, **attrs)
