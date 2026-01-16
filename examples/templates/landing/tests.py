from fasthtml.common import *

from faststrap import Badge, Button, Col, Container, Icon, Row, add_bootstrap

app, rt = fast_app()
add_bootstrap(app)


def LandingPage():
    """Hero section with CTA."""
    return Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge("New: v0.5.0 Released", variant="primary", cls="mb-3 px-3 py-2"),
                        H1(
                            "Build Beautiful UIs in ",
                            Span("Pure Python", cls="text-primary"),
                            cls="display-3 fw-bold mb-4",
                        ),
                        P(
                            "The most complete Bootstrap 5 component library for FastHTML. "
                            "51+ production-ready components with zero JavaScript required.",
                            cls="lead text-muted mb-4 fs-4",
                        ),
                        Div(
                            Button(
                                Icon("rocket-takeoff", cls="me-2"),
                                "Get Started Free",
                                variant="primary",
                                size="lg",
                                cls="me-3 px-4 py-3",
                            ),
                            Button(
                                Icon("github", cls="me-2"),
                                "View on GitHub",
                                variant="outline-secondary",
                                size="lg",
                                cls="px-4 py-3",
                            ),
                            cls="d-flex flex-wrap gap-3",
                        ),
                        Div(
                            Icon("check-circle", cls="text-success me-2"),
                            Span("Free forever", cls="text-muted me-4"),
                            Icon("check-circle", cls="text-success me-2"),
                            Span("MIT License", cls="text-muted me-4"),
                            Icon("check-circle", cls="text-success me-2"),
                            Span("No credit card required", cls="text-muted"),
                            cls="mt-4 d-flex flex-wrap align-items-center",
                        ),
                        cls="text-center text-md-start",
                    ),
                    cols=12,
                    lg=6,
                    cls="d-flex align-items-center",
                ),
                Col(
                    Div(
                        # Code preview
                        Div(
                            Pre(
                                Code(
                                    """from fasthtml.common import *
from faststrap import Card, Button

app, rt = fast_app()
add_bootstrap(app)

@rt("/")
def get():
    return Card(
        "Welcome to Faststrap!",
        Button("Get Started",
               variant="primary"),
        header="Hello World 👋"
    )

serve()""",
                                    cls="language-python text-start",
                                ),
                                cls="bg-dark text-white p-4 rounded shadow-lg",
                            ),
                            cls="position-relative",
                        ),
                        cls="d-none d-lg-block",
                    ),
                    cols=12,
                    lg=6,
                ),
            ),
            cls="py-5",
        ),
        cls="bg-light py-5",
    )


@rt("/")
def get():
    return Div(LandingPage(), cls="bg-light py-5")


serve(port=5006)
