"""Tests for MapView component."""

from fasthtml.common import to_xml

from faststrap.components.display.map_view import LEAFLET_CSS_URL, LEAFLET_JS_URL, MapView


def _render_parts(parts: tuple[object, ...]) -> str:
    return "\n".join(to_xml(part) for part in parts)


def test_map_view_includes_leaflet_assets_by_default() -> None:
    parts = MapView(latitude=6.5244, longitude=3.3792)
    html = _render_parts(parts)
    assert LEAFLET_CSS_URL in html
    assert LEAFLET_JS_URL in html
    assert "L.map(" in html


def test_map_view_can_skip_asset_injection() -> None:
    parts = MapView(latitude=6.5244, longitude=3.3792, include_assets=False)
    html = _render_parts(parts)
    assert LEAFLET_CSS_URL not in html
    assert LEAFLET_JS_URL not in html
    assert "L.map(" in html


def test_map_view_has_stability_and_registry_metadata() -> None:
    assert getattr(MapView, "__faststrap_experimental__", False) is True
    metadata = getattr(MapView, "__faststrap_metadata__", {})
    assert metadata.get("requires_js") is True


def test_map_view_rejects_invalid_coordinates() -> None:
    try:
        MapView(latitude=120, longitude=3.0)
        raise AssertionError("Expected ValueError for invalid latitude")
    except ValueError as exc:
        assert "latitude must be between -90 and 90" in str(exc)


def test_map_view_popup_uses_plain_js_string_not_template_literal() -> None:
    parts = MapView(latitude=1.0, longitude=2.0, popup_text="${alert(1)}")
    html = _render_parts(parts)
    assert 'marker.bindPopup("${alert(1)}");' in html
