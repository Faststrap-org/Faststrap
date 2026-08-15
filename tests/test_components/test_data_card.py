"""Tests for DataCard component."""

from fasthtml.common import to_xml

from faststrap.components.display.data_card import DataCard


def test_data_card_renders_card() -> None:
    """DataCard renders a card div."""
    component = DataCard("Model A")
    html = to_xml(component)
    assert "<div" in html
    assert "Model A" in html
    assert "faststrap-data-card" in html


def test_data_card_with_subtitle() -> None:
    """Subtitle is rendered in the header."""
    component = DataCard("Model A", subtitle="v1.0.0")
    html = to_xml(component)
    assert "v1.0.0" in html


def test_data_card_with_status() -> None:
    """Status is rendered as a badge."""
    component = DataCard("Model A", status="active")
    html = to_xml(component)
    assert "bg-success" in html
    assert "active" in html


def test_data_card_with_metrics() -> None:
    """Metrics are rendered as key-value rows."""
    component = DataCard("Model A", metrics={"Accuracy": "95%", "Loss": "0.05"})
    html = to_xml(component)
    assert "Accuracy" in html
    assert "95%" in html
    assert "Loss" in html
    assert "0.05" in html


def test_data_card_with_fields() -> None:
    """Fields are rendered as a metadata table."""
    component = DataCard(
        "Dataset X",
        fields={"Size": "10K rows", "Source": "Internal", "License": "MIT"},
    )
    html = to_xml(component)
    assert "10K rows" in html
    assert "Internal" in html
    assert "MIT" in html


def test_data_card_with_footer() -> None:
    """Footer content is rendered."""
    from fasthtml.common import Button

    component = DataCard("Model A", footer=Button("Deploy", variant="primary"))
    html = to_xml(component)
    assert "Deploy" in html
    assert "card-footer" in html


def test_data_card_merges_custom_classes() -> None:
    """Custom classes are merged."""
    component = DataCard("Model A", cls="my-card")
    html = to_xml(component)
    assert "faststrap-data-card" in html
    assert "my-card" in html


def test_data_card_status_variants() -> None:
    """Status strings map to correct badge variants."""
    for status, expected_cls in [
        ("active", "bg-success"),
        ("failed", "bg-danger"),
        ("pending", "bg-warning"),
        ("unknown", "bg-secondary"),
    ]:
        component = DataCard("X", status=status)
        html = to_xml(component)
        assert expected_cls in html, f"Expected {expected_cls} for status {status}"
