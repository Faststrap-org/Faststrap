# OTP Input

The `OTPInput` components provide one-time password / PIN input fields with CSS-only and multi-field variants.

## Quick Start

```python
OTPInput(length=6, name="otp")
```

## Usage Scenarios

### Single-Field CSS-Only OTP

```python
OTPInput(length=6, name="otp", variant="primary", size="md", placeholder="•")
```

### Multi-Field Auto-Advance OTP

```python
OTPInputGroup(length=6, name="otp", variant="primary", size="md", gap=2, autofocus=True)
```

### Custom Variant and Size

```python
OTPInput(length=4, name="pin", variant="success", size="lg")
OTPInputGroup(length=8, name="pin", variant="danger", size="sm", gap=1)
```

## Parameter Reference

### OTPInput

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `length` | `int` | `6` | Number of digits expected |
| `name` | `str` | `"otp"` | Form field name for the concatenated value |
| `variant` | `str` | `"primary"` | Bootstrap color variant for focus styling |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Input size |
| `placeholder` | `str` | `"•"` | Character to show in each position |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### OTPInputGroup

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `length` | `int` | `6` | Number of digit boxes |
| `name` | `str` | `"otp"` | Form field name for the concatenated value |
| `variant` | `str` | `"primary"` | Bootstrap color variant for focus styling |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Input size |
| `gap` | `int` | `2` | Gap between boxes in Bootstrap spacing units |
| `autofocus` | `bool` | `True` | Auto-focus the first input on render |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Single-field OTP uses `aria-label` with the expected digit count.
- Multi-field OTP uses `aria-label` per digit (e.g., "Digit 1 of 6").
- `autocomplete="one-time-code"` is set for browser OTP autofill support.

## API Reference

::: faststrap.components.forms.otp_input.OTPInput
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.otp_input.OTPInputGroup
    options:
        show_source: true
        heading_level: 4
