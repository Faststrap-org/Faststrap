"""
04_data_display/svg_display.py
Demonstrates: Svg, render_svg, VisuallyHidden, DataTable state helpers

- Svg & render_svg: Safe SVG markup rendering with built-in sanitization
- VisuallyHidden: Accessible screen-reader only elements (.visually-hidden)
- DataTable URL helpers: datatable_page_url, datatable_export_params
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, Span, A, serve
from faststrap import (
    add_bootstrap,
    Container,
    Svg,
    render_svg,
    VisuallyHidden,
    Card,
    Row,
    Col,
    Stack,
    Button,
    Badge,
    datatable_page_url,
    datatable_export_params,
)

app = FastHTML()
add_bootstrap(app, theme="purple-magic", mode="light")

SAMPLE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="80" height="80">
  <circle cx="50" cy="50" r="45" fill="#6f42c1" />
  <polygon points="50,15 61,38 86,41 68,59 72,84 50,72 28,84 32,59 14,41 39,38" fill="#ffc107" />
</svg>"""

RADAR_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100" height="100">
  <circle cx="60" cy="60" r="50" fill="none" stroke="#0dcaf0" stroke-width="2" opacity="0.3"/>
  <circle cx="60" cy="60" r="30" fill="none" stroke="#0dcaf0" stroke-width="2" opacity="0.6"/>
  <circle cx="60" cy="60" r="10" fill="#0dcaf0"/>
  <line x1="60" y1="10" x2="60" y2="110" stroke="#0dcaf0" stroke-width="1" opacity="0.4"/>
  <line x1="10" y1="60" x2="110" y2="60" stroke="#0dcaf0" stroke-width="1" opacity="0.4"/>
</svg>"""


@app.get("/")
def home():
    # Build persistent DataTable pagination URL
    next_page_url = datatable_page_url("/admin/users", page=2, per_page=25, sort="email", direction="desc")
    # Export state dictionary
    export_params = datatable_export_params(sort="created_at", direction="desc", search="alice", include_pagination=True, page=1)

    return Container(
        H1("SVG Rendering & Accessibility", cls="display-5 fw-bold mb-2"),
        P("Secure SVG rendering, screen-reader helpers, and DataTable URL builders.", cls="lead text-muted mb-5"),

        # ── Svg Component ──────────────────────────────────────────────────
        H2("1. Svg Component & render_svg", cls="h4 fw-semibold mb-1"),
        P("Render raw SVG safely with built-in tag and protocol sanitization.", cls="text-muted mb-3"),
        Row(
            Col(
                Card(
                    Div(Svg(SAMPLE_SVG, cls="d-inline-block"), cls="text-center p-3"),
                    header="Svg Component (Star Badge)",
                    cls="h-100",
                ),
                span=12, md=6, cls="mb-4",
            ),
            Col(
                Card(
                    Div(Svg(RADAR_SVG, cls="d-inline-block"), cls="text-center p-3"),
                    header="Svg Component (Radar Scope)",
                    cls="h-100",
                ),
                span=12, md=6, cls="mb-4",
            ),
        ),

        # ── VisuallyHidden ─────────────────────────────────────────────────
        H2("2. VisuallyHidden Helper", cls="h4 fw-semibold mb-1"),
        P("Keeps critical context accessible to screen readers without showing on screen.", cls="text-muted mb-3"),
        Card(
            Stack(
                P(
                    "This button has an icon with hidden accessibility text: ",
                    Button(
                        Span("❤️"),
                        VisuallyHidden("Add to Favorites"),
                        variant="outline-danger",
                        size="sm",
                        cls="ms-2",
                    ),
                ),
                P(
                    "Table status column with accessible label: ",
                    Badge("●", cls="bg-success text-success"),
                    VisuallyHidden("Server Online and Healthy"),
                ),
                gap=3,
            ),
            header="VisuallyHidden for WCAG AA Compliance",
            cls="mb-5",
        ),

        # ── DataTable URL State Helpers ────────────────────────────────────
        H2("3. DataTable URL & Export Builders", cls="h4 fw-semibold mb-1"),
        P("Generate robust query strings for pagination links and export buttons.", cls="text-muted mb-3"),
        Card(
            Stack(
                P(Span("Generated Page URL: ", cls="fw-bold"), A(next_page_url, href=next_page_url, cls="text-break")),
                P(Span("Generated Export Params: ", cls="fw-bold"), Span(str(export_params), cls="badge bg-light text-dark border")),
                gap=2,
            ),
            header="datatable_page_url & datatable_export_params",
            cls="mb-5",
        ),

        cls="my-5",
    )


if __name__ == "__main__":
    serve()
