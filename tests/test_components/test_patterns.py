"""Tests for pattern components (FooterModern, TestimonialSection)."""

from fasthtml.common import to_xml

from faststrap.components.patterns import (
    FooterModern,
    Testimonial,
    TestimonialSection,
)


# FooterModern Tests
def test_footer_modern_basic():
    """FooterModern renders with basic content."""
    footer = FooterModern(brand="MyApp")
    html = to_xml(footer)

    assert "MyApp" in html
    assert "footer" in html.lower()


def test_footer_modern_with_tagline():
    """FooterModern displays tagline."""
    footer = FooterModern(brand="MyApp", tagline="Building the future")
    html = to_xml(footer)

    assert "MyApp" in html
    assert "Building the future" in html


def test_footer_modern_with_columns():
    """FooterModern displays link columns."""
    footer = FooterModern(
        columns=[
            {
                "title": "Product",
                "links": [
                    {"text": "Features", "href": "/features"},
                    {"text": "Pricing", "href": "/pricing"},
                ],
            }
        ]
    )
    html = to_xml(footer)

    assert "Product" in html
    assert "Features" in html
    assert "/features" in html


def test_footer_modern_with_social():
    """FooterModern displays social links."""
    footer = FooterModern(
        social_links=[
            {"icon": "twitter", "href": "https://twitter.com/app"},
            {"icon": "github", "href": "https://github.com/app"},
        ]
    )
    html = to_xml(footer)

    assert "twitter" in html
    assert "github" in html


def test_footer_modern_copyright():
    """FooterModern displays copyright text."""
    footer = FooterModern(copyright_text="© 2026 MyCompany Inc.")
    html = to_xml(footer)

    assert "© 2026 MyCompany Inc." in html


def test_footer_modern_variants():
    """FooterModern supports background variants."""
    footer = FooterModern(brand="Test", bg_variant="light", text_variant="dark")
    html = to_xml(footer)

    assert "bg-light" in html
    assert "text-dark" in html


# Testimonial Tests
def test_testimonial_basic():
    """Testimonial renders with quote and author."""
    testimonial = Testimonial(quote="Great product!", author="John Doe")
    html = to_xml(testimonial)

    assert "Great product!" in html
    assert "John Doe" in html


def test_testimonial_with_role():
    """Testimonial displays author role."""
    testimonial = Testimonial(quote="Amazing!", author="Jane Smith", role="CEO, Acme Corp")
    html = to_xml(testimonial)

    assert "Jane Smith" in html
    assert "CEO, Acme Corp" in html


def test_testimonial_with_avatar():
    """Testimonial displays avatar image."""
    testimonial = Testimonial(quote="Test", author="Test User", avatar="/static/avatar.jpg")
    html = to_xml(testimonial)

    assert "/static/avatar.jpg" in html
    assert "rounded-circle" in html


def test_testimonial_with_rating():
    """Testimonial displays star rating."""
    testimonial = Testimonial(quote="Excellent!", author="User", rating=5)
    html = to_xml(testimonial)

    assert "star" in html  # Star icons


# TestimonialSection Tests
def test_testimonial_section_basic():
    """TestimonialSection renders with testimonials."""
    section = TestimonialSection(
        Testimonial(quote="Great!", author="User 1"),
        Testimonial(quote="Amazing!", author="User 2"),
    )
    html = to_xml(section)

    assert "Great!" in html
    assert "Amazing!" in html


def test_testimonial_section_title():
    """TestimonialSection displays custom title."""
    section = TestimonialSection(Testimonial(quote="Test", author="User"), title="Customer Reviews")
    html = to_xml(section)

    assert "Customer Reviews" in html


def test_testimonial_section_subtitle():
    """TestimonialSection displays subtitle."""
    section = TestimonialSection(
        Testimonial(quote="Test", author="User"), subtitle="Hear from our happy customers"
    )
    html = to_xml(section)

    assert "Hear from our happy customers" in html


def test_testimonial_section_columns():
    """TestimonialSection supports custom column count."""
    section = TestimonialSection(
        Testimonial(quote="1", author="A"), Testimonial(quote="2", author="B"), columns=2
    )
    html = to_xml(section)

    # Should have grid layout
    assert "row" in html.lower() or "col" in html.lower()
