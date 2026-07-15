"""Tests for OTPInput and OTPInputGroup components."""

from fasthtml.common import to_xml

from faststrap.components.forms import OTPInput, OTPInputGroup


# --- OTPInput (single-field, zero-JS) ---


def test_otp_input_basic():
    """OTPInput renders a single input field."""
    otp = OTPInput()
    html = to_xml(otp)

    assert 'inputmode="numeric"' in html
    assert 'maxlength="6"' in html
    assert 'autocomplete="one-time-code"' in html


def test_otp_input_custom_length():
    """OTPInput supports custom length."""
    otp = OTPInput(length=4)
    html = to_xml(otp)

    assert 'maxlength="4"' in html
    assert 'pattern="\\d{4}"' in html


def test_otp_input_custom_name():
    """OTPInput supports custom name attribute."""
    otp = OTPInput(name="verification")
    html = to_xml(otp)

    assert 'name="verification"' in html


def test_otp_input_size_sm():
    """OTPInput supports small size."""
    otp = OTPInput(size="sm")
    html = to_xml(otp)

    assert "form-control-sm" in html


def test_otp_input_size_lg():
    """OTPInput supports large size."""
    otp = OTPInput(size="lg")
    html = to_xml(otp)

    assert "form-control-lg" in html


def test_otp_input_accessibility():
    """OTPInput has proper aria label."""
    otp = OTPInput(length=6)
    html = to_xml(otp)

    assert "verification code" in html.lower()


def test_otp_input_custom_placeholder():
    """OTPInput supports custom placeholder."""
    otp = OTPInput(placeholder="*")
    html = to_xml(otp)

    assert 'placeholder="******"' in html


def test_otp_input_custom_classes():
    """OTPInput merges custom classes."""
    otp = OTPInput(cls="my-class")
    html = to_xml(otp)

    assert "my-class" in html


# --- OTPInputGroup (multi-field, JS-enhanced) ---


def test_otp_group_basic():
    """OTPInputGroup renders multiple input fields."""
    group = OTPInputGroup()
    html = to_xml(group)

    assert 'data-fs-otp-group="true"' in html
    assert 'data-otp-index="0"' in html
    assert 'data-otp-index="5"' in html


def test_otp_group_custom_length():
    """OTPInputGroup supports custom length."""
    group = OTPInputGroup(length=4)
    html = to_xml(group)

    assert 'data-otp-index="3"' in html
    assert 'data-otp-length="4"' in html


def test_otp_group_individual_inputs():
    """OTPInputGroup renders individual digit inputs."""
    group = OTPInputGroup(length=4)
    html = to_xml(group)

    assert 'maxlength="1"' in html
    assert 'inputmode="numeric"' in html
    assert "otp-digit-input" in html


def test_otp_group_gap():
    """OTPInputGroup supports gap between inputs."""
    group = OTPInputGroup(gap=3)
    html = to_xml(group)

    assert "gap-3" in html


def test_otp_group_no_gap():
    """OTPInputGroup supports zero gap."""
    group = OTPInputGroup(gap=0)
    html = to_xml(group)

    assert "gap-0" not in html


def test_otp_group_autofocus():
    """OTPInputGroup supports autofocus on first input."""
    group = OTPInputGroup(autofocus=True)
    html = to_xml(group)

    assert 'autofocus="true"' in html


def test_otp_group_size():
    """OTPInputGroup supports size variants."""
    group = OTPInputGroup(size="lg")
    html = to_xml(group)

    assert "form-control-lg" in html


def test_otp_group_variant():
    """OTPInputGroup supports color variants."""
    group = OTPInputGroup(variant="success")
    html = to_xml(group)

    assert "border-success" in html


def test_otp_group_custom_classes():
    """OTPInputGroup merges custom classes."""
    group = OTPInputGroup(cls="my-group")
    html = to_xml(group)

    assert "my-group" in html


def test_otp_group_data_attributes():
    """OTPInputGroup handles data attributes."""
    group = OTPInputGroup(data_form="login")
    html = to_xml(group)

    assert 'data-form="login"' in html
