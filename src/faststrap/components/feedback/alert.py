"""Bootstrap Alert component for contextual feedback messages."""

from typing import Any, Literal

from fasthtml.common import Button, Div, Span

from ...core.base import merge_classes

VariantType = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
]


def _convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert Python kwargs to HTML attributes (hx_get → hx-get)."""
    converted = {}
    for k, v in kwargs.items():
        if k.startswith("hx_") or k.startswith("data_") or k.startswith("aria_"):
            converted[k.replace("_", "-")] = v
        elif k == "cls":
            converted[k] = v
        else:
            converted[k.replace("_", "-")] = v
    return converted


def Alert(
    *children: Any,
    variant: VariantType = "primary",
    dismissible: bool = False,
    heading: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Alert component for contextual feedback messages.

    Args:
        *children: Alert content
        variant: Bootstrap color variant
        dismissible: Add close button to dismiss alert
        heading: Optional heading text (styled with alert-heading)
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with alert classes

    Example:
        Basic usage:
        >>> Alert("Operation successful!", variant="success")

        With heading:
        >>> Alert(
        ...     "Check your inbox for confirmation.",
        ...     variant="info",
        ...     heading="Email Sent"
        ... )

        Dismissible:
        >>> Alert(
        ...     "This alert can be closed.",
        ...     variant="warning",
        ...     dismissible=True
        ... )

        With HTMX:
        >>> Alert(
        ...     "Loading...",
        ...     variant="info",
        ...     hx_get="/status",
        ...     hx_trigger="load"
        ... )

    Note:
        Dismissible alerts require Bootstrap's JavaScript.
        The alert will fade out when the close button is clicked.

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/alerts/
    """
    # Build base classes
    classes = ["alert", f"alert-{variant}"]

    # Add dismissible class if needed
    if dismissible:
        classes.append("alert-dismissible fade show")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes, "role": "alert"}

    # Convert remaining kwargs
    attrs.update(_convert_attrs(kwargs))

    # Build content
    content = []

    # Add heading if provided
    if heading:
        content.append(Div(heading, cls="alert-heading h4"))

    # Add main content
    content.extend(children)

    # Add close button if dismissible
    if dismissible:
        close_btn = Button(
            Span("×", aria_hidden="true"),
            type="button",
            cls="btn-close",
            data_bs_dismiss="alert",
            aria_label="Close",
        )
        content.append(close_btn)

    return Div(*content, **attrs)
