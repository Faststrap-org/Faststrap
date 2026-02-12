"""Form Group Component with Validation.

Wraps input + label + help text + validation feedback in one component.
"""

from typing import Any

from fasthtml.common import Div, Label, Small

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs


def FormGroup(
    input_element: Any,
    label: str | None = None,
    help_text: str | None = None,
    error: str | None = None,
    success: str | None = None,
    is_invalid: bool = False,
    is_valid: bool = False,
    required: bool = False,
    **kwargs: Any,
) -> Div:
    """Form group with label, input, help text, and validation feedback.

    Wraps Bootstrap form controls with proper structure and validation states.
    Eliminates boilerplate for form field creation.

    Args:
        input_element: Input, Select, or Textarea component
        label: Label text (optional)
        help_text: Help text shown below input
        error: Error message (shown when is_invalid=True)
        success: Success message (shown when is_valid=True)
        is_invalid: Whether to show invalid state
        is_valid: Whether to show valid state
        required: Whether field is required (adds asterisk to label)
        **kwargs: Additional HTML attributes for the container

    Returns:
        Div containing label, input, and feedback

    Example:
        Basic form group:
        >>> FormGroup(
        ...     Input(name="email", type="email"),
        ...     label="Email Address",
        ...     help_text="We'll never share your email"
        ... )

        With validation error:
        >>> FormGroup(
        ...     Input(name="password", type="password"),
        ...     label="Password",
        ...     error="Password must be at least 8 characters",
        ...     is_invalid=True
        ... )

        With success state:
        >>> FormGroup(
        ...     Input(name="username", value="john_doe"),
        ...     label="Username",
        ...     success="Username is available!",
        ...     is_valid=True
        ... )

        Required field:
        >>> FormGroup(
        ...     Input(name="name"),
        ...     label="Full Name",
        ...     required=True
        ... )

    Note:
        The input_element should be a FastHTML Input, Select, or Textarea.
        Validation classes (is-invalid, is-valid) are automatically added
        to the input element based on is_invalid/is_valid flags.
    """
    # Build label
    label_element = None
    if label:
        label_text: Any = label
        if required:
            from fasthtml.common import Span

            label_text = (label, Span(" *", cls="text-danger"))

        label_element = Label(
            label_text,
            cls="form-label",
        )

    # Add validation classes to input
    if hasattr(input_element, "attrs"):
        input_cls = input_element.attrs.get("cls", "")
        if is_invalid:
            input_cls = merge_classes(input_cls, "is-invalid")
        elif is_valid:
            input_cls = merge_classes(input_cls, "is-valid")
        input_element.attrs["cls"] = input_cls

    # Build help text
    help_element = None
    if help_text and not (is_invalid or is_valid):
        help_element = Small(help_text, cls="form-text text-muted")

    # Build validation feedback
    feedback_element = None
    if is_invalid and error:
        feedback_element = Div(error, cls="invalid-feedback d-block")
    elif is_valid and success:
        feedback_element = Div(success, cls="valid-feedback d-block")

    # Build container
    base_classes = ["mb-3"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Assemble form group
    elements = []
    if label_element:
        elements.append(label_element)
    elements.append(input_element)
    if help_element:
        elements.append(help_element)
    if feedback_element:
        elements.append(feedback_element)

    return Div(*elements, **attrs)
