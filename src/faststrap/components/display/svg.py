"""SVG rendering component with optional sanitization."""

from __future__ import annotations

import importlib
from typing import Any, cast

from fasthtml.common import Div, NotStr

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

DEFAULT_SVG_TAGS = [
    "svg",
    "g",
    "path",
    "rect",
    "circle",
    "line",
    "polyline",
    "polygon",
    "ellipse",
    "text",
    "tspan",
    "defs",
    "linearGradient",
    "radialGradient",
    "stop",
    "clipPath",
    "mask",
    "pattern",
    "title",
    "desc",
]

DEFAULT_SVG_ATTRIBUTES: dict[str, list[str]] = {
    "*": [
        "id",
        "class",
        "fill",
        "fill-opacity",
        "stroke",
        "stroke-width",
        "stroke-linecap",
        "stroke-linejoin",
        "stroke-opacity",
        "opacity",
        "transform",
        "viewBox",
        "width",
        "height",
        "x",
        "y",
        "rx",
        "ry",
        "cx",
        "cy",
        "r",
        "x1",
        "x2",
        "y1",
        "y2",
        "points",
        "d",
        "font-size",
        "font-family",
        "text-anchor",
        "aria-label",
        "role",
        "focusable",
    ],
    "svg": ["xmlns", "viewBox", "width", "height", "role", "aria-label", "focusable"],
}

DEFAULT_SVG_PROTOCOLS = ["http", "https", "data"]


def _load_bleach_module() -> Any:
    try:
        return importlib.import_module("bleach")
    except ImportError as exc:
        msg = "SVG sanitization requires `bleach`. Install with `pip install faststrap[markdown]`."
        raise ImportError(msg) from exc


def render_svg(
    svg: str,
    *,
    sanitize: bool = True,
    allowed_tags: list[str] | None = None,
    allowed_attributes: dict[str, list[str]] | None = None,
    allowed_protocols: list[str] | None = None,
) -> str:
    """Render SVG markup with optional sanitization."""
    if not sanitize:
        return svg

    bleach_module = _load_bleach_module()
    return cast(
        str,
        bleach_module.clean(
            svg,
            tags=allowed_tags or DEFAULT_SVG_TAGS,
            attributes=allowed_attributes or DEFAULT_SVG_ATTRIBUTES,
            protocols=allowed_protocols or DEFAULT_SVG_PROTOCOLS,
            strip=True,
        ),
    )


@register(category="display")
@beta
def Svg(
    svg: str,
    *,
    sanitize: bool = True,
    allowed_tags: list[str] | None = None,
    allowed_attributes: dict[str, list[str]] | None = None,
    allowed_protocols: list[str] | None = None,
    **kwargs: Any,
) -> Div:
    """Render raw SVG into a styled container."""
    content = render_svg(
        svg,
        sanitize=sanitize,
        allowed_tags=allowed_tags,
        allowed_attributes=allowed_attributes,
        allowed_protocols=allowed_protocols,
    )

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-svg", user_cls),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(NotStr(content), **attrs)
