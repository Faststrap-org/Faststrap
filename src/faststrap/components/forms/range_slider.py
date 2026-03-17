"""RangeSlider component for numeric range inputs."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Label, Small, Span
from fasthtml.common import Input as FTInput

from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs


@register(category="forms")
def RangeSlider(
    name: str,
    *,
    label: str | None = None,
    help_text: str | None = None,
    min_value: int | float = 0,
    max_value: int | float = 100,
    step: int | float = 1,
    value: int | float | None = None,
    dual: bool = False,
    min_name: str | None = None,
    max_name: str | None = None,
    min_selected: int | float | None = None,
    max_selected: int | float | None = None,
    show_value: bool = True,
    value_suffix: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap range slider."""
    cfg = resolve_defaults(
        "RangeSlider",
        min_value=min_value,
        max_value=max_value,
        step=step,
        dual=dual,
        show_value=show_value,
        value_suffix=value_suffix,
    )
    c_min_value = cfg.get("min_value", min_value)
    c_max_value = cfg.get("max_value", max_value)
    c_step = cfg.get("step", step)
    c_dual = cfg.get("dual", dual)
    c_show_value = cfg.get("show_value", show_value)
    c_value_suffix = cfg.get("value_suffix", value_suffix)

    slider_id = kwargs.pop("id", name)

    def _build_input(input_name: str, input_value: int | float | None, extra_id: str) -> FTInput:
        attrs: dict[str, Any] = {
            "type": "range",
            "name": input_name,
            "id": extra_id,
            "min": str(c_min_value),
            "max": str(c_max_value),
            "step": str(c_step),
            "cls": "form-range",
        }
        if input_value is not None:
            attrs["value"] = str(input_value)
        attrs.update(convert_attrs(kwargs))
        return FTInput(**attrs)

    inputs: list[Any] = []
    value_display = None

    if c_dual:
        min_field = min_name or f"{name}_min"
        max_field = max_name or f"{name}_max"
        inputs.append(_build_input(min_field, min_selected, f"{slider_id}-min"))
        inputs.append(_build_input(max_field, max_selected, f"{slider_id}-max"))
        if c_show_value:
            display = (
                f"{min_selected if min_selected is not None else c_min_value}"
                f"{c_value_suffix} — "
                f"{max_selected if max_selected is not None else c_max_value}{c_value_suffix}"
            )
            value_display = Span(display, cls="small text-muted")
    else:
        inputs.append(_build_input(name, value, slider_id))
        if c_show_value:
            display_value = value if value is not None else c_min_value
            value_display = Span(f"{display_value}{c_value_suffix}", cls="small text-muted")

    nodes: list[Any] = []
    if label:
        nodes.append(Label(label, **{"for": slider_id}, cls="form-label"))

    nodes.extend(inputs)

    if value_display:
        nodes.append(value_display)

    if help_text:
        help_id = f"{slider_id}-help"
        nodes.append(Small(help_text, cls="form-text text-muted", id=help_id))

    return Div(*nodes, cls="mb-3 faststrap-range-slider")
