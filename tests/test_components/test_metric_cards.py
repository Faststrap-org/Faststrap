"""Tests for metric card components."""

from fasthtml.common import to_xml

from faststrap import KPICard, MetricCard, TrendCard


def test_metric_card_delta():
    html = to_xml(MetricCard("Revenue", "$10", delta="+5%", delta_type="up"))
    assert "Revenue" in html
    assert "$10" in html
    assert "+5%" in html
    assert "text-success" in html


def test_trend_card_sparkline():
    html = to_xml(TrendCard("Visitors", 100, sparkline="<svg></svg>", sparkline_safe=True))
    assert "Visitors" in html
    assert "<svg>" in html


def test_kpi_card_metrics():
    html = to_xml(
        KPICard(
            "KPIs",
            metrics=[
                ("Sales", "$10", "+2%", "up"),
                ("Churn", "2%", "-0.5%", "down"),
            ],
        )
    )
    assert "Sales" in html
    assert "Churn" in html
