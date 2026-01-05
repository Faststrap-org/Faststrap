"""Bootstrap Placeholder (skeleton loading) components."""

from typing import Any, Literal

from fasthtml.common import Div, Span

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs

AnimationType = Literal["glow", "wave"]
SizeType = Literal["xs", "sm", "lg"]


@register(category="feedback")
def Placeholder(
    width: str | None = None,
    height: str | None = None,
    animation: AnimationType | None = None,
    variant: str | None = None,
    size: SizeType | None = None,
    **kwargs: Any,
) -> Span:
    """Bootstrap Placeholder for skeleton loading screens.

    Args:
        width: Placeholder width (CSS value, e.g., "100%", "200px")
        height: Placeholder height (CSS value)
        animation: Animation type (glow or wave)
        variant: Color variant (primary, secondary, etc.)
        size: Size variant (xs, sm, lg)
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Span element with placeholder classes

    Example:
        Basic placeholder:
        >>> Placeholder(width="100%")

        With animation:
        >>> Placeholder(width="75%", animation="glow")

        Colored placeholder:
        >>> Placeholder(width="50%", variant="primary")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/placeholders/
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "Placeholder",
        animation=animation,
        variant=variant,
        size=size,
    )

    c_animation = cfg.get("animation")
    c_variant = cfg.get("variant")
    c_size = cfg.get("size")

    # Build classes
    classes = ["placeholder"]

    if c_variant:
        classes.append(f"bg-{c_variant}")

    if c_size:
        classes.append(f"placeholder-{c_size}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}

    # Style for dimensions
    style_parts = []
    if width:
        style_parts.append(f"width: {width}")
    if height:
        style_parts.append(f"height: {height}")

    if style_parts:
        existing_style = kwargs.pop("style", "")
        if isinstance(existing_style, dict):
            # Merge with existing style dict
            if width:
                existing_style["width"] = width
            if height:
                existing_style["height"] = height
            attrs["style"] = existing_style
        else:
            # String style
            combined_style = "; ".join(style_parts)
            if existing_style:
                combined_style = f"{existing_style}; {combined_style}"
            attrs["style"] = combined_style

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    # Wrap in animation container if needed
    if c_animation:
        return Span(Span(**attrs), cls=f"placeholder-{c_animation}")

    return Span(**attrs)


@register(category="feedback")
def PlaceholderCard(
    show_image: bool = True,
    show_title: bool = True,
    show_text: bool = True,
    animation: AnimationType | None = None,
    **kwargs: Any,
) -> Div:
    """Pre-built Card skeleton placeholder.

    Args:
        show_image: Show image placeholder at top
        show_title: Show title placeholder
        show_text: Show text placeholders
        animation: Animation type (glow or wave)
        **kwargs: Additional HTML attributes for card

    Returns:
        FastHTML Div element with card skeleton

    Example:
        Full card skeleton:
        >>> PlaceholderCard(animation="glow")

        Title and text only:
        >>> PlaceholderCard(show_image=False, animation="wave")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/placeholders/
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "PlaceholderCard",
        animation=animation,
    )

    c_animation = cfg.get("animation")

    # Build card structure
    card_parts = []

    # Image placeholder
    if show_image:
        card_parts.append(
            Placeholder(width="100%", height="180px", animation=c_animation, cls="card-img-top")
        )

    # Card body
    body_parts = []

    if show_title:
        body_parts.append(
            Placeholder(width="75%", height="1.5rem", animation=c_animation, cls="mb-2")
        )

    if show_text:
        body_parts.extend(
            [
                Placeholder(width="100%", height="1rem", animation=c_animation, cls="mb-2"),
                Placeholder(width="100%", height="1rem", animation=c_animation, cls="mb-2"),
                Placeholder(width="60%", height="1rem", animation=c_animation),
            ]
        )

    if body_parts:
        card_parts.append(Div(*body_parts, cls="card-body"))

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("card", user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(*card_parts, **attrs)


@register(category="feedback")
def PlaceholderButton(
    width: str = "100px",
    animation: AnimationType | None = None,
    variant: str = "primary",
    **kwargs: Any,
) -> Span:
    """Button-shaped placeholder.

    Args:
        width: Button width
        animation: Animation type (glow or wave)
        variant: Button color variant
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Span element styled as button placeholder

    Example:
        >>> PlaceholderButton(width="120px", animation="glow")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/placeholders/
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "PlaceholderButton",
        animation=animation,
    )

    c_animation = cfg.get("animation")

    # Build classes
    classes = ["placeholder", f"btn-{variant}"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes, "style": {"width": width}}

    attrs.update(convert_attrs(kwargs))

    # Wrap in animation if needed
    if c_animation:
        return Span(Span(**attrs), cls=f"placeholder-{c_animation}")

    return Span(**attrs)
