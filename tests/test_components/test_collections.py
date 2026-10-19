"""Tests for responsive collection primitives and DataTable card mode."""

import pytest
from fasthtml.common import Button, Div, Span, Strong, to_xml

from faststrap import CollectionView, DataTable, GridList, ListItem, ListView, ViewToggle
from faststrap.core.registry import list_components


def test_list_item_supports_mobile_style_slots_and_link_state() -> None:
    html = to_xml(
        ListItem(
            title="Ada Lovelace",
            subtitle="Mathematics",
            meta="Active now",
            leading="AL",
            trailing=Button("Open", size="sm"),
            href="/people/ada",
            selected=True,
            lines=3,
        )
    )
    assert 'href="/people/ada"' in html
    assert "faststrap-list-item-title" in html
    assert "faststrap-list-item-subtitle" in html
    assert "faststrap-list-item-meta" in html
    assert 'aria-current="true"' in html


def test_list_item_active_and_loading_states_are_visible_and_non_navigable() -> None:
    active = to_xml(ListItem(title="Current page", href="/current", active=True))
    loading = to_xml(ListItem(title="Saving", href="/save", loading=True))
    assert 'aria-current="page"' in active
    assert "faststrap-list-item-active" in active
    assert 'aria-busy="true"' in loading
    assert "spinner-border" in loading
    assert 'href="/save"' not in loading


def test_list_and_grid_views_expose_customization_surface() -> None:
    list_html = to_xml(ListView(ListItem("One"), density="compact", divided=False, label="Files"))
    grid_html = to_xml(GridList("One", "Two", min_width="12rem", columns=2, gap=4))
    assert "faststrap-list-view-compact" in list_html
    assert 'aria-label="Files"' in list_html
    assert 'role="listitem"' in list_html
    assert list_html.count('role="listitem"') == 1
    assert "faststrap-grid-list" in grid_html
    assert 'role="listitem" class="faststrap-grid-list-item"' in grid_html
    assert "--fs-grid-columns: 2" in grid_html
    assert "--fs-grid-gap: 1.0rem" in grid_html


def test_collection_view_selects_grid_or_compact_list() -> None:
    grid_html = to_xml(CollectionView("One", mode="grid", grid_columns=3))
    compact_html = to_xml(CollectionView(ListItem("One"), mode="compact"))
    assert "faststrap-collection-view-grid" in grid_html
    assert "--fs-grid-columns: 3" in grid_html
    assert "faststrap-collection-view-compact" in compact_html
    assert "faststrap-list-view-compact" in compact_html


def test_collection_view_renders_records_with_mode_specific_renderer() -> None:
    records = [{"name": "Report", "kind": "PDF"}]
    list_html = to_xml(
        CollectionView(
            records=records,
            mode="list",
            list_renderer=lambda row: ListItem(title=row["name"], meta=row["kind"]),
        )
    )
    card_html = to_xml(
        CollectionView(
            records=records,
            mode="grid",
            card_renderer=lambda row: Div(row["name"], cls="file-card"),
        )
    )
    assert "Report" in list_html and "PDF" in list_html
    assert 'class="file-card"' in card_html


def test_collection_view_rejects_ambiguous_or_missing_record_renderers() -> None:
    with pytest.raises(ValueError, match="list_renderer is required"):
        CollectionView(records=[{"name": "Report"}])
    with pytest.raises(ValueError, match="not both"):
        CollectionView(
            ListItem("Already rendered"),
            records=[{"name": "Report"}],
            list_renderer=lambda row: row,
        )


def test_collection_views_support_loading_and_empty_content() -> None:
    loading = to_xml(ListView(loading=True, loading_content="Loading users"))
    empty = to_xml(GridList(empty="No files found"))
    assert 'role="status"' in loading and "Loading users" in loading
    assert 'role="status"' in empty and "No files found" in empty


def test_view_toggle_supports_link_and_application_owned_modes() -> None:
    link_html = to_xml(ViewToggle(value="grid", endpoint="/files?folder=reports"))
    local_html = to_xml(ViewToggle(value="list"))
    assert 'href="/files?folder=reports&amp;view=grid"' in link_html
    assert 'aria-current="true"' in link_html
    assert 'data-fs-view="list"' in local_html
    assert 'aria-pressed="true"' in local_html


def test_data_table_renders_table_and_cards_in_card_mode() -> None:
    html = to_xml(
        DataTable(
            [{"name": "Q3 report", "owner": "Finance", "size": "2.4 MB", "id": "internal"}],
            columns=["name", "owner", "size", "id"],
            header_map={"name": "File", "owner": "Owner", "size": "Size"},
            mobile_mode="cards",
            mobile_title="name",
            mobile_subtitle="owner",
            mobile_meta=["size", "id"],
            mobile_hidden=["id"],
            mobile_breakpoint="lg",
            mobile_card_cls="shadow-sm",
        )
    )
    assert "d-none d-lg-block" in html
    assert "d-lg-none" in html
    assert "faststrap-data-table-card" in html
    assert "shadow-sm" in html
    assert "File" in html and "Size" in html
    assert 'faststrap-data-table-card-label">id<' not in html


def test_data_table_stack_mode_and_custom_mobile_renderers() -> None:
    html = to_xml(
        DataTable(
            [{"name": "Ada", "status": "active", "score": 98}],
            mobile_mode="stack",
            mobile_title="name",
            mobile_meta=["status", "score"],
            mobile_field_renderers={
                "status": lambda value, row: Span(value.title(), cls="badge bg-success"),
                "score": lambda value, row: Strong(f"{value}%"),
            },
        )
    )
    assert "faststrap-data-table-stack" in html
    assert "badge bg-success" in html and "Active" in html
    assert "98%" in html


def test_data_table_custom_mobile_card_renderer_receives_row() -> None:
    html = to_xml(
        DataTable(
            [{"name": "Ada", "status": "active"}],
            mobile_mode="cards",
            mobile_card_renderer=lambda row: Div(
                Button(f"Open {row['name']}", hx_get=f"/people/{row['name']}"),
                row["status"],
            ),
            mobile_card_cls="custom-record-card",
            mobile_card_attrs={"data-testid": "person-card"},
        )
    )
    assert "custom-record-card" in html
    assert 'data-testid="person-card"' in html
    assert 'hx-get="/people/Ada"' in html


def test_data_table_mobile_renderer_uses_current_paginated_rows_and_wrapper_target() -> None:
    html = to_xml(
        DataTable(
            # In endpoint mode the route supplies the current page's rows.
            [{"name": "Second"}],
            pagination=True,
            page=2,
            per_page=1,
            total_rows=2,
            endpoint="/records",
            table_id="records-table",
            hx_target="#records-table",
            mobile_mode="cards",
            mobile_card_renderer=lambda row: Div(row["name"]),
        )
    )
    assert 'id="records-table"' in html
    assert "Second" in html
    assert "First" not in html
    assert 'hx-target="#records-table"' in html


def test_data_table_mobile_hidden_excludes_title_and_subtitle_from_cards() -> None:
    html = to_xml(
        DataTable(
            [{"name": "Private report", "owner": "Finance", "size": "2.4 MB"}],
            mobile_mode="cards",
            mobile_title="name",
            mobile_subtitle="owner",
            mobile_hidden=["name", "owner"],
        )
    )
    card_html = html.split('class="d-md-none"', maxsplit=1)[1]
    assert "Private report" not in card_html
    assert "Finance" not in card_html


def test_data_table_none_mobile_mode_uses_only_the_configured_table() -> None:
    html = to_xml(DataTable([{"name": "Ada"}], mobile_mode=None))
    assert "faststrap-data-table-card" not in html
    assert "<table" in html


@pytest.mark.parametrize(
    "factory",
    [
        lambda: ListItem("x", density="roomy"),
        lambda: GridList("x", columns=0),
        lambda: CollectionView("x", mode="table"),
        lambda: ViewToggle(value="cards", options=("list", "grid")),
        lambda: DataTable([], mobile_mode="grid"),
        lambda: DataTable([], mobile_breakpoint="phone"),
    ],
)
def test_collection_components_validate_public_options(factory) -> None:
    with pytest.raises(ValueError):
        factory()


def test_collection_components_are_registered() -> None:
    registered = set(list_components())
    assert registered.issuperset(
        {"ListItem", "ListView", "GridList", "CollectionView", "ViewToggle"}
    )
