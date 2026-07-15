"""Tests for AspectRatio component."""

from fasthtml.common import Div, to_xml

from faststrap.components.layout import AspectRatio


def test_aspect_ratio_default():
    """AspectRatio defaults to 16/9."""
    ar = AspectRatio(Div("Content"))
    html = to_xml(ar)

    assert "aspect-ratio: 16/9" in html
    assert "overflow-hidden" in html


def test_aspect_ratio_custom():
    """AspectRatio supports custom ratio."""
    ar = AspectRatio(Div("Content"), ratio="4/3")
    html = to_xml(ar)

    assert "aspect-ratio: 4/3" in html


def test_aspect_ratio_square():
    """AspectRatio supports 1/1 square ratio."""
    ar = AspectRatio(Div("Avatar"), ratio="1/1")
    html = to_xml(ar)

    assert "aspect-ratio: 1/1" in html


def test_aspect_ratio_widescreen():
    """AspectRatio supports 21/9 ultrawide ratio."""
    ar = AspectRatio(Div("Banner"), ratio="21/9")
    html = to_xml(ar)

    assert "aspect-ratio: 21/9" in html


def test_aspect_ratio_children_fill():
    """AspectRatio children fill the container."""
    ar = AspectRatio(Div("Image"))
    html = to_xml(ar)

    assert "width: 100%" in html
    assert "height: 100%" in html


def test_aspect_ratio_custom_classes():
    """AspectRatio merges custom classes."""
    ar = AspectRatio(Div("Content"), cls="rounded")
    html = to_xml(ar)

    assert "rounded" in html
    assert "overflow-hidden" in html


def test_aspect_ratio_htmx():
    """AspectRatio supports HTMX attributes."""
    ar = AspectRatio(Div("Content"), hx_get="/media/1")
    html = to_xml(ar)

    assert 'hx-get="/media/1"' in html


def test_aspect_ratio_data_attributes():
    """AspectRatio handles data attributes."""
    ar = AspectRatio(Div("Content"), data_type="video")
    html = to_xml(ar)

    assert 'data-type="video"' in html


def test_aspect_ratio_multiple_children():
    """AspectRatio can contain multiple children wrapped in a container."""
    ar = AspectRatio(Div(Div("First"), Div("Second")))
    html = to_xml(ar)

    assert "First" in html
    assert "Second" in html
