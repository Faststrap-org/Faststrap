"""Responsive aspect ratio container component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="layout")
@stable
def AspectRatio(
    children: Any,
    *,
    ratio: str = "16/9",
    **kwargs: Any,
) -> Div:
    """Render content in a responsive aspect ratio container.

    Uses the CSS aspect-ratio property for consistent sizing across viewports.
    Children fill the container; use object-fit on child media for best results.

    Args:
        children: Content to display (images, videos, iframes, etc.)
        ratio: Aspect ratio as width/height string (e.g. "16/9", "4/3", "1/1", "21/9")
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element constrained to the specified aspect ratio
    """
    user_cls = kwargs.pop("cls", "")

    classes = ["overflow-hidden"]

    style = f"aspect-ratio: {ratio};"

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
        "style": style,
    }
    attrs.update(convert_attrs(kwargs))

    # Wrap children in a container that fills the aspect ratio box
    inner = Div(
        children,
        style="width: 100%; height: 100%;",
    )

    return Div(inner, **attrs)
