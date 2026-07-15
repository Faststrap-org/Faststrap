# GeoMap

**Planned** · `@experimental`

Embeds a lightweight geographic map view. Builds on the existing `MapView` component with additional data-point overlay support.

---

## Quick Start

```python
from faststrap.components.advance import GeoMap

GeoMap(
    center=[51.5074, -0.1278],
    zoom=12,
    points=[
        {"lat": 51.5074, "lon": -0.1278, "label": "London"},
        {"lat": 48.8566, "lon": 2.3522, "label": "Paris"},
    ],
    title="Office Locations",
)
```

---

## Features

- OpenStreetMap-based tile rendering (no API key required)
- Customizable center coordinates and zoom level
- Point markers with tooltips
- Polygon/polyline overlay for regions
- Responsive full-width or fixed-size wrapper

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `center` | `list[float]` | `[51.5074, -0.1278]` | `[lat, lon]` center coordinates |
| `zoom` | `int` | `10` | Initial zoom level |
| `points` | `list[dict] \| None` | `None` | Markers: `{lat, lon, label, color}` |
| `polygons` | `list[list[list[float]]] \| None` | `None` | Polygon overlays as `[lat, lon]` coordinate rings |
| `title` | `str \| None` | `None` | Optional title |
| `height` | `int \| str` | `400` | Map height |
| `tile_url` | `str \| None` | `None` | Custom tile URL (defaults to OSM) |
| `attribution` | `str \| None` | `None` | Map attribution text |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Extends the existing `MapView` component.
- Uses Leaflet.js for client-side map rendering (small JS footprint).
- Marked `@experimental`.
