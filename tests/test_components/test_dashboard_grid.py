"""Tests for DashboardGrid component."""

from fasthtml.common import Div, to_xml

from faststrap.components.layout import DashboardGrid


def test_dashboard_grid_basic_styles():
    grid = DashboardGrid(Div("A"), cols=3, gap=2, dense=True, cls="custom")
    html = to_xml(grid)

    assert "faststrap-dashboard-grid" in html
    assert "custom" in html
    assert "grid-template-columns: repeat(3" in html
    assert "gap: 2rem" in html
    assert "grid-auto-flow: dense" in html


def test_dashboard_grid_auto_fit():
    grid = DashboardGrid(Div("A"), min_card_width=320)
    html = to_xml(grid)

    assert "auto-fit" in html
    assert "minmax(320px" in html
