# Range Slider

The `RangeSlider` component creates a numeric range input with optional dual-handle support and value display.

## Quick Start

```python
RangeSlider("volume", label="Volume", value=50)
```

## Usage Scenarios

### Custom Range

```python
RangeSlider("price", label="Price", min_value=10, max_value=500, step=10, value=100)
```

### Dual Range

```python
RangeSlider(
    "budget",
    label="Budget Range",
    dual=True,
    min_value=0,
    max_value=1000,
    min_selected=100,
    max_selected=500,
    step=50,
)
```

### With Suffix

```python
RangeSlider("temperature", label="Temperature", min_value=-20, max_value=50, value=22, value_suffix="°C")
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `label` | `str \| None` | `None` | Label text for the range |
| `help_text` | `str \| None` | `None` | Help text below the range |
| `min_value` | `int \| float` | `0` | Minimum value |
| `max_value` | `int \| float` | `100` | Maximum value |
| `step` | `int \| float` | `1` | Step increment |
| `value` | `int \| float \| None` | `None` | Initial value (single mode) |
| `dual` | `bool` | `False` | Enable dual-handle range |
| `min_name` | `str \| None` | `None` | Name for min input in dual mode |
| `max_name` | `str \| None` | `None` | Name for max input in dual mode |
| `min_selected` | `int \| float \| None` | `None` | Initial min value (dual mode) |
| `max_selected` | `int \| float \| None` | `None` | Initial max value (dual mode) |
| `show_value` | `bool` | `True` | Show current value display |
| `value_suffix` | `str` | `""` | Suffix appended to displayed value |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Labels are associated with inputs via `for` and `id` attributes.
- Help text is linked via `aria-describedby`.
- Inputs use `type="range"` with proper `min`, `max`, and `step` attributes.

## API Reference

::: faststrap.components.forms.range_slider.RangeSlider
    options:
        show_source: true
        heading_level: 4
