# RangeSlider

Single or dual range slider with optional live value display.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Score</label>
      <input type="range" class="form-range" min="0" max="100" value="75">
      <span class="small text-muted">75</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import RangeSlider

RangeSlider("score", min_value=0, max_value=100, value=75, label="Score")
```
  </div>
</div>

---

## Dual Range

```python
RangeSlider(
    "budget",
    dual=True,
    min_selected=200,
    max_selected=1200,
    min_name="min_budget",
    max_name="max_budget",
)
```

Dual mode renders two range inputs. Validate that min is not greater than max server-side.

---

## Value Display

```python
RangeSlider(
    "score",
    value=25,
    show_value=True,
    value_suffix="%",
)
```

---

## Step Control

```python
RangeSlider("score", min_value=0, max_value=100, step=5)
```

---

## API Reference

::: faststrap.components.forms.range_slider.RangeSlider
    options:
        show_source: true
        heading_level: 4
