"""
Faststrap v0.7.0 Component Wave Demo

Demonstrates newly added core UI surfaces:
- ResultCard
- Avatar and AvatarGroup
- StatusBadge and BadgeGroup
- Timeline and TimelineItem
- Stepper and StepperStep
- CalendarDatePicker
- InlineEditor
"""

from fasthtml.common import (
    Div,
    FastHTML,
    H1,
    H5,
    P,
    serve,
)

from faststrap import (
    Avatar,
    AvatarGroup,
    BadgeGroup,
    Button,
    CalendarDatePicker,
    Card,
    Col,
    Container,
    InlineEditor,
    ResultCard,
    Row,
    StatusBadge,
    Stepper,
    StepperStep,
    Timeline,
    TimelineItem,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="light")

TEAM = [
    ("Ada Lovelace", "online", "success"),
    ("Alan Turing", "busy", "danger"),
    ("Grace Hopper", "away", "warning"),
    ("Katherine Johnson", "online", "success"),
]


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.7.0 Component Wave", cls="display-5 fw-bold mb-2"),
        P(
            "A focused tour of the new reusable components added during the v0.7.0 roadmap.",
            cls="lead text-muted mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("People and status", cls="mb-3"),
                    AvatarGroup(
                        *[
                            Avatar(name, status=status, status_variant=variant, size="lg")
                            for name, status, variant in TEAM
                        ],
                        total=7,
                        max_visible=3,
                        size="lg",
                        cls="mb-3",
                    ),
                    BadgeGroup(
                        StatusBadge("Production", status="active", show_dot=True),
                        StatusBadge("Sync pending", status="pending", show_dot=True),
                        StatusBadge("Needs review", status="warning", show_dot=True),
                    ),
                ),
                span=12,
                lg=6,
            ),
            Col(
                ResultCard(
                    "Release checklist ready",
                    "All planned component waves are implemented and ready for examples/showcases.",
                    status="success",
                    action=Button("View roadmap", as_="a", href="/roadmap", variant="success"),
                ),
                span=12,
                lg=6,
            ),
            cls="g-4 mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("Workflow stepper", cls="mb-3"),
                    Stepper(
                        StepperStep(
                            "Components", description="Roadmap completed", status="complete"
                        ),
                        StepperStep("Examples", description="Now in progress", status="current"),
                        StepperStep("Showcases", description="Next", status="pending"),
                        StepperStep("Release", description="Major release", status="pending"),
                    ),
                ),
                span=12,
                lg=7,
            ),
            Col(
                Card(
                    H5("Date filter", cls="mb-3"),
                    CalendarDatePicker(
                        "release_date",
                        label="Target date",
                        value="2026-05-07",
                        endpoint="/schedule",
                        hx_target="#schedule-result",
                    ),
                    Div(
                        "Pick a date to preview scheduling feedback.",
                        id="schedule-result",
                        cls="small text-muted mt-2",
                    ),
                ),
                span=12,
                lg=5,
            ),
            cls="g-4 mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("Activity timeline", cls="mb-3"),
                    Timeline(
                        TimelineItem(
                            "Wave 1 shipped",
                            description="ResultCard, Avatar, StatusBadge, BadgeGroup, InlineEditor.",
                            time="Earlier",
                            icon="check",
                            variant="success",
                        ),
                        TimelineItem(
                            "Workflow components shipped",
                            description="Timeline, Stepper, CalendarDatePicker, FormWizard, CommandPalette.",
                            time="Then",
                            icon="diagram-3",
                            variant="primary",
                            active=True,
                        ),
                        TimelineItem(
                            "Examples started",
                            description="Focused examples now cover the new public APIs.",
                            time="Now",
                            icon="code-slash",
                            variant="info",
                        ),
                    ),
                ),
                span=12,
                lg=7,
            ),
            Col(
                Card(
                    H5("Inline edit", cls="mb-3"),
                    InlineEditor(
                        "project_name",
                        "Faststrap Docs Playground",
                        endpoint="/rename",
                        edit_endpoint="/rename/edit",
                        id="project-name-editor",
                    ),
                    P(
                        "Use HTMX endpoints to swap between display and edit states.",
                        cls="small text-muted mt-3 mb-0",
                    ),
                ),
                span=12,
                lg=5,
            ),
            cls="g-4",
        ),
        cls="my-5",
    )


@app.get("/schedule")
def schedule(release_date: str | None = None):
    return Div(
        StatusBadge(f"Scheduled for {release_date or 'a future date'}", status="info"),
        cls="mt-2",
    )


@app.get("/rename/edit")
def rename_edit():
    return InlineEditor(
        "project_name",
        "Faststrap Docs Playground",
        editing=True,
        endpoint="/rename",
        id="project-name-editor",
    )


@app.post("/rename")
def rename(project_name: str = "Faststrap Docs Playground"):
    return InlineEditor(
        "project_name",
        project_name,
        endpoint="/rename",
        edit_endpoint="/rename/edit",
        id="project-name-editor",
    )


if __name__ == '__main__':
    serve()
