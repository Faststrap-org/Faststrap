# ModelMetrics

**Planned** · `@experimental`
!!! warning "Planned Component"
    This component is part of the `faststrap[plots]` / `faststrap[ml]` optional
    extra and has not been implemented yet. The documentation is a preview of
    the planned API.


Composed dashboard card showing comprehensive ML model evaluation metrics: accuracy, precision, recall, F1-score, and optional confusion matrix preview.

---

## Quick Start

```python
from faststrap.components.advance import ModelMetrics

ModelMetrics(
    title="Random Forest Evaluation",
    metrics={
        "Accuracy": "94.2%",
        "Precision": "91.8%",
        "Recall": "89.5%",
        "F1 Score": "90.6%",
    },
    confusion_matrix=[[50, 3], [4, 43]],
    confusion_matrix_labels=["Negative", "Positive"],
)
```

---

## Features

- Grid of named metric values with optional trend indicators
- Compact confusion matrix preview below the metric grid
- Bootstrap card layout with variant support
- Works with sklearn `classification_report` output
- Composable: use standalone or embed in `DashboardGrid`

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Card title |
| `metrics` | `dict[str, str \| tuple[str, str]]` | required | Metric name → value (or value + trend tuple) |
| `confusion_matrix` | `list[list[int]] \| None` | `None` | 2D confusion matrix for inline preview |
| `confusion_matrix_labels` | `list[str] \| None` | `None` | Class labels for the matrix |
| `variant` | `str \| None` | `None` | Bootstrap card variant |
| `columns` | `int` | `2` | Number of metric columns per row |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Pure server-rendered — no JS required for the base view.
- For a full confusion matrix, use the dedicated `ConfusionMatrix` component.
- Marked `@experimental`.
