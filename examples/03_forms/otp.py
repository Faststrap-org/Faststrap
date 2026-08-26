"""
03_forms/otp.py
Demonstrates: OTPInput, OTPInputGroup

OTPInput: single row of N digit boxes (for use inside custom forms).
OTPInputGroup: fully-featured OTP widget with auto-submit and accessibility.

Use case: 2FA / email verification flow.
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    OTPInput,
    OTPInputGroup,
    Button,
    Alert,
    Card,
    Stack,
    AuthLayout,
    FormGroup,
)

app = FastHTML()
add_bootstrap(app, theme="purple-magic", mode="light")


@app.get("/")
def home():
    return Container(
        H1("OTP Input Components", cls="display-5 fw-bold mb-2"),
        P("One-time password inputs for 2FA and email verification flows.", cls="lead text-muted mb-5"),

        # ── OTPInput (standalone) ─────────────────────────────────────────
        H2("OTPInput — standalone", cls="h4 fw-semibold mb-1"),
        P("Use inside your own form. Controls: length, variant, size, placeholder.", cls="text-muted mb-3"),
        Card(
            Stack(
                OTPInput(6, name="code_default", variant="primary"),
                OTPInput(4, name="code_sm", variant="success", size="sm"),
                OTPInput(6, name="code_lg", variant="warning", size="lg"),
                gap=3,
            ),
            header="OTPInput — 6-digit (primary), 4-digit sm (success), 6-digit lg (warning)",
            cls="mb-5",
        ),

        # ── OTPInputGroup (with submit) ───────────────────────────────────
        H2("OTPInputGroup — with auto-submit", cls="h4 fw-semibold mb-1"),
        P("Auto-moves focus between boxes. Submits when all boxes are filled.", cls="text-muted mb-3"),
        Card(
            Div(
                OTPInputGroup(
                    6,
                    name="verify_code",
                    variant="primary",
                    size="md",
                    autofocus=True,
                    gap=2,
                ),
                Button("Verify Code", variant="primary", type="submit", cls="w-100 mt-3"),
                cls="d-flex flex-column align-items-center",
            ),
            header="OTPInputGroup(6, autofocus=True)",
            cls="mb-5",
        ),
        cls="my-5",
    )


@app.get("/verify")
def verify_page():
    """Full-page 2FA verification using AuthLayout."""
    return AuthLayout(
        Alert(
            "A 6-digit verification code was sent to you@example.com",
            variant="info",
            cls="mb-3",
        ),
        OTPInputGroup(6, name="code", autofocus=True, gap=2),
        Button("Verify", variant="primary", type="submit", cls="w-100 mt-3"),
        title="Verify Your Identity",
        subtitle="Enter the code we sent to your email.",
        brand_name="MyApp",
        action="/api/verify",
        method="post",
        footer_text="Didn't receive a code?",
        footer_link="/resend",
        footer_link_text="Resend",
    )


@app.post("/api/verify")
def handle_verify(code: str = ""):
    if len(code) == 6 and code.isdigit():
        return Alert("Verification successful!", variant="success")
    return Alert("Invalid code. Please try again.", variant="danger")


if __name__ == "__main__":
    serve()
