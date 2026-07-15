# DistributionPlot

**Planned** · `@experimental` · Requires `faststrap[chartjs]`

Renders a histogram with optional KDE (kernel density estimation) overlay from a pandas Series or numpy array. Designed for exploratory data analysis dashboards.

---

## Quick Start

```python
from faststrap.components.advance import DistributionPlot
import pandas as pd

data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5])

DistributionPlot(
    data,
    bins=10,
    kde=True,
    title="Score Distribution",
)
```

---

## Features

- Histogram with configurable bin count
- Optional KDE overlay line
- Theme-aware colors (adapts to light/dark mode)
- Responsive sizing via Bootstrap utilities
- Accepts `pandas.Series`, `pandas.DataFrame` column, or `numpy.ndarray`

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `pd.Series \| np.ndarray` | required | Numeric data to visualize |
| `bins` | `int` | `10` | Number of histogram bins |
| `kde` | `bool` | `False` | Show KDE overlay curve |
| `title` | `str \| None` | `None` | Optional chart title |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `height` | `int \| str` | `300` | Chart height in pixels or CSS value |
| `theme_colors` | `dict \| None` | `None` | Override bar and line colors |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Requires `faststrap[chartjs]` for the Chart.js rendering backend.
- For server-side rendering without JS, consider wrapping `matplotlib` output with `Chart()`.
- Marked `@experimental` — API may change before stable release.
