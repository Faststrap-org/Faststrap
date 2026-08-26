"""
04_data_display/visual_cards.py
Demonstrates: FlipCard, TiltCard, RevealCard, GlowCard

Interactive card variants with CSS-powered visual effects:
- FlipCard: 3D flip to reveal a back face on hover
- TiltCard: 3D perspective tilt following cursor
- RevealCard: overlay slides up to reveal content on hover
- GlowCard: ambient glow border on hover
"""

from fasthtml.common import FastHTML, H1, H2, H3, H4, P, Div, A, Img, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    FlipCard,
    TiltCard,
    RevealCard,
    GlowCard,
    Button,
    Badge,
    Card,
    Row,
    Col,
    Icon,
    Avatar,
)

app = FastHTML()
add_bootstrap(app, theme="purple-magic", mode="dark")


@app.get("/")
def home():
    return Container(
        H1("Interactive Card Variants", cls="display-5 fw-bold mb-2"),
        P("CSS-powered card effects — no JavaScript required.", cls="lead text-muted mb-5"),

        # ── FlipCard ───────────────────────────────────────────────────────
        H2("FlipCard — hover to flip", cls="h4 fw-semibold mb-1"),
        P("Pass front= and back= content. The card flips on hover.", cls="text-muted mb-3"),
        Row(
            Col(
                FlipCard(
                    front=Div(
                        Avatar("Alice Chen", size="lg", cls="mb-3"),
                        H4("Alice Chen", cls="mb-1"),
                        P("Senior Engineer", cls="text-muted mb-0"),
                        cls="text-center p-4",
                    ),
                    back=Div(
                        H4("About Alice", cls="mb-2"),
                        P("8 years experience in Python and distributed systems.", cls="small mb-3"),
                        Div(
                            Badge("Python", cls="bg-primary me-1"),
                            Badge("FastHTML", cls="bg-success me-1"),
                            Badge("AWS", cls="bg-warning text-dark"),
                        ),
                        Button("View Profile", variant="outline-light", size="sm", cls="mt-3"),
                        cls="text-center p-4",
                    ),
                    height="260px",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                FlipCard(
                    front=Div(
                        Icon("graph-up-arrow", cls="display-4 text-success mb-2"),
                        H4("Revenue Up", cls="mb-1"),
                        P("$48,290 this quarter", cls="text-muted"),
                        cls="text-center p-4",
                    ),
                    back=Div(
                        H4("Breakdown", cls="mb-2"),
                        P("Product A: $22k", cls="small mb-1"),
                        P("Product B: $18k", cls="small mb-1"),
                        P("Services: $8k", cls="small"),
                        cls="text-center p-4",
                    ),
                    height="260px",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col=None,
        ),

        # ── GlowCard ───────────────────────────────────────────────────────
        H2("GlowCard — ambient glow on hover", cls="h4 fw-semibold mb-3 mt-3"),
        Row(
            Col(
                GlowCard(
                    H4("Feature One", cls="mb-2"),
                    P("Hover to see the ambient glow border effect.", cls="text-muted small"),
                    glow_color="rgba(99, 102, 241, 0.6)",
                    cls="p-4 h-100",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                GlowCard(
                    H4("Feature Two", cls="mb-2"),
                    P("glow_color can be any CSS colour value.", cls="text-muted small"),
                    glow_color="rgba(16, 185, 129, 0.6)",
                    intensity="strong",
                    cls="p-4 h-100",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                GlowCard(
                    H4("Feature Three", cls="mb-2"),
                    P("intensity= controls the glow strength.", cls="text-muted small"),
                    glow_color="rgba(249, 115, 22, 0.6)",
                    intensity="subtle",
                    cls="p-4 h-100",
                ),
                span=12, md=4, cls="mb-4",
            ),
        ),

        # ── RevealCard ─────────────────────────────────────────────────────
        H2("RevealCard — hover to reveal", cls="h4 fw-semibold mb-1 mt-3"),
        P("Overlay slides up on hover revealing title, description, and action.", cls="text-muted mb-3"),
        Row(
            Col(
                RevealCard(
                    img_src="https://picsum.photos/seed/rv1/400/300",
                    title="Mountain Retreat",
                    description="Escape to the alpine wilderness. Book now.",
                    action=Button("Book Now", variant="primary", size="sm"),
                    height="220px",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                RevealCard(
                    img_src="https://picsum.photos/seed/rv2/400/300",
                    title="Coastal Resort",
                    description="Sun, sea, and serenity. Limited availability.",
                    action=Button("View Details", variant="outline-light", size="sm"),
                    height="220px",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                RevealCard(
                    img_src="https://picsum.photos/seed/rv3/400/300",
                    title="City Break",
                    description="Explore the best of urban culture and dining.",
                    action=Button("Explore", variant="warning", size="sm"),
                    height="220px",
                ),
                span=12, md=4, cls="mb-4",
            ),
        ),

        # ── TiltCard ───────────────────────────────────────────────────────
        H2("TiltCard — 3D tilt on hover", cls="h4 fw-semibold mb-1 mt-3"),
        P("Move the cursor over the card. The card tilts in 3D following the pointer.", cls="text-muted mb-3"),
        Row(
            Col(
                TiltCard(
                    Div(
                        Icon("code-slash", cls="display-4 text-primary mb-2"),
                        H4("Developer Tools", cls="mb-2"),
                        P("Interactive 3D tilt powered by CSS transforms.", cls="text-muted small"),
                        cls="text-center p-4",
                    ),
                    cls="h-100",
                ),
                span=12, md=4, cls="mb-4",
            ),
            Col(
                TiltCard(
                    Div(
                        Icon("shield-check", cls="display-4 text-success mb-2"),
                        H4("Secure by Default", cls="mb-2"),
                        P("No JavaScript required for the tilt effect.", cls="text-muted small"),
                        cls="text-center p-4",
                    ),
                    cls="h-100",
                ),
                span=12, md=4, cls="mb-4",
            ),
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
