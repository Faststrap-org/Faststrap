"""Tests for Switcher layout component."""

from fasthtml.common import to_xml

from faststrap.components.layout.switcher import Switcher


def test_switcher_renders_container() -> None:
    """Switcher renders a div with children."""
    from fasthtml.common import Div

    child = Div("Panel A")
    component = Switcher(child, child)
    html = to_xml(component)
    assert "<div" in html
    assert "Panel A" in html


def test_switcher_defaults_to_md_breakpoint() -> None:
    """Default breakpoint is md."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"))
    html = to_xml(component)
    assert "flex-md-row" in html


def test_switcher_uses_flex_column_by_default() -> None:
    """Without ratio, switcher stacks on mobile via flex-column."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"))
    html = to_xml(component)
    assert "flex-column" in html


def test_switcher_respects_custom_breakpoint() -> None:
    """Custom breakpoint is reflected in responsive classes."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"), breakpoint="lg")
    html = to_xml(component)
    assert "flex-lg-row" in html


def test_switcher_grid_mode_with_ratio() -> None:
    """When ratio is provided, switcher uses CSS grid."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"), ratio="1fr 2fr")
    html = to_xml(component)
    assert "faststrap-switcher-grid" in html
    assert "grid-template-columns: 1fr 2fr" in html


def test_switcher_grid_mode_min_item_width() -> None:
    """min_item_width adds grid-auto-columns style."""
    from fasthtml.common import Div

    component = Switcher(
        Div("A"), ratio="repeat(auto-fit, minmax(200px, 1fr))", min_item_width="200px"
    )
    html = to_xml(component)
    assert "grid-auto-columns: 200px" in html


def test_switcher_merges_custom_classes() -> None:
    """Custom classes are merged with base switcher classes."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), cls="my-custom-class")
    html = to_xml(component)
    assert "faststrap-switcher" in html
    assert "my-custom-class" in html


def test_switcher_custom_gap_int() -> None:
    """Integer gap renders as Bootstrap gap utility."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"), gap=4)
    html = to_xml(component)
    assert "gap-4" in html


def test_switcher_custom_gap_string() -> None:
    """String gap is appended as-is when ratio is set."""
    from fasthtml.common import Div

    component = Switcher(Div("A"), Div("B"), ratio="1fr 1fr", gap="my-gap")
    html = to_xml(component)
    assert "my-gap" in html
