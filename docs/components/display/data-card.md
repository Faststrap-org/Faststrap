# DataCard

`@experimental`

Structured metadata card for models, datasets, experiments, and entities.

---

## Quick Start

```python
from faststrap import DataCard

DataCard(
    "ResNet-50",
    subtitle="Image Classification",
    status="active",
    metrics={"Accuracy": "95.2%", "Loss": "0.04"},
    fields={"Framework": "PyTorch", "Version": "v2.1"},
)
```

---

## Features

- Title, subtitle, and status badge
- Metrics section for key-value pairs
- Metadata table for detailed fields
- Optional footer for actions

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Primary title or entity name. |
| `subtitle` | `str \| None` | `None` | Optional secondary description. |
| `status` | `str \| None` | `None` | Status string rendered as a badge. |
| `metrics` | `dict[str, str] \| None` | `None` | Metric name → value pairs. |
| `fields` | `dict[str, str] \| None` | `None` | Field name → value pairs rendered as a table. |
| `footer` | `Any \| None` | `None` | Optional footer content. |
| `variant` | `str` | `"default"` | Visual variant. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

---

## Usage Examples

### Model Card

```python
DataCard(
    "GPT-4o",
    subtitle="OpenAI Multimodal",
    status="active",
    metrics={"Parameters": "1.8T", "Context": "128K"},
    fields={"Provider": "OpenAI", "Type": "LLM", "License": "Proprietary"},
)
```

### Dataset Card

```python
DataCard(
    "CIFAR-10",
    subtitle="Image Classification",
    status="completed",
    metrics={"Samples": "60K", "Classes": "10", "Size": "163 MB"},
    fields={"Format": "Pickle", "Split": "50K/10K"},
)
```

### Experiment Run

```python
DataCard(
    "Run #42",
    subtitle="2024-01-15",
    status="failed",
    metrics={"Duration": "2h 34m", "Epochs": "50"},
    fields={"Learning Rate": "0.001", "Batch Size": "32"},
    footer=Button("Retry", variant="outline-primary"),
)
```

---

## Notes

- Status strings are mapped to Bootstrap badge variants automatically.
- Marked `@experimental`.

---

## API Reference

::: faststrap.components.display.data_card.DataCard
    options:
        show_source: true
        heading_level: 4
