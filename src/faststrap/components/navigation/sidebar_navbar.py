"""Premium Sidebar Navbar component with vertical layout."""

from typing import Any

from fasthtml.common import A, Div, Nav, Span

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@register(category="navigation")
def SidebarNavbar(
    *items: Any,
    brand: str | None = None,
    brand_href: str = "/",
    position: str | None = None,
    width: str | None = None,
    collapsible: bool | None = None,
    theme: str | None = None,
    sticky: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Premium vertical sidebar navbar with icon support.

    A modern sidebar navigation component perfect for dashboards and admin panels.
    Fully theme-aware and responsive with mobile collapse support.

    Args:
        *items: Navigation items (tuples of (label, href, icon) or SidebarNavItem components)
        brand: Brand name/logo text
        brand_href: Brand link URL
        position: Sidebar position ("left" or "right")
        width: Sidebar width (CSS value, default: "250px")
        collapsible: Enable mobile collapse
        theme: Theme variant ("light" or "dark")
        sticky: Make sidebar sticky
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with sidebar structure

    Example:
        Basic sidebar:
        >>> SidebarNavbar(
        ...     ("Dashboard", "/dashboard", "house"),
        ...     ("Users", "/users", "people"),
        ...     ("Settings", "/settings", "gear"),
        ...     brand="My App",
        ...     theme="dark"
        ... )

        With custom width:
        >>> SidebarNavbar(
        ...     ("Home", "/", "house"),
        ...     ("About", "/about", "info-circle"),
        ...     width="300px",
        ...     position="right"
        ... )

    Note:
        Items can be tuples (label, href, icon) or SidebarNavItem components.
        Icons use Bootstrap Icons names (without "bi-" prefix).

    See Also:
        - Icon component for icon names
        - DashboardLayout for full dashboard setup
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "SidebarNavbar",
        position=position,
        width=width,
        collapsible=collapsible,
        theme=theme,
        sticky=sticky,
    )

    c_position = cfg.get("position", "left")
    c_width = cfg.get("width", "250px")
    c_collapsible = cfg.get("collapsible", True)
    c_theme = cfg.get("theme", "dark")
    c_sticky = cfg.get("sticky", True)

    # Build classes
    classes = ["sidebar-navbar", "d-flex", "flex-column"]

    if c_theme == "dark":
        classes.extend(["bg-dark", "text-white"])
    else:
        classes.extend(["bg-light", "border-end"])

    if c_sticky:
        classes.append("sticky-top")

    if c_position == "right":
        classes.append("sidebar-right")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build sidebar parts
    sidebar_parts = []

    # Brand
    if brand:
        brand_classes = "sidebar-brand d-flex align-items-center p-3 mb-3 text-decoration-none"
        if c_theme == "dark":
            brand_classes += " text-white border-bottom border-secondary"
        else:
            brand_classes += " text-dark border-bottom"

        sidebar_parts.append(A(Span(brand, cls="fs-4 fw-bold"), href=brand_href, cls=brand_classes))

    # Navigation items
    nav_items = []
    for item in items:
        if isinstance(item, tuple):
            # Tuple format: (label, href, icon)
            if len(item) == 3:
                label, href, icon_name = item
                nav_items.append(SidebarNavItem(label, href=href, icon=icon_name, theme=c_theme))
            elif len(item) == 2:
                label, href = item
                nav_items.append(SidebarNavItem(label, href=href, theme=c_theme))
        else:
            # Already a component
            nav_items.append(item)

    sidebar_parts.append(Nav(*nav_items, cls="nav nav-pills flex-column mb-auto px-2"))

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes, "style": {"width": c_width, "min-height": "100vh"}}

    # Collapsible ID for mobile
    if c_collapsible:
        attrs["id"] = "sidebarNav"

    attrs.update(convert_attrs(kwargs))

    return Div(*sidebar_parts, **attrs)


def SidebarNavItem(
    label: str,
    href: str = "#",
    icon: str | None = None,
    active: bool = False,
    theme: str = "dark",
    **kwargs: Any,
) -> A:
    """Individual sidebar navigation item.

    Args:
        label: Item label text
        href: Link URL
        icon: Bootstrap icon name (without "bi-" prefix)
        active: Mark as active/selected
        theme: Theme variant ("light" or "dark")
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML A element with nav-link styling

    Example:
        >>> SidebarNavItem("Dashboard", href="/dashboard", icon="house", active=True)
    """
    # Build classes
    classes = ["nav-link", "d-flex", "align-items-center", "gap-2", "py-2", "px-3"]

    if active:
        classes.append("active")
    else:
        if theme == "dark":
            classes.append("text-white")
        else:
            classes.append("text-dark")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build content
    content = []
    if icon:
        content.append(Icon(icon, cls="fs-5"))
    content.append(Span(label))

    # Build attributes
    attrs: dict[str, Any] = {"href": href, "cls": all_classes}

    attrs.update(convert_attrs(kwargs))

    return A(*content, **attrs)
