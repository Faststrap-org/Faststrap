# LiveChart

**Planned** · `@experimental` · Requires `faststrap[chartjs]`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


SSE-powered auto-updating Chart.js chart. Pushes new data points from the server and the chart updates in real time without page reloads.

---

## Quick Start

```python
from faststrap.components.advance import LiveChart
from faststrap.presets import SSEStream

# Server route
@app.get("/chart-stream")
async def chart_stream():
    async for value in data_generator():
        yield SSEStream.event("data", json.dumps({"x": timestamp(), "y": value}))

# Template
LiveChart(
    endpoint="/chart-stream",
    chart_type="line",
    title="Live Sensor Readings",
)
```

---

## Features

- Server-Sent Events (SSE) for real-time data push
- Supports all Chart.js chart types (line, bar, scatter, etc.)
- Configurable update strategy: append, replace window, or full replace
- Automatic reconnection on connection loss
- Works with the existing `SSETarget` infrastructure

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | required | SSE endpoint URL |
| `chart_type` | `str` | `"line"` | Chart.js chart type |
| `title` | `str \| None` | `None` | Optional chart title |
| `max_points` | `int \| None` | `None` | Maximum data points to retain |
| `update_strategy` | `"append" \| "window" \| "replace"` | `"append"` | How new data is applied |
| `window_size` | `int` | `50` | Points retained when using `window` strategy |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `height` | `int \| str` | `300` | Chart height |
| `reconnect` | `bool` | `True` | Auto-reconnect on SSE error |
| `retry_ms` | `int \| None` | `None` | Reconnect delay in milliseconds |
| `with_credentials` | `bool` | `False` | Send credentials with SSE request |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Requires `faststrap[chartjs]`.
- The SSE endpoint should emit events with JSON `{x, y}` or `{labels, datasets}` payloads.
- Marked `@experimental`.
