# Form Workflow

Use this reference when a Faststrap app needs a complete server-driven form flow with:

- field structure
- live validation
- submit-time validation
- success feedback
- clean error presentation

The examples below use `FormGroup`, HTMX, and standard Faststrap feedback primitives.

---

## Goal

Build forms in four layers:

1. field structure with `FormGroup`
2. optional live validation for key fields
3. final submit validation on the server
4. success/error response that updates the UI clearly

---

## Example Form

```python
from fasthtml.common import Div, Form
from faststrap import Button, FormErrorSummary, FormGroup, Input, LoadingButton


def newsletter_signup_form(errors: dict[str, str] | None = None, values: dict[str, str] | None = None):
    errors = errors or {}
    values = values or {}

    return Div(
        Form(
            FormErrorSummary(errors, title="Please correct the highlighted fields") if errors else "",
            FormGroup(
                Input(
                    "name",
                    value=values.get("name", ""),
                    placeholder="Full name",
                ),
                label="Full Name",
                error=errors.get("name"),
                is_invalid="name" in errors,
                required=True,
            ),
            FormGroup(
                Input(
                    "email",
                    input_type="email",
                    value=values.get("email", ""),
                    placeholder="you@example.com",
                    hx_post="/forms/newsletter/validate-email",
                    hx_trigger="blur",
                    hx_target="#newsletter-email-feedback",
                    hx_swap="outerHTML",
                ),
                label="Email",
                help_text="We will only send occasional product updates.",
                error=errors.get("email"),
                is_invalid="email" in errors,
                required=True,
            ),
            Div(id="newsletter-email-feedback"),
            LoadingButton(
                "Join Newsletter",
                type="submit",
                variant="primary",
                endpoint="/forms/newsletter",
                target="#newsletter-shell",
            ),
            cls="app-stack-md",
        ),
        id="newsletter-shell",
    )
```

---

## Field Validation Endpoint

Use targeted field validation only where it adds real value.

```python
@app.post("/forms/newsletter/validate-email")
def validate_newsletter_email(email: str = ""):
    if not email:
        return Div(
            "Email is required.",
            id="newsletter-email-feedback",
            cls="invalid-feedback d-block",
        )

    if "@" not in email:
        return Div(
            "Enter a valid email address.",
            id="newsletter-email-feedback",
            cls="invalid-feedback d-block",
        )

    if email.lower().endswith("@example.com"):
        return Div(
            "Please use a real inbox address.",
            id="newsletter-email-feedback",
            cls="invalid-feedback d-block",
        )

    return Div(
        "Email looks good.",
        id="newsletter-email-feedback",
        cls="valid-feedback d-block",
    )
```

Guidance:

- reserve live validation for fields like email, username, referral code, or slug uniqueness
- keep the target stable and predictable
- always repeat validation on final submit

---

## Final Submit Handler

```python
from faststrap.presets import toast_response


@app.post("/forms/newsletter")
def submit_newsletter(name: str = "", email: str = ""):
    values = {"name": name, "email": email}
    errors: dict[str, str] = {}

    if not name.strip():
        errors["name"] = "Please enter your full name."

    if not email.strip():
        errors["email"] = "Email is required."
    elif "@" not in email:
        errors["email"] = "Enter a valid email address."
    elif email.lower().endswith("@example.com"):
        errors["email"] = "Please use a real inbox address."

    if errors:
        return newsletter_signup_form(errors=errors, values=values)

    save_newsletter_signup(name=name.strip(), email=email.strip().lower())

    return toast_response(
        Div(
            "Thanks for joining. Watch your inbox for updates.",
            cls="alert alert-success mb-0",
        ),
        message="Signup complete",
        variant="success",
    )
```

This gives you:

- field-level feedback
- top-level summary on submit
- full server validation
- HTMX-friendly success feedback

---

## Loading State on Submit

Never submit a form without a loading indicator. Use `LoadingButton` so the user knows the request is in flight and cannot double-submit.

```python
from faststrap import LoadingButton

LoadingButton(
    "Send Message",
    endpoint="/contact",
    method="post",
    target="#form-feedback",
    variant="primary",
)
```

`LoadingButton` automatically:
- disables the button during the request
- shows a spinner
- sets `aria-busy="true"`

If you are not using HTMX, use `Button(loading=True)` and toggle it with JavaScript, or show a `Spinner` next to the button.

---

## UX Feedback Checklist for Forms

- [ ] Submit button is a `LoadingButton` (HTMX) or shows loading state
- [ ] Error summary appears at the top of the form when validation fails
- [ ] Individual fields show inline errors via `FormGroupFromErrors`
- [ ] Success shows a `Toast` or inline `Alert` with `variant="success"`
- [ ] Error shows a `Toast` with `variant="danger"` or re-renders the form with errors
- [ ] Loading state is visible (button spinner, page spinner, or placeholder)

---

## Result Card Pattern

If the app later gains a dedicated `ResultCard`, use it. Until then, use an `Alert` or styled `Card` in the success target.

```python
from faststrap import Alert


def signup_success_state():
    return Alert(
        "Your preferences were saved successfully.",
        variant="success",
        dismissible=False,
    )
```

---

## Validation Rules

For good form UX:

- show helper text before the user makes a mistake
- show inline validation at the field where possible
- show a form-level summary when multiple fields fail
- keep error text specific and actionable
- keep the submit button available unless there is a strong reason to disable it

Avoid:

- vague errors like `"Invalid input"`
- relying on color alone to communicate failure
- validating only on blur without validating again on submit

---

## Recommended Pattern Split

Use these building blocks together:

- structure:
  - `Form`
  - `FormGroup`
- backend error mapping:
  - `FormGroupFromErrors`
  - `map_formgroup_validation`
- feedback:
  - `FormErrorSummary`
  - `Alert`
  - `toast_response`
- interaction:
  - HTMX `hx_post`, `hx_target`, `hx_swap`

This is the standard server-first Faststrap form workflow until higher-level form patterns are added.
