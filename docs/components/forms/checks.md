# Checkbox, Radio & Switch

These components allow users to select one or more options from a list. Faststrap provides `Checkbox` for multiple select, `Radio` for single select, `Switch` for toggles, and `Range` for slider inputs.

## Quick Start

```python
Checkbox("subscribe", label="Subscribe to newsletter")
Radio("plan", value="monthly", label="Monthly Plan")
Switch("notifications", label="Enable Notifications")
```

## Usage Scenarios

### Grouping Radios

```python
Div(
    Radio("shipping", value="standard", label="Standard Shipping (Free)", checked=True),
    Radio("shipping", value="express", label="Express Shipping ($10)"),
    Radio("shipping", value="overnight", label="Overnight ($25)")
)
```

### Inline Layout

```python
Div(
    Checkbox("tag", value="python", label="Python", inline=True),
    Checkbox("tag", value="javascript", label="JavaScript", inline=True),
    Checkbox("tag", value="rust", label="Rust", inline=True)
)
```

### Switches

```python
Switch("wifi", label="Wi-Fi", checked=True)
Switch("bluetooth", label="Bluetooth")
Switch("airplane", label="Airplane Mode", disabled=True)
```

### Button Style (Toggle Buttons)

```python
Div(
    Radio("view", value="list", label="List View", btn_style=True, variant="outline-primary", checked=True),
    Radio("view", value="grid", label="Grid View", btn_style=True, variant="outline-primary"),
    cls="btn-group"
)
```

### Range Slider

```python
Range("volume", label="Volume", value=50)
Range("price", label="Price", min_val=10, max_val=500, step=10)
```

## Parameter Reference

### Checkbox

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `label` | `str \| None` | `None` | Label text |
| `value` | `str` | `"1"` | Value when checked |
| `checked` | `bool` | `False` | Whether initially checked |
| `disabled` | `bool` | `False` | Disable the checkbox |
| `required` | `bool` | `False` | Mark as required |
| `inline` | `bool` | `False` | Display inline |
| `reverse` | `bool` | `False` | Put checkbox on right side of label |
| `checkbox_id` | `str \| None` | `None` | ID for the input |
| `size` | `str \| None` | `None` | Control size (`sm`, `lg`) |
| `input_cls` | `str` | `""` | Additional classes for input |
| `label_cls` | `str` | `""` | Additional classes for label |
| `help_text` | `str \| None` | `None` | Help text below input |

### Radio

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute (same name groups radios) |
| `label` | `str \| None` | `None` | Label text |
| `value` | `str` | `""` | Value when selected |
| `checked` | `bool` | `False` | Whether initially selected |
| `disabled` | `bool` | `False` | Disable the radio |
| `required` | `bool` | `False` | Mark as required |
| `inline` | `bool` | `False` | Display inline |
| `reverse` | `bool` | `False` | Put radio on right side of label |
| `radio_id` | `str \| None` | `None` | ID for the input |
| `input_cls` | `str` | `""` | Additional classes for input |
| `label_cls` | `str` | `""` | Additional classes for label |

### Switch

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `label` | `str \| None` | `None` | Label text |
| `value` | `str` | `"1"` | Value when checked |
| `checked` | `bool` | `False` | Whether initially on |
| `disabled` | `bool` | `False` | Disable the switch |
| `required` | `bool` | `False` | Mark as required |
| `reverse` | `bool` | `False` | Put switch on right side of label |
| `switch_id` | `str \| None` | `None` | ID for the input |
| `input_cls` | `str` | `""` | Additional classes for input |
| `label_cls` | `str` | `""` | Additional classes for label |

### Range

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | Required | Input name attribute |
| `label` | `str \| None` | `None` | Label text |
| `value` | `int \| float \| None` | `None` | Initial value |
| `min_val` | `int \| float` | `0` | Minimum value |
| `max_val` | `int \| float` | `100` | Maximum value |
| `step` | `int \| float \| None` | `None` | Step increment |
| `disabled` | `bool` | `False` | Disable the range |
| `range_id` | `str \| None` | `None` | ID for the input |
| `input_cls` | `str` | `""` | Additional classes for input |
| `label_cls` | `str` | `""` | Additional classes for label |

## Accessibility

- Labels are associated with inputs via `for` and `id` attributes.
- Required fields use the `required` attribute.
- Switch inputs include `role="switch"` for proper screen reader semantics.

## API Reference

::: faststrap.components.forms.checks.Checkbox
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.checks.Radio
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.checks.Switch
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.checks.Range
    options:
        show_source: true
        heading_level: 4
