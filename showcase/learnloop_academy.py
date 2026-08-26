"""Flagship showcase — LearnLoop Academy.

Production-grade edtech / online course platform for Faststrap:

- Inter body + Syne display headlines
- Electric violet / teal dual-tone dark palette
- DashboardLayout-style shell with progress tracking sidebar
- Raw Nav() navbar for reliable Bootstrap 5 collapse
- Row(cols=1, cols_md=N, cols_lg=N) responsive grids throughout
- Progress bars, Tabs, Accordion for course content patterns
- Fx entrance + hover animations on every section
- HTMX AutoRefresh for live enrollment counter
- Port 5018
"""

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H5,
    A,
    Br,
    Button,
    Div,
    FastHTML,
    Link,
    Nav,
    P,
    Script,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Card,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    Math,
    ProgressBar,
    Row,
    TabPane,
    Tabs,
    Testimonial,
    TestimonialSection,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import AutoRefresh

# ── Theme ────────────────────────────────────────────────────────────────────

LL_THEME = create_theme(
    primary="#7C3AED",  # electric violet
    secondary="#0D9488",  # teal
    success="#10B981",
    danger="#EF4444",
    warning="#F59E0B",
    info="#06B6D4",
)

app = FastHTML()
add_bootstrap(app, font_family="Inter", theme=LL_THEME, mode="dark")

# ── CSS ──────────────────────────────────────────────────────────────────────

LL_CSS = Style("""
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=swap');

/* ── Page shell ─────────────────────────────────────── */
.ll-shell {
  background:
    radial-gradient(ellipse at top left,  rgba(124,58,237,0.28) 0%, transparent 38%),
    radial-gradient(ellipse at 96%  5%,   rgba(13,148,136,0.20) 0%, transparent 30%),
    linear-gradient(180deg, #070b14 0%, #0a0f1e 48%, #0d1326 100%);
  min-height: 100vh;
  color: #e2e8f0;
}

/* ── Navbar ─────────────────────────────────────────── */
.ll-nav {
  background: rgba(7,11,20,0.80) !important;
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(124,58,237,0.16);
  padding: 0.55rem 0;
}
.ll-brand {
  font-family: 'Syne', sans-serif;
  font-size: 1.35rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a78bfa, #2dd4bf);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.02em;
}
.ll-nav .nav-link {
  color: rgba(226,232,240,0.72) !important;
  font-weight: 600;
  font-size: 0.88rem;
  border-radius: 999px;
  padding: 0.5rem 0.9rem !important;
  transition: color 0.18s ease, background 0.18s ease;
}
.ll-nav .nav-link:hover { color: #fff !important; background: rgba(124,58,237,0.14); }
.ll-enroll-btn {
  background: linear-gradient(135deg, #7C3AED, #0D9488) !important;
  border: none !important;
  border-radius: 50px !important;
  font-weight: 700 !important;
  font-size: 0.85rem !important;
  padding: 0.5rem 1.25rem !important;
  color: #fff !important;
  transition: opacity 0.2s, transform 0.2s !important;
}
.ll-enroll-btn:hover { opacity: 0.9 !important; transform: translateY(-1px) !important; }

/* ── Hero ───────────────────────────────────────────── */
.ll-hero { padding: 5rem 0 3.5rem; }
.ll-hero-headline {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.6rem, 6.5vw, 5rem);
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -0.04em;
  color: #f0f6ff;
}
.ll-gradient-text {
  background: linear-gradient(135deg, #a78bfa 0%, #2dd4bf 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.ll-eyebrow {
  display: inline-flex; align-items: center; gap: 0.45rem;
  background: rgba(124,58,237,0.16);
  border: 1px solid rgba(124,58,237,0.28);
  color: #c4b5fd;
  border-radius: 999px;
  padding: 0.35rem 0.85rem;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}
.ll-live-badge {
  display: inline-flex; align-items: center; gap: 0.4rem;
  background: rgba(13,148,136,0.14);
  border: 1px solid rgba(13,148,136,0.28);
  color: #2dd4bf;
  border-radius: 999px;
  padding: 0.3rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 700;
}
.ll-live-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #2dd4bf;
  animation: ll-pulse 1.6s ease-in-out infinite;
}
@keyframes ll-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.4; transform: scale(0.7); }
}

/* ── Section heading ────────────────────────────────── */
.ll-overline {
  display: block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: #a78bfa;
  margin-bottom: 0.45rem;
}
.ll-section-heading {
  font-family: 'Syne', sans-serif;
  font-size: clamp(1.9rem, 3.5vw, 2.6rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #f0f6ff;
  line-height: 1.1;
}

/* ── Course card ────────────────────────────────────── */
.ll-course-card {
  position: relative;
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 1.25rem;
  overflow: hidden;
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  height: 100%;
}
.ll-course-card:hover {
  transform: translateY(-6px);
  border-color: rgba(124,58,237,0.28);
  box-shadow: 0 28px 60px rgba(2,6,23,0.36);
}
.ll-course-thumb {
  width: 100%; height: 160px;
  object-fit: cover;
}
.ll-course-body { padding: 1.25rem; }
.ll-course-level {
  font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em;
  text-transform: uppercase; border-radius: 999px;
  padding: 0.25rem 0.65rem; display: inline-block;
  margin-bottom: 0.6rem;
}
.ll-level-bg { background: rgba(124,58,237,0.16); color: #a78bfa; }
.ll-level-int { background: rgba(13,148,136,0.16); color: #2dd4bf; }
.ll-level-adv { background: rgba(239,68,68,0.14);  color: #fca5a5; }
.ll-course-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: #f0f6ff;
  line-height: 1.3;
  margin-bottom: 0.5rem;
}
.ll-course-meta { font-size: 0.78rem; color: rgba(148,163,184,0.7); }
.ll-rating { color: #F59E0B; font-size: 0.8rem; }

/* ── Stat card ──────────────────────────────────────── */
.ll-stat-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 1.25rem;
  padding: 1.75rem;
  text-align: center;
  transition: transform 0.22s ease;
}
.ll-stat-card:hover { transform: translateY(-4px); }
.ll-stat-val {
  font-family: 'Syne', sans-serif;
  font-size: 2.6rem;
  font-weight: 800;
  background: linear-gradient(135deg, #a78bfa, #2dd4bf);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
}
.ll-stat-lbl { font-size: 0.82rem; color: rgba(148,163,184,0.72); margin-top: 0.3rem; }

/* ── Feature item ───────────────────────────────────── */
.ll-feature {
  display: flex; gap: 1rem; align-items: flex-start;
  padding: 1.25rem;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 1rem;
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.ll-feature:hover { transform: translateY(-3px); border-color: rgba(124,58,237,0.22); }
.ll-feat-icon {
  width: 2.5rem; height: 2.5rem; min-width: 2.5rem;
  display: flex; align-items: center; justify-content: center;
  border-radius: 0.75rem;
  background: rgba(124,58,237,0.14);
  color: #a78bfa;
  font-size: 1.1rem;
}

/* ── Progress section ───────────────────────────────── */
.ll-progress-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 1.25rem;
  padding: 1.75rem;
}

/* ── CTA ────────────────────────────────────────────── */
.ll-cta {
  background:
    radial-gradient(ellipse at 25% 50%, rgba(124,58,237,0.36), transparent 55%),
    radial-gradient(ellipse at 78% 60%, rgba(13,148,136,0.26), transparent 45%),
    linear-gradient(135deg, #0a0f1e, #13064e);
  border-radius: 2rem;
  padding: 4rem 2rem;
  border: 1px solid rgba(124,58,237,0.20);
}
""")

# ── Data ─────────────────────────────────────────────────────────────────────

COURSES = [
    (
        "Python for Data Science",
        "Beginner",
        "bg",
        "21 hrs",
        "4.9",
        "8,240",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600",
    ),
    (
        "Full-Stack FastHTML",
        "Beginner",
        "bg",
        "18 hrs",
        "4.8",
        "5,102",
        "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=600",
    ),
    (
        "Machine Learning A–Z",
        "Intermediate",
        "int",
        "34 hrs",
        "4.9",
        "12,400",
        "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600",
    ),
    (
        "UI/UX Design Foundations",
        "Beginner",
        "bg",
        "15 hrs",
        "4.7",
        "6,880",
        "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=600",
    ),
    (
        "Cloud & DevOps Essentials",
        "Intermediate",
        "int",
        "28 hrs",
        "4.8",
        "4,312",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600",
    ),
    (
        "Advanced Prompt Engineering",
        "Advanced",
        "adv",
        "12 hrs",
        "4.9",
        "9,670",
        "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=600",
    ),
]

FEATURES = [
    (
        "patch-check-fill",
        "Expert Instructors",
        "Every course is built and maintained by practitioners with real-world experience in their field.",
    ),
    (
        "phone",
        "Learn Anywhere",
        "Mobile-optimised lessons, downloadable resources, and offline access so you learn on your terms.",
    ),
    (
        "trophy-fill",
        "Certificates",
        "Industry-recognised certificates upon completion — shareable on LinkedIn and verifiable by employers.",
    ),
    (
        "people-fill",
        "Live Cohorts",
        "Join scheduled cohort sessions with peers, live Q&A with instructors, and group project tracks.",
    ),
    (
        "translate",
        "10 Languages",
        "Course UI and subtitles available in English, French, Yoruba, Igbo, Hausa, Swahili, and more.",
    ),
    (
        "lightning-charge",
        "AI-Powered Paths",
        "Personalised learning paths that adapt to your pace, quiz results, and career goals automatically.",
    ),
]

STATS = [
    ("120K+", "Learners Enrolled"),
    ("850+", "Courses Available"),
    ("96%", "Completion Rate"),
    ("4.9/5", "Average Rating"),
]

LEARNING_PATHS = [
    (
        "Data & AI Track",
        [
            "Python Fundamentals",
            "Data Analysis with Pandas",
            "Machine Learning A–Z",
            "Deep Learning Foundations",
            "AI Product Design",
        ],
        "#a78bfa",
    ),
    (
        "Full-Stack Web Track",
        [
            "HTML, CSS & JS Basics",
            "FastHTML & Python UI",
            "Databases & APIs",
            "DevOps Essentials",
            "Launch Your Product",
        ],
        "#2dd4bf",
    ),
    (
        "Design Track",
        [
            "Design Thinking",
            "UI/UX Foundations",
            "Figma Mastery",
            "Design Systems",
            "Portfolio Projects",
        ],
        "#F59E0B",
    ),
]

LEVEL_CLS = {"bg": "ll-level-bg", "int": "ll-level-int", "adv": "ll-level-adv"}

# ── Helpers ───────────────────────────────────────────────────────────────────


def course_card(
    title: str,
    level: str,
    level_key: str,
    duration: str,
    rating: str,
    students: str,
    thumb: str,
    idx: int = 0,
) -> Any:
    from fasthtml.common import Img

    return Div(
        Img(src=thumb, cls="ll-course-thumb", alt=title),
        Div(
            Span(level, cls=f"ll-course-level {LEVEL_CLS[level_key]}"),
            Div(title, cls="ll-course-title"),
            Div(
                Span(
                    *[Icon("star-fill", cls="text-warning") for _ in range(5)],
                    cls="ll-rating me-1 d-inline-flex align-items-center gap-1",
                ),
                Span(rating, cls="fw-600 me-2"),
                Span(f"({students} students)"),
                cls="ll-course-meta mb-2",
            ),
            Div(
                Icon("clock", cls="me-1"),
                duration,
                " · ",
                Icon("play-circle", cls="ms-2 me-1"),
                "On-demand",
                cls="ll-course-meta",
            ),
            A(
                "Enroll Now",
                href="#",
                cls="btn btn-primary btn-sm w-100 mt-3 fw-600",
                style="border-radius:50px;",
            ),
            cls="ll-course-body",
        ),
        cls=f"ll-course-card {Fx.fade_in}",
        style=f"animation-delay:{idx * 70}ms;",
    )


def feature_item(icon: str, title: str, desc: str, idx: int = 0) -> Any:
    return Div(
        Div(Icon(icon), cls="ll-feat-icon"),
        Div(
            Strong(title, cls="d-block mb-1"),
            P(desc, cls="small mb-0", style="color:rgba(148,163,184,0.82);"),
        ),
        cls=f"ll-feature {Fx.fade_in}",
        style=f"animation-delay:{idx * 60}ms;",
    )


def stat_card(val: str, label: str, idx: int = 0) -> Any:
    return Div(
        Div(val, cls="ll-stat-val"),
        Div(label, cls="ll-stat-lbl"),
        cls=f"ll-stat-card {Fx.fade_in}",
        style=f"animation-delay:{idx * 80}ms;",
    )


# ── Route ─────────────────────────────────────────────────────────────────────


@app.get("/")
def home() -> Any:
    return Div(
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
        ),
        Script(
            defer=True,
            src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
        ),
        LL_CSS,
        # ── Navbar ─────────────────────────────────────────────────────────
        Nav(
            Div(
                A(
                    Span("learn", cls=""),
                    Span("loop", style="color:#2dd4bf;"),
                    cls="navbar-brand ll-brand",
                    href="#",
                ),
                Button(
                    Span(cls="navbar-toggler-icon"),
                    cls="navbar-toggler border-0",
                    type="button",
                    data_bs_toggle="collapse",
                    data_bs_target="#llNavCollapse",
                    aria_controls="llNavCollapse",
                    aria_expanded="false",
                    aria_label="Toggle navigation",
                ),
                Div(
                    Div(
                        A("Courses", href="#courses", cls="nav-link"),
                        A("Paths", href="#paths", cls="nav-link"),
                        A("Features", href="#features", cls="nav-link"),
                        A("Reviews", href="#reviews", cls="nav-link"),
                        A("Start Learning", href="#courses", cls="nav-link ll-enroll-btn ms-2"),
                        cls="navbar-nav ms-auto align-items-center gap-1",
                    ),
                    cls="collapse navbar-collapse",
                    id="llNavCollapse",
                ),
                cls="container-xl",
            ),
            cls="navbar navbar-expand-lg navbar-dark ll-nav position-sticky top-0 z-3",
        ),
        # ── Shell ───────────────────────────────────────────────────────────
        Div(
            Container(
                # ── Hero ───────────────────────────────────────────────────
                Div(
                    Row(
                        Col(
                            Span(
                                Icon("mortarboard-fill", cls="me-1"),
                                "Nigeria's #1 Tech Learning Platform",
                                cls="ll-eyebrow",
                            ),
                            H1(
                                "Learn Skills That",
                                Br(),
                                Span("Get You Hired.", cls="ll-gradient-text"),
                                cls=f"ll-hero-headline {Fx.slide_up}",
                            ),
                            P(
                                "120,000+ learners. 850+ expert-led courses. "
                                "Real skills, real certificates, real career outcomes — "
                                "every lesson built for today's job market.",
                                cls=f"mt-3 mb-4 fs-5 {Fx.fade_in} {Fx.delay_sm}",
                                style="color:rgba(148,163,184,0.88);max-width:500px;line-height:1.65;",
                            ),
                            Div(
                                A(
                                    Icon("rocket-takeoff-fill", cls="me-2"),
                                    "Browse All Courses",
                                    href="#courses",
                                    cls=f"btn btn-primary btn-lg fw-700 me-3 {Fx.fade_in} {Fx.delay_md}",
                                    style="border-radius:50px;",
                                ),
                                A(
                                    Icon("play-circle-fill", cls="me-2"),
                                    "Watch Demo",
                                    href="#",
                                    cls=f"btn btn-link text-light fw-600 {Fx.fade_in} {Fx.delay_lg}",
                                ),
                                cls="d-flex align-items-center flex-wrap gap-2",
                            ),
                            Div(
                                Div(cls="ll-live-dot"),
                                AutoRefresh(
                                    endpoint="/api/enrollment-count",
                                    target="this",
                                    interval=8000,
                                    content=Span("1,247 learners enrolled this week"),
                                ),
                                cls="ll-live-badge mt-4 d-inline-flex",
                            ),
                            lg=6,
                        ),
                        Col(
                            # Progress preview card
                            Div(
                                Div(
                                    Strong("My Learning Journey", cls="d-block mb-3 fs-6"),
                                    *[
                                        Div(
                                            Div(
                                                Span(course, cls="small fw-600"),
                                                Span(pct, cls="small text-muted"),
                                                cls="d-flex justify-content-between mb-1",
                                            ),
                                            ProgressBar(
                                                int(pct.replace("%", "")), variant=var, cls="mb-3"
                                            ),
                                        )
                                        for course, pct, var in [
                                            ("Python for Data Science", "78%", "primary"),
                                            ("ML Fundamentals", "45%", "info"),
                                            ("FastHTML Full-Stack", "92%", "success"),
                                        ]
                                    ],
                                    Div(
                                        Icon("trophy-fill", cls="text-warning me-2"),
                                        Strong("3 certificates earned this month"),
                                        cls="mt-3 small",
                                    ),
                                    cls="ll-progress-card",
                                ),
                                cls=f"{Fx.slide_left} {Fx.delay_md}",
                            ),
                            lg=6,
                            cls="d-none d-lg-block align-self-center",
                        ),
                        cls="align-items-center",
                        cols=1,
                        cols_lg=2,
                    ),
                    cls="ll-hero",
                ),
                # ── Stats ───────────────────────────────────────────────────
                Row(
                    *[
                        Col(stat_card(value, label, i), cls="mb-4")
                        for i, (value, label) in enumerate(STATS)
                    ],
                    cls="g-3 mb-5",
                    cols=2,
                    cols_md=4,
                ),
                # ── Courses ─────────────────────────────────────────────────
                Div(
                    Span("explore", cls="ll-overline"),
                    H2("Featured Courses", cls="ll-section-heading mb-1"),
                    P(
                        "Expert-built. Practically focused. Career-changing.",
                        cls="mb-4",
                        style="color:rgba(148,163,184,0.72);",
                    ),
                    Row(
                        *[Col(course_card(*c, idx=i), cls="mb-4") for i, c in enumerate(COURSES)],
                        cls="g-3",
                        cols=1,
                        cols_md=2,
                        cols_lg=3,
                    ),
                    id="courses",
                    cls="mb-5",
                ),
                # ── Learning Paths ───────────────────────────────────────────
                Div(
                    Span("structured learning", cls="ll-overline"),
                    H2("Curated Learning Paths", cls="ll-section-heading mb-1"),
                    P(
                        "Go from zero to job-ready with our step-by-step tracks.",
                        cls="mb-4",
                        style="color:rgba(148,163,184,0.72);",
                    ),
                    # Tabs nav
                    Tabs(
                        *[
                            (f"ll-path-{i}", name, i == 0)
                            for i, (name, _, _) in enumerate(LEARNING_PATHS)
                        ],
                    ),
                    # Tabs content
                    Div(
                        *[
                            TabPane(
                                Div(
                                    *[
                                        Div(
                                            Span(
                                                str(j + 1),
                                                cls="fw-800 me-3",
                                                style=f"color:{color};font-family:'Syne',sans-serif;font-size:1.1rem;min-width:1.5rem;",
                                            ),
                                            Div(
                                                Span(step, cls="fw-600 d-block"),
                                                ProgressBar(
                                                    (j + 1) * 20,
                                                    variant="primary",
                                                    cls="mt-1",
                                                    style="height:4px;background:rgba(255,255,255,0.06);",
                                                ),
                                                cls="flex-grow-1",
                                            ),
                                            cls="d-flex align-items-center py-3",
                                            style=(
                                                "border-bottom:1px solid rgba(255,255,255,0.05);"
                                                if j < len(steps) - 1
                                                else ""
                                            ),
                                        )
                                        for j, step in enumerate(steps)
                                    ],
                                    cls="ll-progress-card",
                                ),
                                tab_id=f"ll-path-{i}",
                                active=(i == 0),
                            )
                            for i, (name, steps, color) in enumerate(LEARNING_PATHS)
                        ],
                        cls="tab-content mt-3",
                    ),
                    id="paths",
                    cls="mb-5",
                ),
                # ── Features ─────────────────────────────────────────────────
                Div(
                    Span("why learnloop", cls="ll-overline"),
                    H2("Built for Serious Learners", cls="ll-section-heading mb-1"),
                    P(
                        "Everything you need to go from curious to competent.",
                        cls="mb-4",
                        style="color:rgba(148,163,184,0.72);",
                    ),
                    Row(
                        *[Col(feature_item(*f, idx=i), cls="mb-3") for i, f in enumerate(FEATURES)],
                        cls="g-3",
                        cols=1,
                        cols_md=2,
                        cols_lg=3,
                    ),
                    id="features",
                    cls="mb-5",
                ),
                # ── Testimonials ─────────────────────────────────────────────
                Div(
                    Span("learner stories", cls="ll-overline"),
                    H2("Real Results, Real People", cls="ll-section-heading mb-4"),
                    TestimonialSection(
                        Testimonial(
                            quote="I finished the Python for Data Science track in 8 weeks and got a data analyst offer in Lagos. The certificate was accepted immediately by the hiring team.",
                            author="Chidinma Okonkwo",
                            role="Data Analyst, Sterling Bank",
                            rating=5,
                        ),
                        Testimonial(
                            quote="LearnLoop's FastHTML course is the best web dev resource I've found anywhere. I built and launched my agency site before I even finished the track.",
                            author="Abdullahi Musa",
                            role="Freelance Developer",
                            rating=5,
                        ),
                        Testimonial(
                            quote="The ML course is absolutely world-class. The pacing, the projects, the feedback from instructors — it's better than any bootcamp I've attended.",
                            author="Yetunde Adeniyi",
                            role="ML Engineer, Flutterwave",
                            rating=5,
                        ),
                        columns=3,
                    ),
                    id="reviews",
                    cls="mb-5",
                ),
                # ── CTA ───────────────────────────────────────────────────────
                Div(
                    Span(
                        "your future starts here",
                        cls="ll-overline text-center d-block",
                        style="color:rgba(167,139,250,0.7);",
                    ),
                    H2(
                        "Join 120,000+ Learners",
                        Br(),
                        "Transforming Their Careers.",
                        cls=f"ll-section-heading text-center text-white {Fx.slide_up}",
                        style="font-size:clamp(1.9rem,3.5vw,2.8rem);",
                    ),
                    P(
                        "Start your first course today — no credit card required.",
                        cls=f"text-center mb-4 {Fx.fade_in} {Fx.delay_sm}",
                        style="color:rgba(255,255,255,0.6);",
                    ),
                    Div(
                        A(
                            Icon("rocket-takeoff-fill", cls="me-2"),
                            "Start Learning Free",
                            href="#courses",
                            cls="btn btn-primary btn-lg fw-700 me-3",
                            style="border-radius:50px;background:linear-gradient(135deg,#7C3AED,#0D9488)!important;border:none;",
                        ),
                        A(
                            "View All 850+ Courses",
                            href="#courses",
                            cls="btn btn-outline-light btn-lg fw-600",
                            style="border-radius:50px;",
                        ),
                        cls="text-center",
                    ),
                    cls=f"ll-cta mb-5 {Fx.fade_in}",
                ),
                # ── Math Preview ──────────────────────────────────────────────
                Div(
                    Span("STEM courses", cls="ll-overline"),
                    H2("Math & Science, Rendered Live", cls="ll-section-heading mb-1"),
                    P(
                        "LaTeX equations render directly in lesson content.",
                        cls="mb-4",
                        style="color:rgba(148,163,184,0.72);",
                    ),
                    Row(
                        Col(
                            Card(
                                H5("Physics 101", cls="card-title"),
                                P("Newton's law of universal gravitation:"),
                                Math(
                                    r"F = G \frac{m_1 m_2}{r^2}",
                                    display_mode=True,
                                ),
                            ),
                            cols=12, cols_md=6,
                        ),
                        Col(
                            Card(
                                H5("Chemistry", cls="card-title"),
                                P("Water formation reaction:"),
                                Math(
                                    r"\ce{2H2 + O2 -> 2H2O}",
                                    display_mode=True,
                                ),
                            ),
                            cols=12, cols_md=6,
                        ),
                        g=3,
                        cls="mb-5",
                    ),
                    id="math-preview",
                ),
                # ── Footer ────────────────────────────────────────────────────
                FooterModern(
                    brand="learnloop.",
                    tagline="Expert-led courses for Africa's next generation of tech talent.",
                    columns=[
                        {
                            "title": "Learn",
                            "links": [
                                {"text": "All Courses", "href": "#courses"},
                                {"text": "Learning Paths", "href": "#paths"},
                                {"text": "Live Cohorts", "href": "#"},
                                {"text": "Certificates", "href": "#"},
                            ],
                        },
                        {
                            "title": "Company",
                            "links": [
                                {"text": "About", "href": "#"},
                                {"text": "Careers", "href": "#"},
                                {"text": "Blog", "href": "#"},
                                {"text": "Partners", "href": "#"},
                            ],
                        },
                        {
                            "title": "Support",
                            "links": [
                                {"text": "FAQ", "href": "#"},
                                {"text": "Contact Us", "href": "#"},
                                {"text": "Community", "href": "#"},
                                {"text": "Refund Policy", "href": "#"},
                            ],
                        },
                    ],
                    social_links=[
                        {"icon": "twitter-x", "href": "#"},
                        {"icon": "linkedin", "href": "#"},
                        {"icon": "youtube", "href": "#"},
                        {"icon": "instagram", "href": "#"},
                    ],
                    copyright_text="© 2026 LearnLoop Academy Ltd. All Rights Reserved.",
                    cls="mt-2 rounded-4",
                ),
            ),
            cls="ll-shell py-2",
        ),
        ToastContainer(position="top-end"),
    )


# ── API Endpoints ─────────────────────────────────────────────────────────────


@app.get("/api/enrollment-count")
def enrollment_count() -> Any:
    import random

    count = random.randint(1_200, 1_400)
    return Span(f"{count:,} learners enrolled this week")


if __name__ == "__main__":
    serve(port=5018)
