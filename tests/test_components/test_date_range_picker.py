"""Tests for DateRangePicker component."""

from fasthtml.common import to_xml

from faststrap import DateRangePicker


def test_date_range_picker_basic():
    html = to_xml(DateRangePicker())

    assert "faststrap-date-range" in html
    assert 'data-fs-date-range="true"' in html
    assert "start_date" in html
    assert "end_date" in html


def test_date_range_picker_presets():
    html = to_xml(
        DateRangePicker(
            presets=[("Last 7 days", "2026-01-01", "2026-01-07")],
            endpoint="/reports",
            hx_target="#results",
        )
    )

    assert "Last 7 days" in html
    assert 'data-fs-date-preset="true"' in html
    assert 'data-fs-date-start="2026-01-01"' in html
    assert 'data-fs-date-end="2026-01-07"' in html
    assert 'data-fs-date-start-name="start_date"' in html
    assert 'data-fs-date-end-name="end_date"' in html


def test_date_range_picker_presets_can_auto_submit():
    html = to_xml(
        DateRangePicker(
            presets=[("Last 7 days", "2026-01-01", "2026-01-07")],
            endpoint="/reports",
            method="post",
            auto=True,
        )
    )

    assert 'method="post"' in html
    assert 'action="/reports"' in html
    assert 'data-fs-date-preset-submit="true"' in html
