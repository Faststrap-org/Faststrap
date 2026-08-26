"""
06_feedback/toasts_extended.py
Demonstrates: ErrorToast, NoticeToast, NoticeAlert

Extends the basic toast/alert examples with the remaining notification variants.
- ErrorToast: error-state toast with red styling
- NoticeToast: general-purpose notice with kind= (info/success/warning/error)
- NoticeAlert: inline alert version of NoticeToast
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    ErrorToast,
    NoticeToast,
    NoticeAlert,
    SuccessToast,
    WarningToast,
    InfoToast,
    ToastContainer,
    Card,
    Stack,
    Button,
)

app = FastHTML()
add_bootstrap(app, theme="red-alert", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Extended Toast & Alert Variants", cls="display-5 fw-bold mb-2"),
        P("Missing toast and alert variants — ErrorToast, NoticeToast, and NoticeAlert.", cls="lead text-muted mb-5"),

        # ── ErrorToast ─────────────────────────────────────────────────────
        H2("ErrorToast", cls="h4 fw-semibold mb-1"),
        P("ErrorToast(message, title=). Pre-styled for error states.", cls="text-muted mb-3"),
        Card(
            Stack(
                ErrorToast("Failed to save your changes. Please try again."),
                ErrorToast("Payment declined. Check your card details.", title="Payment Error"),
                ErrorToast("Connection timed out after 30 seconds.", title="Network Error"),
                gap=2,
            ),
            header="ErrorToast — default and custom titles",
            cls="mb-5",
        ),

        # ── NoticeToast ────────────────────────────────────────────────────
        H2("NoticeToast", cls="h4 fw-semibold mb-1"),
        P("NoticeToast(message, kind=). kind= accepts: info, success, warning, error.", cls="text-muted mb-3"),
        Card(
            Stack(
                NoticeToast("Your account has been created successfully.", kind="success"),
                NoticeToast("Your subscription will renew in 3 days.", kind="info", title="Renewal Reminder"),
                NoticeToast("Storage is at 89% capacity.", kind="warning", title="Storage Warning"),
                NoticeToast("API rate limit reached. Try again in 60s.", kind="error"),
                gap=2,
            ),
            header="NoticeToast — all four kinds",
            cls="mb-5",
        ),

        # ── Full comparison with existing variants ─────────────────────────
        H2("Full Toast Family Comparison", cls="h4 fw-semibold mb-1"),
        P("All toast types side by side.", cls="text-muted mb-3"),
        Card(
            Stack(
                SuccessToast("Profile updated successfully"),
                WarningToast("This action cannot be undone"),
                InfoToast("3 new messages in your inbox"),
                ErrorToast("Upload failed — file too large"),
                NoticeToast("Server restarting in 5 minutes", kind="warning", title="Maintenance"),
                gap=2,
            ),
            header="All variants — SuccessToast, WarningToast, InfoToast, ErrorToast, NoticeToast",
            cls="mb-5",
        ),

        # ── NoticeAlert ────────────────────────────────────────────────────
        H2("NoticeAlert — inline banners", cls="h4 fw-semibold mb-1"),
        P("NoticeAlert(message, kind=). Inline version of NoticeToast for page-level notices.", cls="text-muted mb-3"),
        Card(
            Stack(
                NoticeAlert("Your email has been verified.", kind="success"),
                NoticeAlert("You are in read-only mode. Contact an admin for write access.", kind="info"),
                NoticeAlert("Your trial ends in 2 days. Upgrade to keep access.", kind="warning"),
                NoticeAlert("Unable to load some resources. Refresh the page.", kind="error"),
                gap=2,
            ),
            header="NoticeAlert — all kinds",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
