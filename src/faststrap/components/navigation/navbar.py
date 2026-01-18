"""Bootstrap Navbar component for site navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Button, Div, Nav, Span

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.theme import resolve_defaults
from ...core.types import ExpandType
from ...utils.attrs import convert_attrs

# Deterministic ID counter for navbar togglers
_navbar_id_counter = 0


def _get_next_navbar_id() -> str:
    """Generate deterministic navbar ID for collapse toggler.

    Returns:
        Unique navbar ID string (e.g., 'navbar1', 'navbar2', etc.)
    """
    global _navbar_id_counter
    _navbar_id_counter += 1
    return f"navbar{_navbar_id_counter}"


@stable
def Navbar(
    *children: Any,
    items: list[Any] | None = None,
    brand: Any | None = None,
    brand_href: str = "/",
    variant: str | None = None,
    color_scheme: str | None = None,
    bg: str | None = None,
    expand: ExpandType | None = None,
    sticky: str | None = None,
    fixed: str | None = None,
    container: bool | str = True,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Navbar component for responsive site navigation.

    Args:
        *children: Navbar content
        items: Navbar items list (links, buttons, etc.)
        brand: Brand text or logo
        brand_href: Brand link URL (default: "/")
        variant: Color scheme alias (light or dark text)
        color_scheme: Color scheme (light or dark text)
        bg: Background color class
        expand: Breakpoint where navbar expands
        sticky: Stick to top or bottom
        fixed: Fix to top or bottom
        container: Wrap in container
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Navbar",
        variant=variant,
        color_scheme=color_scheme,
        bg=bg,
        expand=expand,
        sticky=sticky,
        fixed=fixed,
        container=container,
    )

    # Use color_scheme (with variant as fallback)
    # Priority: 1. explicit color_scheme, 2. explicit variant, 3. global default
    c_scheme = color_scheme or variant or cfg.get("color_scheme") or cfg.get("variant", "light")

    c_bg = cfg.get("bg")
    c_expand = expand if expand is not None else cfg.get("expand", "lg")
    c_sticky = cfg.get("sticky")
    c_fixed = cfg.get("fixed")
    c_container = cfg.get("container", True)

    # Build navbar classes
    classes = ["navbar"]

    # Add expand class
    if c_expand is True:
        classes.append("navbar-expand")
    elif isinstance(c_expand, str) and c_expand not in ("never", "false"):
        if c_expand == "always":
            classes.append("navbar-expand")
        else:
            classes.append(f"navbar-expand-{c_expand}")

    # Add variant/color-scheme
    classes.append(f"navbar-{c_scheme}")

    # Add background
    if c_bg:
        classes.append(f"bg-{c_bg}")

    # Add sticky/fixed positioning
    if c_sticky:
        classes.append(f"sticky-{c_sticky}")
    elif c_fixed:
        classes.append(f"fixed-{c_fixed}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Build navbar content
    parts = []

    # Merge *children and items
    nav_content = list(children)
    if items:
        nav_content.extend(items)

    # Wrap in container if requested
    if c_container:
        container_cls = "container" if c_container is True else f"container-{c_container}"

        # Build container content
        container_parts = []

        # Brand
        if brand:
            brand_elem = A(brand, cls="navbar-brand", href=brand_href)
            container_parts.append(brand_elem)

        # Toggler for mobile (collapse button)
        if c_expand:
            toggler_id = kwargs.get("id")
            if not toggler_id:
                toggler_id = _get_next_navbar_id()

            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            container_parts.append(toggler)

            # Collapsible content
            collapse = Div(*nav_content, cls="collapse navbar-collapse", id=toggler_id)
            container_parts.append(collapse)
        else:
            # No collapse, just add children directly
            container_parts.extend(nav_content)

        parts.append(Div(*container_parts, cls=container_cls))
    else:
        # No container wrapper
        if brand:
            parts.append(A(brand, cls="navbar-brand", href=brand_href))

        if c_expand:
            # Still need collapse for mobile
            toggler_id = kwargs.get("id")
            if not toggler_id:
                toggler_id = _get_next_navbar_id()

            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            parts.append(toggler)

            collapse = Div(*nav_content, cls="collapse navbar-collapse", id=toggler_id)
            parts.append(collapse)
        else:
            parts.extend(nav_content)

    return Nav(*parts, **attrs)
