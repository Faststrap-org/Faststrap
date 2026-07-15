# ROCCurve

**Planned** · `@experimental`

Renders a Receiver Operating Characteristic (ROC) curve with AUC annotation. Supports binary and multi-class classification with overlaid curves.

---

## Quick Start

```python
from faststrap.components.advance import ROCCurve
from sklearn.metrics import roc_curve, auc

fpr, tpr, _ = roc_curve(y_true, y_scores)

ROCCurve(
    fpr=fpr,
    tpr=tpr,
    auc_score=auc(fpr, tpr),
    title="ROC Curve — Binary Classifier",
)
```

---

## Features

- Single or multi-class ROC curves on the same axes
- AUC score annotation
- Diagonal random-classifier reference line
- Theme-aware colors (light/dark)
- Accepts pre-computed fpr/tpr arrays or sklearn `RocCurveDisplay` data

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `fpr` | `list \| np.ndarray` | required (or `curves`) | False positive rate array |
| `tpr` | `list \| np.ndarray` | required (or `curves`) | True positive rate array |
| `curves` | `list[dict] \| None` | `None` | Multi-class: list of `{fpr, tpr, label, auc}` dicts |
| `auc_score` | `float \| None` | `None` | AUC score to annotate |
| `title` | `str \| None` | `None` | Optional chart title |
| `show_random_line` | `bool` | `True` | Show diagonal reference line |
| `responsive` | `bool` | `True` | Full-width responsive wrapper |
| `height` | `int \| str` | `350` | Chart height |
| `**kwargs` | `Any` | | Extra wrapper attributes |

---

## Notes

- Pure server-rendered — no JS required for static curves.
- Marked `@experimental`.
