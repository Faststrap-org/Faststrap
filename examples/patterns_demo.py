"""Faststrap Patterns Demo.

Showcasing modern UI patterns: FeatureGrid, PricingGroup, and NavbarModern.
"""

from fasthtml.common import H2, Div, FastHTML, serve

from faststrap import (
    Button,
    Container,
    Feature,
    FeatureGrid,
    NavbarModern,
    PricingGroup,
    PricingTier,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="purple-magic", font_family="Poppins")


@app.route("/")
def home():
    nav = NavbarModern(brand="Patterns Demo", items=[], glass=True)

    # 1. Feature Grid
    features = Div(
        H2("Professional Patterns", cls="text-center mb-5"),
        FeatureGrid(
            Feature(
                "Modern Navbar",
                "Glassmorphism components with sticky positioning.",
                icon="stars",
                icon_cls="bg-primary-subtle text-primary",
            ),
            Feature(
                "Feature Grids",
                "Easily showcase your product's value proposition.",
                icon="grid-3x3-gap",
                icon_cls="bg-success-subtle text-success",
            ),
            Feature(
                "Pricing Tables",
                "Built-in components for comparison and conversion.",
                icon="credit-card",
                icon_cls="bg-warning-subtle text-warning",
            ),
            cols=3,
        ),
        cls="py-5",
    )

    # 2. Pricing Section
    pricing = Div(
        H2("Upgrade Your Experience", cls="text-center mb-5"),
        PricingGroup(
            PricingTier(
                "Personal",
                "$0",
                ["5 Projects", "Basic Support", "Limited Storage"],
                cta=Button("Choose Personal", cls="btn-outline-primary w-100"),
            ),
            PricingTier(
                "Team",
                "$49",
                ["Unlimited Projects", "Priority Support", "Team Collaboration", "Custom Branding"],
                featured=True,
                cta=Button("Get Started", cls="btn-primary w-100"),
            ),
            PricingTier(
                "Organization",
                "Custom",
                [
                    "Enterprise SLA",
                    "Dedicated Account Manager",
                    "SSO & Security",
                    "Custom Contracts",
                ],
                cta=Button("Contact Us", cls="btn-outline-primary w-100"),
            ),
        ),
        cls="py-5",
    )

    return Container(nav, features, pricing, cls="py-4")


if __name__ == "__main__":
    serve(port=5014)
