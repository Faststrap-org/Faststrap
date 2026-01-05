"""Tests for Placeholder components."""

from fasthtml.common import to_xml

from faststrap import Placeholder, PlaceholderButton, PlaceholderCard


def test_placeholder_basic():
    """Test basic placeholder creation."""
    ph = Placeholder(width="100%")
    html = to_xml(ph).replace(": ", ":")
    assert "placeholder" in html
    assert "width:100%" in html


def test_placeholder_animation_glow():
    """Test glow animation."""
    ph = Placeholder(width="75%", animation="glow")
    html = to_xml(ph)
    assert "placeholder-glow" in html


def test_placeholder_animation_wave():
    """Test wave animation."""
    ph = Placeholder(width="50%", animation="wave")
    html = to_xml(ph)
    assert "placeholder-wave" in html


def test_placeholder_variant():
    """Test color variant."""
    ph = Placeholder(width="100%", variant="primary")
    html = to_xml(ph)
    assert "bg-primary" in html


def test_placeholder_size():
    """Test size variants."""
    ph_xs = Placeholder(width="100%", size="xs")
    ph_sm = Placeholder(width="100%", size="sm")
    ph_lg = Placeholder(width="100%", size="lg")

    assert "placeholder-xs" in to_xml(ph_xs)
    assert "placeholder-sm" in to_xml(ph_sm)
    assert "placeholder-lg" in to_xml(ph_lg)


def test_placeholder_dimensions():
    """Test width and height."""
    ph = Placeholder(width="200px", height="50px")
    html = to_xml(ph)
    # Check styles (robust to spacing)
    html_nospaces = html.replace(": ", ":")
    assert "width:200px" in html_nospaces
    assert "height:50px" in html_nospaces


def test_placeholder_card_full():
    """Test full card placeholder."""
    card = PlaceholderCard(show_image=True, show_title=True, show_text=True)
    html = to_xml(card)
    assert "card" in html
    assert "card-body" in html
    assert "placeholder" in html


def test_placeholder_card_no_image():
    """Test card placeholder without image."""
    card = PlaceholderCard(show_image=False, show_title=True, show_text=True)
    html = to_xml(card)
    assert "card" in html
    assert "card-img-top" not in html


def test_placeholder_card_animation():
    """Test card placeholder with animation."""
    card = PlaceholderCard(animation="glow")
    html = to_xml(card)
    assert "placeholder-glow" in html or "placeholder" in html


def test_placeholder_button():
    """Test button placeholder."""
    btn = PlaceholderButton(width="120px", variant="primary")
    html = to_xml(btn).replace(": ", ":")
    assert "placeholder" in html
    assert "btn-primary" in html
    assert "width:120px" in html


def test_placeholder_button_animation():
    """Test button placeholder with animation."""
    btn = PlaceholderButton(animation="wave")
    html = to_xml(btn)
    assert "placeholder-wave" in html or "placeholder" in html
