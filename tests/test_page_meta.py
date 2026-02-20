"""Tests for PageMeta helper."""

from faststrap import PageMeta


def test_page_meta_generates_core_tags():
    tags = PageMeta(
        title="My Page",
        description="Desc",
        canonical="https://example.com/page",
        image="https://example.com/og.png",
    )
    html = "".join(str(t) for t in tags)
    assert "<title>My Page</title>" in html
    assert 'name="description"' in html
    assert 'rel="canonical"' in html
    assert 'property="og:image"' in html


def test_page_meta_dedupes_canonical():
    tags = PageMeta(url="https://a.com", canonical="https://b.com")
    html = "".join(str(t) for t in tags)
    assert html.count('rel="canonical"') == 1
