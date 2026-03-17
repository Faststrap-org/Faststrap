"""Bootstrap Tooltip and Popover components."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Span

from ...core.registry import register
from ...core.types import PlacementType, TriggerType
from ...utils.attrs import convert_attrs


@register(category="feedback", requires_js=True)
def Tooltip(
    text: str,
    *children: Any,
    placement: PlacementType = "top",
    trigger: TriggerType = "hover focus",
    html: bool = False,
    tag: str = "span",
    **kwargs: Any,
) -> Any:
    """Bootstrap Tooltip component (wrapper).

    Wraps content to add a tooltip on hover/focus.
    Requires the FastStrap init script (auto-included via add_bootstrap).

    Args:
        text: Tooltip text
        *children: Element(s) that trigger the tooltip
        placement: Position (top, right, bottom, left)
        trigger: Events that trigger the tooltip
        html: Allow HTML in tooltip text
        tag: HTML tag for the wrapper (default: "span")
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML element (Span by default) with tooltip attributes

    Example:
        >>> Tooltip("I am a tooltip", Button("Hover me"))

        >>> Tooltip("<b>Bold</b> tip", Icon("info"), html=True)
    """
    # Build attributes
    attrs: dict[str, Any] = {
        "data-bs-toggle": "tooltip",
        "data-bs-title": text,
        "data-bs-placement": placement,
        "data-bs-trigger": trigger,
    }

    if html:
        attrs["data-bs-html"] = "true"

    attrs.update(convert_attrs(kwargs))

    # We use Span by default as it's inline and non-intrusive
    # Ideally users pass a single child, but we support multiple
    return Span(*children, **attrs)


@register(category="feedback", requires_js=True)
def Popover(
    title: str,
    content: str,
    *children: Any,
    placement: PlacementType = "right",
    trigger: TriggerType = "click",
    html: bool = False,
    tag: str = "span",
    container: str | None = "body",
    **kwargs: Any,
) -> Any:
    """Bootstrap Popover component (wrapper).

    Wraps content to show a popover on click/hover.
    Requires the FastStrap init script.

    Args:
        title: Popover header
        content: Popover body text
        *children: Element(s) that trigger the popover
        placement: Position (top, right, bottom, left)
        trigger: Events (click, hover, focus)
        html: Allow HTML in content
        tag: HTML tag for wrapper
        container: Container to append to ("body" avoids containment issues)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML element with popover attributes

    Example:
        >>> Popover("Title", "Content here", Button("Click me"))
    """
    attrs: dict[str, Any] = {
        "data-bs-toggle": "popover",
        "data-bs-title": title,
        "data-bs-content": content,
        "data-bs-placement": placement,
        "data-bs-trigger": trigger,
    }

    if container:
        attrs["data-bs-container"] = container

    if html:
        attrs["data-bs-html"] = "true"

    attrs.update(convert_attrs(kwargs))

    # Using Span ("d-inline-block" might be needed for some triggers if wrapper)
    # But let's trust user or default behavior
    return Span(*children, **attrs)
