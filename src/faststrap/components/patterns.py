"""Compatibility re-exports for pattern components.

This module remains for backward compatibility. The canonical implementations
live under the ``faststrap.components.patterns`` package.
"""

from .patterns import (
    Feature,
    FeatureGrid,
    FooterModern,
    NavbarModern,
    PricingGroup,
    PricingTier,
    Testimonial,
    TestimonialSection,
)

__all__ = [
    "Feature",
    "FeatureGrid",
    "FooterModern",
    "NavbarModern",
    "PricingGroup",
    "PricingTier",
    "Testimonial",
    "TestimonialSection",
]
