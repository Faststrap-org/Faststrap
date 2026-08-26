"""Flagship showcase — Education Exam Suite.

Production-grade exam/question-bank management for Faststrap:

- create_theme() with academic palette (navy/gold)
- Custom CSS for premium academic aesthetic
- Math for rendered exam equations (KaTeX CDN)
- Switcher for responsive question layout
- SplitPane for master/detail question browser
- SearchBar for question filtering
- ProfileDropdown for instructor menu
- DataCard for exam metadata
- FilePreview for attached resources
- DashboardGrid, DataTable, Card, Button, Form
- AutoRefresh for live metrics
- Fx animations throughout
- Port 5020
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    A,
    Button,
    Div,
    FastHTML,
    H1,
    H2,
    H3,
    H4,
    H5,
    Input,
    Link,
    P,
    Script,
    Small,
    Span,
    Style,
    Table,
    Tbody,
    Td,
    Tfoot,
    Thead,
    Tr,
    Th,
    serve,
)

from faststrap import (
    Col,
    Container,
    DashboardGrid,
    DataCard,
    DataTable,
    FilePreview,
    Math,
    ProfileDropdown,
    Row,
    Card,
    Navbar,
    SearchBar,
    SplitPane,
    Switcher,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import AutoRefresh, hx_refresh

THEME_KEY = "exam_theme"

EXAM_THEME = create_theme(
    primary="#1e3a5f",
    secondary="#c9a84c",
    success="#2d6e32",
    danger="#b02a2a",
    warning="#b8860b",
    info="#2563a8",
)

app = FastHTML()
add_bootstrap(app, theme=EXAM_THEME, font_family="Inter")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');

:root {
  --exam-gold: #c9a84c;
  --exam-navy: #1e3a5f;
  --exam-paper: #faf8f3;
}

.exam-shell {
  min-height: 100vh;
  background: var(--exam-paper);
  color: #1f2937;
}

.exam-shell[data-bs-theme="dark"] {
  background: #0b1220;
  color: #e2e8f0;
}

.exam-nav {
  background: var(--exam-navy) !important;
  border-bottom: 1px solid rgba(201,168,76,0.25);
}

.exam-brand {
  font-family: 'Crimson Pro', serif;
  font-weight: 700;
  color: var(--exam-gold);
  letter-spacing: -0.02em;
}

.exam-hero {
  background: linear-gradient(160deg, rgba(30,58,95,0.95), rgba(30,58,95,0.75));
  color: #fff;
  padding: 4rem 0;
}

.exam-card {
  border: 1px solid rgba(30,58,95,0.08);
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  transition: box-shadow 0.2s, transform 0.2s;
}

.exam-shell[data-bs-theme="dark"] .exam-card {
  background: rgba(30,58,95,0.35);
  border-color: rgba(201,168,76,0.12);
}

.exam-card:hover {
  box-shadow: 0 8px 24px rgba(30,58,95,0.10);
  transform: translateY(-2px);
}

.exam-math-card {
  background: linear-gradient(135deg, rgba(30,58,95,0.04), rgba(201,168,76,0.06));
  border: 1px solid rgba(201,168,76,0.18);
  border-radius: 12px;
}

.exam-section-label {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--exam-gold);
}

.exam-footer {
  background: var(--exam-navy);
  color: rgba(255,255,255,0.7);
  padding: 2rem 0;
}
"""

EXAMS = [
    {
        "id": "CAL-101",
        "title": "Calculus I — Derivatives",
        "questions": 24,
        "duration": "90 min",
        "status": "active",
        "difficulty": "Medium",
    },
    {
        "id": "PHY-201",
        "title": "Physics — Mechanics",
        "questions": 18,
        "duration": "60 min",
        "status": "draft",
        "difficulty": "Hard",
    },
    {
        "id": "CHE-101",
        "title": "Chemistry — Stoichiometry",
        "questions": 20,
        "duration": "45 min",
        "status": "active",
        "difficulty": "Easy",
    },
]

QUESTIONS = [
    {
        "id": 1,
        "topic": "Calculus",
        "title": "Derivative of e^x",
        "difficulty": "Easy",
        "equation": r"\frac{d}{dx} e^x = e^x",
        "attachment": "notes.pdf",
    },
    {
        "id": 2,
        "topic": "Physics",
        "title": "Kinetic Energy",
        "difficulty": "Medium",
        "equation": r"E_k = \frac{1}{2}mv^2",
        "attachment": "diagram.png",
    },
    {
        "id": 3,
        "topic": "Chemistry",
        "title": "Ideal Gas Law",
        "difficulty": "Easy",
        "equation": r"PV = nRT",
        "attachment": "data.csv",
    },
]


def exam_card(exam: dict, idx: int = 0) -> Any:
    return Card(
        Div(
            Span(exam["id"], cls="exam-section-label"),
            H4(exam["title"], cls="h5 mt-2 mb-2"),
            Row(
                Col(Small(f"Questions: {exam['questions']}"), cls="text-muted"),
                Col(Small(f"Duration: {exam['duration']}"), cls="text-muted text-end"),
                cls="g-2 mb-2",
            ),
            Div(
                Span(exam["difficulty"], cls="badge text-bg-secondary me-2"),
                Span(exam["status"].title(), cls=f"badge text-bg-{'success' if exam['status']=='active' else 'warning'}"),
            ),
        ),
        cls=f"exam-card h-100",
        style=f"animation-delay:{idx * 80}ms;",
    )


def question_row(q: dict) -> Any:
    return Tr(
        Td(q["id"]),
        Td(q["topic"]),
        Td(q["title"]),
        Td(q["difficulty"]),
        Td(
            A("View", href=f"/question/{q['id']}", cls="btn btn-sm btn-outline-primary"),
        ),
    )


@app.get("/")
def home(req) -> Any:
    theme = req.session.get(THEME_KEY, "light")
    return Div(
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
        ),
        Script(
            defer=True,
            src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
        ),
        Style(CSS),
        Navbar(
            SearchBar(
                placeholder="Search questions...",
                endpoint="/search",
                target="#search-results",
                cls="me-3",
            ),
            ProfileDropdown(
                "Dr. Alex Okafor",
                subtitle="Mathematics Dept.",
                items=[
                    ("Dashboard", "/"),
                    ("Question Bank", "/questions"),
                    ("Settings", "/settings"),
                    ("Sign out", "/logout"),
                ],
            ),
            brand="ExamForge",
            brand_href="/",
            items=[
                {"text": "Exams", "href": "#exams"},
                {"text": "Question Bank", "href": "#questions"},
                {"text": "Analytics", "href": "#analytics"},
            ],
            variant="dark",
            bg="dark",
            expand="lg",
            sticky="top",
            cls="exam-nav",
        ),
        Div(cls="exam-hero mb-5"),
        Container(
            Div(
                H1("Exam Suite", cls="display-5 fw-bold mb-2"),
                P(
                    "Build, organize, and deliver math-heavy assessments with live-rendered equations.",
                    cls="lead text-muted mb-0",
                ),
                cls="py-5",
            ),
            Row(
                Col(
                    DataCard(
                        "Calculus I",
                        subtitle="Midterm Exam",
                        status="active",
                        metrics={
                            "Questions": "24",
                            "Duration": "90 min",
                            "Pass Rate": "78%",
                        },
                        fields={
                            "Due": "Oct 15",
                            "Attempts": "3",
                        },
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    DataCard(
                        "Physics",
                        subtitle="Final Exam",
                        status="warning",
                        metrics={
                            "Questions": "18",
                            "Duration": "60 min",
                            "Pass Rate": "65%",
                        },
                        fields={
                            "Due": "Nov 02",
                            "Attempts": "2",
                        },
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    DataCard(
                        "Chemistry",
                        subtitle="Quiz 3",
                        status="success",
                        metrics={
                            "Questions": "20",
                            "Duration": "45 min",
                            "Pass Rate": "92%",
                        },
                        fields={
                            "Due": "Completed",
                            "Attempts": "1",
                        },
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                Col(
                    Card(
                        AutoRefresh(
                            endpoint="/api/metrics",
                            target="this",
                            interval=5000,
                            content=Div(
                                P("Active students: 1,247", cls="mb-1"),
                                P("Submissions today: 38", cls="mb-0 text-muted"),
                            ),
                        ),
                        title="Live Metrics",
                    ),
                    cols=12, cols_md=6, cols_lg=3,
                ),
                g=3,
                cls="mb-5",
            ),
            H2("Question Bank", cls="h4 mb-3"),
            SplitPane(
                Div(id="question-list"),
                Div(
                    H4("Preview", cls="mb-3"),
                    Div(
                        P("Select a question to preview.", cls="text-muted"),
                        id="question-preview",
                    ),
                ),
                initial_ratio="40/60",
                stack_on="md",
            ),
            Div(id="search-results", cls="mt-3"),
            H2("Equation Gallery", cls="h4 mb-3 mt-5"),
            Switcher(
                Card(
                    Math(r"\frac{d}{dx} e^x = e^x", display_mode=True),
                    title="Derivatives",
                ),
                Card(
                    Math(r"E_k = \frac{1}{2}mv^2", display_mode=True),
                    title="Kinetic Energy",
                ),
                Card(
                    Math(r"\ce{2H2 + O2 -> 2H2O}", display_mode=True),
                    title="Chemistry",
                ),
                ratio="1fr 1fr 1fr",
                gap=3,
            ),
            cls="my-5",
        ),
        Div(
            Container(
                P("© 2026 ExamForge. Built with Faststrap.", cls="mb-0"),
            ),
            cls="exam-footer mt-5",
        ),
        cls="exam-shell",
        data_bs_theme=theme,
    )


@app.get("/search")
def search(q: str = ""):
    if not q:
        return P("Type a keyword to search...", cls="text-muted")
    filtered = [q for q in QUESTIONS if q["topic"].lower() in q["topic"].lower() or q["title"].lower().find(q.lower()) >= 0]
    if not filtered:
        return P(f"No questions matching '{q}'", cls="text-muted")
    return Table(
        Thead(Tr(Th("ID"), Th("Topic"), Th("Title"), Th("Difficulty"), Th("Action"))),
        Tbody(*[question_row(q) for q in filtered]),
        striped=True,
        hover=True,
        cls="mt-3",
    )


@app.get("/question/{qid}")
def question_detail(qid: int):
    question = next((q for q in QUESTIONS if q["id"] == qid), None)
    if not question:
        return P("Question not found.", cls="text-danger")
    return Card(
        H4(question["title"], cls="h5 mb-3"),
        Math(question["equation"], display_mode=True),
        P(f"Difficulty: {question['difficulty']}", cls="text-muted"),
        FilePreview(
            src=f"https://via.placeholder.com/400x300?text={question['attachment']}",
            title=question["attachment"],
            height="150px",
        ),
    )


@app.get("/api/metrics")
def metrics() -> Any:
    import random
    return Div(
        P(f"Active students: {random.randint(1200, 1300):,}", cls="mb-1"),
        P(f"Submissions today: {random.randint(30, 50)}", cls="mb-0 text-muted"),
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "dark" if req.session.get(THEME_KEY, "light") == "light" else "light"
    return hx_refresh()


if __name__ == "__main__":
    serve(port=5020)
