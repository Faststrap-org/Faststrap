# FormGroup

The `FormGroup` component wraps form inputs with labels, help text, and validation feedback in a single, clean component. It eliminates the boilerplate of manually creating Bootstrap form structures and handles validation states automatically.

!!! success "Goal"
    By the end of this guide, you'll be able to create professional form fields with validation, help text, and required indicators **in a single line of Python.**

---

## Quick Start

Here's the simplest way to create a form field.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Email Address</label>
      <input type="email" class="form-control" placeholder="you@example.com">
      <small class="form-text text-muted">We'll never share your email</small>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(type="email", placeholder="you@example.com"),
    label="Email Address",
    help_text="We'll never share your email"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Validation States

Show users when their input is valid or invalid.

<div class="component-preview">
  <div class="preview-header">Error State</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Password</label>
      <input type="password" class="form-control is-invalid">
      <div class="invalid-feedback d-block">Password must be at least 8 characters</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(type="password", name="password"),
    label="Password",
    error="Password must be at least 8 characters",
    is_invalid=True
)
```
  </div>
</div>

<div class="component-preview">
  <div class="preview-header">Success State</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Username</label>
      <input type="text" class="form-control is-valid" value="john_doe">
      <div class="valid-feedback d-block">Username is available!</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(name="username", value="john_doe"),
    label="Username",
    success="Username is available!",
    is_valid=True
)
```
  </div>
</div>

### 2. Required Fields

Automatically add required indicators.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Full Name <span class="text-danger">*</span></label>
      <input type="text" class="form-control">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(name="name"),
    label="Full Name",
    required=True  # Adds red asterisk
)
```
  </div>
</div>

### 3. Help Text

Guide users with contextual help.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">API Key</label>
      <input type="text" class="form-control">
      <small class="form-text text-muted">Find this in your account settings</small>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FormGroup(
    Input(name="api_key"),
    label="API Key",
    help_text="Find this in your account settings"
)
```
  </div>
</div>

---

## Practical Functionality

### Server-Side Validation

Integrate with backend validation.

```python
@app.post("/register")
def register(req):
    email = req.form.get("email")
    password = req.form.get("password")
    
    # Validate
    errors = {}
    if not email or "@" not in email:
        errors["email"] = "Please enter a valid email"
    if not password or len(password) < 8:
        errors["password"] = "Password must be at least 8 characters"
    
    if errors:
        # Re-render form with errors
        return Form(
            FormGroup(
                Input(name="email", value=email),
                label="Email",
                error=errors.get("email"),
                is_invalid="email" in errors
            ),
            FormGroup(
                Input(type="password", name="password"),
                label="Password",
                error=errors.get("password"),
                is_invalid="password" in errors
            ),
            Button("Sign Up", type="submit")
        )
    
    # Success - create user
    create_user(email, password)
    return hx_redirect("/dashboard")
```

### HTMX Live Validation

Validate as users type.

```python
# Form with live validation
FormGroup(
    Input(
        name="username",
        hx_post="/validate/username",
        hx_trigger="keyup changed delay:500ms",
        hx_target="next .feedback"
    ),
    label="Username",
    help_text="3-20 characters, letters and numbers only"
)

# Validation endpoint
@app.post("/validate/username")
def validate_username(username: str):
    if len(username) < 3:
        return Div(
            "Username too short",
            cls="invalid-feedback d-block feedback"
        )
    elif not username.isalnum():
        return Div(
            "Only letters and numbers allowed",
            cls="invalid-feedback d-block feedback"
        )
    else:
        return Div(
            "Username available!",
            cls="valid-feedback d-block feedback"
        )
```

### Complete Registration Form

```python
def RegistrationForm():
    return Form(
        FormGroup(
            Input(name="name"),
            label="Full Name",
            required=True
        ),
        FormGroup(
            Input(type="email", name="email"),
            label="Email Address",
            help_text="We'll never share your email",
            required=True
        ),
        FormGroup(
            Input(type="password", name="password"),
            label="Password",
            help_text="At least 8 characters",
            required=True
        ),
        FormGroup(
            Input(type="password", name="confirm_password"),
            label="Confirm Password",
            required=True
        ),
        Button("Create Account", type="submit", variant="primary", full_width=True),
        hx_post="/register",
        hx_target="#form-container"
    )
```

---

## Integration Patterns

### With Select and Textarea

FormGroup works with any form control.

```python
# Select dropdown
FormGroup(
    Select(
        Option("Select country...", value="", selected=True),
        Option("United States", value="us"),
        Option("United Kingdom", value="uk"),
        name="country"
    ),
    label="Country",
    required=True
)

# Textarea
FormGroup(
    Textarea(name="bio", rows=4),
    label="Bio",
    help_text="Tell us about yourself (optional)"
)
```

### With Custom Input Components

```python
# With SearchableSelect
FormGroup(
    SearchableSelect(
        endpoint="/api/users/search",
        name="assigned_to"
    ),
    label="Assign To",
    help_text="Search by name or email"
)

# With ThemeToggle
FormGroup(
    ThemeToggle(current_theme="dark"),
    label="Appearance"
)
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `input_element` | `Any` | Required | Input, Select, or Textarea component |
| `label` | `str \| None` | `None` | Label text (optional) |
| `help_text` | `str \| None` | `None` | Help text shown below input |
| `error` | `str \| None` | `None` | Error message (shown when is_invalid=True) |
| `success` | `str \| None` | `None` | Success message (shown when is_valid=True) |
| `is_invalid` | `bool` | `False` | Whether to show invalid state |
| `is_valid` | `bool` | `False` | Whether to show valid state |
| `required` | `bool` | `False` | Whether field is required (adds asterisk) |
| `**kwargs` | `Any` | - | Additional HTML attributes for container |

---

## Best Practices

### ✅ Do This

```python
# Use semantic validation
FormGroup(
    Input(type="email", name="email"),
    label="Email",
    error="Please enter a valid email address",
    is_invalid=True
)

# Provide helpful help text
FormGroup(
    Input(type="password", name="password"),
    label="Password",
    help_text="At least 8 characters with 1 number",
    required=True
)

# Show success feedback
FormGroup(
    Input(name="username", value="john_doe"),
    label="Username",
    success="Username is available!",
    is_valid=True
)
```

### ❌ Don't Do This

```python
# Don't show both error and success
FormGroup(
    Input(name="test"),
    error="Error!",
    success="Success!",
    is_invalid=True,
    is_valid=True  # Confusing!
)

# Don't use vague error messages
FormGroup(
    Input(name="email"),
    error="Invalid",  # Too vague
    is_invalid=True
)
```

---

::: faststrap.components.forms.formgroup.FormGroup
    options:
        show_source: true
        heading_level: 4
