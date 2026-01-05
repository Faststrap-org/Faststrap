"""Premium Glass Navbar with glassmorphism effect."""

from typing import Any, Literal

from fasthtml.common import A, Button, Div, Nav, Span

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs

BlurStrength = Literal["low", "medium", "high"]


@register(category="navigation")
def GlassNavbar(
    *items: Any,
    brand: str | None = None,
    brand_href: str = "/",
    blur_strength: BlurStrength | None = None,
    transparency: float | None = None,
    theme: str | None = None,
    sticky: bool | None = None,
    expand: str | None = None,
    **kwargs: Any,
) -> Nav:
    """Premium glassmorphism navbar with blur and transparency.

    A modern, premium navbar with glassmorphism effect (frosted glass appearance).
    Fully theme-aware with customizable blur and transparency.

    Args:
        *items: Navigation items (tuples of (label, href) or Nav components)
        brand: Brand name/logo text
        brand_href: Brand link URL
        blur_strength: Backdrop blur strength ("low", "medium", "high")
        transparency: Background transparency (0.0 to 1.0)
        theme: Theme variant ("light" or "dark")
        sticky: Make navbar sticky on scroll
        expand: Breakpoint for collapse ("sm", "md", "lg", "xl", "xxl")
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Nav element with glassmorphism styling

    Example:
        Basic glass navbar:
        >>> GlassNavbar(
        ...     ("Home", "/"),
        ...     ("About", "/about"),
        ...     ("Contact", "/contact"),
        ...     brand="My App",
        ...     blur_strength="medium",
        ...     theme="light"
        ... )

        High transparency:
        >>> GlassNavbar(
        ...     ("Features", "/features"),
        ...     ("Pricing", "/pricing"),
        ...     brand="Product",
        ...     transparency=0.9,
        ...     blur_strength="high"
        ... )

    Note:
        The glassmorphism effect works best over colorful backgrounds or images.
        Uses CSS backdrop-filter for the blur effect.

    See Also:
        - Navbar for standard navbar
        - SidebarNavbar for vertical sidebar
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "GlassNavbar",
        blur_strength=blur_strength,
        transparency=transparency,
        theme=theme,
        sticky=sticky,
        expand=expand,
    )

    c_blur = cfg.get("blur_strength", "medium")
    c_transparency = cfg.get("transparency", 0.8)
    c_theme = cfg.get("theme", "light")
    c_sticky = cfg.get("sticky", True)
    c_expand = cfg.get("expand", "lg")

    # Blur values
    blur_values = {"low": "5px", "medium": "10px", "high": "20px"}
    blur_px = blur_values.get(c_blur, "10px")

    # Build classes
    classes = ["navbar", f"navbar-expand-{c_expand}"]

    if c_theme == "dark":
        classes.append("navbar-dark")
    else:
        classes.append("navbar-light")

    if c_sticky:
        classes.append("sticky-top")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build glassmorphism style
    glass_style = {
        "backdrop-filter": f"blur({blur_px})",
        "-webkit-backdrop-filter": f"blur({blur_px})",  # Safari support
        "background-color": (
            f"rgba(255, 255, 255, {c_transparency})"
            if c_theme == "light"
            else f"rgba(0, 0, 0, {c_transparency})"
        ),
        "border-bottom": (
            "1px solid rgba(255, 255, 255, 0.2)"
            if c_theme == "dark"
            else "1px solid rgba(0, 0, 0, 0.1)"
        ),
        "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    }

    # Merge with user style
    user_style = kwargs.pop("style", {})
    if isinstance(user_style, dict):
        glass_style.update(user_style)
    else:
        # Convert string style to dict
        # For simplicity, just use glass_style
        pass

    # Build navbar parts
    navbar_parts = []

    # Container
    container_parts = []

    # Brand
    if brand:
        brand_classes = "navbar-brand fw-bold"
        container_parts.append(A(brand, href=brand_href, cls=brand_classes))

    # Toggler for mobile
    container_parts.append(
        Button(
            Span(cls="navbar-toggler-icon"),
            cls="navbar-toggler",
            type="button",
            data_bs_toggle="collapse",
            data_bs_target="#glassNavbarContent",
            aria_controls="glassNavbarContent",
            aria_expanded="false",
            aria_label="Toggle navigation",
        )
    )

    # Navigation items
    nav_items = []
    for item in items:
        if isinstance(item, tuple):
            # Tuple format: (label, href)
            if len(item) >= 2:
                label, href = item[:2]
                active = item[2] if len(item) > 2 else False
                nav_items.append(GlassNavItem(label, href=href, active=active))
        else:
            # Already a component
            nav_items.append(item)

    # Collapse wrapper
    container_parts.append(
        Div(
            Div(*nav_items, cls="navbar-nav ms-auto"),
            cls="collapse navbar-collapse",
            id="glassNavbarContent",
        )
    )

    navbar_parts.append(Div(*container_parts, cls="container-fluid"))

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes, "style": glass_style}

    attrs.update(convert_attrs(kwargs))

    return Nav(*navbar_parts, **attrs)


def GlassNavItem(
    label: str,
    href: str = "#",
    active: bool = False,
    **kwargs: Any,
) -> A:
    """Individual glass navbar navigation item.

    Args:
        label: Item label text
        href: Link URL
        active: Mark as active/selected
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML A element with nav-link styling

    Example:
        >>> GlassNavItem("Home", href="/", active=True)
    """
    # Build classes
    classes = ["nav-link"]

    if active:
        classes.append("active")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"href": href, "cls": all_classes}

    attrs.update(convert_attrs(kwargs))

    return A(label, **attrs)
