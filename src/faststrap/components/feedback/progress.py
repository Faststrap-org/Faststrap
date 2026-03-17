"""Bootstrap Progress component for progress bars."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import VariantType
from ...utils.attrs import convert_attrs


@register(category="feedback")
def Progress(
    value: int,
    max_value: int = 100,
    variant: VariantType | None = None,
    striped: bool | None = None,
    animated: bool | None = None,
    label: str | None = None,
    height: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Progress component for progress bars.

    Args:
        value: Current progress value
        max_value: Maximum value (default 100)
        variant: Bootstrap color variant
        striped: Use striped style
        animated: Animate stripes (requires striped=True)
        label: Label text to display
        height: Custom height (e.g., "20px")
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults("Progress", variant=variant, striped=striped, animated=animated)

    c_variant = cfg.get("variant", "primary")
    c_striped = cfg.get("striped", False)
    c_animated = cfg.get("animated", False)

    # Calculate percentage (guard against zero/negative max)
    if max_value <= 0:
        pct: float = 0.0
    else:
        pct = min(100.0, max(0.0, (value / max_value) * 100))

    # Build bar classes
    bar_classes = ["progress-bar"]
    if c_variant:
        bar_classes.append(f"bg-{c_variant}")
    if c_striped:
        bar_classes.append("progress-bar-striped")
    if c_animated:
        bar_classes.append("progress-bar-animated")

    # Create progress bar
    bar = Div(
        label or "",
        cls=" ".join(bar_classes),
        role="progressbar",
        aria_valuenow=value,
        aria_valuemin=0,
        aria_valuemax=max_value,
        style=f"width: {pct}%",
    )

    # Build wrapper
    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes("progress", user_cls)

    wrapper_attrs: dict[str, Any] = {"cls": wrapper_cls}
    if height:
        wrapper_attrs["style"] = f"height: {height}"

    # Convert remaining kwargs
    wrapper_attrs.update(convert_attrs(kwargs))

    return Div(bar, **wrapper_attrs)


@register(category="feedback")
def ProgressBar(
    value: int,
    max_value: int = 100,
    variant: VariantType | None = None,
    striped: bool | None = None,
    animated: bool | None = None,
    label: str | None = None,
    **kwargs: Any,
) -> Div:
    """Individual progress bar for stacked progress bars."""
    # Resolve API defaults
    cfg = resolve_defaults(
        "Progress", variant=variant, striped=striped, animated=animated  # Reusing Progress defaults
    )

    c_variant = cfg.get("variant", "primary")
    c_striped = cfg.get("striped", False)
    c_animated = cfg.get("animated", False)

    # Calculate percentage (guard against zero/negative max)
    if max_value <= 0:
        pct: float = 0.0
    else:
        pct = min(100.0, max(0.0, (value / max_value) * 100))

    # Build classes
    classes = ["progress-bar"]
    if c_variant:
        classes.append(f"bg-{c_variant}")
    if c_striped:
        classes.append("progress-bar-striped")
    if c_animated:
        classes.append("progress-bar-animated")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "role": "progressbar",
        "aria_valuenow": value,
        "aria_valuemin": 0,
        "aria_valuemax": max_value,
        "style": f"width: {pct}%",
    }

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    return Div(label or "", **attrs)
