"""Pricing Pattern Components."""

from typing import Any

from fasthtml.common import H2, H3, Div, Li, P, Span, Ul

from ...core._stability import beta
from ..display.card import Card
from ..forms.button import Button
from ..layout.grid import Col, Row


@beta
def PricingTier(
    name: str,
    price: str | int,
    period: str = "month",
    features: list[str] | None = None,
    button_text: str = "Get Started",
    button_href: str = "#",
    highlighted: bool = False,
    **kwargs: Any,
) -> Any:
    """A single pricing tier card.

    Args:
        name: Tier name (e.g., "Pro", "Enterprise")
        price: Price amount
        period: Billing period (e.g., "month", "year")
        features: List of feature strings
        button_text: CTA button text
        button_href: CTA button link
        highlighted: Whether to highlight this tier
        **kwargs: Additional attributes

    Returns:
        Card component with pricing content

    Note:
        Marked as @beta - API may change in future releases.
    """
    if features is None:
        features = []

    # Build feature list
    feature_items = [Li(feat) for feat in features]
    feature_list = Ul(*feature_items, cls="list-unstyled")

    # Build price display
    price_display = Div(
        Span("$", cls="fs-4"),
        Span(str(price), cls="display-4 fw-bold"),
        Span(f"/{period}", cls="text-muted"),
        cls="mb-4",
    )

    # Build CTA button
    cta_button = Button(
        button_text,
        href=button_href,
        variant="primary",
        outline=not highlighted,
        size="lg",
        cls="w-100",
    )

    # Build card
    card_cls = "h-100 text-center"
    if highlighted:
        card_cls += " border-primary shadow-lg"

    return Card(
        H3(name, cls="card-title"),
        price_display,
        feature_list,
        cta_button,
        cls=card_cls,
        **kwargs,
    )


@beta
def PricingGroup(
    *tiers: Any,
    title: str = "Choose Your Plan",
    subtitle: str | None = None,
    **kwargs: Any,
) -> Div:
    """Group of pricing tiers in a responsive grid.

    Args:
        *tiers: PricingTier components
        title: Section title
        subtitle: Optional subtitle
        **kwargs: Additional attributes

    Returns:
        Div with pricing tiers in grid

    Note:
        Marked as @beta - API may change in future releases.
    """
    # Build header
    header = Div(
        H2(title, cls="text-center mb-2"),
        P(subtitle, cls="text-center text-muted mb-5") if subtitle else None,
    )

    # Build tier grid
    col_size = 12 // len(tiers) if tiers else 12
    cols = [Col(tier, md=col_size, cls="mb-4") for tier in tiers]

    return Div(
        header,
        Row(*cols),
        cls="pricing-group py-5",
        **kwargs,
    )
