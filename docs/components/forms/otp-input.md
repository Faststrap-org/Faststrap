# OTPInput

`OTPInput` and `OTPInputGroup` render one-time password (OTP) / PIN input fields for verification flows like two-factor authentication and password resets.

- `OTPInput` is a **CSS-only** single-field input with visual digit separation. It requires zero JavaScript.
- `OTPInputGroup` is a multi-field group with **auto-advance** between digit boxes, powered by a small JavaScript initializer.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Forms](https://getbootstrap.com/docs/5.3/forms/overview/)

---

## Quick Start

### CSS-Only Single Field

```python
from faststrap import OTPInput

OTPInput(length=6, name="otp")
```

### Multi-Field with Auto-Advance

```python
from faststrap import OTPInputGroup

OTPInputGroup(length=6, name="otp")
```

---

## Visual Examples & Use Cases

### 1. CSS-Only OTPInput

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="form-control text-center letter-spaced-otp" style="letter-spacing: 0.5em; font-family: monospace; max-width: 13.2em; text-align: center;">
      • • • • • •
    </div>
  </div>
  <div class="preview-code" markdown>
```python
OTPInput(length=6, name="otp")
```
  </div>
</div>

### 2. OTPInputGroup (Auto-Advance)

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-2" data-fs-otp-group="true">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control text-center otp-digit-input" style="width: 3rem;">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
OTPInputGroup(length=6, name="otp")
```
  </div>
</div>

### 3. Size Variants

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-2" data-fs-otp-group="true">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control form-control-sm text-center otp-digit-input" style="width: 2.5rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control form-control-sm text-center otp-digit-input" style="width: 2.5rem;">
      <input type="text" inputmode="numeric" maxlength="1" class="form-control form-control-sm text-center otp-digit-input" style="width: 2.5rem;">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
OTPInputGroup(length=3, size="sm", name="otp")
```
  </div>
</div>

---

## Practical Functionality

### 1. Inside a Form

```python
from faststrap import Form, FormGroup, OTPInput, Button

Form(
    FormGroup("Verification Code", OTPInput(length=6, name="otp")),
    Button("Verify", type="submit", variant="primary"),
    method="post",
    action="/verify",
)
```

### 2. With HTMX Verification

```python
from faststrap import Form, FormGroup, OTPInputGroup, Button

Form(
    FormGroup("Code", OTPInputGroup(length=6, name="otp")),
    Button("Verify", type="submit", variant="primary",
           hx_post="/verify-otp",
           hx_target="#result",
           hx_swap="innerHTML"),
    method="post",
    action="/verify-otp",
)
```

### 3. Custom Placeholder Character

```python
OTPInput(length=4, name="pin", placeholder="-")
# Shows: - - - -
```

---

## Parameter Reference

### `OTPInput`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `length` | `int` | `6` | Number of digits expected. |
| `name` | `str` | `"otp"` | Form field name for the concatenated value. |
| `variant` | `VariantType` | `"primary"` | Bootstrap color variant for focus styling. |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Input size. |
| `placeholder` | `str` | `"•"` | Character shown in each position. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

### `OTPInputGroup`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `length` | `int` | `6` | Number of digit boxes. |
| `name` | `str` | `"otp"` | Form field name prefix. |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Input size. |
| `variant` | `VariantType` | `"primary"` | Bootstrap color variant. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

---

## Accessibility

- Uses `inputmode="numeric"` for mobile numeric keyboards.
- Uses `autocomplete="one-time-code"` for SMS autofill on iOS/Android.
- `OTPInputGroup` requires JavaScript for auto-advance; the `OTPInput` variant works without JS.

---

## API Reference

::: faststrap.components.forms.otp_input.OTPInput
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.otp_input.OTPInputGroup
    options:
        show_source: true
        heading_level: 4
