"""Tests for FormGroup error mapping helpers."""

from fasthtml.common import Input, to_xml

from faststrap.components.forms import (
    FormGroupFromErrors,
    extract_field_error,
    map_formgroup_validation,
)


def test_extract_field_error_string():
    assert extract_field_error({"email": "Invalid email"}, "email") == "Invalid email"


def test_extract_field_error_list():
    assert extract_field_error({"email": ["Invalid email"]}, "email") == "Invalid email"


def test_map_formgroup_validation():
    result = map_formgroup_validation({"name": "Required"}, "name")
    assert result["is_invalid"] is True
    assert result["error"] == "Required"


def test_formgroup_from_errors():
    html = to_xml(
        FormGroupFromErrors(
            Input(name="email"), field="email", errors={"email": "Invalid"}, label="Email"
        )
    )
    assert "invalid-feedback" in html
    assert "is-invalid" in html
