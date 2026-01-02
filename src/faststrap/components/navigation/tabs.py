"""Bootstrap Tabs component for Faststrap."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Button, Div, Li, Ul

from ...core.base import merge_classes
from ...core.theme import resolve_defaults
from ...core.types import TabType
from ...utils.attrs import convert_attrs


def Tabs(
    *items: tuple[str, Any, bool] | tuple[str, Any],
    variant: TabType | None = None,
    justified: bool | None = None,
    fill: bool | None = None,
    vertical: bool | None = None,
    htmx: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Tabs navigation component.

    Args:
        *items: Tuples of (id, label) or (id, label, active)
        variant: 'tabs' or 'pills'
        justified: Make tabs full width
        fill: Proportionally fill width
        vertical: Stack tabs vertically
        htmx: Enable HTMX-safe behavior
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Tabs", variant=variant, justified=justified, fill=fill, vertical=vertical, htmx=htmx
    )

    c_variant = cfg.get("variant", "tabs")
    c_justified = cfg.get("justified", False)
    c_fill = cfg.get("fill", False)
    c_vertical = cfg.get("vertical", False)
    c_htmx = cfg.get("htmx", False)

    # ---- Nav CSS classes -------------------------------------------------- #
    nav_classes = ["nav"]
    nav_classes.append("nav-tabs" if c_variant == "tabs" else "nav-pills")

    if c_justified:
        nav_classes.append("nav-justified")
    if c_fill:
        nav_classes.append("nav-fill")
    if c_vertical:
        nav_classes.append("flex-column")

    # ---- Build nav items -------------------------------------------------- #
    nav_items = []
    has_active = False

    for idx, item in enumerate(items):
        if len(item) == 3:
            tab_id, label, is_active = item
        elif len(item) == 2:
            tab_id, label = item
            is_active = False
        else:
            raise ValueError("Tab item must be (id, label) or (id, label, active)")

        # First tab active fallback
        if idx == 0 and not has_active and not is_active:
            is_active = True

        if is_active:
            has_active = True

        btn_id = f"{tab_id}-tab"
        link_classes = merge_classes("nav-link", "active" if is_active else "")

        # Enhanced active tab styling for better visibility
        if is_active:
            link_classes = merge_classes(link_classes, "text-body", "fw-bold")
        else:
            link_classes = merge_classes(link_classes, "text-body")

        btn_attrs = {
            "cls": link_classes,
            "id": btn_id,
            "type": "button",
            "role": "tab",
            "aria_controls": tab_id,
            "aria_selected": "true" if is_active else "false",
        }

        # HTMX Safety
        if not c_htmx:
            btn_attrs["data_bs_toggle"] = "tab"
            btn_attrs["data_bs_target"] = f"#{tab_id}"

        nav_link = Button(label, **btn_attrs)
        nav_items.append(Li(nav_link, cls="nav-item", role="presentation"))

    # ---- Build nav element ------------------------------------------------ #
    user_cls = kwargs.pop("cls", "")
    final_nav_cls = merge_classes(" ".join(nav_classes), user_cls)

    nav_attrs = {
        "cls": final_nav_cls,
        "role": "tablist",
    }
    nav_attrs.update(convert_attrs(kwargs))

    nav = Ul(*nav_items, **nav_attrs)

    # ---- Final Layout ------------------------------------------------------ #
    if c_vertical:
        return Div(
            Div(nav, cls="col-auto"),
            Div(cls="col"),
            cls="row g-0",
        )
    else:
        return Div(nav)


def TabPane(
    *children: Any,
    tab_id: str,
    active: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap tab content pane."""
    classes = ["tab-pane", "fade"]
    if active:
        classes.extend(["show", "active"])

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    attrs = {
        "cls": all_classes,
        "role": "tabpanel",
        "id": tab_id,
        "aria-labelledby": f"{tab_id}-tab",
        "tabindex": "0",
    }

    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
