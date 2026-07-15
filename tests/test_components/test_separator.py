"""Tests for Separator component."""

from fasthtml.common import to_xml

from faststrap.components.layout import Separator


def test_separator_horizontal_default():
    """Separator renders horizontal by default."""
    sep = Separator()
    html = to_xml(sep)

    assert 'role="separator"' in html
    assert 'aria-orientation="horizontal"' in html
    assert "border-top" in html


def test_separator_vertical():
    """Separator renders vertical when specified."""
    sep = Separator(orientation="vertical")
    html = to_xml(sep)

    assert 'role="separator"' in html
    assert 'aria-orientation="vertical"' in html
    assert "vr" in html


def test_separator_with_label():
    """Separator renders a centered label."""
    sep = Separator(label="Section")
    html = to_xml(sep)

    assert "Section" in html
    assert "d-flex" in html
    assert "align-items-center" in html


def test_separator_custom_spacing():
    """Separator supports Bootstrap spacing."""
    sep = Separator(spacing=3)
    html = to_xml(sep)

    assert "my-3" in html


def test_separator_custom_thickness():
    """Separator supports custom border thickness."""
    sep = Separator(thickness=2)
    html = to_xml(sep)

    assert "border-top-width: 2px" in html


def test_separator_vertical_custom_thickness():
    """Vertical separator supports custom thickness."""
    sep = Separator(orientation="vertical", thickness=3)
    html = to_xml(sep)

    assert "width: 3px" in html


def test_separator_vertical_spacing():
    """Vertical separator supports spacing."""
    sep = Separator(orientation="vertical", spacing=2)
    html = to_xml(sep)

    assert "margin-inline" in html


def test_separator_custom_classes():
    """Separator merges custom classes."""
    sep = Separator(cls="my-custom-class")
    html = to_xml(sep)

    assert "my-custom-class" in html


def test_separator_htmx():
    """Separator supports HTMX attributes."""
    sep = Separator(hx_get="/sections", hx_trigger="load")
    html = to_xml(sep)

    assert 'hx-get="/sections"' in html
    assert 'hx-trigger="load"' in html


def test_separator_data_attributes():
    """Separator handles data attributes."""
    sep = Separator(data_section="intro")
    html = to_xml(sep)

    assert 'data-section="intro"' in html
