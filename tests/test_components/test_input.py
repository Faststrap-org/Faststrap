"""Tests for Input component."""

from fasthtml.common import to_xml

from faststrap.components.forms import Input


def test_input_basic():
    """Input renders with basic attributes."""
    inp = Input("email")
    html = to_xml(inp)

    assert 'name="email"' in html
    assert 'type="text"' in html
    assert "form-control" in html


def test_input_types():
    """Input supports all input types."""
    types = ["email", "password", "number", "tel", "url", "search", "date", "time"]

    for input_type in types:
        inp = Input("field", input_type=input_type)
        html = to_xml(inp)
        assert f'type="{input_type}"' in html


def test_input_with_label():
    """Input with label wraps in div."""
    inp = Input("username", label="Username")
    html = to_xml(inp)

    assert "Username" in html
    assert "form-label" in html
    assert "mb-3" in html  # Wrapper div


def test_input_with_help_text():
    """Input supports help text."""
    inp = Input("email", help_text="Enter your email")
    html = to_xml(inp)

    assert "Enter your email" in html
    assert "form-text" in html
    assert "text-muted" in html


def test_input_sizes():
    """Input supports size variants."""
    small = Input("field", size="sm")
    large = Input("field", size="lg")

    assert "form-control-sm" in to_xml(small)
    assert "form-control-lg" in to_xml(large)


def test_input_placeholder():
    """Input supports placeholder."""
    inp = Input("email", placeholder="Enter email")
    html = to_xml(inp)

    assert 'placeholder="Enter email"' in html


def test_input_value():
    """Input can have initial value."""
    inp = Input("username", value="john_doe")
    html = to_xml(inp)

    assert 'value="john_doe"' in html


def test_input_disabled():
    """Input can be disabled."""
    inp = Input("field", disabled=True)
    html = to_xml(inp)

    assert "disabled" in html


def test_input_readonly():
    """Input can be readonly."""
    inp = Input("field", readonly=True)
    html = to_xml(inp)

    assert "readonly" in html


def test_input_required():
    """Input can be required."""
    inp = Input("email", label="Email", required=True)
    html = to_xml(inp)

    assert "required" in html
    assert "*" in html  # Required indicator


def test_input_id_label_linkage():
    """Input ID links to label correctly."""
    inp = Input("email", label="Email Address")
    html = to_xml(inp)

    assert 'id="email"' in html
    assert 'for="email"' in html


def test_input_custom_id():
    """Input accepts custom ID."""
    inp = Input("email", label="Email", id="custom_id")
    html = to_xml(inp)

    assert 'id="custom_id"' in html
    assert 'for="custom_id"' in html


def test_input_aria_describedby():
    """Input has aria-describedby for help text."""
    inp = Input("email", help_text="Help text")
    html = to_xml(inp)

    assert 'aria-describedby="email-help"' in html
    assert 'id="email-help"' in html


def test_input_htmx():
    """Input supports HTMX attributes."""
    inp = Input("email", hx_post="/validate", hx_trigger="blur")
    html = to_xml(inp)

    assert 'hx-post="/validate"' in html
    assert 'hx-trigger="blur"' in html


def test_input_custom_classes():
    """Input merges custom classes."""
    inp = Input("field", cls="custom-input")
    html = to_xml(inp)

    assert "form-control" in html
    assert "custom-input" in html


def test_input_data_attributes():
    """Input handles data attributes."""
    inp = Input("field", data_validation="email")
    html = to_xml(inp)

    assert 'data-validation="email"' in html


def test_input_without_wrapper():
    """Input without label/help returns just input."""
    inp = Input("email", input_type="email")
    html = to_xml(inp)

    assert "mb-3" not in html  # No wrapper div
    assert "form-control" in html


def test_input_validation():
    """Input supports validation states."""
    # Valid
    valid = Input("username", validation_state="valid", validation_message="Looks good!")
    html_valid = to_xml(valid)
    assert "is-valid" in html_valid
    assert "valid-feedback" in html_valid
    assert "Looks good!" in html_valid

    # Invalid
    invalid = Input("username", validation_state="invalid", validation_message="Bad username!")
    html_invalid = to_xml(invalid)
    assert "is-invalid" in html_invalid
    assert "invalid-feedback" in html_invalid
    assert "Bad username!" in html_invalid
