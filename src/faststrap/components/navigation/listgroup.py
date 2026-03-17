"""Bootstrap ListGroup and Collapse components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A, Button, Div, Li, Ul

from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs


@register(category="navigation")
def ListGroup(
    *children: Any,
    flush: bool = False,
    horizontal: bool | Literal["sm", "md", "lg", "xl", "xxl"] = False,
    numbered: bool = False,
    **kwargs: Any,
) -> Ul | Div:
    """Bootstrap ListGroup component.

    A flexible component for displaying lists of content.

    Args:
        *children: ListGroupItem components or other content
        flush: Remove borders for edge-to-edge display in parent containers
        horizontal: Display items horizontally. True for all breakpoints,
                   or specify breakpoint (sm, md, lg, xl, xxl)
        numbered: Display numbered list
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Ul or Div element with list-group structure

    Example:
        Basic list:
        >>> ListGroup(
        ...     ListGroupItem("Item 1"),
        ...     ListGroupItem("Item 2"),
        ...     ListGroupItem("Item 3"),
        ... )

        With active and disabled items:
        >>> ListGroup(
        ...     ListGroupItem("Active", active=True),
        ...     ListGroupItem("Normal"),
        ...     ListGroupItem("Disabled", disabled=True),
        ... )

        Flush style:
        >>> ListGroup(
        ...     ListGroupItem("Edge to edge"),
        ...     flush=True
        ... )

        Horizontal:
        >>> ListGroup(
        ...     ListGroupItem("Left"),
        ...     ListGroupItem("Center"),
        ...     ListGroupItem("Right"),
        ...     horizontal=True
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/list-group/
    """
    # Build classes
    classes = ["list-group"]

    if flush:
        classes.append("list-group-flush")

    if horizontal:
        if horizontal is True:
            classes.append("list-group-horizontal")
        else:
            classes.append(f"list-group-horizontal-{horizontal}")

    if numbered:
        classes.append("list-group-numbered")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Use Div for numbered lists (they use ol styling via CSS)
    if numbered:
        return Div(*children, **attrs)

    return Ul(*children, **attrs)


@register(category="navigation")
def ListGroupItem(
    *children: Any,
    variant: VariantType | None = None,
    active: bool = False,
    disabled: bool = False,
    action: bool = False,
    href: str | None = None,
    badge: Any = None,
    **kwargs: Any,
) -> Li | A | Button:
    """Bootstrap ListGroup Item component.

    A single item within a ListGroup.

    Args:
        *children: Item content
        variant: Bootstrap color variant for background
        active: Mark item as active/selected
        disabled: Disable the item
        action: Enable hover/focus styles (for interactive items)
        href: Make item a link (renders as <a>)
        badge: Optional badge to display on right side
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Li, A, or Button element

    Example:
        Basic item:
        >>> ListGroupItem("Simple item")

        Active with variant:
        >>> ListGroupItem("Selected", variant="primary", active=True)

        Link item:
        >>> ListGroupItem("Click me", href="/page", action=True)

        With badge:
        >>> ListGroupItem("Messages", badge=Badge("5", variant="primary"))

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/list-group/
    """
    # Build classes
    classes = ["list-group-item"]

    if variant:
        classes.append(f"list-group-item-{variant}")

    if active:
        classes.append("active")

    if disabled:
        classes.append("disabled")

    if action or href:
        classes.append("list-group-item-action")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}

    if active:
        attrs["aria-current"] = "true"

    if disabled and not href:
        attrs["aria-disabled"] = "true"

    attrs.update(convert_attrs(kwargs))

    # Build content with optional badge
    content = list(children)
    if badge:
        # Wrap content for flex layout with badge
        content = [
            Div(
                Div(*children),
                badge,
                cls="d-flex justify-content-between align-items-center w-100",
            )
        ]

    # Determine element type
    if href:
        if disabled:
            attrs["tabindex"] = "-1"
            attrs["aria-disabled"] = "true"
        return A(*content, href=href, **attrs)

    return Li(*content, **attrs)


@register(category="navigation", requires_js=True)
def Collapse(
    *children: Any,
    collapse_id: str,
    show: bool = False,
    horizontal: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap Collapse component.

    A collapsible content container that can be toggled.

    Args:
        *children: Content to show/hide
        collapse_id: Required unique ID for the collapse
        show: Whether collapse is initially visible
        horizontal: Collapse horizontally instead of vertically
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with collapse classes

    Example:
        Basic collapse:
        >>> Button("Toggle", data_bs_toggle="collapse", data_bs_target="#myCollapse")
        >>> Collapse("Hidden content", collapse_id="myCollapse")

        Initially visible:
        >>> Collapse("Visible content", collapse_id="demo", show=True)

        Horizontal collapse:
        >>> Collapse(
        ...     Div("Content", style="width: 300px"),
        ...     collapse_id="horizontal",
        ...     horizontal=True
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/collapse/
    """
    # Build classes
    classes = ["collapse"]

    if horizontal:
        classes.append("collapse-horizontal")

    if show:
        classes.append("show")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(*children, id=collapse_id, **attrs)
