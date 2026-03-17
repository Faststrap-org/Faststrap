"""MultiSelect component for multiple option selections."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from fasthtml.common import Div, Label, Option, Small
from fasthtml.common import Select as FTSelect

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


@register(category="forms")
def MultiSelect(
    name: str,
    *options: tuple[str, str] | tuple[str, str, bool],
    label: str | None = None,
    help_text: str | None = None,
    size: SizeType | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    selected: Iterable[str] | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap MultiSelect component."""
    cfg = resolve_defaults("MultiSelect", size=size, disabled=disabled, required=required)

    c_size = cfg.get("size")
    c_disabled = cfg.get("disabled", False)
    c_required = cfg.get("required", False)

    select_id = kwargs.pop("id", name)
    selected_set = {str(item) for item in selected} if selected else set()

    classes = ["form-select", "faststrap-multi-select"]
    if c_size:
        classes.append(f"form-select-{c_size}")

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    attrs: dict[str, Any] = {
        "cls": cls,
        "name": name,
        "id": select_id,
        "multiple": True,
    }

    if c_disabled:
        attrs["disabled"] = True
    if c_required:
        attrs["required"] = True

    if help_text:
        attrs["aria_describedby"] = f"{select_id}-help"

    attrs.update(convert_attrs(kwargs))

    option_nodes: list[Any] = []
    for item in options:
        is_selected = False
        if len(item) == 3:
            value, label_text, is_selected = item
        elif len(item) == 2:
            value, label_text = item
            is_selected = str(value) in selected_set
        else:
            raise ValueError(
                f"Option must be (value, label) or (value, label, selected), got {item}"
            )

        opt_attrs: dict[str, Any] = {"value": value}
        if is_selected:
            opt_attrs["selected"] = True

        option_nodes.append(Option(label_text, **opt_attrs))

    select_el = FTSelect(*option_nodes, **attrs)

    if not label and not help_text:
        return select_el

    nodes: list[Any] = []
    if label:
        nodes.append(
            Label(
                label,
                " ",
                Small("*", cls="text-danger") if c_required else "",
                **{"for": select_id},
                cls="form-label",
            )
        )

    nodes.append(select_el)

    if help_text:
        help_id = f"{select_id}-help"
        nodes.append(Small(help_text, cls="form-text text-muted", id=help_id))

    return Div(*nodes, cls="mb-3")
