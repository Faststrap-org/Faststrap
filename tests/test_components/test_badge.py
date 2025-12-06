"""Tests for Badge component."""

from faststrap.components.display import Badge


def test_badge_basic():
    """Badge renders with basic content."""
    badge = Badge("New")
    html = str(badge)

    assert "New" in html
    assert "badge" in html
    assert "text-bg-primary" in html


def test_badge_variants():
    """Badge supports all color variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        badge = Badge("Test", variant=variant)
        html = str(badge)
        assert f"text-bg-{variant}" in html


def test_badge_pill():
    """Badge supports pill (rounded) style."""
    badge = Badge("99+", pill=True)
    html = str(badge)

    assert "badge" in html
    assert "rounded-pill" in html


def test_badge_not_pill_by_default():
    """Badge is not pill by default."""
    badge = Badge("Test")
    html = str(badge)

    assert "badge" in html
    assert "rounded-pill" not in html


def test_badge_custom_classes():
    """Badge merges custom classes correctly."""
    badge = Badge("Custom", cls="ms-2 fs-6")
    html = str(badge)

    assert "badge" in html
    assert "ms-2" in html
    assert "fs-6" in html


def test_badge_htmx():
    """Badge supports HTMX attributes."""
    badge = Badge("Live", hx_get="/status", hx_trigger="every 5s")
    html = str(badge)

    assert 'hx-get="/status"' in html
    assert 'hx-trigger="every 5s"' in html


def test_badge_multiple_children():
    """Badge can contain multiple elements."""
    badge = Badge("Count: ", "42")
    html = str(badge)

    assert "Count:" in html
    assert "42" in html


def test_badge_data_attributes():
    """Badge handles data attributes correctly."""
    badge = Badge("Data", data_value="123", data_status="active")
    html = str(badge)

    assert 'data-value="123"' in html
    assert 'data-status="active"' in html
