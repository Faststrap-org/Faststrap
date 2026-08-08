"""Tests for SwapOnEvent preset."""

from fasthtml.common import to_xml

from faststrap.presets.interactions import SwapOnEvent


def test_swap_on_event_renders_container():
    """SwapOnEvent renders a container div."""
    html = to_xml(SwapOnEvent("Initial content"))

    assert "Initial content" in html
    assert "faststrap-swap-on-event" in html


def test_swap_on_event_default_event_name():
    """SwapOnEvent uses the default event name in data attribute."""
    html = to_xml(SwapOnEvent())

    assert "faststrap:swap" in html
    assert "data-fs-swap-event" in html


def test_swap_on_event_custom_event_and_target():
    """SwapOnEvent accepts custom event name and target."""
    html = to_xml(
        SwapOnEvent(
            "Hello",
            event_name="my:custom-event",
            target="#target",
            swap="outerHTML",
        )
    )

    assert "my:custom-event" in html
    assert "#target" in html
    assert "outerHTML" in html
    assert "data-fs-swap-target" in html
    assert "data-fs-swap" in html
