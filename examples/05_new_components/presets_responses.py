"""
Presets Responses Demo
Demonstrates response helpers: hx_redirect, hx_refresh, toast_response, and @require_auth decorator
"""

from fasthtml.common import H1, H4, H5, A, Div, FastHTML, Hr, P, serve

from faststrap import (
    Alert,
    Button,
    Card,
    Container,
    FormGroup,
    Icon,
    Input,
    ToastContainer,
    add_bootstrap,
)
from faststrap.presets import hx_redirect, hx_refresh, require_auth, toast_response

app = FastHTML()
add_bootstrap(app)

# Simple session simulation
sessions = {}


@app.get("/")
def home():
    return Container(
        H1("HTMX Response Helpers Demo", cls="mb-4"),
        # hx_redirect Demo
        Card(
            H5("1. hx_redirect() - Server-Side Redirects", cls="card-title"),
            P("Click to redirect to another page:", cls="text-muted"),
            Button(
                "Redirect to Success Page",
                variant="primary",
                hx_post="/api/redirect-demo",
                cls="me-2",
            ),
            Button(
                "Redirect to External Site",
                variant="secondary",
                hx_post="/api/redirect-external",
            ),
            cls="mb-4",
        ),
        # hx_refresh Demo
        Card(
            H5("2. hx_refresh() - Full Page Refresh", cls="card-title"),
            P("Click to refresh the entire page:", cls="text-muted"),
            Button(
                "Refresh Page",
                variant="info",
                hx_post="/api/refresh-demo",
            ),
            cls="mb-4",
        ),
        # toast_response Demo
        Card(
            H5("3. toast_response() - Toast Notifications", cls="card-title"),
            P("Click to show toast notifications:", cls="text-muted"),
            Button(
                "Success Toast",
                variant="success",
                hx_post="/api/toast-success",
                cls="me-2",
            ),
            Button(
                "Error Toast",
                variant="danger",
                hx_post="/api/toast-error",
                cls="me-2",
            ),
            Button(
                "Info Toast",
                variant="info",
                hx_post="/api/toast-info",
            ),
            cls="mb-4",
        ),
        # @require_auth Demo
        Card(
            H5("4. @require_auth - Route Protection", cls="card-title"),
            P("Try accessing protected content:", cls="text-muted"),
            Button(
                "Access Protected Route (Not Logged In)",
                variant="warning",
                hx_get="/api/protected",
                hx_target="#auth-result",
            ),
            Div(id="auth-result", cls="mt-3"),
            cls="mb-4",
        ),
        # Login Demo
        Card(
            H5("Login Demo", cls="card-title"),
            P("Login to access protected routes:", cls="text-muted"),
            FormGroup(
                Input(name="username", placeholder="Username", id="username-input"),
                label="Username",
            ),
            Button(
                "Login",
                variant="primary",
                hx_post="/api/login",
                hx_include="#username-input",
                hx_target="#login-result",
            ),
            Div(id="login-result", cls="mt-3"),
            cls="mb-4",
        ),
        # Toast container
        ToastContainer(position="top-end"),
        cls="my-5",
    )


@app.post("/api/redirect-demo")
def redirect_demo():
    """Redirect to success page"""
    return hx_redirect("/success")


@app.post("/api/redirect-external")
def redirect_external():
    """Redirect to external site"""
    return hx_redirect("https://fastht.ml")


@app.get("/success")
def success_page():
    return Container(
        Alert(
            H4("Redirect Successful!", cls="alert-heading"),
            P("You were redirected here using hx_redirect()"),
            Hr(),
            A("Go Back", href="/", cls="btn btn-primary"),
            variant="success",
        ),
        cls="my-5",
    )


@app.post("/api/refresh-demo")
def refresh_demo():
    """Trigger full page refresh"""
    return hx_refresh()


@app.post("/api/toast-success")
def toast_success():
    """Show success toast"""
    return toast_response(
        content="",
        message="Operation completed successfully!",
        variant="success",
    )


@app.post("/api/toast-error")
def toast_error():
    """Show error toast"""
    return toast_response(
        content="",
        message="Something went wrong. Please try again.",
        variant="danger",
    )


@app.post("/api/toast-info")
def toast_info():
    """Show info toast"""
    return toast_response(
        content="",
        message="This is an informational message.",
        variant="info",
    )


@app.get("/api/protected")
@require_auth(session_key="user_id", login_url="/")
def protected_route(request):
    """Protected route - requires authentication"""
    user_id = request.session.get("user_id")
    return Alert(
        Icon("shield-check", cls="me-2"),
        f"Welcome! You are logged in as user {user_id}",
        variant="success",
    )


@app.post("/api/login")
def login(username: str):
    """Simple login endpoint"""
    if not username:
        return Alert("Please enter a username", variant="danger")

    # Simulate login
    user_id = len(sessions) + 1
    sessions[user_id] = username

    return Div(
        Alert(
            Icon("check-circle-fill", cls="me-2"),
            f"Logged in as {username}! Now try accessing the protected route.",
            variant="success",
        ),
        hx_swap_oob="innerHTML:#login-result",
    )


serve()
