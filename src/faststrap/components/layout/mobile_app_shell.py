"""Responsive application shell for desktop and mobile navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Main

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from .safe_area import SafeArea


def _slot(value: Any, *, cls: str) -> Any | None:
    if value is None:
        return None
    return Div(value, cls=cls)


@register(category="layout")
@beta
def MobileAppShell(
    *children: Any,
    desktop_nav: Any | None = None,
    mobile_nav: Any | None = None,
    sidebar: Any | None = None,
    drawer: Any | None = None,
    mobile_toolbar: Any | None = None,
    bottom_nav: Any | None = None,
    safe_area: bool = True,
    content_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Compose responsive navigation, content, and mobile-safe-area surfaces.

    Navigation slots are deliberately rendered by the caller, so existing
    ``Navbar``, ``SidebarNavbar``, ``Drawer``, and ``BottomNav`` APIs remain
    unchanged and can be replaced independently.
    """
    user_cls = kwargs.pop("cls", "")
    content_children = [SafeArea(*children, edges="bottom")] if safe_area else list(children)
    content: Any = Main(
        *content_children,
        id="main-content",
        cls=merge_classes("faststrap-mobile-app-content flex-grow-1 min-w-0", content_cls or ""),
    )

    parts: list[Any] = []
    for value, cls in (
        (desktop_nav, "d-none d-lg-block"),
        (mobile_nav, "d-lg-none"),
        (sidebar, "d-none d-lg-block"),
        (drawer, "faststrap-mobile-app-drawer"),
        (mobile_toolbar, "d-lg-none"),
    ):
        if (part := _slot(value, cls=cls)) is not None:
            parts.append(part)

    parts.append(content)
    if bottom_nav is not None:
        parts.append(_slot(bottom_nav, cls="d-lg-none faststrap-mobile-app-bottom-nav"))

    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-mobile-app-shell d-flex flex-column min-vh-100", user_cls),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*parts, **attrs)
