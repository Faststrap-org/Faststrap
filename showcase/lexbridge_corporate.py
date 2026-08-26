"""Flagship showcase — Lexbridge Corporate.

Production-grade law / consulting firm website for Faststrap:

- Cormorant Garamond display font + Inter body
- Slate/gold professional light-mode palette
- Atmospheric hero with radial gradient overlay
- Raw Nav() navbar for reliable Bootstrap 5 collapse
- Accordion for practice areas / FAQs
- Row(cols=1, cols_md=N, cols_lg=N) responsive grids throughout
- Trust indicators: stat banner, team cards, client logos
- Fx entrance + hover animations on every section
- Port 5017
"""

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H3,
    H4,
    A,
    Br,
    Button,
    Div,
    FastHTML,
    Img,
    Nav,
    P,
    Span,
    Style,
    serve,
)

from faststrap import (
    Accordion,
    AccordionItem,
    Badge,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    Row,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
    create_theme,
)

# ── Theme ────────────────────────────────────────────────────────────────────

LB_THEME = create_theme(
    primary="#1B2B4B",  # deep navy
    secondary="#C9A84C",  # antique gold
    success="#2D6A4F",
    danger="#A63D2F",
    warning="#C9A84C",
    info="#4A6FA5",
)

app = FastHTML()
add_bootstrap(app, font_family="Inter", theme=LB_THEME, mode="light")

# ── CSS ──────────────────────────────────────────────────────────────────────

LB_CSS = Style("""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&display=swap');

/* ── Page shell ─────────────────────────────────────── */
.lb-shell {
  background: #f9f8f5;
  color: #1B2B4B;
  min-height: 100vh;
}

/* ── Navbar ─────────────────────────────────────────── */
.lb-nav {
  background: rgba(249,248,245,0.96) !important;
  backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(27,43,75,0.10);
}
.lb-brand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1B2B4B !important;
  letter-spacing: 0.04em;
}
.lb-brand span { color: #C9A84C; }
.lb-nav .nav-link {
  color: rgba(27,43,75,0.72) !important;
  font-weight: 600;
  font-size: 0.88rem;
  letter-spacing: 0.02em;
  border-radius: 999px;
  padding: 0.5rem 0.9rem !important;
  transition: color 0.2s ease, background 0.2s ease;
}
.lb-nav .nav-link:hover { color: #1B2B4B !important; background: rgba(201,168,76,0.10); }
.lb-nav-cta {
  background: #1B2B4B !important;
  color: #fff !important;
  border: none;
  border-radius: 50px;
  padding: 0.5rem 1.2rem !important;
  font-weight: 700;
  font-size: 0.85rem;
  transition: background 0.2s ease, transform 0.2s ease;
}
.lb-nav-cta:hover { background: #C9A84C !important; color: #fff !important; transform: translateY(-1px); }

/* ── Hero ───────────────────────────────────────────── */
.lb-hero {
  position: relative;
  overflow: hidden;
  background:
    linear-gradient(135deg, rgba(27,43,75,0.92) 0%, rgba(20,30,55,0.85) 100%),
    url('https://images.unsplash.com/photo-1556761175-4b46a572b786?w=1600') center/cover no-repeat;
  min-height: 88vh;
  display: flex;
  align-items: center;
  padding: 4rem 0;
}
.lb-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 70% 50%, rgba(201,168,76,0.18), transparent 55%);
}
.lb-hero-headline {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2.8rem, 6vw, 5rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -0.01em;
  color: #fff;
}
.lb-gold { color: #C9A84C; }
.lb-gold-line {
  width: 64px; height: 3px;
  background: linear-gradient(90deg, #C9A84C, rgba(201,168,76,0.3));
  border-radius: 999px;
  margin: 1.5rem 0;
}
.lb-hero-tagline {
  font-size: 1.05rem;
  color: rgba(255,255,255,0.72);
  line-height: 1.7;
  max-width: 480px;
}

/* ── Section overline ───────────────────────────────── */
.lb-overline {
  display: block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 0.5rem;
}
.lb-section-heading {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem, 4vw, 2.8rem);
  font-weight: 700;
  color: #1B2B4B;
  line-height: 1.12;
}
.lb-divider {
  width: 40px; height: 2px;
  background: #C9A84C;
  border-radius: 999px;
  margin: 1rem 0 1.5rem;
}

/* ── Stat box ───────────────────────────────────────── */
.lb-stat-box {
  background: #fff;
  border: 1px solid rgba(27,43,75,0.08);
  border-radius: 1rem;
  padding: 1.75rem 1.25rem;
  text-align: center;
  transition: transform 0.22s ease, box-shadow 0.22s ease;
  height: 100%;
}
.lb-stat-box:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 48px rgba(27,43,75,0.10);
}
.lb-stat-val {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3rem;
  font-weight: 700;
  color: #1B2B4B;
  line-height: 1;
}
.lb-stat-label { font-size: 0.82rem; color: #6B7A99; margin-top: 0.25rem; }

/* ── Practice cards ─────────────────────────────────── */
.lb-practice-card {
  background: #fff;
  border: 1px solid rgba(27,43,75,0.07);
  border-radius: 1rem;
  padding: 2rem;
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  height: 100%;
  position: relative;
  overflow: hidden;
}
.lb-practice-card::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, #C9A84C, rgba(201,168,76,0.3));
  border-radius: 1rem 1rem 0 0;
}
.lb-practice-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 50px rgba(27,43,75,0.10);
  border-color: rgba(201,168,76,0.25);
}
.lb-practice-icon {
  width: 3rem; height: 3rem;
  display: flex; align-items: center; justify-content: center;
  border-radius: 0.75rem;
  background: rgba(27,43,75,0.06);
  color: #1B2B4B;
  font-size: 1.3rem;
  margin-bottom: 1rem;
}

/* ── Trust banner ───────────────────────────────────── */
.lb-trust-banner {
  background: #1B2B4B;
  border-radius: 1.5rem;
  padding: 2.5rem 2rem;
}
.lb-trust-item { text-align: center; color: #fff; }
.lb-trust-val {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2.5rem;
  font-weight: 700;
  color: #C9A84C;
  line-height: 1;
}
.lb-trust-lbl { font-size: 0.82rem; color: rgba(255,255,255,0.6); margin-top: 0.3rem; }

/* ── Team card ──────────────────────────────────────── */
.lb-team-card {
  background: #fff;
  border: 1px solid rgba(27,43,75,0.07);
  border-radius: 1rem;
  overflow: hidden;
  transition: transform 0.22s ease, box-shadow 0.22s ease;
  height: 100%;
}
.lb-team-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 50px rgba(27,43,75,0.12);
}
.lb-team-photo {
  width: 100%; height: 240px;
  object-fit: cover;
  object-position: center top;
}
.lb-team-info { padding: 1.25rem; }
.lb-team-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1B2B4B;
}
.lb-team-role { font-size: 0.8rem; color: #C9A84C; font-weight: 600; letter-spacing: 0.04em; }

/* ── Accordion overrides ────────────────────────────── */
.lb-accordion .accordion-item {
  border: 1px solid rgba(27,43,75,0.08);
  border-radius: 0.75rem !important;
  margin-bottom: 0.5rem;
  overflow: hidden;
}
.lb-accordion .accordion-button {
  font-weight: 600;
  color: #1B2B4B;
  background: #fff;
  box-shadow: none;
  font-size: 0.95rem;
}
.lb-accordion .accordion-button:not(.collapsed) {
  color: #C9A84C;
  background: rgba(201,168,76,0.05);
  box-shadow: none;
}
.lb-accordion .accordion-button::after {
  filter: brightness(0) saturate(100%) invert(14%) sepia(72%) saturate(400%) hue-rotate(195deg) brightness(90%);
}

/* ── CTA strip ──────────────────────────────────────── */
.lb-cta {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(201,168,76,0.25), transparent 55%),
    linear-gradient(135deg, #1B2B4B, #0f1e36);
  border-radius: 2rem;
  padding: 4rem 2rem;
  border: 1px solid rgba(201,168,76,0.15);
}

/* ── Client logo strip ──────────────────────────────── */
.lb-logo-strip {
  background: #fff;
  border: 1px solid rgba(27,43,75,0.07);
  border-radius: 1rem;
  padding: 1.5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 2rem 3rem;
}
.lb-client-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: rgba(27,43,75,0.35);
  letter-spacing: 0.04em;
}
""")

# ── Data ─────────────────────────────────────────────────────────────────────

PRACTICES = [
    (
        "briefcase-fill",
        "Corporate Law",
        "Mergers, acquisitions, governance, and commercial agreements for businesses at every stage of growth.",
    ),
    (
        "building",
        "Real Estate",
        "Complex property transactions, development projects, leasing disputes, and title clearance.",
    ),
    (
        "people-fill",
        "Employment Law",
        "Executive contracts, wrongful termination claims, workplace compliance, and restructuring advice.",
    ),
    (
        "safe2-fill",
        "Dispute Resolution",
        "Litigation strategy, arbitration, mediation, and expert representation before superior courts.",
    ),
    (
        "globe-americas",
        "International Trade",
        "Cross-border contracts, customs regulations, sanctions compliance, and trade finance structuring.",
    ),
    (
        "graph-up-arrow",
        "Tax & Regulatory",
        "Corporate tax advisory, regulatory filings, transfer pricing, and government relations counsel.",
    ),
]

STATS = [
    ("35+", "Years of Practice"),
    ("1,200+", "Cases Won"),
    ("98%", "Client Retention"),
    ("6", "Offices Nationwide"),
]

TEAM = [
    (
        "Adaeze Okonkwo, SAN",
        "Managing Partner",
        "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400",
    ),
    (
        "Emeka Nwachukwu",
        "Head of Corporate Law",
        "https://images.unsplash.com/photo-1556761175-b413da4baf72?w=400",
    ),
    (
        "Fatima Al-Hassan",
        "Senior Partner, Disputes",
        "https://images.unsplash.com/photo-1594824476967-48c8b964273f?w=400",
    ),
    (
        "Chukwudi Eze",
        "Partner, Real Estate",
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400",
    ),
]

FAQS = [
    (
        "How do I schedule an initial consultation?",
        "You can use the contact form on this page or call our main office. Initial consultations are offered at a fixed advisory rate with no obligation to proceed.",
    ),
    (
        "Do you handle matters outside Lagos?",
        "Yes. Lexbridge has offices in Lagos, Abuja, Port Harcourt, Ibadan, Kano, and Enugu, and we routinely appear before courts across all states.",
    ),
    (
        "What industries do you specialise in?",
        "We primarily serve financial services, real estate, oil & gas, telecoms, and public-sector clients, though our commercial practice covers most industries.",
    ),
    (
        "How are your fees structured?",
        "Fee structures vary by engagement. We offer fixed fees for standard transactions, retainer arrangements for ongoing advisory needs, and hourly rates for contentious matters.",
    ),
    (
        "Can individuals engage the firm, not just companies?",
        "Absolutely. We represent high-net-worth individuals, executives, and private clients on estate planning, family law, property, and employment matters.",
    ),
]

CLIENTS = [
    "Sterling Capital",
    "Zenith Group",
    "Nnamdi Holdings",
    "PanAfrica RE",
    "Oando PLC",
    "FCMB Advisory",
]

# ── Helpers ───────────────────────────────────────────────────────────────────


def practice_card(icon: str, title: str, desc: str, idx: int = 0) -> Any:
    return Div(
        Div(Icon(icon), cls="lb-practice-icon"),
        H4(
            title,
            cls="fw-700 mb-2",
            style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#1B2B4B;",
        ),
        P(desc, cls="small mb-0", style="color:#6B7A99;line-height:1.65;"),
        cls=f"lb-practice-card {Fx.fade_in}",
        style=f"animation-delay:{idx * 70}ms;",
    )


def stat_box(val: str, label: str, idx: int = 0) -> Any:
    return Div(
        Div(val, cls="lb-stat-val"),
        Div(label, cls="lb-stat-label"),
        cls=f"lb-stat-box {Fx.fade_in}",
        style=f"animation-delay:{idx * 80}ms;",
    )


def team_card(name: str, role: str, photo: str, idx: int = 0) -> Any:
    return Div(
        Img(src=photo, cls="lb-team-photo", alt=name),
        Div(
            Div(name, cls="lb-team-name"),
            Div(role, cls="lb-team-role mt-1"),
            Div(
                A(Icon("linkedin"), href="#", cls="text-muted me-2"),
                A(Icon("envelope"), href="#", cls="text-muted"),
                cls="mt-2",
            ),
            cls="lb-team-info",
        ),
        cls=f"lb-team-card {Fx.fade_in} {Fx.hover_lift}",
        style=f"animation-delay:{idx * 80}ms;",
    )


# ── Route ─────────────────────────────────────────────────────────────────────


@app.get("/")
def home() -> Any:
    return Div(
        LB_CSS,
        # ── Navbar ─────────────────────────────────────────────────────────
        Nav(
            Div(
                A(
                    Span("Lex", cls=""),
                    Span("bridge", cls="lb-gold"),
                    Span(" & Partners"),
                    cls="navbar-brand lb-brand",
                    href="#",
                ),
                Button(
                    Span(cls="navbar-toggler-icon"),
                    cls="navbar-toggler border-0",
                    type="button",
                    data_bs_toggle="collapse",
                    data_bs_target="#lbNavCollapse",
                    aria_controls="lbNavCollapse",
                    aria_expanded="false",
                    aria_label="Toggle navigation",
                ),
                Div(
                    Div(
                        A("Practice Areas", href="#practice", cls="nav-link"),
                        A("Our Team", href="#team", cls="nav-link"),
                        A("About", href="#about", cls="nav-link"),
                        A("FAQ", href="#faq", cls="nav-link"),
                        A("Contact", href="#contact", cls="nav-link lb-nav-cta ms-2"),
                        cls="navbar-nav ms-auto align-items-center gap-1",
                    ),
                    cls="collapse navbar-collapse",
                    id="lbNavCollapse",
                ),
                cls="container",
            ),
            cls="navbar navbar-expand-lg lb-nav position-sticky top-0 z-3",
        ),
        # ── Shell ───────────────────────────────────────────────────────────
        Div(
            # ── Hero ───────────────────────────────────────────────────────
            Div(
                Container(
                    Row(
                        Col(
                            Div(
                                Badge(
                                    Icon("award-fill", cls="me-1 text-warning"),
                                    "Ranked: Top 10 Law Firms · Nigeria 2026",
                                    cls="mb-4 d-inline-flex align-items-center px-3 py-2",
                                    style="background:rgba(201,168,76,0.18);color:#C9A84C;border:1px solid rgba(201,168,76,0.35);border-radius:999px;font-size:0.78rem;font-weight:700;",
                                ),
                                H1(
                                    "Trusted Counsel.",
                                    Br(),
                                    Span("Exceptional", cls="lb-gold"),
                                    " Results.",
                                    cls=f"lb-hero-headline {Fx.slide_up}",
                                ),
                                Div(cls="lb-gold-line"),
                                P(
                                    "For over 35 years, Lexbridge & Partners has delivered strategic legal "
                                    "advice and fearless representation to leading corporations, institutions, "
                                    "and individuals across Nigeria and beyond.",
                                    cls=f"lb-hero-tagline {Fx.fade_in} {Fx.delay_sm}",
                                ),
                                Div(
                                    A(
                                        Icon("calendar-check", cls="me-2"),
                                        "Book a Consultation",
                                        href="#contact",
                                        cls=f"btn btn-warning fw-700 me-3 {Fx.fade_in} {Fx.delay_md}",
                                        style="border-radius:50px;color:#1B2B4B;",
                                    ),
                                    A(
                                        "Our Practice Areas",
                                        href="#practice",
                                        cls=f"btn btn-outline-light fw-600 {Fx.fade_in} {Fx.delay_lg}",
                                        style="border-radius:50px;",
                                    ),
                                    cls="mt-4 d-flex flex-wrap gap-2",
                                ),
                            ),
                            lg=7,
                        ),
                        Col(
                            Div(
                                *[
                                    Div(
                                        Div(val, cls="lb-trust-val"),
                                        Div(label, cls="lb-trust-lbl"),
                                        cls="lb-trust-item",
                                    )
                                    for val, label in STATS
                                ],
                                cls="d-grid gap-3",
                                style="grid-template-columns: 1fr 1fr;",
                            ),
                            lg=5,
                            cls="d-none d-lg-flex align-items-center",
                        ),
                        cls="",
                        cols=1,
                        cols_lg=2,
                    ),
                ),
                cls="lb-hero",
                id="home",
            ),
            (
                Container(
                    cls_=None,
                )
                if False
                else Div(
                    # ── Stats strip (mobile) ────────────────────────────────────
                    Container(
                        Row(
                            *[
                                Col(stat_box(value, label, i), cls="mb-4")
                                for i, (value, label) in enumerate(STATS)
                            ],
                            cls="g-3 d-lg-none mt-4",
                            cols=2,
                            cols_sm=4,
                        ),
                    ),
                    # ── Practice Areas ──────────────────────────────────────────
                    Container(
                        Div(
                            Span("what we do", cls="lb-overline"),
                            H2("Practice Areas", cls="lb-section-heading"),
                            Div(cls="lb-divider"),
                            P(
                                "We bring deep sector knowledge and decades of precedent to every matter.",
                                style="color:#6B7A99;max-width:540px;",
                            ),
                        ),
                        Row(
                            *[
                                Col(practice_card(*p, idx=i), cls="mb-4")
                                for i, p in enumerate(PRACTICES)
                            ],
                            cls="g-3 mt-2",
                            cols=1,
                            cols_md=2,
                            cols_lg=3,
                        ),
                        id="practice",
                        cls="mt-5 pt-4",
                    ),
                    # ── Trust Banner ────────────────────────────────────────────
                    Container(
                        Div(
                            Row(
                                *[
                                    Col(
                                        Div(
                                            Div(val, cls="lb-trust-val"),
                                            Div(label, cls="lb-trust-lbl"),
                                            cls="lb-trust-item",
                                        ),
                                        cls=f"mb-3 {Fx.fade_in}",
                                        style=f"animation-delay:{i*80}ms;",
                                    )
                                    for i, (val, label) in enumerate(STATS)
                                ],
                                cls="g-3 align-items-center text-center",
                                cols=2,
                                cols_md=4,
                            ),
                            cls="lb-trust-banner",
                        ),
                        cls="mt-5",
                    ),
                    # ── Our Team ─────────────────────────────────────────────────
                    Container(
                        Span("meet our counsel", cls="lb-overline"),
                        H2("Our People", cls="lb-section-heading"),
                        Div(cls="lb-divider"),
                        P(
                            "Our partners combine exceptional academic credentials with decades of "
                            "front-line client experience.",
                            cls="mb-4",
                            style="color:#6B7A99;max-width:520px;",
                        ),
                        Row(
                            *[Col(team_card(*m, idx=i), cls="mb-4") for i, m in enumerate(TEAM)],
                            cls="g-4",
                            cols=1,
                            cols_md=2,
                            cols_lg=4,
                        ),
                        id="team",
                        cls="mt-5 pt-4",
                    ),
                    # ── Testimonials ─────────────────────────────────────────────
                    Container(
                        Span("client voices", cls="lb-overline"),
                        H2("What Our Clients Say", cls="lb-section-heading mb-1"),
                        Div(cls="lb-divider"),
                        TestimonialSection(
                            Testimonial(
                                quote="Lexbridge handled our acquisition of a listed company with flawless precision. Their counsel saved us months of regulatory friction and millions in exposure.",
                                author="CEO, Sterling Capital",
                                role="Corporate Client",
                                rating=5,
                            ),
                            Testimonial(
                                quote="The disputes team secured an outcome we thought impossible. Clear strategy, great communication, and they never lost sight of commercial reality.",
                                author="MD, PanAfrica Real Estate",
                                role="Dispute Resolution Client",
                                rating=5,
                            ),
                            Testimonial(
                                quote="We've retained Lexbridge for over 12 years. They feel like an extension of our legal department rather than outside counsel.",
                                author="GC, Oando PLC",
                                role="Long-term Retainer Client",
                                rating=5,
                            ),
                            columns=3,
                        ),
                        id="about",
                        cls="mt-5 pt-4",
                    ),
                    # ── Client Logos ─────────────────────────────────────────────
                    Container(
                        Span("trusted by", cls="lb-overline text-center d-block"),
                        H3(
                            "Our Clients",
                            cls="lb-section-heading text-center mb-3",
                            style="font-size:1.8rem;",
                        ),
                        Div(
                            *[Span(name, cls="lb-client-name") for name in CLIENTS],
                            cls="lb-logo-strip",
                        ),
                        cls="mt-5",
                    ),
                    # ── FAQ ───────────────────────────────────────────────────────
                    Container(
                        Row(
                            Col(
                                Span("frequently asked", cls="lb-overline"),
                                H2("Common Questions", cls="lb-section-heading"),
                                Div(cls="lb-divider"),
                                P(
                                    "Can't find your answer here? Contact our client services team directly.",
                                    style="color:#6B7A99;",
                                ),
                            ),
                            Col(
                                Accordion(
                                    *[
                                        AccordionItem(
                                            question,
                                            answer,
                                            item_id=f"lb-faq-{i}",
                                        )
                                        for i, (question, answer) in enumerate(FAQS)
                                    ],
                                    flush=False,
                                    cls="lb-accordion",
                                ),
                            ),
                            cls="g-5 align-items-start",
                            cols=1,
                            cols_lg=2,
                        ),
                        id="faq",
                        cls="mt-5 pt-4",
                    ),
                    # ── CTA ───────────────────────────────────────────────────────
                    Container(
                        Div(
                            Span(
                                "get in touch",
                                cls="lb-overline text-center d-block",
                                style="color:rgba(201,168,76,0.7);",
                            ),
                            H2(
                                "Ready to Discuss Your Matter?",
                                cls=f"lb-section-heading text-white text-center {Fx.slide_up}",
                                style="font-size:clamp(1.8rem,3.5vw,2.8rem);",
                            ),
                            P(
                                "Our senior partners are available for initial consultations. "
                                "Speak directly with a qualified barrister — no obligation.",
                                cls=f"text-center mb-4 {Fx.fade_in} {Fx.delay_sm}",
                                style="color:rgba(255,255,255,0.6);max-width:520px;margin:0 auto 1.5rem;",
                            ),
                            Div(
                                A(
                                    Icon("telephone-fill", cls="me-2"),
                                    "Call +234 1 234 5678",
                                    href="tel:+2341234567",
                                    cls="btn btn-warning btn-lg fw-700 me-3",
                                    style="border-radius:50px;color:#1B2B4B;",
                                ),
                                A(
                                    Icon("envelope-fill", cls="me-2"),
                                    "Email Us",
                                    href="mailto:enquiries@lexbridge.ng",
                                    cls="btn btn-outline-light btn-lg fw-600",
                                    style="border-radius:50px;",
                                ),
                                cls="text-center",
                            ),
                            cls=f"lb-cta {Fx.fade_in}",
                        ),
                        id="contact",
                        cls="mt-5",
                    ),
                    # ── Footer ────────────────────────────────────────────────────
                    Container(
                        FooterModern(
                            brand="Lexbridge & Partners",
                            tagline="Trusted legal counsel across Nigeria and beyond — since 1989.",
                            columns=[
                                {
                                    "title": "Practice Areas",
                                    "links": [
                                        {"text": "Corporate Law", "href": "#practice"},
                                        {"text": "Real Estate", "href": "#practice"},
                                        {"text": "Employment Law", "href": "#practice"},
                                        {"text": "Dispute Resolution", "href": "#practice"},
                                    ],
                                },
                                {
                                    "title": "Firm",
                                    "links": [
                                        {"text": "Our Team", "href": "#team"},
                                        {"text": "About Us", "href": "#about"},
                                        {"text": "Careers", "href": "#"},
                                        {"text": "Contact", "href": "#contact"},
                                    ],
                                },
                                {
                                    "title": "Offices",
                                    "links": [
                                        {"text": "Lagos (HQ)", "href": "#"},
                                        {"text": "Abuja", "href": "#"},
                                        {"text": "Port Harcourt", "href": "#"},
                                        {"text": "Ibadan", "href": "#"},
                                    ],
                                },
                            ],
                            social_links=[
                                {"icon": "linkedin", "href": "#"},
                                {"icon": "twitter-x", "href": "#"},
                                {"icon": "facebook", "href": "#"},
                            ],
                            copyright_text="© 2026 Lexbridge & Partners. All Rights Reserved. RC: 123456. Not legal advice.",
                            cls="mt-5 rounded-4",
                        ),
                        cls="mt-4 pb-4",
                    ),
                    cls="lb-shell",
                )
            ),
        ),
        ToastContainer(position="top-end"),
    )


if __name__ == "__main__":
    serve(port=5016)
