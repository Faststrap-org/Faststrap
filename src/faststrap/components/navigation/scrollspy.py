"""Bootstrap Scrollspy for auto-updating navigation."""

from typing import Any

from fasthtml.common import Div

from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="navigation", requires_js=True)
def Scrollspy(
    *children: Any,
    target: str,
    offset: int | None = None,
    method: str | None = None,
    smooth_scroll: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Scrollspy for auto-updating navigation based on scroll position.

    Automatically updates navigation links based on scroll position. Highlights
    the current section in the navigation as you scroll through the page.

    Args:
        *children: Content sections to watch
        target: CSS selector for the navigation element (e.g., "#navbar")
        offset: Offset from top in pixels when calculating position
        method: Scrollspy method ("auto", "offset", or "position")
        smooth_scroll: Enable smooth scrolling when clicking nav links
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with scrollspy data attributes

    Example:
        Basic scrollspy:
        >>> # Navigation
        >>> Navbar(
        ...     NavItem("Section 1", href="#section1"),
        ...     NavItem("Section 2", href="#section2"),
        ...     id="navbar"
        ... )
        >>>
        >>> # Content with scrollspy
        >>> Scrollspy(
        ...     Div(H2("Section 1"), P("Content..."), id="section1"),
        ...     Div(H2("Section 2"), P("Content..."), id="section2"),
        ...     target="#navbar"
        ... )

        With offset:
        >>> Scrollspy(
        ...     Div(..., id="intro"),
        ...     Div(..., id="features"),
        ...     target="#nav",
        ...     offset=100  # Account for fixed navbar
        ... )

    Note:
        Requires Bootstrap's JavaScript. Navigation items must have href
        attributes matching the IDs of the content sections.

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/scrollspy/
    """
    # Build data attributes
    data_attrs: dict[str, Any] = {
        "data_bs_spy": "scroll",
        "data_bs_target": target,
    }

    if offset is not None:
        data_attrs["data_bs_offset"] = str(offset)

    if method:
        data_attrs["data_bs_method"] = method

    if smooth_scroll:
        data_attrs["data_bs_smooth_scroll"] = "true"

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("", user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "tabindex": "0",  # Required for scrollspy
    }
    attrs.update(data_attrs)
    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
