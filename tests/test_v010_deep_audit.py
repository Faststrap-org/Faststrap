"""Comprehensive v0.10.0 deep audit test suite.

Tests every new/updated v0.10.0 component with parameter permutations,
asserting semantic tags, ARIA attributes, clean XML rendering without
duplicate/conflicting attributes, and integration behavior.
"""

from __future__ import annotations

from pathlib import Path
from typing import get_type_hints

import pytest
from fasthtml.common import H1, A, Button, Div, Span, Strong, to_xml
from fasthtml.core import FT

from faststrap import (
    Chip,
    ChipGroup,
    CollectionView,
    DataTable,
    EmptyState,
    GridList,
    ListItem,
    ListView,
    MobileAppShell,
    MobileToolbar,
    SafeArea,
    SegmentedControl,
    Snackbar,
    StickyActionBar,
    Tag,
    ViewToggle,
)
from faststrap.components.display.tag import Chip as ChipComponent

# ==============================================================================
# Category A: Semantic HTML Tag & Attribute Correctness
# ==============================================================================


class TestSemanticHTMLAndAttributes:
    """Audit semantic HTML tags, attribute clashing, and ARIA attributes."""

    def test_chip_tag_selection_href_renders_anchor(self) -> None:
        """When href is supplied, Chip should render an <a> tag."""
        chip = Chip("Link Chip", href="/dest")
        assert chip.tag == "a"
        xml = to_xml(chip)
        assert xml.startswith("<a ")
        assert 'href="/dest"' in xml
        assert "data-fs-chip" in xml

    def test_chip_tag_selection_type_renders_button(self) -> None:
        """When type is supplied, Chip should render a <button> tag."""
        chip = Chip("Button Chip", type="button")
        assert chip.tag == "button"
        xml = to_xml(chip)
        assert xml.startswith("<button ")
        assert 'type="button"' in xml

    def test_chip_tag_selection_default_renders_span(self) -> None:
        """When neither href nor type is supplied, Chip should render a <span> tag."""
        chip = Chip("Plain Chip")
        assert chip.tag == "span"
        xml = to_xml(chip)
        assert xml.startswith("<span ")

    def test_chip_handles_htmx_attributes(self) -> None:
        """Chip must cleanly accept HTMX attributes like hx_get, hx_post, hx_target."""
        chip = Chip("HTMX Chip", hx_get="/api/filter", hx_target="#target", hx_swap="outerHTML")
        xml = to_xml(chip)
        assert chip.tag == "button"
        assert xml.startswith("<button ")
        assert 'type="button"' in xml
        assert 'hx-get="/api/filter"' in xml
        assert 'hx-target="#target"' in xml
        assert 'hx-swap="outerHTML"' in xml

    @pytest.mark.parametrize(
        "kwargs",
        [
            {"href": "/remove", "removable": True},
            {"type": "button", "removable": True},
            {"hx_post": "/remove", "removable": True},
        ],
    )
    def test_removable_chip_rejects_nested_action_semantics(self, kwargs: dict) -> None:
        with pytest.raises(ValueError, match="removable chips cannot"):
            Chip("Remove", **kwargs)

    def test_tag_and_chip_no_duplicate_cls_and_class_attributes(self) -> None:
        """Tag and Chip should never output both cls='...' and class='...' in XML."""
        tag = Tag("Custom Tag", cls="my-tag-cls")
        tag_xml = to_xml(tag)
        assert 'class="' in tag_xml
        assert " cls=" not in tag_xml

        chip = Chip("Custom Chip", cls="my-chip-cls", selected=True)
        chip_xml = to_xml(chip)
        assert 'class="' in chip_xml
        assert " cls=" not in chip_xml
        assert "chip-selected" in chip_xml

    def test_segmented_control_attribute_clashing_on_options(self) -> None:
        """Options inside SegmentedControl should not have duplicate class and cls attributes."""
        btn1 = Button("Day", cls="btn-primary")
        btn2 = Button("Week")
        sc = SegmentedControl(btn1, btn2, active_index=0)
        xml = to_xml(sc)
        # Note: If SegmentedControl modifies option attrs with cls='active' instead of merging
        # into 'class', it generates both class="..." and cls="active"
        # We check whether the output contains invalid raw cls attribute
        assert (
            " cls=" not in xml
        ), "SegmentedControl generated conflicting cls attribute on child button"
        assert (
            'class="btn-primary active"' in xml
            or 'class="active btn-primary"' in xml
            or "active" in xml
        )

    def test_aria_roles_and_states_conform_to_standards(self) -> None:
        """Verify aria-pressed, aria-selected, aria-current, aria-expanded, role='group'/'listitem'."""
        # 1. ListItem
        li_selected = ListItem("Title", selected=True)
        li_active = ListItem("Title", active=True)
        li_disabled = ListItem("Title", disabled=True)
        li_loading = ListItem("Title", loading=True)

        assert to_xml(li_selected).count('role="listitem"') == 1
        assert 'aria-current="true"' in to_xml(li_selected)
        assert 'aria-current="true"' in to_xml(li_active)
        assert 'aria-disabled="true"' in to_xml(li_disabled)
        assert 'aria-busy="true"' in to_xml(li_loading)

        # 2. ViewToggle
        vt = ViewToggle(value="grid", options=("list", "grid"))
        vt_xml = to_xml(vt)
        assert 'role="group"' in vt_xml
        assert 'aria-label="Choose view"' in vt_xml
        assert 'aria-pressed="true"' in vt_xml
        assert 'aria-pressed="false"' in vt_xml

        # 3. SegmentedControl
        sc = SegmentedControl(Button("A"), Button("B"), active_index=0)
        sc_xml = to_xml(sc)
        assert 'role="group"' in sc_xml
        assert 'role="radio"' not in sc_xml
        assert 'aria-checked="true"' not in sc_xml
        assert 'aria-pressed="true"' in sc_xml
        assert 'aria-pressed="false"' in sc_xml

        # 4. Chip and ChipGroup
        chip_sel = Chip("Selected", selected=True)
        assert 'aria-pressed="true"' in to_xml(chip_sel)

        # ChipGroup selection
        cg = ChipGroup(Chip("A"), Chip("B"), selected=0, label="Filters")
        cg_xml = to_xml(cg)
        assert 'role="group"' in cg_xml
        assert 'aria-label="Filters"' in cg_xml


# ==============================================================================
# Category B: CSS Layout, Flexbox, & Overflow
# ==============================================================================


class TestCSSLayoutAndOverflow:
    """Audit flex shrink, min-width 0, multiline clamping, and safe-area styles."""

    def test_list_item_content_has_min_w_0(self) -> None:
        """ListItem content wrapper must have min-w-0 and flex-grow-1 to prevent flex blowout."""
        li = ListItem(title="A very long overflowing title that should truncate or clamp properly")
        xml = to_xml(li)
        assert "min-w-0" in xml
        assert "flex-grow-1" in xml
        assert "faststrap-list-item-content" in xml

    def test_list_item_multi_line_clamping_classes(self) -> None:
        """Check lines=1, lines=2, and lines=3 classes on ListItem."""
        li1 = ListItem(title="One line", lines=1)
        li2 = ListItem(title="Two lines", lines=2)
        li3 = ListItem(title="Three lines", lines=3)

        assert "faststrap-list-item-lines-1" in to_xml(li1)
        assert "faststrap-list-item-lines-2" in to_xml(li2)
        assert "faststrap-list-item-lines-3" in to_xml(li3)

    def test_list_item_with_rich_text_children_in_title(self) -> None:
        """ListItem title containing rich HTML elements (e.g. Span, Strong) renders properly."""
        rich_title = Span(Strong("Bold"), " and normal text")
        li = ListItem(title=rich_title, lines=2)
        xml = to_xml(li)
        assert "<strong>Bold</strong>" in xml or "Bold" in xml
        assert "faststrap-list-item-title" in xml

    def test_safe_area_edge_and_mode_classes(self) -> None:
        """SafeArea renders safe-area-padding-* and safe-area-margin-* classes."""
        for edge in ["all", "top", "right", "bottom", "left", "vertical", "horizontal"]:
            p = SafeArea("Content", edges=edge, mode="padding")
            assert f"safe-area-padding-{edge}" in to_xml(p)

            m = SafeArea("Content", edges=edge, mode="margin")
            assert f"safe-area-margin-{edge}" in to_xml(m)


# ==============================================================================
# Category C: DataTable Mobile Mode Inspection
# ==============================================================================


class TestDataTableMobileMode:
    """Audit DataTable mobile cards, stack, IDs, accessibility, and HTMX targets."""

    def test_datatable_mobile_modes_render_expected_containers(self) -> None:
        """DataTable(mobile_mode='cards'|'stack'|'scroll') renders corresponding elements."""
        records = [{"name": "Item 1", "category": "General", "val": 42}]

        # scroll mode
        dt_scroll = DataTable(records, mobile_mode="scroll")
        xml_scroll = to_xml(dt_scroll)
        assert "table-responsive" in xml_scroll
        assert "faststrap-data-table-cards" not in xml_scroll
        assert "faststrap-data-table-stack" not in xml_scroll

        # cards mode
        dt_cards = DataTable(records, mobile_mode="cards", mobile_breakpoint="md")
        xml_cards = to_xml(dt_cards)
        assert "d-none d-md-block" in xml_cards
        assert "d-md-none" in xml_cards
        assert "faststrap-data-table-cards" in xml_cards
        assert "faststrap-data-table-card" in xml_cards

        # stack mode
        dt_stack = DataTable(records, mobile_mode="stack", mobile_breakpoint="lg")
        xml_stack = to_xml(dt_stack)
        assert "d-none d-lg-block" in xml_stack
        assert "d-lg-none" in xml_stack
        assert "faststrap-data-table-stack" in xml_stack

    def test_datatable_mobile_options_mapping(self) -> None:
        """Verify mobile_title, mobile_subtitle, mobile_meta, and mobile_card_cls."""
        records = [{"id": "1", "name": "Item 1", "sub": "Subtitle text", "extra": "Meta info"}]
        dt = DataTable(
            records,
            columns=["id", "name", "sub", "extra"],
            mobile_mode="cards",
            mobile_title="name",
            mobile_subtitle="sub",
            mobile_meta=["extra"],
            mobile_hidden=["id"],
            mobile_card_cls="custom-card-cls",
        )
        xml = to_xml(dt)
        assert "custom-card-cls" in xml
        assert "Subtitle text" in xml
        assert "Meta info" in xml
        # 'id' column was marked mobile_hidden
        card_html = xml.split('class="d-md-none"')[1]
        assert 'faststrap-data-table-card-label">id<' not in card_html

    def test_datatable_mobile_card_renderer(self) -> None:
        """Verify custom mobile_card_renderer receives row dict."""
        records = [{"name": "Custom", "sku": "SKU-99"}]
        dt = DataTable(
            records,
            mobile_mode="cards",
            mobile_card_renderer=lambda row: Div(
                H1(row["name"]),
                Span(row["sku"]),
                cls="bespoke-card",
            ),
        )
        xml = to_xml(dt)
        assert "bespoke-card" in xml
        assert "SKU-99" in xml

    def test_datatable_htmx_swap_targets_match_wrapper(self) -> None:
        """Search and pagination links inside mobile mode target the same container."""
        dt = DataTable(
            [{"name": "Alpha"}, {"name": "Beta"}],
            pagination=True,
            page=1,
            per_page=1,
            total_rows=2,
            endpoint="/api/items",
            table_id="my-test-table",
            hx_target="#my-test-table",
            searchable=True,
            mobile_mode="cards",
        )
        xml = to_xml(dt)
        assert 'id="my-test-table"' in xml
        # Search input targets #my-test-table
        assert 'hx-target="#my-test-table"' in xml
        # Pagination links target #my-test-table
        assert xml.count('hx-target="#my-test-table"') >= 2

    def test_mobile_sort_controls_preserve_state_and_reset_page(self) -> None:
        xml = to_xml(
            DataTable(
                [{"name": "Alpha", "state": "active"}],
                columns=["name", "state"],
                header_map={"name": "Name", "state": "Status"},
                sortable=True,
                sort="name",
                direction="asc",
                mobile_mode="cards",
                mobile_sortable=True,
                searchable=True,
                search="alpha",
                filters={"team": "blue"},
                pagination=True,
                page=4,
                endpoint="/items",
                total_rows=100,
                table_id="sort-table",
                push_url=True,
            )
        )
        assert 'aria-label="Sort records"' in xml
        assert 'aria-label="Sort by Name, currently asc"' in xml
        assert 'hx-target="#sort-table"' in xml
        assert 'hx-push-url="true"' in xml
        assert "sort=name&amp;direction=desc" in xml
        assert "team=blue" in xml and "q=alpha" in xml
        assert "page=1" in xml

    def test_mobile_sort_controls_can_be_disabled_and_need_a_link_base(self) -> None:
        options = {
            "data": [{"name": "Alpha"}],
            "sortable": True,
            "mobile_mode": "stack",
        }
        assert 'aria-label="Sort records"' not in to_xml(DataTable(**options))
        assert 'aria-label="Sort records"' not in to_xml(
            DataTable(**options, base_url="/items", mobile_sortable=False)
        )

    def test_datatable_duplicate_dom_ids_audit(self) -> None:
        """Audit for duplicate IDs when child elements contain explicit IDs in both table and mobile views."""
        # When mobile_card_attrs includes an id, DataTable rejects it:
        with pytest.raises(ValueError, match="mobile_card_attrs cannot include 'id'"):
            DataTable(
                [{"a": 1}], mobile_mode="cards", mobile_card_attrs={"id": "duplicate-card-id"}
            )

        # When mobile_card_renderer produces elements with static IDs across records:
        records = [{"id": "1", "name": "Item 1"}]
        dt = DataTable(
            records,
            mobile_mode="cards",
            mobile_card_renderer=lambda r: Button("Action", id="action-btn-static"),
        )
        xml = to_xml(dt)
        # Verify the static ID is rendered in the mobile card view
        assert "action-btn-static" in xml


# ==============================================================================
# Category D: ViewToggle & CollectionView Integration
# ==============================================================================


class TestViewToggleAndCollectionView:
    """Audit ViewToggle query sync, HTMX integration, and CollectionView edge cases."""

    def test_view_toggle_direct_url_sync(self) -> None:
        """ViewToggle with endpoint generates query parameters for each view mode."""
        vt = ViewToggle(value="list", endpoint="/products?category=shoes", param="view")
        xml = to_xml(vt)
        assert 'href="/products?category=shoes&amp;view=list"' in xml
        assert 'href="/products?category=shoes&amp;view=grid"' in xml
        assert 'aria-current="true"' in xml

    def test_view_toggle_htmx_partial_swaps(self) -> None:
        """ViewToggle with endpoint and hx_target renders HTMX attributes."""
        vt = ViewToggle(
            value="grid",
            endpoint="/products",
            param="view",
            hx_target="#collection-container",
            hx_swap="outerHTML",
            push_url=True,
        )
        xml = to_xml(vt)
        assert 'hx-get="/products?view=grid"' in xml
        assert 'hx-target="#collection-container"' in xml
        assert 'hx-swap="outerHTML"' in xml
        assert 'hx-push-url="true"' in xml

    def test_collection_view_with_empty_state_and_none_records(self) -> None:
        """CollectionView renders EmptyState properly when records is None or items empty."""
        empty = EmptyState("No products found", description="Check back later")
        cv = CollectionView(empty=empty)
        xml = to_xml(cv)
        assert "faststrap-collection-empty" in xml
        assert "No products found" in xml
        assert "Check back later" in xml

    def test_collection_view_with_empty_records_list(self) -> None:
        """CollectionView with records=[] renders empty state."""
        empty = EmptyState("Empty list")
        cv = CollectionView(
            records=[],
            list_renderer=lambda r: ListItem(r["title"]),
            empty=empty,
        )
        xml = to_xml(cv)
        assert "faststrap-collection-empty" in xml
        assert "Empty list" in xml

    def test_collection_view_mode_switching_list_and_grid(self) -> None:
        """CollectionView switches between ListView and GridList correctly."""
        records = [{"title": "Card 1"}, {"title": "Card 2"}]
        cv_list = CollectionView(
            records=records,
            mode="list",
            list_renderer=lambda r: ListItem(r["title"]),
        )
        assert "faststrap-list-view" in to_xml(cv_list)

        cv_grid = CollectionView(
            records=records,
            mode="grid",
            card_renderer=lambda r: Div(r["title"]),
        )
        assert "faststrap-grid-list" in to_xml(cv_grid)

    def test_collection_view_empty_records_do_not_require_renderer(self) -> None:
        empty = EmptyState("Nothing here")
        for records in ([], iter(())):
            html = to_xml(CollectionView(records=records, empty=empty))
            assert "faststrap-collection-empty" in html
            assert "Nothing here" in html

    def test_safe_area_css_has_non_env_fallbacks(self) -> None:
        css = (
            Path(__file__).parents[1] / "src/faststrap/static/css/faststrap-layouts.css"
        ).read_text()
        assert "padding-top: 0;" in css
        assert "padding-top: env(safe-area-inset-top, 0px);" in css
        assert "padding-bottom: 0.5rem;" in css
        assert "env(safe-area-inset-bottom, 0px)" in css

    def test_rendered_v010_components_do_not_emit_raw_cls_attributes(self) -> None:
        components = [
            ListItem("Item", cls="custom"),
            ListView(ListItem("Item"), cls="custom"),
            GridList(Div("Card"), cls="custom"),
            CollectionView(ListItem("Item"), cls="custom"),
            ViewToggle(cls="custom"),
            Chip("Chip", selected=True, cls="custom"),
            ChipGroup(Chip("Chip"), selected=0, cls="custom"),
            SafeArea("Area", cls="custom"),
            StickyActionBar(Button("Save"), cls="custom"),
            MobileAppShell("Content", cls="custom"),
            MobileToolbar("Title", cls="custom"),
            Snackbar("Saved", cls="custom"),
            SegmentedControl(Button("One", cls="existing"), cls="custom"),
            DataTable([{"value": "one"}], mobile_mode="cards", cls="custom"),
        ]
        for component in components:
            assert " cls=" not in to_xml(component)


# ==============================================================================
# Category E: Modern Feedback & Mobile Layout Primitives
# ==============================================================================


class TestModernFeedbackAndLayoutPrimitives:
    """Audit Snackbar, MobileAppShell, MobileToolbar, and StickyActionBar."""

    def test_snackbar_variants_and_placements(self) -> None:
        """Audit Snackbar variant and placement classes and ARIA live attributes."""
        for v in ["info", "success", "warning", "danger", "dark"]:
            for p in ["inline", "top", "bottom"]:
                sb = Snackbar("Feedback", variant=v, placement=p, dismissible=True)
                xml = to_xml(sb)
                assert f"faststrap-snackbar-{p}" in xml
                if v in {"danger", "warning"}:
                    assert 'role="alert"' in xml
                    assert 'aria-live="assertive"' in xml
                else:
                    assert 'role="status"' in xml
                    assert 'aria-live="polite"' in xml
                assert "btn-close" in xml

    def test_sticky_action_bar_permutations(self) -> None:
        """Audit StickyActionBar safe_area and breakpoint permutations."""
        bar = StickyActionBar(
            Button("Cancel"), Button("Save", variant="primary"), stack_at="sm", safe_area=True
        )
        xml = to_xml(bar)
        assert "faststrap-sticky-action-bar" in xml
        assert "faststrap-sticky-action-bar-safe" in xml
        assert "position-sticky" in xml
        assert "bottom-0" in xml

    def test_mobile_toolbar_permutations(self) -> None:
        """Audit MobileToolbar slots, sticky mode, and semantic role='banner'."""
        tb = MobileToolbar(
            "Page Title",
            subtitle="Subtitle text",
            back_href="/back",
            back_label="Return",
            actions=[Button("Save")],
            sticky=True,
        )
        xml = to_xml(tb)
        assert 'role="banner"' in xml
        assert "position-sticky top-0" in xml
        assert 'href="/back"' in xml
        assert 'aria-label="Return"' in xml

    def test_mobile_app_shell_slots_and_safe_area(self) -> None:
        """Audit MobileAppShell layout structure and safe area nesting."""
        shell = MobileAppShell(
            Div("Main Content Area"),
            desktop_nav=Div("Desktop Header"),
            mobile_toolbar=Div("Mobile Bar"),
            bottom_nav=Div("Bottom Nav"),
            safe_area=True,
        )
        xml = to_xml(shell)
        assert "faststrap-mobile-app-shell" in xml
        assert 'id="main-content"' in xml
        assert "safe-area-padding-bottom" in xml

    def test_mobile_app_shell_sidebar_is_in_desktop_row_and_options_are_configurable(self) -> None:
        xml = to_xml(
            MobileAppShell(
                "Content",
                sidebar=Div("Sidebar"),
                breakpoint="md",
                content_id="workspace",
            )
        )
        assert "faststrap-mobile-app-desktop-layout d-flex" in xml
        assert "faststrap-mobile-app-sidebar" in xml
        assert 'id="workspace"' in xml
        assert "d-none d-md-block" in xml

    def test_mobile_app_shell_can_omit_content_id_and_validates_breakpoint(self) -> None:
        assert 'id="main-content"' not in to_xml(MobileAppShell("Content", content_id=None))
        with pytest.raises(ValueError, match="breakpoint must"):
            MobileAppShell("Content", breakpoint="bad")


def test_chip_type_hints_resolve_public_anchor_type() -> None:
    assert get_type_hints(ChipComponent)["return"] is FT


def test_chip_selection_uses_semantic_controls_and_clears_stale_state() -> None:
    from faststrap import Chip, ChipGroup

    chip = ChipGroup(
        Chip("A", selected=True),
        Chip("B", selected=True),
        selected=1,
    )
    html = to_xml(chip)
    assert html.count('aria-pressed="true"') == 1
    assert html.count('aria-pressed="false"') == 1
    assert html.count("chip-selected") == 1
    assert html.count("<button") == 2


def test_chip_group_preserves_link_and_removable_semantics() -> None:
    from faststrap import Chip, ChipGroup

    html = to_xml(ChipGroup(Chip("Link", href="/link"), Chip("Remove", removable=True), selected=0))
    assert 'aria-current="true"' in html
    assert "aria-pressed=" not in html
    assert "<a " in html


def test_segmented_control_uses_native_button_and_link_semantics() -> None:
    html = to_xml(SegmentedControl(Button("A"), A("B", href="/b"), active_index=1))
    assert 'role="group"' in html
    assert 'role="radio"' not in html
    assert "aria-checked=" not in html
    assert 'aria-pressed="false"' in html
    assert 'aria-current="true"' in html


def test_datatable_rejects_repeated_mobile_renderer_ids() -> None:
    records = [{"name": "One"}, {"name": "Two"}]
    with pytest.raises(ValueError, match="duplicate or reserved element id"):
        DataTable(
            records,
            mobile_mode="cards",
            mobile_card_renderer=lambda row: Button(row["name"], id="repeated"),
        )


def test_datatable_rejects_mobile_renderer_id_matching_wrapper() -> None:
    with pytest.raises(ValueError, match="duplicate or reserved element id"):
        DataTable(
            [{"name": "One"}],
            mobile_mode="cards",
            id="records",
            mobile_card_renderer=lambda row: Button(row["name"], id="records"),
        )
