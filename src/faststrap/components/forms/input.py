"""Bootstrap Input component for text form controls."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Label, Small
from fasthtml.common import Input as FTInput

from ...core.base import merge_classes
from ...core.theme import resolve_defaults
from ...core.types import InputType, SizeType
from ...utils.attrs import convert_attrs


def Input(
    name: str,
    input_type: InputType | None = None,
    placeholder: str | None = None,
    value: str | None = None,
    label: str | None = None,
    help_text: str | None = None,
    size: SizeType | None = None,
    disabled: bool | None = None,
    readonly: bool | None = None,
    required: bool | None = None,
    validation_state: str | None = None,
    validation_message: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Input component for text form controls.

    Args:
        name: Input name attribute
        input_type: HTML input type
        placeholder: Placeholder text
        value: Initial value
        label: Label text
        help_text: Helper text below input
        size: Input size (sm, lg)
        disabled: Whether input is disabled
        readonly: Whether input is readonly
        required: Whether input is required
        validation_state: Validation state ('valid' or 'invalid')
        validation_message: Validation feedback message
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Input",
        input_type=input_type,
        size=size,
        disabled=disabled,
        readonly=readonly,
        required=required,
    )

    c_type = cfg.get("input_type", "text")
    c_size = cfg.get("size")
    c_disabled = cfg.get("disabled", False)
    c_readonly = cfg.get("readonly", False)
    c_required = cfg.get("required", False)

    # Ensure ID is present for label linkage
    input_id = kwargs.pop("id", name)

    # Build input classes
    input_classes = ["form-control"]
    if c_size:
        input_classes.append(f"form-control-{c_size}")
    if validation_state:
        input_classes.append(f"is-{validation_state}")

    user_cls = kwargs.pop("cls", "")
    input_cls = merge_classes(" ".join(input_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": input_cls,
        "type": c_type,
        "name": name,
        "id": input_id,
    }

    if placeholder:
        attrs["placeholder"] = placeholder
    if value:
        attrs["value"] = value
    if c_disabled:
        attrs["disabled"] = True
    if c_readonly:
        attrs["readonly"] = True
    if c_required:
        attrs["required"] = True

    # ARIA for help text
    if help_text:
        attrs["aria_describedby"] = f"{name}-help"

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Create input element
    input_elem = FTInput(**attrs)

    # If just input (no label/help), return input only
    if not label and not help_text and not validation_message:
        return input_elem

    # Wrap in div with label, help text, and validation message
    elements = []

    if label:
        label_elem = Label(
            label,
            " ",
            Small("*", cls="text-danger") if c_required else "",
            **{"for": input_id},
            cls="form-label",
        )
        elements.append(label_elem)

    elements.append(input_elem)

    if help_text:
        help_elem = Small(help_text, cls="form-text text-muted", id=f"{name}-help")
        elements.append(help_elem)

    if validation_message and validation_state:
        feedback_cls = "valid-feedback" if validation_state == "valid" else "invalid-feedback"
        feedback_elem = Div(validation_message, cls=feedback_cls)
        elements.append(feedback_elem)

    return Div(*elements, cls="mb-3")
