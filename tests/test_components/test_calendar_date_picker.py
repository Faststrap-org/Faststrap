"""Tests for CalendarDatePicker component."""

import pytest
from fasthtml.common import to_xml

from faststrap import CalendarDatePicker


def test_calendar_date_picker_renders_native_date_input() -> None:
    html = to_xml(
        CalendarDatePicker(
            "publish_date",
            label="Publish date",
            value="2026-05-07",
            min_date="2026-01-01",
            max_date="2026-12-31",
        )
    )

    assert "faststrap-calendar-date-picker" in html
    assert 'type="date"' in html
    assert 'name="publish_date"' in html
    assert 'value="2026-05-07"' in html
    assert 'min="2026-01-01"' in html
    assert 'max="2026-12-31"' in html
    assert "Publish date" in html


def test_calendar_date_picker_supports_htmx_auto_submit() -> None:
    html = to_xml(
        CalendarDatePicker(
            endpoint="/events",
            hx_target="#events",
            auto=True,
            push_url=True,
            clear_label="Clear",
        )
    )

    assert 'hx-get="/events"' in html
    assert 'hx-target="#events"' in html
    assert 'hx-trigger="change delay:300ms"' in html
    assert 'hx-push-url="true"' in html
    assert "Clear" in html


def test_calendar_date_picker_rejects_unknown_method() -> None:
    with pytest.raises(ValueError, match="method must be"):
        CalendarDatePicker(method="patch")  # type: ignore[arg-type]


def test_calendar_date_picker_get_form_omits_enctype() -> None:
    html = to_xml(CalendarDatePicker())
    assert "enctype" not in html


def test_calendar_date_picker_controls_share_baseline() -> None:
    """Input wrapper margin is neutralized so buttons align with the control."""
    html = to_xml(CalendarDatePicker(label="Date"))
    assert "mb-3" not in html
    assert "align-items-end" in html
