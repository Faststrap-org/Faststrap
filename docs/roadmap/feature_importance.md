# FeatureImportance

**Planned** · `@experimental`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


Renders a horizontal bar chart showing feature importance scores. Compatible with sklearn tree-based models, SHAP values, and custom importance arrays.

---

## Quick Start

```python
from faststrap.components.advance import FeatureImportance
import numpy as np

FeatureImportance(
    features=["age", "income", "score", "hours"],
    importances=[0.35, 0.28, 0.22, 0.15],
    title="Feature Importance — Random Forest",
)
```

---

## Features

- Horizontal bar chart sorted by importance (highest at top)
- Auto-scales to percentage or raw importance values
- Optional top-N feature limit
- Color-coded bars (Bootstrap variant or custom)
- Accepts sklearn model `.feature_importances_` directly

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `features` | `list[str]` | required | Feature names |
| `importances` | `list[float]` | required | Importance scores (same order as features) |
| `model` | `Any \| None` | `None` | sklearn model (extracts `.feature_importances_` and `.feature_names_in_`) |
| `top_n` | `int \| None` | `None` | Limit to top N features |
| `normalize` | `bool` | `True` | Scale importances to 0–100% |
| `title` | `str \| None` | `None` | Optional chart title |
| `bar_variant` | `str` | `"primary"` | Bootstrap color variant for bars |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Pure server-rendered — no JS required.
- Marked `@experimental`.
