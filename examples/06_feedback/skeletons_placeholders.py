"""
06_feedback/skeletons_placeholders.py
Demonstrates: Placeholder, PlaceholderCard, PlaceholderButton, SimpleToast

- Placeholder & PlaceholderCard: Skeleton loading screens that improve perceived performance
- SimpleToast: Pure CSS toast notifications that work without JavaScript
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    Placeholder,
    PlaceholderCard,
    PlaceholderButton,
    SimpleToast,
    Card,
    Row,
    Col,
    Stack,
    Button,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")


@app.get("/")
def home():
    return Container(
        # Pure CSS Toast Notification
        SimpleToast(
            "Welcome! This toast is animated with pure CSS and requires no JS.",
            title="Faststrap Notice",
            variant="primary",
            position="top-end",
        ),

        H1("Skeleton Loaders & Pure-CSS Toasts", cls="display-5 fw-bold mb-2"),
        P("Maintain layout stability while content loads asynchronously.", cls="lead text-muted mb-5"),

        # ── Pre-built Skeleton Cards ───────────────────────────────────────
        H2("1. PlaceholderCard (Pre-built Card Skeletons)", cls="h4 fw-semibold mb-1"),
        P("Instant skeleton surfaces with animated wave and glow effects.", cls="text-muted mb-3"),
        Row(
            Col(
                PlaceholderCard(animation="wave", show_image=True),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                PlaceholderCard(animation="glow", show_image=True),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                PlaceholderCard(animation="wave", show_image=False),
                span=12, md=4, cls="mb-4",
            ),
        ),

        # ── Custom Placeholder Skeletons ───────────────────────────────────
        H2("2. Granular Placeholder Elements", cls="h4 fw-semibold mb-1"),
        P("Assemble custom loading shapes using Placeholder with width, height, and variant.", cls="text-muted mb-3"),
        Card(
            Stack(
                Placeholder(width="40%", height="24px", animation="glow", variant="primary", cls="mb-2"),
                Placeholder(width="80%", height="16px", animation="wave", cls="mb-1"),
                Placeholder(width="65%", height="16px", animation="wave", cls="mb-3"),
                Div(
                    PlaceholderButton(width="120px", animation="glow", variant="primary"),
                    PlaceholderButton(width="90px", animation="wave", variant="secondary", cls="ms-2"),
                ),
                gap=2,
            ),
            header="Custom Skeleton Block",
            cls="p-4 mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
