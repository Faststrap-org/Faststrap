"""Generated FastCloud SaaS showcase rescued from the unfinished root test page.

This file is intentionally kept in ``showcase/`` so it can serve as a real
reference app instead of an untracked scratch page at the repository root.
"""

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H3,
    A,
    Div,
    FastHTML,
    Form,
    Main,
    P,
    Section,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Button,
    Container,
    Feature,
    FeatureGrid,
    FooterModern,
    Fx,
    Icon,
    Input,
    NavbarModern,
    PricingGroup,
    PricingTier,
    Testimonial,
    TestimonialSection,
    ThemeToggle,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import hx_refresh, toast_response

THEME_KEY = "fastcloud-theme"

FASTCLOUD_THEME = create_theme(
    primary="#6A6FF5",
    secondary="#111C33",
    success="#12B886",
    danger="#FF6B6B",
    warning="#F59F00",
    info="#4DABF7",
    radius="0.95rem",
    radius_lg="1.4rem",
    surface_bg_light="#ffffff",
    surface_bg_dark="#1c2433",
    surface_muted_bg_light="#f5f7fd",
    surface_muted_bg_dark="#141a27",
    surface_shadow="0 20px 50px rgba(15, 23, 42, 0.12)",
)

APP_CSS = """
.app-shell {
  min-height: 100vh;
  background:
    radial-gradient(circle at 12% 10%, rgba(106, 111, 245, 0.28), transparent 26%),
    radial-gradient(circle at 88% 8%, rgba(77, 171, 247, 0.18), transparent 22%),
    linear-gradient(180deg, #08101f 0%, #0b1324 40%, #f4f7fc 40%, #f4f7fc 100%);
  overflow-x: clip;
}

/* Light mode: coherent light gradient so split design still reads */
.app-shell[data-bs-theme="light"] {
  color: #0f172a;
  background:
    radial-gradient(circle at 12% 10%, rgba(106, 111, 245, 0.14), transparent 26%),
    radial-gradient(circle at 88% 8%, rgba(77, 171, 247, 0.09), transparent 22%),
    linear-gradient(180deg, #eef2ff 0%, #f0f4fe 30%, #f4f7fc 30%, #f4f7fc 100%);
}

/* Light-mode nav: white frosted glass instead of always-dark */
.app-shell[data-bs-theme="light"] .app-nav-wrap {
  background: rgba(250, 251, 255, 0.92);
  border-bottom-color: rgba(106, 111, 245, 0.1);
}
.app-shell[data-bs-theme="light"] .app-navbar .nav-link {
  color: rgba(15, 23, 42, 0.68);
}
.app-shell[data-bs-theme="light"] .app-navbar .nav-link:hover,
.app-shell[data-bs-theme="light"] .app-navbar .nav-link.active {
  color: #4f52d4;
  background: rgba(106, 111, 245, 0.07);
}

.app-shell[data-bs-theme="dark"] {
  background:
    radial-gradient(circle at 12% 10%, rgba(106, 111, 245, 0.3), transparent 24%),
    radial-gradient(circle at 88% 8%, rgba(77, 171, 247, 0.14), transparent 20%),
    linear-gradient(180deg, #08101f 0%, #0b1324 100%);
}

.app-nav-wrap {
  position: sticky;
  top: 0;
  z-index: 30;
  background: rgba(8, 14, 28, 0.82);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(22px) saturate(1.45);
}

.app-navbar {
  background: transparent;
  border: 0;
  box-shadow: none;
  padding-top: 0.8rem;
  padding-bottom: 0.8rem;
}

.app-navbar .nav-link {
  color: rgba(226, 232, 240, 0.76);
  font-size: 0.92rem;
  font-weight: 600;
  padding: 0.45rem 0.85rem !important;
}

.app-navbar .nav-link:hover,
.app-navbar .nav-link.active {
  color: #fff;
  background: rgba(255, 255, 255, 0.08);
}

.hero-section {
  position: relative;
  padding: 5.5rem 0 4.5rem;
}

.hero-copy { max-width: 44rem; }

.hero-kicker {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.42rem 0.82rem;
  border-radius: 999px;
  background: rgba(106, 111, 245, 0.16);
  color: #c7d2fe;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.hero-display {
  font-size: clamp(3rem, 6vw, 5.6rem);
  line-height: 0.94;
  letter-spacing: -0.05em;
  color: #f8fbff;
}

.hero-copy .lead {
  max-width: 42rem;
  color: rgba(226, 232, 240, 0.78);
}

.hero-metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 2rem;
}

.metric-card {
  padding: 1rem 1.1rem;
  border-radius: 1.2rem;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.07);
  box-shadow: 0 22px 48px rgba(15, 23, 42, 0.18);
}

.metric-label {
  display: block;
  font-size: 0.78rem;
  color: rgba(226, 232, 240, 0.62);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.metric-value {
  display: block;
  margin-top: 0.35rem;
  font-size: 1.45rem;
  font-weight: 800;
  color: #fff;
}

.section-surface { padding: 4.5rem 0; }

.surface-panel {
  padding: 1.6rem;
  border-radius: 1.35rem;
  background: rgba(255, 255, 255, 0.88);
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 20px 48px rgba(15, 23, 42, 0.08);
}

.app-shell[data-bs-theme="dark"] .surface-panel,
.app-shell[data-bs-theme="dark"] .feature-shell,
.app-shell[data-bs-theme="dark"] .waitlist-card,
.app-shell[data-bs-theme="dark"] .testimonial-card,
.app-shell[data-bs-theme="dark"] .pricing-group .card,
.app-shell[data-bs-theme="dark"] .footer-modern {
  background: rgba(22, 28, 41, 0.92);
  border-color: rgba(255, 255, 255, 0.08);
  color: #e5edf8;
}

.section-headline { max-width: 42rem; }
.section-headline h2 {
  font-size: clamp(2rem, 4vw, 3.2rem);
  line-height: 1.02;
  letter-spacing: -0.04em;
}
.section-headline p { font-size: 1.06rem; }

.feature-shell {
  height: 100%;
  padding: 1.6rem;
  border-radius: 1.3rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 18px 44px rgba(15, 23, 42, 0.08);
}

.feature-shell .feature-icon {
  width: 3.2rem;
  height: 3.2rem;
  border-radius: 1rem;
  margin-bottom: 1rem;
  font-size: 1.15rem;
  background: linear-gradient(135deg, #6a6ff5, #4dabf7);
  color: white;
}

.feature-shell h3 { font-size: 1.28rem; letter-spacing: -0.03em; }
.feature-shell p  { font-size: 0.98rem; color: #64748b; }

.app-shell[data-bs-theme="dark"] .feature-shell p,
.app-shell[data-bs-theme="dark"] .pricing-group .card .text-muted,
.app-shell[data-bs-theme="dark"] .footer-modern .text-muted,
.app-shell[data-bs-theme="dark"] .testimonial-card .text-muted {
  color: rgba(226, 232, 240, 0.68) !important;
}

.pricing-group .card {
  padding: 1rem;
  border-radius: 1.35rem;
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 18px 44px rgba(15, 23, 42, 0.08);
}

.pricing-group .border-primary {
  box-shadow: 0 28px 64px rgba(106, 111, 245, 0.18);
}

.waitlist-card {
  max-width: 56rem;
  margin-inline: auto;
  padding: 2.2rem;
  border-radius: 1.45rem;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(15, 23, 42, 0.08);
  box-shadow: 0 24px 64px rgba(15, 23, 42, 0.1);
}

.waitlist-card .form-control,
.waitlist-card .form-select {
  min-height: 3.1rem;
  border-radius: 0.95rem;
}

.waitlist-card .btn {
  min-height: 3.1rem;
  font-weight: 700;
}

.testimonial-card { border-radius: 1.35rem; }
.footer-modern    { margin-top: 0 !important; }

@media (max-width: 991.98px) {
  .hero-section { padding-top: 4.5rem; }
}

/* 2-col on tablet, full-stack only on very small phones */
@media (max-width: 767.98px) {
  .hero-metrics { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 479.98px) {
  .hero-metrics { grid-template-columns: 1fr; }
}
"""

FEATURES: list[dict[str, str]] = [
    {
        "icon": "lightning-charge",
        "title": "Instant deploys",
        "description": "Ship a production service in minutes with preview URLs, edge caching, and sensible defaults.",
    },
    {
        "icon": "shield-check",
        "title": "Security by default",
        "description": "SOC2-minded controls, private networking, and encrypted secrets without manual glue code.",
    },
    {
        "icon": "graph-up-arrow",
        "title": "Operational visibility",
        "description": "Monitor throughput, trace incidents, and inspect deploy health from one clean surface.",
    },
    {
        "icon": "globe2",
        "title": "Global edge footprint",
        "description": "Keep latency low with edge delivery and regional compute choices that stay close to customers.",
    },
    {
        "icon": "terminal",
        "title": "Developer-first APIs",
        "description": "Automate infra, teams, and deploys with APIs that feel scriptable instead of ceremonial.",
    },
    {
        "icon": "people",
        "title": "Team workflows",
        "description": "Review environments, incident timelines, and approval flows built for fast-moving product teams.",
    },
]

TIERS = [
    PricingTier(
        "Starter",
        29,
        period="month",
        features=["3 projects", "100GB bandwidth", "Community support", "Core analytics"],
        button_text="Start starter",
        button_href="#waitlist",
    ),
    PricingTier(
        "Growth",
        99,
        period="month",
        features=[
            "Unlimited projects",
            "1TB bandwidth",
            "Priority support",
            "Tracing and deploy insights",
            "Team seats",
        ],
        button_text="Start growth",
        button_href="#waitlist",
        highlighted=True,
    ),
    PricingTier(
        "Enterprise",
        "Custom",
        period="engagement",
        features=[
            "Dedicated infrastructure",
            "Security review",
            "Custom SLA",
            "Migration support",
            "Onboarding workshops",
        ],
        button_text="Talk to sales",
        button_href="#waitlist",
    ),
]

TESTIMONIALS = [
    Testimonial(
        quote="FastCloud gave our platform team a cleaner path from deploy to observability without another fragile front-end stack.",
        author="Sarah Chen",
        role="CTO, RelayGrid",
        rating=5,
        cls=f"testimonial-card {Fx.base} {Fx.fade_in} {Fx.hover_lift}",
    ),
    Testimonial(
        quote="The speed of iteration is the real win. We launched previews, fixed incidents faster, and stopped fighting our tooling.",
        author="Marcus Johnson",
        role="Lead engineer, Northline",
        rating=5,
        cls=f"testimonial-card {Fx.base} {Fx.fade_in} {Fx.delay_sm} {Fx.hover_lift}",
    ),
    Testimonial(
        quote="It feels like infrastructure designed by product-minded engineers. The team finally trusts the deploy workflow.",
        author="Emily Rodriguez",
        role="VP engineering, CloudNine",
        rating=5,
        cls=f"testimonial-card {Fx.base} {Fx.fade_in} {Fx.delay_md} {Fx.hover_lift}",
    ),
]

FOOTER_COLUMNS = [
    {
        "title": "Product",
        "links": [
            {"text": "Features", "href": "#features"},
            {"text": "Pricing", "href": "#pricing"},
            {"text": "Roadmap", "href": "#testimonials"},
        ],
    },
    {
        "title": "Resources",
        "links": [
            {"text": "Docs", "href": "https://faststrap-org.github.io/Faststrap/"},
            {"text": "GitHub", "href": "https://github.com/Faststrap-org/Faststrap"},
        ],
    },
    {
        "title": "Company",
        "links": [
            {"text": "About", "href": "#hero"},
            {"text": "Contact", "href": "#waitlist"},
        ],
    },
]

SOCIAL_LINKS = [
    {"icon": "github", "href": "https://github.com/Faststrap-org/Faststrap"},
    {"icon": "box-arrow-up-right", "href": "https://faststrap-org.github.io/Faststrap/"},
]

app = FastHTML(hdrs=(Style(APP_CSS),))
add_bootstrap(
    app,
    font_family="Plus Jakarta Sans",
    theme=FASTCLOUD_THEME,
    mode="auto",
    include_favicon=False,
)


def current_theme(req) -> str:
    theme = req.session.get(THEME_KEY, "dark")
    return theme if theme in {"light", "dark"} else "dark"


def feature_grid() -> Any:
    return FeatureGrid(
        *[
            Feature(
                item["title"],
                item["description"],
                icon=item["icon"],
                cls=f"feature-shell {Fx.base} {Fx.fade_in}",
                icon_wrapper_cls="shadow-sm",
                title_cls="mb-2 fw-bold",
                description_cls="mb-0",
            )
            for item in FEATURES
        ],
        columns=3,
        row_cls="g-4",
        col_cls="h-100",
    )


def waitlist_panel(email: str = "", company_size: str = "") -> Any:
    return Div(
        H2("Start with a cleaner deploy loop.", cls="display-6 fw-bold mb-3"),
        P(
            "Join the preview list for guided onboarding, rollout templates, and Faststrap-powered operational surfaces.",
            cls="lead text-muted mb-4",
        ),
        Form(
            Div(
                Input(
                    name="email",
                    placeholder="Work email",
                    value=email,
                    input_type="email",
                    cls="flex-grow-1",
                    aria_label="Work email",
                ),
                Div(
                    Span(Icon("buildings"), cls="input-group-text"),
                    Input(
                        name="company_size",
                        placeholder="Team size",
                        value=company_size,
                        cls="form-control",
                        aria_label="Company size",
                    ),
                    cls="input-group flex-grow-1",
                ),
                Button("Join the preview", type="submit", variant="primary", cls="px-4"),
                cls="d-flex flex-column flex-lg-row gap-3",
            ),
            hx_post="/subscribe",
            hx_target="#waitlist-card",
            hx_swap="outerHTML",
        ),
        id="waitlist-card",
        cls="waitlist-card",
    )


@app.post("/theme/toggle")
def toggle_theme(req):
    req.session[THEME_KEY] = "light" if current_theme(req) == "dark" else "dark"
    return hx_refresh()


@app.post("/subscribe")
def subscribe(email: str = "", company_size: str = ""):
    normalized_email = email.strip()
    normalized_size = company_size.strip()
    if not normalized_email or "@" not in normalized_email:
        return toast_response(
            content=waitlist_panel(normalized_email, normalized_size),
            message="Enter a valid work email to continue.",
            variant="danger",
        )

    success_panel = Div(
        Span(Icon("check-circle-fill"), cls="text-success fs-2 mb-3 d-inline-flex"),
        H3("You are on the list.", cls="fw-bold mb-2"),
        P(
            f"We will reach out at {normalized_email} with onboarding details and rollout guidance.",
            cls="text-muted mb-0",
        ),
        id="waitlist-card",
        cls="waitlist-card text-center",
    )
    return toast_response(
        content=success_panel,
        message="Preview request received.",
        variant="success",
    )


@app.get("/")
def home(req):
    theme = current_theme(req)
    navbar = Div(
        NavbarModern(
            brand=Div(
                Span(
                    Icon("lightning-charge-fill"),
                    cls="d-inline-flex align-items-center justify-content-center me-2",
                    style="width:2rem;height:2rem;border-radius:0.7rem;background:linear-gradient(135deg,#6a6ff5,#4dabf7);color:white;",
                ),
                Strong("FastCloud", cls="fw-semibold text-white"),
                cls="d-flex align-items-center",
            ),
            items=[
                ("Features", "#features"),
                ("Pricing", "#pricing"),
                ("Customers", "#testimonials"),
                ThemeToggle(current_theme=theme, endpoint="/theme/toggle", cls="ms-lg-3"),
                Button("Get started", href="#waitlist", variant="primary", cls="ms-lg-3"),
            ],
            cls="app-navbar",
            container="lg",
        ),
        cls="app-nav-wrap",
    )

    hero = Section(
        Container(
            Div(
                Div(
                    Span(
                        Icon("stars"),
                        " Infrastructure for fast-moving teams",
                        cls="hero-kicker mb-4",
                    ),
                    H1(
                        "Deploy faster. Operate with clarity.",
                        cls=f"hero-display fw-black mb-4 {Fx.base} {Fx.fade_in}",
                    ),
                    P(
                        "FastCloud pairs polished operational surfaces with an infrastructure platform built for product teams that want speed without chaos.",
                        cls=f"lead mb-0 {Fx.base} {Fx.fade_in} {Fx.delay_sm}",
                    ),
                    Div(
                        A("See features", href="#features", cls="btn btn-primary btn-lg me-3 mt-4"),
                        A(
                            "Join preview",
                            href="#waitlist",
                            cls="btn btn-outline-light btn-lg mt-4",
                        ),
                    ),
                    Div(
                        Div(
                            Span("99.99%", cls="metric-value"),
                            Span("SLA target", cls="metric-label"),
                            cls="metric-card",
                        ),
                        Div(
                            Span("42s", cls="metric-value"),
                            Span("median deploy", cls="metric-label"),
                            cls="metric-card",
                        ),
                        Div(
                            Span("180+", cls="metric-value"),
                            Span("edge regions", cls="metric-label"),
                            cls="metric-card",
                        ),
                        cls="hero-metrics",
                    ),
                    cls="hero-copy",
                ),
                cls="row justify-content-center",
            ),
        ),
        id="hero",
        cls="hero-section",
    )

    features = Section(
        Container(
            Div(
                Span(Icon("grid-1x2-fill"), " Platform strengths", cls="hero-kicker mb-3"),
                H2("A cleaner path from deployment to product confidence.", cls="fw-bold mb-3"),
                P(
                    "This rescued showcase now doubles as a usable Faststrap reference: component-first, HTMX-friendly, and visually polished without leaning on generic Bootstrap defaults.",
                    cls="text-muted mb-0",
                ),
                cls="section-headline mb-5",
            ),
            feature_grid(),
        ),
        id="features",
        cls="section-surface",
    )

    pricing = Section(
        Container(
            PricingGroup(
                *TIERS,
                title="Pricing that grows with the workload.",
                subtitle="Start small, scale with confidence, and keep the product team operating from one coherent platform surface.",
                id="pricing",
            )
        ),
        cls="section-surface",
    )

    testimonials = Section(
        TestimonialSection(
            *TESTIMONIALS,
            title="Trusted by shipping teams",
            subtitle="The strongest signal is not the hero copy — it is whether operations, deploys, and debugging all feel calmer after the switch.",
            cls="section-surface",
            id="testimonials",
        )
    )

    waitlist = Section(
        Container(waitlist_panel()),
        id="waitlist",
        cls="section-surface pb-5",
    )

    footer = FooterModern(
        brand="FastCloud",
        tagline="A generated showcase rescued into a real reference app.",
        columns=FOOTER_COLUMNS,
        social_links=SOCIAL_LINKS,
        copyright_text="Copyright 2026 FastCloud. Built with Faststrap.",
        cls="footer-modern",
    )

    return Div(
        navbar,
        Main(hero, features, pricing, testimonials, waitlist, cls="flex-grow-1"),
        footer,
        ToastContainer(id="toast-container", position="top-end"),
        cls="app-shell",
        data_bs_theme=theme,
    )


if __name__ == "__main__":
    serve(port=5006)
