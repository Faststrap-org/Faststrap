"""Bootstrap Spinner component for loading indicators."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Span

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from ...utils.attrs import convert_attrs


@register(category="feedback")
def Spinner(
    variant: VariantType | None = None,
    size: str | None = None,
    spinner_type: str | None = None,
    label: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Spinner component for loading indicators.

    Args:
        variant: Bootstrap color variant
        size: Spinner size (e.g., "sm")
        spinner_type: Spinner animation type ("border" or "grow")
        label: Screen reader label text
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div element with spinner animation
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Spinner", variant=variant, size=size, spinner_type=spinner_type, label=label
    )

    c_variant = cfg.get("variant", "primary")
    c_size = cfg.get("size")
    c_type = cfg.get("spinner_type", "border")
    c_label = cfg.get("label", "Loading...")

    # Build spinner classes
    classes = [f"spinner-{c_type}"]

    if c_variant:
        classes.append(f"text-{c_variant}")

    if c_size == "sm":
        classes.append(f"spinner-{c_type}-sm")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "role": "status",
    }

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Screen reader text
    sr_text = Span(c_label, cls="visually-hidden")

    return Div(sr_text, **attrs)
