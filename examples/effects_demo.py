"""Faststrap Effects Demo.

Showcasing Phase 5A: Zero-JS Visual Effects & Google Fonts Integration.
"""

from fasthtml.common import H1, H2, H4, Div, FastHTML, P, serve

from faststrap import (
    Card,
    Col,
    Container,
    Fx,
    Icon,
    Row,
    add_bootstrap,
)

# 1. Initialize App with FastHTML
app = FastHTML()

# 2. Add Bootstrap with Theme AND Google Fonts (New Feature!)
# We'll use 'Outfit' font for a modern look
add_bootstrap(
    app, theme="green-nature", mode="light", font_family="Outfit", font_weights=[300, 400, 500, 700]
)


@app.route("/")
def home():
    return Container(
        # Header with effects
        Div(
            H1("✨ Faststrap Effects", cls=f"display-3 fw-bold {Fx.fade_in_down}"),
            P(
                "Zero-JS animations and interactions using native CSS.",
                cls=f"lead {Fx.fade_in_up} {Fx.delay_sm}",
            ),
            P(
                "Now running with Google Font 'Outfit' (Auto-loaded!)",
                cls=f"text-muted small {Fx.fade_in} {Fx.delay_md}",
            ),
            cls="text-center py-5",
        ),
        # Section 1: Entrance Animations
        H2("1. Entrance Animations", cls="mb-4 border-bottom pb-2"),
        Row(
            Col(Card("This card fades in", header="Fade In", cls=[Fx.fade_in, "h-100"])),
            Col(Card("This card slides up", header="Slide Up", cls=[Fx.slide_up, "h-100"])),
            Col(Card("This card slides down", header="Slide Down", cls=[Fx.slide_down, "h-100"])),
            Col(Card("This card zooms in", header="Zoom In", cls=[Fx.zoom_in, "h-100"])),
            Col(Card("This slides from right", header="Slide Left", cls=[Fx.slide_left, "h-100"])),
            Col(Card("This slides from left", header="Slide Right", cls=[Fx.slide_right, "h-100"])),
            Col(Card("This bounces in!", header="Bounce In", cls=[Fx.bounce_in, "h-100"])),
            cls="g-3",
            cols=2,
            cols_md=3,
            cols_lg=4,
        ), 
        # Section 2: Hover Interactions
        H2("2. Hover Interactions", cls="mb-4 border-bottom pb-2 mt-4"),
        P("Hover over these cards to see micro-interactions.", cls="text-muted mb-4"),
        Row(
            Col(
                Card(
                    "I lift up when hovered!",
                    header="Hover Lift",
                    cls=[Fx.base, Fx.hover_lift, "cursor-pointer h-100"],
                ),
            ),
            Col(
                Card(
                    "I get bigger when hovered!",
                    header="Hover Scale",
                    cls=[Fx.base, Fx.hover_scale, "cursor-pointer h-100"],
                ),
            ),
            Col(
                Card(
                    "I 3D tilt when hovered!",
                    header="Hover Tilt",
                    cls=[Fx.base, Fx.hover_tilt, "cursor-pointer h-100"],
                ),
            ),
            Col(
                Card(
                    "I glow with the primary color!",
                    header="Hover Glow",
                    cls=[Fx.base, Fx.hover_glow, "cursor-pointer h-100"],
                ),
            ),
            Col(
                Card(
                    "I start gray and get color!",
                    header="Hover Colorize",
                    cls=[Fx.base, Fx.hover_colorize, "bg-success text-white cursor-pointer h-100"],
                ),
            ),
            cls="g-3",
            cols=2,
            cols_md=3,
            cols_lg=4,
        ),
        # Section 3: Modifiers (Speed & Delay)
        H2("3. Speed & Delay Modifiers", cls="mb-4 border-bottom pb-2 mt-4"),
        Row(
            Col(
                Card("Fast (150ms)", cls=[Fx.base, Fx.hover_lift, Fx.fast, "h-100"]),
            ),
            Col(
                Card("Slow (500ms)", cls=[Fx.base, Fx.hover_lift, Fx.slow, "h-100"]),
            ),
            Col(
                Card("Slower (1000ms)", cls=[Fx.base, Fx.hover_lift, Fx.slower, "h-100"]),
            ),
            Col(
                Card("Delayed (200ms)", cls=[Fx.slide_up, Fx.delay_sm, "bg-light h-100"]),
            ),
            Col(
                Card("Delayed (300ms)", cls=[Fx.slide_up, Fx.delay_md, "bg-light h-100"]),
            ),
            Col(
                Card("Delayed (1000ms)", cls=[Fx.slide_up, Fx.delay_xl, "bg-light h-100"]),
            ),
            cls="g-3",
            cols=2,
            cols_md=3,
            cols_lg=4,
        ),
        # Section 4: Loading States
        H2("4. Loading States", cls="mb-4 border-bottom pb-2 mt-4"),
        Row(
            Col(
                Card(
                    Div(
                        cls=f"rounded bg-secondary {Fx.shimmer}",
                        style="height: 100px; opacity: 0.1",
                    ),
                    header="Shimmer Effect",
                    cls="h-100",
                ),
            ),
            Col(
                Card(
                    Div(
                        Icon("heart-fill", size=2, cls="text-danger"),
                        cls=f"text-center py-4 {Fx.pulse}",
                    ),
                    header="Pulse Effect",
                    cls="h-100",
                ),
            ),
            Col(
                Card(
                    Div(
                        Icon("arrow-repeat", size=2, cls="text-primary"),
                        cls=f"text-center py-4 {Fx.spin}",
                    ),
                    header="Spin Effect",
                    cls="h-100",
                ),
            ),
            cls="g-3",
            cols=2,
            cols_md=3,
            cols_lg=4,
        ),
        # Section 5: Visual Effects
        H2("5. Visual Effects", cls="mb-4 border-bottom pb-2 mt-4"),
        Row(
            Col(
                Card(
                    "This card has a soft shadow.",
                    header="Soft Shadow",
                    cls=[Fx.shadow_soft, "h-100 border-0"],
                ),
            ),
            Col(
                Card(
                    "This card has a sharp retro shadow.",
                    header="Sharp Shadow",
                    cls=[Fx.shadow_sharp, "h-100 border-dark"],
                ),
            ),
            Col(
                Div(
                    H4("Glassmorphism"),
                    P("Blurry background effect."),
                    cls=f"p-4 rounded {Fx.glass} text-dark",
                ),
                style="background: url('https://picsum.photos/id/16/300/200'); background-size: cover; padding: 50px !important;",
            ),
            Col(
                Card(
                    "This background is alive!",
                    header="Gradient Shift",
                    cls=[Fx.gradient_shift, "h-100 text-white"],
                    style="background: linear-gradient(270deg, #ff0000, #0000ff, #00ff00);",
                ),
            ),
            cls="g-3",
            cols=1,
            cols_md=2,
            cols_lg=3,
        ),
        cls="py-4",
        # style="background-color: #f8f9fa; width: 100%;",
    )


if __name__ == "__main__":
    serve(port=5010)
