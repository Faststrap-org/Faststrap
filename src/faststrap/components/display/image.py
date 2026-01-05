"""Bootstrap Image component with responsive utilities."""

from typing import Any, Literal

from fasthtml.common import Img

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs

AlignType = Literal["start", "center", "end"]


@register(category="display")
def Image(
    src: str,
    alt: str | None = None,
    fluid: bool | None = None,
    thumbnail: bool | None = None,
    rounded: bool | None = None,
    rounded_circle: bool | None = None,
    align: AlignType | None = None,
    width: str | int | None = None,
    height: str | int | None = None,
    loading: Literal["lazy", "eager"] | None = None,
    **kwargs: Any,
) -> Img:
    """Bootstrap Image component with responsive utilities.

    Args:
        src: Image source URL (required)
        alt: Alternative text for accessibility
        fluid: Make image responsive (max-width: 100%, height: auto)
        thumbnail: Add thumbnail styling (border, padding, rounded)
        rounded: Add rounded corners
        rounded_circle: Make image circular
        align: Float alignment (start=left, end=right, center)
        width: Image width (CSS value or pixels)
        height: Image height (CSS value or pixels)
        loading: Native lazy loading (lazy or eager)
        **kwargs: Additional HTML attributes (cls, id, style, etc.)

    Returns:
        FastHTML Img element with Bootstrap image classes

    Example:
        Basic responsive image:
        >>> Image(src="photo.jpg", alt="Photo", fluid=True)

        Thumbnail with rounded corners:
        >>> Image(src="avatar.jpg", alt="Avatar", thumbnail=True, rounded_circle=True)

        Aligned image:
        >>> Image(src="logo.png", alt="Logo", align="center")

        Lazy loading:
        >>> Image(src="large.jpg", alt="Large image", fluid=True, loading="lazy")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/content/images/
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "Image",
        fluid=fluid,
        thumbnail=thumbnail,
        rounded=rounded,
        rounded_circle=rounded_circle,
        align=align,
        loading=loading,
    )

    c_fluid = cfg.get("fluid", False)
    c_thumbnail = cfg.get("thumbnail", False)
    c_rounded = cfg.get("rounded", False)
    c_rounded_circle = cfg.get("rounded_circle", False)
    c_align = cfg.get("align")
    c_loading = cfg.get("loading")

    # Build classes
    classes = []

    if c_fluid:
        classes.append("img-fluid")

    if c_thumbnail:
        classes.append("img-thumbnail")

    if c_rounded:
        classes.append("rounded")

    if c_rounded_circle:
        classes.append("rounded-circle")

    # Alignment (float classes)
    if c_align:
        if c_align == "start":
            classes.append("float-start")
        elif c_align == "end":
            classes.append("float-end")
        elif c_align == "center":
            # Center requires mx-auto and d-block
            classes.extend(["d-block", "mx-auto"])

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "src": src,
        "cls": all_classes,
    }

    # Alt text (important for accessibility)
    if alt:
        attrs["alt"] = alt

    # Dimensions
    if width:
        attrs["width"] = width if isinstance(width, str) else f"{width}px"
    if height:
        attrs["height"] = height if isinstance(height, str) else f"{height}px"

    # Lazy loading
    if c_loading:
        attrs["loading"] = c_loading

    # Convert remaining kwargs
    attrs.update(convert_attrs(kwargs))

    return Img(**attrs)
