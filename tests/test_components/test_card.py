"""Tests for Card component."""

from fasthtml.common import to_xml

from faststrap.components.display import Card


def test_card_basic():
    """Card renders with basic content."""
    card = Card("Content")
    html = to_xml(card)

    assert "Content" in html
    assert "card" in html
    assert "card-body" in html


def test_card_with_title():
    """Card can have a title."""
    card = Card("Body text", title="Card Title")
    html = to_xml(card)

    assert "Card Title" in html
    assert "card-title" in html
    assert "Body text" in html


def test_card_with_subtitle():
    """Card can have a subtitle."""
    card = Card("Content", title="Title", subtitle="Subtitle")
    html = to_xml(card)

    assert "Title" in html
    assert "Subtitle" in html
    assert "card-subtitle" in html


def test_card_with_header():
    """Card can have a header section."""
    card = Card("Body", header="Featured")
    html = to_xml(card)

    assert "Featured" in html
    assert "card-header" in html


def test_card_with_footer():
    """Card can have a footer section."""
    card = Card("Body", footer="Last updated")
    html = to_xml(card)

    assert "Last updated" in html
    assert "card-footer" in html


def test_card_with_img_top():
    """Card can have top image."""
    card = Card("Content", img_top="image.jpg")
    html = to_xml(card)

    assert 'src="image.jpg"' in html
    assert "card-img-top" in html


def test_card_with_img_bottom():
    """Card can have bottom image."""
    card = Card("Content", img_bottom="image.jpg")
    html = to_xml(card)

    assert 'src="image.jpg"' in html
    assert "card-img-bottom" in html


def test_card_image_attributes_are_configurable():
    card = Card(
        "Content",
        img_top="laptop.jpg",
        img_alt="Laptop on a desk",
        img_loading="lazy",
        img_width=640,
        img_height=360,
        img_cls="object-fit-cover",
        img_attrs={"data-testid": "card-image"},
    )
    html = to_xml(card)

    assert 'alt="Laptop on a desk"' in html
    assert 'loading="lazy"' in html
    assert 'width="640"' in html
    assert 'height="360"' in html
    assert "card-img-top object-fit-cover" in html
    assert 'data-testid="card-image"' in html


def test_card_img_overlay():
    """Card supports image overlay mode."""
    card = Card("Overlay text", title="Title", img_top="bg.jpg", img_overlay=True)
    html = to_xml(card)

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
    html = to_xml(card)

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
    html = to_xml(card)

    assert "card" in html
    assert "shadow-lg" in html
    assert "border-primary" in html


def test_card_htmx():
    """Card supports HTMX attributes."""
    card = Card("Dynamic", hx_get="/load", hx_trigger="revealed")
    html = to_xml(card)

    assert 'hx-get="/load"' in html
    assert 'hx-trigger="revealed"' in html


def test_card_multiple_children():
    """Card can contain multiple body elements."""
    card = Card("First paragraph. ", "Second paragraph.")
    html = to_xml(card)

    assert "First paragraph." in html
    assert "Second paragraph." in html


def test_card_data_attributes():
    """Card handles data attributes correctly."""
    card = Card("Content", data_id="123", data_category="featured")
    html = to_xml(card)

    assert 'data-id="123"' in html
    assert 'data-category="featured"' in html


def test_card_empty_body():
    """Card works with just header/footer."""
    card = Card(header="Only Header", footer="Only Footer")
    html = to_xml(card)

    assert "Only Header" in html
    assert "Only Footer" in html
    assert "card-header" in html
    assert "card-footer" in html


def test_card_supports_nested_attr_escape_hatches():
    """Card exposes nested attribute hooks for composite sections."""
    card = Card(
        "Body copy",
        title="Title",
        subtitle="Subtitle",
        header="Header",
        footer="Footer",
        header_attrs={"data_role": "card-header"},
        body_attrs={"data_section": "card-body"},
        footer_attrs={"id": "card-footer"},
        title_attrs={"data_title": "main"},
        subtitle_attrs={"data_subtitle": "supporting"},
        text_attrs={"data_copy": "body"},
    )
    html = to_xml(card)

    assert 'data-role="card-header"' in html
    assert 'data-section="card-body"' in html
    assert 'id="card-footer"' in html
    assert 'data-title="main"' in html
    assert 'data-subtitle="supporting"' in html
    assert 'data-copy="body"' in html


def test_card_nested_attrs_merge_with_nested_classes():
    """Nested attrs should merge classes instead of overriding component defaults."""
    card = Card(
        "Body copy",
        title="Title",
        header="Header",
        header_cls="border-0",
        body_cls="p-4",
        title_cls="text-primary",
        header_attrs={"cls": "bg-primary-subtle"},
        body_attrs={"cls": "shadow-sm"},
        title_attrs={"cls": "display-6"},
    )
    html = to_xml(card)

    assert "card-header border-0 bg-primary-subtle" in html
    assert "card-body p-4 shadow-sm" in html
    assert "card-title text-primary display-6" in html
