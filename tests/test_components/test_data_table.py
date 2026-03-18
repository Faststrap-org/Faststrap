"""Tests for DataTable component."""

from fasthtml.common import to_xml

from faststrap import DataTable


def test_data_table_renders_sortable_headers_and_pagination():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]

    table = DataTable(
        data,
        sortable=True,
        sort="name",
        direction="asc",
        pagination=True,
        page=1,
        per_page=1,
        total_rows=2,
        endpoint="/users",
    )
    html = to_xml(table)

    assert 'aria-sort="ascending"' in html
    assert "sort=name" in html
    assert "direction=desc" in html
    assert "page=2" in html


def test_data_table_search_input():
    data = [{"name": "Alice"}]
    table = DataTable(
        data,
        searchable=True,
        search="al",
        endpoint="/users",
    )
    html = to_xml(table)

    assert 'type="search"' in html
    assert 'name="q"' in html
    assert 'value="al"' in html


def test_data_table_local_sort_and_search_apply_to_rendered_rows():
    data = [
        {"name": "Bob", "team": "Operations"},
        {"name": "Alice", "team": "Engineering"},
    ]

    sorted_html = to_xml(DataTable(data, sortable=True, sort="name", direction="asc"))
    assert sorted_html.index("Alice") < sorted_html.index("Bob")

    filtered_html = to_xml(DataTable(data, searchable=True, search="oper"))
    assert "Bob" in filtered_html
    assert "Alice" not in filtered_html


def test_data_table_base_url_search_form_and_unsorted_aria_sort():
    html = to_xml(
        DataTable(
            [{"name": "Alice"}],
            sortable=True,
            searchable=True,
            base_url="/users",
            filters={"team": "ops"},
            pagination=True,
            per_page=10,
        )
    )

    assert 'method="get"' in html
    assert 'action="/users"' in html
    assert 'name="team"' in html
    assert 'value="ops"' in html
    assert 'name="page"' in html
    assert 'value="1"' in html
    assert 'aria-sort="' not in html


def test_data_table_include_index_tracks_paginated_slice():
    html = to_xml(
        DataTable(
            [{"name": "A"}, {"name": "B"}, {"name": "C"}],
            include_index=True,
            pagination=True,
            page=2,
            per_page=1,
        )
    )

    assert '<th scope="row">1</th>' in html
    assert '<th scope="row">0</th>' not in html


def test_data_table_export_params_helper():
    params = DataTable.export_params(
        sort="name",
        direction="desc",
        search="al",
        filters={"team": "ops", "active": True, "empty": None},
        include_pagination=True,
        page=2,
        per_page=50,
    )
    assert params["sort"] == "name"
    assert params["direction"] == "desc"
    assert params["q"] == "al"
    assert params["team"] == "ops"
    assert params["active"] == "true"
    assert "empty" not in params
    assert params["page"] == 2
    assert params["per_page"] == 50
