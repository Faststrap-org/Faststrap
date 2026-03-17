"""Bootstrap InputGroup and FloatingLabel components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Label, Span
from fasthtml.common import Input as FTInput

from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import SizeType
from ...utils.attrs import convert_attrs


@register(category="forms")
def InputGroup(
    *children: Any,
    size: SizeType | None = None,
    nowrap: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap InputGroup component.

    Extend form controls with text, buttons, or other elements.

    Args:
        *children: Form controls and addons (InputGroupText, Button, Input, etc.)
        size: Group size (sm, lg)
        nowrap: Prevent wrapping on smaller screens
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with input-group structure

    Example:
        With text addon:
        >>> InputGroup(
        ...     InputGroupText("@"),
        ...     Input("username", placeholder="Username"),
        ... )

        With button:
        >>> InputGroup(
        ...     Input("search", placeholder="Search..."),
        ...     Button("Go", variant="primary"),
        ... )

        Large size:
        >>> InputGroup(
        ...     InputGroupText("$"),
        ...     Input("amount", input_type="number"),
        ...     InputGroupText(".00"),
        ...     size="lg"
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/input-group/
    """
    # Build classes
    classes = ["input-group"]

    if size:
        classes.append(f"input-group-{size}")

    if nowrap:
        classes.append("flex-nowrap")

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)


@register(category="forms")
def InputGroupText(
    *children: Any,
    **kwargs: Any,
) -> Span:
    """Bootstrap InputGroup Text addon.

    Text or icon addon for InputGroup.

    Args:
        *children: Text or icon content
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Span element with input-group-text class

    Example:
        >>> InputGroupText("@")
        >>> InputGroupText("$")
        >>> InputGroupText(Icon("search"))
    """
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("input-group-text", user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Span(*children, **attrs)


@register(category="forms")
def FloatingLabel(
    name: str,
    *,
    label: str,
    input_type: Literal[
        "text",
        "password",
        "email",
        "number",
        "url",
        "tel",
        "search",
        "date",
        "time",
        "datetime-local",
    ] = "text",
    value: str = "",
    placeholder: str = "",
    disabled: bool = False,
    readonly: bool = False,
    required: bool = False,
    input_id: str | None = None,
    input_cls: str = "",
    label_cls: str = "",
    **kwargs: Any,
) -> Div:
    """Bootstrap FloatingLabel input component.

    An input with an animated floating label that moves when focused.

    Args:
        name: Input name attribute
        label: Label text (required for floating labels)
        input_type: HTML input type
        value: Initial value
        placeholder: Placeholder text (usually same as label)
        disabled: Disable the input
        readonly: Make input read-only
        required: Mark as required field
        input_id: ID for the input (auto-generated from name if not provided)
        input_cls: Additional classes for input element
        label_cls: Additional classes for label element
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with form-floating structure

    Example:
        Basic:
        >>> FloatingLabel("email", label="Email address", input_type="email")

        With value:
        >>> FloatingLabel("name", label="Your name", value="John Doe")

        Password:
        >>> FloatingLabel("password", label="Password", input_type="password", required=True)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/floating-labels/
    """
    fl_id = input_id or f"floating-{name}"

    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes("form-floating", user_cls)

    # Input classes and attributes
    all_input_cls = merge_classes("form-control", input_cls)

    input_attrs: dict[str, Any] = {
        "type": input_type,
        "cls": all_input_cls,
        "name": name,
        "id": fl_id,
        "placeholder": placeholder or label,  # Placeholder required for floating effect
    }

    if value:
        input_attrs["value"] = value
    if disabled:
        input_attrs["disabled"] = True
    if readonly:
        input_attrs["readonly"] = True
    if required:
        input_attrs["required"] = True

    input_attrs.update(convert_attrs(kwargs))

    # Label
    label_cls_final = merge_classes("", label_cls) if label_cls else None

    label_attrs: dict[str, Any] = {"fr": fl_id}
    if label_cls_final:
        label_attrs["cls"] = label_cls_final

    return Div(
        FTInput(**input_attrs),
        Label(label, **label_attrs),
        cls=wrapper_cls,
    )
