"""Bootstrap form controls: Checkbox, Radio, Switch, and Range."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, Label
from fasthtml.common import Input as FTInput

from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


@register(category="forms")
def Checkbox(
    name: str,
    *,
    label: str | None = None,
    value: str = "1",
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    inline: bool = False,
    reverse: bool = False,
    checkbox_id: str | None = None,
    size: SizeType | None = None,
    input_cls: str = "",
    label_cls: str = "",
    help_text: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Checkbox component.

    A styled checkbox form control with optional label.

    Args:
        name: Input name attribute
        label: Label text for the checkbox
        value: Value when checked (default: "1")
        checked: Whether checkbox is initially checked
        disabled: Disable the checkbox
        required: Mark as required field
        inline: Display inline with other checkboxes
        reverse: Put checkbox on the right side of label
        checkbox_id: ID for the input (auto-generated from name if not provided)
        size: Control size (sm, lg)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        help_text: Help text displayed below
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with form-check structure

    Example:
        Basic checkbox:
        >>> Checkbox("remember", label="Remember me")

        Checked by default:
        >>> Checkbox("agree", label="I agree", checked=True, required=True)

        Inline checkboxes:
        >>> Checkbox("opt1", label="Option 1", inline=True)
        >>> Checkbox("opt2", label="Option 2", inline=True)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/checks-radios/
    """
    cb_id = checkbox_id or f"checkbox-{name}"

    # Wrapper classes
    wrapper_classes = ["form-check"]
    if inline:
        wrapper_classes.append("form-check-inline")
    if reverse:
        wrapper_classes.append("form-check-reverse")

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(wrapper_classes), user_cls)

    # Input classes
    input_classes = ["form-check-input"]
    if size:
        input_classes.append(f"form-check-input-{size}")
    all_input_cls = merge_classes(" ".join(input_classes), input_cls)

    # Input attributes
    input_attrs: dict[str, Any] = {
        "type": "checkbox",
        "cls": all_input_cls,
        "name": name,
        "value": value,
        "id": cb_id,
    }

    if checked:
        input_attrs["checked"] = True
    if disabled:
        input_attrs["disabled"] = True
    if required:
        input_attrs["required"] = True

    input_attrs.update(convert_attrs(kwargs))

    # Build elements
    elements = [FTInput(**input_attrs)]

    if label:
        label_cls_final = merge_classes("form-check-label", label_cls)
        elements.append(Label(label, cls=label_cls_final, fr=cb_id))

    if help_text:
        elements.append(Div(help_text, cls="form-text"))

    return Div(*elements, cls=wrapper_cls)


@register(category="forms")
def Radio(
    name: str,
    *,
    label: str | None = None,
    value: str = "",
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    inline: bool = False,
    reverse: bool = False,
    radio_id: str | None = None,
    input_cls: str = "",
    label_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap Radio button component.

    A styled radio button form control. Group multiple radios with same name.

    Args:
        name: Input name attribute (same name groups radios together)
        label: Label text for the radio
        value: Value when selected
        checked: Whether radio is initially selected
        disabled: Disable the radio
        required: Mark as required field
        inline: Display inline with other radios
        reverse: Put radio on the right side of label
        radio_id: ID for the input (auto-generated if not provided)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with form-check structure

    Example:
        Radio group:
        >>> Radio("color", label="Red", value="red", checked=True)
        >>> Radio("color", label="Blue", value="blue")
        >>> Radio("color", label="Green", value="green")

        Inline radios:
        >>> Radio("size", label="Small", value="sm", inline=True)
        >>> Radio("size", label="Large", value="lg", inline=True)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/checks-radios/
    """
    r_id = radio_id or f"radio-{name}-{value}"

    # Wrapper classes
    wrapper_classes = ["form-check"]
    if inline:
        wrapper_classes.append("form-check-inline")
    if reverse:
        wrapper_classes.append("form-check-reverse")

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(wrapper_classes), user_cls)

    # Input classes
    all_input_cls = merge_classes("form-check-input", input_cls)

    # Input attributes
    input_attrs: dict[str, Any] = {
        "type": "radio",
        "cls": all_input_cls,
        "name": name,
        "value": value,
        "id": r_id,
    }

    if checked:
        input_attrs["checked"] = True
    if disabled:
        input_attrs["disabled"] = True
    if required:
        input_attrs["required"] = True

    input_attrs.update(convert_attrs(kwargs))

    # Build elements
    elements = [FTInput(**input_attrs)]

    if label:
        label_cls_final = merge_classes("form-check-label", label_cls)
        elements.append(Label(label, cls=label_cls_final, fr=r_id))

    return Div(*elements, cls=wrapper_cls)


@register(category="forms")
def Switch(
    name: str,
    *,
    label: str | None = None,
    value: str = "1",
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    reverse: bool = False,
    switch_id: str | None = None,
    input_cls: str = "",
    label_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap Switch (toggle) component.

    A toggle switch styled as an alternative to checkboxes.

    Args:
        name: Input name attribute
        label: Label text for the switch
        value: Value when checked (default: "1")
        checked: Whether switch is initially on
        disabled: Disable the switch
        required: Mark as required field
        reverse: Put switch on the right side of label
        switch_id: ID for the input (auto-generated from name if not provided)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with form-check form-switch structure

    Example:
        Basic switch:
        >>> Switch("notifications", label="Enable notifications")

        Pre-toggled:
        >>> Switch("darkmode", label="Dark mode", checked=True)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/checks-radios/#switches
    """
    sw_id = switch_id or f"switch-{name}"

    # Wrapper classes
    wrapper_classes = ["form-check", "form-switch"]
    if reverse:
        wrapper_classes.append("form-check-reverse")

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes(" ".join(wrapper_classes), user_cls)

    # Input classes
    all_input_cls = merge_classes("form-check-input", input_cls)

    # Input attributes - switches use role="switch"
    input_attrs: dict[str, Any] = {
        "type": "checkbox",
        "cls": all_input_cls,
        "name": name,
        "value": value,
        "id": sw_id,
        "role": "switch",
    }

    if checked:
        input_attrs["checked"] = True
    if disabled:
        input_attrs["disabled"] = True
    if required:
        input_attrs["required"] = True

    input_attrs.update(convert_attrs(kwargs))

    # Build elements
    elements = [FTInput(**input_attrs)]

    if label:
        label_cls_final = merge_classes("form-check-label", label_cls)
        elements.append(Label(label, cls=label_cls_final, fr=sw_id))

    return Div(*elements, cls=wrapper_cls)


@register(category="forms")
def Range(
    name: str,
    *,
    label: str | None = None,
    value: int | float | None = None,
    min_val: int | float = 0,
    max_val: int | float = 100,
    step: int | float | None = None,
    disabled: bool = False,
    range_id: str | None = None,
    input_cls: str = "",
    label_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap Range (slider) component.

    A styled range slider input control.

    Args:
        name: Input name attribute
        label: Label text for the range
        value: Initial value
        min_val: Minimum value (default: 0)
        max_val: Maximum value (default: 100)
        step: Step increment (default: 1)
        disabled: Disable the range
        range_id: ID for the input (auto-generated from name if not provided)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with form-range structure

    Example:
        Basic range:
        >>> Range("volume", label="Volume", value=50)

        With custom range:
        >>> Range("price", label="Price", min_val=10, max_val=500, step=10)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/range/
    """
    r_id = range_id or f"range-{name}"

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes("mb-3", user_cls)

    # Input classes
    all_input_cls = merge_classes("form-range", input_cls)

    # Input attributes
    input_attrs: dict[str, Any] = {
        "type": "range",
        "cls": all_input_cls,
        "name": name,
        "id": r_id,
        "min": str(min_val),
        "max": str(max_val),
    }

    if value is not None:
        input_attrs["value"] = str(value)
    if step is not None:
        input_attrs["step"] = str(step)
    if disabled:
        input_attrs["disabled"] = True

    input_attrs.update(convert_attrs(kwargs))

    # Build elements
    elements = []

    if label:
        label_cls_final = merge_classes("form-label", label_cls)
        elements.append(Label(label, cls=label_cls_final, fr=r_id))

    elements.append(FTInput(**input_attrs))

    return Div(*elements, cls=wrapper_cls)
