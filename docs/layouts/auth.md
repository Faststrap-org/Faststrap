# Auth Layout

The `AuthLayout` component creates a centered authentication page layout perfect for login, registration, and password reset forms. Features branding, form fields, footer links, and responsive design.

!!! success "Goal"
    By the end of this guide, you'll be able to create beautiful login and registration pages **in minutes with zero CSS.**

---

## Quick Start

Here's the simplest way to create a login page.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="min-vh-100 d-flex align-items-center justify-content-center bg-light">
      <div class="card shadow" style="max-width: 400px; width: 100%;">
        <div class="card-body p-4">
          <h3 class="text-center mb-4">Welcome Back</h3>
          <form>
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input type="email" class="form-control">
            </div>
            <div class="mb-3">
              <label class="form-label">Password</label>
              <input type="password" class="form-control">
            </div>
            <button class="btn btn-primary w-100">Sign In</button>
          </form>
          <p class="text-center mt-3 mb-0 small">
            <span class="text-muted">Don't have an account?</span>
            <a href="/register">Sign up</a>
          </p>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
AuthLayout(
    FormGroup(Input(type="email", name="email"), label="Email"),
    FormGroup(Input(type="password", name="password"), label="Password"),
    Button("Sign In", type="submit", variant="primary", full_width=True),
    title="Welcome Back"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Login Page

Complete login form with branding.

```python
@app.get("/login")
def login_page():
    return AuthLayout(
        FormGroup(
            Input(type="email", name="email", placeholder="you@example.com"),
            label="Email Address",
            required=True
        ),
        FormGroup(
            Input(type="password", name="password"),
            label="Password",
            required=True
        ),
        Div(
            A("Forgot password?", href="/reset-password", cls="text-decoration-none"),
            cls="text-end mb-3"
        ),
        Button("Sign In", type="submit", variant="primary", full_width=True),
        title="Welcome Back",
        subtitle="Sign in to your account",
        logo="/static/logo.png",
        footer_text="Don't have an account?",
        footer_link="/register",
        footer_link_text="Sign up",
        form_attrs={
            "hx_post": "/auth/login",
            "hx_target": "#auth-container"
        }
    )
```

### 2. Registration Page

Sign-up form with terms acceptance.

```python
@app.get("/register")
def register_page():
    return AuthLayout(
        FormGroup(
            Input(name="name", placeholder="John Doe"),
            label="Full Name",
            required=True
        ),
        FormGroup(
            Input(type="email", name="email", placeholder="you@example.com"),
            label="Email Address",
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
        Checkbox(
            "I agree to the Terms of Service and Privacy Policy",
            name="agree_terms",
            required=True
        ),
        Button("Create Account", type="submit", variant="primary", full_width=True),
        title="Create Account",
        subtitle="Join thousands of users",
        logo="/static/logo.png",
        footer_text="Already have an account?",
        footer_link="/login",
        footer_link_text="Sign in",
        form_attrs={
            "hx_post": "/auth/register",
            "hx_target": "#auth-container"
        }
    )
```

### 3. Password Reset

Simple password reset form.

```python
@app.get("/reset-password")
def reset_password_page():
    return AuthLayout(
        P("Enter your email and we'll send you a reset link.", cls="text-muted mb-4"),
        FormGroup(
            Input(type="email", name="email", placeholder="you@example.com"),
            label="Email Address",
            required=True
        ),
        Button("Send Reset Link", type="submit", variant="primary", full_width=True),
        title="Reset Password",
        footer_text="Remember your password?",
        footer_link="/login",
        footer_link_text="Sign in",
        form_attrs={
            "hx_post": "/auth/reset-password",
            "hx_target": "#auth-container"
        }
    )
```

---

## Practical Functionality

### With Social Login

Add OAuth buttons.

```python
AuthLayout(
    # Social login buttons
    Button(
        Icon("google", cls="me-2"),
        "Continue with Google",
        variant="outline-dark",
        full_width=True,
        cls="mb-2",
        onclick="window.location='/auth/google'"
    ),
    Button(
        Icon("github", cls="me-2"),
        "Continue with GitHub",
        variant="outline-dark",
        full_width=True,
        cls="mb-3",
        onclick="window.location='/auth/github'"
    ),
    
    # Divider
    Div(
        Hr(cls="flex-grow-1"),
        Span("or", cls="px-3 text-muted"),
        Hr(cls="flex-grow-1"),
        cls="d-flex align-items-center mb-3"
    ),
    
    # Email/password form
    FormGroup(Input(type="email", name="email"), label="Email"),
    FormGroup(Input(type="password", name="password"), label="Password"),
    Button("Sign In", type="submit", variant="primary", full_width=True),
    
    title="Welcome Back"
)
```

### With Error Handling

Show validation errors.

```python
@app.post("/auth/login")
def login(email: str, password: str, req):
    # Validate
    if not email or "@" not in email:
        return AuthLayout(
            FormGroup(
                Input(type="email", name="email", value=email),
                label="Email",
                error="Please enter a valid email",
                is_invalid=True
            ),
            FormGroup(
                Input(type="password", name="password"),
                label="Password"
            ),
            Button("Sign In", type="submit", variant="primary", full_width=True),
            title="Welcome Back"
        )
    
    # Authenticate
    user = authenticate(email, password)
    if not user:
        return ErrorDialog(
            message="Invalid email or password",
            title="Login Failed",
            show=True
        )
    
    # Success
    req.session["user_id"] = user.id
    return hx_redirect("/dashboard")
```

### With Loading State

Show loading during authentication.

```python
AuthLayout(
    FormGroup(Input(type="email", name="email"), label="Email"),
    FormGroup(Input(type="password", name="password"), label="Password"),
    LoadingButton(
        "Sign In",
        endpoint="/auth/login",
        loading_text="Signing in...",
        variant="primary",
        full_width=True
    ),
    title="Welcome Back",
    form_attrs={
        "hx_post": "/auth/login",
        "hx_indicator": "#loading"
    }
)
```

---

## Integration Patterns

### With HTMX

Full HTMX-powered auth flow.

```python
@app.get("/login")
def login_page():
    return Html(
        Head(Title("Login")),
        Body(
            Div(
                AuthLayout(
                    FormGroup(Input(type="email", name="email"), label="Email"),
                    FormGroup(Input(type="password", name="password"), label="Password"),
                    Button("Sign In", type="submit", variant="primary", full_width=True),
                    title="Welcome Back",
                    form_attrs={
                        "hx_post": "/auth/login",
                        "hx_target": "#auth-container",
                        "hx_swap": "outerHTML"
                    }
                ),
                id="auth-container"
            )
        )
    )

@app.post("/auth/login")
def login(email: str, password: str, req):
    user = authenticate(email, password)
    
    if user:
        req.session["user_id"] = user.id
        return hx_redirect("/dashboard")
    else:
        # Return form with error
        return Div(
            ErrorDialog(
                message="Invalid credentials",
                show=True,
                hx_swap_oob="true"
            ),
            AuthLayout(...),  # Re-render form
            id="auth-container"
        )
```

### Multi-Step Registration

Wizard-style registration.

```python
@app.get("/register/step1")
def register_step1():
    return AuthLayout(
        FormGroup(Input(name="email"), label="Email"),
        FormGroup(Input(type="password", name="password"), label="Password"),
        Button("Next", type="submit", variant="primary", full_width=True),
        title="Create Account",
        subtitle="Step 1 of 3",
        form_attrs={"hx_post": "/register/step2"}
    )

@app.post("/register/step2")
def register_step2(email: str, password: str):
    # Save to session
    req.session["reg_email"] = email
    req.session["reg_password"] = password
    
    return AuthLayout(
        FormGroup(Input(name="name"), label="Full Name"),
        FormGroup(Input(name="company"), label="Company"),
        Button("Next", type="submit", variant="primary", full_width=True),
        title="Tell us about yourself",
        subtitle="Step 2 of 3",
        form_attrs={"hx_post": "/register/step3"}
    )
```

---

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*fields` | `Any` | Required | Form fields and content |
| `title` | `str \| None` | `None` | Page title |
| `subtitle` | `str \| None` | `None` | Page subtitle |
| `logo` | `str \| None` | `None` | Logo image URL |
| `footer_text` | `str \| None` | `None` | Footer text (e.g., "Don't have an account?") |
| `footer_link` | `str \| None` | `None` | Footer link URL |
| `footer_link_text` | `str \| None` | `None` | Footer link text |
| `form_attrs` | `dict \| None` | `None` | Additional form attributes (HTMX, etc.) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

---

## Best Practices

### ✅ Do This

```python
# Use clear titles
AuthLayout(
    ...,
    title="Welcome Back",
    subtitle="Sign in to continue"
)

# Include branding
AuthLayout(
    ...,
    logo="/static/logo.png"
)

# Provide navigation
AuthLayout(
    ...,
    footer_text="Don't have an account?",
    footer_link="/register",
    footer_link_text="Sign up"
)

# Use HTMX for smooth UX
form_attrs={
    "hx_post": "/auth/login",
    "hx_target": "#auth-container"
}
```

### ❌ Don't Do This

```python
# Don't skip error handling
# Always validate and show errors

# Don't forget footer links
# Users need to navigate between login/register

# Don't use inline styles
# Use Bootstrap classes instead

# Don't skip HTTPS
# Always use secure connections for auth
```

---

::: faststrap.layouts.auth.AuthLayout
    options:
        show_source: true
        heading_level: 4
