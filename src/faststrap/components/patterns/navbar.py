"""Navbar Pattern Component."""

from typing import Any

from fasthtml.common import Nav

from ...components.navigation.navbar import Navbar
from ...core._stability import beta
from ...core.base import merge_classes


@beta
def NavbarModern(
    brand: Any,
    items: list[Any] | None = None,
    sticky: bool = True,
    glass: bool = True,
    **kwargs: Any,
) -> Nav:
    """A premium, modern navbar with optional glassmorphism.

    Args:
        brand: Brand content
        items: List of nav items
        sticky: Stick to top
        glass: Apply glassmorphism effect
        **kwargs: Additional attributes

    Returns:
        Navbar component with modern styling

    Note:
        Marked as @beta - API may change in future releases.
    """
    user_cls = kwargs.pop("cls", "")
    classes = ["navbar", "navbar-expand-lg"]
    if glass:
        classes.append("navbar-glass")
    if sticky:
        classes.append("sticky-top")

    all_cls = merge_classes(" ".join(classes), user_cls)
    return Navbar(brand=brand, items=items, cls=all_cls, **kwargs)
