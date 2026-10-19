"""Safe-area-aware layout wrapper for mobile browser insets."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

SafeAreaEdges = Literal["all", "top", "right", "bottom", "left", "vertical", "horizontal"]
SafeAreaMode = Literal["padding", "margin"]


@register(category="layout")
@beta
def SafeArea(
    *children: Any,
    edges: SafeAreaEdges = "all",
    mode: SafeAreaMode = "padding",
    **kwargs: Any,
) -> Div:
    """Wrap content with CSS safe-area inset padding or margin."""
    if edges not in {"all", "top", "right", "bottom", "left", "vertical", "horizontal"}:
        raise ValueError("edges must be a supported safe-area edge group")
    if mode not in {"padding", "margin"}:
        raise ValueError("mode must be 'padding' or 'margin'")

    user_cls = kwargs.pop("cls", "")
    attrs = {
        "cls": merge_classes(
            "faststrap-safe-area",
            f"safe-area-{mode}-{edges}",
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
