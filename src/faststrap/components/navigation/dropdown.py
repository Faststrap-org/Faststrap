"""Bootstrap Dropdown component for Faststrap."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Button, Div, Li, Ul

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import DirectionType, VariantType
from ...utils.attrs import convert_attrs


@register(category="navigation", requires_js=True)
def Dropdown(
    *items: Any,
    label: str | None = None,
    variant: VariantType | None = None,
    size: str | None = None,
    split: bool | None = None,
    direction: DirectionType | None = None,
    toggle_cls: str | None = None,
    menu_cls: str | None = None,
    item_cls: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Dropdown component for contextual menus.

    Args:
        *items: Dropdown menu items
        label: Button label text
        variant: Bootstrap button variant
        size: Button size
        split: Use split button style
        direction: Dropdown direction (down, up, start, end)
        toggle_cls: Additional classes for the toggle button
        menu_cls: Additional classes for the dropdown menu
        item_cls: Additional classes for dropdown items
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Dropdown",
        label=label,
        variant=variant,
        size=size,
        split=split,
        direction=direction,
        toggle_cls=toggle_cls,
        menu_cls=menu_cls,
        item_cls=item_cls,
    )

    c_label = cfg.get("label", "Dropdown")
    c_variant = cfg.get("variant", "primary")
    c_size = cfg.get("size")
    c_split = cfg.get("split", False)
    c_direction = cfg.get("direction", "down")
    c_toggle_cls = cfg.get("toggle_cls", "")
    c_menu_cls = cfg.get("menu_cls", "")
    c_item_cls = cfg.get("item_cls", "")

    # ---- Container classes ------------------------------------------------ #
    container_classes = []

    container_classes.append(
        {
            "up": "dropup",
            "start": "dropstart",
            "end": "dropend",
            "down": "dropdown",
        }[c_direction]
    )

    if c_split:
        container_classes.append("btn-group")

    # ---- Button classes --------------------------------------------------- #
    btn_classes = ["btn", f"btn-{c_variant}"]
    if c_size:
        btn_classes.append(f"btn-{c_size}")

    btn_class_str = " ".join(btn_classes)

    toggle_id = kwargs.pop("id", "dropdownMenuButton")

    # ---- Build buttons ---------------------------------------------------- #
    buttons: list[Any] = []

    if c_split:
        # Action button (left)
        buttons.append(
            Button(c_label, cls=merge_classes(btn_class_str, c_toggle_cls), type="button")
        )

        # Toggle (right)
        buttons.append(
            Button(
                "",
                cls=merge_classes(btn_class_str, "dropdown-toggle dropdown-toggle-split"),
                type="button",
                id=toggle_id,
                data_bs_toggle="dropdown",
                aria_expanded="false",
            )
        )
    else:
        buttons.append(
            Button(
                c_label,
                cls=merge_classes(btn_class_str, "dropdown-toggle", c_toggle_cls),
                type="button",
                id=toggle_id,
                data_bs_toggle="dropdown",
                aria_expanded="false",
            )
        )

    # ---- Build dropdown items -------------------------------------------- #
    menu_items: list[Any] = []

    for item in items:
        # Check for divider string
        if isinstance(item, str) and item == "---":
            menu_items.append(Li(cls="dropdown-divider"))
            continue

        # Check for hr element
        if hasattr(item, "name") and item.name == "hr":
            menu_items.append(Li(cls="dropdown-divider"))
            continue

        # String -> <a>
        if isinstance(item, str):
            menu_items.append(
                Li(
                    A(
                        item,
                        cls=merge_classes("dropdown-item", c_item_cls),
                        href="#",
                        role="menuitem",
                    )
                )
            )
            continue

        # A / Button elements
        if hasattr(item, "name") and item.name in {"a", "button"}:
            cls = merge_classes("dropdown-item", c_item_cls, item.attrs.get("cls", ""))
            cloned_attrs = {**item.attrs, "cls": cls}
            cloned = item.__class__(*item.children, **cloned_attrs)
            menu_items.append(Li(cloned))
            continue

        # Fallback wrapper
        menu_items.append(Li(item, cls=merge_classes("dropdown-item", c_item_cls)))

    # ---- Build menu -------------------------------------------------------- #
    menu = Ul(
        *menu_items,
        cls=merge_classes("dropdown-menu", c_menu_cls),
        role="menu",
        aria_labelledby=toggle_id,
    )

    # ---- Final container --------------------------------------------------- #
    user_cls = kwargs.pop("cls", "")
    final_container_cls = merge_classes(" ".join(container_classes), user_cls)

    attrs: dict[str, Any] = {"cls": final_container_cls}
    attrs.update(convert_attrs(kwargs))

    return Div(*buttons, menu, **attrs)


@register(category="navigation", requires_js=True)
def DropdownItem(
    *children: Any,
    active: bool = False,
    disabled: bool = False,
    **kwargs: Any,
) -> A:
    """Dropdown item helper."""
    classes = ["dropdown-item"]
    if active:
        classes.append("active")
    if disabled:
        classes.append("disabled")

    cls_str = merge_classes(" ".join(classes), kwargs.pop("cls", ""))

    attrs: dict[str, Any] = {
        "cls": cls_str,
        "role": "menuitem",
    }

    if disabled:
        attrs["aria_disabled"] = "true"
        attrs["tabindex"] = "-1"

    if "href" not in kwargs:
        attrs["href"] = "#"

    attrs.update(convert_attrs(kwargs))

    return A(*children, **attrs)


@register(category="navigation", requires_js=True)
def DropdownDivider() -> Li:
    """Divider helper."""
    return Li(cls="dropdown-divider")
