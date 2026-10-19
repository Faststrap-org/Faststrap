"""Safe-area-aware sticky action bar."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="layout")
@beta
def StickyActionBar(
    *children: Any,
    stack_at: Literal["sm", "md", "lg", "xl", "xxl", None] = "sm",
    safe_area: bool = True,
    justify: Literal["start", "center", "end", "between"] = "end",
    **kwargs: Any,
) -> Div:
    """Render a bottom-sticky action surface for mobile workflows."""
    if stack_at not in {None, "sm", "md", "lg", "xl", "xxl"}:
        raise ValueError("stack_at must be a Bootstrap breakpoint or None")
    if justify not in {"start", "center", "end", "between"}:
        raise ValueError("justify must be start, center, end, or between")

    user_cls = kwargs.pop("cls", "")
    stack_class = f"flex-{stack_at}-row" if stack_at else "flex-row"
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-sticky-action-bar position-sticky bottom-0 z-1 border-top bg-body",
            "py-2 px-3",
            "d-flex flex-column gap-2",
            stack_class,
            f"justify-content-{justify}",
            "faststrap-sticky-action-bar-safe" if safe_area else "",
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
