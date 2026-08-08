# LiveMetric

**Planned** · `@experimental`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


SSE-powered real-time metric card. Displays a numeric value that updates as the server pushes new data. Extends the `MetricCard` pattern with live streaming.

---

## Quick Start

```python
from faststrap.components.advance import LiveMetric

LiveMetric(
    title="Active Users",
    endpoint="/metrics/stream",
    value_key="count",
    delta_key="change",
    format="comma",
)
```

---

## Features

- SSE-powered real-time value updates
- Automatic trend/delta display (up/down/neutral)
- Number formatting (comma-separated, currency, percentage)
- Smooth transition animation on value change
- Falls back to static display if SSE is unavailable

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | required | SSE endpoint URL |
| `title` | `str` | required | Metric label |
| `value_key` | `str` | `"value"` | JSON key for the metric value |
| `delta_key` | `str \| None` | `None` | JSON key for the delta/trend value |
| `format` | `"plain" \| "comma" \| "currency" \| "percent"` | `"plain"` | Number formatting |
| `prefix` | `str \| None` | `None` | Value prefix (e.g. `"$"`) |
| `suffix` | `str \| None` | `None` | Value suffix (e.g. `"%"`) |
| `variant` | `str \| None` | `None` | Bootstrap card variant |
| `reconnect` | `bool` | `True` | Auto-reconnect on SSE error |
| `aria_live` | `str` | `"polite"` | ARIA live region politeness |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- No optional extra required — uses the built-in SSE infrastructure.
- Marked `@experimental`.
