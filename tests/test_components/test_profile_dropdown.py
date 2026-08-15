"""Tests for ProfileDropdown component."""

from fasthtml.common import to_xml

from faststrap.components.navigation.profile_dropdown import ProfileDropdown


def test_profile_dropdown_renders_container() -> None:
    """ProfileDropdown renders a div with dropdown structure."""
    component = ProfileDropdown("Alice")
    html = to_xml(component)
    assert "<div" in html
    assert "dropdown-toggle" in html
    assert "Alice" in html


def test_profile_dropdown_with_subtitle() -> None:
    """Subtitle is rendered in the toggle area."""
    component = ProfileDropdown("Alice", subtitle="Admin")
    html = to_xml(component)
    assert "Admin" in html
    assert "text-muted" in html


def test_profile_dropdown_with_items() -> None:
    """Menu items are rendered as dropdown items."""
    component = ProfileDropdown(
        "Alice",
        items=[("Profile", "/profile"), ("Settings", "/settings"), ("Sign out", "/logout")],
    )
    html = to_xml(component)
    assert "Profile" in html
    assert "Settings" in html
    assert "Sign out" in html
    assert "/profile" in html
    assert "/settings" in html
    assert "/logout" in html


def test_profile_dropdown_without_items() -> None:
    """Without items, only toggle is rendered."""
    component = ProfileDropdown("Alice")
    html = to_xml(component)
    assert "dropdown-toggle" in html
    assert "dropdown-menu" not in html


def test_profile_dropdown_avatar_initials() -> None:
    """Without src, initials are shown in avatar circle."""
    component = ProfileDropdown("Alice Smith")
    html = to_xml(component)
    assert "AS" in html
    assert "rounded-circle" in html


def test_profile_dropdown_alignment_end() -> None:
    """Default alignment is end."""
    component = ProfileDropdown("Alice", items=[("Profile", "/profile")])
    html = to_xml(component)
    assert "dropdown-menu-end" in html


def test_profile_dropdown_alignment_start() -> None:
    """Custom alignment is applied."""
    component = ProfileDropdown("Alice", items=[("Profile", "/profile")], alignment="start")
    html = to_xml(component)
    assert "dropdown-menu-start" in html


def test_profile_dropdown_merges_custom_classes() -> None:
    """Custom classes are merged."""
    component = ProfileDropdown("Alice", cls="my-profile")
    html = to_xml(component)
    assert "faststrap-profile-dropdown" in html
    assert "my-profile" in html


def test_profile_dropdown_sets_data_attributes() -> None:
    """When items are provided, data attribute is set."""
    component = ProfileDropdown("Alice", items=[("Profile", "/profile")])
    html = to_xml(component)
    assert 'data-fs-items="true"' in html
