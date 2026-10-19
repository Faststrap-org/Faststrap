"""Accessible server-rendered segmented control."""

from __future__ import annotations

from typing import Any, Literal
from uuid import uuid4

from fasthtml.common import Div, Input

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="forms")
@beta
def SegmentedControl(
    *options: Any,
    name: str | None = None,
    values: list[str] | None = None,
    active_index: int = 0,
    orientation: Literal["horizontal", "vertical"] = "horizontal",
    active_cls: str = "active",
    hidden_input: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a single-choice control from buttons, links, or HTMX options.

    The active state is server-rendered. A hidden input can carry the selected
    value through a surrounding form; links and HTMX attributes remain fully
    usable for route-driven navigation.
    """
    option_list = list(options)
    if not option_list:
        raise ValueError("SegmentedControl requires at least one option")
    if values is not None and len(values) != len(option_list):
        raise ValueError("values length must match number of options")
    if orientation not in {"horizontal", "vertical"}:
        raise ValueError("orientation must be horizontal or vertical")

    safe_index = max(0, min(active_index, len(option_list) - 1))
    input_id = f"fs-segmented-{uuid4().hex[:8]}"
    for index, option in enumerate(option_list):
        if not hasattr(option, "attrs"):
            continue
        option_attrs = option.attrs
        option_attrs["role"] = "radio"
        option_attrs["aria-checked"] = "true" if index == safe_index else "false"
        option_attrs["aria-pressed"] = "true" if index == safe_index else "false"
        if index == safe_index:
            option_attrs["cls"] = merge_classes(option_attrs.get("cls", ""), active_cls)
        if values is not None:
            option_attrs["data-fs-value"] = values[index]

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-segmented-control btn-group",
            "flex-column" if orientation == "vertical" else "",
            user_cls,
        ),
        "role": "radiogroup",
        "data_fs_segmented_control": "true",
    }
    if name:
        attrs["data_fs_input_id"] = input_id
    attrs.update(convert_attrs(kwargs))

    children = list(option_list)
    if name and hidden_input:
        selected = values[safe_index] if values else str(safe_index)
        children.append(Input(type="hidden", name=name, value=selected, id=input_id))
    return Div(*children, **attrs)
