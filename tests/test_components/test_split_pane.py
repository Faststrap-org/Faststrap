"""Tests for SplitPane layout component."""

from fasthtml.common import Div, to_xml

from faststrap.components.layout.split_pane import SplitPane


def test_split_pane_renders_container() -> None:
    """SplitPane renders a wrapper div with left, divider, and right."""
    component = SplitPane(Div("Left"), Div("Right"))
    html = to_xml(component)
    assert "<div" in html
    assert "Left" in html
    assert "Right" in html


def test_split_pane_default_ratio() -> None:
    """Default initial_ratio is 30/70."""
    component = SplitPane(Div("L"), Div("R"))
    html = to_xml(component)
    assert 'data-fs-split-ratio="30/70"' in html


def test_split_pane_custom_ratio() -> None:
    """Custom ratio is stored in data attribute and reflected in style."""
    component = SplitPane(Div("L"), Div("R"), initial_ratio="40/60")
    html = to_xml(component)
    assert 'data-fs-split-ratio="40/60"' in html


def test_split_pane_divider_width() -> None:
    """Divider width is stored as data attribute."""
    component = SplitPane(Div("L"), Div("R"), divider_width="6px")
    html = to_xml(component)
    assert 'data-fs-split-divider-width="6px"' in html


def test_split_pane_min_max_left() -> None:
    """Min and max left widths are stored as data attributes."""
    component = SplitPane(
        Div("L"),
        Div("R"),
        min_left="300px",
        max_left="60%",
    )
    html = to_xml(component)
    assert 'data-fs-split-min-left="300px"' in html
    assert 'data-fs-split-max-left="60%"' in html


def test_split_pane_collapsible() -> None:
    """Collapsible flag sets data attribute."""
    component = SplitPane(Div("L"), Div("R"), collapsible=True)
    html = to_xml(component)
    assert 'data-fs-split-collapsible="true"' in html


def test_split_pane_collapsed() -> None:
    """Collapsed flag sets data attribute."""
    component = SplitPane(Div("L"), Div("R"), collapsed=True)
    html = to_xml(component)
    assert 'data-fs-split-collapsed="true"' in html


def test_split_pane_invalid_breakpoint_raises() -> None:
    """Invalid breakpoint raises ValueError."""
    try:
        SplitPane(Div("L"), Div("R"), stack_on="invalid")
    except ValueError as exc:
        assert "Invalid breakpoint" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid breakpoint")


def test_split_pane_no_stack() -> None:
    """stack_on=None disables responsive stacking."""
    component = SplitPane(Div("L"), Div("R"), stack_on=None)
    html = to_xml(component)
    assert "flex-md-row" not in html


def test_split_pane_merges_custom_classes() -> None:
    """Custom classes are merged with base classes."""
    component = SplitPane(Div("L"), Div("R"), cls="my-split")
    html = to_xml(component)
    assert "faststrap-split-pane" in html
    assert "my-split" in html
