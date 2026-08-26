# MapView (Experimental)

`MapView` renders an interactive Leaflet map with optional CDN asset injection.

## Import

```python
from faststrap import MapView
```

## Basic Usage

```python
MapView(
    latitude=6.5244,
    longitude=3.3792,
    zoom=12,
    popup_text="Lagos",
)
```

## Key Options

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `latitude` | `float` | required | Center latitude. Must be between `-90` and `90`. |
| `longitude` | `float` | required | Center longitude. Must be between `-180` and `180`. |
| `zoom` | `int` | `13` | Leaflet zoom level, `0` to `22`. |
| `height` | `str` | `"320px"` | Map container height. |
| `width` | `str` | `"100%"` | Map container width. |
| `marker` | `bool` | `True` | Place a marker at the center coordinate. |
| `popup_text` | `str \| None` | `None` | Optional marker popup text. |
| `map_id` | `str \| None` | `None` | Explicit DOM ID. Auto-generated when omitted. |
| `include_assets` | `bool` | `True` | Inject Leaflet CSS/JS from CDN. |
| `tiles_url` | `str` | OpenStreetMap tiles | Leaflet tile URL template. |
| `attribution` | `str` | OpenStreetMap attribution | Tile attribution HTML. |
| `leaflet_css_url` | `str` | Leaflet CDN CSS | Override CSS URL. |
| `leaflet_js_url` | `str` | Leaflet CDN JS | Override JS URL. |
| `**kwargs` | `Any` | | Extra container attributes. |

## Reusing Leaflet Assets

If the page already loads Leaflet once, set `include_assets=False` for additional maps:

```python
MapView(
    latitude=40.7128,
    longitude=-74.0060,
    include_assets=False,
)
```

## Custom Tile Providers

```python
MapView(
    latitude=51.5074,
    longitude=-0.1278,
    tiles_url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    popup_text="London",
)
```

## Size Implication

Leaflet is CDN-first in this component, so Faststrap wheel size does not
increase unless you choose to vendor assets yourself.

## Accessibility

- Provide an accessible label or surrounding context for the map container.
- If `popup_text` is used, ensure it conveys the same information as any nearby text.

## API Reference

::: faststrap.components.display.map_view.MapView
