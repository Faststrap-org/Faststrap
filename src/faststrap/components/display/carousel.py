"""Bootstrap Carousel component for image/content sliders."""

from typing import Any
from uuid import uuid4

from fasthtml.common import Button, Div, Span

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import resolve_defaults
from ...utils.attrs import convert_attrs


@register(category="display", requires_js=True)
def Carousel(
    *items: Any,
    carousel_id: str | None = None,
    controls: bool | None = None,
    indicators: bool | None = None,
    interval: int | None = None,
    keyboard: bool | None = None,
    pause: bool | str | None = None,
    ride: bool | str | None = None,
    wrap: bool | None = None,
    fade: bool | None = None,
    dark: bool | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Carousel for image/content sliders.

    Args:
        *items: CarouselItem components
        carousel_id: Unique ID for carousel (auto-generated if not provided)
        controls: Show previous/next controls
        indicators: Show slide indicators
        interval: Auto-play interval in milliseconds (5000 = 5s, False = no auto-play)
        keyboard: Enable keyboard navigation
        pause: Pause on hover ("hover" or False)
        ride: Auto-start carousel ("carousel" or False)
        wrap: Enable continuous loop
        fade: Use fade transition instead of slide
        dark: Use dark variant for controls/indicators
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with carousel structure

    Example:
        Basic carousel:
        >>> Carousel(
        ...     CarouselItem(Img(src="1.jpg"), caption="First slide"),
        ...     CarouselItem(Img(src="2.jpg"), caption="Second slide"),
        ...     controls=True,
        ...     indicators=True
        ... )

        Auto-playing carousel:
        >>> Carousel(
        ...     CarouselItem(Img(src="1.jpg")),
        ...     CarouselItem(Img(src="2.jpg")),
        ...     interval=3000,  # 3 seconds
        ...     ride="carousel"
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/carousel/
    """
    # Resolve defaults
    cfg = resolve_defaults(
        "Carousel",
        controls=controls,
        indicators=indicators,
        interval=interval,
        keyboard=keyboard,
        pause=pause,
        ride=ride,
        wrap=wrap,
        fade=fade,
        dark=dark,
    )

    c_controls = cfg.get("controls", False)
    c_indicators = cfg.get("indicators", False)
    c_interval = cfg.get("interval", 5000)
    c_keyboard = cfg.get("keyboard", True)
    c_pause = cfg.get("pause", "hover")
    c_ride = cfg.get("ride", False)
    c_wrap = cfg.get("wrap", True)
    c_fade = cfg.get("fade", False)
    c_dark = cfg.get("dark", False)

    # Generate ID if not provided
    if carousel_id is None:
        carousel_id = f"carousel-{uuid4().hex[:8]}"

    # Build classes
    classes = ["carousel", "slide"]

    if c_fade:
        classes.append("carousel-fade")

    if c_dark:
        classes.append("carousel-dark")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build data attributes for Bootstrap carousel
    data_attrs: dict[str, Any] = {
        "data_bs_ride": c_ride if c_ride else None,
    }

    if c_interval is not False:
        data_attrs["data_bs_interval"] = str(c_interval)
    else:
        data_attrs["data_bs_interval"] = "false"

    if not c_keyboard:
        data_attrs["data_bs_keyboard"] = "false"

    if c_pause is False:
        data_attrs["data_bs_pause"] = "false"
    elif c_pause:
        data_attrs["data_bs_pause"] = c_pause

    if not c_wrap:
        data_attrs["data_bs_wrap"] = "false"

    # Filter None values
    data_attrs = {k: v for k, v in data_attrs.items() if v is not None}

    # Build carousel parts
    carousel_parts = []

    # Indicators
    if c_indicators:
        indicators_list = [
            Button(
                type="button",
                data_bs_target=f"#{carousel_id}",
                data_bs_slide_to=str(i),
                cls="active" if i == 0 else "",
                aria_current="true" if i == 0 else None,
                aria_label=f"Slide {i + 1}",
            )
            for i in range(len(items))
        ]
        carousel_parts.append(Div(*indicators_list, cls="carousel-indicators"))

    # Inner (slides)
    carousel_parts.append(Div(*items, cls="carousel-inner"))

    # Controls
    if c_controls:
        # Previous button
        carousel_parts.append(
            Button(
                Span(cls="carousel-control-prev-icon", aria_hidden="true"),
                Span("Previous", cls="visually-hidden"),
                cls="carousel-control-prev",
                type="button",
                data_bs_target=f"#{carousel_id}",
                data_bs_slide="prev",
            )
        )

        # Next button
        carousel_parts.append(
            Button(
                Span(cls="carousel-control-next-icon", aria_hidden="true"),
                Span("Next", cls="visually-hidden"),
                cls="carousel-control-next",
                type="button",
                data_bs_target=f"#{carousel_id}",
                data_bs_slide="next",
            )
        )

    # Build final attributes
    attrs: dict[str, Any] = {
        "id": carousel_id,
        "cls": all_classes,
    }
    attrs.update(data_attrs)
    attrs.update(convert_attrs(kwargs))

    return Div(*carousel_parts, **attrs)


def CarouselItem(
    *content: Any,
    caption: str | None = None,
    caption_title: str | None = None,
    active: bool = False,
    interval: int | None = None,
    **kwargs: Any,
) -> Div:
    """Individual carousel slide item.

    Args:
        *content: Slide content (typically an Img element)
        caption: Caption text below image
        caption_title: Caption title (shown above caption text)
        active: Mark as active slide (first slide should be active)
        interval: Override carousel interval for this slide
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element with carousel-item structure

    Example:
        Image with caption:
        >>> CarouselItem(
        ...     Img(src="slide1.jpg", cls="d-block w-100"),
        ...     caption_title="First Slide",
        ...     caption="This is the first slide",
        ...     active=True
        ... )

        Custom interval:
        >>> CarouselItem(
        ...     Img(src="slide2.jpg", cls="d-block w-100"),
        ...     interval=10000  # Show for 10 seconds
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/carousel/
    """
    # Build classes
    classes = ["carousel-item"]

    if active:
        classes.append("active")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build item parts
    item_parts = list(content)

    # Add caption if provided
    if caption or caption_title:
        caption_parts = []
        if caption_title:
            caption_parts.append(Div(caption_title, cls="h5"))
        if caption:
            caption_parts.append(Div(caption, cls="p"))

        item_parts.append(Div(*caption_parts, cls="carousel-caption d-none d-md-block"))

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}

    if interval is not None:
        attrs["data_bs_interval"] = str(interval)

    attrs.update(convert_attrs(kwargs))

    return Div(*item_parts, **attrs)
