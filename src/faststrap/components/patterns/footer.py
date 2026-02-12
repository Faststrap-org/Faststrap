"""Footer Pattern Component.

Modern multi-column footer with branding, links, social icons, and copyright.
"""

from typing import Any

from fasthtml.common import A, Div, Footer, Hr, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon


@beta
def FooterModern(
    brand: str | Any | None = None,
    tagline: str | None = None,
    columns: list[dict[str, Any]] | None = None,
    social_links: list[dict[str, str]] | None = None,
    copyright_text: str | None = None,
    bg_variant: str | None = None,
    text_variant: str | None = None,
    **kwargs: Any,
) -> Footer:
    """Modern multi-column footer with branding, links, and social icons.

    Perfect for landing pages and marketing sites. Responsive grid layout
    with brand section, link columns, social icons, and copyright.

    Args:
        brand: Brand name or logo element
        tagline: Optional tagline under brand
        columns: List of column dicts with 'title' and 'links' (list of dicts with 'text' and 'href')
        social_links: List of social link dicts with 'icon' and 'href'
        copyright_text: Copyright text (default: "© 2024 All rights reserved")
        bg_variant: Background color variant
        text_variant: Text color variant
        **kwargs: Additional HTML attributes

    Returns:
        Footer element with modern layout

    Example:
        Basic footer:
        >>> FooterModern(
        ...     brand="MyApp",
        ...     tagline="Building the future",
        ...     columns=[
        ...         {
        ...             "title": "Product",
        ...             "links": [
        ...                 {"text": "Features", "href": "/features"},
        ...                 {"text": "Pricing", "href": "/pricing"},
        ...             ]
        ...         },
        ...         {
        ...             "title": "Company",
        ...             "links": [
        ...                 {"text": "About", "href": "/about"},
        ...                 {"text": "Contact", "href": "/contact"},
        ...             ]
        ...         }
        ...     ],
        ...     social_links=[
        ...         {"icon": "twitter", "href": "https://twitter.com/myapp"},
        ...         {"icon": "github", "href": "https://github.com/myapp"},
        ...     ]
        ... )

        Custom styling:
        >>> FooterModern(
        ...     brand=H2("MyBrand", cls="text-primary"),
        ...     bg_variant="light",
        ...     text_variant="dark",
        ...     copyright_text="© 2026 MyCompany Inc."
        ... )

    Note:
        Marked as @beta - API may change in future releases.
    """
    from ...core.theme import resolve_defaults
    from ..layout.grid import Col, Container, Row

    # Resolve API defaults
    cfg = resolve_defaults("FooterModern", bg_variant=bg_variant, text_variant=text_variant)
    c_bg_variant = cfg.get("bg_variant", "dark")
    c_text_variant = cfg.get("text_variant", "light")

    # Default values
    if columns is None:
        columns = []
    if social_links is None:
        social_links = []
    if copyright_text is None:
        copyright_text = f"© {2026} All rights reserved"

    # Build brand section
    brand_section = None
    if brand or tagline:
        brand_content = []
        if brand:
            if isinstance(brand, str):
                brand_content.append(Span(brand, cls="fs-4 fw-bold"))
            else:
                brand_content.append(brand)
        if tagline:
            brand_content.append(P(tagline, cls="text-muted small mt-2"))

        brand_section = Col(
            Div(*brand_content),
            md=3,
            cls="mb-4 mb-md-0",
        )

    # Build link columns
    link_columns = []
    for column in columns:
        title = column.get("title", "")
        links = column.get("links", [])

        link_items = []
        for link in links:
            link_items.append(
                P(
                    A(
                        link.get("text", ""),
                        href=link.get("href", "#"),
                        cls=f"text-{c_text_variant} text-decoration-none",
                    ),
                    cls="mb-2",
                )
            )

        link_columns.append(
            Col(
                Div(
                    P(title, cls="fw-bold mb-3"),
                    *link_items,
                ),
                md=2,
                cls="mb-4 mb-md-0",
            )
        )

    # Build social links
    social_section = None
    if social_links:
        social_icons = []
        for social in social_links:
            social_icons.append(
                A(
                    Icon(social.get("icon", "")),
                    href=social.get("href", "#"),
                    cls=f"text-{c_text_variant} me-3 fs-4",
                    target="_blank",
                    rel="noopener noreferrer",
                )
            )

        social_section = Col(
            Div(
                P("Follow Us", cls="fw-bold mb-3"),
                Div(*social_icons, cls="d-flex"),
            ),
            md=3,
            cls="mb-4 mb-md-0",
        )

    # Build top section
    top_row_cols = []
    if brand_section:
        top_row_cols.append(brand_section)
    top_row_cols.extend(link_columns)
    if social_section:
        top_row_cols.append(social_section)

    top_section = Row(*top_row_cols) if top_row_cols else None

    # Build copyright section
    copyright_section = Div(
        Hr(cls=f"border-{c_text_variant} opacity-25 my-4"),
        P(copyright_text, cls="text-center text-muted small mb-0"),
    )

    # Build footer content
    footer_content = []
    if top_section:
        footer_content.append(top_section)
    footer_content.append(copyright_section)

    # Build classes
    base_classes = [f"bg-{c_bg_variant}", f"text-{c_text_variant}", "py-5", "mt-5"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Footer(
        Container(*footer_content),
        **attrs,
    )
