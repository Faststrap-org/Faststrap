"""
06_feedback/loaders.py
Demonstrates: DotsLoader, PulseLoader, RingLoader, WaveLoader,
              ShadowLoader, PolygonLoader, TypewriterLoader, ProgressRing

All loading state components Faststrap provides, in a gallery format.
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    DotsLoader,
    PulseLoader,
    RingLoader,
    WaveLoader,
    ShadowLoader,
    PolygonLoader,
    TypewriterLoader,
    ProgressRing,
    Card,
    Row,
    Col,
    Stack,
    Badge,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")


def loader_card(title, *content, desc=""):
    return Col(
        Card(
            Stack(*content, gap=2),
            P(desc, cls="text-muted small mt-2 mb-0"),
            header=title,
            cls="h-100 text-center",
        ),
        span=12, md=4, cls="mb-4",
    )


@app.get("/")
def home():
    return Container(
        H1("Loaders & Progress Indicators", cls="display-5 fw-bold mb-2"),
        P("All loading-state components — use instead of plain Spinner for richer UX.", cls="lead text-muted mb-5"),

        H2("Animated Loaders", cls="h4 fw-semibold mb-3"),
        Row(
            loader_card(
                "DotsLoader",
                DotsLoader(variant="primary", label="Loading..."),
                DotsLoader(variant="success"),
                DotsLoader(variant="warning"),
                desc="Animated bouncing dots. variant= matches Bootstrap colours.",
            ),
            loader_card(
                "PulseLoader",
                PulseLoader(variant="primary", size="sm", label="Small"),
                PulseLoader(variant="danger", size="md", label="Medium"),
                PulseLoader(variant="success", size="lg", label="Large"),
                desc="Pulsing circle. Use size= for sm/md/lg.",
            ),
            loader_card(
                "RingLoader",
                RingLoader(variant="primary", label="Connecting"),
                RingLoader(variant="info", size="lg"),
                desc="Spinning ring. size= accepts any CSS value.",
            ),
        ),
        Row(
            loader_card(
                "WaveLoader",
                WaveLoader(variant="primary", label="Uploading..."),
                WaveLoader(variant="success"),
                desc="Oscillating wave bars.",
            ),
            loader_card(
                "PolygonLoader",
                PolygonLoader(label="Processing"),
                desc="Geometric rotating polygon.",
            ),
            loader_card(
                "ShadowLoader",
                ShadowLoader("Fetching data..."),
                ShadowLoader("Please wait"),
                desc="Text with animated shadow. Pass the loading message as first arg.",
            ),
        ),
        Row(
            loader_card(
                "TypewriterLoader",
                TypewriterLoader("Analysing results..."),
                TypewriterLoader("Building your dashboard"),
                desc="Text types out character-by-character.",
            ),
        ),

        # ── ProgressRing ───────────────────────────────────────────────────
        H2("ProgressRing", cls="h4 fw-semibold mb-1 mt-2"),
        P("Circular progress indicator. Value 0–100. variant= and show_text=.", cls="text-muted mb-3"),
        Card(
            Row(
                Col(
                    Stack(
                        ProgressRing(25, variant="danger", show_text=True, label="Risk"),
                        P("25%", cls="fw-bold text-center"),
                        gap=1,
                    ),
                    span=6, md=3, cls="text-center mb-3",
                ),
                Col(
                    Stack(
                        ProgressRing(50, variant="warning", show_text=True, label="Midway"),
                        P("50%", cls="fw-bold text-center"),
                        gap=1,
                    ),
                    span=6, md=3, cls="text-center mb-3",
                ),
                Col(
                    Stack(
                        ProgressRing(75, variant="info", show_text=True, label="Good"),
                        P("75%", cls="fw-bold text-center"),
                        gap=1,
                    ),
                    span=6, md=3, cls="text-center mb-3",
                ),
                Col(
                    Stack(
                        ProgressRing(100, variant="success", show_text=True, label="Complete"),
                        P("100%", cls="fw-bold text-center"),
                        gap=1,
                    ),
                    span=6, md=3, cls="text-center mb-3",
                ),
            ),
            header="ProgressRing — 25 / 50 / 75 / 100%",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
