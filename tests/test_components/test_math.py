"""Tests for Math component."""

from fasthtml.common import to_xml

from faststrap.components.display.math import Math


def test_math_inline_renders_span() -> None:
    """Inline math renders a span with delimited LaTeX."""
    component = Math(r"\frac{a}{b}")
    html = to_xml(component)
    assert "<span" in html
    assert 'class="math faststrap-math"' in html
    assert r"\(\frac{a}{b}\)" in html
    assert 'data-fs-math-display="false"' in html


def test_math_display_mode_renders_div() -> None:
    """Display math renders a div with display-mode classes."""
    component = Math(r"\int x dx", display_mode=True)
    html = to_xml(component)
    assert "<div" in html
    assert "faststrap-math-display" in html
    assert r"$$\int x dx$$" in html
    assert 'data-fs-math-display="true"' in html


def test_math_throw_on_error_attribute() -> None:
    """throw_on_error=True sets the corresponding data attribute."""
    component = Math(r"\unknown", throw_on_error=True)
    html = to_xml(component)
    assert 'data-fs-math-throw-on-error="true"' in html


def test_math_merges_custom_classes() -> None:
    """Custom classes are merged with base math classes."""
    component = Math(r"E=mc^2", cls="mt-3 text-center")
    html = to_xml(component)
    assert "math faststrap-math mt-3 text-center" in html


def test_math_unsupported_renderer_raises() -> None:
    """Unsupported renderer raises ValueError."""
    try:
        Math(r"x", renderer="mathjax")
    except ValueError as exc:
        assert "Unsupported math renderer" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported renderer")


def test_math_chemistry_mhchem() -> None:
    """Chemistry formulas with mhchem syntax are preserved."""
    component = Math(r"\ce{2H2 + O2 -> 2H2O}")
    html = to_xml(component)
    assert r"\ce{2H2 + O2 -> 2H2O}" in html


def test_math_preserves_additional_attributes() -> None:
    """Additional kwargs are converted to HTML attributes."""
    component = Math(r"x", id="formula-1", data_topic="algebra")
    html = to_xml(component)
    assert 'id="formula-1"' in html
    assert 'data-topic="algebra"' in html


def test_math_display_mode_defaults_to_false() -> None:
    """Display mode is off by default for inline math."""
    component = Math(r"x^2")
    html = to_xml(component)
    assert 'data-fs-math-display="false"' in html
    assert "<span" in html


def test_math_theme_default_resolution() -> None:
    """resolve_defaults integration works for Math."""
    from faststrap.core.theme import reset_component_defaults, set_component_defaults

    set_component_defaults("Math", display_mode=True, throw_on_error=True)
    try:
        component = Math(r"x")
        html = to_xml(component)
        assert 'data-fs-math-display="true"' in html
        assert 'data-fs-math-throw-on-error="true"' in html
    finally:
        reset_component_defaults("Math")
