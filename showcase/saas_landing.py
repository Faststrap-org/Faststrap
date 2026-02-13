"""
Showcase 1 — SaaS Marketing Page
A modern SaaS landing page with scroll-reveal animations, HTMX presets,
and all major Faststrap components. Demonstrates ActiveSearch, LazyLoad,
testimonials, pricing cards, and animated metrics.
"""

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H4,
    H5,
    A,
    Br,
    Code,
    Div,
    FastHTML,
    Li,
    P,
    Pre,
    Small,
    Span,
    Strong,
    Ul,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Card,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    ListGroup,
    ListGroupItem,
    Row,
    StatCard,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
)
from faststrap.presets import ActiveSearch, toast_response

app = FastHTML()
add_bootstrap(app)


# ─── Data ────────────────────────────────────────────────────────────
FEATURES: list[dict[str, Any]] = [
    {
        "icon": "lightning-charge-fill",
        "title": "Blazingly Fast",
        "desc": "FastHTML + HTMX delivers SPA-like speed with zero JavaScript bundles.",
    },
    {
        "icon": "shield-check",
        "title": "Secure by Default",
        "desc": "Session-based auth with @require_auth. No token headaches.",
    },
    {
        "icon": "code-slash",
        "title": "Pure Python",
        "desc": "Write your entire UI in Python. No JSX, no templates, no context switching.",
    },
    {
        "icon": "palette-fill",
        "title": "Beautiful Themes",
        "desc": "Bootstrap 5.3 with dark mode, custom palettes, and CSS effects.",
    },
    {
        "icon": "search",
        "title": "Live Search",
        "desc": "ActiveSearch with debounce — replaces React search components.",
    },
    {
        "icon": "bar-chart-fill",
        "title": "SEO Ready",
        "desc": "Built-in SEO tags, Open Graph, Twitter Cards, and JSON-LD.",
    },
]

PRICING: list[dict[str, Any]] = [
    {
        "name": "Starter",
        "price": "Free",
        "period": "forever",
        "features": [
            "5 components",
            "Community support",
            "Basic themes",
            "MIT license",
        ],
        "variant": "outline-primary",
        "popular": False,
    },
    {
        "name": "Pro",
        "price": "$29",
        "period": "/month",
        "features": [
            "67+ components",
            "Priority support",
            "All themes & effects",
            "HTMX Presets",
            "SEO module",
        ],
        "variant": "primary",
        "popular": True,
    },
    {
        "name": "Enterprise",
        "price": "$99",
        "period": "/month",
        "features": [
            "Everything in Pro",
            "Custom components",
            "Dedicated support",
            "SLA guarantee",
            "Source code access",
        ],
        "variant": "outline-primary",
        "popular": False,
    },
]


def section_heading(title: str, subtitle: str = "", delay: int = 0) -> Any:
    """Reusable animated section heading."""
    delay_cls = f" {Fx.delay_sm}" if delay else ""
    return Div(
        H2(title, cls=f"fw-bold text-center mb-3 {Fx.fade_in}{delay_cls}"),
        (
            P(subtitle, cls=f"text-center text-muted mb-5 {Fx.fade_in} {Fx.delay_sm}")
            if subtitle
            else None
        ),
    )


# ─── Routes ──────────────────────────────────────────────────────────
@app.get("/")
def home() -> Any:
    return Div(
        # ── Hero Section ─────────────────────────────────────────
        Div(
            Container(
                Row(
                    Col(
                        Badge("v0.5.4", variant="info", pill=True, cls=f"mb-3 {Fx.fade_in}"),
                        H1(
                            "Build Stunning UIs",
                            Br(),
                            Span("in Pure Python", cls="text-primary"),
                            cls=f"display-3 fw-bold mb-4 {Fx.slide_up}",
                        ),
                        P(
                            "FastStrap brings 67 production-ready Bootstrap 5 "
                            "components to FastHTML. Zero JavaScript required.",
                            cls=f"lead text-muted mb-4 {Fx.slide_up} {Fx.delay_sm}",
                        ),
                        Div(
                            A(
                                "Get Started Free",
                                href="#pricing",
                                cls=f"btn btn-primary btn-lg me-3 {Fx.fade_in} {Fx.delay_md}",
                            ),
                            A(
                                Icon("github", cls="me-2"),
                                "View on GitHub",
                                href="https://github.com/Faststrap-org/Faststrap",
                                cls=f"btn btn-outline-dark btn-lg {Fx.fade_in} {Fx.delay_lg}",
                                target="_blank",
                            ),
                        ),
                        cols=12,
                        lg=6,
                        cls="d-flex flex-column justify-content-center",
                    ),
                    Col(
                        Card(
                            Pre(
                                Code(
                                    "from faststrap import *\n\n"
                                    '@app.get("/")\n'
                                    "def home():\n"
                                    "    return Container(\n"
                                    '        Hero("Welcome"),\n'
                                    '        Card("Hello World"),\n'
                                    "    )\n\n"
                                    "serve()",
                                    cls="language-python",
                                ),
                                cls="mb-0",
                            ),
                            cls=f"shadow-lg border-0 {Fx.slide_left} {Fx.delay_md}",
                        ),
                        cols=12,
                        lg=6,
                        cls="d-none d-lg-block",
                    ),
                    cls="min-vh-75 align-items-center",
                ),
            ),
            cls="py-5 bg-body-tertiary",
        ),
        # ── Live Search Demo ─────────────────────────────────────
        Div(
            Container(
                section_heading(
                    "Try ActiveSearch — Live",
                    "No JavaScript. Just HTMX + Python.",
                ),
                Row(
                    Col(
                        Card(
                            H5("Search Components", cls="card-title mb-3"),
                            ActiveSearch(
                                endpoint="/api/search",
                                target="#search-results",
                                placeholder="Try typing 'button', 'card', 'modal'...",
                                debounce=200,
                            ),
                            Div(
                                P("Results appear here", cls="text-muted"),
                                id="search-results",
                                cls="mt-3",
                            ),
                            cls=f"{Fx.slide_up} {Fx.hover_lift} {Fx.shadow_soft}",
                        ),
                        cols=12,
                        md=8,
                        offset_md=2,
                    ),
                ),
            ),
            cls="py-5",
        ),
        # ── Features Grid ────────────────────────────────────────
        Div(
            Container(
                section_heading(
                    "Everything You Need",
                    "Stop writing boilerplate. Start shipping.",
                ),
                Row(
                    *[
                        Col(
                            Card(
                                Div(
                                    Icon(f["icon"], size="2rem", cls="text-primary mb-3"),
                                    cls="text-center",
                                ),
                                H5(f["title"], cls="card-title text-center"),
                                P(f["desc"], cls="card-text text-muted text-center"),
                                cls=f"{Fx.fade_in} {Fx.hover_lift} {Fx.shadow_soft}",
                                style=f"animation-delay: {i * 100}ms;",
                            ),
                            cols=12,
                            md=6,
                            lg=4,
                            cls="mb-4",
                        )
                        for i, f in enumerate(FEATURES)
                    ],
                ),
            ),
            cls="py-5 bg-body-tertiary",
        ),
        # ── Stats Section ────────────────────────────────────────
        Div(
            Container(
                Row(
                    Col(
                        StatCard(
                            title="Components",
                            value="67",
                            icon="grid-3x3-gap-fill",
                            trend="+12",
                            trend_label="new in v0.5.4",
                            cls=f"{Fx.slide_up} {Fx.hover_lift}",
                        ),
                        cols=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        StatCard(
                            title="Tests Passing",
                            value="250+",
                            icon="check-circle-fill",
                            cls=f"{Fx.slide_up} {Fx.hover_lift} {Fx.delay_sm}",
                        ),
                        cols=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        StatCard(
                            title="Bundle Size",
                            value="0 KB",
                            icon="feather",
                            cls=f"{Fx.slide_up} {Fx.hover_lift} {Fx.delay_md}",
                        ),
                        cols=12,
                        md=3,
                        cls="mb-4",
                    ),
                    Col(
                        StatCard(
                            title="JavaScript",
                            value="None",
                            icon="emoji-sunglasses",
                            cls=f"{Fx.slide_up} {Fx.hover_lift} {Fx.delay_lg}",
                        ),
                        cols=12,
                        md=3,
                        cls="mb-4",
                    ),
                ),
            ),
            cls="py-5",
        ),
        # ── Testimonials ─────────────────────────────────────────
        Div(
            Container(
                section_heading(
                    "Loved by Developers",
                    "See what the community is saying.",
                ),
                TestimonialSection(
                    Testimonial(
                        quote=(
                            "FastStrap is exactly what FastHTML was missing."
                            " I shipped my SaaS MVP in a weekend."
                        ),
                        author="Sarah Chen",
                        role="Indie Hacker",
                        rating=5,
                    ),
                    Testimonial(
                        quote=(
                            "The HTMX presets are genius. ActiveSearch and"
                            " InfiniteScroll with zero JavaScript? Sign me up."
                        ),
                        author="Marcus Rivera",
                        role="Senior Developer, TechCorp",
                        rating=5,
                    ),
                    Testimonial(
                        quote=(
                            "We migrated from Next.js to FastHTML + FastStrap."
                            " Our codebase is 70% smaller."
                        ),
                        author="Priya Patel",
                        role="CTO, StartupXYZ",
                        rating=5,
                    ),
                    columns=3,
                ),
            ),
            cls="py-5 bg-body-tertiary",
        ),
        # ── Pricing ──────────────────────────────────────────────
        Div(
            Container(
                section_heading(
                    "Simple Pricing",
                    "Start free. Upgrade as you grow.",
                ),
                Row(
                    *[
                        Col(
                            Card(
                                (
                                    Badge("Most Popular", variant="warning", pill=True, cls="mb-2")
                                    if p["popular"]
                                    else None
                                ),
                                H4(p["name"], cls="card-title"),
                                H2(
                                    p["price"],
                                    Small(p["period"], cls="text-muted fs-6"),
                                    cls="mb-4",
                                ),
                                Ul(
                                    *[
                                        Li(
                                            Icon("check-lg", cls="text-success me-2"),
                                            feat,
                                        )
                                        for feat in p["features"]
                                    ],
                                    cls="list-unstyled mb-4",
                                ),
                                A(
                                    "Get Started",
                                    href="#",
                                    cls=f"btn btn-{p['variant']} btn-lg w-100",
                                ),
                                cls=(
                                    f"text-center p-4 h-100 {Fx.fade_in}"
                                    f" {Fx.hover_lift}"
                                    f" {'border-primary shadow-lg' if p['popular'] else Fx.shadow_soft}"
                                ),
                                style=f"animation-delay: {i * 150}ms;",
                            ),
                            cols=12,
                            md=4,
                            cls="mb-4",
                        )
                        for i, p in enumerate(PRICING)
                    ],
                ),
            ),
            cls="py-5",
            id="pricing",
        ),
        # ── CTA Section ──────────────────────────────────────────
        Div(
            Container(
                Div(
                    H2("Ready to Build?", cls=f"text-white mb-3 {Fx.fade_in}"),
                    P(
                        "Install FastStrap and ship your next project in record time.",
                        cls=f"text-white-50 mb-4 {Fx.fade_in} {Fx.delay_sm}",
                    ),
                    Pre(
                        Code("pip install faststrap", cls="text-white"),
                        cls=f"bg-dark bg-opacity-50 p-3 rounded d-inline-block {Fx.fade_in} {Fx.delay_md}",
                    ),
                    cls="text-center py-5",
                ),
            ),
            cls="bg-primary",
        ),
        # ── Footer ───────────────────────────────────────────────
        FooterModern(
            brand="FastStrap",
            tagline="Beautiful UIs. Pure Python. Zero JS.",
            columns=[
                {
                    "title": "Product",
                    "links": [
                        {"text": "Components", "href": "#"},
                        {"text": "HTMX Presets", "href": "#"},
                        {"text": "SEO Module", "href": "#"},
                        {"text": "Effects", "href": "#"},
                    ],
                },
                {
                    "title": "Resources",
                    "links": [
                        {"text": "Documentation", "href": "#"},
                        {"text": "Examples", "href": "#"},
                        {"text": "Showcase", "href": "#"},
                        {"text": "GitHub", "href": "https://github.com/Faststrap-org/Faststrap"},
                    ],
                },
                {
                    "title": "Community",
                    "links": [
                        {"text": "Discord", "href": "#"},
                        {"text": "Twitter", "href": "#"},
                        {"text": "Blog", "href": "#"},
                        {"text": "Contribute", "href": "#"},
                    ],
                },
            ],
            social_links=[
                {"icon": "github", "href": "https://github.com/Faststrap-org/Faststrap"},
                {"icon": "twitter", "href": "#"},
                {"icon": "discord", "href": "#"},
            ],
            copyright_text="© 2026 FastStrap. Open Source under MIT License.",
            bg_variant="dark",
            text_variant="light",
        ),
        # Toast container for demo
        ToastContainer(position="top-end"),
    )


# ─── API Endpoints ───────────────────────────────────────────────────
COMPONENTS: list[str] = [
    "Button",
    "Card",
    "Modal",
    "Navbar",
    "Alert",
    "Badge",
    "Toast",
    "Spinner",
    "Progress",
    "Accordion",
    "Dropdown",
    "Tabs",
    "Breadcrumb",
    "Pagination",
    "Table",
    "ListGroup",
    "Hero",
    "StatCard",
    "EmptyState",
    "ErrorPage",
    "FormGroup",
    "SearchableSelect",
    "ThemeToggle",
    "FooterModern",
    "Testimonial",
    "ActiveSearch",
    "InfiniteScroll",
    "AutoRefresh",
    "LazyLoad",
    "LoadingButton",
]


@app.get("/api/search")
def search(q: str = "") -> Any:
    """Search Faststrap components."""
    if len(q) < 2:
        return ""
    results = [c for c in COMPONENTS if q.lower() in c.lower()]
    if not results:
        return Alert("No components found", variant="info")
    return ListGroup(
        *[
            ListGroupItem(
                Icon("box-seam", cls="me-2 text-primary"),
                Strong(name),
                cls=f"{Fx.fade_in}",
                style=f"animation-delay: {i * 50}ms;",
            )
            for i, name in enumerate(results[:8])
        ],
        flush=True,
    )


@app.post("/api/signup")
def signup() -> Any:
    """Demo signup endpoint."""
    return toast_response(
        content="",
        message="Welcome aboard! Check your email to get started.",
        variant="success",
    )


serve()
