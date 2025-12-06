"""Tests for Card component."""

from faststrap.components.display import Card


def test_card_basic():
    """Card renders with basic content."""
    card = Card("Content")
    html = str(card)

    assert "Content" in html
    assert "card" in html
    assert "card-body" in html


def test_card_with_title():
    """Card can have a title."""
    card = Card("Body text", title="Card Title")
    html = str(card)

    assert "Card Title" in html
    assert "card-title" in html
    assert "Body text" in html


def test_card_with_subtitle():
    """Card can have a subtitle."""
    card = Card("Content", title="Title", subtitle="Subtitle")
    html = str(card)

    assert "Title" in html
    assert "Subtitle" in html
    assert "card-subtitle" in html


def test_card_with_header():
    """Card can have a header section."""
    card = Card("Body", header="Featured")
    html = str(card)

    assert "Featured" in html
    assert "card-header" in html


def test_card_with_footer():
    """Card can have a footer section."""
    card = Card("Body", footer="Last updated")
    html = str(card)

    assert "Last updated" in html
    assert "card-footer" in html


def test_card_with_img_top():
    """Card can have top image."""
    card = Card("Content", img_top="image.jpg")
    html = str(card)

    assert 'src="image.jpg"' in html
    assert "card-img-top" in html


def test_card_with_img_bottom():
    """Card can have bottom image."""
    card = Card("Content", img_bottom="image.jpg")
    html = str(card)

    assert 'src="image.jpg"' in html
    assert "card-img-bottom" in html


def test_card_img_overlay():
    """Card supports image overlay mode."""
    card = Card("Overlay text", title="Title", img_top="bg.jpg", img_overlay=True)
    html = str(card)

    assert "card-img-overlay" in html
    assert "card-img" in html
    assert "Overlay text" in html


def test_card_full_structure():
    """Card with all parts works correctly."""
    card = Card(
        "Main content",
        title="Title",
        subtitle="Subtitle",
        header="Header",
        footer="Footer",
        img_top="top.jpg",
    )
    html = str(card)

    assert "Header" in html
    assert "Title" in html
    assert "Subtitle" in html
    assert "Main content" in html
    assert "Footer" in html
    assert "card-header" in html
    assert "card-footer" in html
    assert "card-img-top" in html


def test_card_custom_classes():
    """Card merges custom classes correctly."""
    card = Card("Content", cls="shadow-lg border-primary")
    html = str(card)

    assert "card" in html
    assert "shadow-lg" in html
    assert "border-primary" in html


def test_card_htmx():
    """Card supports HTMX attributes."""
    card = Card("Dynamic", hx_get="/load", hx_trigger="revealed")
    html = str(card)

    assert 'hx-get="/load"' in html
    assert 'hx-trigger="revealed"' in html


def test_card_multiple_children():
    """Card can contain multiple body elements."""
    card = Card("First paragraph. ", "Second paragraph.")
    html = str(card)

    assert "First paragraph." in html
    assert "Second paragraph." in html


def test_card_data_attributes():
    """Card handles data attributes correctly."""
    card = Card("Content", data_id="123", data_category="featured")
    html = str(card)

    assert 'data-id="123"' in html
    assert 'data-category="featured"' in html


def test_card_empty_body():
    """Card works with just header/footer."""
    card = Card(header="Only Header", footer="Only Footer")
    html = str(card)

    assert "Only Header" in html
    assert "Only Footer" in html
    assert "card-header" in html
    assert "card-footer" in html
