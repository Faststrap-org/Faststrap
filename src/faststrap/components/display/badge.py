"""Bootstrap Badge component for status indicators and labels."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Span

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from ...utils.attrs import convert_attrs


@register(category="display")
@stable
def Badge(
    *children: Any,
    variant: VariantType | None = None,
    pill: bool | None = None,
    **kwargs: Any,
) -> Span:
    """Bootstrap Badge component for status indicators and labels.

    Args:
        *children: Badge content (text, numbers, icons)
        variant: Bootstrap color variant
        pill: Use rounded pill style
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Span element with badge classes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Badge",
        variant=variant,
        pill=pill,
    )

    c_variant = cfg.get("variant", "primary")
    c_pill = cfg.get("pill", False)

    # Build base classes
    classes = ["badge"]

    # Add variant background
    classes.append(f"text-bg-{c_variant}")

    # Add pill style if requested
    if c_pill:
        classes.append("rounded-pill")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    return Span(*children, **attrs)
