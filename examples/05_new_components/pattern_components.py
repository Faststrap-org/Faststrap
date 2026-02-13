"""
Pattern Components Demo
Demonstrates FooterModern, Testimonial, and TestimonialSection components
"""

from fasthtml.common import Div, FastHTML, H1, H2, serve

from faststrap import (
    Col,
    Container,
    FooterModern,
    Row,
    Testimonial,
    TestimonialSection,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    return Div(
        # Main content
        Container(
            H1("Pattern Components Demo", cls="my-5 text-center"),
            # Testimonials Section
            H2("Customer Testimonials", cls="text-center mb-4"),
            TestimonialSection(
                Testimonial(
                    quote=(
                        "FastStrap has completely transformed how we build"
                        " web applications. The zero-JS philosophy is brilliant!"
                    ),
                    author="Sarah Johnson",
                    role="CTO, TechCorp",
                    rating=5,
                ),
                Testimonial(
                    quote=(
                        "The component library is comprehensive and the"
                        " documentation is excellent. Highly recommended!"
                    ),
                    author="Michael Chen",
                    role="Lead Developer, StartupXYZ",
                    rating=5,
                ),
                Testimonial(
                    quote=(
                        "We migrated from React to FastHTML + FastStrap"
                        " and our development speed doubled."
                    ),
                    author="Emily Rodriguez",
                    role="Engineering Manager, BigCo",
                    rating=4,
                ),
                columns=3,
            ),
            # Individual Testimonial
            H2("Featured Testimonial", cls="text-center mb-4 mt-5"),
            Row(
                Col(
                    Testimonial(
                        quote=(
                            "FastStrap's HTMX presets saved us weeks of"
                            " development time. The ActiveSearch and"
                            " InfiniteScroll components work flawlessly"
                            " out of the box."
                        ),
                        author="David Park",
                        role="Senior Full-Stack Developer",
                        rating=5,
                    ),
                    cols=12,
                    md=8,
                    offset_md=2,
                )
            ),
            # Placeholder content
            Div(style="height: 200px;"),  # Spacer to show footer
        ),
        # Footer Demo
        FooterModern(
            brand="FastStrap",
            tagline="Build beautiful web UIs in pure Python",
            columns=[
                {
                    "title": "Product",
                    "links": [
                        {"text": "Features", "href": "/features"},
                        {"text": "Documentation", "href": "/docs"},
                        {"text": "Examples", "href": "/examples"},
                        {"text": "Pricing", "href": "/pricing"},
                    ],
                },
                {
                    "title": "Company",
                    "links": [
                        {"text": "About", "href": "/about"},
                        {"text": "Blog", "href": "/blog"},
                        {"text": "Careers", "href": "/careers"},
                        {"text": "Contact", "href": "/contact"},
                    ],
                },
                {
                    "title": "Resources",
                    "links": [
                        {"text": "Community", "href": "/community"},
                        {"text": "Support", "href": "/support"},
                        {"text": "Status", "href": "/status"},
                        {"text": "GitHub", "href": "https://github.com"},
                    ],
                },
            ],
            social_links=[
                {"icon": "github", "href": "https://github.com"},
                {"icon": "twitter", "href": "https://twitter.com"},
                {"icon": "linkedin", "href": "https://linkedin.com"},
                {"icon": "discord", "href": "https://discord.com"},
            ],
            copyright_text="© 2026 FastStrap. All rights reserved.",
            bg_variant="dark",
            text_variant="light",
        ),
    )


serve()
