"""
Error Dialogs Demo
Demonstrates ErrorDialog component for modal error displays with retry functionality
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)

# Simulate a counter for retry demo
retry_counter = {"count": 0}


@app.get("/")
def home():
    return Container(
        H1("Error Dialogs Demo", cls="mb-4"),
        P("Click the buttons below to trigger different error dialogs:", cls="lead"),
        Row(
            Col(
                Card(
                    Button(
                        "Trigger Basic Error",
                        variant="danger",
                        hx_get="/trigger-basic-error",
                        hx_target="#error-dialog-container",
                        hx_swap="innerHTML",
                    ),
                    P("Shows a simple error dialog without retry", cls="text-muted small mt-2"),
                    body_cls="text-center",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    Button(
                        "Trigger Error with Retry",
                        variant="warning",
                        hx_get="/trigger-retry-error",
                        hx_target="#error-dialog-container",
                        hx_swap="innerHTML",
                    ),
                    P(
                        "Shows error with retry button (simulates occasional failure)",
                        cls="text-muted small mt-2",
                    ),
                    body_cls="text-center",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-3",
            ),
            Col(
                Card(
                    Button(
                        "Trigger Info Dialog",
                        variant="info",
                        hx_get="/trigger-info-dialog",
                        hx_target="#error-dialog-container",
                        hx_swap="innerHTML",
                    ),
                    P(
                        "Shows an informational dialog (variant='info')",
                        cls="text-muted small mt-2",
                    ),
                    body_cls="text-center",
                ),
                cols=12,
                md=6,
                lg=4,
                cls="mb-3",
            ),
        ),
        Alert(
            Strong("How it works: "),
            "ErrorDialog uses HTMX's out-of-band swap (hx-swap-oob) to inject the modal into the page and show it automatically.",
            variant="info",
            cls="mt-4",
        ),
        # Container for error dialogs (will be replaced via OOB swap)
        Div(id="error-dialog-container"),
        cls="my-5",
    )


@app.get("/trigger-basic-error")
def trigger_basic_error():
    """Return error dialog without retry"""
    return ErrorDialog(
        message="Failed to load user data. Please try again later.",
        title="Loading Error",
        variant="danger",
        show=True,
    )


@app.get("/trigger-retry-error")
def trigger_retry_error():
    """Return error dialog with retry - simulates occasional failure"""
    retry_counter["count"] += 1

    # Succeed after 2 retries
    if retry_counter["count"] >= 3:
        retry_counter["count"] = 0
        return Div(
            Alert(
                Icon("check-circle-fill", cls="me-2"),
                "Success! Operation completed successfully.",
                variant="success",
                dismissible=True,
            ),
            hx_swap_oob="innerHTML:#error-dialog-container",
        )

    return ErrorDialog(
        message=f"Operation failed (attempt {retry_counter['count']}/3). Click retry to try again.",
        title="Operation Failed",
        variant="warning",
        retry_url="/trigger-retry-error",
        retry_text="Retry",
        show=True,
    )


@app.get("/trigger-info-dialog")
def trigger_info_dialog():
    """Return info dialog (not an error, just informational)"""
    return ErrorDialog(
        message="Your session will expire in 5 minutes. Please save your work.",
        title="Session Expiring Soon",
        variant="info",
        close_text="Got it",
        show=True,
    )


@app.get("/trigger-success-dialog")
def trigger_success_dialog():
    """Return success dialog"""
    return ErrorDialog(
        message="Your changes have been saved successfully!",
        title="Success",
        variant="success",
        close_text="Close",
        show=True,
    )


serve()
