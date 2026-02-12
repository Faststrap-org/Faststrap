"""
Error Pages Demo
Demonstrates ErrorPage component for full-page error displays (404, 500, 403, custom errors)
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    return Container(
        H1("Error Pages Demo", cls="mb-4"),
        P("Click the links below to see different error pages:", cls="lead"),
        Card(
            ListGroup(
                ListGroupItem(
                    A("404 - Page Not Found", href="/404", cls="text-decoration-none"),
                    cls="d-flex justify-content-between align-items-center",
                ),
                ListGroupItem(
                    A("500 - Server Error", href="/500", cls="text-decoration-none"),
                    cls="d-flex justify-content-between align-items-center",
                ),
                ListGroupItem(
                    A("403 - Forbidden", href="/403", cls="text-decoration-none"),
                    cls="d-flex justify-content-between align-items-center",
                ),
                ListGroupItem(
                    A(
                        "Custom Error with Backend Message",
                        href="/custom-error",
                        cls="text-decoration-none",
                    ),
                    cls="d-flex justify-content-between align-items-center",
                ),
                flush=True,
            ),
            header="Available Error Pages",
        ),
        Alert(
            Strong("Tip: "),
            "ErrorPage components automatically provide appropriate icons, colors, and messages for common HTTP error codes.",
            variant="info",
            cls="mt-4",
        ),
        cls="my-5",
    )


@app.get("/404")
def not_found():
    """Standard 404 page"""
    return ErrorPage(404)


@app.get("/500")
def server_error():
    """Standard 500 page"""
    return ErrorPage(500)


@app.get("/403")
def forbidden():
    """Standard 403 page"""
    return ErrorPage(403)


@app.get("/custom-error")
def custom_error():
    """Custom error with backend message"""
    return ErrorPage(
        code=500,
        title="Oops! Something Went Wrong",
        message="We encountered an unexpected error while processing your request. Our team has been notified and is working on a fix.",
        icon="exclamation-triangle-fill",
        action_text="Try Again",
        action_href="/",
        show_code=True,
    )


@app.get("/no-action")
def no_action_error():
    """Error page without action button"""
    return ErrorPage(
        code=503,
        title="Service Temporarily Unavailable",
        message="We're performing scheduled maintenance. Please check back in a few minutes.",
        action_text=None,  # No action button
        show_code=False,  # Hide error code
    )


serve()
