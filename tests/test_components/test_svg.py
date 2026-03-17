"""Tests for SVG rendering component."""

from types import SimpleNamespace

import pytest
from fasthtml.common import to_xml

from faststrap.components.display import svg as svg_module
from faststrap.components.display.svg import Svg, render_svg


def test_render_svg_sanitizes_markup(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sanitization strips unsafe markup by default."""

    def fake_import(name: str):
        if name == "bleach":
            return SimpleNamespace(
                clean=lambda html, **_kwargs: html.replace("<script>x()</script>", "")
            )
        raise ImportError

    monkeypatch.setattr(svg_module.importlib, "import_module", fake_import)
    rendered = render_svg("<svg></svg><script>x()</script>")
    assert "<svg" in rendered
    assert "<script>" not in rendered


def test_svg_component_wraps_content(monkeypatch: pytest.MonkeyPatch) -> None:
    """Svg component returns a div with SVG markup inside."""

    def fake_import(name: str):
        if name == "bleach":
            return SimpleNamespace(clean=lambda html, **_kwargs: html)
        raise ImportError

    monkeypatch.setattr(svg_module.importlib, "import_module", fake_import)
    component = Svg("<svg></svg>", cls="mt-3")
    html = to_xml(component)
    assert "faststrap-svg mt-3" in html
    assert "<svg" in html


def test_svg_missing_dependency_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """A clear error is raised if bleach dependency is absent."""

    def fake_import(_name: str):
        raise ImportError

    monkeypatch.setattr(svg_module.importlib, "import_module", fake_import)
    with pytest.raises(ImportError, match="Install with `pip install faststrap\\[markdown\\]`"):
        render_svg("<svg></svg>")
