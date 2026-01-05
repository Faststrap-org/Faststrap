"""
Example: Effects Showcase

Demonstrates: All Faststrap effects in action
Components: Card, Button, Badge, Fx effects
Difficulty: Advanced

See all available Faststrap effects:
- Entrance animations
- Hover interactions
- Loading states
- Visual effects
- Modifiers (speed, delay)
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)


@app.route("/")
def get():
    return Container(
        H1("Faststrap Effects Showcase", cls=f"{Fx.fade_in} text-center mb-5"),
        # Entrance Animations
        Card(
            H3("Entrance Animations", cls="mb-4"),
            Row(
                Col(Card("Fade In", cls=f"{Fx.fade_in}"), md=3),
                Col(Card("Slide Up", cls=f"{Fx.slide_up}"), md=3),
                Col(Card("Slide Down", cls=f"{Fx.slide_down}"), md=3),
                Col(Card("Zoom In", cls=f"{Fx.zoom_in}"), md=3),
            ),
            cls="mb-4 p-4",
        ),
        # Hover Effects
        Card(
            H3("Hover Effects", cls="mb-4"),
            P("Hover over these cards to see the effects:", cls="text-muted mb-3"),
            Row(
                Col(Card("Hover Lift", cls=f"{Fx.hover_lift}"), md=3),
                Col(Card("Hover Scale", cls=f"{Fx.hover_scale}"), md=3),
                Col(Card("Hover Glow", cls=f"{Fx.hover_glow}"), md=3),
                Col(Card("Hover Tilt", cls=f"{Fx.hover_tilt}"), md=3),
            ),
            cls="mb-4 p-4",
        ),
        # Visual Effects
        Card(
            H3("Visual Effects", cls="mb-4"),
            Row(
                Col(Card("Glass Effect", cls=f"{Fx.glass}"), md=3),
                Col(Card("Soft Shadow", cls=f"{Fx.shadow_soft}"), md=3),
                Col(Card("Sharp Shadow", cls=f"{Fx.shadow_sharp}"), md=3),
                Col(Card("Gradient Shift", cls=f"{Fx.gradient_shift}"), md=3),
            ),
            cls="mb-4 p-4",
        ),
        # Loading States
        Card(
            H3("Loading States", cls="mb-4"),
            Row(
                Col(
                    Card(
                        Div(Icon("arrow-repeat"), cls=f"{Fx.spin} fs-1 text-primary"),
                        P("Spin", cls="mt-2"),
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        Div(Icon("circle"), cls=f"{Fx.pulse} fs-1 text-success"),
                        P("Pulse", cls="mt-2"),
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        Div(cls=f"{Fx.shimmer}", style={"width": "100%", "height": "40px"}),
                        P("Shimmer", cls="mt-2"),
                    ),
                    md=4,
                ),
            ),
            cls="mb-4 p-4",
        ),
        # Combining Effects
        Card(
            H3("Combining Effects", cls="mb-4"),
            P("Effects can be combined for more complex animations:", cls="text-muted mb-3"),
            Row(
                Col(
                    Card(
                        "Fade + Lift + Shadow", cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.shadow_soft}"
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        "Slide + Scale + Glow",
                        cls=f"{Fx.slide_up} {Fx.hover_scale} {Fx.hover_glow}",
                    ),
                    md=4,
                ),
                Col(
                    Card("Zoom + Tilt + Glass", cls=f"{Fx.zoom_in} {Fx.hover_tilt} {Fx.glass}"),
                    md=4,
                ),
            ),
            cls="mb-4 p-4",
        ),
        # Speed Modifiers
        Card(
            H3("Speed Modifiers", cls="mb-4"),
            Row(
                Col(Card("Fast (150ms)", cls=f"{Fx.fade_in} {Fx.fast}"), md=4),
                Col(Card("Default (300ms)", cls=f"{Fx.fade_in}"), md=4),
                Col(Card("Slow (500ms)", cls=f"{Fx.fade_in} {Fx.slow}"), md=4),
            ),
            cls="mb-4 p-4",
        ),
        # Delay Modifiers
        Card(
            H3("Delay Modifiers", cls="mb-4"),
            Row(
                Col(Card("No Delay", cls=f"{Fx.fade_in}"), md=3),
                Col(Card("Delay XS", cls=f"{Fx.fade_in} {Fx.delay_xs}"), md=3),
                Col(Card("Delay SM", cls=f"{Fx.fade_in} {Fx.delay_sm}"), md=3),
                Col(Card("Delay MD", cls=f"{Fx.fade_in} {Fx.delay_md}"), md=3),
            ),
            cls="p-4",
        ),
        cls="py-5",
    )


if __name__ == "__main__":
    serve(port=5019)
