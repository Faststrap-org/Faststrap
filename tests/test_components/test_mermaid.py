"""Tests for Mermaid component."""

from fasthtml.common import to_xml

from faststrap.components.display.mermaid import Mermaid


def test_mermaid_component_renders_attrs() -> None:
    """Mermaid component renders data attributes and classes."""
    component = Mermaid(
        "graph TD; A-->B;",
        theme="dark",
        security_level="strict",
        min_width="280px",
    )
    html = to_xml(component)
    assert "mermaid" in html
    assert "faststrap-mermaid" in html
    assert "data-fs-mermaid" in html
    assert 'data-fs-mermaid-theme="dark"' in html
    assert 'data-fs-mermaid-security="strict"' in html
    assert "min-width: 280px" in html
