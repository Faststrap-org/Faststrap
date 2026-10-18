"""Bootstrap Card component with header, body, footer support."""

from typing import Any, Literal

from fasthtml.common import H5, Div, Img

from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs


@register(category="display")
@stable
def Card(
    *children: Any,
    title: str | None = None,
    subtitle: str | None = None,
    header: Any | None = None,
    footer: Any | None = None,
    img_top: str | None = None,
    img_bottom: str | None = None,
    img_overlay: bool = False,
    img_alt: str | None = "",
    img_loading: Literal["lazy", "eager"] | None = None,
    img_width: str | int | None = None,
    img_height: str | int | None = None,
    img_cls: str | None = None,
    img_attrs: dict[str, Any] | None = None,
    header_cls: str | None = UNSET,
    body_cls: str | None = UNSET,
    footer_cls: str | None = UNSET,
    title_cls: str | None = None,
    subtitle_cls: str | None = None,
    text_cls: str | None = None,
    header_attrs: dict[str, Any] | None = None,
    body_attrs: dict[str, Any] | None = None,
    footer_attrs: dict[str, Any] | None = None,
    title_attrs: dict[str, Any] | None = None,
    subtitle_attrs: dict[str, Any] | None = None,
    text_attrs: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Card component for flexible content containers.

    Args:
        *children: Card body content
        title: Card title (styled with card-title)
        subtitle: Card subtitle (styled with card-subtitle)
        header: Card header content (separate section above body)
        footer: Card footer content (separate section below body)
        img_top: Image URL for top of card
        img_bottom: Image URL for bottom of card
        img_overlay: Use image as background with overlay text
        img_alt: Alternative text shared by card images. Leave empty for
            decorative images.
        img_loading: Native image loading mode, ``"lazy"`` or ``"eager"``.
        img_width: Optional image width attribute.
        img_height: Optional image height attribute.
        img_cls: Extra classes applied to card images.
        img_attrs: Extra HTML attributes applied to card images.
        header_attrs: Extra attributes for the header wrapper
        body_attrs: Extra attributes for the body wrapper
        footer_attrs: Extra attributes for the footer wrapper
        title_attrs: Extra attributes for the title element
        subtitle_attrs: Extra attributes for the subtitle element
        text_attrs: Extra attributes for the text wrapper
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with card structure

    Examples:
        Basic card:
        >>> Card("Card content", title="Card Title")

        With header and footer:
        >>> Card(
        ...     "Main content",
        ...     title="Title",
        ...     header="Featured",
        ...     footer="Last updated 3 mins ago"
        ... )
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "Card",
        header_cls=header_cls,
        body_cls=body_cls,
        footer_cls=footer_cls,
    )

    c_title = title
    c_subtitle = subtitle
    c_header = header
    c_footer = footer
    c_img_top = img_top
    c_img_bottom = img_bottom
    c_img_overlay = img_overlay
    image_attrs: dict[str, Any] = {
        "alt": img_alt or "",
        "cls": img_cls or "",
    }
    if img_loading is not None:
        image_attrs["loading"] = img_loading
    if img_width is not None:
        image_attrs["width"] = img_width
    if img_height is not None:
        image_attrs["height"] = img_height
    image_attrs.update(dict(img_attrs or {}))

    def card_image(src: str, default_cls: str) -> Img:
        attrs = dict(image_attrs)
        attrs["cls"] = merge_classes(default_cls, attrs.pop("cls", ""))
        return Img(src=src, **attrs)

    # CSS classes (fallback to empty string if None)
    c_header_cls = cfg.get("header_cls") or ""
    c_body_cls = cfg.get("body_cls") or ""
    c_footer_cls = cfg.get("footer_cls") or ""
    c_title_cls = title_cls or ""
    c_subtitle_cls = subtitle_cls or ""
    c_text_cls = text_cls or ""
    c_header_attrs = convert_attrs(dict(header_attrs or {}))
    c_body_attrs = convert_attrs(dict(body_attrs or {}))
    c_footer_attrs = convert_attrs(dict(footer_attrs or {}))
    c_title_attrs = convert_attrs(dict(title_attrs or {}))
    c_subtitle_attrs = convert_attrs(dict(subtitle_attrs or {}))
    c_text_attrs = convert_attrs(dict(text_attrs or {}))

    # Build base classes
    classes = ["card"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    # Build card structure
    parts = []

    # Add header if provided
    if c_header:
        parts.append(
            Div(
                c_header,
                cls=merge_classes("card-header", c_header_cls, c_header_attrs.pop("cls", "")),
                **c_header_attrs,
            )
        )

    # Add top image
    if c_img_top and not c_img_overlay:
        parts.append(card_image(c_img_top, "card-img-top"))

    # Build body content
    body_content = []

    # Add image for overlay mode
    if c_img_overlay and c_img_top:
        parts.append(card_image(c_img_top, "card-img"))
        actual_body_cls = "card-img-overlay"
    else:
        actual_body_cls = "card-body"

    # Add title
    if c_title:
        body_content.append(
            H5(
                c_title,
                cls=merge_classes("card-title", c_title_cls, c_title_attrs.pop("cls", "")),
                **c_title_attrs,
            )
        )

    # Add subtitle
    if c_subtitle:
        body_content.append(
            Div(
                c_subtitle,
                cls=merge_classes(
                    "card-subtitle mb-2 text-muted",
                    c_subtitle_cls,
                    c_subtitle_attrs.pop("cls", ""),
                ),
                **c_subtitle_attrs,
            )
        )

    # Add main content
    if children:
        # If there's a title/subtitle, wrap content in P for better semantics
        if c_title or c_subtitle:
            body_content.append(
                Div(
                    *children,
                    cls=merge_classes("card-text", c_text_cls, c_text_attrs.pop("cls", "")),
                    **c_text_attrs,
                )
            )
        else:
            body_content.extend(children)

    # Add body
    if body_content:
        parts.append(
            Div(
                *body_content,
                cls=merge_classes(actual_body_cls, c_body_cls, c_body_attrs.pop("cls", "")),
                **c_body_attrs,
            )
        )

    # Add bottom image
    if c_img_bottom and not c_img_overlay:
        parts.append(card_image(c_img_bottom, "card-img-bottom"))

    # Add footer
    if c_footer:
        parts.append(
            Div(
                c_footer,
                cls=merge_classes(
                    "card-footer text-muted",
                    c_footer_cls,
                    c_footer_attrs.pop("cls", ""),
                ),
                **c_footer_attrs,
            )
        )

    return Div(*parts, **attrs)
