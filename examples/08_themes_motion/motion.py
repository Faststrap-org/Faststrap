"""
08_themes_motion/motion.py
Demonstrates: Motion, MotionPreset, GsapPreset

Motion: wraps children and applies entrance animations via GSAP.
MotionPreset / GsapPreset: enum-like presets for motion configurations.

Note: Requires GSAP CDN. Call gsap_assets() or add GSAP via add_bootstrap().
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, serve
from faststrap import (
    add_bootstrap,
    Container,
    Motion,
    Card,
    Button,
    Badge,
    Row,
    Col,
    Stack,
    Cluster,
    Icon,
    gsap_assets,
)

app = FastHTML()
add_bootstrap(app, theme="purple-magic", mode="dark")


@app.get("/")
def home():
    # gsap_assets() returns the script tags needed for Motion to work
    return (
        *gsap_assets(),
        Container(
            H1("Motion & GSAP Animations", cls="display-5 fw-bold mb-2"),
            P(
                "Motion wraps any component and applies GSAP entrance animations. "
                "Scroll down to see each section animate in.",
                cls="lead text-muted mb-5",
            ),

            # ── Preset gallery ─────────────────────────────────────────────
            H2("Motion Presets", cls="h4 fw-semibold mb-1"),
            P("preset= controls the entrance animation. delay= staggers elements.", cls="text-muted mb-3"),
            Row(
                *[
                    Col(
                        Motion(
                            Card(
                                Icon("stars", cls="display-5 mb-2 text-primary"),
                                P(preset, cls="fw-semibold mb-0"),
                                P("Entrance animation", cls="text-muted small"),
                                cls="text-center p-3 h-100",
                            ),
                            preset=preset,
                            delay=i * 0.15,
                        ),
                        span=12, sm=6, md=4, lg=3, cls="mb-4",
                    )
                    for i, preset in enumerate(["fade", "fade-up", "fade-down", "slide-left", "slide-right", "pop", "scale"])
                ],
                cls="g-3",
            ),

            # ── Duration & easing ──────────────────────────────────────────
            H2("Duration & Easing", cls="h4 fw-semibold mb-1 mt-3"),
            P("duration= (seconds) and ease= (GSAP easing string) give fine control.", cls="text-muted mb-3"),
            Row(
                Col(
                    Motion(
                        Card(
                            P("duration=0.3, ease=power1.out", cls="fw-mono small"),
                            P("Fast & snappy", cls="text-muted"),
                            cls="p-3",
                        ),
                        preset="fade-up", duration=0.3, ease="power1.out",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
                Col(
                    Motion(
                        Card(
                            P("duration=1.2, ease=elastic.out(1, 0.5)", cls="fw-mono small"),
                            P("Elastic bounce", cls="text-muted"),
                            cls="p-3",
                        ),
                        preset="pop", duration=1.2, ease="elastic.out(1, 0.5)",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
                Col(
                    Motion(
                        Card(
                            P("duration=0.8, ease=back.out(2)", cls="fw-mono small"),
                            P("Overshooting back ease", cls="text-muted"),
                            cls="p-3",
                        ),
                        preset="slide-right", duration=0.8, ease="back.out(2)",
                    ),
                    span=12, md=4, cls="mb-4",
                ),
            ),

            # ── Stagger ────────────────────────────────────────────────────
            H2("Stagger", cls="h4 fw-semibold mb-1 mt-3"),
            P("stagger= sequences multiple children so they animate one after another.", cls="text-muted mb-3"),
            Motion(
                Cluster(
                    *[Badge(f"Item {i+1}", cls="bg-primary fs-6 p-2") for i in range(6)],
                    gap=2,
                ),
                preset="fade-up",
                stagger=0.1,
                cls="mb-5",
            ),

            cls="my-5",
        ),
    )


if __name__ == "__main__":
    serve()
