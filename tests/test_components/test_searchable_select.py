"""Tests for SearchableSelect component."""

from fasthtml.common import to_xml

from faststrap.components.forms import SearchableSelect


def test_searchable_select_basic():
    """SearchableSelect renders with basic settings."""
    select = SearchableSelect(endpoint="/api/search", name="user_id")
    html = to_xml(select)

    assert "/api/search" in html
    assert 'name="user_id"' in html
    assert "form-control" in html


def test_searchable_select_placeholder():
    """SearchableSelect shows custom placeholder."""
    select = SearchableSelect(
        endpoint="/api/search", name="country", placeholder="Search countries..."
    )
    html = to_xml(select)

    assert "Search countries..." in html


def test_searchable_select_initial_options():
    """SearchableSelect displays initial options."""
    select = SearchableSelect(
        endpoint="/api/users",
        name="user",
        initial_options=[
            ("1", "John Doe"),
            ("2", "Jane Smith"),
        ],
    )
    html = to_xml(select)

    assert "John Doe" in html
    assert "Jane Smith" in html


def test_searchable_select_debounce():
    """SearchableSelect supports custom debounce."""
    select = SearchableSelect(endpoint="/api/search", name="test", debounce=500)
    html = to_xml(select)

    assert "500" in html  # Debounce value in trigger


def test_searchable_select_htmx_attributes():
    """SearchableSelect has proper HTMX attributes."""
    select = SearchableSelect(endpoint="/api/search", name="test")
    html = to_xml(select)

    assert "hx-get" in html
    assert "hx-trigger" in html
    assert "hx-target" in html
    assert "hx-swap" in html


def test_searchable_select_custom_id():
    """SearchableSelect supports custom ID."""
    select = SearchableSelect(endpoint="/api/search", name="test", select_id="custom-select-id")
    html = to_xml(select)

    assert "custom-select-id" in html


def test_searchable_select_results_container():
    """SearchableSelect has results container."""
    select = SearchableSelect(endpoint="/api/search", name="test")
    html = to_xml(select)

    assert "list-group" in html
    assert "max-height" in html  # Scrollable results


def test_searchable_select_hidden_select():
    """SearchableSelect includes hidden select for form submission."""
    select = SearchableSelect(endpoint="/api/search", name="user_id")
    html = to_xml(select)

    assert 'name="user_id"' in html
    assert "d-none" in html  # Hidden select


def test_searchable_select_custom_classes():
    """SearchableSelect merges custom classes."""
    select = SearchableSelect(endpoint="/api/search", name="test", cls="custom-searchable")
    html = to_xml(select)

    assert "custom-searchable" in html
    assert "searchable-select" in html
