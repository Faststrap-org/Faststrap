"""Opinionated action button variants."""

from __future__ import annotations

from typing import Any, Literal, cast

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.types import SizeType, VariantType
from .button import Button

GradientPreset = Literal["purple", "blue", "green", "orange", "pink"]
FabPosition = Literal["bottom-right", "bottom-left", "top-right", "top-left"]

GRADIENT_PRESETS: dict[str, str] = {
    "purple": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "blue": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
    "green": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
    "orange": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
    "pink": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
}


@register(category="forms")
@beta
def GradientButton(
    *children: Any,
    gradient: GradientPreset | str | None = UNSET,
    size: SizeType | None = UNSET,
    **kwargs: Any,
) -> Any:
    """Render a Bootstrap-compatible button with a gradient surface."""
    cfg = resolve_defaults("GradientButton", gradient=gradient, size=size)
    c_gradient = cfg.get("gradient") or "purple"
    c_size = cast(SizeType | None, cfg.get("size"))
    gradient_value = GRADIENT_PRESETS.get(str(c_gradient), str(c_gradient))

    user_cls = kwargs.pop("cls", "")
    # Copy before mutating so callers can safely reuse their css_vars dict.
    css_vars = {**(kwargs.pop("css_vars", {}) or {})}
    css_vars["--faststrap-gradient-button-bg"] = gradient_value

    return Button(
        *children,
        size=c_size,
        variant="primary",
        cls=merge_classes("faststrap-gradient-button", user_cls),
        css_vars=css_vars,
        **kwargs,
    )


@register(category="forms")
@beta
def FloatingActionButton(
    *children: Any,
    icon: str | None = None,
    variant: VariantType | None = UNSET,
    position: FabPosition | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Any:
    """Render a fixed-position floating action button."""
    cfg = resolve_defaults(
        "FloatingActionButton",
        variant=variant,
        position=position,
        label=label,
    )
    c_variant = cast(VariantType, cfg.get("variant") or "primary")
    c_position = cfg.get("position") or "bottom-right"
    c_label = cfg.get("label") or "Primary action"

    user_cls = kwargs.pop("cls", "")
    classes = merge_classes(
        "faststrap-floating-action-button rounded-circle",
        f"fab-{c_position}",
        user_cls,
    )

    return Button(
        *children,
        variant=c_variant,
        icon=icon,
        cls=classes,
        aria_label=c_label,
        **kwargs,
    )
