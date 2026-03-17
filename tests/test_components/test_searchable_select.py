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


def test_searchable_select_auto_id_is_deterministic():
    """Auto-generated select ID should be stable for same endpoint/name."""
    s1 = SearchableSelect(endpoint="/api/search", name="user_id")
    s2 = SearchableSelect(endpoint="/api/search", name="user_id")
    h1 = to_xml(s1)
    h2 = to_xml(s2)
    marker = 'id="searchable-select-'
    id1 = h1.split(marker, 1)[1].split('"', 1)[0]
    id2 = h2.split(marker, 1)[1].split('"', 1)[0]
    assert id1 == id2


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


def test_searchable_select_respects_min_chars():
    """Search input sets minlength when min_chars is provided."""
    select = SearchableSelect(endpoint="/api/search", name="test", min_chars=3)
    html = to_xml(select)

    assert 'minlength="3"' in html


def test_searchable_select_required_hidden_select():
    """Hidden select receives required attribute."""
    select = SearchableSelect(endpoint="/api/search", name="user_id", required=True)
    html = to_xml(select)

    assert 'required="True"' in html or "required" in html


def test_searchable_select_initial_options_wire_click_handler():
    """Initial options include click handler to update hidden select value."""
    select = SearchableSelect(
        endpoint="/api/search",
        name="user_id",
        select_id="user-select",
        initial_options=[("1", "Alice")],
    )
    html = to_xml(select)

    assert "hx-on:click" in html
    assert "user-select" in html


def test_searchable_select_escapes_user_supplied_select_id_in_js():
    """User-provided select_id should be safely escaped in click handler JavaScript."""
    select = SearchableSelect(
        endpoint="/api/search",
        name="user_id",
        select_id="x');alert(1);//",
        initial_options=[("1", "Alice")],
    )
    html = to_xml(select)

    assert "alert(1)" in html  # still present as data, but escaped in string literal
    assert 'getElementById("x&#39;);alert(1);//")' in html
    assert "getElementById('x');alert(1);//')" not in html


def test_searchable_select_csp_safe_avoids_inline_handlers():
    """CSP-safe mode should avoid hx-on-click inline handlers."""
    select = SearchableSelect(
        endpoint="/api/search",
        name="user_id",
        select_id="user-select",
        csp_safe=True,
        initial_options=[("1", "Alice")],
    )
    html = to_xml(select)
    assert "hx-on:click" not in html
    assert 'data-fs-searchable-select="true"' in html
    assert 'data-fs-searchable-option="true"' in html
    assert 'data-fs-value="1"' in html
