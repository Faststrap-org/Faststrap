# FormGroup

The `FormGroup` component wraps input + label + help text + validation feedback in one reusable component.

## Quick Start

```python
FormGroup(
    Input(name="email", type="email"),
    label="Email Address",
    help_text="We'll never share your email",
)
```

## Usage Scenarios

### With Validation Error

```python
FormGroup(
    Input(name="password", type="password"),
    label="Password",
    error="Password must be at least 8 characters",
    is_invalid=True,
)
```

### With Success State

```python
FormGroup(
    Input(name="username", value="john_doe"),
    label="Username",
    success="Username is available!",
    is_valid=True,
)
```

### Required Field

```python
FormGroup(
    Input(name="name"),
    label="Full Name",
    required=True,
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `input_element` | `Any` | Required | Input, Select, or Textarea component |
| `label` | `str \| None` | `None` | Label text (optional) |
| `help_text` | `str \| None` | `None` | Help text shown below input |
| `error` | `str \| None` | `None` | Error message (shown when `is_invalid=True`) |
| `success` | `str \| None` | `None` | Success message (shown when `is_valid=True`) |
| `is_invalid` | `bool` | `False` | Whether to show invalid state |
| `is_valid` | `bool` | `False` | Whether to show valid state |
| `required` | `bool` | `False` | Whether field is required (adds asterisk to label) |
| `**kwargs` | `Any` | - | Additional HTML attributes for the container |

## Accessibility

- Labels are associated with inputs via `for` and `id` attributes.
- Required fields display a red asterisk.
- Validation feedback uses `invalid-feedback d-block` and `valid-feedback d-block`.
- Help text uses `form-text text-muted`.

## API Reference

::: faststrap.components.forms.formgroup.FormGroup
    options:
        show_source: true
        heading_level: 4
