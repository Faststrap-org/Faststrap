"""Sheet component (Bottom Drawer) for mobile-first interfaces."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core.base import merge_classes
from ...core.registry import register
from ..navigation.drawer import Drawer


@register(category="display", requires_js=True)
def Sheet(
    *children: Any,
    sheet_id: str | None = None,
    title: str | None = None,
    height: str = "auto",  # auto, 50%, 100%
    radius: str = "lg",
    **kwargs: Any,
) -> Div:
    """
    A mobile-native "Bottom Sheet" component.

    This is a wrapper around `Drawer` with specific styling to look like
    a bottom sheet (rounded top corners, bottom placement).

    Args:
        *children: Content
        sheet_id: Unique ID
        title: Title
        height: CSS height value (default: auto)
        radius: Top-corner rounding token (``lg`` default keeps the original
            ``rounded-top-4``; use ``md`` or ``none`` for calmer surfaces).
        **kwargs: Arguments passed to Drawer
    """
    # Force placement to bottom
    kwargs["placement"] = "bottom"

    # Radius handling: keep the historical rounded top corners by default.
    user_cls = kwargs.pop("cls", "")
    radius_map = {
        "lg": "rounded-top-4",
        "md": "rounded-top-3",
        "sm": "rounded-top-2",
        "none": "rounded-top-0",
    }
    sheet_cls = radius_map.get(radius, "rounded-top-4")

    # Add handle visual
    # We inject a small handle at the top of the body or header
    # But since Drawer structure is rigid, we'll just style the container

    # Merge classes
    final_cls = merge_classes(sheet_cls, user_cls)

    # Custom styles
    user_style = kwargs.pop("style", {})
    if isinstance(user_style, dict):
        if height != "auto":
            user_style["height"] = height
            user_style["max-height"] = "90vh"  # Never full full screen to keep context
    elif isinstance(user_style, str):
        style_str = user_style.strip()
        if height != "auto":
            sheet_height = f"height: {height}; max-height: 90vh;"
            user_style = f"{sheet_height} {style_str}" if style_str else sheet_height
        else:
            user_style = style_str

    return Drawer(
        *children, drawer_id=sheet_id, title=title, cls=final_cls, style=user_style, **kwargs
    )
