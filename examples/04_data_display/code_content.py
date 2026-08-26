"""
04_data_display/code_content.py
Demonstrates: CodeBlock, Mermaid, Tag, Kbd

- CodeBlock: syntax-highlighted code snippet with optional filename and copy button
- Mermaid: render diagrams from Mermaid syntax (flowcharts, sequence diagrams, etc.)
- Tag: coloured chip/label for categorisation
- Kbd: keyboard shortcut display
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    CodeBlock,
    Mermaid,
    Tag,
    Kbd,
    Card,
    Stack,
    Cluster,
    Row,
    Col,
)

app = FastHTML()
add_bootstrap(app, theme="indigo-night", mode="dark")

PYTHON_EXAMPLE = """from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Container, Card, Button

app = FastHTML()
add_bootstrap(app, theme="blue-ocean")

@app.get("/")
def home():
    return Container(
        Card(
            Button("Click me", variant="primary"),
            header="Hello Faststrap",
        )
    )

if __name__ == "__main__":
    serve()"""

JS_EXAMPLE = """// HTMX custom event trigger
document.getElementById("my-btn").addEventListener("click", () => {
    htmx.trigger("#target", "faststrap:swap", { value: 42 });
});"""

MERMAID_FLOWCHART = """flowchart TD
    A([User visits page]) --> B{Authenticated?}
    B -->|Yes| C[Load Dashboard]
    B -->|No| D[Redirect to Login]
    D --> E[User logs in]
    E --> C
    C --> F([Show Content])"""

MERMAID_SEQUENCE = """sequenceDiagram
    Browser->>+Server: GET /dashboard
    Server-->>-Browser: HTML + HTMX attrs
    Browser->>+Server: hx-get /api/stats
    Server-->>-Browser: Partial HTML
    Browser->>Browser: Swap into DOM"""


@app.get("/")
def home():
    return Container(
        H1("Code & Content Display", cls="display-5 fw-bold mb-2"),
        P("Components for rendering code, diagrams, tags, and keyboard shortcuts.", cls="lead text-muted mb-5"),

        # ── CodeBlock ──────────────────────────────────────────────────────
        H2("CodeBlock", cls="h4 fw-semibold mb-1"),
        P("Syntax-highlighted code with optional filename and copy button.", cls="text-muted mb-3"),
        Stack(
            CodeBlock(PYTHON_EXAMPLE, language="python", filename="app.py", copy=True),
            CodeBlock(JS_EXAMPLE, language="javascript", filename="events.js", copy=True),
            gap=3,
            cls="mb-5",
        ),

        # ── Mermaid ────────────────────────────────────────────────────────
        H2("Mermaid Diagrams", cls="h4 fw-semibold mb-1"),
        P("Server-side Mermaid rendering. Supports flowcharts, sequence diagrams, gantt, etc.", cls="text-muted mb-3"),
        Row(
            Col(
                Card(Mermaid(MERMAID_FLOWCHART), header="Flowchart — Auth Flow"),
                span=12, md=6, cls="mb-4",
            ),
            Col(
                Card(Mermaid(MERMAID_SEQUENCE), header="Sequence — HTMX Request"),
                span=12, md=6, cls="mb-4",
            ),
        ),

        # ── Tag ────────────────────────────────────────────────────────────
        H2("Tag", cls="h4 fw-semibold mb-1"),
        P("Coloured chips for categories, labels, and filters.", cls="text-muted mb-3"),
        Card(
            Stack(
                Cluster(
                    Tag("python", variant="primary"),
                    Tag("fasthtml", variant="success"),
                    Tag("htmx", variant="info"),
                    Tag("bootstrap", variant="warning"),
                    gap=2,
                ),
                Cluster(
                    Tag("sm chip", variant="secondary", size="sm"),
                    Tag("with icon", variant="primary", icon="code-slash"),
                    Tag("removable", variant="danger", removable=True),
                    gap=2,
                ),
            ),
            header="Tag — variants, sizes, icons, removable",
            cls="mb-5",
        ),

        # ── Kbd ────────────────────────────────────────────────────────────
        H2("Kbd — Keyboard Shortcuts", cls="h4 fw-semibold mb-1"),
        P("Display keyboard shortcuts inline in documentation or help text.", cls="text-muted mb-3"),
        Card(
            Stack(
                P(Span("Save: ", cls="me-2"), Kbd("Ctrl"), Span(" + ", cls="mx-1"), Kbd("S")),
                P(Span("Undo: ", cls="me-2"), Kbd("Ctrl"), Span(" + ", cls="mx-1"), Kbd("Z")),
                P(Span("Find: ", cls="me-2"), Kbd("Ctrl"), Span(" + ", cls="mx-1"), Kbd("F")),
                P(Span("Command Palette: ", cls="me-2"), Kbd("Ctrl", size="lg"), Span(" + ", cls="mx-1"), Kbd("K", size="lg")),
                P(Span("Dark variant: ", cls="me-2"), Kbd("Esc", variant="dark"), Span(" or ", cls="mx-2"), Kbd("Tab", variant="dark")),
                gap=3,
            ),
            header="Kbd — light and dark variants",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
