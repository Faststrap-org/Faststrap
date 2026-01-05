"""Tests for Carousel component."""

from fasthtml.common import Img, to_xml

from faststrap import Carousel, CarouselItem


def test_carousel_basic():
    """Test basic carousel creation."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), CarouselItem(Img(src="2.jpg")))
    html = to_xml(carousel)
    assert "carousel" in html
    assert "carousel-inner" in html


def test_carousel_with_id():
    """Test carousel with custom ID."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), carousel_id="myCarousel")
    html = to_xml(carousel)
    assert 'id="myCarousel"' in html


def test_carousel_controls():
    """Test carousel with controls."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), controls=True)
    html = to_xml(carousel)
    assert "carousel-control-prev" in html
    assert "carousel-control-next" in html


def test_carousel_indicators():
    """Test carousel with indicators."""
    carousel = Carousel(
        CarouselItem(Img(src="1.jpg"), active=True), CarouselItem(Img(src="2.jpg")), indicators=True
    )
    html = to_xml(carousel)
    assert "carousel-indicators" in html


def test_carousel_fade():
    """Test carousel with fade transition."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), fade=True)
    html = to_xml(carousel)
    assert "carousel-fade" in html


def test_carousel_dark():
    """Test dark variant carousel."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), dark=True)
    html = to_xml(carousel)
    assert "carousel-dark" in html


def test_carousel_interval():
    """Test carousel with custom interval."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), interval=3000)
    html = to_xml(carousel)
    assert 'data-bs-interval="3000"' in html


def test_carousel_no_autoplay():
    """Test carousel without autoplay."""
    carousel = Carousel(CarouselItem(Img(src="1.jpg"), active=True), interval=False)
    html = to_xml(carousel)
    assert 'data-bs-interval="false"' in html


def test_carousel_item_caption():
    """Test carousel item with caption."""
    item = CarouselItem(Img(src="test.jpg"), caption="Test caption", active=True)
    html = to_xml(item)
    assert "carousel-item" in html
    assert "carousel-caption" in html
    assert "Test caption" in html


def test_carousel_item_caption_title():
    """Test carousel item with caption title."""
    item = CarouselItem(
        Img(src="test.jpg"), caption_title="Title", caption="Caption text", active=True
    )
    html = to_xml(item)
    assert "Title" in html
    assert "Caption text" in html


def test_carousel_item_active():
    """Test active carousel item."""
    item = CarouselItem(Img(src="test.jpg"), active=True)
    html = to_xml(item)
    assert "active" in html


def test_carousel_item_custom_interval():
    """Test carousel item with custom interval."""
    item = CarouselItem(Img(src="test.jpg"), interval=10000)
    html = to_xml(item)
    assert 'data-bs-interval="10000"' in html
