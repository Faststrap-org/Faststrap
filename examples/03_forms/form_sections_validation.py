"""
03_forms/form_sections_validation.py
Demonstrates: FormSection, FormErrorSummary, FormBuilder, extract_field_error, map_formgroup_validation

- FormSection: Semantic section cards for organizing complex multi-part forms
- FormErrorSummary: Top-of-form error alert for summarizing validation failures
- FormBuilder: Declarative form builder from field definitions
- Backend Error Mappers: extract_field_error & map_formgroup_validation
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Form, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    FormSection,
    FormErrorSummary,
    FormGroup,
    Input,
    Select,
    Button,
    Alert,
    Card,
    extract_field_error,
    map_formgroup_validation,
)

app = FastHTML()
add_bootstrap(app, theme="green-nature", mode="light")


@app.get("/")
def home():
    # Sample backend validation errors dict
    errors = {
        "email": "Please enter a valid business email address.",
        "password": "Password must be at least 8 characters long.",
        "terms": "You must accept the terms of service to continue.",
    }

    # Extract single field error (used to demonstrate extract_field_error)
    email_error = extract_field_error(errors, "email")  # noqa: used in FormErrorSummary header
    # Map formgroup validation flags (includes error + is_invalid keys)
    email_val = map_formgroup_validation(errors, "email")

    return Container(
        H1("Form Structure & Validation Mappers", cls="display-5 fw-bold mb-2"),
        P("Semantic form sections, error summaries, and validation mappers.", cls="lead text-muted mb-5"),

        # ── FormErrorSummary ───────────────────────────────────────────────
        H2("1. FormErrorSummary", cls="h4 fw-semibold mb-1"),
        P("Renders a top-of-form alert summarizing all failed validation rules.", cls="text-muted mb-3"),
        P(
            Span("extract_field_error(errors, 'email') → ", cls="text-muted small font-monospace"),
            Span(f'"{email_error}"', cls="badge bg-danger-subtle text-danger-emphasis font-monospace"),
            cls="mb-2",
        ),
        FormErrorSummary(
            errors,
            title="There were errors with your submission",
            variant="danger",
            dismissible=True,
            cls="mb-4",
        ),

        # ── FormSection Multi-Part Layout ──────────────────────────────────
        H2("2. FormSection", cls="h4 fw-semibold mb-1"),
        P("Group related fields under titled sections with descriptions and divider borders.", cls="text-muted mb-3"),
        Card(
            Form(
                FormSection(
                    FormGroup(
                        Input("fullname", placeholder="e.g. Jane Doe", value="Jane Doe"),
                        label="Full Name",
                        required=True,
                    ),
                    FormGroup(
                        Input("email", input_type="email", value="invalid-email"),
                        label="Work Email",
                        **email_val,
                        required=True,
                    ),
                    title="Personal Information",
                    description="Your identity and primary contact channel.",
                ),
                FormSection(
                    FormGroup(
                        Select(
                            "company_size",
                            ("1-10", "1-10 Employees"),
                            ("11-50", "11-50 Employees"),
                            ("51-200", "51-200 Employees"),
                            ("200+", "200+ Enterprise"),
                        ),
                        label="Organization Size",
                    ),
                    FormGroup(
                        Input("role", placeholder="e.g. Lead Architect"),
                        label="Job Title",
                    ),
                    title="Company Details",
                    description="Information regarding your organization.",
                ),
                FormSection(
                    FormGroup(
                        Input("password", input_type="password", value="123"),
                        label="Master Password",
                        **map_formgroup_validation(errors, "password"),
                    ),
                    title="Security Settings",
                    description="Configure access credentials.",
                    divider=False,
                ),
                Button("Save Profile", variant="success", size="lg", type="submit", cls="mt-3"),
                action="/api/save-profile",
                method="post",
            ),
            cls="p-4 mb-5",
        ),

        cls="my-5",
    )


@app.post("/api/save-profile")
def save_profile():
    return Alert("Profile saved successfully!", variant="success")


if __name__ == "__main__":
    serve()
