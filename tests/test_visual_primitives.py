"""Tests for CSS-only visual primitives absorbed into Faststrap core."""

from fasthtml.common import to_xml

from faststrap import (
    DotsLoader,
    FlipCard,
    FloatingActionButton,
    GlowCard,
    GradientButton,
    ParallaxSection,
    PolygonLoader,
    ProgressRing,
    PulseLoader,
    RevealCard,
    RingLoader,
    ShadowLoader,
    TiltCard,
    TypewriterLoader,
    WaveLoader,
)
from faststrap.core.assets import FASTSTRAP_CDN_CSS_FILES, local_assets
from faststrap.core.registry import list_components


def test_visual_cards_render_expected_classes() -> None:
    html = to_xml(FlipCard("Front", "Back", height="240px", duration="0.4s"))
    assert "faststrap-flip-card" in html
    assert "--faststrap-flip-duration: 0.4s" in html
    assert "Front" in html
    assert "Back" in html

    assert "faststrap-tilt-card" in to_xml(TiltCard("Lift"))
    assert "faststrap-glow-card" in to_xml(GlowCard("Glow", intensity="high"))


def test_reveal_card_and_parallax_render_media_styles() -> None:
    reveal = to_xml(RevealCard("/hero.jpg", "Suite", description="Private balcony"))
    assert 'src="/hero.jpg"' in reveal
    assert "faststrap-reveal-overlay" in reveal
    assert "Private balcony" in reveal

    section = to_xml(ParallaxSection("Content", img_src="/bg.jpg", overlay_opacity=0.25))
    assert "faststrap-parallax-section" in section
    assert "background-image: url('/bg.jpg')" in section
    assert "--faststrap-parallax-overlay-opacity: 0.25" in section


def test_css_only_loaders_render_accessible_statuses() -> None:
    for component in (
        DotsLoader,
        RingLoader,
        WaveLoader,
        PulseLoader,
        PolygonLoader,
    ):
        html = to_xml(component(label="Fetching"))
        assert 'role="status"' in html
        assert "Fetching" in html

    assert "faststrap-typewriter-loader" in to_xml(TypewriterLoader("Working..."))
    assert "faststrap-shadow-loader" in to_xml(ShadowLoader("Working..."))


def test_progress_ring_renders_svg_progressbar() -> None:
    html = to_xml(ProgressRing(75, variant="success"))
    assert 'role="progressbar"' in html
    assert 'aria-valuenow="75"' in html
    assert "75%" in html
    assert "var(--bs-success)" in html


def test_action_buttons_use_core_button_surface() -> None:
    gradient = to_xml(GradientButton("Launch", gradient="blue", href="/start"))
    assert "faststrap-gradient-button" in gradient
    assert "--faststrap-gradient-button-bg" in gradient
    assert 'href="/start"' in gradient

    fab = to_xml(FloatingActionButton(icon="plus", variant="success", position="top-left"))
    assert "faststrap-floating-action-button" in fab
    assert "fab-top-left" in fab
    assert 'aria-label="Primary action"' in fab



def test_gradient_button_does_not_mutate_caller_css_vars() -> None:
    shared: dict = {"--custom": "1px"}
    to_xml(GradientButton("Launch", css_vars=shared))
    assert shared == {"--custom": "1px"}


def test_visual_css_is_loaded_with_core_assets() -> None:
    assert "css/faststrap-visual.css" in FASTSTRAP_CDN_CSS_FILES
    rendered = "".join(to_xml(asset) for asset in local_assets("/static", include_js=False))
    assert "/static/css/faststrap-visual.css" in rendered


def test_new_components_are_registered() -> None:
    registered = set(list_components())
    for name in {
        "FlipCard",
        "GlowCard",
        "RevealCard",
        "TiltCard",
        "DotsLoader",
        "RingLoader",
        "WaveLoader",
        "PulseLoader",
        "PolygonLoader",
        "ProgressRing",
        "GradientButton",
        "FloatingActionButton",
        "ParallaxSection",
    }:
        assert name in registered
