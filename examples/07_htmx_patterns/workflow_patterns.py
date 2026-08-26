"""
Faststrap v0.7.0 Workflow Patterns Demo

Demonstrates:
- CommandPalette and CommandItem
- FormWizard and WizardStep
- LiveValidationField and ValidationMessage
- Pagination HTMX/query helpers
- DataTable.query_params and DataTable.page_url
- ConfirmAction
- theme_variant_css
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
    Card,
    Col,
    CommandItem,
    CommandPalette,
    ConfirmAction,
    Container,
    DataTable,
    EmptyState,
    FormWizard,
    Input,
    LiveValidationField,
    Pagination,
    ResultCard,
    Row,
    Select,
    Spinner,
    ValidationMessage,
    WizardStep,
    add_bootstrap,
    theme_variant_css,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")

PEOPLE = [
    {"name": "Ada Lovelace", "role": "Research", "status": "Active"},
    {"name": "Alan Turing", "role": "Security", "status": "Review"},
    {"name": "Grace Hopper", "role": "Platform", "status": "Active"},
    {"name": "Katherine Johnson", "role": "Analytics", "status": "Invited"},
    {"name": "Dorothy Vaughan", "role": "Operations", "status": "Active"},
]


CUSTOM_CSS = theme_variant_css(
    ".workflow-surface",
    light={"background": "rgba(255, 255, 255, 0.82)", "border-color": "rgba(13, 110, 253, 0.16)"},
    dark={"background": "rgba(15, 23, 42, 0.68)", "border-color": "rgba(125, 211, 252, 0.24)"},
)


def command_results(q: str = ""):
    commands = [
        ("Open dashboard", "Go to the operations dashboard", "speedometer2", "G D"),
        ("Create invoice", "Start a finance workflow", "receipt", "C I"),
        ("Invite teammate", "Send a workspace invite", "person-plus", "I T"),
    ]
    query = q.lower().strip()
    filtered = [item for item in commands if not query or query in item[0].lower()]
    if not filtered:
        return EmptyState("No commands", description="Try another search term.", compact=True)
    return [
        CommandItem(label, description=description, icon=icon, shortcut=shortcut, href="#")
        for label, description, icon, shortcut in filtered
    ]


@app.get("/")
def home(page: int = 1, q: str = ""):
    current_page = max(1, min(page, 3))
    params = DataTable.query_params(
        search=q, filters={"segment": "team"}, page=current_page, per_page=2
    )
    next_url = DataTable.page_url("/", page=min(current_page + 1, 3), per_page=2, search=q)
    return Container(
        CUSTOM_CSS,
        H1("Faststrap v0.7.0 Workflow Patterns", cls="display-5 fw-bold mb-2"),
        P(
            "Server-driven interaction patterns that stay Pythonic and HTMX-friendly.",
            cls="lead text-muted mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("Command palette", cls="mb-3"),
                    CommandPalette(
                        *command_results(q),
                        id="workflow-command-palette",
                        endpoint="/commands",
                        placeholder="Search actions...",
                    ),
                    cls="workflow-surface border",
                ),
                span=12,
                lg=6,
            ),
            Col(
                Card(
                    H5("Live validation", cls="mb-3"),
                    LiveValidationField(
                        Input("email", input_type="email", placeholder="you@example.com"),
                        "/validate/email",
                        label="Email",
                        help_text="Blur the field to validate with HTMX.",
                        indicator="#email-spinner",
                    ),
                    Spinner(size="sm", id="email-spinner", cls="htmx-indicator"),
                    Div(id="email-feedback"),
                    cls="workflow-surface border",
                ),
                span=12,
                lg=6,
            ),
            cls="g-4 mb-4",
        ),
        Row(
            Col(
                Card(
                    H5("Form wizard", cls="mb-3"),
                    FormWizard(
                        WizardStep(
                            "Profile",
                            Input("name", placeholder="Workspace name"),
                            description="Name",
                        ),
                        WizardStep(
                            "Plan",
                            Select("plan", ("starter", "Starter"), ("pro", "Pro")),
                            description="Plan",
                        ),
                        WizardStep(
                            "Confirm",
                            ResultCard("Ready", "Review and finish.", status="info", compact=True),
                            description="Confirm",
                        ),
                        current_step=1,
                        endpoint="/wizard",
                        hx_target="#wizard-result",
                    ),
                    Div(id="wizard-result"),
                    cls="workflow-surface border",
                ),
                span=12,
                lg=7,
            ),
            Col(
                Card(
                    H5("Pagination and action helpers", cls="mb-3"),
                    P(f"Reusable query params: {params}", cls="small text-muted"),
                    P(f"Next page URL: {next_url}", cls="small text-muted"),
                    Pagination(
                        current_page=current_page,
                        total_pages=3,
                        base_url="/",
                        query_params={"q": q},
                        htmx=True,
                        hx_target="#pager-demo",
                        hx_push_url=True,
                    ),
                    ConfirmAction(
                        "Archive selected",
                        url="/archive",
                        method="delete",
                        confirm="Archive the selected people?",
                        target="#archive-result",
                        swap="outerHTML",
                    ),
                    Div(id="archive-result", cls="mt-3"),
                    id="pager-demo",
                    cls="workflow-surface border",
                ),
                span=12,
                lg=5,
            ),
            cls="g-4 mb-4",
        ),
        Card(
            H5("DataTable state", cls="mb-3"),
            DataTable(
                PEOPLE,
                sortable=True,
                searchable=True,
                pagination=True,
                page=current_page,
                per_page=2,
                base_url="/",
                filters={"segment": "team"},
            ),
            cls="workflow-surface border",
        ),
        cls="my-5",
    )


@app.get("/commands")
def commands(q: str = ""):
    return Div(*command_results(q))


@app.post("/validate/email")
def validate_email(email: str = ""):
    if "@" not in email:
        return ValidationMessage("Enter a valid email address.", state="invalid")
    return ValidationMessage("Email looks good.", state="valid")


@app.post("/wizard")
def wizard(step: int = 0):
    return ResultCard("Wizard moved", f"Requested step {step}.", status="success", compact=True)


@app.delete("/archive")
def archive():
    return ResultCard(
        "Archived",
        "The selected people were archived.",
        status="success",
        compact=True,
        id="archive-result",
    )


if __name__ == '__main__':
    serve()
