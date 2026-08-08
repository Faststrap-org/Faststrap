"""Tests for Debounce preset."""

from faststrap.presets.interactions import Debounce


def test_debounce_default_delay():
    """Debounce returns default 300ms trigger string."""
    result = Debounce()

    assert "delay:300ms" in result
    assert "changed" in result


def test_debounce_custom_delay():
    """Debounce returns custom delay trigger string."""
    result = Debounce(delay=500)

    assert "delay:500ms" in result


def test_debounce_custom_trigger():
    """Debounce supports custom trigger events."""
    result = Debounce(trigger="keyup")

    assert "keyup" in result
    assert "delay:300ms" in result


def test_debounce_custom_event():
    """Debounce supports custom base event."""
    result = Debounce(event="input", delay=200)

    assert "input" in result
    assert "delay:200ms" in result


def test_debounce_output_is_string():
    """Debounce returns a string suitable for hx-trigger."""
    result = Debounce(delay=100)

    assert isinstance(result, str)
