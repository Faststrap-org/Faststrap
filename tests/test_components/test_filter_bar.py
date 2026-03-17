"""Tests for FilterBar component."""

from fasthtml.common import to_xml

from faststrap import FilterBar, Input, Select


def test_filter_bar_auto_mode():
    bar = FilterBar(
        Input("q", placeholder="Search"),
        Select("status", options=[("Active", "active"), ("Paused", "paused")]),
        endpoint="/filters",
        mode="auto",
        hx_target="#results",
    )
    html = to_xml(bar)

    assert "faststrap-filter-bar" in html
    assert 'hx-get="/filters"' in html
    assert 'hx-target="#results"' in html
    assert "hx-trigger" in html


def test_filter_bar_apply_mode_buttons():
    bar = FilterBar(
        Input("q"),
        endpoint="/filters",
        mode="apply",
        apply_label="Apply Filters",
        reset_label="Reset",
        reset_href="/filters",
    )
    html = to_xml(bar)

    assert "Apply Filters" in html
    assert "Reset" in html
