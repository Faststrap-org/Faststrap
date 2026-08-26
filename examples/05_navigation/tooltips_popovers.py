"""
05_navigation/tooltips_popovers.py
Demonstrates: Tooltip, Popover

Interactive contextual overlays:
- Tooltip: Hover/focus micro-tips with top/bottom/start/end placements
- Popover: Click/hover content panels with title, rich body, and dismiss
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    Tooltip,
    Popover,
    Button,
    Card,
    Row,
    Col,
    Stack,
    Cluster,
    Icon,
)

app = FastHTML()
add_bootstrap(app, theme="cyan-sky", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Tooltips & Popovers", cls="display-5 fw-bold mb-2"),
        P("Contextual guidance and popup cards using Bootstrap overlays.", cls="lead text-muted mb-5"),

        # ── Tooltips ───────────────────────────────────────────────────────
        H2("1. Tooltips", cls="h4 fw-semibold mb-1"),
        P("Micro-information on hover or focus. Supports 4 cardinal placements.", cls="text-muted mb-3"),
        Card(
            Cluster(
                Tooltip(
                    "Tooltip on top",
                    Button("Tooltip Top", variant="primary"),
                    placement="top",
                ),
                Tooltip(
                    "Tooltip on bottom",
                    Button("Tooltip Bottom", variant="secondary"),
                    placement="bottom",
                ),
                Tooltip(
                    "Tooltip on start (left)",
                    Button("Tooltip Start", variant="success"),
                    placement="left",
                ),
                Tooltip(
                    "Tooltip on end (right)",
                    Button("Tooltip End", variant="info"),
                    placement="right",
                ),
                gap=3,
            ),
            header="Tooltip Placements",
            cls="mb-5",
        ),

        # ── Popovers ───────────────────────────────────────────────────────
        H2("2. Popovers", cls="h4 fw-semibold mb-1"),
        P("Richer popups with titles and body content, triggered on click or hover.", cls="text-muted mb-3"),
        Card(
            Cluster(
                Popover(
                    "Account Security",
                    "Two-factor authentication is recommended for all administrator accounts.",
                    Button(Icon("shield-lock", cls="me-1"), "Security Info", variant="primary"),
                    placement="top",
                ),
                Popover(
                    "API Quota Details",
                    "You have consumed 84,200 of your 100,000 monthly requests.",
                    Button(Icon("speedometer", cls="me-1"), "Quota Status", variant="warning"),
                    placement="right",
                ),
                Popover(
                    "Quick Tip",
                    "Hover to preview without clicking!",
                    Button(Icon("info-circle", cls="me-1"), "Hover Trigger", variant="outline-dark"),
                    trigger="hover focus",
                    placement="bottom",
                ),
                gap=3,
            ),
            header="Interactive Popover Cards",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
