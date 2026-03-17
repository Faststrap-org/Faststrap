"""Mermaid diagram rendering component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs


def _normalize_size(value: str | int) -> str:
    if isinstance(value, int):
        return f"{value}px"
    return value


@register(category="display", requires_js=True)
@beta
def Mermaid(
    diagram: str,
    *,
    theme: str | None = None,
    security_level: str | None = None,
    min_width: str | int | None = None,
    **kwargs: Any,
) -> Div:
    """Render Mermaid diagram text inside a Mermaid container."""
    cfg = resolve_defaults(
        "Mermaid",
        theme=theme,
        security_level=security_level,
    )
    c_theme = cfg.get("theme", theme)
    c_security = cfg.get("security_level", security_level)

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes("mermaid faststrap-mermaid", user_cls)

    attrs: dict[str, Any] = {
        "cls": cls,
        "data_fs_mermaid": "true",
    }

    if c_theme:
        attrs["data_fs_mermaid_theme"] = c_theme
    if c_security:
        attrs["data_fs_mermaid_security"] = c_security

    if min_width is not None:
        attrs["style"] = f"min-width: {_normalize_size(min_width)};"

    attrs.update(convert_attrs(kwargs))

    return Div(diagram, **attrs)
