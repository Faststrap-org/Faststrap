"""
03_forms/advanced_buttons.py
Demonstrates: GradientButton, FloatingActionButton, CloseButton, PlaceholderButton

Beyond the standard Button, Faststrap has specialised button variants
for visual effects, fixed-position actions, dismiss controls, and skeleton states.
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    GradientButton,
    FloatingActionButton,
    CloseButton,
    PlaceholderButton,
    Alert,
    Card,
    Row,
    Col,
    Stack,
    Cluster,
    Icon,
)

app = FastHTML()
add_bootstrap(app, theme="orange-sunset", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Advanced Buttons", cls="display-5 fw-bold mb-2"),
        P("Specialised button variants for gradients, FABs, dismiss controls, and loading states.", cls="lead text-muted mb-5"),

        # ── GradientButton ─────────────────────────────────────────────────
        H2("GradientButton", cls="h4 fw-semibold mb-1"),
        P("Pre-built gradient presets for eye-catching CTAs.", cls="text-muted mb-3"),
        Card(
            Cluster(
                GradientButton("Sunrise", gradient="sunrise"),
                GradientButton("Ocean", gradient="ocean"),
                GradientButton("Forest", gradient="forest"),
                GradientButton("Candy", gradient="candy"),
                GradientButton("Midnight", gradient="midnight"),
                gap=2,
            ),
            Cluster(
                GradientButton("Small", gradient="sunrise", size="sm"),
                GradientButton("Medium", gradient="ocean", size="md"),
                GradientButton("Large", gradient="forest", size="lg"),
                gap=2,
                cls="mt-3",
            ),
            header="GradientButton — all presets and sizes",
            cls="mb-5",
        ),

        # ── CloseButton ────────────────────────────────────────────────────
        H2("CloseButton", cls="h4 fw-semibold mb-1"),
        P("Accessible dismiss button — used in alerts, modals, drawers, and toasts.", cls="text-muted mb-3"),
        Card(
            Cluster(
                Div(
                    Span("Default close button: ", cls="me-2"),
                    CloseButton(),
                ),
                Div(
                    Span("White variant (for dark backgrounds): ", cls="me-2 text-white"),
                    CloseButton(white=True),
                    cls="bg-dark p-2 rounded",
                ),
                gap=3,
            ),
            header="CloseButton — default and white",
            cls="mb-5",
        ),

        # ── PlaceholderButton ──────────────────────────────────────────────
        H2("PlaceholderButton", cls="h4 fw-semibold mb-1"),
        P("A skeleton placeholder that looks like a button — for loading states.", cls="text-muted mb-3"),
        Card(
            Cluster(
                PlaceholderButton(width="100px", animation="glow"),
                PlaceholderButton(width="140px", animation="wave"),
                PlaceholderButton(width="80px", animation="glow", variant="secondary"),
                gap=2,
            ),
            header="PlaceholderButton — glow and wave animations",
            cls="mb-5",
        ),

        # ── FloatingActionButton ───────────────────────────────────────────
        H2("FloatingActionButton (FAB)", cls="h4 fw-semibold mb-1"),
        P("Fixed-position primary action button. position= controls corner placement.", cls="text-muted mb-3"),
        Card(
            Alert("A FAB is fixed to the viewport corner. Scroll down to see it stay in place.", variant="info"),
            P("Available positions: bottom-end (default), bottom-start, top-end, top-start"),
            header="FloatingActionButton",
        ),

        # FAB rendered outside card so it's fixed to viewport
        FloatingActionButton(icon="plus-lg", variant="primary", label="Add New Item", position="top-end", cls="m-4"),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
