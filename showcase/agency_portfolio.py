"""Flagship showcase — Vortex Creative Agency Portfolio.

Production-grade agency portfolio for Faststrap:

- Animated hero with CSS grid-line background (no JS)
- Stats strip: Years / Projects / Clients / Awards
- InfiniteScroll project gallery with rich mock UI previews
- Glassmorphism service cards with hover glow
- Team section with initials avatars
- TestimonialSection with star ratings
- Contact form with LoadingButton + toast feedback
- FooterModern with social links
- ThemeToggle, PageMeta
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H5,
    A,
    Br,
    Div,
    FastHTML,
    P,
    Span,
    Style,
    Textarea,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Col,
    Container,
    FooterModern,
    FormGroup,
    Fx,
    Icon,
    Input,
    Navbar,
    PageMeta,
    Row,
    Spinner,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import InfiniteScroll, LoadingButton, toast_response

# ── Theme ──────────────────────────────────────────────────────────────────────
VORTEX_THEME = create_theme(
    primary="#6366F1",
    secondary="#A78BFA",
    success="#10B981",
    danger="#F43F5E",
    warning="#F59E0B",
    dark="#0A0B14",
    light="#F8F9FF",
)

app = FastHTML()
add_bootstrap(app, theme=VORTEX_THEME, font_family="Inter", mode="dark")

# ── Data ───────────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "Nebula Dashboard",
        "category": "Web App",
        "desc": "Real-time analytics with 3D data visualization.",
        "color": "#6366F1",
        "tag": "React · Python · FastHTML",
    },
    {
        "title": "Pulse Fitness",
        "category": "Mobile",
        "desc": "AI-powered fitness tracker with gamified workouts.",
        "color": "#EC4899",
        "tag": "React Native · FastAPI",
    },
    {
        "title": "Verdant Farms",
        "category": "Branding",
        "desc": "Complete identity system for organic farm-to-table.",
        "color": "#10B981",
        "tag": "Figma · Illustrator",
    },
    {
        "title": "Aurora Finance",
        "category": "Web App",
        "desc": "Personal finance dashboard with goal tracking.",
        "color": "#F59E0B",
        "tag": "Faststrap · Chart.js",
    },
    {
        "title": "Cipher Security",
        "category": "Web App",
        "desc": "Enterprise password manager, zero-knowledge arch.",
        "color": "#F43F5E",
        "tag": "Python · WASM",
    },
    {
        "title": "Bloom Studio",
        "category": "Branding",
        "desc": "Brand identity for boutique floral design studio.",
        "color": "#8B5CF6",
        "tag": "Figma · After Effects",
    },
]

MORE_PROJECTS = [
    {
        "title": "Horizon Travel",
        "category": "Web App",
        "desc": "AI-powered travel booking and itinerary planning.",
        "color": "#06B6D4",
        "tag": "FastHTML · GPT-4",
    },
    {
        "title": "Muse Gallery",
        "category": "Branding",
        "desc": "Contemporary art gallery identity and exhibition.",
        "color": "#A855F7",
        "tag": "Figma · Motion",
    },
    {
        "title": "Quantum Labs",
        "category": "Web App",
        "desc": "Research collaboration for quantum computing.",
        "color": "#14B8A6",
        "tag": "Python · WebGL",
    },
]

SERVICES = [
    {
        "icon": "palette-fill",
        "title": "Brand Identity",
        "desc": "Logos, color systems, guidelines, and motion identity.",
        "color": "#6366F1",
    },
    {
        "icon": "phone-fill",
        "title": "Product Design",
        "desc": "Mobile and web apps that delight — from wireframe to ship.",
        "color": "#EC4899",
    },
    {
        "icon": "code-slash",
        "title": "Development",
        "desc": "Full-stack engineering — FastHTML, FastAPI, React, WASM.",
        "color": "#10B981",
    },
    {
        "icon": "megaphone-fill",
        "title": "Growth",
        "desc": "SEO, performance marketing, and data-driven strategy.",
        "color": "#F59E0B",
    },
]

TEAM = [
    {"name": "Luna Park", "role": "Creative Director", "initial": "LP", "color": "#6366F1"},
    {"name": "Kai Zhang", "role": "Lead Engineer", "initial": "KZ", "color": "#10B981"},
    {"name": "Maya Singh", "role": "UX / Product", "initial": "MS", "color": "#EC4899"},
    {"name": "Jago Okoye", "role": "Brand Strategist", "initial": "JO", "color": "#F59E0B"},
]

STATS = [
    ("12+", "Years Studio"),
    ("140+", "Projects Shipped"),
    ("98%", "Client Satisfaction"),
    ("24/7", "Support SLA"),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
/* ════════════════════════════════════════════════════════════
   Vortex Agency · Cinematic CSS
   Dark-first with indigo accent. Atmospheric only.
   ════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

body {
  font-family: 'Inter', system-ui, sans-serif;
  background: #0A0B14;
  color: #E5E7EB;
}

/* ── Animated hero grid ─────────────────────────────────────── */
@keyframes vx-grid-drift {
  from { background-position: 0 0; }
  to   { background-position: 60px 60px; }
}

.vx-hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  background:
    linear-gradient(180deg, rgba(10,11,20,0) 0%, rgba(10,11,20,1) 100%),
    linear-gradient(135deg, #0c0d1a 0%, #12133a 50%, #0c1424 100%);
  overflow: hidden;
}

.vx-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(99,102,241,0.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(99,102,241,0.07) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: vx-grid-drift 12s linear infinite;
}

.vx-hero::after {
  content: "";
  position: absolute;
  top: -20%;
  left: 50%;
  transform: translateX(-50%);
  width: 700px;
  height: 700px;
  background: radial-gradient(circle, rgba(99,102,241,0.18) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.vx-hero-content { position: relative; z-index: 1; }

/* ── Hero text gradient ─────────────────────────────────────── */
@keyframes vx-shimmer {
  0%   { background-position: -400px 0; }
  100% { background-position: 400px 0; }
}

.vx-gradient-text {
  background: linear-gradient(90deg, #818CF8, #C084FC, #60A5FA, #818CF8);
  background-size: 400px 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: vx-shimmer 4s linear infinite;
}

/* ── Stats strip ────────────────────────────────────────────── */
.vx-stats-strip {
  background: rgba(99,102,241,0.06);
  border-top: 1px solid rgba(99,102,241,0.15);
  border-bottom: 1px solid rgba(99,102,241,0.15);
  padding: 2.5rem 0;
}

.vx-stat-value {
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg, #818CF8, #C084FC);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}

.vx-stat-label {
  font-size: 0.82rem;
  color: #6B7280;
  font-weight: 500;
  margin-top: 0.25rem;
  letter-spacing: 0.02em;
}

/* ── Section labels ─────────────────────────────────────────── */
.vx-section-overline {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #6366F1;
  margin-bottom: 0.75rem;
  display: block;
}

/* ── Service cards ──────────────────────────────────────────── */
.vx-service-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 2rem 1.5rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  height: 100%;
}

.vx-service-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 60px rgba(99,102,241,0.15);
  border-color: rgba(99,102,241,0.35);
}

.vx-service-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  margin-bottom: 1.25rem;
}

/* ── Project cards ──────────────────────────────────────────── */
.vx-project-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
}

.vx-project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 64px rgba(0,0,0,0.4);
}

.vx-project-preview {
  height: 200px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* Mock UI lines inside project preview */
.vx-mock-line {
  height: 6px;
  border-radius: 3px;
  opacity: 0.4;
  margin: 4px 0;
}

.vx-mock-block {
  height: 40px;
  border-radius: 8px;
  opacity: 0.2;
  margin-bottom: 8px;
}

.vx-project-body { padding: 1.25rem 1.5rem 1.5rem; }

/* ── Team cards ─────────────────────────────────────────────── */
.vx-team-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 2rem 1rem;
  text-align: center;
  transition: transform 0.25s ease;
}

.vx-team-card:hover { transform: translateY(-4px); }

.vx-team-avatar {
  width: 5rem;
  height: 5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.4rem;
  margin: 0 auto 1rem;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

/* ── Sections ───────────────────────────────────────────────── */
.vx-section { padding: 6rem 0; }
.vx-section-dark { background: #0A0B14; }
.vx-section-mid  { background: #0D0E1C; }
"""


def vx_mock_ui(color: str) -> Any:
    """Generate a mock UI preview inside a project card using pure CSS divs."""
    return Div(
        # Simulated browser chrome
        Div(
            Div(
                cls="vx-mock-block w-100",
                style=f"background:{color};height:28px;opacity:0.5;border-radius:4px 4px 0 0;",
            ),
            # Mock content rows
            Div(cls="vx-mock-line w-75", style=f"background:{color};"),
            Div(cls="vx-mock-line w-50", style=f"background:{color};"),
            Div(cls="vx-mock-block", style=f"background:{color};width:100%;opacity:0.08;"),
            Div(cls="vx-mock-line w-100", style=f"background:{color};opacity:0.35;"),
            Div(cls="vx-mock-line w-65", style=f"background:{color};opacity:0.25;"),
            # Mock card row
            Div(
                *[
                    Div(
                        cls="vx-mock-block flex-fill mx-1",
                        style=f"background:{color};opacity:0.18;height:30px;",
                    )
                    for _ in range(3)
                ],
                cls="d-flex",
            ),
            style="width:85%;padding:12px;",
        ),
        style="background:linear-gradient(160deg, rgba(0,0,0,0.6), rgba(0,0,0,0.8));width:100%;height:100%;display:flex;align-items:center;justify-content:center;",
    )


def project_card(p: dict, index: int = 0) -> Any:
    return Div(
        # Preview area
        Div(
            vx_mock_ui(p["color"]),
            style=f"background:linear-gradient(135deg, {p['color']}33, {p['color']}11);",
            cls="vx-project-preview",
        ),
        # Body
        Div(
            Div(
                Badge(
                    p["category"],
                    variant="light",
                    pill=True,
                    cls="text-white-50 border border-white border-opacity-10 mb-2",
                ),
                cls="mb-2",
            ),
            H5(p["title"], cls="text-white fw-700 mb-1", style="font-size:1.05rem;"),
            P(p["desc"], cls="text-white-50 small mb-2", style="line-height:1.5;"),
            Span(p["tag"], cls="text-white-25 small", style="font-size:0.72rem;opacity:0.45;"),
            cls="vx-project-body",
        ),
        cls="vx-project-card",
        style=f"animation-delay:{index * 80}ms;",
    )


@app.get("/")
def home() -> Any:
    return Div(
        Style(CSS),
        PageMeta(
            title="Vortex Agency — Crafting Digital Experiences",
            description="Award-winning creative agency specializing in brand identity, web apps, and growth strategy. Built with Faststrap.",
        ),
        # ── Navigation ─────────────────────────────────────────────
        Navbar(
            brand=Div(
                Icon("grid-fill", cls="me-2 text-primary"),
                Span("VORTEX", cls="fw-800 text-white", style="letter-spacing:0.04em;"),
            ),
            items=[
                {"text": "Work", "href": "#work"},
                {"text": "Services", "href": "#services"},
                {"text": "Team", "href": "#team"},
                {"text": "Contact", "href": "#contact"},
            ],
            variant="dark",
            expand="lg",
            sticky="top",
            cls="border-bottom",
            style="background:rgba(10,11,20,0.85)!important;backdrop-filter:blur(16px);border-color:rgba(255,255,255,0.06)!important;",
        ),
        # ── Hero ────────────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Badge(
                        Icon("award-fill", cls="me-1"),
                        "Award-Winning Agency · Est. 2012",
                        variant="light",
                        pill=True,
                        cls=f"mb-4 text-white bg-white bg-opacity-10 border border-white border-opacity-10 {Fx.fade_in}",
                    ),
                    H1(
                        "We craft digital",
                        Br(),
                        Span("experiences", cls="vx-gradient-text"),
                        " that matter.",
                        cls=f"display-2 fw-black text-white mb-4 {Fx.slide_up}",
                        style="font-weight:900;letter-spacing:-0.03em;line-height:1.05;",
                    ),
                    P(
                        "Vortex is an independent creative studio building brands, products, "
                        "and digital experiences that leave a mark. We work with founders, "
                        "scale-ups, and enterprises.",
                        cls=f"lead text-white-50 mb-5 {Fx.slide_up} {Fx.delay_sm}",
                        style="max-width:560px;",
                    ),
                    Div(
                        A(
                            Icon("arrow-right-circle-fill", cls="me-2"),
                            "View Our Work",
                            href="#work",
                            cls=f"btn btn-primary btn-lg me-3 fw-600 {Fx.fade_in} {Fx.delay_md}",
                            style="border-radius:50px;",
                        ),
                        A(
                            Icon("envelope-fill", cls="me-2"),
                            "Let's Talk",
                            href="#contact",
                            cls=f"btn btn-outline-light btn-lg fw-600 {Fx.fade_in} {Fx.delay_lg}",
                            style="border-radius:50px;",
                        ),
                        cls="d-flex flex-wrap gap-2",
                    ),
                    cls="vx-hero-content py-5",
                ),
            ),
            cls="vx-hero",
        ),
        # ── Stats Strip ─────────────────────────────────────────────
        Div(
            Container(
                Row(
                    *[
                        Col(
                            Div(
                                Div(val, cls="vx-stat-value"),
                                Div(label, cls="vx-stat-label"),
                            ),
                            cls="text-center mb-3",
                            cols=6,
                            md=3,
                        )
                        for val, label in STATS
                    ],
                    cols=2,
                    cols_md=3,
                ),
            ),
            cls="vx-stats-strip",
        ),
        # ── Services ────────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Span("What We Do", cls="vx-section-overline text-center d-block"),
                    H2(
                        "Services that scale\nwith you.",
                        cls="text-center text-white fw-800 mb-2",
                        style="letter-spacing:-0.03em;",
                    ),
                    P(
                        "From zero to launch and beyond — we cover the full stack of digital growth.",
                        cls="text-center text-white-50 mb-5",
                    ),
                    cls="mb-2",
                ),
                Row(
                    *[
                        Col(
                            Div(
                                Div(
                                    Icon(s["icon"]),
                                    cls="vx-service-icon",
                                    style=f"background:{s['color']}22;color:{s['color']};",
                                ),
                                H5(s["title"], cls="text-white fw-700 mb-2"),
                                P(s["desc"], cls="text-white-50 small mb-0"),
                                cls="vx-service-card",
                                style=f"animation-delay:{i*80}ms;",
                            ),
                            cols=12,
                            md=6,
                            lg=3,
                            cls=f"mb-4 {Fx.fade_in}",
                        )
                        for i, s in enumerate(SERVICES)
                    ],
                    cols=2,
                    cols_md=3,
                ),
            ),
            id="services",
            cls="vx-section vx-section-mid",
        ),
        # ── Portfolio ────────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Span("Selected Work", cls="vx-section-overline text-center d-block"),
                    H2(
                        "Projects we're proud of.",
                        cls="text-center text-white fw-800 mb-2",
                        style="letter-spacing:-0.03em;",
                    ),
                    P(
                        "Scroll down for more — our portfolio grows every month.",
                        cls="text-center text-white-50 mb-5",
                    ),
                ),
                Div(
                    Row(
                        *[
                            Col(
                                project_card(p, i),
                                cols=12,
                                md=6,
                                lg=4,
                                cls=f"mb-4 {Fx.fade_in}",
                            )
                            for i, p in enumerate(PROJECTS)
                        ],
                        cols=1,
                        cols_md=2,
                        cols_lg=3,
                    ),
                    InfiniteScroll(
                        endpoint="/api/more-projects?page=2",
                        target="#portfolio-grid",
                        content=Div(
                            Spinner(cls="text-primary"),
                            cls="text-center py-4",
                        ),
                    ),
                    id="portfolio-grid",
                ),
            ),
            id="work",
            cls="vx-section vx-section-dark",
        ),
        # ── Team ────────────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Span("The People", cls="vx-section-overline text-center d-block"),
                    H2(
                        "Meet the studio.",
                        cls="text-center text-white fw-800 mb-5",
                        style="letter-spacing:-0.03em;",
                    ),
                ),
                Row(
                    *[
                        Col(
                            Div(
                                Div(
                                    t["initial"],
                                    cls="vx-team-avatar text-white",
                                    style=f"background:linear-gradient(135deg,{t['color']},{t['color']}99);",
                                ),
                                H5(
                                    t["name"],
                                    cls="text-white fw-700 mb-1",
                                    style="font-size:0.95rem;",
                                ),
                                P(
                                    t["role"],
                                    cls="small mb-0",
                                    style=f"color:{t['color']};font-weight:500;",
                                ),
                                cls="vx-team-card",
                            ),
                            cols=6,
                            lg=3,
                            cls=f"mb-4 {Fx.fade_in}",
                        )
                        for t in TEAM
                    ],
                    cols=2,
                    cols_md=3,
                ),
            ),
            id="team",
            cls="vx-section vx-section-mid",
        ),
        # ── Testimonials ─────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Span("Client Love", cls="vx-section-overline text-center d-block"),
                    H2(
                        "What our clients say.",
                        cls="text-center text-white fw-800 mb-5",
                        style="letter-spacing:-0.03em;",
                    ),
                ),
                TestimonialSection(
                    Testimonial(
                        quote="Vortex completely transformed our brand. The attention to detail, the speed of execution, and the quality of the final product were all exceptional.",
                        author="Emma Larsson",
                        role="CEO, Verdant Farms",
                        rating=5,
                    ),
                    Testimonial(
                        quote="Our dashboard went from functional to extraordinary. Our users noticed immediately. NPS went from 42 to 71 after launch.",
                        author="Raj Patel",
                        role="Product Lead, Nebula Inc.",
                        rating=5,
                    ),
                    columns=2,
                ),
            ),
            cls="vx-section vx-section-dark",
        ),
        # ── Contact ──────────────────────────────────────────────────
        Div(
            Container(
                Row(
                    Col(
                        Span("Let's create together", cls="vx-section-overline"),
                        H2(
                            "Got a project in mind?",
                            cls="text-white fw-800 mb-3",
                            style="letter-spacing:-0.03em;",
                        ),
                        P(
                            "We typically reply within 4 hours on weekdays.",
                            cls="text-white-50 mb-4",
                        ),
                        Div(
                            Div(
                                Icon("envelope-fill", cls="me-3 text-primary"),
                                Span("hello@vortex.agency", cls="text-white"),
                                cls="d-flex align-items-center mb-3",
                            ),
                            Div(
                                Icon("geo-alt-fill", cls="me-3 text-primary"),
                                Span("Lagos, Nigeria · Remote Worldwide", cls="text-white-50"),
                                cls="d-flex align-items-center mb-3",
                            ),
                            Div(
                                Icon("clock-fill", cls="me-3 text-primary"),
                                Span("Mon – Fri, 9 AM – 6 PM WAT", cls="text-white-50"),
                                cls="d-flex align-items-center",
                            ),
                        ),
                        cols=12,
                        md=5,
                        cls="mb-4 mb-md-0",
                    ),
                    Col(
                        Div(
                            FormGroup(
                                Input(
                                    name="name",
                                    placeholder="Your name",
                                    cls="border-0",
                                    style="background:rgba(255,255,255,0.05);color:#fff;",
                                ),
                                label="Name",
                                cls="text-white-50",
                            ),
                            FormGroup(
                                Input(
                                    "email",
                                    input_type="email",
                                    placeholder="your@email.com",
                                    cls="border-0",
                                    style="background:rgba(255,255,255,0.05);color:#fff;",
                                ),
                                label="Email",
                                cls="text-white-50",
                            ),
                            FormGroup(
                                Input(
                                    name="budget",
                                    placeholder="e.g. $5,000 – $15,000",
                                    cls="border-0",
                                    style="background:rgba(255,255,255,0.05);color:#fff;",
                                ),
                                label="Estimated Budget",
                                cls="text-white-50",
                            ),
                            FormGroup(
                                Textarea(
                                    name="message",
                                    placeholder="Tell us about your project...",
                                    rows=4,
                                    cls="border-0 w-100",
                                    style="background:rgba(255,255,255,0.05);color:#fff;resize:none;",
                                ),
                                label="Message",
                                cls="text-white-50",
                            ),
                            LoadingButton(
                                Icon("send-fill", cls="me-2"),
                                "Send Message",
                                endpoint="/api/contact",
                                target="#contact-result",
                                variant="primary",
                                cls="w-100 fw-600",
                                style="border-radius:50px;",
                            ),
                            Div(id="contact-result", cls="mt-3"),
                            cls="p-4 rounded-4",
                            style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);",
                        ),
                        cols=12,
                        md=7,
                    ),
                    cols=1,
                    cols_md=2,
                ),
            ),
            id="contact",
            cls="vx-section vx-section-mid",
        ),
        # ── Footer ───────────────────────────────────────────────────
        FooterModern(
            brand=Div(
                Icon("grid-fill", cls="me-2"),
                Span("VORTEX"),
            ),
            tagline="Crafting digital experiences since 2012.",
            columns=[
                {
                    "title": "Studio",
                    "links": [
                        {"text": "About", "href": "#"},
                        {"text": "Work", "href": "#work"},
                        {"text": "Services", "href": "#services"},
                        {"text": "Team", "href": "#team"},
                    ],
                },
                {
                    "title": "Connect",
                    "links": [
                        {"text": "Contact", "href": "#contact"},
                        {"text": "Careers", "href": "#"},
                        {"text": "Blog", "href": "#"},
                        {"text": "Press", "href": "#"},
                    ],
                },
            ],
            social_links=[
                {"icon": "instagram", "href": "#"},
                {"icon": "dribbble", "href": "#"},
                {"icon": "linkedin", "href": "#"},
                {"icon": "twitter-x", "href": "#"},
            ],
            copyright_text="© 2026 Vortex Studio. All rights reserved.",
            bg_variant="dark",
            text_variant="light",
        ),
        ToastContainer(position="top-end"),
    )


# ── API ─────────────────────────────────────────────────────────────────────────


@app.get("/api/more-projects")
def more_projects(page: int = 2) -> Any:
    import time

    time.sleep(0.4)
    items = [
        Col(project_card(p, i), cols=12, md=6, lg=4, cls=f"mb-4 {Fx.fade_in}")
        for i, p in enumerate(MORE_PROJECTS)
    ]
    result = Row(*items, cols=1, cols_md=2, cols_lg=3)
    if page < 3:
        return Div(
            result,
            InfiniteScroll(
                endpoint=f"/api/more-projects?page={page + 1}",
                target="#portfolio-grid",
                content=Div(Spinner(cls="text-primary"), cls="text-center py-4"),
            ),
        )
    return Div(
        result,
        P(
            Icon("check-circle-fill", cls="me-2 text-success"),
            "You've seen all our work.",
            cls="text-center text-white-50 py-4",
        ),
    )


@app.post("/api/contact")
def contact() -> Any:
    return toast_response(
        content=Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Message sent! We'll respond within 4 hours.",
            variant="success",
        ),
        message="Thanks for reaching out!",
        variant="success",
    )


if __name__ == "__main__":
    serve(port=5005)
