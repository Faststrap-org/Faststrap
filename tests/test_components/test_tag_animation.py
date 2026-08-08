"""Tests for Tag animation data attribute."""

from fasthtml.common import to_xml

from faststrap.components.display import Tag


def test_tag_renders_data_fs_tag_attribute():
    """Tag renders data-fs-tag attribute for JS initialization."""
    tag = Tag("Python")
    html = to_xml(tag)

    assert 'data-fs-tag="true"' in html


def test_tag_removable_has_data_attribute():
    """Removable Tag still renders data-fs-tag."""
    tag = Tag("Python", removable=True)
    html = to_xml(tag)

    assert 'data-fs-tag="true"' in html
    assert "btn-close" in html
