"""Tests for components added in v0.5.0."""

from fasthtml.common import to_xml

from faststrap import (
    Carousel,
    CarouselItem,
    Image,
    Placeholder,
    PlaceholderButton,
    PlaceholderCard,
    Scrollspy,
    reset_component_defaults,
    set_component_defaults,
)


class TestImage:
    """Tests for Image component."""

    def test_basic_image(self):
        img = Image(src="test.jpg", alt="Test")
        html = to_xml(img)
        assert 'src="test.jpg"' in html
        assert 'alt="Test"' in html

    def test_fluid_image(self):
        img = Image(src="test.jpg", fluid=True)
        html = to_xml(img)
        assert "img-fluid" in html

    def test_thumbnail_image(self):
        img = Image(src="test.jpg", thumbnail=True)
        html = to_xml(img)
        assert "img-thumbnail" in html

    def test_rounded_image(self):
        img = Image(src="test.jpg", rounded=True)
        html = to_xml(img)
        assert "rounded" in html

    def test_rounded_circle(self):
        img = Image(src="avatar.jpg", rounded_circle=True)
        html = to_xml(img)
        assert "rounded-circle" in html

    def test_alignment_center(self):
        img = Image(src="test.jpg", align="center")
        html = to_xml(img)
        assert "d-block" in html
        assert "mx-auto" in html

    def test_alignment_start(self):
        img = Image(src="test.jpg", align="start")
        html = to_xml(img)
        assert "float-start" in html

    def test_alignment_end(self):
        img = Image(src="test.jpg", align="end")
        html = to_xml(img)
        assert "float-end" in html

    def test_lazy_loading(self):
        img = Image(src="test.jpg", loading="lazy")
        html = to_xml(img)
        assert 'loading="lazy"' in html

    def test_dimensions(self):
        img = Image(src="test.jpg", width=300, height=200)
        html = to_xml(img)
        assert 'width="300px"' in html
        assert 'height="200px"' in html

    def test_dimensions_string(self):
        img = Image(src="test.jpg", width="50%", height="auto")
        html = to_xml(img)
        assert 'width="50%"' in html
        assert 'height="auto"' in html

    def test_respects_defaults(self):
        set_component_defaults("Image", fluid=True, rounded=True)
        img = Image(src="test.jpg")
        html = to_xml(img)
        assert "img-fluid" in html
        assert "rounded" in html
        reset_component_defaults()

    def test_explicit_overrides_defaults(self):
        set_component_defaults("Image", fluid=True)
        img = Image(src="test.jpg", fluid=False)
        html = to_xml(img)
        assert "img-fluid" not in html
        reset_component_defaults()


class TestCarousel:
    """Tests for Carousel component."""

    def test_basic_carousel(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            CarouselItem("Item 2"),
        )
        html = to_xml(carousel)
        assert "carousel" in html
        assert "slide" in html
        assert "carousel-inner" in html
        assert "carousel-item" in html

    def test_carousel_with_controls(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            controls=True,
        )
        html = to_xml(carousel)
        assert "carousel-control-prev" in html
        assert "carousel-control-next" in html
        assert "carousel-control-prev-icon" in html
        assert "carousel-control-next-icon" in html

    def test_carousel_with_indicators(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            CarouselItem("Item 2"),
            indicators=True,
        )
        html = to_xml(carousel)
        assert "carousel-indicators" in html
        assert 'data-bs-slide-to="0"' in html
        assert 'data-bs-slide-to="1"' in html

    def test_carousel_fade(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            fade=True,
        )
        html = to_xml(carousel)
        assert "carousel-fade" in html

    def test_carousel_dark(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            dark=True,
        )
        html = to_xml(carousel)
        assert "carousel-dark" in html

    def test_carousel_interval(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            interval=3000,
        )
        html = to_xml(carousel)
        assert 'data-bs-interval="3000"' in html

    def test_carousel_no_interval(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            interval=False,
        )
        html = to_xml(carousel)
        assert 'data-bs-interval="false"' in html

    def test_carousel_keyboard(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            keyboard=False,
        )
        html = to_xml(carousel)
        assert 'data-bs-keyboard="false"' in html

    def test_carousel_pause(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            pause=False,
        )
        html = to_xml(carousel)
        assert 'data-bs-pause="false"' in html

    def test_carousel_wrap(self):
        carousel = Carousel(
            CarouselItem("Item 1", active=True),
            wrap=False,
        )
        html = to_xml(carousel)
        assert 'data-bs-wrap="false"' in html

    def test_carousel_item_caption(self):
        item = CarouselItem(
            "Content",
            caption="Caption text",
            caption_title="Title",
            active=True,
        )
        html = to_xml(item)
        assert "carousel-caption" in html
        assert "Caption text" in html
        assert "Title" in html
        assert "d-none d-md-block" in html

    def test_carousel_item_interval(self):
        item = CarouselItem("Content", interval=10000, active=True)
        html = to_xml(item)
        assert 'data-bs-interval="10000"' in html

    def test_carousel_respects_defaults(self):
        set_component_defaults("Carousel", controls=True, indicators=True, fade=True)
        carousel = Carousel(CarouselItem("Item 1", active=True))
        html = to_xml(carousel)
        assert "carousel-control-prev" in html
        assert "carousel-indicators" in html
        assert "carousel-fade" in html
        reset_component_defaults()


class TestPlaceholder:
    """Tests for Placeholder components."""

    def test_basic_placeholder(self):
        ph = Placeholder(width="100%")
        html = to_xml(ph)
        assert "placeholder" in html
        assert "width: 100%" in html

    def test_placeholder_with_height(self):
        ph = Placeholder(width="50%", height="2rem")
        html = to_xml(ph)
        assert "width: 50%" in html
        assert "height: 2rem" in html

    def test_placeholder_with_animation_glow(self):
        ph = Placeholder(width="50%", animation="glow")
        html = to_xml(ph)
        assert "placeholder-glow" in html
        assert "placeholder" in html

    def test_placeholder_with_animation_wave(self):
        ph = Placeholder(width="75%", animation="wave")
        html = to_xml(ph)
        assert "placeholder-wave" in html

    def test_placeholder_with_variant(self):
        ph = Placeholder(width="75%", variant="primary")
        html = to_xml(ph)
        assert "bg-primary" in html

    def test_placeholder_with_size(self):
        ph = Placeholder(width="50%", size="lg")
        html = to_xml(ph)
        assert "placeholder-lg" in html

    def test_placeholder_size_sm(self):
        ph = Placeholder(width="50%", size="sm")
        html = to_xml(ph)
        assert "placeholder-sm" in html

    def test_placeholder_size_xs(self):
        ph = Placeholder(width="50%", size="xs")
        html = to_xml(ph)
        assert "placeholder-xs" in html

    def test_placeholder_card(self):
        card = PlaceholderCard(animation="wave")
        html = to_xml(card)
        assert "card" in html
        assert "placeholder" in html
        assert "placeholder-wave" in html

    def test_placeholder_card_no_image(self):
        card = PlaceholderCard(show_image=False)
        html = to_xml(card)
        assert "card" in html
        assert "card-img-top" not in html

    def test_placeholder_card_no_title(self):
        card = PlaceholderCard(show_title=False)
        html = to_xml(card)
        assert "card" in html
        # Should still have text placeholders
        assert "placeholder" in html

    def test_placeholder_button(self):
        btn = PlaceholderButton(width="120px", variant="success")
        html = to_xml(btn)
        assert "placeholder" in html
        assert "btn-success" in html
        assert "width:120px" in html

    def test_placeholder_button_with_animation(self):
        btn = PlaceholderButton(animation="glow")
        html = to_xml(btn)
        assert "placeholder-glow" in html

    def test_placeholder_respects_defaults(self):
        set_component_defaults("Placeholder", animation="glow", variant="secondary")
        ph = Placeholder(width="100%")
        html = to_xml(ph)
        assert "placeholder-glow" in html
        assert "bg-secondary" in html
        reset_component_defaults()


class TestScrollspy:
    """Tests for Scrollspy component."""

    def test_basic_scrollspy(self):
        spy = Scrollspy(
            "Content",
            target="#navbar",
        )
        html = to_xml(spy)
        assert 'data-bs-spy="scroll"' in html
        assert 'data-bs-target="#navbar"' in html
        assert 'tabindex="0"' in html

    def test_scrollspy_with_offset(self):
        spy = Scrollspy(
            "Content",
            target="#nav",
            offset=100,
        )
        html = to_xml(spy)
        assert 'data-bs-offset="100"' in html

    def test_scrollspy_with_method(self):
        spy = Scrollspy(
            "Content",
            target="#nav",
            method="position",
        )
        html = to_xml(spy)
        assert 'data-bs-method="position"' in html

    def test_scrollspy_smooth_scroll(self):
        spy = Scrollspy(
            "Content",
            target="#nav",
            smooth_scroll=True,
        )
        html = to_xml(spy)
        assert 'data-bs-smooth-scroll="true"' in html

    def test_scrollspy_multiple_options(self):
        spy = Scrollspy(
            "Content",
            target="#nav",
            offset=50,
            method="auto",
            smooth_scroll=True,
        )
        html = to_xml(spy)
        assert 'data-bs-offset="50"' in html
        assert 'data-bs-method="auto"' in html
        assert 'data-bs-smooth-scroll="true"' in html
