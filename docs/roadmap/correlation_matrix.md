# CorrelationMatrix

**Planned** · `@experimental` · Requires `faststrap[chartjs]`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


Renders a correlation heatmap from a pandas DataFrame. Useful for EDA dashboards, feature selection interfaces, and data profiling tools.

---

## Quick Start

```python
from faststrap.components.advance import CorrelationMatrix
import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": [3, 2, 1], "c": [2, 3, 1]})

CorrelationMatrix(
    df,
    title="Feature Correlations",
    annotate=True,
)
```

---

## Features

- Automatic correlation computation from DataFrame
- Color-coded heatmap with diverging color scale
- Optional numeric annotation inside cells
- Option to mask the upper triangle (since correlation matrices are symmetric)
- Theme-aware (light/dark mode color scale)

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `pd.DataFrame` | required | DataFrame with numeric columns |
| `columns` | `list[str] \| None` | `None` | Subset of columns to correlate |
| `method` | `"pearson" \| "spearman" \| "kendall"` | `"pearson"` | Correlation method |
| `annotate` | `bool` | `True` | Show correlation values in cells |
| `mask_upper` | `bool` | `False` | Mask the upper triangle |
| `title` | `str \| None` | `None` | Optional chart title |
| `colormap` | `str \| None` | `None` | Override the diverging color map |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Requires `faststrap[chartjs]`.
- Correlation is computed server-side using `DataFrame.corr()`.
- Marked `@experimental` — API may change.
