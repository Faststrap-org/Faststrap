"""Test UI: CloudMetrics Analytics Dashboard - Faststrap Framework Evaluation

This test demonstrates whether the Faststrap framework and SKILL.md guidance
successfully produce premium, non-generic-Bootstrap UIs when followed strictly.

Reference apps: novaflow_ai_saas.py, northstar_ops_dashboard.py
Philosophy: Component-first, Bootstrap structure, HTMX interactivity, Custom CSS polish
Port: 5099
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# ruff: noqa: E402
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from fasthtml.common import (
    H1,
    H2,
    H4,
    Button,
    Div,
    FastHTML,
    P,
    Span,
    Style,
    serve,
)

from faststrap import (
    Alert,
    Card,
    Col,
    Container,
    ErrorPage,
    Icon,
    Input,
    PageMeta,
    Row,
    TabPane,
    Tabs,
    ThemeToggle,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import hx_refresh

# ─────────────────────────────────────────────────────────────────────────────
# THEME DEFINITION (Step 1: Shared design language)
# ─────────────────────────────────────────────────────────────────────────────

CLOUDMETRICS_THEME = create_theme(
    primary="#5B6CFF",  # Indigo (premium, not generic blue)
    secondary="#1F2937",  # Dark charcoal
    success="#10B981",  # Emerald
    danger="#EF4444",  # Red
    warning="#F59E0B",  # Amber
    info="#06B6D4",  # Cyan
    dark="#030712",  # Near-black shell
    light="#F8FAFC",  # Off-white
    radius="0.625rem",  # Intentional radii (not default 0.375)
    radius_lg="1rem",
)

THEME_KEY = "cm-theme"

app = FastHTML()
add_bootstrap(app, theme=CLOUDMETRICS_THEME, font_family="Inter", mode="auto")

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS (Step 2: Premium surface treatment)
# Philosophy: Minimal, intentional. Bootstrap does layout, we do atmosphere.
# ─────────────────────────────────────────────────────────────────────────────

DASHBOARD_CSS = Style("""
/* ════════════════════════════════════════════════════════════
   CloudMetrics · Premium Analytics Dashboard
   Palette: Indigo/charcoal dark shell with emerald accents
   Geometry: 4px separators, 6-8px card radii, intentional glass
   Philosophy: "Operational clarity" — precise, not cozy
   ════════════════════════════════════════════════════════════ */

/* ── Global shell ──────────────────────────────────────────── */
.cm-shell {
  background:
    radial-gradient(ellipse at 1% 0%, rgba(91, 108, 255, 0.18) 0%, transparent 35%),
    radial-gradient(ellipse at 98% 5%, rgba(6, 182, 212, 0.14) 0%, transparent 30%),
    linear-gradient(180deg, #030712 0%, #0a0f1e 40%, #0d1428 100%);
  min-height: 100vh;
  color: #e2e8f0;
}

.cm-shell[data-bs-theme="light"] {
  background:
    radial-gradient(ellipse at 1% 0%, rgba(91, 108, 255, 0.08) 0%, transparent 35%),
    radial-gradient(ellipse at 98% 5%, rgba(6, 182, 212, 0.07) 0%, transparent 30%),
    linear-gradient(180deg, #f8fafc 0%, #f0f4f8 100%);
  color: #0a0f1e;
}

/* ── Sidebar styling ───────────────────────────────────────── */
.cm-shell #sidebar-wrapper {
  background: linear-gradient(180deg, rgba(3, 7, 18, 0.98), rgba(10, 15, 30, 0.96)) !important;
  border-right: 1px solid rgba(91, 108, 255, 0.12) !important;
  backdrop-filter: blur(18px);
}

.cm-shell[data-bs-theme="light"] #sidebar-wrapper {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.99), rgba(248, 250, 252, 0.97)) !important;
  border-right: 1px solid rgba(91, 108, 255, 0.08) !important;
}

/* ── Navbar ────────────────────────────────────────────────── */
.cm-navbar {
  background: rgba(3, 7, 18, 0.82) !important;
  border-bottom: 1px solid rgba(91, 108, 255, 0.10) !important;
  backdrop-filter: blur(16px);
  padding: 0.85rem 1.5rem;
}

.cm-shell[data-bs-theme="light"] .cm-navbar {
  background: rgba(248, 250, 252, 0.92) !important;
  border-bottom: 1px solid rgba(91, 108, 255, 0.08) !important;
}

.cm-navbar .navbar-brand {
  font-weight: 700;
  font-size: 1.25rem;
  background: linear-gradient(135deg, #5B6CFF, #06B6D4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.015em;
}

.cm-navbar .nav-link {
  color: rgba(226, 232, 240, 0.72) !important;
  font-weight: 500;
  font-size: 0.9rem;
  border-radius: 5px;
  padding: 0.4rem 0.9rem !important;
  transition: all 0.15s ease;
}

.cm-navbar .nav-link:hover {
  color: #fff !important;
  background: rgba(91, 108, 255, 0.14);
}

.cm-shell[data-bs-theme="light"] .cm-navbar .nav-link {
  color: rgba(15, 23, 42, 0.72) !important;
}

.cm-shell[data-bs-theme="light"] .cm-navbar .nav-link:hover {
  color: #0a0f1e !important;
  background: rgba(91, 108, 255, 0.10);
}

/* ── Content area ──────────────────────────────────────────── */
.cm-content {
  background: transparent !important;
  padding: 1.75rem 1.5rem;
}

/* ── Cards & Surface Treatment ────────────────────────────── */
.cm-card {
  background: rgba(15, 23, 42, 0.50);
  border: 1px solid rgba(91, 108, 255, 0.14);
  border-radius: 0.75rem;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.04);
  transition: all 0.2s ease;
}

.cm-card:hover {
  border-color: rgba(91, 108, 255, 0.24);
  box-shadow: 0 8px 24px rgba(91, 108, 255, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.04);
}

.cm-shell[data-bs-theme="light"] .cm-card {
  background: rgba(255, 255, 255, 0.70);
  border-color: rgba(91, 108, 255, 0.12);
  box-shadow: 0 2px 8px rgba(91, 108, 255, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.5);
}

.cm-shell[data-bs-theme="light"] .cm-card:hover {
  border-color: rgba(91, 108, 255, 0.20);
  box-shadow: 0 6px 16px rgba(91, 108, 255, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.6);
}

/* ── Typography hierarchy ──────────────────────────────────── */
.cm-headline {
  font-size: clamp(1.8rem, 4vw, 2.4rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: #f0f6ff;
}

.cm-shell[data-bs-theme="light"] .cm-headline {
  color: #030712;
}

.cm-section-head {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.015em;
  color: #f0f6ff;
  margin-bottom: 1rem;
}

.cm-shell[data-bs-theme="light"] .cm-section-head {
  color: #0a0f1e;
}

.cm-body-quiet {
  font-size: 0.9rem;
  color: rgba(226, 232, 240, 0.64);
  line-height: 1.5;
}

.cm-shell[data-bs-theme="light"] .cm-body-quiet {
  color: rgba(15, 23, 42, 0.64);
}

/* ── Stat cards ────────────────────────────────────────────── */
.cm-stat-card {
  position: relative;
  padding: 1.25rem;
  border-left: 4px solid rgba(91, 108, 255, 0.6);
  transition: all 0.25s ease;
}

.cm-stat-card:hover {
  border-left-color: #5B6CFF;
  transform: translateX(2px);
}

.cm-stat-value {
  font-size: 1.75rem;
  font-weight: 800;
  line-height: 1.1;
  color: #fff;
}

.cm-shell[data-bs-theme="light"] .cm-stat-value {
  color: #030712;
}

.cm-stat-label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(226, 232, 240, 0.56);
  margin-top: 0.5rem;
}

.cm-shell[data-bs-theme="light"] .cm-stat-label {
  color: rgba(15, 23, 42, 0.56);
}

.cm-stat-delta {
  font-size: 0.85rem;
  font-weight: 600;
  margin-top: 0.75rem;
}

.cm-delta-up {
  color: #10B981;
}

.cm-delta-down {
  color: #EF4444;
}

/* ── Filter bar ────────────────────────────────────────────– */
.cm-filter-group {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 1.5rem;
}

.cm-filter-group input,
.cm-filter-group select {
  background: rgba(15, 23, 42, 0.40) !important;
  border: 1px solid rgba(91, 108, 255, 0.16) !important;
  color: #e2e8f0 !important;
  border-radius: 0.5rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.9rem;
  transition: all 0.15s ease;
}

.cm-filter-group input:focus,
.cm-filter-group select:focus {
  border-color: rgba(91, 108, 255, 0.4) !important;
  background: rgba(15, 23, 42, 0.60) !important;
  box-shadow: 0 0 0 3px rgba(91, 108, 255, 0.1);
}

.cm-shell[data-bs-theme="light"] .cm-filter-group input,
.cm-shell[data-bs-theme="light"] .cm-filter-group select {
  background: rgba(255, 255, 255, 0.60) !important;
  border-color: rgba(91, 108, 255, 0.12) !important;
  color: #0a0f1e !important;
}

/* ── Action buttons ────────────────────────────────────────── */
.cm-btn-primary {
  background: linear-gradient(135deg, #5B6CFF 0%, #4A52D9 100%);
  border: none;
  border-radius: 0.625rem;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 0.55rem 1.2rem;
  color: #fff;
  box-shadow: 0 4px 12px rgba(91, 108, 255, 0.28);
  transition: all 0.2s ease;
}

.cm-btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(91, 108, 255, 0.36);
}

.cm-btn-secondary {
  background: rgba(91, 108, 255, 0.12);
  border: 1px solid rgba(91, 108, 255, 0.24);
  border-radius: 0.625rem;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 0.55rem 1.2rem;
  color: rgba(226, 232, 240, 0.90);
  transition: all 0.15s ease;
}

.cm-btn-secondary:hover {
  background: rgba(91, 108, 255, 0.18);
  border-color: rgba(91, 108, 255, 0.32);
}

/* ── Tab styling ────────────────────────────────────────────– */
.cm-tabs .nav-link {
  color: rgba(226, 232, 240, 0.60) !important;
  border: none !important;
  border-bottom: 2px solid transparent !important;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 0.75rem 0 !important;
  transition: all 0.15s ease;
}

.cm-tabs .nav-link:hover {
  color: rgba(226, 232, 240, 0.90) !important;
  border-bottom-color: rgba(91, 108, 255, 0.4) !important;
}

.cm-tabs .nav-link.active {
  color: #5B6CFF !important;
  border-bottom-color: #5B6CFF !important;
}

/* ── Empty state ───────────────────────────────────────────– */
.cm-empty {
  text-align: center;
  padding: 3rem 1.5rem;
  color: rgba(226, 232, 240, 0.56);
}

.cm-empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.6;
}

/* ── Loading skeleton ──────────────────────────────────────– */
.cm-skeleton {
  background: linear-gradient(
    90deg,
    rgba(91, 108, 255, 0.1),
    rgba(91, 108, 255, 0.2),
    rgba(91, 108, 255, 0.1)
  );
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
  border-radius: 0.5rem;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* ── Responsive adjustments ────────────────────────────────– */
@media (max-width: 768px) {
  .cm-filter-group {
    flex-direction: column;
  }

  .cm-filter-group input,
  .cm-filter-group select {
    width: 100%;
  }

  .cm-content {
    padding: 1rem;
  }
}
""")

# ─────────────────────────────────────────────────────────────────────────────
# MOCK DATA
# ─────────────────────────────────────────────────────────────────────────────

EVENTS = [
    {"id": 1, "name": "Page View", "count": "1.2M", "delta": "+8.2%"},
    {"id": 2, "name": "Click Event", "count": "892K", "delta": "+5.1%"},
    {"id": 3, "name": "Form Submit", "count": "142K", "delta": "-2.3%"},
    {"id": 4, "name": "Error Logged", "count": "24K", "delta": "-12.5%"},
]

EVENTS_DETAIL = [
    {
        "event": "Page View",
        "yesterday": "1.1M",
        "today": "1.2M",
        "change": "+8.2%",
        "status": "up",
    },
    {
        "event": "Click Event",
        "yesterday": "849K",
        "today": "892K",
        "change": "+5.1%",
        "status": "up",
    },
    {
        "event": "Form Submit",
        "yesterday": "145K",
        "today": "142K",
        "change": "-2.3%",
        "status": "down",
    },
    {
        "event": "Error Logged",
        "yesterday": "27K",
        "today": "24K",
        "change": "-12.5%",
        "status": "down",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────


def current_theme(req) -> str:
    t = req.session.get(THEME_KEY, "dark")
    return t if t in {"light", "dark"} else "dark"


# ─────────────────────────────────────────────────────────────────────────────
# UI COMPONENTS (Step 3: Faststrap components first)
# ─────────────────────────────────────────────────────────────────────────────


def stat_card_row() -> Any:
    """Row of stat cards using custom cm-card + cm-stat-card styling."""
    cards = []
    for event in EVENTS:
        delta_cls = "cm-delta-up" if event["delta"].startswith("+") else "cm-delta-down"
        cards.append(
            Col(
                Card(
                    Div(
                        P(event["count"], cls="cm-stat-value"),
                        P(event["name"], cls="cm-stat-label"),
                        P(event["delta"], cls=f"cm-stat-delta {delta_cls}"),
                        cls="cm-stat-card",
                    ),
                    cls="cm-card h-100",
                ),
                cls="col-12 col-md-6 col-lg-3 mb-3",
            )
        )
    return Row(*cards, cls="g-2")


def filter_controls() -> Any:
    """Filter bar using Bootstrap row/col + custom CSS."""
    return Div(
        Div(
            Input(
                name="search",
                input_type="text",
                placeholder="Search events...",
            ),
            Input(
                name="date_filter",
                input_type="date",
            ),
            Button(
                Icon("arrow-clockwise"),
                " Refresh",
                cls="btn cm-btn-secondary",
                hx_get="/api/events",
                hx_target="#events-table",
                hx_swap="innerHTML",
            ),
            cls="cm-filter-group",
        ),
        cls="mb-2",
    )


def events_table() -> Any:
    """Events table rows using Bootstrap badge styling."""
    rows = []
    for event in EVENTS_DETAIL:
        delta_cls = "text-success" if event["status"] == "up" else "text-danger"
        rows.append(
            Div(
                Div(
                    P(event["event"], cls="cm-body-quiet"),
                    cls="d-none d-md-block",
                ),
                Div(
                    Span(event["yesterday"], cls="badge bg-secondary"),
                    cls="d-none d-md-inline",
                ),
                Div(
                    Span(event["today"], cls="badge bg-primary"),
                ),
                Div(
                    Span(event["change"], cls=f"badge {delta_cls}"),
                ),
                cls="d-flex justify-content-between align-items-center p-2 cm-card",
                style="border-left: 4px solid rgba(91, 108, 255, 0.3); margin-bottom: 0.5rem;",
            )
        )

    return Div(
        *rows,
        cls="cm-events-list",
        id="events-table",
    )


def empty_state_example() -> Any:
    """Empty state example."""
    return Div(
        Div(
            Div("📊", cls="cm-empty-icon"),
            P("No events recorded yet", cls="cm-section-head"),
            P(
                "Start sending events from your application to see them appear here.",
                cls="cm-body-quiet",
            ),
            Button(
                "View Documentation",
                cls="btn cm-btn-primary mt-2",
            ),
            cls="cm-empty",
        ),
        cls="cm-card",
    )


def page_header(theme: str = "dark") -> Any:
    """Page header with ThemeToggle."""
    return Div(
        Container(
            Div(
                Div(
                    H1("CloudMetrics", cls="cm-headline"),
                    P(
                        "Real-time analytics and event tracking dashboard",
                        cls="cm-body-quiet mt-2",
                    ),
                    cls="col-12 col-md-8",
                ),
                Div(
                    ThemeToggle(
                        current_theme=theme,
                        endpoint="/theme/toggle",
                        cls="mt-2 mt-md-0",
                    ),
                    cls="col-12 col-md-4 d-flex justify-content-end",
                ),
                cls="row align-items-center",
            ),
            cls="py-3",
        ),
        cls="border-bottom",
        style="border-bottom-color: rgba(91, 108, 255, 0.1)",
    )


# ─────────────────────────────────────────────────────────────────────────────
# MAIN DASHBOARD PAGE (Step 4: Compose from components)
# ─────────────────────────────────────────────────────────────────────────────


def dashboard_page() -> Any:
    """Main dashboard content — stat cards + tabbed event browser."""
    return Container(
        # ── Header section ──────────────────────────────────────
        Div(
            H2("Event Overview", cls="cm-section-head"),
            P(
                "Live metrics and event counts from the last 24 hours",
                cls="cm-body-quiet mb-3",
            ),
        ),
        stat_card_row(),
        # ── Tabs nav (Faststrap Tabs takes tuples) ──────────────
        Tabs(
            ("cm-tab-events", "Events Today", True),
            ("cm-tab-trends", "Trends", False),
            ("cm-tab-settings", "Settings", False),
            cls="cm-tabs mt-4 mb-3",
        ),
        # ── Tab pane content ────────────────────────────────────
        Div(
            TabPane(
                filter_controls(),
                events_table(),
                tab_id="cm-tab-events",
                active=True,
                cls="cm-tab-content",
            ),
            TabPane(
                Div(
                    P(
                        "Trend analysis coming soon. Use HTMX to load chart data.",
                        cls="cm-body-quiet text-center py-4",
                    ),
                ),
                tab_id="cm-tab-trends",
                cls="cm-tab-content",
            ),
            TabPane(
                Div(
                    Alert(
                        "Event tracking preferences would be configured here.",
                        variant="info",
                    ),
                ),
                tab_id="cm-tab-settings",
                cls="cm-tab-content",
            ),
            cls="tab-content",
        ),
        cls="cm-content py-4",
    )


# ─────────────────────────────────────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────────────────────────────────────


@app.post("/theme/toggle")
def toggle_theme(req):
    req.session[THEME_KEY] = "light" if current_theme(req) == "dark" else "dark"
    return hx_refresh()


@app.get("/")
def home(req):
    """Main dashboard page."""
    theme = current_theme(req)
    return (
        Div(
            # Navbar
            Div(
                Div(
                    Div(
                        H4("CloudMetrics", cls="navbar-brand mb-0"),
                        cls="col",
                    ),
                    Div(
                        ThemeToggle(
                            current_theme=theme,
                            endpoint="/theme/toggle",
                            cls="me-2",
                        ),
                        cls="col-auto",
                    ),
                    cls="row align-items-center",
                ),
                cls="cm-navbar",
            ),
            # Page header
            page_header(theme),
            # Dashboard content
            dashboard_page(),
            # Footer
            Div(
                P(
                    "CloudMetrics Analytics • v0.1 Test UI",
                    cls="text-center cm-body-quiet mb-0 py-3",
                ),
                cls="border-top",
                style="border-top-color: rgba(91, 108, 255, 0.1); margin-top: 2rem;",
            ),
            cls="cm-shell",
            data_bs_theme=theme,
        ),
        DASHBOARD_CSS,
        PageMeta(
            title="CloudMetrics Dashboard",
            description="Real-time analytics dashboard built with Faststrap",
        ),
        ToastContainer(),
    )


@app.get("/api/events")
def api_events() -> Any:
    """Mock API endpoint for HTMX to refresh events."""
    return events_table()


# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLING
# ─────────────────────────────────────────────────────────────────────────────


@app.get("/error")
def error_page():
    """Error page example."""
    return ErrorPage(
        404,
        title="Page Not Found",
        message="The page you requested could not be found.",
        cls="cm-shell",
    )


# ─────────────────────────────────────────────────────────────────────────────
# SERVER
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    serve(port=5099)
