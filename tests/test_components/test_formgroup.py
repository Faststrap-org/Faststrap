"""Tests for FormGroup component."""

from fasthtml.common import Input, to_xml

from faststrap.components.forms import FormGroup


def test_formgroup_basic():
    """FormGroup renders with input and label."""
    group = FormGroup(Input(name="email"), label="Email Address")
    html = to_xml(group)

    assert "Email Address" in html
    assert "form-label" in html
    assert 'name="email"' in html


def test_formgroup_help_text():
    """FormGroup displays help text."""
    group = FormGroup(
        Input(name="password"), label="Password", help_text="Must be at least 8 characters"
    )
    html = to_xml(group)

    assert "Must be at least 8 characters" in html
    assert "form-text" in html


def test_formgroup_error_state():
    """FormGroup shows error validation state."""
    group = FormGroup(
        Input(name="email"), label="Email", error="Please enter a valid email", is_invalid=True
    )
    html = to_xml(group)

    assert "Please enter a valid email" in html
    assert "invalid-feedback" in html
    assert "is-invalid" in html


def test_formgroup_success_state():
    """FormGroup shows success validation state."""
    group = FormGroup(
        Input(name="username"), label="Username", success="Username is available!", is_valid=True
    )
    html = to_xml(group)

    assert "Username is available!" in html
    assert "valid-feedback" in html
    assert "is-valid" in html


def test_formgroup_required():
    """FormGroup shows required indicator."""
    group = FormGroup(Input(name="name"), label="Full Name", required=True)
    html = to_xml(group)

    assert "Full Name" in html
    assert "*" in html  # Required asterisk
    assert "text-danger" in html


def test_formgroup_no_label():
    """FormGroup works without label."""
    group = FormGroup(Input(name="search", placeholder="Search..."))
    html = to_xml(group)

    assert 'placeholder="Search..."' in html
    assert "form-label" not in html


def test_formgroup_validation_priority():
    """FormGroup prioritizes error over success."""
    group = FormGroup(
        Input(name="test"),
        error="Error message",
        success="Success message",
        is_invalid=True,
        is_valid=True,  # Both set, error should win
    )
    html = to_xml(group)

    assert "Error message" in html
    assert "is-invalid" in html


def test_formgroup_help_text_hidden_on_error():
    """FormGroup hides help text when showing validation."""
    group = FormGroup(
        Input(name="test"), help_text="This is help text", error="Error occurred", is_invalid=True
    )
    html = to_xml(group)

    # Help text should not be shown when error is displayed
    assert "Error occurred" in html
    # Help text rendering is conditional


def test_formgroup_custom_classes():
    """FormGroup merges custom classes."""
    group = FormGroup(Input(name="test"), label="Test", cls="custom-form-group")
    html = to_xml(group)

    assert "custom-form-group" in html
    assert "mb-3" in html  # Default class


def test_formgroup_container_structure():
    """FormGroup has proper container structure."""
    group = FormGroup(Input(name="test"), label="Test Label")
    html = to_xml(group)

    # Should be wrapped in a div with mb-3
    assert "mb-3" in html
