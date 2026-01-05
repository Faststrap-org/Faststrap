"""Tests for Image component."""

from fasthtml.common import to_xml

from faststrap import Image


def test_image_basic():
    """Test basic image creation."""
    img = Image(src="test.jpg", alt="Test image")
    html = to_xml(img)
    assert 'src="test.jpg"' in html
    assert 'alt="Test image"' in html


def test_image_fluid():
    """Test fluid (responsive) image."""
    img = Image(src="test.jpg", fluid=True)
    html = to_xml(img)
    assert "img-fluid" in html


def test_image_thumbnail():
    """Test thumbnail styling."""
    img = Image(src="test.jpg", thumbnail=True)
    html = to_xml(img)
    assert "img-thumbnail" in html


def test_image_rounded():
    """Test rounded corners."""
    img = Image(src="test.jpg", rounded=True)
    html = to_xml(img)
    assert "rounded" in html


def test_image_rounded_circle():
    """Test circular image."""
    img = Image(src="test.jpg", rounded_circle=True)
    html = to_xml(img)
    assert "rounded-circle" in html


def test_image_align_start():
    """Test left alignment."""
    img = Image(src="test.jpg", align="start")
    html = to_xml(img)
    assert "float-start" in html


def test_image_align_end():
    """Test right alignment."""
    img = Image(src="test.jpg", align="end")
    html = to_xml(img)
    assert "float-end" in html


def test_image_align_center():
    """Test center alignment."""
    img = Image(src="test.jpg", align="center")
    html = to_xml(img)
    assert "d-block" in html
    assert "mx-auto" in html


def test_image_dimensions():
    """Test width and height."""
    img = Image(src="test.jpg", width="300px", height="200px")
    html = to_xml(img)
    assert 'width="300px"' in html
    assert 'height="200px"' in html


def test_image_lazy_loading():
    """Test lazy loading attribute."""
    img = Image(src="test.jpg", loading="lazy")
    html = to_xml(img)
    assert 'loading="lazy"' in html


def test_image_combined():
    """Test multiple attributes combined."""
    img = Image(
        src="avatar.jpg", alt="User avatar", fluid=True, rounded_circle=True, loading="lazy"
    )
    html = to_xml(img)
    assert "img-fluid" in html
    assert "rounded-circle" in html
    assert 'loading="lazy"' in html
    assert 'alt="User avatar"' in html


def test_image_custom_class():
    """Test custom CSS classes."""
    img = Image(src="test.jpg", cls="custom-class")
    html = to_xml(img)
    assert "custom-class" in html
