"""Tests for Chart component."""

import pytest
from fasthtml.common import to_xml

from faststrap import Chart


def test_chart_svg_requires_safe_flag():
    with pytest.raises(ValueError):
        Chart("<svg></svg>", backend="svg")


def test_chart_svg_allows_safe_flag():
    html = to_xml(Chart("<svg></svg>", backend="svg", allow_unsafe_html=True))
    assert "<svg>" in html


def test_chart_html_backend():
    html = to_xml(Chart("<div>chart</div>", backend="html", allow_unsafe_html=True))
    assert "<div>chart</div>" in html
