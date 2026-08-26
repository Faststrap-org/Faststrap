"""
02_layout/parallax_hero.py
Demonstrates: ParallaxSection

ParallaxSection creates a CSS-only background image hero section with fixed background attachment
and optional dark overlay opacity for text contrast.
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, serve
from faststrap import (
    add_bootstrap,
    Container,
    ParallaxSection,
    Button,
    Card,
    Row,
    Col,
    Cluster,
    Icon,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")


@app.get("/")
def home():
    return Div(
        # ── Parallax Hero Section ──────────────────────────────────────────
        ParallaxSection(
            Container(
                H1("Build Faster with Faststrap", cls="display-4 fw-bold text-white mb-3"),
                P(
                    "High-performance Bootstrap 5.3 components for FastHTML with zero-JS transitions and built-in HTMX presets.",
                    cls="lead text-white-50 mb-4",
                ),
                Cluster(
                    Button("Get Started", variant="primary", size="lg"),
                    Button("View Documentation", variant="outline-light", size="lg"),
                    gap=3,
                    justify="center",
                ),
                cls="text-center py-5",
            ),
            img_src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1600&q=80",
            height="500px",
            overlay_opacity=0.6,
        ),

        Container(
            H2("Content Below Parallax Section", cls="h4 fw-bold mt-5 mb-3"),
            P("Scroll the page to experience the fixed background parallax effect.", cls="text-muted mb-4"),
            Row(
                Col(
                    Card(
                        Icon("speedometer2", cls="display-5 text-primary mb-3"),
                        H2("Blazing Fast", cls="h5 card-title"),
                        P("Server-rendered Python components that compile to raw HTML in microseconds.", cls="card-text text-muted"),
                        cls="h-100 p-4",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
                Col(
                    Card(
                        Icon("code-slash", cls="display-5 text-success mb-3"),
                        H2("HTMX-First", cls="h5 card-title"),
                        P("Interactive server actions without writing client-side JavaScript.", cls="card-text text-muted"),
                        cls="h-100 p-4",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
                Col(
                    Card(
                        Icon("palette", cls="display-5 text-warning mb-3"),
                        H2("Themeable", cls="h5 card-title"),
                        P("10 built-in color themes with instant light/dark mode adaptation.", cls="card-text text-muted"),
                        cls="h-100 p-4",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
            ),
            cls="py-4",
        ),
    )


if __name__ == "__main__":
    serve()
