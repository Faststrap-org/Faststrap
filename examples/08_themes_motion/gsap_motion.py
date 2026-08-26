"""
Faststrap v0.7.0 Optional Integrations Demo

Demonstrates opt-in polished integrations:
- ModernToast and ModernToastStack
- ChartJS with add_chartjs(app)
- GSAP Motion with add_gsap(app), GsapReveal, and Gsap attrs
"""

from fasthtml.common import (
    FastHTML,
    H1,
    H5,
    P,
    serve,
)

from faststrap import (
    BadgeGroup,
    Card,
    ChartJS,
    Col,
    Container,
    Gsap,
    GsapReveal,
    ModernToast,
    ModernToastStack,
    ResultCard,
    Row,
    StatusBadge,
    add_bootstrap,
    add_chartjs,
    add_gsap,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")
add_chartjs(app)
add_gsap(app)

CHART_DATA = {
    "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
    "datasets": [
        {
            "label": "Signups",
            "data": [120, 180, 240, 310, 420],
            "borderColor": "#0d9488",
            "backgroundColor": "rgba(13, 148, 136, 0.16)",
            "tension": 0.35,
            "fill": True,
        }
    ],
}


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.7.0 Optional Integrations", cls="display-5 fw-bold mb-2"),
        P(
            "These integrations are opt-in so Faststrap stays zero-JS by default, but polished teams can add richer behavior when they want it.",
            cls="lead text-muted mb-4",
        ),
        GsapReveal(
            Row(
                Col(
                    Card(
                        H5("ModernToast", cls="mb-3"),
                        ModernToastStack(
                            ModernToast(
                                "Saved",
                                "Your dashboard preferences were applied.",
                                variant="success",
                                duration=4000,
                                style="glass",
                            ),
                            ModernToast(
                                "Sync running",
                                "Reports are refreshing in the background.",
                                variant="info",
                                duration=6500,
                                style="soft",
                            ),
                            position="top-end",
                            cls="position-relative p-0 mt-3",
                        ),
                    ),
                    span=12,
                    lg=5,
                ),
                Col(
                    Card(
                        H5("ChartJS", cls="mb-3"),
                        ChartJS(
                            "signup-chart",
                            type="line",
                            data=CHART_DATA,
                            options={"plugins": {"legend": {"display": True}}},
                            height=220,
                        ),
                    ),
                    span=12,
                    lg=7,
                ),
                cls="g-4 mb-4",
            ),
            preset="fade-up",
            stagger=0.08,
        ),
        Row(
            Col(
                Card(
                    H5("GSAP preset attrs", cls="mb-3"),
                    P("Use Python-friendly helpers when you want motion without writing raw JS."),
                    BadgeGroup(
                        StatusBadge("fade-up", status="info"),
                        StatusBadge("pop", status="success"),
                        StatusBadge("stagger", status="pending"),
                    ),
                    **Gsap.pop_attrs(duration=0.5, delay=0.15),
                ),
                span=12,
                md=6,
            ),
            Col(
                Card(
                    H5("Still graceful", cls="mb-3"),
                    P(
                        "If GSAP or Chart.js assets are not loaded, the HTML still renders useful content."
                    ),
                    ResultCard(
                        "Progressive enhancement",
                        "Core Faststrap remains Bootstrap + HTMX friendly.",
                        status="info",
                        compact=True,
                    ),
                    **Gsap.slide_left_attrs(duration=0.45, delay=0.25),
                ),
                span=12,
                md=6,
            ),
            cls="g-4",
        ),
        cls="my-5",
    )


if __name__ == '__main__':
    serve()
