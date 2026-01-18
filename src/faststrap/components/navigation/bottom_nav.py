"""Bootstrap-styled Bottom Navigation Bar for mobile apps."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Div, Nav, Small

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@register(category="navigation")
def BottomNav(
    *children: Any,
    variant: str | None = None,
    fixed: bool | None = True,  # Default to fixed-bottom which is standard for apps
    labels: bool = True,
    **kwargs: Any,
) -> Nav:
    """Bottom Navigation Bar for mobile applications.

    Args:
        *children: BottomNavItem components
        variant: Color scheme (light, dark, or custom class)
        fixed: Fix to bottom of viewport (default: True)
        labels: Show labels (True) or icons only (False)
        **kwargs: Additional attributes
    """
    cfg = resolve_defaults("BottomNav", variant=variant)
    c_variant = cfg.get("variant", "light")

    classes = ["navbar", "navbar-bottom", "w-100"]

    if fixed:
        classes.append("fixed-bottom")

    if c_variant == "dark":
        classes.append("bg-dark")
        classes.append("navbar-dark")
    elif c_variant == "light":
        classes.append("bg-white")  # Stronger than bg-light for bottom nav
        classes.append("navbar-light")
    else:
        classes.append(f"bg-{c_variant}")

    # Add border top for separation
    classes.append("border-top")

    # Merge user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Custom styles to ensure equal width items
    style = kwargs.pop("style", {})
    if isinstance(style, str):
        # Determine if it's string style, if so prepend
        style = f"padding-bottom: env(safe-area-inset-bottom); {style}"
    else:
        style["padding-bottom"] = "env(safe-area-inset-bottom)"  # iPhone Home Bar support

    attrs = {"cls": all_classes, "style": style}
    attrs.update(convert_attrs(kwargs))

    # Pass configuration down to children if needed context existed
    # For now, children (BottomNavItem) are independent

    content = Div(
        *children, cls="container-fluid d-flex justify-content-around align-items-center h-100 px-0"
    )

    return Nav(content, **attrs)


@register(category="navigation")
def BottomNavItem(
    label: str,
    href: str = "#",
    icon: str | None = None,
    active: bool = False,
    cls: str | None = None,
    **kwargs: Any,
) -> A:
    """Individual item for BottomNav.

    Args:
        label: Text label
        href: Link URL
        icon: Bootstrap icon name (e.g., "house", "person")
        active: Active state
        cls: Custom classes
        **kwargs: Additional attributes
    """
    classes = [
        "nav-link",
        "d-flex",
        "flex-column",
        "align-items-center",
        "justify-content-center",
        "w-100",
        "py-2",
    ]

    if active:
        classes.append("active")
        kwargs["aria-current"] = "page"

    # Merge user classes
    all_classes = merge_classes(" ".join(classes), cls)

    parts = []
    if icon:
        # Icon size should be slightly larger for touch targets
        parts.append(Icon(name=icon, size="1.25em", cls="mb-1" if label else ""))

    if label:
        parts.append(Small(label, cls="d-block", style="font-size: 0.75rem; line-height: 1;"))

    return A(*parts, href=href, cls=all_classes, **convert_attrs(kwargs))
