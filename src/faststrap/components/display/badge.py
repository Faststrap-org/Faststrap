"""Bootstrap Badge component for status indicators and labels."""

from typing import Any, Literal

from fasthtml.common import Span

from ...core.base import merge_classes

VariantType = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
]


def _convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert Python kwargs to HTML attributes (hx_get → hx-get)."""
    converted = {}
    for k, v in kwargs.items():
        if k.startswith("hx_") or k.startswith("data_") or k.startswith("aria_"):
            converted[k.replace("_", "-")] = v
        elif k == "cls":
            converted[k] = v
        else:
            converted[k.replace("_", "-")] = v
    return converted


def Badge(
    *children: Any,
    variant: VariantType = "primary",
    pill: bool = False,
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

    Example:
        Basic usage:
        >>> Badge("New", variant="success")

        Pill style:
        >>> Badge("99+", variant="danger", pill=True)

        With icon:
        >>> Badge(Icon("check"), "Verified", variant="info")

        In button:
        >>> Button("Messages ", Badge("4", variant="danger"))

        With HTMX:
        >>> Badge("Live", variant="warning", hx_get="/status", hx_trigger="every 5s")

    Note:
        Badges scale to match their immediate parent's font size.
        Use text-bg-* classes for colored backgrounds with contrasting text.

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/badge/
    """
    # Build base classes
    classes = ["badge"]

    # Add variant background
    classes.append(f"text-bg-{variant}")

    # Add pill style if requested
    if pill:
        classes.append("rounded-pill")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}

    # Convert remaining kwargs
    attrs.update(_convert_attrs(kwargs))

    return Span(*children, **attrs)
