# Live Validation

The `LiveValidationField` and `ValidationMessage` components wire inputs for HTMX live validation and render validation feedback.

## Quick Start

```python
LiveValidationField(
    Input("email", input_type="email"),
    validate_url="/validate/email",
    label="Email Address",
)
```

## Usage Scenarios

### With Validation Endpoint

```python
LiveValidationField(
    Input("username", value=""),
    validate_url="/validate/username",
    label="Username",
    help_text="Must be unique",
)
```

### Validation Message Fragment

```python
ValidationMessage("Username is available", state="valid")
ValidationMessage("Username is taken", state="invalid")
```

### With Indicator

```python
LiveValidationField(
    Input("promo_code"),
    validate_url="/validate/promo",
    label="Promo Code",
    indicator="#spinner",
)
```

## Parameter Reference

### LiveValidationField

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `input_element` | `Any` | Required | Input, Select, or Textarea component |
| `validate_url` | `str` | Required | Validation endpoint URL |
| `label` | `str \| None` | `None` | Label text |
| `help_text` | `str \| None` | `None` | Help text below input |
| `error` | `str \| None` | `None` | Error message |
| `success` | `str \| None` | `None` | Success message |
| `is_invalid` | `bool` | `False` | Whether to show invalid state |
| `is_valid` | `bool` | `False` | Whether to show valid state |
| `required` | `bool` | `False` | Mark as required |
| `method` | `"get" \| "post"` | `"post"` | Validation request method |
| `trigger` | `str` | `"blur changed delay:300ms"` | HTMX trigger |
| `target` | `str` | `"closest .mb-3"` | HTMX target |
| `swap` | `str` | `"outerHTML"` | HTMX swap style |
| `indicator` | `str \| None` | `None` | HTMX indicator selector |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### ValidationMessage

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `message` | `str \| None` | Required | Message to display |
| `state` | `"invalid" \| "valid" \| "neutral"` | `"invalid"` | Validation state |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Validation messages use semantic `invalid-feedback` and `valid-feedback` classes.
- Inputs retain their native `aria` attributes.
- Help text is preserved via `aria-describedby`.

## API Reference

::: faststrap.components.forms.errors.LiveValidationField
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.errors.ValidationMessage
    options:
        show_source: true
        heading_level: 4
