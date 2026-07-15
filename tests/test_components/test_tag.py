"""Tests for Tag component."""

from fasthtml.common import to_xml

from faststrap.components.display import Tag


def test_tag_basic():
    """Tag renders with basic content."""
    tag = Tag("Python")
    html = to_xml(tag)

    assert "Python" in html
    assert "badge" in html


def test_tag_variant():
    """Tag supports color variants."""
    tag = Tag("Success", variant="success")
    html = to_xml(tag)

    assert "text-bg-success" in html


def test_tag_all_variants():
    """Tag supports all standard variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info"]

    for variant in variants:
        tag = Tag("Test", variant=variant)
        html = to_xml(tag)
        assert f"text-bg-{variant}" in html


def test_tag_size_sm():
    """Tag supports small size."""
    tag = Tag("Small", size="sm")
    html = to_xml(tag)

    assert "badge-sm" in html


def test_tag_size_md():
    """Tag defaults to medium size."""
    tag = Tag("Medium")
    html = to_xml(tag)

    assert "px-2" in html
    assert "py-1" in html


def test_tag_removable():
    """Tag shows close button when removable."""
    tag = Tag("Removable", removable=True)
    html = to_xml(tag)

    assert "btn-close" in html
    assert "Remove" in html


def test_tag_not_removable_by_default():
    """Tag does not show close button by default."""
    tag = Tag("Static")
    html = to_xml(tag)

    assert "btn-close" not in html


def test_tag_with_icon():
    """Tag supports leading icon."""
    tag = Tag("Java", icon="code-s-slash")
    html = to_xml(tag)

    assert "code-s-slash" in html
    assert "Java" in html


def test_tag_custom_classes():
    """Tag merges custom classes."""
    tag = Tag("Custom", cls="ms-2")
    html = to_xml(tag)

    assert "ms-2" in html


def test_tag_htmx():
    """Tag supports HTMX attributes."""
    tag = Tag("Filter", hx_get="/filter?tag=python")
    html = to_xml(tag)

    assert 'hx-get="/filter?tag=python"' in html


def test_tag_data_attributes():
    """Tag handles data attributes."""
    tag = Tag("Tag", data_id="42")
    html = to_xml(tag)

    assert 'data-id="42"' in html


def test_tag_removable_with_on_remove():
    """Tag removable with HTMX on_remove attribute."""
    tag = Tag("Closeable", removable=True, on_remove="hx-delete='/tags/1'")
    html = to_xml(tag)

    assert "btn-close" in html
    assert 'hx-delete="/tags/1"' in html
