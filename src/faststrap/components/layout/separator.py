"""Semantic separator/divider component."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="layout")
@stable
def Separator(
    *,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    thickness: int | None = None,
    spacing: int | None = None,
    label: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a semantic separator/divider.

    Args:
        orientation: horizontal (default) or vertical
        thickness: border width in px (default: 1)
        spacing: margin in Bootstrap spacing units (0-5)
        label: optional text label centered on the divider
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with separator styling
    """
    user_cls = kwargs.pop("cls", "")

    if orientation == "vertical":
        classes = ["vr"]
        style_parts = ["display: inline-block; width: 1px;"]
        if thickness is not None:
            style_parts.append(f"width: {thickness}px;")
        if spacing is not None:
            style_parts.append(f"margin-inline: {spacing * 0.25}rem;")
        attrs: dict[str, Any] = {
            "cls": merge_classes(" ".join(classes), user_cls),
            "role": "separator",
            "aria-orientation": "vertical",
            "style": " ".join(style_parts),
        }
        attrs.update(convert_attrs(kwargs))
        return Div(**attrs)
    else:
        if label:
            # Labeled divider: line — text — line
            line_cls = merge_classes("flex-grow-1 border", user_cls)
            label_cls = "px-2 text-muted small"
            style_parts = ["border-top-width: 1px;"]
            if thickness is not None:
                style_parts.append(f"border-top-width: {thickness}px;")
            if spacing is not None:
                style_parts.append(f"margin-block: {spacing * 0.25}rem;")

            attrs = {
                "cls": "d-flex align-items-center",
                "role": "separator",
                "aria-orientation": "horizontal",
            }
            if spacing is not None:
                attrs["style"] = " ".join(style_parts)
            attrs.update(convert_attrs(kwargs))

            return Div(
                Div(cls=line_cls),
                Span(label, cls=label_cls),
                Div(cls=line_cls),
                **attrs,
            )
        else:
            # Simple divider
            classes = ["border-top"]
            if spacing is not None:
                classes.append(f"my-{spacing}")
            attrs = {
                "cls": merge_classes(" ".join(classes), user_cls),
                "role": "separator",
                "aria-orientation": "horizontal",
            }
            if thickness is not None:
                attrs["style"] = f"border-top-width: {thickness}px;"
            attrs.update(convert_attrs(kwargs))
            return Div(**attrs)
