"""
Production Landing Page Template - Modern SaaS Marketing Site

A fully responsive, conversion-optimized landing page showcasing Faststrap.

Features:
- Hero with animated gradient
- Features grid with icons
- Pricing tiers
- Testimonials
- FAQ accordion
- CTA sections
- Responsive footer
- Fully mobile optimized

Run: python main.py
"""

from fasthtml.common import *

from faststrap import (
    Accordion,
    AccordionItem,
    Badge,
    Button,
    Card,
    Col,
    Container,
    Icon,
    Row,
    add_bootstrap,
    create_theme,
)

# Initialize app
app = FastHTML()

# Modern SaaS theme
landing_theme = create_theme(
    primary="#6366F1",  # Indigo
    secondary="#8B5CF6",  # Purple
    success="#10B981",
    info="#3B82F6",
    warning="#F59E0B",
    danger="#EF4444",
)

add_bootstrap(app, theme=landing_theme, mode="light")


def Hero():
    """Hero section with CTA."""
    return Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge("New: v0.5.0 Released", variant="primary", cls="mb-3 px-3 py-2"),
                        H1(
                            "Build Beautiful UIs in ",
                            Span("Pure Python", cls="text-primary"),
                            cls="display-4 display-md-3 fw-bold mb-4",
                        ),
                        P(
                            "The most complete Bootstrap 5 component library for FastHTML. "
                            "51+ production-ready components with zero JavaScript required.",
                            cls="lead text-muted mb-4 fs-5 fs-md-4",
                        ),
                        Div(
                            Button(
                                Icon("rocket-takeoff", cls="me-2"),
                                "Get Started Free",
                                variant="primary",
                                size="lg",
                                cls="mb-3 mb-md-0 me-md-3 w-100 w-md-auto px-4 py-3",
                            ),
                            Button(
                                Icon("github", cls="me-2"),
                                "View on GitHub",
                                variant="outline-secondary",
                                size="lg",
                                cls="w-100 w-md-auto px-4 py-3",
                            ),
                            cls="d-flex flex-column flex-md-row gap-3",
                        ),
                        Div(
                            Icon("check-circle", cls="text-success me-2"),
                            Span("Free forever", cls="text-muted small me-3 me-md-4"),
                            Icon("check-circle", cls="text-success me-2"),
                            Span("MIT License", cls="text-muted small me-3 me-md-4"),
                            Icon("check-circle", cls="text-success me-2"),
                            Span("No credit card", cls="text-muted small"),
                            cls="mt-4 d-flex flex-wrap align-items-center justify-content-center justify-content-md-start",
                        ),
                        cls="text-center text-md-start",
                    ),
                    cols=12,
                    lg=6,
                    cls="d-flex align-items-center mb-5 mb-lg-0",
                ),
                Col(
                    Div(
                        # Code preview
                        Div(
                            Pre(
                                Code(
                                    """from fasthtml.common import *
from faststrap import Card, Button

app, rt = fast_app()
add_bootstrap(app)

@rt("/")
def get():
    return Card(
        "Welcome to Faststrap!",
        Button("Get Started",
               variant="primary"),
        header="Hello World 👋"
    )

serve()""",
                                    cls="language-python text-start small",
                                ),
                                cls="bg-dark text-white p-3 p-md-4 rounded shadow-lg overflow-auto",
                            ),
                            cls="position-relative",
                        ),
                        cls="d-none d-lg-block",
                    ),
                    cols=12,
                    lg=6,
                ),
            ),
            cls="py-5",
        ),
        cls="bg-light py-4 py-md-5",
    )


def FeatureCard(icon: str, title: str, description: str):
    """Feature card component."""
    return Card(
        Div(
            Div(Icon(icon, size=40, cls="text-primary mb-3"), cls="text-center"),
            H5(title, cls="text-center mb-3"),
            P(description, cls="text-muted text-center mb-0 small"),
            cls="p-3 p-md-4",
        ),
        cls="h-100 border-0 shadow-sm hover-shadow transition",
    )


def Features():
    """Features section."""
    features = [
        {
            "icon": "lightning-charge",
            "title": "Zero JavaScript",
            "description": "Build interactive UIs without writing JavaScript. Pure Python all the way.",
        },
        {
            "icon": "puzzle",
            "title": "51+ Components",
            "description": "Production-ready components for forms, navigation, feedback, and layouts.",
        },
        {
            "icon": "bootstrap",
            "title": "Bootstrap Native",
            "description": "Built on Bootstrap 5.3, familiar to millions of developers worldwide.",
        },
        {
            "icon": "code-slash",
            "title": "Type Safe",
            "description": "Full type hints for excellent IDE autocomplete and error checking.",
        },
        {
            "icon": "palette",
            "title": "Customizable",
            "description": "Themes, defaults, slot classes - customize everything to match your brand.",
        },
        {
            "icon": "universal-access",
            "title": "Accessible",
            "description": "WCAG 2.1 AA compliant with proper ARIA attributes and semantic HTML.",
        },
    ]

    return Div(
        Container(
            Div(
                H2("Why Choose Faststrap?", cls="text-center display-5 fw-bold mb-3"),
                P(
                    "Everything you need to build modern web applications in Python",
                    cls="text-center text-muted lead mb-5",
                ),
                cls="mb-4",
            ),
            Row(
                *[
                    Col(
                        FeatureCard(f["icon"], f["title"], f["description"]),
                        cols=12,
                        sm=6,
                        lg=4,
                        cls="mb-4",
                    )
                    for f in features
                ]
            ),
        ),
        cls="py-4 py-md-5",
    )


def PricingCard(name: str, price: str, features: list, cta_text: str, featured: bool = False):
    """Pricing tier card."""
    return Card(
        Div(
            H4(name, cls="text-center mb-3"),
            Div(
                Span(price, cls="display-4 fw-bold"),
                Span("/month" if price != "Free" else "", cls="text-muted"),
                cls="text-center mb-4",
            ),
            Div(
                *[
                    Div(
                        Icon("check-circle", cls="text-success me-2"),
                        Span(feature, cls="small"),
                        cls="mb-2",
                    )
                    for feature in features
                ],
                cls="mb-4",
            ),
            Button(
                cta_text, variant="primary" if featured else "outline-primary", cls="w-100 py-2"
            ),
            cls="p-3 p-md-4",
        ),
        cls=f"h-100 {'border-primary border-2 shadow-lg' if featured else 'border-0 shadow-sm'}",
    )


def Pricing():
    """Pricing section."""
    return Div(
        Container(
            Div(
                H2("Simple, Transparent Pricing", cls="text-center display-5 fw-bold mb-3"),
                P(
                    "Faststrap is 100% free and open-source. Forever.",
                    cls="text-center text-muted lead mb-5",
                ),
                cls="mb-4",
            ),
            Row(
                Col(
                    PricingCard(
                        "Open Source",
                        "Free",
                        [
                            "All 51+ components",
                            "Full documentation",
                            "Community support",
                            "MIT License",
                            "Unlimited projects",
                            "Commercial use allowed",
                        ],
                        "Get Started",
                        featured=True,
                    ),
                    cols=12,
                    md=6,
                    lg=4,
                    cls="mb-4 offset-lg-2",
                ),
                Col(
                    PricingCard(
                        "Enterprise Support",
                        "Contact Us",
                        [
                            "Everything in Open Source",
                            "Priority bug fixes",
                            "Custom components",
                            "1-on-1 training",
                            "SLA guarantee",
                            "Dedicated support",
                        ],
                        "Contact Sales",
                    ),
                    cols=12,
                    md=6,
                    lg=4,
                    cls="mb-4",
                ),
            ),
        ),
        cls="py-4 py-md-5 bg-light",
    )


def Stats():
    """Statistics section."""
    return Div(
        Container(
            Row(
                *[
                    Col(
                        Div(
                            H2(value, cls="display-4 fw-bold text-primary mb-2"),
                            P(label, cls="text-muted mb-0"),
                            cls="text-center",
                        ),
                        cols=6,
                        md=3,
                        cls="mb-4",
                    )
                    for value, label in [
                        ("51+", "Components"),
                        ("320+", "Tests"),
                        ("95%", "Coverage"),
                        ("15+", "Contributors"),
                    ]
                ]
            )
        ),
        cls="py-4 py-md-5",
    )


def Testimonials():
    """Testimonials section."""
    testimonials = [
        {
            "quote": "Faststrap saved me weeks of development time. The components just work!",
            "author": "Sarah Johnson",
            "role": "Full Stack Developer",
        },
        {
            "quote": "Finally, a Bootstrap library that feels native to Python. Love it!",
            "author": "Michael Chen",
            "role": "Tech Lead",
        },
        {
            "quote": "The best way to build UIs with FastHTML. Clean API, great docs.",
            "author": "Emma Davis",
            "role": "Software Engineer",
        },
    ]

    return Div(
        Container(
            Div(
                H2("Loved by Developers", cls="text-center display-5 fw-bold mb-3"),
                P(
                    "See what developers are saying about Faststrap",
                    cls="text-center text-muted lead mb-5",
                ),
                cls="mb-4",
            ),
            Row(
                *[
                    Col(
                        Card(
                            P(f'"{t["quote"]}"', cls="mb-4 fst-italic"),
                            Div(
                                Strong(t["author"]),
                                Br(),
                                Small(t["role"], cls="text-muted"),
                                cls="text-center",
                            ),
                            cls="p-3 p-md-4 border-0 shadow-sm",
                        ),
                        cols=12,
                        md=4,
                        cls="mb-4",
                    )
                    for t in testimonials
                ]
            ),
        ),
        cls="py-4 py-md-5 bg-light",
    )


def FAQ():
    """FAQ section with accordion."""
    faqs = [
        (
            "Is Faststrap really free?",
            "Yes! Faststrap is 100% free and open-source under the MIT License. You can use it in personal and commercial projects without any restrictions.",
        ),
        (
            "Do I need to know JavaScript?",
            "No! That's the beauty of Faststrap. Everything is pure Python. The components handle all the JavaScript for you.",
        ),
        (
            "Can I customize the components?",
            "Absolutely! You can customize themes, set component defaults, use slot classes, and override any Bootstrap class.",
        ),
        (
            "Does it work with HTMX?",
            "Yes! Faststrap components work seamlessly with HTMX. Just add hx_* attributes to any component.",
        ),
        (
            "What about mobile responsiveness?",
            "All components are fully responsive out of the box, using Bootstrap's mobile-first grid system.",
        ),
    ]

    return Div(
        Container(
            Div(
                H2("Frequently Asked Questions", cls="text-center display-5 fw-bold mb-3"),
                P("Got questions? We've got answers.", cls="text-center text-muted lead mb-5"),
                cls="mb-4",
            ),
            Row(
                Col(
                    Accordion(
                        *[
                            AccordionItem(answer, title=question, item_id=f"faq-{i}", show=i == 0)
                            for i, (question, answer) in enumerate(faqs)
                        ],
                        accordion_id="faqAccordion",
                    ),
                    cols=12,
                    lg=8,
                    cls="offset-lg-2",
                )
            ),
        ),
        cls="py-4 py-md-5",
    )


def CTA():
    """Call-to-action section."""
    return Div(
        Container(
            Row(
                Col(
                    Div(
                        H2(
                            "Ready to Build Something Amazing?",
                            cls="display-5 fw-bold mb-4 text-white",
                        ),
                        P(
                            "Join thousands of developers building beautiful UIs with Faststrap",
                            cls="lead mb-4 text-white-50",
                        ),
                        Div(
                            Button(
                                Icon("download", cls="me-2"),
                                "Install Faststrap",
                                variant="light",
                                size="lg",
                                cls="mb-3 mb-md-0 me-md-3 w-100 w-md-auto px-4 py-3",
                            ),
                            Button(
                                Icon("book", cls="me-2"),
                                "Read Documentation",
                                variant="outline-light",
                                size="lg",
                                cls="w-100 w-md-auto px-4 py-3",
                            ),
                            cls="d-flex flex-column flex-md-row gap-3",
                        ),
                        cls="text-center",
                    ),
                    cols=12,
                )
            )
        ),
        cls="py-4 py-md-5 bg-primary",
    )


def Footer():
    """Responsive footer section."""
    return Div(
        Container(
            Row(
                Col(
                    Div(
                        H5("Faststrap", cls="mb-3"),
                        P(
                            "The complete Bootstrap 5 component library for FastHTML",
                            cls="text-muted small",
                        ),
                        cls="mb-4",
                    ),
                    cols=12,
                    md=4,
                    cls="mb-4 mb-md-0",
                ),
                Col(
                    Div(
                        H6("Product", cls="mb-3"),
                        Div(
                            A(
                                "Documentation",
                                href="/docs",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Components",
                                href="/components",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Examples",
                                href="/examples",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "GitHub",
                                href="https://github.com",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                        ),
                        cls="mb-4",
                    ),
                    cols=6,
                    md=2,
                    cls="mb-4 mb-md-0",
                ),
                Col(
                    Div(
                        H6("Resources", cls="mb-3"),
                        Div(
                            A(
                                "Getting Started",
                                href="/start",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Tutorials",
                                href="/tutorials",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Blog",
                                href="/blog",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Changelog",
                                href="/changelog",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                        ),
                        cls="mb-4",
                    ),
                    cols=6,
                    md=2,
                    cls="mb-4 mb-md-0",
                ),
                Col(
                    Div(
                        H6("Community", cls="mb-3"),
                        Div(
                            A(
                                "Discord",
                                href="#",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Twitter",
                                href="#",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Contributing",
                                href="/contributing",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Code of Conduct",
                                href="/conduct",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                        ),
                        cls="mb-4",
                    ),
                    cols=6,
                    md=2,
                    cls="mb-4 mb-md-0",
                ),
                Col(
                    Div(
                        H6("Legal", cls="mb-3"),
                        Div(
                            A(
                                "License",
                                href="/license",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Privacy",
                                href="/privacy",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                            A(
                                "Terms",
                                href="/terms",
                                cls="text-muted d-block mb-2 small text-decoration-none",
                            ),
                        ),
                        cls="mb-4",
                    ),
                    cols=6,
                    md=2,
                ),
            ),
            Hr(cls="my-4"),
            Div(
                P(
                    "© 2026 Faststrap. Built with ❤️ for the FastHTML community.",
                    cls="text-muted text-center mb-0 small",
                ),
                cls="py-3",
            ),
        ),
        cls="py-4 py-md-5 bg-light",
    )


@app.route("/")
def get():
    """Landing page."""
    return Div(
        Hero(),
        Stats(),
        Features(),
        Testimonials(),
        Pricing(),
        FAQ(),
        CTA(),
        Footer(),
        # Custom styles for responsiveness and animations
        Style(
            """
            .hover-shadow {
                transition: box-shadow 0.3s ease-in-out;
            }
            .hover-shadow:hover {
                box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
            }

            /* Responsive typography */
            @media (max-width: 767.98px) {
                .display-4 {
                    font-size: 2.5rem !important;
                }
                .display-5 {
                    font-size: 2rem !important;
                }
            }

            /* Responsive button widths */
            .w-md-auto {
                width: 100%;
            }

            @media (min-width: 768px) {
                .w-md-auto {
                    width: auto !important;
                }
            }

            /* Ensure proper wrapping and no shrinking on mobile */
            @media (max-width: 767.98px) {
                .d-flex {
                    flex-wrap: wrap !important;
                }
                .btn {
                    min-width: 100% !important;
                    white-space: normal !important;
                }
                .gap-3 > * {
                    flex-shrink: 0 !important;
                }
            }

            /* Prevent content shrinking */
            * {
                flex-shrink: 1;
            }

            @media (max-width: 767.98px) {
                .container, .container-fluid {
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }
            }
        """
        ),
        cls="bg-white",
        data_bs_theme="light",
    )


if __name__ == "__main__":
    serve(port=5089)
