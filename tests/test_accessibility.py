"""Tests for accessibility helpers."""

from fasthtml.common import to_xml

from faststrap import FocusTrap, LiveRegion, SkipLink, VisuallyHidden


def test_skip_link():
    html = to_xml(SkipLink(target="#content", text="Skip"))
    assert 'href="#content"' in html
    assert "Skip" in html


def test_visually_hidden():
    html = to_xml(VisuallyHidden("Only screen readers"))
    assert "visually-hidden" in html


def test_live_region():
    html = to_xml(LiveRegion("Saved", politeness="assertive"))
    assert 'aria-live="assertive"' in html
    assert 'role="alert"' in html


def test_focus_trap():
    html = to_xml(FocusTrap("Dialog"))
    assert 'data-fs-focus-trap="true"' in html
    assert 'tabindex="-1"' in html
