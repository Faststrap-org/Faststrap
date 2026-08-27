"""Tests for the minor-release API additions from the ergonomics audit.

Covers: shared visual tokens, Toast-family hooks, ModernToast tokens/slots and
global defaults, FloatingActionButton size/offset/shape, GradientButton
text_color/hover and AA-contrast presets, ProfileDropdown flexible layout,
CalendarDatePicker button hooks, ResultCard slots, Sheet radius, and the
ErrorDialog icon hook.
"""

import pytest
from fasthtml.common import Button as FTButton
from fasthtml.common import to_xml

from faststrap import (
    CalendarDatePicker,
    ErrorDialog,
    FloatingActionButton,
    GradientButton,
    ModernToast,
    ProfileDropdown,
    ResultCard,
    Sheet,
    SimpleToast,
    Toast,
    ToastContainer,
)
from faststrap.core.theme import reset_component_defaults, set_component_defaults
from faststrap.core.visual import RADIUS_CLASSES, SHADOW_CLASSES, radius_class

# ── Shared visual tokens ────────────────────────────────────────────────


def test_radius_class_tokens():
    assert RADIUS_CLASSES["md"] == "rounded-3"
    assert radius_class("lg") == "rounded-4"
    assert radius_class(None) == ""
    assert SHADOW_CLASSES["sm"] == "shadow-sm"


# ── Toast family ─────────────────────────────────────────────────────────


def test_toast_slot_classes_and_radius():
    html = to_xml(
        Toast(
            "Body",
            title="Header",
            variant="light",
            radius="sm",
            header_cls="custom-header",
            body_cls="custom-body",
            close_button_cls="me-1",
        )
    )
    assert "rounded-2" in html
    assert "custom-header" in html
    assert "custom-body" in html
    assert "me-1" in html


def test_simple_toast_body_cls_and_radius():
    html = to_xml(SimpleToast("Body", radius="none", body_cls="fw-bold"))
    assert "rounded-0" in html
    assert "fw-bold" in html


def test_toast_container_auto_id_and_conflict():
    auto = to_xml(ToastContainer(container_id=None))
    assert 'id="toast-container-' in auto

    named = to_xml(ToastContainer(container_id="mine"))
    assert 'id="mine"' in named

    with pytest.raises(ValueError):
        ToastContainer(Toast("A"), container_id="x", id="y")


# ── ModernToast ──────────────────────────────────────────────────────────


def test_modern_toast_radius_shadow_and_slots():
    html = to_xml(
        ModernToast(
            "Saved",
            message="All good",
            radius="md",
            shadow="sm",
            title_cls="tt",
            message_cls="mm",
            close_button_cls="cc",
        )
    )
    assert "rounded-3" in html
    assert "shadow-sm" in html
    assert "rounded-4" not in html
    assert "shadow-lg" not in html
    assert "tt" in html
    assert "mm" in html
    assert "cc" in html


def test_modern_toast_minimal_style_has_surface_class():
    html = to_xml(ModernToast("Hi", visual_style="minimal"))
    assert "faststrap-modern-toast-minimal" in html


def test_modern_toast_global_defaults():
    try:
        set_component_defaults("ModernToast", intent="success")
        html = to_xml(ModernToast("Hi"))
        assert 'data-fs-intent="success"' in html
        assert "border-success" in html
    finally:
        reset_component_defaults("ModernToast")


# ── Action buttons ───────────────────────────────────────────────────────


def test_fab_size_offset_shape():
    small = to_xml(FloatingActionButton(icon="plus", size="sm", offset=4))
    assert "--fs-fab-size: 44px" in small
    assert "--fs-fab-inset: 4rem" in small

    pill = to_xml(FloatingActionButton("Edit draft", icon="edit", shape="pill"))
    assert "fab-pill" in pill
    assert "rounded-circle" not in pill

    # Default output stays compatible with the historical 56px circle.
    legacy = to_xml(FloatingActionButton(icon="plus"))
    assert "--fs-fab-size: 56px" in legacy
    assert "rounded-circle" in legacy
    assert "fab-bottom-right" in legacy


def test_gradient_button_text_color_hover_presets():
    html = to_xml(GradientButton("Go", gradient="orange", text_color="#111", hover="lift"))
    assert "--faststrap-gradient-button-text: #111" in html
    assert "hover-lift" in html
    # Darkened AA-contrast endpoint replaces the old near-white #fee140.
    assert "#fee140" not in html
    assert "#ea580c" in html

    none_hover = to_xml(GradientButton("Go", hover="none"))
    assert "hover-lift" not in none_hover


# ── ProfileDropdown ──────────────────────────────────────────────────────


def test_profile_dropdown_horizontal_layout_and_sizes():
    html = to_xml(
        ProfileDropdown(
            "Alice Smith",
            subtitle="Admin",
            avatar_size=40,
            layout="horizontal",
            src="/a.png",
        )
    )
    assert 'width="40"' in html
    assert 'height="40"' in html
    assert "d-block w-100" not in html  # stacked subtitle is gone
    assert "text-truncate" in html


def test_profile_dropdown_slot_classes_footer_and_item_attrs():
    footer_btn = FTButton("Switch workspace", type="button", cls="btn btn-sm")
    html = to_xml(
        ProfileDropdown(
            "Alice",
            items=[
                ("Profile", "/profile"),
                ("Sign out", "/logout", {"data-testid": "logout"}),
            ],
            trigger_cls="trig",
            menu_cls="menu-x",
            item_cls="item-x",
            footer=footer_btn,
        )
    )
    assert "trig" in html
    assert "menu-x" in html
    assert "item-x" in html
    assert 'data-testid="logout"' in html
    assert "dropdown-divider" in html
    assert "Switch workspace" in html


def test_profile_dropdown_global_defaults():
    try:
        set_component_defaults("ProfileDropdown", avatar_size=48)
        html = to_xml(ProfileDropdown("Alice"))
        assert 'width="48"' in html or "height: 48px" in html
    finally:
        reset_component_defaults("ProfileDropdown")


# ── CalendarDatePicker / ResultCard / Sheet / ErrorDialog ────────────────


def test_calendar_date_picker_button_cls_hooks():
    html = to_xml(
        CalendarDatePicker(
            apply_label="Apply",
            clear_label="Clear",
            apply_cls="btn-sm apply-x",
            clear_cls="clear-x",
        )
    )
    assert "apply-x" in html
    assert "clear-x" in html
    assert "btn-sm" in html


def test_result_card_slots():
    html = to_xml(
        ResultCard(
            "Done",
            message="Everything synced.",
            icon_cls="fs-2 ic",
            title_cls="tc",
            message_cls="mc",
        )
    )
    assert "fs-2" in html
    assert "ic" in html
    assert "tc" in html
    assert "mc" in html


def test_sheet_radius_token():
    assert "rounded-top-4" in to_xml(Sheet("x"))
    md = to_xml(Sheet("x", radius="md"))
    assert "rounded-top-3" in md
    assert "rounded-top-4" not in md


def test_error_dialog_icon_hook():
    default = str(to_xml(ErrorDialog(message="boom", modal_id="ed")))
    assert "fs-1" in default  # historical weight retained by default

    calmed = str(to_xml(ErrorDialog(message="boom", modal_id="ed2", icon_cls="fs-3")))
    assert "fs-3" in calmed
