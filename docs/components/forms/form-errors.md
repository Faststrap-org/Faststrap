# Form Errors

Faststrap provides utilities for mapping backend validation errors to `FormGroup` components. These helpers make it easy to display server-side validation errors in a Bootstrap-compatible format.

Components and utilities in this module:
- `FormErrorSummary` — renders a compact alert summary of all validation errors
- `FormGroupFromErrors` — wraps a `FormGroup` and auto-applies error state from a backend error mapping
- `ValidationMessage` — renders a single validation feedback message for one field
- `LiveValidationField` — wraps an input with HTMX live validation attributes
- `extract_field_error` — helper to extract a displayable error message for a specific field
- `map_formgroup_validation` — returns `FormGroup`-ready validation flags for a field

---

## Quick Start

```python
from faststrap import FormErrorSummary, FormGroupFromErrors, map_formgroup_validation

# Server-side validation
@app.post("/login")
def login(email: str, password: str):
    errors = validate_input(email, password)
    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="email"), "email", errors=errors),
            FormGroupFromErrors(Input(name="password"), "password", errors=errors),
        )
    return RedirectResponse("/dashboard")
```

---

## Visual Examples & Use Cases

### 1. Form Error Summary

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="alert alert-danger" role="alert">
      <h6 class="alert-heading h6 mb-2">Please fix the following</h6>
      <ul class="mb-0">
        <li>email: Invalid email address</li>
        <li>password: Password must be at least 8 characters</li>
      </ul>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormErrorSummary({
    "email": "Invalid email address",
    "password": "Password must be at least 8 characters",
})
```
  </div>
</div>

### 2. FormGroup with Error State

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label is-invalid">Email</label>
      <input type="email" name="email" class="form-control is-invalid" value="invalid">
      <div class="invalid-feedback d-block">Invalid email address</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(name="email", type="email", value="invalid"),
    error="Invalid email address",
    is_invalid=True,
)
```
  </div>
</div>

### 3. Live Validation Field

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Username</label>
      <input type="text" name="username" class="form-control"
             hx-post="/validate/username"
             hx-trigger="blur changed delay:300ms"
             hx-target="closest .mb-3"
             hx-swap="outerHTML">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import LiveValidationField

LiveValidationField(
    Input(name="username"),
    validate_url="/validate/username",
    label="Username",
)
```
  </div>
</div>

---

## Practical Functionality

### 1. Complete Validation Flow

```python
from faststrap import Form, FormGroup, FormErrorSummary, FormGroupFromErrors, Button

@app.post("/register")
def register(username: str, email: str, password: str):
    errors = validate_registration(username, email, password)
    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="username"), "username", errors=errors),
            FormGroupFromErrors(Input(name="email"), "email", errors=errors),
            FormGroupFromErrors(Input(name="password"), "password", errors=errors),
        )
    return RedirectResponse("/welcome")
```

### 2. Using `extract_field_error`

```python
from faststrap import extract_field_error

# Extract single error for a field
error = extract_field_error(errors, "email")
# Returns "Invalid email address" or None

# Handles various error formats:
errors = {
    "email": "Invalid email address",
    "age": ["Must be 18+", "Must be under 100"],
    "name": {"msg": "Required"},
}
```

### 3. Live Validation Endpoint

```python
@app.post("/validate/username")
def validate_username(username: str):
    if not is_available(username):
        return FormGroup(
            Input(name="username", value=username),
            error="Username is taken",
            is_invalid=True,
        )
    return FormGroup(
        Input(name="username", value=username),
        success="Username is available",
        is_valid=True,
    )
```

---

## Parameter Reference

### `FormErrorSummary`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `errors` | `Mapping[str, Any] \| Iterable[str] \| str \| None` | required | Validation errors to display. |
| `title` | `str` | `"Please fix the following"` | Alert heading text. |
| `variant` | `str \| None` | `None` | Bootstrap alert variant (defaults to `"danger"`). |
| `heading_cls` | `str \| None` | `None` | Extra classes for the heading element. |
| `list_cls` | `str \| None` | `None` | Extra classes for the error list. |
| `show_field_names` | `bool` | `True` | Prefix errors with field names. |
| `dismissible` | `bool \| None` | `None` | Show dismiss button. |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes. |

### `FormGroupFromErrors`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_element` | `Any` | required | Input element to wrap. |
| `field` | `str` | required | Field name to look up in errors. |
| `errors` | `Mapping[str, Any] \| None` | `None` | Error mapping from the server. |
| `**kwargs` | `Any` | `{}` | Additional FormGroup attributes. |

### `LiveValidationField`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_element` | `Any` | required | Input element to enhance. |
| `validate_url` | `str` | required | HTMX validation endpoint. |
| `label` | `str \| None` | `None` | Field label. |
| `help_text` | `str \| None` | `None` | Help text below the field. |
| `error` | `str \| None` | `None` | Initial error message. |
| `success` | `str \| None` | `None` | Initial success message. |
| `is_invalid` | `bool` | `False` | Show invalid state. |
| `is_valid` | `bool` | `False` | Show valid state. |
| `required` | `bool` | `False` | Show required indicator. |
| `method` | `"get" \| "post"` | `"post"` | HTMX request method. |
| `trigger` | `str` | `"blur changed delay:300ms"` | HTMX trigger string. |
| `target` | `str` | `"closest .mb-3"` | HTMX target selector. |
| `swap` | `str` | `"outerHTML"` | HTMX swap strategy. |
| `indicator` | `str \| None` | `None` | HTMX loading indicator selector. |
| `**kwargs` | `Any` | `{}` | Additional attributes. |

---

## API Reference

::: faststrap.components.forms.errors.FormErrorSummary
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.errors.FormGroupFromErrors
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.errors.ValidationMessage
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.errors.LiveValidationField
    options:
        show_source: true
        heading_level: 4
