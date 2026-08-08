# Form

The `Form` component is a compatibility wrapper around FastHTML's native `Form` element. It ensures wildcard imports do not accidentally break ordinary form markup, and it provides `FormBuilder.from_pydantic()` for generating Bootstrap-styled forms from Pydantic models.

For most use cases, you will use FastHTML's native `Form` directly, or `FormBuilder.from_pydantic()` for generated forms.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Forms Documentation](https://getbootstrap.com/docs/5.3/forms/overview/)

---

## Quick Start

### Native Form

```python
from fasthtml.common import Form
from faststrap import FormGroup, Input, Button

Form(
    FormGroup("Email", Input(name="email", type="email", required=True)),
    FormGroup("Password", Input(name="password", type="password", required=True)),
    Button("Sign In", type="submit", variant="primary"),
    method="post",
    action="/login",
)
```

### Generated from Pydantic

```python
from faststrap import FormBuilder

FormBuilder.from_pydantic(
    MyPydanticModel,
    action="/submit",
    method="post",
    submit_label="Save",
    submit_variant="primary",
)
```

---

## Visual Examples & Use Cases

### 1. Basic POST Form

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="faststrap-generated-form" method="post">
      <div class="mb-3">
        <label class="form-label">Email</label>
        <input type="email" name="email" class="form-control" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input type="password" name="password" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary">Sign In</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
Form(
    FormGroup("Email", Input(name="email", type="email", required=True)),
    FormGroup("Password", Input(name="password", type="password", required=True)),
    Button("Sign In", type="submit", variant="primary"),
    method="post",
    action="/login",
)
```
  </div>
</div>

### 2. Pydantic-Generated Form

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="faststrap-generated-form" method="post">
      <div class="mb-3">
        <label class="form-label">Name</label>
        <input type="text" name="name" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">Age</label>
        <input type="number" name="age" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
from pydantic import BaseModel

class UserForm(BaseModel):
    name: str
    age: int

FormBuilder.from_pydantic(
    UserForm,
    submit_label="Save",
    submit_variant="primary",
)
```
  </div>
</div>

### 3. Form with HTMX

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="faststrap-generated-form" method="post" hx-post="/search" hx-target="#results" hx-swap="innerHTML">
      <div class="mb-3">
        <label class="form-label">Search</label>
        <input type="search" name="q" class="form-control" placeholder="Search...">
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
Form(
    FormGroup("Search", Input(name="q", type="search", placeholder="Search...")),
    Button("Search", type="submit", variant="primary"),
    method="post",
    hx_post="/search",
    hx_target="#results",
    hx_swap="innerHTML",
)
```
  </div>
</div>

### 4. File Upload Form

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="faststrap-generated-form" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label class="form-label">Upload File</label>
        <input type="file" name="file" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Upload</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
Form(
    FormGroup("Upload", FileInput(name="file")),
    Button("Upload", type="submit", variant="primary"),
    method="post",
    enctype="multipart/form-data",
)
```
  </div>
</div>

---

## Practical Functionality

### 1. Form Validation

Faststrap provides several utilities for server-side validation:

```python
from faststrap import FormErrorSummary, FormGroupFromErrors, map_formgroup_validation

# In your route handler:
@app.post("/login")
def login(email: str, password: str):
    errors = validate_login(email, password)
    if errors:
        return FormErrorSummary(errors), FormGroupFromErrors(errors, "email")
    return RedirectResponse("/dashboard")
```

### 2. Live Validation with HTMX

```python
from faststrap import LiveValidationField

Form(
    LiveValidationField(
        Input(name="username"),
        validate_url="/validate/username",
        label="Username",
    ),
)
```

### 3. OTP Input Inside Forms

```python
from faststrap import Form, FormGroup, OTPInput, Button

Form(
    FormGroup("Verification Code", OTPInput(length=6, name="otp")),
    Button("Verify", type="submit", variant="primary"),
    method="post",
    action="/verify",
)
```

---

## Parameter Reference

### `FormBuilder.from_pydantic`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model_class` | `type[Any]` | required | Pydantic BaseModel class |
| `action` | `str \| None` | `None` | Form action URL |
| `method` | `str` | `"post"` | HTTP method |
| `include` | `list[str] \| None` | `None` | Fields to include |
| `exclude` | `list[str] \| None` | `None` | Fields to exclude |
| `submit_label` | `str` | `"Submit"` | Submit button text |
| `submit_variant` | `str` | `"primary"` | Submit button Bootstrap variant |
| `form_cls` | `str` | `""` | Extra CSS classes for form |
| `button_cls` | `str` | `""` | Extra CSS classes for submit button |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes |

### `Form` (Native Wrapper)

The `Form` wrapper accepts the same arguments as FastHTML's native `Form`:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*children` | `Any` | required | Form fields and content |
| `method` | `str` | `"post"` | HTTP method |
| `action` | `str \| None` | `None` | Form action URL |
| `enctype` | `str` | `"application/x-www-form-urlencoded"` | Encoding type |
| `**kwargs` | `Any` | `{}` | Additional HTML attributes (hx_*, data_*, etc.) |

---

## API Reference

::: faststrap.components.forms.form.FormBuilder
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.form.Form
    options:
        show_source: true
        heading_level: 4
