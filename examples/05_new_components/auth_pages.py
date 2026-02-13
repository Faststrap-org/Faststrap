"""
Auth Pages Demo
Demonstrates AuthLayout component for login, register, and password reset pages
"""

from fasthtml.common import A, Div, FastHTML, H1, H5, Label, P, serve

from faststrap import (
    Alert,
    AuthLayout,
    Button,
    Card,
    Col,
    Container,
    FormGroup,
    Icon,
    Input,
    Row,
    add_bootstrap,
)
from faststrap.presets import hx_redirect

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    return Container(
        H1("Auth Pages Demo", cls="mb-4"),
        P("Choose an authentication page to view:", cls="lead"),
        Row(
            Col(
                Card(
                    H5("Login Page", cls="card-title"),
                    P("Standard login form with email and password", cls="text-muted"),
                    A("View Login", href="/login", cls="btn btn-primary"),
                    body_cls="text-center",
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    H5("Register Page", cls="card-title"),
                    P("User registration with validation", cls="text-muted"),
                    A("View Register", href="/register", cls="btn btn-success"),
                    body_cls="text-center",
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    H5("Password Reset", cls="card-title"),
                    P("Password reset request form", cls="text-muted"),
                    A("View Reset", href="/reset-password", cls="btn btn-warning"),
                    body_cls="text-center",
                ),
                cols=12,
                md=4,
                cls="mb-3",
            ),
        ),
        cls="my-5",
    )


@app.get("/login")
def login_page():
    """Login page using AuthLayout"""
    return AuthLayout(
        FormGroup(
            Input(name="email", type="email", placeholder="you@example.com", required=True),
            label="Email Address",
            required=True,
        ),
        FormGroup(
            Input(name="password", type="password", placeholder="••••••••", required=True),
            label="Password",
            required=True,
        ),
        Div(
            Input(type="checkbox", name="remember", id="remember", cls="form-check-input"),
            Label("Remember me", fr="remember", cls="form-check-label ms-2"),
            cls="form-check mb-3",
        ),
        Button("Sign In", variant="primary", type="submit", cls="w-100"),
        title="Sign In",
        subtitle="Welcome back! Please sign in to continue.",
        logo="/assets/logo.svg",  # Optional logo
        brand_name="FastStrap",
        action="/api/login",
        method="post",
        footer_text="Don't have an account?",
        footer_link="/register",
        footer_link_text="Sign up",
    )


@app.get("/register")
def register_page():
    """Register page using AuthLayout"""
    return AuthLayout(
        FormGroup(
            Input(name="name", placeholder="John Doe", required=True),
            label="Full Name",
            required=True,
        ),
        FormGroup(
            Input(name="email", type="email", placeholder="you@example.com", required=True),
            label="Email Address",
            required=True,
        ),
        FormGroup(
            Input(name="password", type="password", placeholder="••••••••", required=True),
            label="Password",
            help_text="Must be at least 8 characters",
            required=True,
        ),
        FormGroup(
            Input(name="confirm_password", type="password", placeholder="••••••••", required=True),
            label="Confirm Password",
            required=True,
        ),
        Div(
            Input(type="checkbox", name="terms", id="terms", required=True, cls="form-check-input"),
            Label(
                "I agree to the ",
                A("Terms of Service", href="/terms", target="_blank"),
                " and ",
                A("Privacy Policy", href="/privacy", target="_blank"),
                fr="terms",
                cls="form-check-label ms-2",
            ),
            cls="form-check mb-3",
        ),
        Button("Create Account", variant="success", type="submit", cls="w-100"),
        title="Create Account",
        subtitle="Join us today! Fill in the details below.",
        brand_name="FastStrap",
        action="/api/register",
        method="post",
        footer_text="Already have an account?",
        footer_link="/login",
        footer_link_text="Sign in",
    )


@app.get("/reset-password")
def reset_password_page():
    """Password reset page using AuthLayout"""
    return AuthLayout(
        Alert(
            "Enter your email address and we'll send you a link to reset your password.",
            variant="info",
            cls="mb-3",
        ),
        FormGroup(
            Input(name="email", type="email", placeholder="you@example.com", required=True),
            label="Email Address",
            required=True,
        ),
        Button("Send Reset Link", variant="primary", type="submit", cls="w-100"),
        title="Reset Password",
        subtitle="Forgot your password? No problem!",
        brand_name="FastStrap",
        action="/api/reset-password",
        method="post",
        footer_text="Remember your password?",
        footer_link="/login",
        footer_link_text="Sign in",
    )


@app.post("/api/login")
def handle_login(email: str, password: str):
    """Handle login submission"""
    # Simulate validation
    if not email or not password:
        return Alert("Please fill in all fields", variant="danger")

    # Simulate successful login
    return hx_redirect("/dashboard")


@app.post("/api/register")
def handle_register(name: str, email: str, password: str, confirm_password: str):
    """Handle registration submission"""
    if password != confirm_password:
        return Alert("Passwords do not match", variant="danger")

    # Simulate successful registration
    return hx_redirect("/login")


@app.post("/api/reset-password")
def handle_reset(email: str):
    """Handle password reset submission"""
    return Alert(
        Icon("check-circle-fill", cls="me-2"),
        f"Password reset link sent to {email}",
        variant="success",
    )


@app.get("/dashboard")
def dashboard():
    """Simple dashboard after login"""
    return Container(
        Alert(
            H4("Welcome!", cls="alert-heading"),
            P("You have successfully logged in."),
            variant="success",
        ),
        cls="my-5",
    )


serve()
