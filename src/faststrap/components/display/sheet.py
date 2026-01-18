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
        **kwargs: Arguments passed to Drawer
    """
    # Force placement to bottom
    kwargs["placement"] = "bottom"

    # Custom class for sheet styling (rounded corners)
    user_cls = kwargs.pop("cls", "")
    sheet_cls = "rounded-top-4"  # Bootstrap 5 utility for large top rounding

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

    return Drawer(
        *children, drawer_id=sheet_id, title=title, cls=final_cls, style=user_style, **kwargs
    )
