"""Tests for BottomNav components."""

from fasthtml.common import to_xml

from faststrap.components.navigation import BottomNav, BottomNavItem


def test_bottom_nav_basic_render() -> None:
    nav = BottomNav(
        BottomNavItem("Home", href="/", icon="house", active=True),
        BottomNavItem("Profile", href="/profile", icon="person"),
    )
    html = to_xml(nav)
    assert "navbar-bottom" in html
    assert "fixed-bottom" in html
    assert "border-top" in html
    assert 'aria-current="page"' in html


def test_bottom_nav_accepts_string_style() -> None:
    nav = BottomNav(BottomNavItem("Home"), style="margin-top: 1rem;")
    html = to_xml(nav)
    assert "padding-bottom: 0" in html
    assert "padding-bottom: env(safe-area-inset-bottom, 0px)" in html
    assert "margin-top: 1rem" in html
