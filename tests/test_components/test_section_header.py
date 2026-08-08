"""Tests for SectionHeader component."""

from fasthtml.common import to_xml

from faststrap.components.layout import SectionHeader


def test_section_header_basic():
    """SectionHeader renders title and section classes."""
    html = to_xml(SectionHeader("Users"))

    assert "Users" in html
    assert "mb-3" in html


def test_section_header_with_subtitle():
    """SectionHeader renders subtitle when provided."""
    html = to_xml(SectionHeader("Users", subtitle="Manage team members"))

    assert "Users" in html
    assert "Manage team members" in html
    assert "text-muted" in html


def test_section_header_with_eyebrow():
    """SectionHeader renders eyebrow label when provided."""
    html = to_xml(SectionHeader("Users", eyebrow="Admin"))

    assert "Users" in html
    assert "Admin" in html
    assert "text-uppercase" in html


def test_section_header_with_badge():
    """SectionHeader renders badge beside title when provided."""
    from faststrap import Badge

    html = to_xml(SectionHeader("Users", badge=Badge("New")))

    assert "Users" in html
    assert "New" in html
    assert "ms-2" in html


def test_section_header_with_actions():
    """SectionHeader renders action buttons when provided."""
    from faststrap import Button

    html = to_xml(
        SectionHeader(
            "Users",
            actions=[Button("Add user", variant="primary")],
        )
    )

    assert "Users" in html
    assert "Add user" in html
    assert "d-flex" in html


def test_section_header_size_sm_uses_h3():
    """SectionHeader with size='sm' uses h3."""
    html = to_xml(SectionHeader("Users", size="sm"))

    assert "Users" in html
    assert "<h3" in html


def test_section_header_size_md_uses_h2():
    """SectionHeader with size='md' uses h2."""
    html = to_xml(SectionHeader("Users", size="md"))

    assert "Users" in html
    assert "<h2" in html


def test_section_header_custom_classes():
    """SectionHeader merges custom classes."""
    html = to_xml(SectionHeader("Users", cls="mt-4"))

    assert "mt-4" in html
    assert "mb-3" in html
