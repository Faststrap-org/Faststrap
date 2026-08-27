"""Opinionated action button variants."""

from __future__ import annotations

from typing import Any, Literal, cast, get_args

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.types import SizeType, VariantType
from .button import Button

GradientPreset = Literal["purple", "blue", "green", "orange", "pink"]
FabPosition = Literal["bottom-right", "bottom-left", "top-right", "top-left"]
FabSize = Literal["sm", "md", "lg"]
FabShape = Literal["circle", "pill"]
GradientHover = Literal["default", "lift", "glow", "none"]

# All presets keep >=3:1 contrast (WCAG 1.4.11 non-text/UI) against the
# default white label across the full gradient; darker ends approach 4.5:1.
# Pass `text_color` for custom gradients or a strict AA small-text target.
GRADIENT_PRESETS: dict[str, str] = {
    "purple": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "blue": "linear-gradient(135deg, #1d4ed8 0%, #0284c7 100%)",
    "green": "linear-gradient(135deg, #15803d 0%, #0d9488 100%)",
    "orange": "linear-gradient(135deg, #ea580c 0%, #c2410c 100%)",
    "pink": "linear-gradient(135deg, #ec4899 0%, #be185d 100%)",
}

_FAB_SIZE_PX: dict[str, int] = {"sm": 44, "md": 48, "lg": 56}


@register(category="forms")
@beta
def GradientButton(
    *children: Any,
    gradient: GradientPreset | str | None = UNSET,
    size: SizeType | None = UNSET,
    text_color: str | None = None,
    hover: GradientHover = "default",
    **kwargs: Any,
) -> Any:
    """Render a Bootstrap-compatible button with a gradient surface.

    Args:
        *children: Button content.
        gradient: Preset name or a raw CSS ``linear-gradient(...)`` value.
        size: Core ``Button`` size.
        text_color: Override for the label color. Set this when a preset's
            light end would otherwise fail contrast against white text.
        hover: Hover treatment: ``default`` (subtle brightness), ``lift``
            (translate + shadow), ``glow`` (focus-style ring), or ``none``.
        **kwargs: Additional ``Button`` kwargs (cls, css_vars, hx-*, ...).
    """
    cfg = resolve_defaults("GradientButton", gradient=gradient, size=size)
    c_gradient = cfg.get("gradient") or "purple"
    c_size = cast(SizeType | None, cfg.get("size"))
    gradient_value = GRADIENT_PRESETS.get(str(c_gradient), str(c_gradient))

    user_cls = kwargs.pop("cls", "")
    # Copy before mutating so callers can safely reuse their css_vars dict.
    css_vars = {**(kwargs.pop("css_vars", {}) or {})}
    css_vars["--faststrap-gradient-button-bg"] = gradient_value
    if text_color:
        css_vars["--faststrap-gradient-button-text"] = text_color

    classes = ["faststrap-gradient-button"]
    if hover == "lift":
        classes.append("hover-lift")
    elif hover == "glow":
        classes.append("hover-glow")
    elif hover == "none":
        classes.append("hover-none")

    return Button(
        *children,
        size=c_size,
        variant="primary",
        cls=merge_classes(*classes, user_cls),
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
    size: FabSize | None = UNSET,
    offset: int | None = UNSET,
    shape: FabShape | None = UNSET,
    **kwargs: Any,
) -> Any:
    """Render a fixed-position floating action button.

    Args:
        *children: Optional text content; combine with ``shape="pill"`` for an
            extended FAB.
        icon: Bootstrap icon name for icon-only usage.
        variant: Bootstrap color variant.
        position: Fixed corner placement.
        label: Accessible label (required meaningfully when icon-only).
        size: Logical size token driving the ``--fs-fab-size`` CSS variable
            (``sm``=44px, ``md``=48px, ``lg``=56px). Default keeps the
            historical 56px circle.
        offset: Inset from the viewport edge in spacing units (1 unit =
            ``--bs-spacer`` ≈ 1rem), driving ``--fs-fab-inset``. Reduce for
            tighter mobile layouts.
        shape: ``circle`` (default) or ``pill`` for extended icon+label FABs.
        **kwargs: Additional ``Button`` kwargs (cls, css_vars, hx-*, style, ...).
    """
    if (
        position is not UNSET
        and position is not None
        and str(position) not in get_args(FabPosition)
    ):
        raise ValueError(f"position must be one of {get_args(FabPosition)}, got {position!r}")
    if size is not UNSET and size is not None and str(size) not in get_args(FabSize):
        raise ValueError(f"size must be one of {get_args(FabSize)}, got {size!r}")
    if shape is not UNSET and shape is not None and str(shape) not in get_args(FabShape):
        raise ValueError(f"shape must be one of {get_args(FabShape)}, got {shape!r}")

    cfg = resolve_defaults(
        "FloatingActionButton",
        variant=variant,
        position=position,
        label=label,
        size=size,
        offset=offset,
        shape=shape,
    )
    c_variant = cast(VariantType, cfg.get("variant") or "primary")
    c_position = cfg.get("position") or "bottom-right"
    c_label = cfg.get("label") or "Primary action"
    c_size = cast(FabSize | None, cfg.get("size")) or "lg"
    c_offset = cfg.get("offset")
    c_shape = cast(FabShape, cfg.get("shape") or "circle")

    user_cls = kwargs.pop("cls", "")
    fab_classes = ["faststrap-floating-action-button"]
    if c_shape == "pill":
        fab_classes.append("fab-pill")
    else:
        fab_classes.append("rounded-circle")
    fab_classes.append(f"fab-{c_position}")

    css_vars = {**(kwargs.pop("css_vars", {}) or {})}
    css_vars.setdefault("--fs-fab-size", f"{_FAB_SIZE_PX.get(str(c_size), 56)}px")
    if c_offset is not None:
        css_vars["--fs-fab-inset"] = f"{c_offset}rem"

    kwargs["css_vars"] = css_vars

    return Button(
        *children,
        variant=c_variant,
        icon=icon,
        cls=merge_classes(*fab_classes, user_cls),
        aria_label=c_label,
        **kwargs,
    )
