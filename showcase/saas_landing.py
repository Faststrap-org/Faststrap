"""Flagship showcase — Faststrap Product Landing Page.

Production-grade SaaS marketing page for the Faststrap library itself:

- Syne display font + Inter body
- Electric indigo/sky dual-tone brand palette
- Dark radial-gradient atmospheric background
- Glass navbar (raw Nav() for full Bootstrap 5 collapse control)
- Row(cols=1, cols_md=N, cols_lg=N) responsive grids throughout
- Fx entrance + hover animations on every section
- HTMX ActiveSearch live component search demo
- Premium pricing cards + stat counters
- Port 5016
"""

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H5,
    A,
    Br,
    Button,
    Code,
    Div,
    FastHTML,
    Nav,
    P,
    Pre,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    ListGroup,
    ListGroupItem,
    Row,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import ActiveSearch

# ── Theme ────────────────────────────────────────────────────────────────────

SL_THEME = create_theme(
    primary="#6A6FF5",
    secondary="#4DABF7",
    success="#12B886",
    danger="#FF6B6B",
    warning="#F59F00",
    info="#38BDF8",
)

app = FastHTML()
add_bootstrap(app, font_family="Inter", theme=SL_THEME, mode="dark")

# ── CSS ──────────────────────────────────────────────────────────────────────

SL_CSS = Style("""
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=swap');

/* ── Page shell ────────────────────────────────────── */
.sl-shell {
  background:
    radial-gradient(ellipse at top left,  rgba(106,111,245,0.32) 0%, transparent 38%),
    radial-gradient(ellipse at 96%  6%,   rgba(77,171,247,0.22)  0%, transparent 30%),
    radial-gradient(ellipse at 50% 80%,   rgba(106,111,245,0.10) 0%, transparent 42%),
    linear-gradient(180deg, #07101e 0%, #0b1324 44%, #0f172a 100%);
  min-height: 100vh;
  color: #e2e8f0;
}

/* ── Glass navbar ───────────────────────────────────── */
.sl-nav {
  background: rgba(8,15,30,0.72) !important;
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(106,111,245,0.14);
  padding: 0.6rem 0;
}
.sl-brand {
  font-family: 'Syne', sans-serif;
  font-size: 1.45rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #38bdf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.02em;
}
.sl-nav .nav-link {
  color: rgba(226,232,240,0.72) !important;
  font-weight: 600;
  font-size: 0.92rem;
  border-radius: 999px;
  padding: 0.55rem 1rem !important;
  transition: color 0.18s ease, background 0.18s ease;
}
.sl-nav .nav-link:hover {
  color: #fff !important;
  background: rgba(106,111,245,0.12);
}

/* ── Hero ───────────────────────────────────────────── */
.sl-hero { padding: 5rem 0 4rem; }
.sl-hero-headline {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.8rem, 7vw, 5.2rem);
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -0.04em;
  color: #f0f6ff;
}
.sl-headline-gradient {
  background: linear-gradient(135deg, #a5b4fc 0%, #38bdf8 60%, #a5b4fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.sl-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.38rem 0.9rem;
  border-radius: 999px;
  background: rgba(106,111,245,0.16);
  border: 1px solid rgba(106,111,245,0.28);
  color: #c7d2fe;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}
.sl-code-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
  border: 1px solid rgba(106,111,245,0.22);
  border-radius: 1.25rem;
  backdrop-filter: blur(10px);
  box-shadow: 0 32px 80px rgba(2,6,23,0.42);
  overflow: hidden;
}
.sl-code-card pre {
  margin: 0;
  padding: 1.5rem;
  background: transparent;
  font-size: 0.85rem;
  line-height: 1.7;
  color: #c7d2fe;
}
.sl-code-card .sl-code-bar {
  background: rgba(106,111,245,0.12);
  border-bottom: 1px solid rgba(106,111,245,0.16);
  padding: 0.6rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}
.sl-dot {
  width: 11px; height: 11px;
  border-radius: 50%;
}

/* ── Section heading ────────────────────────────────── */
.sl-section-overline {
  display: block;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #818cf8;
  margin-bottom: 0.6rem;
}

/* ── Feature cards ──────────────────────────────────── */
.sl-feature-card {
  position: relative;
  overflow: hidden;
  padding: 1.75rem;
  border-radius: 1.25rem;
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.07);
  backdrop-filter: blur(10px);
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  height: 100%;
}
.sl-feature-card:hover {
  transform: translateY(-6px);
  border-color: rgba(106,111,245,0.28);
  box-shadow: 0 28px 70px rgba(2,6,23,0.32), 0 0 0 1px rgba(106,111,245,0.12);
}
.sl-feature-card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 3px;
  background: linear-gradient(90deg, rgba(106,111,245,0.9), rgba(77,171,247,0.4));
  border-radius: 1.25rem 1.25rem 0 0;
}
.sl-icon-badge {
  width: 2.8rem; height: 2.8rem;
  display: inline-flex; align-items: center; justify-content: center;
  border-radius: 0.9rem;
  margin-bottom: 1rem;
  font-size: 1.25rem;
}

/* ── Stats banner ───────────────────────────────────── */
.sl-stats-banner {
  background: linear-gradient(135deg, rgba(106,111,245,0.12), rgba(77,171,247,0.08));
  border: 1px solid rgba(106,111,245,0.18);
  border-radius: 1.5rem;
  padding: 2.5rem 2rem;
}
.sl-stat-val {
  font-family: 'Syne', sans-serif;
  font-size: 2.4rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a5b4fc, #38bdf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}
.sl-stat-lbl {
  font-size: 0.82rem;
  color: rgba(148,163,184,0.82);
  margin-top: 0.3rem;
}

/* ── Search demo ────────────────────────────────────── */
.sl-search-shell {
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1.5rem;
  padding: 2rem;
  backdrop-filter: blur(10px);
}

/* ── Pricing cards ──────────────────────────────────── */
.sl-pricing-card {
  position: relative;
  overflow: hidden;
  padding: 2rem;
  border-radius: 1.5rem;
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(12px);
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  height: 100%;
}
.sl-pricing-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 28px 64px rgba(2,6,23,0.32);
}
.sl-pricing-card.featured {
  background: linear-gradient(180deg, rgba(106,111,245,0.22), rgba(77,171,247,0.10));
  border-color: rgba(106,111,245,0.42);
  box-shadow: 0 24px 60px rgba(106,111,245,0.18);
}
.sl-price-amount {
  font-family: 'Syne', sans-serif;
  font-size: 3rem;
  font-weight: 800;
  line-height: 1;
}
.sl-feature-check {
  display: flex;
  align-items: flex-start;
  gap: 0.6rem;
  padding: 0.38rem 0;
  font-size: 0.92rem;
  color: rgba(226,232,240,0.82);
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.sl-feature-check:last-child { border-bottom: none; }

/* ── CTA strip ──────────────────────────────────────── */
.sl-cta {
  background:
    radial-gradient(ellipse at 30% 50%, rgba(106,111,245,0.32), transparent 55%),
    radial-gradient(ellipse at 75% 60%, rgba(77,171,247,0.24), transparent 45%),
    linear-gradient(135deg, #0f172a, #1e1b4b);
  border-radius: 2rem;
  padding: 4rem 2rem;
  border: 1px solid rgba(106,111,245,0.22);
}
.sl-cta-code {
  display: inline-block;
  background: rgba(0,0,0,0.42);
  border: 1px solid rgba(106,111,245,0.28);
  border-radius: 0.75rem;
  padding: 0.75rem 1.5rem;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 1rem;
  color: #a5b4fc;
  letter-spacing: 0.02em;
}
""")

# ── Data ─────────────────────────────────────────────────────────────────────

FEATURES = [
    (
        "lightning-charge-fill",
        "Blazingly Fast",
        "FastHTML + HTMX delivers near-SPA speed with zero JavaScript bundles. No React, no Webpack, no overhead.",
        "#6A6FF5",
        "rgba(106,111,245,0.16)",
    ),
    (
        "shield-check-fill",
        "Secure by Default",
        "Session auth, CSRF tokens, and `@require_auth` out of the box. No token headaches or JWT juggling.",
        "#12B886",
        "rgba(18,184,134,0.16)",
    ),
    (
        "code-slash",
        "Pure Python",
        "Write your entire UI, logic, and layout in one language. No JSX, no templates, no mental context switching.",
        "#F59F00",
        "rgba(245,159,0,0.16)",
    ),
    (
        "palette-fill",
        "Beautiful Themes",
        "Bootstrap 5.3 with dark mode, full custom palettes, brand themes, and CSS effects like glassmorphism.",
        "#FF6B6B",
        "rgba(255,107,107,0.16)",
    ),
    (
        "search",
        "Live Search",
        "`ActiveSearch` with debounce replaces complex React search components — pure HTMX, no client code.",
        "#38BDF8",
        "rgba(56,189,248,0.16)",
    ),
    (
        "bar-chart-fill",
        "SEO Ready",
        "Built-in SEO tags, Open Graph, Twitter Cards, and JSON-LD structured data. AI-agent-friendly metadata.",
        "#AB8FF5",
        "rgba(171,143,245,0.16)",
    ),
    (
        "grid-3x3-gap-fill",
        "110+ Components",
        "From grids to glassmorphism. 110 production-ready, themeable Faststrap components — batteries included.",
        "#6A6FF5",
        "rgba(106,111,245,0.16)",
    ),
    (
        "phone",
        "Mobile-First",
        "Every component built responsive-first. Bootstrap grid + Faststrap presets handle all viewport sizes cleanly.",
        "#12B886",
        "rgba(18,184,134,0.16)",
    ),
    (
        "plug-fill",
        "HTMX Presets",
        "`LazyLoad`, `AutoRefresh`, `InfiniteScroll`, `LoadingButton`, `OptimisticAction` — no raw HTMX needed.",
        "#F59F00",
        "rgba(245,159,0,0.16)",
    ),
]

STATS = [
    ("110+", "Components"),
    ("250+", "Tests Passing"),
    ("0 KB", "JS Bundle"),
    ("v0.6", "Current Release"),
]

PRICING = [
    {
        "name": "Starter",
        "price": "Free",
        "period": "forever",
        "featured": False,
        "features": [
            "10 core components",
            "Bootstrap 5 grid",
            "Fx animations",
            "Community support",
            "MIT license",
        ],
        "cta": "Get Started Free",
        "cta_cls": "btn btn-outline-primary w-100 fw-600",
    },
    {
        "name": "Pro",
        "price": "$29",
        "period": "/month",
        "featured": True,
        "features": [
            "110+ components",
            "All HTMX presets",
            "Dark/light dual-theme",
            "SEO module",
            "Priority support",
            "Source access",
        ],
        "cta": "Start Pro Trial",
        "cta_cls": "btn btn-primary w-100 fw-700",
    },
    {
        "name": "Enterprise",
        "price": "$99",
        "period": "/month",
        "featured": False,
        "features": [
            "Everything in Pro",
            "Custom components",
            "Dedicated support",
            "SLA guarantee",
            "White-label rights",
        ],
        "cta": "Contact Sales",
        "cta_cls": "btn btn-outline-secondary w-100 fw-600",
    },
]

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
    "OptimisticAction",
    "DataTable",
    "FilterBar",
    "MetricCard",
    "TrendCard",
    "KPICard",
    "SidebarNavbar",
    "GlassNavbar",
    "PricingGroup",
    "FeatureGrid",
    "TestimonialSection",
]

# ── Helpers ───────────────────────────────────────────────────────────────────


def feature_card(icon: str, title: str, desc: str, color: str, bg: str, idx: int = 0) -> Any:
    return Div(
        Div(Icon(icon), cls="sl-icon-badge", style=f"background:{bg};color:{color};"),
        Strong(title, cls="d-block mb-2 fs-6"),
        P(desc, cls="small mb-0", style="color:rgba(148,163,184,0.85);line-height:1.6;"),
        cls=f"sl-feature-card {Fx.fade_in}",
        style=f"animation-delay:{idx * 70}ms;",
    )


def pricing_card(plan: dict, idx: int = 0) -> Any:
    is_featured = plan["featured"]
    return Div(
        (
            Badge(
                "Most Popular",
                cls="mb-3 d-inline-block",
                style="background:rgba(106,111,245,0.9);font-size:0.75rem;border-radius:999px;padding:0.35rem 0.85rem;",
            )
            if is_featured
            else None
        ),
        Div(
            plan["name"],
            cls="fw-700 mb-3",
            style="font-size:1.05rem;color:rgba(226,232,240,0.65);text-transform:uppercase;letter-spacing:0.06em;font-size:0.82rem;",
        ),
        Span(
            plan["price"],
            cls="sl-price-amount",
            style="color:#a5b4fc;" if is_featured else "color:#f0f6ff;",
        ),
        Span(plan["period"], cls="ms-1 small", style="color:rgba(148,163,184,0.6);"),
        Div(
            *[
                Div(
                    Icon(
                        "check2",
                        cls="flex-shrink-0",
                        style=f"color:{'#818cf8' if is_featured else '#12B886'};",
                    ),
                    Span(feat),
                    cls="sl-feature-check",
                )
                for feat in plan["features"]
            ],
            cls="my-4",
        ),
        A(
            plan["cta"],
            href="#",
            cls=plan["cta_cls"],
            style="border-radius:50px;" if "primary" in plan["cta_cls"] else "border-radius:50px;",
        ),
        cls=f"sl-pricing-card {'featured' if is_featured else ''} {Fx.fade_in}",
        style=f"animation-delay:{idx * 120}ms;",
    )


# ── Route ─────────────────────────────────────────────────────────────────────


@app.get("/")
def home() -> Any:
    return Div(
        SL_CSS,
        # ── Navbar ─────────────────────────────────────────────────────────
        Nav(
            Div(
                A(Span("faststrap.", cls="sl-brand"), cls="navbar-brand", href="#"),
                Button(
                    Span(cls="navbar-toggler-icon"),
                    cls="navbar-toggler border-0",
                    type="button",
                    data_bs_toggle="collapse",
                    data_bs_target="#slNavCollapse",
                    aria_controls="slNavCollapse",
                    aria_expanded="false",
                    aria_label="Toggle navigation",
                ),
                Div(
                    Div(
                        A("Features", href="#features", cls="nav-link"),
                        A("Pricing", href="#pricing", cls="nav-link"),
                        A("Demo", href="#demo", cls="nav-link"),
                        A(
                            Icon("github", cls="me-1"),
                            "GitHub",
                            href="https://github.com/Faststrap-org/Faststrap",
                            cls="nav-link",
                            target="_blank",
                        ),
                        A(
                            "Get Started",
                            href="#pricing",
                            cls="btn btn-primary btn-sm ms-2 fw-600",
                            style="border-radius:50px;",
                        ),
                        cls="navbar-nav ms-auto align-items-center gap-1",
                    ),
                    cls="collapse navbar-collapse",
                    id="slNavCollapse",
                ),
                cls="container-xl",
            ),
            cls="navbar navbar-expand-lg navbar-dark sl-nav position-sticky top-0 z-3",
        ),
        # ── Content shell ───────────────────────────────────────────────────
        Div(
            Container(
                # ── Hero ───────────────────────────────────────────────────
                Div(
                    Row(
                        Col(
                            Div(
                                Span(
                                    Icon("lightning-charge-fill", cls="me-1"),
                                    "v0.6 · 110+ Components",
                                    cls="sl-eyebrow",
                                ),
                                H1(
                                    Span("Build\nStunning UIs"),
                                    Br(),
                                    Span("in ", style="color:rgba(240,246,255,0.7);"),
                                    Span("Pure Python", cls="sl-headline-gradient"),
                                    cls=f"sl-hero-headline {Fx.slide_up}",
                                ),
                                P(
                                    "Faststrap brings 110 production-ready Bootstrap 5 components to FastHTML. "
                                    "Real themes, HTMX presets, Fx animations — zero JavaScript required.",
                                    cls=f"mt-3 mb-4 fs-5 {Fx.fade_in} {Fx.delay_sm}",
                                    style="color:rgba(148,163,184,0.88);max-width:500px;line-height:1.65;",
                                ),
                                Div(
                                    A(
                                        Icon("rocket-takeoff-fill", cls="me-2"),
                                        "Get Started Free",
                                        href="#pricing",
                                        cls=f"btn btn-primary btn-lg fw-700 me-3 {Fx.fade_in} {Fx.delay_md}",
                                        style="border-radius:50px;",
                                    ),
                                    A(
                                        Icon("play-circle", cls="me-2"),
                                        "See Live Demo",
                                        href="#demo",
                                        cls=f"btn btn-link text-light fw-600 {Fx.fade_in} {Fx.delay_lg}",
                                    ),
                                    cls="d-flex align-items-center flex-wrap gap-2",
                                ),
                                Div(
                                    Span(
                                        Icon("star-fill", cls="text-warning"),
                                        " 4.9",
                                        cls="me-3 small fw-600",
                                    ),
                                    Span(
                                        Icon("people-fill", cls="text-primary"),
                                        " 2,400+ devs",
                                        cls="me-3 small",
                                    ),
                                    Span(
                                        Icon("download", cls="text-success"),
                                        " pip install faststrap",
                                        cls="small",
                                        style="font-family:monospace;",
                                    ),
                                    cls=f"mt-4 {Fx.fade_in}",
                                    style="color:rgba(148,163,184,0.65);",
                                ),
                            ),
                            lg=6,
                        ),
                        Col(
                            Div(
                                # Window title bar
                                Div(
                                    Span(cls="sl-dot", style="background:#FF5F57;"),
                                    Span(cls="sl-dot", style="background:#FFBD2E;"),
                                    Span(cls="sl-dot", style="background:#28C840;"),
                                    Span(
                                        "main.py",
                                        cls="ms-auto small",
                                        style="color:rgba(148,163,184,0.5);",
                                    ),
                                    cls="sl-code-bar",
                                ),
                                Pre(
                                    Code(
                                        "from faststrap import *\n\n"
                                        "theme = create_theme(\n"
                                        '    primary="#6A6FF5",\n'
                                        '    secondary="#4DABF7",\n'
                                        ")\n\n"
                                        "app = FastHTML()\n"
                                        "add_bootstrap(\n"
                                        "    app,\n"
                                        '    font_family="Inter",\n'
                                        "    theme=theme,\n"
                                        '    mode="dark",\n'
                                        ")\n\n"
                                        '@app.get("/")\n'
                                        "def home():\n"
                                        "    return Container(\n"
                                        "        GlassNavbar(...),\n"
                                        '        Hero("Welcome"),\n'
                                        '        Card("Hello World"),\n'
                                        "    )\n\n"
                                        "serve()",
                                    ),
                                ),
                                cls=f"sl-code-card {Fx.slide_left} {Fx.delay_md}",
                            ),
                            lg=6,
                            cls="d-none d-md-block",
                        ),
                        cls="align-items-center",
                        cols=1,
                        cols_lg=2,
                    ),
                    cls="sl-hero",
                ),
                # ── Stats Banner ────────────────────────────────────────────
                Div(
                    Row(
                        *[
                            Col(
                                Div(
                                    Div(val, cls="sl-stat-val"),
                                    Div(label, cls="sl-stat-lbl"),
                                    cls="text-center",
                                ),
                                cls=f"mb-3 {Fx.fade_in}",
                                style=f"animation-delay:{i*80}ms;",
                            )
                            for i, (val, label) in enumerate(STATS)
                        ],
                        cls="g-4 align-items-center",
                        cols=2,
                        cols_md=4,
                    ),
                    cls="sl-stats-banner mb-5",
                ),
                # ── Features ────────────────────────────────────────────────
                Div(
                    Span("what you get", cls="sl-section-overline text-center d-block"),
                    H2(
                        "Everything You Need",
                        cls="fw-800 text-center mb-1",
                        style="font-family:'Syne',sans-serif;",
                    ),
                    P(
                        "Stop writing boilerplate. Start shipping.",
                        cls="text-center mb-5",
                        style="color:rgba(148,163,184,0.7);",
                    ),
                    Row(
                        *[Col(feature_card(*f, idx=i), cls="mb-4") for i, f in enumerate(FEATURES)],
                        cls="g-3",
                        cols=1,
                        cols_md=2,
                        cols_lg=3,
                    ),
                    id="features",
                    cls="mt-5 mb-5",
                ),
                # ── Live Demo ────────────────────────────────────────────────
                Div(
                    Span("try it now", cls="sl-section-overline text-center d-block"),
                    H2(
                        "ActiveSearch — Live",
                        cls="fw-800 text-center mb-1",
                        style="font-family:'Syne',sans-serif;",
                    ),
                    P(
                        "No JavaScript. Just HTMX + Python.",
                        cls="text-center mb-4",
                        style="color:rgba(148,163,184,0.7);",
                    ),
                    Row(
                        Col(
                            Div(
                                H5(
                                    Icon("search", cls="me-2"),
                                    "Search 40+ Components",
                                    cls="mb-3 fw-600",
                                ),
                                ActiveSearch(
                                    endpoint="/api/search",
                                    target="#sl-search-results",
                                    placeholder="Try 'button', 'card', 'modal', 'chart'...",
                                    debounce=200,
                                ),
                                Div(
                                    P(
                                        "Start typing to search components...",
                                        cls="text-muted small mt-3",
                                    ),
                                    id="sl-search-results",
                                    cls="mt-3",
                                ),
                                cls="sl-search-shell",
                            ),
                            cls="offset-md-2",
                            md=8,
                        ),
                        cols=1,
                    ),
                    id="demo",
                    cls="mb-5",
                ),
                # ── Testimonials ─────────────────────────────────────────────
                Div(
                    Span("loved by developers", cls="sl-section-overline text-center d-block"),
                    H2(
                        "What Devs Are Saying",
                        cls="fw-800 text-center mb-4",
                        style="font-family:'Syne',sans-serif;",
                    ),
                    TestimonialSection(
                        Testimonial(
                            quote="Faststrap is exactly what FastHTML was missing. I shipped my SaaS MVP in a weekend and it looks better than anything I've built before.",
                            author="Sarah Chen",
                            role="Indie Hacker",
                            rating=5,
                        ),
                        Testimonial(
                            quote="The HTMX presets are genius. ActiveSearch, InfiniteScroll, and AutoRefresh with zero JavaScript? It changed how I build UIs.",
                            author="Marcus Rivera",
                            role="Senior Developer, TechCorp",
                            rating=5,
                        ),
                        Testimonial(
                            quote="We migrated from Next.js to FastHTML + Faststrap. Our codebase is 70% smaller, our Lighthouse score is up 30 points, and the team is happier.",
                            author="Priya Patel",
                            role="CTO, StartupXYZ",
                            rating=5,
                        ),
                        columns=3,
                    ),
                    cls="mb-5",
                ),
                # ── Pricing ──────────────────────────────────────────────────
                Div(
                    Span("simple pricing", cls="sl-section-overline text-center d-block"),
                    H2(
                        "Start Free. Scale as You Grow.",
                        cls="fw-800 text-center mb-1",
                        style="font-family:'Syne',sans-serif;",
                    ),
                    P(
                        "No surprises. Cancel anytime.",
                        cls="text-center mb-5",
                        style="color:rgba(148,163,184,0.7);",
                    ),
                    Row(
                        *[Col(pricing_card(p, i), cls="mb-4") for i, p in enumerate(PRICING)],
                        cls="g-4 align-items-stretch",
                        cols=1,
                        cols_md=3,
                    ),
                    id="pricing",
                    cls="mb-5",
                ),
                # ── CTA ─────────────────────────────────────────────────────
                Div(
                    Span("ready?", cls="sl-section-overline text-center d-block"),
                    H2(
                        "Build Something Beautiful",
                        Br(),
                        "in Pure Python Today.",
                        cls=f"fw-800 text-white text-center mb-3 {Fx.slide_up}",
                        style="font-family:'Syne',sans-serif;font-size:clamp(2rem,4vw,3rem);",
                    ),
                    P(
                        "One pip install. One Python file. Production-grade UI.",
                        cls=f"text-center mb-4 {Fx.fade_in} {Fx.delay_sm}",
                        style="color:rgba(165,180,252,0.72);",
                    ),
                    Div(
                        Div("pip install faststrap", cls="sl-cta-code"),
                        cls=f"text-center mb-4 {Fx.fade_in} {Fx.delay_md}",
                    ),
                    Div(
                        A(
                            Icon("book-half", cls="me-2"),
                            "Read the Docs",
                            href="#",
                            cls="btn btn-primary btn-lg fw-700 me-3",
                            style="border-radius:50px;",
                        ),
                        A(
                            Icon("github", cls="me-2"),
                            "Star on GitHub",
                            href="https://github.com/Faststrap-org/Faststrap",
                            cls="btn btn-outline-light btn-lg fw-600",
                            style="border-radius:50px;",
                            target="_blank",
                        ),
                        cls="text-center",
                    ),
                    cls=f"sl-cta mb-5 {Fx.fade_in}",
                ),
                # ── Footer ───────────────────────────────────────────────
                FooterModern(
                    brand="faststrap.",
                    tagline="Beautiful UIs. Pure Python. Zero JavaScript required.",
                    columns=[
                        {
                            "title": "Product",
                            "links": [
                                {"text": "Components", "href": "#features"},
                                {"text": "HTMX Presets", "href": "#features"},
                                {"text": "Fx Effects", "href": "#features"},
                                {"text": "Pricing", "href": "#pricing"},
                            ],
                        },
                        {
                            "title": "Resources",
                            "links": [
                                {"text": "Documentation", "href": "#"},
                                {"text": "Showcase", "href": "#"},
                                {
                                    "text": "GitHub",
                                    "href": "https://github.com/Faststrap-org/Faststrap",
                                },
                                {"text": "Changelog", "href": "#"},
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
                        {"icon": "twitter-x", "href": "#"},
                        {"icon": "discord", "href": "#"},
                    ],
                    copyright_text="© 2026 Faststrap. Open Source under MIT License.",
                    bg_variant="dark",
                    text_variant="light",
                    cls="rounded-4",
                ),
            ),
            cls="sl-shell py-2",
        ),
        ToastContainer(position="top-end"),
    )


# ── API Endpoints ─────────────────────────────────────────────────────────────


@app.get("/api/search")
def search(q: str = "") -> Any:
    if len(q) < 2:
        return ""
    results = [c for c in COMPONENTS if q.lower() in c.lower()]
    if not results:
        return Alert(
            Icon("search", cls="me-2"),
            "No components matched. Try 'button', 'table', or 'modal'.",
            variant="dark",
            cls="border border-secondary",
        )
    return ListGroup(
        *[
            ListGroupItem(
                Div(
                    Icon("box-seam", cls="me-2 text-primary"),
                    Strong(name),
                    cls="d-flex align-items-center",
                ),
                cls=f"{Fx.fade_in}",
                style=f"background:rgba(255,255,255,0.03);border-color:rgba(255,255,255,0.07);animation-delay:{i*40}ms;",
            )
            for i, name in enumerate(results[:10])
        ],
        flush=True,
    )


if __name__ == "__main__":
    serve(port=5004)
