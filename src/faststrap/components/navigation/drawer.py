"""Bootstrap Offcanvas (Drawer) component for side panels."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H5, Div

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import PlacementType
from ...utils.attrs import convert_attrs
from ..forms.button import CloseButton


@register(category="navigation", requires_js=True)
def Drawer(
    *children: Any,
    drawer_id: str | None = None,
    title: str | None = None,
    footer: Any | None = None,
    placement: PlacementType | None = None,
    backdrop: bool | None = None,
    scroll: bool | None = None,
    dark: bool | None = None,
    header_cls: str | None = None,
    body_cls: str | None = None,
    footer_cls: str | None = None,
    title_cls: str | None = None,
    close_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Offcanvas (Drawer) component for side panels and menus.

    Args:
        *children: Drawer body content
        drawer_id: Unique ID for the drawer (required for Bootstrap JS)
        title: Drawer header title
        footer: Drawer footer content
        placement: Drawer position (start=left, end=right, top, bottom)
        backdrop: Show backdrop overlay
        scroll: Allow body scroll when drawer is open
        dark: Use dark variant (Bootstrap 5.3+)
        **kwargs: Additional HTML attributes (cls, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with offcanvas structure
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Drawer",
        placement=placement,
        backdrop=backdrop,
        scroll=scroll,
        dark=dark,
        header_cls=header_cls,
        body_cls=body_cls,
        footer_cls=footer_cls,
        title_cls=title_cls,
        close_cls=close_cls,
    )

    c_placement = cfg.get("placement", "start")
    c_backdrop = cfg.get("backdrop", True)
    c_scroll = cfg.get("scroll", False)
    c_dark = cfg.get("dark", False)
    c_header_cls = cfg.get("header_cls", "")
    c_body_cls = cfg.get("body_cls", "")
    c_footer_cls = cfg.get("footer_cls", "")
    c_title_cls = cfg.get("title_cls", "")
    c_close_cls = cfg.get("close_cls", "")

    # Ensure drawer id
    if drawer_id is None:
        from uuid import uuid4

        drawer_id = f"drawer-{uuid4().hex}"

    # Build offcanvas classes
    classes = ["offcanvas", f"offcanvas-{c_placement}"]

    if c_dark:
        classes.append("offcanvas-dark")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Prevent accidental conflict with our explicit id
    kwargs.pop("id", None)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "tabindex": "-1",
        "aria_labelledby": f"{drawer_id}Label",
    }

    # Configure backdrop and scroll
    if not c_backdrop:
        attrs["data_bs_backdrop"] = "false"
    if c_scroll:
        attrs["data_bs_scroll"] = "true"

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Build drawer structure
    parts = []

    # Header
    if title:
        header = Div(
            H5(title, cls=merge_classes("offcanvas-title", c_title_cls), id=f"{drawer_id}Label"),
            CloseButton(cls=c_close_cls, data_bs_dismiss="offcanvas"),
            cls=merge_classes("offcanvas-header", c_header_cls),
        )
        parts.append(header)

    # Body
    body = Div(*children, cls=merge_classes("offcanvas-body", c_body_cls))
    parts.append(body)

    # Footer (optional)
    if footer is not None:
        parts.append(Div(footer, cls=merge_classes("offcanvas-footer", c_footer_cls)))

    # Create the drawer with correct attrs including id
    return Div(*parts, id=drawer_id, **attrs)
