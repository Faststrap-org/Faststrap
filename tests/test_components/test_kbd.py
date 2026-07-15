"""Tests for Kbd component."""

from fasthtml.common import to_xml

from faststrap.components.display import Kbd


def test_kbd_basic():
    """Kbd renders with basic content."""
    kbd = Kbd("Ctrl")
    html = to_xml(kbd)

    assert "Ctrl" in html
    assert "kbd" in html


def test_kbd_light_variant():
    """Kbd defaults to light variant."""
    kbd = Kbd("A")
    html = to_xml(kbd)

    assert "bg-light" in html
    assert "text-dark" in html


def test_kbd_dark_variant():
    """Kbd supports dark variant."""
    kbd = Kbd("B", variant="dark")
    html = to_xml(kbd)

    assert "bg-dark" in html
    assert "text-light" in html


def test_kbd_sm_size():
    """Kbd supports small size."""
    kbd = Kbd("X", size="sm")
    html = to_xml(kbd)

    assert "kbd-sm" in html


def test_kbd_md_size():
    """Kbd defaults to medium size."""
    kbd = Kbd("X")
    html = to_xml(kbd)

    assert "kbd" in html
    assert "kbd-sm" not in html
    assert "kbd-lg" not in html


def test_kbd_lg_size():
    """Kbd supports large size."""
    kbd = Kbd("X", size="lg")
    html = to_xml(kbd)

    assert "kbd-lg" in html


def test_kbd_custom_classes():
    """Kbd merges custom classes."""
    kbd = Kbd("Tab", cls="ms-2")
    html = to_xml(kbd)

    assert "ms-2" in html


def test_kbd_htmx():
    """Kbd supports HTMX attributes."""
    kbd = Kbd("F1", hx_get="/help", hx_trigger="click")
    html = to_xml(kbd)

    assert 'hx-get="/help"' in html
    assert 'hx-trigger="click"' in html


def test_kbd_data_attributes():
    """Kbd handles data attributes."""
    kbd = Kbd("Esc", data_action="close")
    html = to_xml(kbd)

    assert 'data-action="close"' in html


def test_kbd_combo():
    """Kbd can represent key combinations."""
    kbd = Kbd("Ctrl", " + ", "Shift", " + ", "P")
    html = to_xml(kbd)

    assert "Ctrl" in html
    assert "Shift" in html
    assert "P" in html
