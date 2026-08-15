"""Responsive Switcher layout component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

_BREAKPOINT_MAP = {
    "sm": "sm",
    "md": "md",
    "lg": "lg",
    "xl": "xl",
    "xxl": "xxl",
}


@register(category="layout")
@experimental
def Switcher(
    *children: Any,
    breakpoint: str = "md",
    ratio: str | None = None,
    gap: int | str = 3,
    min_item_width: str | None = None,
    **kwargs: Any,
) -> Div:
    """Responsive layout that switches from row to column at a breakpoint.

    Pure CSS — no JavaScript required.

    Args:
        *children: Panel contents to render side-by-side on desktop.
        breakpoint: Bootstrap breakpoint to switch from row to column.
            One of ``"sm"``, ``"md"``, ``"lg"``, ``"xl"``, ``"xxl"``.
        ratio: Optional CSS ``grid-template-columns`` value, e.g.
            ``"1fr 2fr"``. When omitted, Bootstrap flex utilities are used.
        gap: Bootstrap gap utility value or custom CSS gap string.
        min_item_width: Optional minimum width before items wrap when
            using ``ratio``.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element with responsive grid/flex layout.
    """
    user_cls = kwargs.pop("cls", "")

    classes = ["faststrap-switcher"]
    style_parts: list[str] = []

    if ratio:
        classes.append("faststrap-switcher-grid")
        style_parts.append(f"grid-template-columns: {ratio}")
        if min_item_width:
            style_parts.append(f"grid-auto-columns: {min_item_width}")
    else:
        bp = _BREAKPOINT_MAP.get(breakpoint, "md")
        classes.append("d-flex")
        classes.append("flex-column")
        classes.append(f"flex-{bp}-row")

    gap_cls = f"gap-{gap}" if isinstance(gap, int) else gap
    classes.append(gap_cls)

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
    }
    if style_parts:
        attrs["style"] = "; ".join(style_parts)
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
