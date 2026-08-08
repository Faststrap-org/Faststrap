# TimeSeriesPlot

**Planned** · `@experimental` · Requires `faststrap[chartjs]`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


Renders a time series line chart with optional moving average overlay. Designed for financial dashboards, monitoring tools, and trend analysis.

---

## Quick Start

```python
from faststrap.components.advance import TimeSeriesPlot
import pandas as pd

df = pd.DataFrame({
    "date": pd.date_range("2026-01-01", periods=30),
    "value": range(30),
})

TimeSeriesPlot(
    dates=df["date"],
    values=df["value"],
    moving_average_window=7,
    title="30-Day Trend with 7-Day Moving Average",
)
```

---

## Features

- Line chart with date axis
- Optional moving average overlay (rolling window)
- Dual-axis support (primary + secondary series)
- Zoom and pan (Chart.js zoom plugin)
- Theme-aware colors

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `dates` | `list \| pd.DatetimeIndex` | required | X-axis date values |
| `values` | `list \| pd.Series` | required | Y-axis numeric values |
| `secondary_values` | `list \| pd.Series \| None` | `None` | Optional secondary Y-axis series |
| `moving_average_window` | `int \| None` | `None` | Rolling window for MA overlay |
| `title` | `str \| None` | `None` | Optional chart title |
| `y_label` | `str \| None` | `None` | Y-axis label |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `height` | `int \| str` | `350` | Chart height |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Requires `faststrap[chartjs]`.
- Moving average is computed server-side using `pd.Series.rolling().mean()`.
- Marked `@experimental`.
