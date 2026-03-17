"""DashboardGrid layout component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


def _normalize_size(value: str | int | float) -> str:
    if isinstance(value, (int, float)):
        return f"{value}rem"
    return value


def _normalize_px(value: str | int | float) -> str:
    if isinstance(value, (int, float)):
        return f"{value}px"
    return value


@register(category="layout")
@beta
def DashboardGrid(
    *children: Any,
    cols: int | None = None,
    gap: str | int | float = 1.5,
    min_card_width: str | int | float = 240,
    dense: bool = False,
    **kwargs: Any,
) -> Div:
    """Responsive dashboard grid using CSS grid."""
    if cols is not None and cols < 1:
        msg = f"cols must be >= 1, got {cols}"
        raise ValueError(msg)

    style: dict[str, Any] = {
        "display": "grid",
        "gap": _normalize_size(gap),
    }

    if cols:
        style["grid_template_columns"] = f"repeat({cols}, minmax(0, 1fr))"
    else:
        style["grid_template_columns"] = (
            f"repeat(auto-fit, minmax({_normalize_px(min_card_width)}, 1fr))"
        )

    if dense:
        style["grid_auto_flow"] = "dense"

    user_style = kwargs.pop("style", None)
    if isinstance(user_style, dict):
        style.update(user_style)

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes("faststrap-dashboard-grid", user_cls)

    kwargs["style"] = style

    attrs: dict[str, Any] = {"cls": wrapper_cls}
    attrs.update(convert_attrs(kwargs))

    if isinstance(user_style, str) and user_style:
        attrs["style"] = f"{attrs.get('style', '')}; {user_style}".strip("; ")

    return Div(*children, **attrs)
