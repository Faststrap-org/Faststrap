"""
02_layout/containers.py
Demonstrates: Stack, Cluster, Center, Separator

- Stack: vertical spacing between children using gap=
- Cluster: horizontal wrapping layout for badges, button groups
- Center: horizontally centered container with optional max_width
- Separator: horizontal rule with optional label
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    Stack,
    Cluster,
    Center,
    Separator,
    Button,
    Badge,
    Card,
    Alert,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Layout Primitives", cls="display-5 fw-bold mb-2"),
        P(
            "Composable layout primitives that handle spacing and alignment "
            "without custom CSS.",
            cls="lead text-muted mb-5",
        ),

        # ── Stack ──────────────────────────────────────────────────────────
        H2("Stack", cls="h4 fw-semibold mb-1"),
        P("Evenly spaces children vertically. Use gap= to control spacing (Bootstrap spacing scale 1–5).", cls="text-muted mb-3"),
        Card(
            Stack(
                Alert("First notification", variant="info"),
                Alert("Second notification", variant="success"),
                Alert("Third notification", variant="warning"),
                gap=3,
            ),
            header="Stack(gap=3) — vertical rhythm",
            cls="mb-5",
        ),

        # ── Cluster ────────────────────────────────────────────────────────
        H2("Cluster", cls="h4 fw-semibold mb-1"),
        P("Groups children horizontally, wrapping when they overflow. Perfect for tag clouds and button sets.", cls="text-muted mb-3"),
        Card(
            Cluster(
                Badge("Python", cls="bg-primary"),
                Badge("FastHTML", cls="bg-success"),
                Badge("Faststrap", cls="bg-info text-dark"),
                Badge("HTMX", cls="bg-warning text-dark"),
                Badge("Bootstrap 5", cls="bg-secondary"),
                Badge("SQLite", cls="bg-dark"),
                Badge("Uvicorn", cls="bg-danger"),
                gap=2,
            ),
            header="Cluster — wrapping tag cloud",
            cls="mb-3",
        ),
        Card(
            Cluster(
                Button("Save", variant="primary"),
                Button("Save & Continue", variant="outline-primary"),
                Button("Preview", variant="outline-secondary"),
                Button("Discard", variant="outline-danger"),
                gap=2,
            ),
            header="Cluster — button toolbar",
            cls="mb-5",
        ),

        # ── Center ─────────────────────────────────────────────────────────
        H2("Center", cls="h4 fw-semibold mb-1"),
        P("Centers content horizontally. max_width= limits expansion. text_center= aligns text.", cls="text-muted mb-3"),
        Card(
            Center(
                H2("Centered Hero", cls="display-6 mb-2"),
                P("This block is limited to 480px wide and horizontally centered within the card."),
                Cluster(
                    Button("Get Started", variant="primary"),
                    Button("Learn More", variant="outline-secondary"),
                    gap=2,
                ),
                max_width="480px",
                text_center=True,
            ),
            header="Center(max_width='480px', text_center=True)",
            cls="mb-5",
        ),

        # ── Separator ──────────────────────────────────────────────────────
        H2("Separator", cls="h4 fw-semibold mb-1"),
        P("A styled horizontal rule. label= places text in the centre.", cls="text-muted mb-3"),
        Card(
            Stack(
                P("First section content — enter your email below."),
                Separator(),
                P("Second section content — or choose a social login."),
                Separator(label="OR"),
                Button("Continue with Google", variant="outline-secondary", cls="w-100"),
                Separator(label="already have an account?", cls="text-muted small"),
                Button("Sign In", variant="link", cls="w-100"),
                gap=3,
            ),
            header="Separator — plain and labelled",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
