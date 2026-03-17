"""Bootstrap Accordion component with collapsible panels."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from fasthtml.common import H2, Button, Div

from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


def _stable_accordion_id(children: tuple[Any, ...], flush: bool, always_open: bool) -> str:
    signature: list[dict[str, Any]] = []
    for child in children:
        if isinstance(child, AccordionItemBuilder):
            signature.append(
                {
                    "title": child.title,
                    "expanded": child.expanded,
                    "header_cls": child.header_cls,
                    "body_cls": child.body_cls,
                    "button_cls": child.button_cls,
                }
            )
        else:
            signature.append({"type": child.__class__.__name__})
    digest = hashlib.sha1(
        json.dumps(
            {"children": signature, "flush": flush, "always_open": always_open},
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()[:8]
    return f"accordion-{digest}"


@register(category="navigation", requires_js=True)
def Accordion(
    *children: Any,
    accordion_id: str | None = None,
    flush: bool = False,
    always_open: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap Accordion component.

    A vertically collapsing component with multiple panels. Only one panel
    can be open at a time unless always_open is True.

    Args:
        *children: AccordionItem components
        accordion_id: Unique ID for the accordion (auto-generated if not provided)
        flush: Remove default background and borders for edge-to-edge design
        always_open: Allow multiple panels to be open simultaneously
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with accordion structure

    Example:
        Basic accordion:
        >>> Accordion(
        ...     AccordionItem("Content 1", title="Section 1", expanded=True),
        ...     AccordionItem("Content 2", title="Section 2"),
        ...     AccordionItem("Content 3", title="Section 3"),
        ... )

        Flush style:
        >>> Accordion(
        ...     AccordionItem("Content", title="Item"),
        ...     flush=True
        ... )

        Always open (multiple can be expanded):
        >>> Accordion(
        ...     AccordionItem("Content 1", title="Item 1", expanded=True),
        ...     AccordionItem("Content 2", title="Item 2", expanded=True),
        ...     always_open=True
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/accordion/
    """
    # Generate deterministic ID when not explicitly provided.
    acc_id = accordion_id or _stable_accordion_id(children, flush, always_open)

    # Build classes
    classes = ["accordion"]

    if flush:
        classes.append("accordion-flush")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Process children to inject parent ID for collapse behavior
    processed_children = []
    for i, child in enumerate(children):
        if hasattr(child, "__accordion_item__"):
            # This is an AccordionItem - inject parent reference
            processed_children.append(child.__accordion_render__(acc_id, i, always_open))
        else:
            processed_children.append(child)

    return Div(*processed_children, id=acc_id, **attrs)


class AccordionItemBuilder:
    """Builder for AccordionItem to support deferred rendering."""

    __accordion_item__ = True

    def __init__(
        self,
        *children: Any,
        title: str = "",
        expanded: bool = False,
        header_cls: str = "",
        body_cls: str = "",
        button_cls: str = "",
        **kwargs: Any,
    ):
        self.children = children
        self.title = title
        self.expanded = expanded
        self.header_cls = header_cls
        self.body_cls = body_cls
        self.button_cls = button_cls
        self.kwargs = kwargs

    def __accordion_render__(self, parent_id: str, index: int, always_open: bool) -> Div:
        """Render the accordion item with parent context."""
        collapse_id = f"{parent_id}-collapse-{index}"
        header_id = f"{parent_id}-header-{index}"

        # Build button classes
        button_classes = ["accordion-button"]
        if not self.expanded:
            button_classes.append("collapsed")

        button_cls = merge_classes(" ".join(button_classes), self.button_cls)

        # Build collapse classes
        collapse_classes = ["accordion-collapse", "collapse"]
        if self.expanded:
            collapse_classes.append("show")

        # Button attributes
        button_attrs: dict[str, Any] = {
            "cls": button_cls,
            "type": "button",
            "data-bs-toggle": "collapse",
            "data-bs-target": f"#{collapse_id}",
            "aria-expanded": "true" if self.expanded else "false",
            "aria-controls": collapse_id,
        }

        # Collapse attributes - only add parent if not always_open
        collapse_attrs: dict[str, Any] = {
            "cls": " ".join(collapse_classes),
            "aria-labelledby": header_id,
        }

        if not always_open:
            collapse_attrs["data-bs-parent"] = f"#{parent_id}"

        # Header classes
        header_cls = merge_classes("accordion-header", self.header_cls)

        # Body classes
        body_cls = merge_classes("accordion-body", self.body_cls)

        # User classes for item
        user_cls = self.kwargs.pop("cls", "")
        item_cls = merge_classes("accordion-item", user_cls)

        # Build the item
        item_attrs: dict[str, Any] = {"cls": item_cls}
        item_attrs.update(convert_attrs(self.kwargs))

        return Div(
            H2(
                Button(self.title, **button_attrs),
                cls=header_cls,
                id=header_id,
            ),
            Div(
                Div(*self.children, cls=body_cls),
                id=collapse_id,
                **collapse_attrs,
            ),
            **item_attrs,
        )


@register(category="navigation", requires_js=True)
def AccordionItem(
    *children: Any,
    title: str = "",
    expanded: bool = False,
    header_cls: str = "",
    body_cls: str = "",
    button_cls: str = "",
    **kwargs: Any,
) -> AccordionItemBuilder:
    """Bootstrap Accordion Item component.

    A single collapsible panel within an Accordion.

    Args:
        *children: Panel content
        title: Header text for the panel
        expanded: Whether panel is initially expanded
        header_cls: Additional classes for header
        body_cls: Additional classes for body
        button_cls: Additional classes for toggle button
        **kwargs: Additional HTML attributes

    Returns:
        AccordionItemBuilder for deferred rendering within Accordion

    Example:
        >>> AccordionItem(
        ...     "This is the content of the panel.",
        ...     title="Click to expand",
        ...     expanded=True
        ... )

        With custom styling:
        >>> AccordionItem(
        ...     "Content",
        ...     title="Styled Item",
        ...     header_cls="bg-primary text-white",
        ...     body_cls="p-4"
        ... )
    """
    return AccordionItemBuilder(
        *children,
        title=title,
        expanded=expanded,
        header_cls=header_cls,
        body_cls=body_cls,
        button_cls=button_cls,
        **kwargs,
    )
