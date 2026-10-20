"""Tests for the v0.10.0 mobile-wave primitives."""

from pathlib import Path

import pytest
from fasthtml.common import A, Button, to_xml

from faststrap import (
    BottomNav,
    Chip,
    ChipGroup,
    MobileAppShell,
    MobileToolbar,
    SafeArea,
    SegmentedControl,
    Snackbar,
    StickyActionBar,
)
from faststrap.core.registry import list_components


def test_safe_area_renders_edge_and_mode_classes() -> None:
    html = to_xml(SafeArea("Content", edges="bottom", mode="padding"))
    assert "faststrap-safe-area" in html
    assert "safe-area-padding-bottom" in html


def test_bottom_nav_safe_area_fallback_and_user_style_override() -> None:
    html = to_xml(BottomNav("Links"))
    assert "padding-bottom:0" in html
    assert "env(safe-area-inset-bottom, 0px)" in html

    custom = {"background-color": "white"}
    custom_html = to_xml(BottomNav("Links", style=custom))
    assert "env(safe-area-inset-bottom, 0px)" in custom_html
    assert custom == {"background-color": "white"}

    explicit_html = to_xml(BottomNav("Links", style="padding-bottom: 1rem"))
    assert "padding-bottom: 1rem" in explicit_html


def test_snackbar_viewport_placements_have_shipped_css_rules() -> None:
    css = (Path(__file__).parents[1] / "src/faststrap/static/css/faststrap-layouts.css").read_text(
        encoding="utf-8"
    )
    assert ".faststrap-snackbar-top" in css
    assert ".faststrap-snackbar-bottom" in css
    assert "position: fixed" in css
    assert "env(safe-area-inset-top, 0px)" in css
    assert "env(safe-area-inset-bottom, 0px)" in css


def test_mobile_app_shell_composes_desktop_mobile_and_bottom_slots() -> None:
    html = to_xml(
        MobileAppShell(
            "Content",
            desktop_nav="Desktop",
            mobile_nav="Mobile",
            bottom_nav=BottomNav("Links"),
        )
    )
    assert "faststrap-mobile-app-shell" in html
    assert "Desktop" in html and "Mobile" in html and "Content" in html
    assert "faststrap-mobile-app-bottom-nav" in html
    assert 'id="main-content"' in html


def test_mobile_toolbar_supports_back_title_and_actions() -> None:
    html = to_xml(
        MobileToolbar(
            "Settings",
            subtitle="Account",
            back_href="/home",
            actions=Button("Save"),
        )
    )
    assert "Settings" in html
    assert "Account" in html
    assert 'href="/home"' in html
    assert "Save" in html


def test_sticky_action_bar_supports_safe_area_and_responsive_stack() -> None:
    html = to_xml(StickyActionBar(Button("Save"), stack_at="md"))
    assert "faststrap-sticky-action-bar" in html
    assert "faststrap-sticky-action-bar-safe" in html
    assert "flex-md-row" in html


def test_chip_and_chip_group_support_selection_and_removal() -> None:
    html = to_xml(
        ChipGroup(
            Chip("Python", value="python"),
            Chip("ML", removable=True, selected=True),
            selected=1,
            label="Topics",
        )
    )
    assert "faststrap-chip-group" in html
    assert 'data-fs-chip="true"' in html
    assert 'data-fs-value="python"' in html
    assert "chip-selected" in html
    assert 'aria-label="Topics"' in html
    assert "btn-close" in html


def test_segmented_control_supports_links_and_form_value() -> None:
    html = to_xml(
        SegmentedControl(
            A("Day", href="?range=day"),
            A("Week", href="?range=week"),
            name="range",
            values=["day", "week"],
            active_index=1,
        )
    )
    assert 'role="group"' in html
    assert 'href="?range=week"' in html
    assert 'aria-current="true"' in html
    assert 'name="range"' in html
    assert 'value="week"' in html


def test_snackbar_is_anchored_and_action_oriented() -> None:
    html = to_xml(
        Snackbar(
            "Draft saved",
            title="Success",
            action=Button("Undo", variant="link"),
            placement="bottom",
            duration=4000,
        )
    )
    assert "faststrap-snackbar" in html
    assert "faststrap-snackbar-bottom" in html
    assert 'data-fs-duration="4000"' in html
    assert "Undo" in html
    assert "Dismiss notification" in html


def test_mobile_wave_components_are_registered() -> None:
    registered = set(list_components())
    assert registered.issuperset(
        {
            "MobileAppShell",
            "SafeArea",
            "Chip",
            "ChipGroup",
            "SegmentedControl",
            "Snackbar",
            "MobileToolbar",
            "StickyActionBar",
        }
    )


@pytest.mark.parametrize(
    "factory",
    [
        lambda: SafeArea("x", edges="bad"),
        lambda: SegmentedControl(),
        lambda: Snackbar("x", duration=-1),
        lambda: StickyActionBar("x", stack_at="bad"),
    ],
)
def test_mobile_wave_validates_public_options(factory) -> None:
    with pytest.raises(ValueError):
        factory()
