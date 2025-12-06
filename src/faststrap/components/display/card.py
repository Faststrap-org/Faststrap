"""Bootstrap Card component with header, body, footer support."""

from typing import Any

from fasthtml.common import Div, H5, Img

from ...core.base import merge_classes


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


def Card(
    *children: Any,
    title: str | None = None,
    subtitle: str | None = None,
    header: Any | None = None,
    footer: Any | None = None,
    img_top: str | None = None,
    img_bottom: str | None = None,
    img_overlay: bool = False,
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
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with card structure

    Example:
        Basic card:
        >>> Card("Card content", title="Card Title")

        With header and footer:
        >>> Card(
        ...     "Main content",
        ...     title="Title",
        ...     header="Featured",
        ...     footer="Last updated 3 mins ago"
        ... )

        With image:
        >>> Card(
        ...     "Beautiful landscape description",
        ...     title="Mountain View",
        ...     img_top="mountain.jpg"
        ... )

        Image overlay:
        >>> Card(
        ...     "Overlay text",
        ...     title="Title on Image",
        ...     img_top="bg.jpg",
        ...     img_overlay=True
        ... )

        With HTMX:
        >>> Card(
        ...     "Click to load more",
        ...     title="Dynamic Card",
        ...     hx_get="/more",
        ...     hx_trigger="click"
        ... )

    Note:
        Cards are flexible containers with minimal required markup.
        Use the grid system for layouts with multiple cards.

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/card/
    """
    # Build base classes
    classes = ["card"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    # Build card structure
    parts = []

    # Add header if provided
    if header:
        parts.append(Div(header, cls="card-header"))

    # Add top image
    if img_top and not img_overlay:
        parts.append(Img(src=img_top, cls="card-img-top", alt=""))

    # Build body content
    body_content = []

    # Add image for overlay mode
    if img_overlay and img_top:
        parts.append(Img(src=img_top, cls="card-img", alt=""))
        body_cls = "card-img-overlay"
    else:
        body_cls = "card-body"

    # Add title
    if title:
        body_content.append(H5(title, cls="card-title"))

    # Add subtitle
    if subtitle:
        body_content.append(Div(subtitle, cls="card-subtitle mb-2 text-muted"))

    # Add main content
    if children:
        # If there's a title/subtitle, wrap content in P for better semantics
        if title or subtitle:
            body_content.append(Div(*children, cls="card-text"))
        else:
            body_content.extend(children)

    # Add body
    if body_content:
        parts.append(Div(*body_content, cls=body_cls))

    # Add bottom image
    if img_bottom and not img_overlay:
        parts.append(Img(src=img_bottom, cls="card-img-bottom", alt=""))

    # Add footer
    if footer:
        parts.append(Div(footer, cls="card-footer text-muted"))

    return Div(*parts, **attrs)
