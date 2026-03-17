"""Bootstrap ButtonGroup component for grouping buttons."""

from typing import Any, Literal

from fasthtml.common import Div

from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

SizeType = Literal["sm", "lg"]


@register(category="forms")
def ButtonGroup(
    *buttons: Any,
    size: SizeType | None = None,
    vertical: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap ButtonGroup for grouping related buttons together.

    Args:
        *buttons: Button components or elements
        size: Button group size (sm, lg)
        vertical: Stack buttons vertically
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with button group

    Example:
        Basic group:
        >>> ButtonGroup(
        ...     Button("Left", variant="primary"),
        ...     Button("Middle", variant="primary"),
        ...     Button("Right", variant="primary")
        ... )

        Vertical group:
        >>> ButtonGroup(
        ...     Button("Top"),
        ...     Button("Middle"),
        ...     Button("Bottom"),
        ...     vertical=True
        ... )

        Small group:
        >>> ButtonGroup(
        ...     Button("One"),
        ...     Button("Two"),
        ...     Button("Three"),
        ...     size="sm"
        ... )

        With toggle buttons (radio-style):
        >>> ButtonGroup(
        ...     Button("Option 1", data_bs_toggle="button"),
        ...     Button("Option 2", data_bs_toggle="button"),
        ...     Button("Option 3", data_bs_toggle="button")
        ... )

    Note:
        Button groups merge adjacent buttons and remove rounded corners
        on inner buttons for a seamless look.

        For toolbar-style layouts, wrap multiple button groups:
        >>> Div(
        ...     ButtonGroup(Button("1"), Button("2")),
        ...     ButtonGroup(Button("3"), Button("4")),
        ...     cls="btn-toolbar"
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/button-group/
    """
    # Build classes
    classes = ["btn-group-vertical" if vertical else "btn-group"]

    # Add size class
    if size:
        classes.append(f"btn-group-{size}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "role": "group",
    }

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    return Div(*buttons, **attrs)


@register(category="forms")
def ButtonToolbar(
    *groups: Any,
    **kwargs: Any,
) -> Div:
    """Bootstrap ButtonToolbar for grouping multiple button groups.

    Args:
        *groups: ButtonGroup components or other toolbar items
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with button toolbar

    Example:
        >>> ButtonToolbar(
        ...     ButtonGroup(
        ...         Button("1"), Button("2"), Button("3")
        ...     ),
        ...     ButtonGroup(
        ...         Button("4"), Button("5")
        ...     ),
        ...     ButtonGroup(
        ...         Button("6")
        ...     )
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/button-group/#button-toolbar
    """
    # Build classes
    classes = ["btn-toolbar"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "role": "toolbar",
    }

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    return Div(*groups, **attrs)
