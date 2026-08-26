"""Flagship showcase — AI Research Hub.

Production-grade ML experiment tracker / model registry for Faststrap:

- create_theme() with AI/tech palette (indigo/cyan)
- Custom CSS for premium research aesthetic
- DataCard for model metadata
- SearchBar for model filtering
- ProfileDropdown for researcher menu
- FilePreview for artifact previews
- Math for loss/metric formulas (KaTeX CDN)
- DashboardGrid, DataTable, Chart, Card, Button
- AutoRefresh for live metrics
- Fx animations throughout
- Port 5021
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    A,
    Button,
    Div,
    FastHTML,
    H1,
    H2,
    H3,
    H4,
    H5,
    Input,
    Link,
    P,
    Script,
    Small,
    Span,
    Style,
    Table,
    Tbody,
    Td,
    Tfoot,
    Thead,
    Tr,
    Th,
    serve,
    Strong
)

from faststrap import (
    Card,
    Chart,
    Col,
    Container,
    DashboardGrid,
    DataCard,
    DataTable,
    FilePreview,
    Math,
    Navbar,
    ProfileDropdown,
    Row,
    SearchBar,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import AutoRefresh, hx_refresh

THEME_KEY = "aihub_theme"

AIHUB_THEME = create_theme(
    primary="#6366f1",
    secondary="#06b6d4",
    success="#10b981",
    danger="#ef4444",
    warning="#f59e0b",
    info="#3b82f6",
)

app = FastHTML()
add_bootstrap(app, theme=AIHUB_THEME, font_family="Inter")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');

:root {
  --aihub-indigo: #6366f1;
  --aihub-cyan: #06b6d4;
  --aihub-bg: #0b0f19;
}

.aihub-shell {
  min-height: 100vh;
  background: var(--aihub-bg);
  color: #e2e8f0;
}

.aihub-shell[data-bs-theme="light"] {
  background: #f8fafc;
  color: #0f172a;
}

.aihub-nav {
  background: rgba(11,15,25,0.85) !important;
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(99,102,241,0.18);
}

.aihub-shell[data-bs-theme="light"] .aihub-nav {
  background: rgba(255,255,255,0.85) !important;
  border-bottom: 1px solid rgba(99,102,241,0.10);
}

.aihub-brand {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  background: linear-gradient(135deg, #6366f1, #06b6d4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.aihub-hero {
  background: radial-gradient(ellipse at 20% 0%, rgba(99,102,241,0.22), transparent 40%),
              radial-gradient(ellipse at 80% 0%, rgba(6,182,212,0.18), transparent 38%);
  padding: 4rem 0;
}

.aihub-card {
  border: 1px solid rgba(99,102,241,0.10);
  border-radius: 14px;
  background: rgba(30,41,59,0.55);
  backdrop-filter: blur(14px);
  transition: box-shadow 0.2s, transform 0.2s;
}

.aihub-shell[data-bs-theme="light"] .aihub-card {
  background: #fff;
  border-color: rgba(99,102,241,0.08);
}

.aihub-card:hover {
  box-shadow: 0 10px 30px rgba(99,102,241,0.12);
  transform: translateY(-2px);
}

.aihub-footer {
  background: rgba(11,15,25,0.6);
  border-top: 1px solid rgba(99,102,241,0.12);
  padding: 2rem 0;
}
"""

MODELS = [
    {
        "id": "MDL-001",
        "name": "Sentiment Transformer",
        "type": "NLP",
        "accuracy": "94.2%",
        "status": "Production",
        "variant": "success",
        "artifact": "model.onnx",
    },
    {
        "id": "MDL-002",
        "name": "Vision ResNet-50",
        "type": "Computer Vision",
        "accuracy": "91.8%",
        "status": "Staging",
        "variant": "warning",
        "artifact": "weights.pth",
    },
    {
        "id": "MDL-003",
        "name": "Tabular XGBoost",
        "type": "Tabular",
        "accuracy": "88.5%",
        "status": "Training",
        "variant": "info",
        "artifact": "checkpoint.pt",
    },
    {
        "id": "MDL-004",
        "name": "Speech Whisper",
        "type": "Audio",
        "accuracy": "96.1%",
        "status": "Production",
        "variant": "success",
        "artifact": "model.bin",
    },
]


def model_card(model: dict, idx: int = 0) -> Any:
    return Card(
        Div(
            Span(model["id"], cls="badge text-bg-primary mb-2"),
            H5(model["name"], cls="card-title mb-2"),
            P(model["type"], cls="text-muted small mb-3"),
            Div(
                Div(
                    Small("Accuracy", cls="text-muted d-block"),
                    Strong(model["accuracy"], cls="h5 mb-0"),
                ),
                Div(
                    Small("Status", cls="text-muted d-block"),
                    Span(model["status"], cls=f"badge text-bg-{model['variant']}"),
                ),
                cls="d-flex justify-content-between",
            ),
        ),
        cls=f"aihub-card h-100",
        style=f"animation-delay:{idx * 80}ms;",
    )


@app.get("/")
def home(req) -> Any:
    theme = req.session.get(THEME_KEY, "dark")
    return Div(
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
        ),
        Script(
            defer=True,
            src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
        ),
        Style(CSS),
        Navbar(
            SearchBar(
                placeholder="Search models, experiments...",
                endpoint="/search",
                target="#search-results",
                cls="me-3",
            ),
            ProfileDropdown(
                "Dr. Sarah Chen",
                subtitle="ML Lead",
                items=[
                    ("Dashboard", "/"),
                    ("Experiments", "/experiments"),
                    ("Settings", "/settings"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="AI Research Hub",
            brand_href="/",
            items=[
                {"text": "Models", "href": "#models"},
                {"text": "Experiments", "href": "#experiments"},
                {"text": "Artifacts", "href": "#artifacts"},
            ],
            variant="dark",
            bg="dark",
            expand="lg",
            sticky="top",
            cls="aihub-nav",
        ),
        Div(cls="aihub-hero mb-5"),
        Container(
            Div(
                H1("Model Registry", cls="display-5 fw-bold mb-2"),
                P(
                    "Track experiments, compare metrics, and deploy models with full artifact lineage.",
                    cls="lead text-muted mb-0",
                ),
                cls="py-5",
            ),
            Row(
                *[
                    Col(model_card(m, idx=i), cols=12, cols_md=6, cols_lg=3)
                    for i, m in enumerate(MODELS)
                ],
                g=3,
                cls="mb-5",
            ),
            H2("Live Experiment Metrics", cls="h4 mb-3"),
            Card(
                AutoRefresh(
                    endpoint="/api/experiment-metrics",
                    target="this",
                    interval=3000,
                    content=Div(
                        P("Loss: 0.0421", cls="mb-1"),
                        P("Accuracy: 94.2%", cls="mb-1"),
                        P("Epoch: 47/100", cls="mb-0 text-muted"),
                    ),
                ),
                title="Live Experiment Metrics",
                cls="aihub-card mb-5",
            ),
            H2("Loss Function", cls="h4 mb-3"),
            Math(
                r"L = -\frac{1}{N}\sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i) \right]",
                display_mode=True,
            ),
            Div(id="search-results", cls="mt-3"),
            H2("Artifacts", cls="h4 mb-3 mt-5"),
            Row(
                Col(
                    FilePreview(
                        src="https://via.placeholder.com/400x300?text=model.onnx",
                        title="model.onnx",
                        height="180px",
                    ),
                    cols=12, cols_md=4,
                ),
                Col(
                    FilePreview(
                        src="https://via.placeholder.com/400x300?text=metrics.json",
                        title="metrics.json",
                        height="180px",
                    ),
                    cols=12, cols_md=4,
                ),
                Col(
                    FilePreview(
                        src="https://via.placeholder.com/400x300?text=config.yaml",
                        title="config.yaml",
                        height="180px",
                    ),
                    cols=12, cols_md=4,
                ),
                g=3,
            ),
            cls="my-5",
        ),
        Div(
            Container(
                P("© 2026 AI Research Hub. Built with Faststrap.", cls="mb-0"),
            ),
            cls="aihub-footer mt-5",
        ),
        cls="aihub-shell",
        data_bs_theme=theme,
    )


@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Type a model or experiment name...", cls="text-muted")
    filtered = [m for m in MODELS if q.lower() in m["name"].lower() or q.lower() in m["type"].lower()]
    if not filtered:
        return P(f"No results for '{q}'", cls="text-muted")
    return Table(
        Thead(Tr(Th("ID"), Th("Name"), Th("Type"), Th("Accuracy"), Th("Status"))),
        Tbody(
            *[
                Tr(
                    Td(m["id"]),
                    Td(m["name"]),
                    Td(m["type"]),
                    Td(m["accuracy"]),
                    Td(Strong(m["status"], cls=f"text-{m['variant']}")),
                )
                for m in filtered
            ]
        ),
        striped=True,
        hover=True,
        cls="mt-3",
    )


@app.get("/api/experiment-metrics")
def experiment_metrics() -> Any:
    import random
    loss = f"{random.uniform(0.03, 0.08):.4f}"
    accuracy = f"{random.uniform(92, 96):.1f}%"
    epoch = random.randint(40, 55)
    return Div(
        P(f"Loss: {loss}", cls="mb-1"),
        P(f"Accuracy: {accuracy}", cls="mb-1"),
        P(f"Epoch: {epoch}/100", cls="mb-0 text-muted"),
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "dark" if req.session.get(THEME_KEY, "dark") == "light" else "light"
    return hx_refresh()


if __name__ == "__main__":
    serve(port=5021)
