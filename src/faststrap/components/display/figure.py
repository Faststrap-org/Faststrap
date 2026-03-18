"""Bootstrap Figure component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Figcaption, Img
from fasthtml.common import Figure as FTFigure

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="display")
@stable
def Figure(
    src: str,
    caption: str | Any | None = None,
    alt: str = "",
    size: str | None = None,
    align: str | None = None,
    fluid: bool = True,
    rounded: bool = True,
    thumbnail: bool = False,
    img_cls: str = "",
    caption_cls: str = "",
    **kwargs: Any,
) -> FTFigure:
    """Bootstrap Figure component.

    Displays an image with an optional caption.

    Args:
        src: Image source URL
        caption: Caption text or component (optional)
        alt: Image alternative text
        size: Width of the figure (e.g. "25%", "50%") - adds w-* class if matches standard sizes, else style
        align: Caption alignment ("start", "center", "end")
        fluid: Make image responsive (img-fluid)
        rounded: Add rounded corners
        thumbnail: Style image as thumbnail
        img_cls: Additional classes for image
        caption_cls: Additional classes for caption
        **kwargs: Additional HTML attributes for the figure element

    Returns:
        FastHTML Figure element

    Example:
        >>> Figure("image.jpg", caption="A nice view")

        >>> Figure("avatar.png", size="50%", rounded=True, align="center")
    """
    user_cls = kwargs.pop("cls", "")
    figure_cls = merge_classes("figure", user_cls)

    # Image classes
    img_classes = ["figure-img"]
    if fluid:
        img_classes.append("img-fluid")
    if rounded:
        img_classes.append("rounded")
    if thumbnail:
        img_classes.append("img-thumbnail")

    all_img_cls = merge_classes(" ".join(img_classes), img_cls)

    # Caption alignment
    cap_classes = ["figure-caption"]
    if align:
        # map 'start', 'center', 'end' to text-*
        if align in ("start", "center", "end"):
            cap_classes.append(f"text-{align}")
        else:
            # Maybe standard 'text-right' etc?
            cap_classes.append(f"text-{align}")

    all_cap_cls = merge_classes(" ".join(cap_classes), caption_cls)

    # Figure attributes
    attrs: dict[str, Any] = {"cls": figure_cls}

    # Handle size on figure or image? Bootstrap usually puts explicit width on image?
    # Actually, figure usually fits content.
    # If size is standard w-25, w-50, w-75, w-100, add to figure class?
    # Or style?
    if size:
        if size in ("25", "50", "75", "100", "25%", "50%", "75%", "100%"):
            sanitized = size.replace("%", "")
            attrs["cls"] += f" w-{sanitized}"
        else:
            style = kwargs.get("style", {})
            if isinstance(style, dict):
                style["width"] = size
                kwargs["style"] = style
            elif isinstance(style, str):
                kwargs["style"] = f"{style}; width: {size}"
            else:
                attrs["style"] = f"width: {size}"

    attrs.update(convert_attrs(kwargs))

    # Content
    content = [Img(src=src, alt=alt, cls=all_img_cls)]

    if caption:
        content.append(Figcaption(caption, cls=all_cap_cls))

    return FTFigure(*content, **attrs)
