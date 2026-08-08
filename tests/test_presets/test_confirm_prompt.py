"""Tests for ConfirmPrompt preset."""

from fasthtml.common import to_xml

from faststrap.presets.interactions import ConfirmPrompt


def test_confirm_prompt_renders_modal():
    """ConfirmPrompt renders a modal dialog."""
    html = to_xml(ConfirmPrompt("Delete this item?"))

    assert "modal" in html
    assert "modal-dialog" in html
    assert "modal-content" in html


def test_confirm_prompt_uses_message_as_body():
    """ConfirmPrompt uses the message in the modal body."""
    html = to_xml(ConfirmPrompt("Delete this item?"))

    assert "Delete this item?" in html


def test_confirm_prompt_has_confirm_and_cancel_buttons():
    """ConfirmPrompt renders confirm and cancel buttons."""
    html = to_xml(ConfirmPrompt("Delete this item?"))

    assert "Delete" in html
    assert "Cancel" in html


def test_confirm_prompt_custom_confirm_text():
    """ConfirmPrompt accepts custom confirm button text."""
    html = to_xml(
        ConfirmPrompt(
            "Delete this item?",
            confirm_button_text="Yes, delete",
        )
    )

    assert "Yes, delete" in html


def test_confirm_prompt_custom_variant():
    """ConfirmPrompt applies variant to confirm button."""
    html = to_xml(
        ConfirmPrompt(
            "Delete this item?",
            confirm_button_variant="danger",
        )
    )

    assert "btn-danger" in html


def test_confirm_prompt_static_backdrop():
    """ConfirmPrompt uses static backdrop."""
    html = to_xml(ConfirmPrompt("Are you sure?"))

    assert "static" in html or "data-bs-backdrop" in html
