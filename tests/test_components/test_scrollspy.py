"""Tests for Scrollspy component."""

from fasthtml.common import H2, Div, P, to_xml

from faststrap import Scrollspy


def test_scrollspy_basic():
    """Test basic scrollspy creation."""
    spy = Scrollspy(
        Div(H2("Section 1"), id="section1"), Div(H2("Section 2"), id="section2"), target="#navbar"
    )
    html = to_xml(spy)
    assert 'data-bs-spy="scroll"' in html
    assert 'data-bs-target="#navbar"' in html
    assert 'tabindex="0"' in html


def test_scrollspy_offset():
    """Test scrollspy with offset."""
    spy = Scrollspy(Div(id="section1"), target="#nav", offset=100)
    html = to_xml(spy)
    assert 'data-bs-offset="100"' in html


def test_scrollspy_method():
    """Test scrollspy method."""
    spy = Scrollspy(Div(id="section1"), target="#nav", method="position")
    html = to_xml(spy)
    assert 'data-bs-method="position"' in html


def test_scrollspy_smooth_scroll():
    """Test smooth scrolling."""
    spy = Scrollspy(Div(id="section1"), target="#nav", smooth_scroll=True)
    html = to_xml(spy)
    assert 'data-bs-smooth-scroll="true"' in html


def test_scrollspy_multiple_sections():
    """Test scrollspy with multiple sections."""
    spy = Scrollspy(
        Div(H2("Intro"), P("Content"), id="intro"),
        Div(H2("Features"), P("Content"), id="features"),
        Div(H2("Pricing"), P("Content"), id="pricing"),
        target="#mainNav",
    )
    html = to_xml(spy)
    assert 'data-bs-spy="scroll"' in html
    assert "Intro" in html
    assert "Features" in html
    assert "Pricing" in html
