"""Tests for ErrorDialog component."""

from fasthtml.common import to_xml

from faststrap.components.feedback import ErrorDialog


def test_error_dialog_basic():
    """ErrorDialog renders with basic message."""
    dialog = ErrorDialog(message="Something went wrong")
    html = to_xml(dialog)

    assert "Something went wrong" in html
    assert "modal" in html
    assert "Error" in html  # Default title


def test_error_dialog_custom_title():
    """ErrorDialog supports custom title."""
    dialog = ErrorDialog(message="Test error", title="Custom Error")
    html = to_xml(dialog)

    assert "Custom Error" in html
    assert "Test error" in html


def test_error_dialog_variants():
    """ErrorDialog supports different variants."""
    variants = ["danger", "warning", "info"]

    for variant in variants:
        dialog = ErrorDialog(message="Test", variant=variant)
        html = to_xml(dialog)
        assert f"text-{variant}" in html or f"btn-{variant}" in html


def test_error_dialog_retry_button():
    """ErrorDialog shows retry button when retry_url provided."""
    dialog = ErrorDialog(message="Network error", retry_url="/api/save", retry_text="Try Again")
    html = to_xml(dialog)

    assert "Try Again" in html
    assert "/api/save" in html


def test_error_dialog_no_retry():
    """ErrorDialog hides retry button when no retry_url."""
    dialog = ErrorDialog(message="Error occurred")
    html = to_xml(dialog)

    assert "Retry" not in html
    assert "Try Again" not in html


def test_error_dialog_custom_id():
    """ErrorDialog supports custom modal ID."""
    dialog = ErrorDialog(message="Test", modal_id="custom-error-modal")
    html = to_xml(dialog)

    assert "custom-error-modal" in html


def test_error_dialog_show_immediately():
    """ErrorDialog can show immediately on load."""
    dialog = ErrorDialog(message="Test", show=True)
    html = to_xml(dialog)

    assert "show" in html or "modal-open" in html


def test_error_dialog_oob_swap():
    """ErrorDialog supports HTMX out-of-band swap."""
    dialog = ErrorDialog(message="Backend error", modal_id="error-modal", hx_swap_oob="true")
    html = to_xml(dialog)

    assert "hx-swap-oob" in html


def test_error_dialog_backend_error():
    """ErrorDialog displays backend error messages."""
    backend_msg = "Database connection failed: timeout after 30s"
    dialog = ErrorDialog(message=backend_msg)
    html = to_xml(dialog)

    assert backend_msg in html


def test_error_dialog_custom_classes():
    """ErrorDialog merges custom classes."""
    dialog = ErrorDialog(message="Test", cls="custom-error-dialog")
    html = to_xml(dialog)

    assert "custom-error-dialog" in html
    assert "modal" in html
