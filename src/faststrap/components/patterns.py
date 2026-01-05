"""Modern UI 패턴 components."""

from typing import Any

from fasthtml.common import H2, H3, Div, I, Nav, P, Span

from ..components.display.card import Card
from ..components.layout.grid import Col, Row
from ..components.navigation.navbar import Navbar
from ..core._stability import beta
from ..core.base import merge_classes


@beta
def NavbarModern(
    brand: Any,
    items: list[Any] | None = None,
    sticky: bool = True,
    glass: bool = True,
    **kwargs: Any,
) -> Nav:
    """A premium, modern navbar with optional glassmorphism.

    Args:
        brand: Brand content
        items: List of nav items
        sticky: Stick to top
        glass: Apply glassmorphism effect
        **kwargs: Additional attributes
    """
    user_cls = kwargs.pop("cls", "")
    classes = ["navbar", "navbar-expand-lg"]
    if glass:
        classes.append("navbar-glass")
    if sticky:
        classes.append("sticky-top")

    all_cls = merge_classes(" ".join(classes), user_cls)
    return Navbar(brand=brand, items=items, cls=all_cls, **kwargs)


@beta
def Feature(
    title: str,
    description: str,
    icon: str | Any | None = None,
    icon_cls: str = "bg-primary text-white",
    **kwargs: Any,
) -> Div:
    """A single feature item with icon, title, and description."""
    icon_el = None
    if isinstance(icon, str):
        icon_el = Div(I(cls=f"bi bi-{icon}"), cls=f"feature-icon {icon_cls}")
    elif icon:
        icon_el = Div(icon, cls=f"feature-icon {icon_cls}")

    return Div(
        icon_el,
        H3(title, cls="fs-4 fw-bold"),
        P(description, cls="text-muted"),
        cls="feature-item p-3",
        **kwargs,
    )


@beta
def FeatureGrid(
    *features: Any,
    cols: int = 3,
    **kwargs: Any,
) -> Div:
    """A grid of Feature components."""
    col_size = 12 // cols if cols <= 12 else 4
    return Row(*[Col(f, md=col_size, cls="mb-4") for f in features], **kwargs)


@beta
def PricingTier(
    name: str,
    price: str,
    features: list[str],
    cta: Any | None = None,
    featured: bool = False,
    period: str = "month",
    **kwargs: Any,
) -> Div:
    """A pricing card tier."""
    cls = kwargs.pop("cls", "")
    card_cls = merge_classes("pricing-card h-100 shadow-sm border-0 py-4", cls)
    if featured:
        card_cls = merge_classes(card_cls, "featured scale-up shadow-lg")

    items = [Div(I(cls="bi bi-check2 text-primary me-2"), f, cls="mb-2") for f in features]

    content = Div(
        Div(name, cls="text-uppercase fw-bold text-muted small mb-2"),
        H2(
            Div(price, Span(f"/{period}", cls="fs-6 text-muted"), cls="d-flex align-items-baseline")
        ),
        Div(*items, cls="my-4 py-2"),
        cta if cta else "",
        cls="card-body text-center",
    )

    return Card(content, cls=card_cls, **kwargs)


@beta
def PricingGroup(
    *tiers: Any,
    **kwargs: Any,
) -> Div:
    """A horizontal group of pricing tiers."""
    return Row(
        *[Col(t, lg=4, md=6, cls="mb-4") for t in tiers], cls="justify-content-center g-4", **kwargs
    )
