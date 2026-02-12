"""Testimonial Pattern Components.

Customer testimonial cards and sections for social proof.
"""

from typing import Any

from fasthtml.common import Blockquote, Div, Img, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...utils.attrs import convert_attrs
from ..display.card import Card


@beta
def Testimonial(
    quote: str,
    author: str,
    role: str | None = None,
    avatar: str | None = None,
    rating: int | None = None,
    **kwargs: Any,
) -> Any:
    """Single testimonial card with quote, author, and optional avatar/rating.

    Args:
        quote: Testimonial quote text
        author: Author name
        role: Author's role/title (optional)
        avatar: URL to author's avatar image (optional)
        rating: Star rating out of 5 (optional)
        **kwargs: Additional HTML attributes

    Returns:
        Card component with testimonial content

    Example:
        Basic testimonial:
        >>> Testimonial(
        ...     quote="This product changed my life!",
        ...     author="John Doe",
        ...     role="CEO, Acme Corp"
        ... )

        With avatar and rating:
        >>> Testimonial(
        ...     quote="Absolutely amazing experience.",
        ...     author="Jane Smith",
        ...     role="Designer",
        ...     avatar="/static/avatars/jane.jpg",
        ...     rating=5
        ... )

    Note:
        Marked as @beta - API may change in future releases.
    """
    from ...utils.icons import Icon

    # Build avatar section
    avatar_section = None
    if avatar:
        avatar_section = Img(
            src=avatar,
            alt=author,
            cls="rounded-circle me-3",
            style="width: 48px; height: 48px; object-fit: cover;",
        )

    # Build rating stars
    rating_section = None
    if rating is not None:
        stars = []
        for i in range(5):
            star_icon = "star-fill" if i < rating else "star"
            stars.append(Icon(star_icon, cls="text-warning"))

        rating_section = Div(
            *stars,
            cls="mb-3",
        )

    # Build author info
    author_info = []
    author_info.append(Span(author, cls="fw-bold d-block"))
    if role:
        author_info.append(Span(role, cls="text-muted small"))

    author_section = Div(
        Div(
            avatar_section,
            Div(*author_info),
            cls="d-flex align-items-center",
        ),
        cls="mt-3",
    )

    # Build quote
    quote_section = Blockquote(
        P(f'"{quote}"', cls="mb-0 fst-italic"),
        cls="mb-3",
    )

    # Build card content
    card_content = []
    if rating_section:
        card_content.append(rating_section)
    card_content.append(quote_section)
    card_content.append(author_section)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("h-100", user_cls)

    return Card(
        *card_content,
        cls=all_classes,
        **kwargs,
    )


@beta
def TestimonialSection(
    *testimonials: Any,
    title: str = "What Our Customers Say",
    subtitle: str | None = None,
    columns: int = 3,
    **kwargs: Any,
) -> Div:
    """Section displaying multiple testimonials in a grid.

    Args:
        *testimonials: Testimonial components to display
        title: Section title
        subtitle: Optional subtitle
        columns: Number of columns in grid (default: 3)
        **kwargs: Additional HTML attributes

    Returns:
        Div with testimonials in responsive grid

    Example:
        Basic testimonial section:
        >>> TestimonialSection(
        ...     Testimonial(
        ...         quote="Great product!",
        ...         author="Alice",
        ...         role="Developer"
        ...     ),
        ...     Testimonial(
        ...         quote="Highly recommend!",
        ...         author="Bob",
        ...         role="Designer"
        ...     ),
        ...     Testimonial(
        ...         quote="Best decision ever!",
        ...         author="Carol",
        ...         role="Manager"
        ...     )
        ... )

        Custom title and 2 columns:
        >>> TestimonialSection(
        ...     *testimonials,
        ...     title="Success Stories",
        ...     subtitle="Hear from our happy customers",
        ...     columns=2
        ... )

    Note:
        Marked as @beta - API may change in future releases.
    """
    from ..layout.grid import Col, Container, Row

    # Build header
    header_content = [
        Div(
            title,
            cls="h2 text-center mb-2",
        )
    ]
    if subtitle:
        header_content.append(P(subtitle, cls="text-center text-muted mb-5"))

    header = Div(*header_content)

    # Build testimonial grid
    col_size = 12 // columns
    testimonial_cols = []
    for testimonial in testimonials:
        testimonial_cols.append(
            Col(
                testimonial,
                md=col_size,
                cls="mb-4",
            )
        )

    testimonial_grid = Row(*testimonial_cols)

    # Build classes
    base_classes = ["py-5"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(
        Container(
            header,
            testimonial_grid,
        ),
        **attrs,
    )
