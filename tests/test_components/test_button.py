"""Tests for Button component."""

from faststrap.components.forms import Button


def test_button_basic():
    """Button renders with basic content."""
    btn = Button("Click Me")
    html = str(btn)

    assert "Click Me" in html
    assert "btn" in html
    assert "btn-primary" in html


def test_button_variants():
    """Button supports all variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        btn = Button("Test", variant=variant)
        assert f"btn-{variant}" in str(btn)


def test_button_outline():
    """Button supports outline style."""
    btn = Button("Test", variant="primary", outline=True)
    assert "btn-outline-primary" in str(btn)


def test_button_sizes():
    """Button supports different sizes."""
    btn_sm = Button("Small", size="sm")
    btn_lg = Button("Large", size="lg")

    assert "btn-sm" in str(btn_sm)
    assert "btn-lg" in str(btn_lg)


def test_button_disabled():
    """Button can be disabled."""
    btn = Button("Disabled", disabled=True)
    assert "disabled" in str(btn)


def test_button_loading():
    """Button shows loading spinner."""
    btn = Button("Loading", loading=True)
    html = str(btn)

    assert "spinner-border" in html
    assert "disabled" in html


def test_button_icon():
    """Button can display icon."""
    btn = Button("Save", icon="check")
    assert "bi-check" in str(btn)


def test_button_htmx():
    """Button supports HTMX attributes."""
    btn = Button("Load", hx_get="/api", hx_target="#result")
    html = str(btn)

    assert 'hx-get="/api"' in html
    assert 'hx-target="#result"' in html


def test_button_custom_classes():
    """Button merges custom classes."""
    btn = Button("Test", cls="mt-3 custom-class")
    html = str(btn)

    assert "btn" in html
    assert "mt-3" in html
    assert "custom-class" in html


def test_button_htmx_conversion():
    """Test that HTMX attributes convert properly."""
    btn = Button("Test", hx_get="/api", data_value="123", aria_label="Button")
    html = str(btn)

    assert 'hx-get="/api"' in html, f"Missing hx-get: {html}"
    assert 'data-value="123"' in html, f"Missing data-value: {html}"
    assert 'aria-label="Button"' in html, f"Missing aria-label: {html}"
    assert "hx_get" not in html, f"Should not have hx_get: {html}"
    assert "data_value" not in html, f"Should not have data_value: {html}"


def test_button_html5_attributes():
    """Test that standard HTML attributes work."""
    btn = Button("Test", type="submit", form="form1", autofocus=True)
    html = str(btn)

    assert 'type="submit"' in html
    assert 'form="form1"' in html
    assert "autofocus" in html
