"""
Faststrap v0.9.0 Display Demo

Demonstrates display components:
- DataCard: structured metadata card for models, datasets, and entities
- FilePreview: generic file preview shell with safe fallback
"""

from fasthtml.common import (
    FastHTML,
    H1,
    H2,
    P,
    serve,
)

from faststrap import (
    Button,
    Col,
    Container,
    DataCard,
    FilePreview,
    Row,
    add_bootstrap,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.9.0 — Display", cls="display-5 fw-bold mb-2"),
        P(
            "Structured metadata cards and generic file preview surfaces.",
            cls="lead text-muted mb-4",
        ),
        Row(
            Col(
                DataCard(
                    "GPT-4o",
                    subtitle="OpenAI",
                    status="active",
                    metrics={
                        "Parameters": "1.8T",
                        "Context": "128K",
                        "Released": "2024",
                    },
                    fields={
                        "Type": "Language Model",
                        "License": "Proprietary",
                        "API": "REST / SDK",
                    },
                    footer=Button("View details", variant="primary", size="sm"),
                    variant="primary",
                ),
                span=12, md=6,
            ),
            Col(
                DataCard(
                    "Sales Dashboard",
                    subtitle="Q4 2024",
                    status="warning",
                    metrics={
                        "Revenue": "$48.2k",
                        "Orders": "384",
                        "Growth": "+5.1%",
                    },
                    fields={
                        "Region": "North America",
                        "Period": "Oct-Dec",
                    },
                ),
                span=12, md=6,
            ),
            g=3,
        ),
        H2("FilePreview", cls="h4 mb-3 mt-4"),
        P("Generic file preview with type inference and safe fallback.", cls="text-muted mb-3"),
        Row(
            Col(
                FilePreview(
                    src="https://via.placeholder.com/400x300.png",
                    title="Screenshot preview",
                    height="200px",
                ),
                span=12, md=4,
            ),
            Col(
                FilePreview(
                    src="https://via.placeholder.com/400x300.pdf",
                    title="Report PDF",
                    height="200px",
                ),
                span=12, md=4,
            ),
            Col(
                FilePreview(
                    src="https://via.placeholder.com/400x300.txt",
                    title="Log file",
                    height="200px",
                ),
                span=12, md=4,
            ),
            g=3,
        ),
        cls="my-5",
    )


if __name__ == '__main__':
    serve()
