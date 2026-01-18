import pytest
from fasthtml.common import FastHTML

from faststrap.core.assets import add_bootstrap
from faststrap.core.theme import (
    Theme,
    get_builtin_theme,
    reset_component_defaults,
    resolve_defaults,
    set_component_defaults,
)


def test_theme_initialization():
    """Test Theme object creation and properties."""
    theme = Theme({"--bs-primary": "#112233"})
    assert theme.variables["--bs-primary"] == "#112233"


def test_builtin_themes():
    """Test retrieving and checking builtin themes."""
    theme = get_builtin_theme("green-nature")
    assert theme is not None
    assert theme.variables["--bs-primary"] == "#7BA05B"

    with pytest.raises(ValueError):
        get_builtin_theme("nonexistent")


def test_theme_css_generation():
    """Test Theme.to_style() output for different modes."""
    theme = get_builtin_theme("blue-ocean")

    # Light mode
    light_css = theme.to_style(mode="light")
    assert ":root" in str(light_css)
    assert f"--bs-primary: {theme.variables['--bs-primary']}" in str(light_css)

    # Dark mode (should contain variables from _DARK_MODE_VARS)
    dark_css = theme.to_style(mode="dark")
    assert "--bs-body-bg: #212529" in str(dark_css)

    # Auto mode (should contain both and media query)
    auto_css = theme.to_style(mode="auto")
    assert '[data-bs-theme="dark"]' in auto_css
    assert "@media (prefers-color-scheme: dark)" in auto_css


def test_resolve_defaults_mechanics():
    """Test the priority logic of resolve_defaults."""
    reset_component_defaults()

    # 1. Hardcoded fallback (resets to primary)
    res = resolve_defaults("Button", variant=None)
    assert res.get("variant") == "primary"

    # 2. Set global default
    set_component_defaults("Button", variant="success", size="lg")
    res = resolve_defaults("Button", variant=None, size=None)
    assert res["variant"] == "success"
    assert res["size"] == "lg"

    # 3. Explicit argument overrides global default
    res = resolve_defaults("Button", variant="danger", size=None)
    assert res["variant"] == "danger"
    assert res["size"] == "lg"

    reset_component_defaults()


def test_add_bootstrap_integration():
    """Test add_bootstrap API with various themes and modes."""
    app = FastHTML()

    # String theme
    add_bootstrap(app, theme="green-nature", mode="dark")
    assert app.htmlkw["data-bs-theme"] == "dark"

    # Theme object
    app2 = FastHTML()
    theme = Theme({"--bs-primary": "#ff0000"})
    add_bootstrap(app2, theme=theme, mode="light")
    assert app2.htmlkw["data-bs-theme"] == "light"
    assert any("#ff0000" in str(a) for a in app2.hdrs)


def test_slot_classes_resolution():
    """Test resolution of slot classes (like header_cls)."""
    reset_component_defaults()
    set_component_defaults("Card", header_cls="bg-primary text-white")

    # No explicit override
    res = resolve_defaults("Card", header_cls=None)
    assert res["header_cls"] == "bg-primary text-white"

    # Explicit override
    res = resolve_defaults("Card", header_cls="custom-header")
    assert res["header_cls"] == "custom-header"

    reset_component_defaults()


def test_google_fonts_integration():
    """Test Google Fonts integration in add_bootstrap."""
    app = FastHTML()

    # Add bootstrap with Google Font
    add_bootstrap(app, font_family="Inter", font_weights=[400, 700])

    # Check that Google Fonts link is in headers
    hdrs_str = [str(h) for h in app.hdrs]
    assert any("fonts.googleapis.com" in s and "Inter" in s for s in hdrs_str)

    # Check that font-family CSS is in headers
    assert any("--bs-body-font-family" in s and "Inter" in s for s in hdrs_str)


def test_google_fonts_with_theme():
    """Test Google Fonts work with themes."""
    app = FastHTML()

    # Built-in theme + font
    add_bootstrap(app, theme="green-nature", font_family="Roboto")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should have both theme and font
    assert any("#7BA05B" in s for s in hdrs_str)  # Theme color
    assert any("Roboto" in s for s in hdrs_str)  # Font


def test_google_fonts_default_weights():
    """Test that default font weights are applied when not specified."""
    app = FastHTML()

    add_bootstrap(app, font_family="Poppins")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should use default weights [400, 500, 700]
    font_link = next((s for s in hdrs_str if "fonts.googleapis.com" in s and "Poppins" in s), None)
    assert font_link is not None
    assert "400" in font_link
    assert "500" in font_link
    assert "700" in font_link


def test_google_fonts_custom_weights():
    """Test custom font weights."""
    app = FastHTML()

    add_bootstrap(app, font_family="Inter", font_weights=[300, 600, 800])

    hdrs_str = [str(h) for h in app.hdrs]
    font_link = next((s for s in hdrs_str if "fonts.googleapis.com" in s and "Inter" in s), None)
    assert font_link is not None
    assert "300" in font_link
    assert "600" in font_link
    assert "800" in font_link


def test_google_fonts_with_spaces():
    """Test font names with spaces are properly URL-encoded."""
    app = FastHTML()

    add_bootstrap(app, font_family="Open Sans")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should encode spaces as %20 (URL encoding)
    assert any("Open%20Sans" in s for s in hdrs_str)


def test_no_font_when_not_specified():
    """Test that no font link is added when font_family is None."""
    app = FastHTML()

    add_bootstrap(app, theme="green-nature")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should not have Google Fonts link
    assert not any("fonts.googleapis.com" in s for s in hdrs_str)
