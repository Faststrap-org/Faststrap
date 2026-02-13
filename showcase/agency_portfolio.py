"""
Showcase 3 — Creative Agency Portfolio
A dark-themed creative agency portfolio with glassmorphism, scroll-reveal
animations, InfiniteScroll project gallery, and contact form with toast feedback.
Demonstrates: Fx.glass, Fx.hover_glow, LazyLoad, InfiniteScroll, FormGroup,
LoadingButton, SEO, FooterModern.
"""

from fasthtml.common import (
    A,
    Br,
    Div,
    FastHTML,
    H1,
    H2,
    H5,
    P,
    Span,
    Textarea,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Card,
    Col,
    Container,
    FooterModern,
    FormGroup,
    Fx,
    Icon,
    Navbar,
    Row,
    Spinner,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
)
from faststrap.presets import InfiniteScroll, LoadingButton, toast_response

app = FastHTML()
add_bootstrap(app)


# ─── Data ────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "Nebula Dashboard",
        "category": "Web App",
        "desc": "Real-time analytics platform with 3D data visualization.",
        "color": "#6366f1",
    },
    {
        "title": "Pulse Fitness",
        "category": "Mobile App",
        "desc": "AI-powered fitness tracker with gamified workout flows.",
        "color": "#ec4899",
    },
    {
        "title": "Verdant Farms",
        "category": "Branding",
        "desc": "Complete identity system for organic farm-to-table startup.",
        "color": "#10b981",
    },
    {
        "title": "Aurora Finance",
        "category": "Web App",
        "desc": "Personal finance dashboard with goal tracking and insights.",
        "color": "#f59e0b",
    },
    {
        "title": "Cipher Security",
        "category": "Web App",
        "desc": "Enterprise password manager with zero-knowledge architecture.",
        "color": "#ef4444",
    },
    {
        "title": "Bloom Studio",
        "category": "Branding",
        "desc": "Brand identity and digital presence for floral design studio.",
        "color": "#8b5cf6",
    },
]

SERVICES = [
    {
        "icon": "palette-fill",
        "title": "Brand Identity",
        "desc": "Logos, color systems, and brand guidelines.",
    },
    {
        "icon": "phone-fill",
        "title": "App Design",
        "desc": "Mobile and web applications that delight users.",
    },
    {
        "icon": "code-slash",
        "title": "Development",
        "desc": "Full-stack development — Python, FastHTML, FastStrap.",
    },
    {
        "icon": "megaphone-fill",
        "title": "Marketing",
        "desc": "SEO, social media, and growth strategy.",
    },
]

TEAM = [
    {"name": "Luna Park", "role": "Creative Director", "initial": "LP"},
    {"name": "Kai Zhang", "role": "Lead Developer", "initial": "KZ"},
    {"name": "Maya Singh", "role": "UX Designer", "initial": "MS"},
    {"name": "Jago Okoye", "role": "Brand Strategist", "initial": "JO"},
]


def project_card(project, index=0):
    """Single project card with glassmorphism and hover glow."""
    return Card(
        Div(
            Div(
                style=(
                    f"background: linear-gradient(135deg, {project['color']}66,"
                    f" {project['color']}22);"
                    " height: 200px; border-radius: 0.5rem 0.5rem 0 0;"
                    " display: flex; align-items: center; justify-content: center;"
                ),
                children=[
                    Icon("image", size="3rem", cls="text-white-50"),
                ],
            ),
        ),
        Div(
            Badge(project["category"], variant="light", pill=True, cls="mb-2"),
            H5(project["title"], cls="card-title text-white"),
            P(project["desc"], cls="card-text text-white-50"),
            cls="card-body",
        ),
        cls=(
            f"border-0 bg-dark bg-opacity-50 overflow-hidden"
            f" {Fx.glass} {Fx.hover_glow} {Fx.fade_in}"
        ),
        style=f"animation-delay: {index * 100}ms;",
    )


@app.get("/")
def home():
    return Div(
        # ── Navigation ───────────────────────────────────────
        Navbar(
            brand="VORTEX",
            items=[
                {"text": "Work", "href": "#work"},
                {"text": "Services", "href": "#services"},
                {"text": "Team", "href": "#team"},
                {"text": "Contact", "href": "#contact"},
            ],
            variant="dark",
            expand="lg",
            sticky=True,
            cls="border-bottom border-secondary",
        ),
        # ── Hero ─────────────────────────────────────────────
        Div(
            Container(
                Div(
                    Badge(
                        "Award-Winning Agency",
                        variant="light",
                        pill=True,
                        cls=f"mb-4 {Fx.fade_in}",
                    ),
                    H1(
                        "We craft digital",
                        Br(),
                        Span("experiences", cls="text-primary"),
                        " that matter.",
                        cls=f"display-2 fw-bold text-white mb-4 {Fx.slide_up}",
                    ),
                    P(
                        "Vortex is a creative agency specializing in brand identity,"
                        " web applications, and digital marketing. Built with FastStrap.",
                        cls=f"lead text-white-50 mb-5 {Fx.slide_up} {Fx.delay_sm}",
                        style="max-width: 600px;",
                    ),
                    Div(
                        A(
                            "View Our Work",
                            href="#work",
                            cls=f"btn btn-primary btn-lg me-3 {Fx.fade_in} {Fx.delay_md}",
                        ),
                        A(
                            "Get In Touch",
                            href="#contact",
                            cls=f"btn btn-outline-light btn-lg {Fx.fade_in} {Fx.delay_lg}",
                        ),
                    ),
                    cls="py-5",
                ),
            ),
            cls="min-vh-100 d-flex align-items-center",
            style=("background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);"),
        ),
        # ── Services ─────────────────────────────────────────
        Div(
            Container(
                H2(
                    "What We Do",
                    cls=f"text-center text-white fw-bold mb-5 {Fx.fade_in}",
                ),
                Row(
                    *[
                        Col(
                            Card(
                                Div(
                                    Icon(
                                        s["icon"],
                                        size="2.5rem",
                                        cls="text-primary mb-3",
                                    ),
                                    cls="text-center",
                                ),
                                H5(s["title"], cls="card-title text-white text-center"),
                                P(s["desc"], cls="card-text text-white-50 text-center"),
                                cls=(
                                    f"border-0 bg-dark bg-opacity-50 h-100"
                                    f" {Fx.glass} {Fx.hover_lift} {Fx.fade_in}"
                                ),
                                style=f"animation-delay: {i * 100}ms;",
                            ),
                            cols=12,
                            md=6,
                            lg=3,
                            cls="mb-4",
                        )
                        for i, s in enumerate(SERVICES)
                    ],
                ),
            ),
            id="services",
            cls="py-5",
            style="background: #0f0f1a;",
        ),
        # ── Work / Portfolio ─────────────────────────────────
        Div(
            Container(
                H2(
                    "Selected Work",
                    cls=f"text-center text-white fw-bold mb-2 {Fx.fade_in}",
                ),
                P(
                    "Browse our latest projects. Scroll down for more.",
                    cls=f"text-center text-white-50 mb-5 {Fx.fade_in} {Fx.delay_sm}",
                ),
                Div(
                    Row(
                        *[
                            Col(
                                project_card(p, i),
                                cols=12,
                                md=6,
                                lg=4,
                                cls="mb-4",
                            )
                            for i, p in enumerate(PROJECTS[:6])
                        ],
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
            cls="py-5",
            style="background: #1a1a2e;",
        ),
        # ── Team ─────────────────────────────────────────────
        Div(
            Container(
                H2(
                    "Meet the Team",
                    cls=f"text-center text-white fw-bold mb-5 {Fx.fade_in}",
                ),
                Row(
                    *[
                        Col(
                            Card(
                                Div(
                                    Div(
                                        t["initial"],
                                        cls=(
                                            "rounded-circle bg-primary text-white"
                                            " d-flex align-items-center justify-content-center mx-auto mb-3"
                                        ),
                                        style="width: 80px; height: 80px; font-size: 1.5rem; font-weight: bold;",
                                    ),
                                    H5(t["name"], cls="card-title text-white text-center mb-1"),
                                    P(t["role"], cls="text-primary text-center small"),
                                    cls="card-body text-center",
                                ),
                                cls=(
                                    f"border-0 bg-dark bg-opacity-50"
                                    f" {Fx.glass} {Fx.hover_lift} {Fx.fade_in}"
                                ),
                                style=f"animation-delay: {i * 100}ms;",
                            ),
                            cols=6,
                            lg=3,
                            cls="mb-4",
                        )
                        for i, t in enumerate(TEAM)
                    ],
                ),
            ),
            id="team",
            cls="py-5",
            style="background: #0f0f1a;",
        ),
        # ── Testimonial Section ──────────────────────────────
        Div(
            Container(
                H2(
                    "Client Love",
                    cls=f"text-center text-white fw-bold mb-5 {Fx.fade_in}",
                ),
                TestimonialSection(
                    Testimonial(
                        quote=(
                            "Vortex completely transformed our brand."
                            " The attention to detail is unmatched."
                        ),
                        author="Emma Larsson",
                        role="CEO, Verdant Farms",
                        rating=5,
                    ),
                    Testimonial(
                        quote=(
                            "Our dashboard went from good to extraordinary."
                            " Users love the new experience."
                        ),
                        author="Raj Patel",
                        role="Product Lead, Nebula Inc.",
                        rating=5,
                    ),
                    columns=2,
                ),
            ),
            cls="py-5",
            style="background: #1a1a2e;",
        ),
        # ── Contact Form ─────────────────────────────────────
        Div(
            Container(
                Row(
                    Col(
                        H2("Let's Talk", cls=f"text-white fw-bold mb-3 {Fx.fade_in}"),
                        P(
                            "Have a project in mind? We'd love to hear about it.",
                            cls=f"text-white-50 mb-4 {Fx.fade_in} {Fx.delay_sm}",
                        ),
                        Div(
                            Div(
                                Icon("envelope-fill", cls="text-primary me-3"),
                                A(
                                    "hello@vortex.agency",
                                    href="mailto:hello@vortex.agency",
                                    cls="text-white",
                                ),
                                cls="d-flex align-items-center mb-3",
                            ),
                            Div(
                                Icon("geo-alt-fill", cls="text-primary me-3"),
                                Span("Lagos, Nigeria", cls="text-white-50"),
                                cls="d-flex align-items-center mb-3",
                            ),
                            Div(
                                Icon("telephone-fill", cls="text-primary me-3"),
                                Span("+234 123 456 789", cls="text-white-50"),
                                cls="d-flex align-items-center mb-3",
                            ),
                        ),
                        cols=12,
                        md=5,
                    ),
                    Col(
                        Card(
                            FormGroup(
                                Input(
                                    name="name",
                                    placeholder="Your name",
                                    cls="bg-dark text-white border-secondary",
                                ),
                                label="Name",
                                cls="text-white-50",
                            ),
                            FormGroup(
                                Input(
                                    name="email",
                                    type="email",
                                    placeholder="your@email.com",
                                    cls="bg-dark text-white border-secondary",
                                ),
                                label="Email",
                                cls="text-white-50",
                            ),
                            FormGroup(
                                Textarea(
                                    name="message",
                                    placeholder="Tell us about your project...",
                                    rows=4,
                                    cls="bg-dark text-white border-secondary",
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
                                cls="w-100",
                            ),
                            Div(id="contact-result", cls="mt-3"),
                            cls=f"border-0 bg-dark bg-opacity-75 {Fx.glass} {Fx.slide_up}",
                        ),
                        cols=12,
                        md=7,
                    ),
                ),
            ),
            id="contact",
            cls="py-5",
            style="background: #0f0f1a;",
        ),
        # ── Footer ───────────────────────────────────────────
        FooterModern(
            brand="VORTEX",
            tagline="Crafting digital experiences since 2024.",
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
                {"icon": "behance", "href": "#"},
                {"icon": "linkedin", "href": "#"},
            ],
            copyright_text="© 2026 Vortex Agency. All rights reserved.",
            bg_variant="dark",
            text_variant="light",
        ),
        # Toast container
        ToastContainer(position="top-end"),
        # Global dark theme
        style="background: #0f0f1a; color: #fff;",
    )


# ─── API Endpoints ───────────────────────────────────────────────────
MORE_PROJECTS = [
    {
        "title": "Horizon Travel",
        "category": "Web App",
        "desc": "Travel booking platform with AI itinerary planning.",
        "color": "#06b6d4",
    },
    {
        "title": "Muse Gallery",
        "category": "Branding",
        "desc": "Contemporary art gallery identity and exhibition design.",
        "color": "#a855f7",
    },
    {
        "title": "Quantum Labs",
        "category": "Web App",
        "desc": "Research collaboration platform for quantum computing.",
        "color": "#14b8a6",
    },
]


@app.get("/api/more-projects")
def more_projects(page: int = 2):
    """Load more projects via InfiniteScroll."""
    import time

    time.sleep(0.5)  # Simulate loading

    items = [
        Col(
            project_card(p, i),
            cols=12,
            md=6,
            lg=4,
            cls="mb-4",
        )
        for i, p in enumerate(MORE_PROJECTS)
    ]

    result = Row(*items)

    # No more pages after page 2
    if page < 3:
        return Div(
            result,
            InfiniteScroll(
                endpoint=f"/api/more-projects?page={page + 1}",
                target="#portfolio-grid",
                content=Div(
                    Spinner(cls="text-primary"),
                    cls="text-center py-4",
                ),
            ),
        )
    return Div(
        result,
        P("That's all for now!", cls="text-center text-white-50 py-4"),
    )


@app.post("/api/contact")
def contact():
    """Handle contact form submission."""
    return toast_response(
        content=Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Message sent! We'll get back to you within 24 hours.",
            variant="success",
        ),
        message="Thank you for reaching out!",
        variant="success",
    )


serve()
