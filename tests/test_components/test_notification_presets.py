"""Tests for notification preset helpers."""

from fasthtml.common import to_xml

from faststrap.components.feedback import (
    ErrorToast,
    InfoToast,
    NoticeAlert,
    NoticeToast,
    SuccessToast,
    WarningToast,
)


def test_notice_toast():
    html = to_xml(NoticeToast("Saved", kind="success"))
    assert "toast" in html
    assert "text-bg-success" in html


def test_notice_alert():
    html = to_xml(NoticeAlert("Failed", kind="danger"))
    assert "alert-danger" in html


def test_variant_helpers():
    assert "text-bg-success" in to_xml(SuccessToast("ok"))
    assert "text-bg-danger" in to_xml(ErrorToast("no"))
    assert "text-bg-warning" in to_xml(WarningToast("watch"))
    assert "text-bg-info" in to_xml(InfoToast("note"))
