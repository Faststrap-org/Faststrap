# FloatingLabel

The `FloatingLabel` component creates modern form inputs with animated labels that float above the input when focused or filled. Perfect for clean, space-efficient forms with a contemporary aesthetic.

!!! success "Goal"
    Master creating floating label inputs, understand Bootstrap form-floating classes, and build modern, elegant forms that provide excellent user experience.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Floating Labels Documentation](https://getbootstrap.com/docs/5.3/forms/floating-labels/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="form-floating mb-3">
      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import FloatingLabel

FloatingLabel(
    "email",
    label="Email address",
    input_type="email"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Login Form - Modern Design

```python
from faststrap import FloatingLabel, Button, Card

Card(
    H3("Sign In", cls="mb-4"),
    FloatingLabel(
        "email",
        label="Email address",
        input_type="email",
        required=True
    ),
    FloatingLabel(
        "password",
        label="Password",
        input_type="password",
        required=True
    ),
    Button("Sign In", variant="primary", cls="w-100 mt-3"),
    cls="p-4 shadow"
)
```

---

### 2. With Values - Pre-filled Inputs

```python
# Label automatically floats when input has value
FloatingLabel(
    "name",
    label="Your Name",
    value="John Doe"  # ← Label floats automatically
)
```

---

### 3. Different Input Types

```python
# Email
FloatingLabel("email", label="Email address", input_type="email")

# Password
FloatingLabel("password", label="Password", input_type="password")

# Number
FloatingLabel("age", label="Age", input_type="number")

# Date
FloatingLabel("birthdate", label="Birth Date", input_type="date")

# Tel
FloatingLabel("phone", label="Phone Number", input_type="tel")
```

---

### 4. Disabled and Readonly States

```python
# Disabled
FloatingLabel(
    "disabled_field",
    label="Disabled Field",
    value="Cannot edit",
    disabled=True
)

# Readonly
FloatingLabel(
    "readonly_field",
    label="Readonly Field",
    value="Can read only",
    readonly=True
)
```

---

## Bootstrap CSS Classes Explained

### Core Classes

| Class | Purpose | Applied To |
|-------|---------|------------|
| `.form-floating` | **Container** - Enables floating label effect | Wrapper `<div>` |
| `.form-control` | **Input styling** - Standard form control | `<input>` element |
| `placeholder` attribute | **Required** - Triggers float animation | `<input>` element |

**Critical**: The `placeholder` attribute is **required** for the floating effect to work, even if you don't want visible placeholder text. Set it to the same value as the label.

---

## Core Faststrap Features

### Global Defaults

```python
from faststrap import set_component_defaults, FloatingLabel

# All floating labels required by default
set_component_defaults("FloatingLabel", required=True)

FloatingLabel("email", label="Email")  # ← Automatically required
```

---

## Common Recipes

### Complete Registration Form

```python
from faststrap import FloatingLabel, Button, Card

Card(
    H3("Create Account"),
    FloatingLabel("name", label="Full Name", required=True),
    FloatingLabel("email", label="Email", input_type="email", required=True),
    FloatingLabel("password", label="Password", input_type="password", required=True),
    FloatingLabel("confirm", label="Confirm Password", input_type="password", required=True),
    Button("Register", variant="primary", cls="w-100 mt-3"),
    cls="p-4"
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | Required | Input name attribute |
| `label` | `str` | Required | Label text (floats on focus/fill) |
| `input_type` | `str` | `"text"` | HTML input type |
| `value` | `str` | `""` | Initial value |
| `placeholder` | `str` | Same as label | Placeholder (required for float effect) |
| `disabled` | `bool` | `False` | Disable input |
| `readonly` | `bool` | `False` | Make readonly |
| `required` | `bool` | `False` | Mark as required |
| `input_id` | `str \| None` | Auto-generated | Input ID |
| `input_cls` | `str` | `""` | Additional input classes |
| `label_cls` | `str` | `""` | Additional label classes |
| `**kwargs` | `Any` | - | Additional HTML attributes |

::: faststrap.components.forms.inputgroup.FloatingLabel
    options:
        show_source: true
        heading_level: 4
