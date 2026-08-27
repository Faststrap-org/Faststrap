"""Tests for ModernToast components."""

import pytest
from fasthtml.common import to_xml

from faststrap import ModernToast, ModernToastStack
from faststrap.components.feedback.modern_toast import ToastPlacement


def test_modern_toast_renders_configurable_surface() -> None:
    html = to_xml(
        ModernToast(
            "Saved",
            "Your settings were updated.",
            intent="success",
            placement=ToastPlacement(position="top-end"),
            duration=3000,
            visual_style="glass",
            action={"label": "Undo", "style": "link"},
        )
    )

    assert "faststrap-modern-toast" in html
    assert "faststrap-modern-toast-glass" in html
    assert 'data-fs-duration="3000"' in html
    assert 'data-fs-position="top-end"' in html
    assert 'role="status"' in html
    assert "Saved" in html
    assert "Undo" in html
    assert "bi-check-circle" in html
    assert 'type="button"' in html
    assert "data-bs-dismiss" not in html
    assert ">x</button>" not in html
    assert "data-fs-dismiss" in html
    assert "data-fs-intent" in html
    assert "data-fs-animation" in html


def test_modern_toast_warning_uses_alert_role() -> None:
    html = to_xml(ModernToast("Careful", intent="warning"))

    assert 'role="alert"' in html
    assert "border-warning" in html


def test_modern_toast_stack_positions_toasts() -> None:
    html = to_xml(
        ModernToastStack(
            ModernToast("Saved"),
            placement=ToastPlacement(position="bottom-end"),
        )
    )

    assert "faststrap-modern-toast-stack" in html
    assert "bottom-0 end-0" in html
    assert "Saved" in html
    assert "data-fs-max-visible" in html


def test_modern_toast_emits_deprecation_warnings_for_legacy_params() -> None:
    with pytest.warns(DeprecationWarning, match="variant="):
        to_xml(ModernToast("Old", variant="success"))

    with pytest.warns(DeprecationWarning, match="position="):
        to_xml(ModernToast("Old", position="top-left"))

    with pytest.warns(DeprecationWarning, match="style="):
        to_xml(ModernToast("Old", style="solid"))


def test_modern_toast_infinite_duration_omits_timer_data() -> None:
    html = to_xml(ModernToast("Hi", duration="infinite"))

    assert 'data-fs-duration="0"' in html


def test_modern_toast_non_dismissible_omits_dismiss_attribute() -> None:
    html = to_xml(ModernToast("Hi", dismissible=False))

    assert "data-fs-dismiss" not in html


def test_modern_toast_pause_on_hover_flag() -> None:
    html = to_xml(ModernToast("Hi", pause_on_hover=True))
    assert 'data-fs-pause-on-hover="true"' in html

    html = to_xml(ModernToast("Hi", pause_on_hover=False))
    assert 'data-fs-pause-on-hover="false"' in html


def test_modern_toast_action_typed_dict_renders_button() -> None:
    html = to_xml(
        ModernToast(
            "Done",
            action={"label": "Retry", "style": "btn-primary", "loading": True},
        )
    )
    assert "Retry" in html
    assert "btn-primary" in html
    assert "disabled" in html


def test_modern_toast_error_intent_uses_danger_classes() -> None:
    html = to_xml(ModernToast("Failed", intent="error"))
    assert "border-danger" in html
    assert "text-danger" in html
    assert "border-error" not in html
    assert "text-error" not in html
    assert 'data-fs-intent="error"' in html  # semantic value preserved for theming


def test_modern_toast_loading_intent_uses_primary_classes() -> None:
    html = to_xml(ModernToast("Loading", intent="loading"))
    assert "border-primary" in html
    assert "text-primary" in html
    assert "text-loading" not in html
    assert 'data-fs-intent="loading"' in html


def test_modern_toast_legacy_variant_danger_maps_to_valid_classes() -> None:
    with pytest.warns(DeprecationWarning, match="variant="):
        html = to_xml(ModernToast("Failed", variant="danger"))
    assert "border-danger" in html
    assert "border-error" not in html
    assert 'data-fs-intent="error"' in html


def test_modern_toast_legacy_variant_warning_maps_intent() -> None:
    with pytest.warns(DeprecationWarning, match="variant="):
        html = to_xml(ModernToast("Careful", variant="warning"))
    assert 'data-fs-intent="warning"' in html
    assert "border-warning" in html


def test_modern_toast_action_style_literals_map_to_btn_classes() -> None:
    for style, expected in [
        ("primary", "btn-primary"),
        ("secondary", "btn-secondary"),
        ("destructive", "btn-danger"),
        ("outline", "btn-outline-secondary"),
    ]:
        html = to_xml(ModernToast("T", action={"label": "Go", "style": style}))
        assert expected in html, f"{style} -> {expected}"


def test_modern_toast_cancel_style_maps_to_btn_class() -> None:
    html = to_xml(ModernToast("T", cancel={"label": "No", "style": "destructive"}))
    assert "btn-danger" in html


def test_modern_toast_literal_error_loads_bootstrap_classes() -> None:
    for intent in ("error", "loading"):
        html = to_xml(ModernToast("T", intent=intent))
        # No raw non-Bootstrap border/text color class is emitted.
        assert f"border-{intent}" not in html
        assert f"text-{intent}" not in html


def test_modern_toast_stack_gap_parameter() -> None:
    html = to_xml(ModernToastStack(ModernToast("x")))
    assert "gap-8" in html
    assert "gap:" not in html.split("style=")[1]  # default gutter uses the gap utility


def test_modern_toast_stack_gutter_override_adds_inline_gap() -> None:
    html = to_xml(ModernToastStack(ModernToast("x"), placement=ToastPlacement(gutter=16)))
    assert "gap: 4.0rem" in html
