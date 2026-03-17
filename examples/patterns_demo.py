"""Faststrap Patterns Demo.

Showcasing modern UI patterns: FeatureGrid, PricingGroup, and NavbarModern.
"""

from fasthtml.common import H2, Div, FastHTML, serve

from faststrap import (
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
            columns=3,
        ),
        cls="py-5",
    )

    # 2. Pricing Section
    pricing = Div(
        H2("Upgrade Your Experience", cls="text-center mb-5"),
        PricingGroup(
            PricingTier(
                "Personal",
                0,
                features=["5 Projects", "Basic Support", "Limited Storage"],
                button_text="Choose Personal",
            ),
            PricingTier(
                "Team",
                49,
                features=[
                    "Unlimited Projects",
                    "Priority Support",
                    "Team Collaboration",
                    "Custom Branding",
                ],
                highlighted=True,
                button_text="Get Started",
            ),
            PricingTier(
                "Organization",
                199,
                features=[
                    "Enterprise SLA",
                    "Dedicated Account Manager",
                    "SSO & Security",
                    "Custom Contracts",
                ],
                button_text="Contact Us",
            ),
        ),
        cls="py-5",
    )

    return Container(nav, features, pricing, cls="py-4")


if __name__ == "__main__":
    serve(port=5014)
