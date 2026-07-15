"""Styled keyboard key indicator component."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Kbd as HtmlKbd

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="display")
@stable
def Kbd(
    *children: Any,
    size: Literal["sm", "md", "lg"] = "md",
    variant: Literal["light", "dark"] = "light",
    **kwargs: Any,
) -> HtmlKbd:
    """Render a styled keyboard key indicator.

    Wraps content in a semantic <kbd> element with Bootstrap-compatible styling.
    Useful for documenting keyboard shortcuts and hotkeys.

    Args:
        *children: Key label content (e.g. "Ctrl", "⌘", "F1")
        size: Font size variant (sm, md, lg)
        variant: Color variant (light for light backgrounds, dark for dark)
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Kbd element with styled keyboard key appearance
    """
    user_cls = kwargs.pop("cls", "")

    classes = ["kbd"]

    # Size variants
    size_map = {
        "sm": "kbd-sm",
        "md": "",
        "lg": "kbd-lg",
    }
    size_class = size_map.get(size, "")
    if size_class:
        classes.append(size_class)

    # Color variant
    if variant == "dark":
        classes.append("bg-dark")
        classes.append("text-light")
    else:
        classes.append("bg-light")
        classes.append("text-dark")
        classes.append("border")
        classes.append("border-secondary-subtle")

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
    }
    attrs.update(convert_attrs(kwargs))

    return HtmlKbd(*children, **attrs)
