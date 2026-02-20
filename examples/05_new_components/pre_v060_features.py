"""
Pre-v0.6.0 Features Demo

Demonstrates:
- Accessibility helpers
- ToggleGroup
- TextClamp
- Notification presets
- FormGroup error mapping
- PageMeta composition
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.get("/")
def home():
    long_text = (
        "Faststrap is a frontend bootstrap framework for Python developers. "
        "This demo shows pre-v0.6.0 capabilities with accessibility defaults, "
        "single-active button groups, long-text rendering helpers, notification presets, "
        "and page metadata composition in one place."
    ) * 2

    return (
        PageMeta(
            title="Faststrap Pre-v0.6 Features",
            description="Demo for new pre-v0.6.0 Faststrap features",
            canonical="https://example.com/pre-v060-demo",
            include_pwa=True,
            pwa_name="Faststrap Demo",
            pwa_short_name="FSDemo",
        ),
        Container(
            SkipLink("#main-content"),
            Div(
                H1("Pre-v0.6.0 Feature Demo", cls="mb-4"),
                Card(
                    H5("1. ToggleGroup"),
                    P("Single-active state for grouped buttons."),
                    ToggleGroup(
                        Button("Newest", variant="outline-primary", cls="me-2"),
                        Button("Popular", variant="outline-primary", active=True, cls="me-2"),
                        Button("Trending", variant="outline-primary"),
                        name="sort",
                        values=["new", "popular", "trending"],
                        # cls="d-flex gap-4"
                    ),
                    cls="mb-4",
                ),
                Card(
                    H5("2. TextClamp"),
                    TextClamp(
                        long_text,
                        max_chars=180,
                        expand_label="Read more",
                        collapse_label="Collapse",
                    ),
                    cls="mb-4",
                ),
                Card(
                    H5("3. Notification Presets"),
                    Div(
                        SuccessToast("Profile saved", cls="mb-2"),
                        WarningToast("Subscription expires soon", cls="mb-2"),
                        InfoToast("You have 3 new messages"),
                        cls="d-flex flex-column gap-2",
                    ),
                    cls="mb-4",
                ),
                Card(
                    H5("4. FormGroupFromErrors"),
                    FormGroupFromErrors(
                        Input(name="email", type="email", value="invalid"),
                        field="email",
                        errors={"email": "Please enter a valid email address."},
                        label="Email Address",
                    ),
                    cls="mb-4",
                ),
                Card(
                    H5("5. Accessibility"),
                    P("Status update example:"),
                    LiveRegion("Saved successfully", politeness="polite"),
                    Div(
                        Button("Open dialog", variant="secondary"),
                        FocusTrap(
                            Input(name="demo"),
                            Button("Close", variant="outline-secondary"),
                            cls="border rounded p-3 mt-3",
                        ),
                    ),
                ),
                id="main-content",
                cls="my-5",
            ),
        ),
    )


serve()
