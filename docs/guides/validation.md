# Validation Guide

Faststrap provides a complete toolkit for form validation, from server-side error summaries to live HTMX validation.

---

## Validation Flow

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="Login", description="Sign in to your account"),
        Container(
            Card(
                Card.Body(
                    Form(
                        FormGroup("Email", Input(name="email", type="email", required=True)),
                        FormGroup("Password", Input(name="password", type="password", required=True)),
                        Button("Sign In", type="submit", variant="primary"),
                        method="post",
                        action="/login",
                    ),
                ),
            ),
            cls="py-5",
        ),
    )

@rt("/login")
def post(email: str, password: str):
    errors = {}
    if not email or "@" not in email:
        errors["email"] = "Please enter a valid email address"
    if not password or len(password) < 8:
        errors["password"] = "Password must be at least 8 characters"

    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="email", type="email", value=email), "email", errors=errors),
            FormGroupFromErrors(Input(name="password", type="password"), "password", errors=errors),
        )

    return RedirectResponse("/dashboard")

serve()
```

---

## FormErrorSummary

`FormErrorSummary` renders a compact alert listing all validation errors.

```python
from faststrap import FormErrorSummary

FormErrorSummary(
    {
        "email": "Invalid email address",
        "password": "Password must be at least 8 characters",
    }
)
```

### Customizing FormErrorSummary

```python
FormErrorSummary(
    errors,
    title="Please correct the following:",
    variant="danger",
    show_field_names=False,
    dismissible=True,
)
```

---

## FormGroupFromErrors

`FormGroupFromErrors` wraps a `FormGroup` and applies error state from a backend error mapping.

```python
from faststrap import FormGroupFromErrors, Input

FormGroupFromErrors(
    Input(name="email", type="email", value=email),
    "email",
    errors=errors,
)
```

This automatically sets:
- `error="Invalid email address"` if the field has an error
- `is_invalid=True` to show the red border and feedback message

---

## Live Validation with HTMX

Use `LiveValidationField` for real-time field validation without a full form submit.

```python
from faststrap import LiveValidationField

LiveValidationField(
    Input(name="username"),
    validate_url="/validate/username",
    label="Username",
    help_text="Choose a unique username",
)
```

### Live Validation Endpoint

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

## ValidationMessage

Render a single validation feedback message:

```python
from faststrap import ValidationMessage

ValidationMessage(
    "Email is required",
    state="invalid",
)
```

States:
- `"invalid"` — red error message
- `"valid"` — green success message
- `"neutral"` — gray help text

---

## Helper Functions

### extract_field_error

```python
from faststrap import extract_field_error

error = extract_field_error(errors, "email")
# Returns "Invalid email address" or None
```

### map_formgroup_validation

```python
from faststrap import map_formgroup_validation

flags = map_formgroup_validation(errors, "email")
# Returns {"error": "Invalid email address", "is_invalid": True}
```

---

## Complete Example

```python
from fasthtml.common import *
from faststrap import *

app, rt = fast_app()

@app.before
def add_bootstrap(req, resp):
    return add_bootstrap(req, resp)

@rt("/")
def get():
    return (
        PageMeta(title="Register", description="Create an account"),
        Container(
            Form(
                FormGroup("Username", LiveValidationField(
                    Input(name="username"),
                    validate_url="/validate/username",
                    label="Username",
                )),
                FormGroup("Email", Input(name="email", type="email", required=True)),
                FormGroup("Password", Input(name="password", type="password", required=True)),
                Button("Register", type="submit", variant="primary"),
                method="post",
                action="/register",
            ),
            cls="py-5",
        ),
    )

@rt("/register")
def post(username: str, email: str, password: str):
    errors = {}
    if not username or len(username) < 3:
        errors["username"] = "Username must be at least 3 characters"
    if not email or "@" not in email:
        errors["email"] = "Invalid email address"
    if not password or len(password) < 8:
        errors["password"] = "Password must be at least 8 characters"

    if errors:
        return (
            FormErrorSummary(errors),
            FormGroupFromErrors(Input(name="username", value=username), "username", errors=errors),
            FormGroupFromErrors(Input(name="email", value=email, type="email"), "email", errors=errors),
            FormGroupFromErrors(Input(name="password", type="password"), "password", errors=errors),
        )

    return RedirectResponse("/welcome")

serve()
```

---

## See Also

- [HTMX Integration Guide](../guides/htmx-integration.md)
- [Error Handling Guide](../guides/error-handling.md)
- [Form Errors Component Reference](../components/forms/form-errors.md)
