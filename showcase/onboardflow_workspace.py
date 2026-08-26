"""Flagship v0.7.0 showcase - OnboardFlow Workspace.

A polished onboarding/product-workflow reference for the v0.7.0 component set:

- FormWizard and Stepper for guided setup
- LiveValidationField for HTMX-friendly validation
- CalendarDatePicker and InlineEditor for form/product interactions
- ConfirmAction for safe destructive actions
- AvatarGroup, StatusBadge, ResultCard, Timeline for workflow context
- GSAP optional motion integration for showcase-grade polish
"""

from __future__ import annotations

from fasthtml.common import H1, H5, Div, FastHTML, P, Span, Style, serve

from faststrap import (
    Avatar,
    AvatarGroup,
    BadgeGroup,
    CalendarDatePicker,
    Card,
    Col,
    ConfirmAction,
    Container,
    FormWizard,
    Gsap,
    InlineEditor,
    Input,
    LiveValidationField,
    ModernToast,
    ModernToastStack,
    ProfileDropdown,
    ResultCard,
    Row,
    StatusBadge,
    Stepper,
    StepperStep,
    Timeline,
    TimelineItem,
    ValidationMessage,
    WizardStep,
    add_bootstrap,
    add_gsap,
    create_theme,
)

FLOW_THEME = create_theme(
    primary="#0F766E",
    secondary="#1F2937",
    success="#22C55E",
    danger="#EF4444",
    warning="#F59E0B",
    info="#38BDF8",
)

app = FastHTML()
add_bootstrap(app, theme=FLOW_THEME, mode="light", font_family="Inter")
add_gsap(app)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,800&display=swap');

.flow-shell {
  min-height: 100vh;
  background:
    radial-gradient(circle at 6% 4%, rgba(15, 118, 110, 0.22), transparent 27%),
    radial-gradient(circle at 92% 10%, rgba(245, 158, 11, 0.16), transparent 24%),
    linear-gradient(180deg, #f6f1e8 0%, #eef7f4 54%, #edf5ff 100%);
  color: #10201e;
}

.flow-title {
  font-family: 'Fraunces', serif;
  font-size: clamp(2.8rem, 7vw, 5.6rem);
  line-height: 0.96;
  letter-spacing: -0.055em;
}

.flow-card {
  background: rgba(255, 255, 255, 0.78) !important;
  border: 1px solid rgba(15, 118, 110, 0.14) !important;
  border-radius: 26px !important;
  box-shadow: 0 24px 80px rgba(15, 23, 42, 0.08);
  backdrop-filter: blur(16px);
}

.flow-hero-card {
  background:
    linear-gradient(145deg, rgba(15, 118, 110, 0.95), rgba(17, 94, 89, 0.9)),
    radial-gradient(circle at 80% 0%, rgba(251, 191, 36, 0.26), transparent 30%);
  color: #ecfeff;
  border-radius: 32px;
  box-shadow: 0 34px 90px rgba(15, 118, 110, 0.28);
}

.flow-pill {
  border: 1px solid rgba(15, 118, 110, 0.18);
  background: rgba(255, 255, 255, 0.72);
}

.flow-panel-title {
  font-family: 'Fraunces', serif;
  letter-spacing: -0.035em;
}

.faststrap-modern-toast-stack.position-relative {
  position: relative !important;
  inset: auto !important;
  transform: none !important;
}
"""


def wizard(current_step: int = 0) -> FormWizard:
    return FormWizard(
        WizardStep(
            "Workspace",
            Input("workspace", placeholder="Acme Studio", label="Workspace name"),
            LiveValidationField(
                Input("email", input_type="email", placeholder="founder@example.com"),
                "/validate/email",
                label="Admin email",
                help_text="Validated with a small HTMX endpoint.",
            ),
            description="Name and owner",
            icon="building",
        ),
        WizardStep(
            "Team",
            AvatarGroup(
                Avatar("Ada Lovelace", status="online", size="lg"),
                Avatar("Grace Hopper", status="away", size="lg"),
                Avatar("Alan Turing", status="busy", size="lg"),
                total=6,
                max_visible=3,
                size="lg",
                cls="mb-3",
            ),
            BadgeGroup(
                StatusBadge("Design", status="info"),
                StatusBadge("Engineering", status="active"),
                StatusBadge("Ops", status="pending"),
            ),
            description="Invite collaborators",
            icon="people",
        ),
        WizardStep(
            "Launch",
            CalendarDatePicker("launch_date", label="Launch date", value="2026-05-21"),
            ResultCard(
                "Ready to launch",
                "Your workspace settings are ready for review.",
                status="success",
                compact=True,
            ),
            description="Date and review",
            icon="rocket-takeoff",
        ),
        current_step=current_step,
        endpoint="/wizard",
        hx_target="#wizard-shell",
        id="wizard-shell",
    )


def page() -> Div:
    return Div(
        Style(CSS),
        Container(
            Row(
                Col(
                    Div(
                        Span("ONBOARDFLOW", cls="badge rounded-pill text-bg-success mb-3"),
                        H1("A calmer way to launch new workspaces", cls="flow-title mb-4"),
                        P(
                            "A v0.7.0 Faststrap reference for onboarding surfaces, server-driven wizards, live validation, and optional motion.",
                            cls="lead text-muted mb-4",
                        ),
                        Div(
                            StatusBadge("Setup guided", status="active", show_dot=True),
                            StatusBadge("HTMX ready", status="info", show_dot=True),
                            StatusBadge("Zero-JS core", status="success", show_dot=True),
                            cls="d-flex flex-wrap gap-2",
                        ),
                    ),
                    cols=12,
                    lg=7,
                    **Gsap.fade_up_attrs(duration=0.55),
                ),
                Col(
                    Div(
                        H5("Launch health", cls="mb-3"),
                        Stepper(
                            StepperStep("Profile", status="complete", icon="check"),
                            StepperStep("Team", status="current", step=2),
                            StepperStep("Launch", status="pending", step=3),
                            orientation="vertical",
                        ),
                        cls="flow-hero-card p-4",
                    ),
                    cols=12,
                    lg=5,
                    **Gsap.pop_attrs(duration=0.55, delay=0.12),
                ),
                cls="g-5 align-items-center py-5",
            ),
            Row(
                Col(
                    Card(
                        H5("Guided setup", cls="flow-panel-title h3 mb-3"),
                        wizard(0),
                        cls="flow-card",
                    ),
                    cols=12,
                    lg=7,
                ),
                Col(
                    Card(
                        H5("Workspace controls", cls="flow-panel-title h3 mb-3"),
                        InlineEditor(
                            "workspace_name",
                            "Northwind Studio",
                            endpoint="/workspace/name",
                            edit_endpoint="/workspace/name/edit",
                            id="workspace-name",
                        ),
                        Div(cls="my-4"),
                        ProfileDropdown(
                            "Alex Operator",
                            subtitle="Workspace Admin",
                            items=[
                                ("Profile", "/profile"),
                                ("Settings", "/settings"),
                                ("Sign out", "/logout"),
                            ],
                        ),
                        Div(cls="my-4"),
                        ConfirmAction(
                            "Reset setup",
                            url="/workspace/reset",
                            method="delete",
                            confirm="Reset this onboarding flow?",
                            target="#reset-result",
                            swap="outerHTML",
                            variant="danger",
                        ),
                        Div(id="reset-result", cls="mt-3"),
                        cls="flow-card",
                    ),
                    cols=12,
                    lg=5,
                ),
                cls="g-4 mb-4",
            ),
            Row(
                Col(
                    Card(
                        H5("Launch timeline", cls="flow-panel-title h3 mb-3"),
                        Timeline(
                            TimelineItem(
                                "Workspace created",
                                description="Core settings and owner profile configured.",
                                time="Today",
                                icon="building",
                                variant="success",
                                active=True,
                            ),
                            TimelineItem(
                                "Team invites queued",
                                description="Three launch collaborators will receive invites.",
                                time="Next",
                                icon="envelope",
                                variant="info",
                            ),
                            TimelineItem(
                                "Launch review",
                                description="Final review before publishing the workspace.",
                                time="Soon",
                                icon="rocket-takeoff",
                                variant="warning",
                            ),
                        ),
                        cls="flow-card",
                    ),
                    cols=12,
                    lg=7,
                ),
                Col(
                    Card(
                        H5("Feedback style", cls="flow-panel-title h3 mb-3"),
                        ModernToastStack(
                            ModernToast(
                                "Invite queued",
                                "Grace will receive a workspace invite.",
                                variant="success",
                                style="glass",
                            ),
                            ModernToast(
                                "Review needed",
                                "Billing details are still incomplete.",
                                variant="warning",
                                style="soft",
                            ),
                            position="top-end",
                            cls="position-relative p-0",
                        ),
                        cls="flow-card",
                    ),
                    cols=12,
                    lg=5,
                ),
                cls="g-4 pb-5",
            ),
        ),
        cls="flow-shell",
    )


@app.get("/")
def home():
    return page()


@app.post("/validate/email")
def validate_email(email: str = ""):
    if "@" not in email:
        return ValidationMessage("Use a valid email address.", state="invalid")
    return ValidationMessage("This email is ready for invites.", state="valid")


@app.post("/wizard")
def wizard_route(step: int = 0):
    return wizard(step)


@app.get("/workspace/name/edit")
def edit_workspace_name():
    return InlineEditor(
        "workspace_name",
        "Northwind Studio",
        editing=True,
        endpoint="/workspace/name",
        id="workspace-name",
    )


@app.post("/workspace/name")
def save_workspace_name(workspace_name: str = "Northwind Studio"):
    return InlineEditor(
        "workspace_name",
        workspace_name,
        endpoint="/workspace/name",
        edit_endpoint="/workspace/name/edit",
        id="workspace-name",
    )


@app.delete("/workspace/reset")
def reset_workspace():
    return ResultCard(
        "Setup reset",
        "The onboarding flow returned to step one.",
        status="warning",
        compact=True,
        id="reset-result",
    )


if __name__ == "__main__":
    serve(port=5029)
