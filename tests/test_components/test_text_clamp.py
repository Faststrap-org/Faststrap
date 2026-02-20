"""Tests for TextClamp component."""

from fasthtml.common import to_xml

from faststrap.components.display import TextClamp


def test_text_clamp_short_text():
    html = to_xml(TextClamp("short", max_chars=20))
    assert "short" in html
    assert 'data-fs-text-clamp="true"' not in html


def test_text_clamp_expandable():
    html = to_xml(TextClamp("x" * 100, max_chars=10, show_more=True))
    assert 'data-fs-text-clamp="true"' in html
    assert 'data-fs-text-toggle="true"' in html
    assert "Show more" in html


def test_text_clamp_without_show_more():
    html = to_xml(TextClamp("x" * 100, max_chars=10, show_more=False))
    assert "..." in html
    assert 'data-fs-text-toggle="true"' not in html
