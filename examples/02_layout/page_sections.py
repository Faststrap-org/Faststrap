"""
02_layout/page_sections.py
Demonstrates: PageHeader, SectionHeader, AspectRatio

- PageHeader: top-of-page title area with eyebrow, subtitle, badge, actions
- SectionHeader: section-level heading within a page
- AspectRatio: constrains children to a fixed aspect ratio (16/9, 4/3, 1/1, etc.)
"""

from fasthtml.common import FastHTML, H1, P, Div, Iframe, Img, serve
from faststrap import (
    add_bootstrap,
    Container,
    PageHeader,
    SectionHeader,
    AspectRatio,
    Button,
    Badge,
    Card,
    Row,
    Col,
    Separator,
)

app = FastHTML()
add_bootstrap(app, theme="teal-oasis", mode="light")


@app.get("/")
def home():
    return Container(

        # ── PageHeader ─────────────────────────────────────────────────────
        PageHeader(
            "Analytics Dashboard",
            eyebrow="Q4 2024",
            subtitle="Track your key metrics and business performance in real time.",
            badge=Badge("Live", cls="bg-success"),
            actions=[
                Button("Export CSV", variant="outline-secondary", size="sm"),
                Button("New Report", variant="primary", size="sm"),
            ],
        ),
        Separator(cls="mb-5"),

        # ── SectionHeader sizes ────────────────────────────────────────────
        SectionHeader(
            "Revenue Overview",
            subtitle="Monthly recurring revenue and growth trends",
            size="lg",
            actions=Button("View All", variant="link", size="sm"),
        ),
        Card(P("Revenue chart placeholder"), cls="mb-4 bg-light"),

        SectionHeader(
            "Top Products",
            subtitle="Best-performing items this quarter",
            size="md",
        ),
        Card(P("Products table placeholder"), cls="mb-4 bg-light"),

        SectionHeader("Quick Stats", size="sm"),
        Card(P("Stats placeholder"), cls="mb-5 bg-light"),

        # ── AspectRatio ────────────────────────────────────────────────────
        SectionHeader(
            "AspectRatio — Responsive Containers",
            subtitle="The child fills the ratio box, preventing layout shift.",
            cls="mb-3",
        ),
        Row(
            Col(
                Card(
                    AspectRatio(
                        Img(src="https://picsum.photos/seed/fs1/800/450", cls="w-100 h-100 object-fit-cover rounded"),
                        ratio="16/9",
                    ),
                    header="16:9 — video / hero image",
                ),
                span=12, md=6, cls="mb-3",
            ),
            Col(
                Card(
                    AspectRatio(
                        Img(src="https://picsum.photos/seed/fs2/600/450", cls="w-100 h-100 object-fit-cover rounded"),
                        ratio="4/3",
                    ),
                    header="4:3 — classic photo",
                ),
                span=12, md=3, cls="mb-3",
            ),
            Col(
                Card(
                    AspectRatio(
                        Img(src="https://picsum.photos/seed/fs3/400/400", cls="w-100 h-100 object-fit-cover rounded"),
                        ratio="1/1",
                    ),
                    header="1:1 — square avatar/tile",
                ),
                span=12, md=3, cls="mb-3",
            ),
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
