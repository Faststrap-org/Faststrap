"""Tests for SearchBar component."""

from fasthtml.common import to_xml

from faststrap.components.navigation.search_bar import SearchBar


def test_search_bar_renders_form() -> None:
    """SearchBar renders a div with a search input."""
    component = SearchBar("Find users...")
    html = to_xml(component)
    assert "<div" in html
    assert 'type="search"' in html
    assert 'placeholder="Find users..."' in html


def test_search_bar_default_name() -> None:
    """Default query parameter name is 'q'."""
    component = SearchBar()
    html = to_xml(component)
    assert 'name="q"' in html


def test_search_bar_custom_name() -> None:
    """Custom name parameter is applied."""
    component = SearchBar(name="query")
    html = to_xml(component)
    assert 'name="query"' in html


def test_search_bar_with_endpoint_adds_htmx() -> None:
    """When endpoint is provided, HTMX attributes are added."""
    component = SearchBar("Search", endpoint="/api/search", target="#results")
    html = to_xml(component)
    assert 'hx-get="/api/search"' in html
    assert 'hx-target="#results"' in html


def test_search_bar_merges_custom_classes() -> None:
    """Custom classes are merged."""
    component = SearchBar("Search", cls="my-search")
    html = to_xml(component)
    assert "faststrap-search-bar" in html
    assert "my-search" in html


def test_search_bar_autocomplete_default() -> None:
    """Default autocomplete is off."""
    component = SearchBar()
    html = to_xml(component)
    assert 'autocomplete="off"' in html


def test_search_bar_custom_autocomplete() -> None:
    """Custom autocomplete is applied."""
    component = SearchBar(autocomplete="on")
    html = to_xml(component)
    assert 'autocomplete="on"' in html
