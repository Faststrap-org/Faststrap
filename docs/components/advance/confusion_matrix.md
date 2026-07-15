# ConfusionMatrix

**Planned** · `@experimental`

Renders a confusion matrix from sklearn-compatible true/predicted label arrays. Displays a color-coded grid with per-class counts and optional normalization.

---

## Quick Start

```python
from faststrap.components.advance import ConfusionMatrix
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 1, 2, 2, 2]
y_pred = [0, 1, 2, 2, 1, 2]

ConfusionMatrix(
    y_true,
    y_pred,
    labels=["Cat", "Dog", "Bird"],
    title="Model Confusion Matrix",
)
```

---

## Features

- Accepts raw label arrays or a pre-computed sklearn confusion matrix
- Optional normalization (row-wise, column-wise, or all)
- Color-coded cells (darker = higher count)
- Per-class precision/recall summary row/column
- Labels for class names

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `y_true` | `list \| np.ndarray` | required (or `matrix`) | True labels |
| `y_pred` | `list \| np.ndarray` | required (or `matrix`) | Predicted labels |
| `matrix` | `np.ndarray \| None` | `None` | Pre-computed confusion matrix (skips y_true/y_pred) |
| `labels` | `list[str] \| None` | `None` | Class names for axis labels |
| `normalize` | `"true" \| "pred" \| "all" \| None` | `None` | Normalization mode |
| `title` | `str \| None` | `None` | Optional title |
| `show_counts` | `bool` | `True` | Show numeric counts in cells |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Pure server-rendered — no JS required for the base visualization.
- Uses Bootstrap grid and utility classes for layout.
- Marked `@experimental`.
