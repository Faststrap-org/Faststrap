# Input

The `Input` component allows users to enter text, numbers, passwords, emails, and more. It wraps the standard HTML `<input>` element with comprehensive Bootstrap styling, validation states, and floating labels.

## Quick Start

```python
Input("full_name", placeholder="Enter your name", label="Full Name")
```

## Usage Scenarios

### Types & Labels

```python
Input("email", input_type="email", label="Email Address", placeholder="name@example.com")
Input("password", input_type="password", label="Password")
```

### Sizing

```python
Input("large_input", placeholder="Large Input", size="lg")
Input("default_input", placeholder="Default Input")
Input("small_input", placeholder="Small Input", size="sm")
```

### Help Text and Disabled State

```python
Input("username", label="Username", help_text="Must be 8-20 characters long.", disabled=True, value="jdoe_archived")
```

### Validation States

```python
Input("username", validation_state="valid", value="Correct!")
Input("username", validation_state="invalid", value="Invalid data")
```

### Floating Labels

```python
FloatingLabel(Input("email", placeholder="name@example.com"), label="Email Address")
```

### HTMX Integration

```python
Input("search", input_type="search", placeholder="Search users...", hx_get="/search_users", hx_trigger="keyup changed delay:500ms", hx_target="#search-results")
```

## Parameter Reference

| FastStrap Param | Type | Bootstrap / HTML Attribute | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Form field name. Required for form submission and label/input association. |
| `input_type` | `str` | `type="..."` | HTML5 input type (`text`, `password`, `email`, `number`, `date`, etc.). Default `text`. |
| `label` | `str` | `<label>` | Text for the associated label element. |
| `placeholder` | `str` | `placeholder="..."` | Ghost text shown when empty. |
| `value` | `Any` | `value="..."` | Initial value of the input. |
| `help_text` | `str` | `.form-text` | Helper text displayed below the input. |
| `size` | `str` | `.form-control-{size}` | Size: `sm` or `lg`. |
| `disabled` | `bool` | `disabled` | Disables interaction. |
| `readonly` | `bool` | `readonly` | Value is visible but not editable. |
| `required` | `bool` | `required` | Marks field as required for browser validation. |
| `validation_state` | `str` | `.is-valid` / `.is-invalid` | Validation state: `valid` or `invalid`. |
| `validation_message` | `str` | `.valid-feedback` / `.invalid-feedback` | Feedback message shown for validation state. |

## Accessibility

- Labels are automatically associated with inputs via `for` and `id` attributes.
- Required fields display a red asterisk.
- Help text is linked via `aria-describedby`.
- Floating labels use proper `for`/`id` associations.

## API Reference

::: faststrap.components.forms.input.Input
    options:
        show_source: true
        heading_level: 4
