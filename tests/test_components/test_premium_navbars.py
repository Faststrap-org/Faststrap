"""Tests for premium navbar components."""

from fasthtml.common import to_xml

from faststrap import GlassNavbar, GlassNavItem, SidebarNavbar, SidebarNavItem

# SidebarNavbar Tests


def test_sidebar_navbar_basic():
    """Test basic sidebar navbar creation."""
    nav = SidebarNavbar(("Home", "/"), ("About", "/about"), brand="Test App")
    html = to_xml(nav)
    assert "sidebar-navbar" in html
    assert "Test App" in html


def test_sidebar_navbar_with_icons():
    """Test sidebar with icons."""
    nav = SidebarNavbar(
        ("Dashboard", "/dashboard", "house"), ("Users", "/users", "people"), brand="Admin"
    )
    html = to_xml(nav)
    assert "sidebar-navbar" in html
    assert "bi-house" in html or "house" in html


def test_sidebar_navbar_theme_dark():
    """Test dark theme sidebar."""
    nav = SidebarNavbar(("Home", "/"), theme="dark")
    html = to_xml(nav)
    assert "bg-dark" in html or "text-white" in html


def test_sidebar_navbar_theme_light():
    """Test light theme sidebar."""
    nav = SidebarNavbar(("Home", "/"), theme="light")
    html = to_xml(nav)
    assert "bg-light" in html or "border-end" in html


def test_sidebar_navbar_position():
    """Test sidebar position."""
    nav_left = SidebarNavbar(("Home", "/"), position="left")
    nav_right = SidebarNavbar(("Home", "/"), position="right")

    assert "sidebar-navbar" in to_xml(nav_left)
    assert "sidebar-right" in to_xml(nav_right)


def test_sidebar_navbar_width():
    """Test custom width."""
    nav = SidebarNavbar(("Home", "/"), width="300px")
    html = to_xml(nav).replace(": ", ":")
    assert "width:300px" in html


def test_sidebar_navbar_sticky():
    """Test sticky sidebar."""
    nav = SidebarNavbar(("Home", "/"), sticky=True)
    html = to_xml(nav)
    assert "sticky-top" in html


def test_sidebar_nav_item():
    """Test sidebar nav item."""
    item = SidebarNavItem("Dashboard", href="/dashboard", icon="house", active=True)
    html = to_xml(item)
    assert "nav-link" in html
    assert "active" in html
    assert "Dashboard" in html


# GlassNavbar Tests


def test_glass_navbar_basic():
    """Test basic glass navbar creation."""
    nav = GlassNavbar(("Home", "/"), ("About", "/about"), brand="Glass App")
    html = to_xml(nav)
    assert "navbar" in html
    assert "Glass App" in html
    assert "backdrop-filter" in html


def test_glass_navbar_blur_strength():
    """Test blur strength options."""
    nav_low = GlassNavbar(("Home", "/"), blur_strength="low")
    nav_med = GlassNavbar(("Home", "/"), blur_strength="medium")
    nav_high = GlassNavbar(("Home", "/"), blur_strength="high")

    # Check styles (robust to spacing)
    assert "backdrop-filter:blur(5px)" in to_xml(nav_low).replace(": ", ":")
    assert "backdrop-filter:blur(10px)" in to_xml(nav_med).replace(": ", ":")
    assert "backdrop-filter:blur(20px)" in to_xml(nav_high).replace(": ", ":")


def test_glass_navbar_transparency():
    """Test transparency setting."""
    nav = GlassNavbar(("Home", "/"), transparency=0.9, theme="light")
    html = to_xml(nav).replace(", ", ",")  # Remove space in rgba
    assert "rgba(255,255,255,0.9)" in html


def test_glass_navbar_theme_dark():
    """Test dark theme glass navbar."""
    nav = GlassNavbar(("Home", "/"), theme="dark")
    html = to_xml(nav).replace(", ", ",")
    assert "navbar-dark" in html
    assert "rgba(0,0,0," in html


def test_glass_navbar_theme_light():
    """Test light theme glass navbar."""
    nav = GlassNavbar(("Home", "/"), theme="light")
    html = to_xml(nav).replace(", ", ",")
    assert "navbar-light" in html
    assert "rgba(255,255,255," in html


def test_glass_navbar_sticky():
    """Test sticky glass navbar."""
    nav = GlassNavbar(("Home", "/"), sticky=True)
    html = to_xml(nav)
    assert "sticky-top" in html


def test_glass_navbar_expand():
    """Test responsive breakpoint."""
    nav = GlassNavbar(("Home", "/"), expand="md")
    html = to_xml(nav)
    assert "navbar-expand-md" in html


def test_glass_nav_item():
    """Test glass nav item."""
    item = GlassNavItem("Home", href="/", active=True)
    html = to_xml(item)
    assert "nav-link" in html
    assert "active" in html
    assert "Home" in html


def test_glass_navbar_with_items():
    """Test glass navbar with tuple items."""
    nav = GlassNavbar(("Home", "/", True), ("About", "/about", False), brand="App")  # active
    html = to_xml(nav)
    assert "navbar" in html
    assert "Home" in html
    assert "About" in html
