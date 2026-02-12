"""Tests for ThemeToggle component."""

from fasthtml.common import to_xml

from faststrap.components.forms import ThemeToggle


def test_theme_toggle_basic():
    """ThemeToggle renders with default settings."""
    toggle = ThemeToggle()
    html = to_xml(toggle)

    assert "form-check" in html
    assert "form-switch" in html
    assert "/theme/toggle" in html


def test_theme_toggle_light_theme():
    """ThemeToggle shows unchecked for light theme."""
    toggle = ThemeToggle(current_theme="light")
    html = to_xml(toggle)

    assert "checked" not in html or 'checked="False"' in html
    assert "bi-sun" in html  # Sun icon for light mode


def test_theme_toggle_dark_theme():
    """ThemeToggle shows checked for dark theme."""
    toggle = ThemeToggle(current_theme="dark")
    html = to_xml(toggle)

    assert "checked" in html
    assert "bi-moon" in html  # Moon icon for dark mode


def test_theme_toggle_custom_endpoint():
    """ThemeToggle supports custom endpoint."""
    toggle = ThemeToggle(endpoint="/api/user/theme")
    html = to_xml(toggle)

    assert "/api/user/theme" in html
    assert "hx-post" in html


def test_theme_toggle_custom_id():
    """ThemeToggle supports custom ID."""
    toggle = ThemeToggle(toggle_id="user-theme-toggle")
    html = to_xml(toggle)

    assert "user-theme-toggle" in html


def test_theme_toggle_with_label():
    """ThemeToggle shows label when requested."""
    toggle = ThemeToggle(show_label=True, label_text="Dark Mode")
    html = to_xml(toggle)

    assert "Dark Mode" in html
    assert "form-check-label" in html


def test_theme_toggle_without_label():
    """ThemeToggle hides label by default."""
    toggle = ThemeToggle(show_label=False)
    html = to_xml(toggle)

    assert "form-check-label" not in html


def test_theme_toggle_htmx_attributes():
    """ThemeToggle has proper HTMX attributes."""
    toggle = ThemeToggle()
    html = to_xml(toggle)

    assert "hx-post" in html
    assert "hx-trigger" in html
    assert "change" in html  # Triggers on change
    assert "hx-swap" in html


def test_theme_toggle_auto_theme():
    """ThemeToggle handles auto theme."""
    toggle = ThemeToggle(current_theme="auto")
    html = to_xml(toggle)

    # Auto should default to unchecked (light)
    assert "checked" not in html or 'checked="False"' in html


def test_theme_toggle_custom_classes():
    """ThemeToggle merges custom classes."""
    toggle = ThemeToggle(cls="custom-toggle")
    html = to_xml(toggle)

    assert "custom-toggle" in html
    assert "form-check" in html
    assert "form-switch" in html
