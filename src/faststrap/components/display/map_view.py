"""Leaflet-based map component (experimental, optional/CDN-first)."""

from __future__ import annotations

import json
from typing import Any
from uuid import uuid4

from fasthtml.common import Div, Link, NotStr, Script

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

LEAFLET_VERSION = "1.9.4"
LEAFLET_CSS_URL = f"https://unpkg.com/leaflet@{LEAFLET_VERSION}/dist/leaflet.css"
LEAFLET_JS_URL = f"https://unpkg.com/leaflet@{LEAFLET_VERSION}/dist/leaflet.js"

DEFAULT_TILES_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
DEFAULT_ATTRIBUTION = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'


@experimental
@register(category="display", requires_js=True)
def MapView(
    *,
    latitude: float,
    longitude: float,
    zoom: int = 13,
    height: str = "320px",
    width: str = "100%",
    marker: bool = True,
    popup_text: str | None = None,
    map_id: str | None = None,
    include_assets: bool = True,
    tiles_url: str = DEFAULT_TILES_URL,
    attribution: str = DEFAULT_ATTRIBUTION,
    leaflet_css_url: str = LEAFLET_CSS_URL,
    leaflet_js_url: str = LEAFLET_JS_URL,
    **kwargs: Any,
) -> tuple[Any, ...]:
    """Render an interactive Leaflet map.

    Notes:
    - Experimental API; may evolve before v0.6.0.
    - Leaflet is CDN-first by default to avoid increasing package size.
    """
    if not (-90 <= latitude <= 90):
        msg = f"latitude must be between -90 and 90, got {latitude}"
        raise ValueError(msg)
    if not (-180 <= longitude <= 180):
        msg = f"longitude must be between -180 and 180, got {longitude}"
        raise ValueError(msg)
    if zoom < 0 or zoom > 22:
        msg = f"zoom must be between 0 and 22, got {zoom}"
        raise ValueError(msg)

    resolved_map_id = map_id or f"faststrap-map-{uuid4().hex[:8]}"
    user_cls = kwargs.pop("cls", "")

    container_attrs: dict[str, Any] = {
        "id": resolved_map_id,
        "cls": merge_classes("faststrap-map-view rounded border", user_cls),
        "style": f"height: {height}; width: {width};",
        "role": "region",
        "aria_label": "Interactive map",
    }
    container_attrs.update(convert_attrs(kwargs))
    map_container = Div(**container_attrs)

    marker_block = ""
    if marker:
        marker_block = f"""
const marker = L.marker([{latitude}, {longitude}]).addTo(map);
"""
        if popup_text:
            marker_block += f"marker.bindPopup({json.dumps(popup_text)});"

    init_script = Script(NotStr(f"""
if (window.L) {{
  const map = L.map({resolved_map_id!r}).setView([{latitude}, {longitude}], {zoom});
  L.tileLayer({tiles_url!r}, {{ attribution: {attribution!r} }}).addTo(map);
  {marker_block}
}} else {{
  console.warn("Faststrap MapView: Leaflet was not loaded.");
}}
"""))

    if include_assets:
        return (
            Link(rel="stylesheet", href=leaflet_css_url),
            Script(src=leaflet_js_url),
            map_container,
            init_script,
        )
    return (map_container, init_script)
