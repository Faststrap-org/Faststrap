"""Single-active toggle button groups."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Input

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs


def ToggleGroup(
    *buttons: Any,
    name: str | None = None,
    values: list[str] | None = None,
    active_index: int = 0,
    active_cls: str = "active",
    hidden_input: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a button group where only one item stays active at a time."""
    btn_list = list(buttons)
    if not btn_list:
        raise ValueError("ToggleGroup requires at least one button.")
    if values is not None and len(values) != len(btn_list):
        raise ValueError("values length must match number of buttons.")

    input_id = f"fs-toggle-{uuid4().hex[:8]}"
    safe_active_index = max(0, min(active_index, len(btn_list) - 1))

    for i, button in enumerate(btn_list):
        if not hasattr(button, "attrs"):
            continue
        button_attrs = button.attrs
        button_attrs["data-fs-toggle-item"] = "true"
        button_attrs["data-fs-value"] = values[i] if values is not None else str(i)
        current_cls = button_attrs.get("cls", "")
        if i == safe_active_index:
            button_attrs["cls"] = merge_classes(current_cls, active_cls)
            button_attrs["aria-pressed"] = "true"
            button_attrs["aria-current"] = "true"
        else:
            button_attrs["aria-pressed"] = "false"
            button_attrs["aria-current"] = "false"

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("btn-group", user_cls),
        "role": "group",
        "data_fs_toggle_group": "true",
        "data_fs_active_class": active_cls,
    }
    if hidden_input and name:
        attrs["data_fs_input_id"] = input_id
    attrs.update(convert_attrs(kwargs))

    children: list[Any] = btn_list
    if hidden_input and name:
        selected = values[safe_active_index] if values else str(safe_active_index)
        children.append(Input(type="hidden", name=name, value=selected, id=input_id))
    return Div(*children, **attrs)
