"""Bootstrap Select component for dropdown selections."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Label, Option, Small
from fasthtml.common import Select as FTSelect

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


@register(category="forms")
def Select(
    name: str,
    *options: tuple[str, str] | tuple[str, str, bool],
    label: str | None = None,
    help_text: str | None = None,
    size: SizeType | None = None,
    disabled: bool | None = None,
    required: bool | None = None,
    multiple: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Select component for dropdown selections.

    Args:
        name: Select name attribute
        *options: Options as (value, label) or (value, label, selected)
        label: Label text
        help_text: Helper text below select
        size: Select size (sm, lg)
        disabled: Whether select is disabled
        required: Whether select is required
        multiple: Allow multiple selections
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Select", size=size, disabled=disabled, required=required, multiple=multiple
    )

    c_size = cfg.get("size")
    c_disabled = cfg.get("disabled", False)
    c_required = cfg.get("required", False)
    c_multiple = cfg.get("multiple", False)

    # Ensure ID for label linkage
    select_id = kwargs.pop("id", name)

    # Build select classes
    classes = ["form-select"]
    if c_size:
        classes.append(f"form-select-{c_size}")

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "name": name,
        "id": select_id,
    }

    if c_disabled:
        attrs["disabled"] = True
    if c_required:
        attrs["required"] = True
    if c_multiple:
        attrs["multiple"] = True

    # ARIA for help text
    if help_text:
        attrs["aria_describedby"] = f"{select_id}-help"

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Process options
    option_nodes: list[Any] = []
    for item in options:
        is_selected = False

        if len(item) == 3:
            value, label_text, is_selected = item
        elif len(item) == 2:
            value, label_text = item
        else:
            raise ValueError(
                f"Option must be (value, label) or (value, label, selected), got {item}"
            )

        opt_attrs: dict[str, Any] = {"value": value}
        if is_selected:
            opt_attrs["selected"] = True

        option_nodes.append(Option(label_text, **opt_attrs))

    # Create select element
    select_el = FTSelect(*option_nodes, **attrs)

    # If just select (no label/help), return select only
    if not label and not help_text:
        return select_el

    # Wrap in div with label and help text
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
